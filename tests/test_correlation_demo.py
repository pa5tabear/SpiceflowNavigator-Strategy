import glob
from analytics.correlation import run_correlation_demo


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return [open(f, 'r', encoding='utf-8').read() for f in files]


def test_correlation_demo():
    transcripts = _load_transcripts()[:2]
    output = run_correlation_demo(transcripts)
    assert 'network' in output
    assert 'correlations' in output
    assert output['network']['edges']
    assert output['correlations']['correlations']
