{
  "tool": "sec_filing_decoder",
  "tier": "T3",
  "price_usd": 0.15,
  "execRole": "cfo",
  "_comment": "Example input/output pair. Real output varies based on live EDGAR data.",
  "input": {
    "ticker": "SHOP",
    "filing_types": ["10-K"],
    "lookback_months": 18,
    "focus": "all"
  },
  "output_excerpt": {
    "summary": "Shopify reported strong revenue growth (+30%) but red flags emerge on MRR deceleration and operating leverage. M&A signals indicate Logistics divestiture in progress.",
    "company": {
      "name": "Shopify Inc.",
      "cik": "0001594805",
      "ticker": "SHOP",
      "sic_industry": "7372 — Prepackaged Software"
    },
    "filings_analyzed": [
      {
        "type": "10-K",
        "filed_date": "2026-02-11",
        "accession_no": "0001594805-26-000023",
        "url": "https://www.sec.gov/Archives/edgar/data/1594805/000159480526000023/"
      }
    ],
    "kpis_movement": [
      {
        "metric": "Revenue (full year)",
        "change_pct": 30.3,
        "direction": "up"
      },
      {
        "metric": "GMV",
        "change_pct": 29.5,
        "direction": "up"
      }
    ],
    "red_flags": [
      {
        "id": "RF-1",
        "category": "guidance-cut",
        "severity": "high",
        "evidence_filing": "10-K 2026-02-11",
        "evidence_quote": "MRR growth decelerated to 21% in Q4 from 27% in Q3...",
        "recommendation": "Monitor Q1 2027 MRR growth ; below 18% would signal saturation"
      }
    ],
    "ma_signals": [
      {
        "signal_type": "divestiture",
        "confidence": "high",
        "evidence_quote": "...completed the divestiture of our Logistics business..."
      }
    ],
    "sentiment_overall": "bullish",
    "recommended_next_actions": [
      "Compare MRR trajectory with Toast, Wix, BigCommerce competitors",
      "Track quarterly 10-Q Logistics impact going forward",
      "Watch for $50M+ acquisition announcements (8-K) signaling new strategic direction"
    ]
  }
}
