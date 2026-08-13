import json
from pathlib import Path

DATA = Path('data/signals.json')

SEVERITY_WEIGHT = {'critical': 1.0, 'high': 0.8, 'medium': 0.55, 'low': 0.3}


def priority_score(signal):
    severity = SEVERITY_WEIGHT[signal['severity'].lower()]
    return round(100 * (0.45 * severity + 0.35 * signal['impact'] + 0.20 * signal['confidence']), 1)


def prioritize(signals):
    enriched = []
    for signal in signals:
        item = dict(signal)
        item['priority_score'] = priority_score(item)
        enriched.append(item)
    return sorted(enriched, key=lambda x: x['priority_score'], reverse=True)


def daily_brief(signals, limit=5):
    ranked = prioritize(signals)[:limit]
    lines = ['# Daily Marketplace Action Plan', '']
    for i, item in enumerate(ranked, 1):
        lines.append(f"{i}. **{item['severity'].upper()}** — {item['title']} (score {item['priority_score']})")
        lines.append(f"   - Why: {item['reason']}")
        lines.append(f"   - Action: {item['action']}")
    return '\n'.join(lines)


def main():
    signals = json.loads(DATA.read_text(encoding='utf-8'))
    brief = daily_brief(signals)
    print(brief)
    Path('daily_action_plan.md').write_text(brief, encoding='utf-8')

if __name__ == '__main__':
    main()
