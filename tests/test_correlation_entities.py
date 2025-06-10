import glob
from analytics.entity import track_entities
from analytics.correlation import build_advanced_network


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return [open(f, 'r', encoding='utf-8').read() for f in files]


def test_correlation_entities():
    transcripts = _load_transcripts()
    tracking = track_entities(transcripts)
    network = build_advanced_network(tracking)
    assert network.edges
    assert 0.0 <= network.density <= 1.0
    assert network.clusters
    assert all(0.0 <= w <= 1.0 for _, _, w in network.edges)
