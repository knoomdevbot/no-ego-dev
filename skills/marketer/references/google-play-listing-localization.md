# Google Play Listing Localization Playbook

Use this when a mobile app needs a Google Play listing for more than one country or language. The goal is not literal translation; it is country-aware positioning, search language, proof, screenshots, compliance, and conversion.

## Source anchors

- Google Play search/discovery guidance: titles should be unique and accessible; descriptions should focus on what users get; avoid keyword spam, excessive emoji/ASCII, subtle misspellings, and misleading metadata. `https://support.google.com/googleplay/android-developer/answer/4448378`
- Google Play preview assets guidance: short description is limited to 80 characters; screenshots/video/feature graphic should show real app value; videos should communicate core value early; graphic text should be localized where appropriate. `https://support.google.com/googleplay/android-developer/answer/9866151`
- Google Play experiments: test graphics and localized text; localized experiments can test descriptions and creative for selected languages. `https://support.google.com/googleplay/android-developer/answer/6227309`
- Google Play translation/localization: add translated store listing, app strings, and in-app products; users see translated listing when their language preference matches. `https://support.google.com/googleplay/android-developer/answer/9844778`
- Google Play country targeting: release tracks can target specific countries/regions; targeting is based on the user's Play country, not current physical location. `https://support.google.com/googleplay/android-developer/answer/7550024`
- Android localization: structure app resources for localization and test languages/layouts before launch. `https://developer.android.com/guide/topics/resources/localization`
- Apple localization is useful as a cross-store benchmark: localize metadata, keywords, previews, screenshots, app name, and marketing per region. `https://developer.apple.com/localization/`

## Country-by-country workflow

For every country in the launch or rollout list, create one row in `.projects/<project>/marketing/play-store-localization.md` before writing listing copy.

```markdown
| Country / Play country | Listing language(s) | User segment / job | Local pain wording | Top search phrases | Local competitors | Screenshots to localize | Trust/compliance notes | Price/currency notes | Launch channels | Experiment plan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

For each row:

1. **Confirm distribution and language.** Is the app available in that Play country? Which listing languages should appear for that country? Do not assume English works because the product team speaks English.
2. **Research local search language.** Use Google Play autocomplete/search results, competitor listings, reviews, Reddit/forums, YouTube/TikTok, local app charts, and support questions. Capture phrases users actually use, including local abbreviations and loanwords.
3. **Localize the promise, not just words.** Rewrite title, short description, full description, screenshot captions, and feature graphic around the local job-to-be-done and objections.
4. **Localize visuals.** Use local language in overlay text, local currency/date/time formats, plausible names/examples, relevant integrations, and device/status-bar screenshots that match the market. Avoid flags, stereotypes, or stock cultural symbols unless they are genuinely relevant.
5. **Check trust and compliance expectations.** Add privacy, data, subscription, refund, health/finance/legal, age, ads, and permission explanations that fit local expectations and policies.
6. **Match local acquisition channels.** Note where local users discover apps: search, Play browsing, YouTube, TikTok, Instagram, WhatsApp, LINE, KakaoTalk, X, Reddit, local forums, local creators, app review sites, or paid campaigns.
7. **Test before scaling.** Run localized store listing experiments where traffic allows. Test one major hypothesis at a time: first screenshot message, short description, feature graphic, or proof point.
8. **Feed results back into product.** Country-specific objections often reveal missing integrations, permissions confusion, pricing issues, onboarding gaps, or unsupported language inside the app.

## Listing asset rules

- **App name/title:** localized, memorable, easy to spell, avoids generic terms and ranking/price claims. Do not stuff keywords.
- **Short description:** under Google Play's 80-character limit; communicate the core purpose and differentiator in simple local language.
- **Full description:** lead with the local user problem and outcome; use scannable benefit bullets; include trust/privacy/pricing details; avoid repetition and irrelevant keywords.
- **Feature graphic:** one clear value proposition or product moment; localize text overlays; keep readable at small sizes.
- **Screenshots:** first 2–3 screenshots should explain the app without reading the full description. Use real UI, localized captions, and one benefit per frame.
- **Video:** show actual in-app experience early; communicate value in the first seconds; keep short; localize captions/audio or avoid relying on audio.
- **Reviews loop:** monitor reviews by language/country; repeated confusion should create product, onboarding, or listing issues.

## Market-specific starting points

These are starting hypotheses, not stereotypes. Verify with local search results, competitor listings, reviews, and native-speaker review before launch.

### United States
- Use direct benefit-led English; be specific about the user and outcome.
- Screenshots should show speed, simplicity, privacy/security proof where relevant, and obvious CTA.
- Avoid unsupported superlatives like “#1,” “best,” or “guaranteed.”

### United Kingdom, Ireland, Australia, New Zealand, Canada English
- Do not blindly reuse US copy when spelling, regulatory terms, currency, or benefits differ.
- Localize pricing, date/time examples, screenshots, support references, and integrations.
- Canada may need both English and French-Canadian coverage depending on audience and category.

### Canada French / France / Belgium / Switzerland French
- Use native French copy rather than word-for-word English structure.
- Prefer clear usefulness and trust over aggressive hype.
- Review privacy/subscription wording carefully; localize screenshots and support examples.

### Germany / Austria / Switzerland German
- Lead with clarity, reliability, privacy, control, and concrete features.
- Avoid vague hype and unsupported claims; explain permissions and data use plainly.
- Localize compound terms naturally; use native reviewer for title/short description.

### Spain / Latin American Spanish
- Decide between Spain Spanish and Latin American Spanish; do not use one if it sounds unnatural for the target country.
- Localize currency, examples, support hours, and idioms.
- For LATAM, consider country-specific payment/pricing trust signals and WhatsApp/social support expectations.

### Mexico
- Spanish copy should be natural Mexican Spanish when Mexico is a major target.
- Highlight practical everyday use, pricing clarity, and support/contact channels.
- Screenshots should avoid Spain-specific idioms and irrelevant currencies/examples.

### Brazil
- Use Brazilian Portuguese, not European Portuguese.
- Localize payment, pricing, date formats, informal/formal tone, and support expectations.
- WhatsApp/Instagram/YouTube may matter for launch support and proof depending on category.

### Portugal
- Use European Portuguese if Portugal is separately targeted.
- Do not reuse Brazilian Portuguese without review.

### Japan
- Invest in native copy review. Japanese ASO often needs natural, concise benefit phrasing rather than translated English slogans.
- Screenshot captions can carry important context; localize examples, UI text, and proof carefully.
- Trust, polish, support, and category fit matter; avoid overly casual tone unless the category expects it.

### South Korea
- Use native Korean and review spacing/terminology carefully.
- Emphasize speed, polish, social proof, platform integrations, and clear subscription/privacy explanations where relevant.
- Kakao/Naver/YouTube/community context may matter outside the Play listing.

### Mainland China / Hong Kong / Taiwan Chinese
- Google Play distribution is not the default Android app-store path in mainland China. Treat mainland China as a separate distribution/compliance strategy, not just a Play listing localization.
- Use Simplified Chinese for mainland China, Traditional Chinese for Taiwan/Hong Kong, and localize terminology separately.
- Review local compliance, content, payments, privacy, and support channels before promising availability.

### India
- English may work for many categories, but Hindi and regional-language listings can matter for broad consumer apps.
- Localize price sensitivity, low-bandwidth/offline value, permissions, phone-number/OTP flows, and support expectations.
- Screenshots should be lightweight, practical, and trust-building.

### Indonesia / Malaysia
- Use Indonesian for Indonesia and Malay for Malaysia where relevant; do not treat them as interchangeable.
- Localize payments, social channels, examples, and support expectations.
- Clarity and lightweight onboarding often matter for broad consumer apps.

### Thailand / Vietnam / Philippines
- Use native-language listing for broad consumer apps; English may work for developer/professional niches but should be verified.
- Localize screenshot text, support channels, and pricing.
- Check local social/video channels for acquisition-message fit.

### MENA / Arabic markets
- Arabic requires right-to-left review for screenshots, UI, and copy.
- Distinguish Gulf, Egypt, Levant, and North African language/register differences when targeting a specific country.
- Review cultural, religious, finance, health, dating, and content sensitivities before launch.

### Turkey
- Use native Turkish copy; localize pricing and payment expectations.
- Avoid literal English word order; lead with concrete benefit and trust.

### Nordics / Netherlands
- English may be acceptable for some professional/developer tools, but native listings can improve trust for consumer apps.
- Use a native review for idiom, tone, and screenshots when the country is a major target.

### Italy
- Use native Italian for consumer apps; keep claims clear and benefit-led.
- Localize pricing, examples, and customer support details.

### Poland / Central and Eastern Europe
- Use native copy for consumer apps; English may work for developer tools but verify.
- Localize pricing, privacy, support, and competitor terminology.

## Quality gate before publishing a localized Play listing

- [ ] Country is included in Play country availability or a test track plan.
- [ ] Listing language matches the target country and user segment.
- [ ] Title and short description are native, concise, accessible, and not keyword-stuffed.
- [ ] First screenshots communicate the local core value without relying on the full description.
- [ ] Full description explains local pain, benefits, trust/privacy, pricing, and support.
- [ ] Feature graphic/video/screenshot text is localized where appropriate.
- [ ] Currency, dates, numbers, names, examples, integrations, and legal/privacy wording fit the country.
- [ ] Native speaker or high-quality reviewer checked the title, short description, screenshots, and first paragraph.
- [ ] Store listing experiment or measurement plan exists for meaningful traffic countries.
- [ ] Repeated country-specific review/support feedback will be converted into issues.
