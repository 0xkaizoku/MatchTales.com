# Comparison Page Schema Templates

Structured data allows AI engines and traditional crawlers to parse tool capabilities,
ratings, and pricing without ambiguity.

## 1. ItemList Schema for "Best Tools" Roundup
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Best SEO Tools in 2026",
  "description": "Ranked and reviewed SEO platforms evaluated on index size and price.",
  "numberOfItems": 3,
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "SoftwareApplication",
        "name": "Tool A",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "offers": {
          "@type": "Offer",
          "price": "99.00",
          "priceCurrency": "USD"
        },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.8",
          "reviewCount": "120"
        }
      }
    }
  ]
}
```

## 2. Head-to-Head Comparison FAQPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Tool A cheaper than Tool B?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Tool A starts at $49 per month for up to 5 users, whereas Tool B starts at $99 per month with a 3-user maximum on the starter tier."
      }
    },
    {
      "@type": "Question",
      "name": "Which tool is better for enterprise teams?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tool B is better for enterprise teams due to dedicated SAML/SSO integration, custom API rate limits, and 24/7 dedicated phone support."
      }
    }
  ]
}
```
