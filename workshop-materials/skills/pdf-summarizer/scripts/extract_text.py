#!/usr/bin/env python3
"""Extract plain text from a PDF file and print it to stdout.

Usage:
    python3 extract_text.py <path-to-pdf>

Requires `pypdf` (pip install pypdf).
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: extract_text.py <path-to-pdf>", file=sys.stderr)
        return 2

    pdf_path = Path(sys.argv[1])
    if not pdf_path.is_file():
        print(f"error: file not found: {pdf_path}", file=sys.stderr)
        return 1

    try:
        from pypdf import PdfReader
    except ImportError:
        print(
            "error: pypdf not installed. Run: pip install pypdf",
            file=sys.stderr,
        )
        return 1

    reader = PdfReader(str(pdf_path))
    for i, page in enumerate(reader.pages, start=1):
        print(f"--- page {i} ---")
        print(page.extract_text() or "")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
