import glob
from analytics.entity import track_entities, build_timeline


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return [open(f, 'r', encoding='utf-8').read() for f in files]


def test_entity_timeline():
    transcripts = _load_transcripts()
    tracking = track_entities(transcripts)
    timeline = build_timeline(tracking)
    assert 'Donald Trump' in timeline.timeline
    # timeline indices should be ascending tuples
    assert all(isinstance(t[0], int) for t in timeline.timeline['Donald Trump'])
