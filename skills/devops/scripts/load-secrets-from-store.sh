#!/usr/bin/env bash
# Load local environment variables from a secret-store mapping file.
#
# Usage (must be sourced to affect the current shell):
#   source scripts/load-secrets-from-store.sh .env.secretstore
#
# Mapping file format:
#   ENV_VAR=op://Vault/Item/Field
#   OTHER_VAR=keychain://service/account
#
# Supported stores:
#   - 1Password CLI references: op://Vault/Item/Field
#   - macOS Keychain fallback: keychain://<service>/<account>

set -euo pipefail

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
  echo "ERROR: source this script instead of executing it: source $0 [.env.secretstore]" >&2
  exit 64
fi

mapping_file="${1:-.env.secretstore}"

if [[ ! -f "$mapping_file" ]]; then
  echo "ERROR: secret mapping file not found: $mapping_file" >&2
  return 66 2>/dev/null || exit 66
fi

require_command() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "ERROR: required command not found: $cmd" >&2
    return 69
  fi
}

load_secret_ref() {
  local ref="$1"

  case "$ref" in
    op://*)
      require_command op || return $?
      op read "$ref"
      ;;
    keychain://*)
      require_command security || return $?
      local rest="${ref#keychain://}"
      local service="${rest%%/*}"
      local account="${rest#*/}"
      if [[ -z "$service" || -z "$account" || "$service" == "$account" ]]; then
        echo "ERROR: invalid keychain reference: $ref (expected keychain://<service>/<account>)" >&2
        return 65
      fi
      security find-generic-password -s "$service" -a "$account" -w
      ;;
    *)
      echo "ERROR: unsupported secret reference for value '$ref'" >&2
      echo "Supported references: op://Vault/Item/Field, keychain://service/account" >&2
      return 65
      ;;
  esac
}

loaded_count=0
line_number=0

while IFS= read -r raw_line || [[ -n "$raw_line" ]]; do
  line_number=$((line_number + 1))

  # Trim leading/trailing whitespace for control checks, while preserving values after '='.
  line="${raw_line#${raw_line%%[![:space:]]*}}"
  line="${line%${line##*[![:space:]]}}"

  [[ -z "$line" || "${line:0:1}" == "#" ]] && continue

  if [[ ! "$line" =~ ^[A-Za-z_][A-Za-z0-9_]*=.+$ ]]; then
    echo "ERROR: malformed mapping at $mapping_file:$line_number" >&2
    echo "Expected ENV_VAR=secret-store-reference" >&2
    return 65 2>/dev/null || exit 65
  fi

  name="${line%%=*}"
  ref="${line#*=}"

  # Basic guardrail: mapping files should contain references, not raw secrets.
  if [[ "$ref" != op://* && "$ref" != keychain://* ]]; then
    echo "ERROR: $name at $mapping_file:$line_number is not a supported secret-store reference" >&2
    return 65 2>/dev/null || exit 65
  fi

  value="$(load_secret_ref "$ref")" || return $?
  export "$name=$value"
  loaded_count=$((loaded_count + 1))
done < "$mapping_file"

echo "Loaded $loaded_count secret-backed environment variable(s) from $mapping_file." >&2
