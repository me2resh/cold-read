# Tablelight engineering stack by chapter (research, 9 May 2026)

Illustrative: all names, numbers and sources are invented. No LinkedIn profile was opened. Legend: ✅ cited; 🟡 inferred; ❔ unknown.

## The platform in one paragraph

Tablelight sells ordering, kitchen display and payments to about 2,400 UK restaurants, 70% on the ordering product alone. The estate is one Rails monolith on AWS London with a React front end and a React Native app, plus a newer Go payments service behind the Adyen integration. Job ads since January describe a split of the monolith into "ordering" and "kitchen" services and a move of reporting from Postgres read replicas to BigQuery 🟡.

## 1. Ordering chapter

| Component | What it does | Runs on today | Confidence | Heading |
|---|---|---|---|---|
| Menu and order API | Order capture from QR, app and POS | Rails, Postgres, Sidekiq ✅ [three ads] | ✅ | Extraction to a service; two ads name "Go or Kotlin" 🟡 |
| QR web ordering | Guest-facing web | React, Next.js on Vercel ✅ [page headers, ad] | ✅ | Unchanged |
| Mobile app | Staff app, 4.3 on iOS, last update 2 Apr 2026 ✅ [App Store] | React Native ✅ | ✅ | Monthly releases ✅ |

## 5. Platform, infrastructure, DevOps and QA

AWS eu-west-2, ECS on Fargate, Terraform, GitHub Actions, Datadog ✅ [ads, status page]. No SRE role has ever been advertised; the two platform engineers report into the Head of Engineering role being hired 🟡. On-call is "shared across squads" ✅ [ad text].

## 7a. Leadership

- CEO, co-founder, ex-restaurant operator ✅ [team page, press]
- CTO, co-founder, "moving to a product role" per the Head of Engineering ad ✅
- VP Product, joined Oct 2025 from a food-delivery marketplace ✅ [appointment release]
- Head of Engineering: the role; reports to the CEO ✅ [ad]

## 8. What it means for the Head of Engineering mandate

Inherits a monolith split that two ads say has started and none says has finished; a payments service that is the company's revenue bet; a platform team of two with no SRE practice; and a founder CTO moving sideways, which makes the first ninety days about trust with the people who built it. The ad's "double the team" line against 14 open roles means the role is a hiring role first 🟡.

## 10. Questions by round

1. What has shipped from the split so far, and what is the next slice?
2. Who is on call tonight, and what happened the last time payments failed?
3. What does the CTO keep after the move to product?
4. Which of the 14 roles are backfills?

## People (one-line reads)

- **CEO:** will test whether you can talk to restaurant owners, not just engineers 🟡 [two podcast episodes on operator pain]
- **CTO:** will test whether you respect what was built; his 2024 blog post on "boring technology" is the tell ✅
- **VP Product:** will test whether engineering can give dates; her marketplace background is release trains 🟡
