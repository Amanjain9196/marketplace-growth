# Marketplace Growth Command Center

**Repository description:** AI-style command center that combines dispatch risk, price breaches, q-commerce availability and ads signals into one prioritized daily action plan.

> Synthetic portfolio project only. No real employer data, credentials, marketplace account IDs, confidential KPIs or commercial terms are included.

## Why this exists
Commerce teams often operate through separate tools for fulfilment, pricing, availability and advertising. Leadership does not need four more dashboards; it needs a clear answer to: **What are the five most important things we should do today?**

## Solution
This project ingests normalized signals from specialist systems and scores them by urgency, business impact and confidence.

```text
RTD risk ─────────────┐
Price breaches ───────┤
Q-commerce OSA ───────┼─> Signal normalizer -> Priority engine -> Daily action plan
Ads opportunities ────┤
Growth anomalies ─────┘
```

## Example output
```text
1. CRITICAL — 12 dispatches are within the SLA risk window.
2. HIGH — SKU-202 is below configured price floor on Marketplace-B.
3. HIGH — Mumbai OSA for SKU-101 is below threshold.
4. MEDIUM — Search demand is rising for a high-converting keyword with limited coverage.
5. MEDIUM — Product-page ad placement has weak conversion efficiency.
```

## Features
- Common schema for heterogeneous business signals
- Urgency × impact × confidence priority score
- Cross-functional daily brief
- Explainable recommended actions
- Synthetic data and extensible adapters

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Portfolio signal
Demonstrates AI-product thinking, systems design and Chief-of-Staff-style prioritization: turning fragmented operating signals into a single executive decision layer.
