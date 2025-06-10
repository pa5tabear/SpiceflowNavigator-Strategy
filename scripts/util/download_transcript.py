import argparse
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup


def download_and_clean(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines()]
    text = '\n'.join(line for line in lines if line)
    return text


def main():
    parser = argparse.ArgumentParser(description='Download and clean transcript')
    parser.add_argument('--url', required=True)
    parser.add_argument('--outfile', required=True)
    args = parser.parse_args()
    text = download_and_clean(args.url)
    out_path = Path(args.outfile)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()
