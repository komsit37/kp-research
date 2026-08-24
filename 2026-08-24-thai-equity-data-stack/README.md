# Thai Equities — Data & Trading API Source Map

**Date:** 2026-08-24

A compact entry point for evaluating the data required to research, backtest and eventually trade Thai equities. It maps official SET/SEC sources, intraday and tick options, Settrade Open API capabilities, the current TISCO constraint, example use cases, and a common sample request for vendor/broker due diligence.

## View

- [Technical architecture: database, connectors, crawler, scheduler and trading boundary](./tech-architecture.html)
- [Current Japanese reference architecture: JPS, Rook, PostgreSQL and Dagu](./jp-reference-architecture.html)
- [Data and vendor source map](./index.html)
- [Public GitHub Pages URL](https://komsit37.github.io/kp-research/2026-08-24-thai-equity-data-stack/)
- [Public technical architecture](https://komsit37.github.io/kp-research/2026-08-24-thai-equity-data-stack/tech-architecture.html)
- [Public Japanese reference architecture](https://komsit37.github.io/kp-research/2026-08-24-thai-equity-data-stack/jp-reference-architecture.html)

## Current working conclusion

- SET/SEC official sources for reference, EOD, corporate actions, filings and point-in-time fundamentals.
- SET SMART Marketplace for authoritative historical intraday tick/book data when required.
- Settrade Open API through a supported broker for live market data and execution.
- TISCO's current Settrade service does not expose the retail Open API; retain it for manual trading or use a second API-enabled broker.

The report is a source-discovery brief, not a vendor recommendation. Product scope, pricing and licensing should be verified directly before implementation.
