# Sources Index — Saudi Real Estate AI

This directory documents all official sources used in the `saudi-real-estate-ai` repository. Every data reference, regulatory citation, and platform specification in this project must trace back to a source listed here. If a source is not listed, it must be added before being cited in any file.

---

## Official Sources Table

| Source | Authority | URL | Coverage | Last Verified |
|---|---|---|---|---|
| REGA — الهيئة العامة للعقار | Government Regulatory Body | https://rega.gov.sa | Real estate licensing, brokerage law, development law, rental law, market reports | 2026-05-01 |
| ejar — منصة إيجار | REGA (operated) | https://ejar.sa | Rental contract registration, lease templates, dispute resolution, tenant/landlord obligations | 2026-05-01 |
| wafi — منصة وافي | REGA (operated) | https://wafi.rega.gov.sa | Off-plan sales regulation, developer licensing, escrow accounts, project registration | 2026-05-01 |
| sakani — برنامج سكني | Ministry of Municipalities and Housing | https://sakani.com.sa | Government housing program, subsidized units, land grants, REDF financing, homeownership targets | 2026-05-01 |
| MOH — وزارة الإسكان | Ministry of Municipalities and Housing | https://www.momah.gov.sa | Housing policy, urban planning, social housing programs, Vision 2030 housing targets | 2026-04-15 |
| REDF — صندوق التنمية العقارية | Real Estate Development Fund | https://redf.gov.sa | Saudi citizen mortgage support, subsidized financing, Sakani program financing arm | 2026-04-15 |
| SAMA — مؤسسة النقد العربي السعودي | Saudi Central Bank | https://www.sama.gov.sa | Mortgage regulations, real estate financing rules, licensed lenders, LTV limits, consumer protection | 2026-04-20 |
| CMA — هيئة السوق المالية | Capital Market Authority | https://cma.org.sa | REIT regulations, real estate investment funds, Tadawul-listed REITs, disclosure requirements | 2026-04-20 |
| نظام التسجيل العيني للعقار | Ministry of Justice | https://www.moj.gov.sa | Real property registration law, title deed system, ownership transfer, mortgage registration | 2026-04-10 |

---

## How to Add a Source

Before adding a new source to this index, it must meet all of the following criteria:

1. **Must be official.** The source must originate from a Saudi government body, a licensed regulatory platform, or an internationally recognized institution. Personal blogs, news articles, and non-verified aggregators are not eligible as primary sources.

2. **Must have a stable URL.** The URL must point directly to the official website or official publication page. Link-rot is a known risk — if a URL changes, update this file immediately.

3. **Must be bilingual if possible.** Given the dual Arabic/English nature of this repository, sources that publish in both Arabic and English are strongly preferred. If a source is Arabic-only, note this in the Coverage column and provide an English summary in the source's dedicated `.md` file.

4. **Must have a "Last Verified" date.** Regulations and platform features change. Every entry must include the date it was last verified to be accurate. If more than 6 months have passed since the last verification date, the source should be re-checked before being cited.

5. **Must have a dedicated source file.** Each source in this index should have a corresponding `sources/<slug>.md` file documenting it in detail (see existing files as templates).

To add a source, open a pull request that:
- Adds a row to the table above
- Adds a dedicated `sources/<slug>.md` file
- Updates any relevant prompts or schemas that reference the source

---

## Source Quality Tiers

### Tier 1 — Government and Regulatory Bodies

The highest-authority sources. These are Saudi government ministries, independent regulatory agencies established by royal decree, and official inter-governmental bodies. Citations from Tier 1 sources carry full legal and regulatory weight.

Examples: REGA, Ministry of Municipalities and Housing, SAMA, CMA, Ministry of Justice, REDF.

### Tier 2 — Licensed Platforms

Official digital platforms operated by or under the direct mandate of Tier 1 authorities. These platforms have legal standing and their data (contracts, licenses, registrations) is legally recognized in Saudi courts and regulatory proceedings.

Examples: ejar (منصة إيجار), wafi (منصة وافي), sakani (برنامج سكني), nafitha (منصة نافذة), REDS (نظام التسجيل العقاري).

### Tier 3 — Academic and Research

Peer-reviewed research, official reports from recognized international organizations (World Bank, IMF, UN-Habitat), and Saudi academic institutions. Tier 3 sources are acceptable for contextual and analytical references but must not be used as primary citations for regulatory requirements.

Examples: Saudi Vision 2030 research publications, KFUPM real estate studies, IMF Article IV consultation reports.

---

> **DISCLAIMER:** This repository is an open-source educational and research tool. The sources listed here are provided for reference purposes only. Regulations, platform features, fees, and legal requirements change frequently. Nothing in this repository constitutes legal, financial, or investment advice. Always verify information directly with the relevant official authority before making any legal or financial decision. The maintainers of this repository are not responsible for decisions made based on outdated or misunderstood source material.
