# Thai Equities — Data & Trading API Source Map

**Date:** 2026-08-24

A compact entry point for evaluating the data required to research, backtest and eventually trade Thai equities. It maps official SET/SEC sources, intraday and tick options, Settrade Open API capabilities, the current TISCO constraint, example use cases, and a common sample request for vendor/broker due diligence.

## View

- [Open the HTML report](./index.html)
- [Public GitHub Pages URL](https://komsit37.github.io/kp-research/2026-08-24-thai-equity-data-stack/)

## Current working conclusion

- SET/SEC official sources for reference, EOD, corporate actions, filings and point-in-time fundamentals.
- SET SMART Marketplace for authoritative historical intraday tick/book data when required.
- Settrade Open API through a supported broker for live market data and execution.
- TISCO's current Settrade service does not expose the retail Open API; retain it for manual trading or use a second API-enabled broker.

The report is a source-discovery brief, not a vendor recommendation. Product scope, pricing and licensing should be verified directly before implementation.
