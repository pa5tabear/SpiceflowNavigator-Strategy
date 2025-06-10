import glob
from analytics.entity import track_entities


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return [open(f, 'r', encoding='utf-8').read() for f in files]


def test_entity_tracking():
    transcripts = _load_transcripts()
    result = track_entities(transcripts)
    assert 'Donald Trump' in result.frequency
    assert result.frequency['Donald Trump'] > 0
    assert result.prominence['Donald Trump'] <= 1.0
    assert all(m.source for m in result.mentions['Donald Trump'])
