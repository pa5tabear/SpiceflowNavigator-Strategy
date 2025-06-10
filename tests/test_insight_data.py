import os
import glob


def test_transcripts_complete():
    files = glob.glob('data/raw_podcasts/*.txt')
    assert len(files) == 5
    for path in files:
        size = os.path.getsize(path)
        assert size > 10000, f"{path} too small"

    text = open('data/raw_podcasts/cleaning_up_global_south.txt', encoding='utf-8').read()
    assert 'Transcript unavailable' not in text
