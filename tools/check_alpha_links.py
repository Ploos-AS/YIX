# SPDX-License-Identifier: MIT
"""Check local documentation and website links without network access."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/Ploos-AS/YIX/blob/main/"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(v for k, v in attrs if k in ("href", "src") and v)

def check(source, link):
    if link.startswith(REPO):
        target = ROOT / unquote(urlsplit(link[len(REPO):]).path)
    else:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return True
        target = source.parent / unquote(parsed.path)
    if target.is_dir():
        return (target / "index.html").is_file() if source.suffix == ".html" else True
    return target.is_file()

def main():
    failures = []
    sources = [ROOT / "README.md", *ROOT.glob("website/**/*.html")]
    for source in sources:
        data = source.read_text(encoding="utf-8")
        if source.suffix == ".html":
            parser = Links()
            parser.feed(data)
            links = parser.links
        else:
            links = re.findall(r"\]\(([^)]+)\)", data)
        for link in links:
            if not check(source, link):
                failures.append(f"{source.relative_to(ROOT)}: {link}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("README and website local link targets exist")
    return 0

if __name__ == "__main__":
    sys.exit(main())
