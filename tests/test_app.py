from app import priority_score, prioritize


def test_critical_signal_ranks_above_low_signal():
    signals = [
        {'severity':'low','impact':0.3,'confidence':0.8},
        {'severity':'critical','impact':0.9,'confidence':0.9},
    ]
    ranked = prioritize(signals)
    assert ranked[0]['severity'] == 'critical'
    assert ranked[0]['priority_score'] > ranked[1]['priority_score']


def test_score_is_bounded():
    signal = {'severity':'high','impact':0.8,'confidence':0.9}
    assert 0 <= priority_score(signal) <= 100
