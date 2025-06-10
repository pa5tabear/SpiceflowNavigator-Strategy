import glob
from analytics.entity import track_entities, detect_relationships


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return [open(f, 'r', encoding='utf-8').read() for f in files]


def test_entity_relationships():
    transcripts = _load_transcripts()
    tracking = track_entities(transcripts)
    network = detect_relationships(tracking)
    assert any(
        a == 'Microsoft' and b == 'Data Center' or a == 'Data Center' and b == 'Microsoft'
        for a, b, _ in network.edges
    )
