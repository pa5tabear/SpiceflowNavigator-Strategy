import glob
from analytics.correlation import cross_source_correlation


def _load_transcripts():
    files = sorted(glob.glob('data/raw_podcasts/*.txt'))
    return {f.split('/')[-1].replace('.txt', ''): open(f, 'r', encoding='utf-8').read() for f in files}


def test_correlation_analysis():
    sources = _load_transcripts()
    # limit to first three for test speed
    subset = dict(list(sources.items())[:3])
    result = cross_source_correlation(subset)
    assert result.correlations
    for corr in result.correlations:
        assert 0.0 <= corr.score <= 1.0
    assert any(c.score > 0 for c in result.correlations)
