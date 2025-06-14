#!/usr/bin/env python3
"""
Script to convert BibTeX files in the 'bib/' directory into Markdown files in the 'papers/' directory.
Each Markdown file contains formatted entries with metadata and URL-encoded keyword badges.
"""

import pathlib
from urllib.parse import quote
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter
import re

def main():
    # Define project root directory as the parent of this script's directory
    project_root = pathlib.Path(__file__).parent.parent.resolve()

    # Define input and output directories
    bib_dir = project_root / "bib"
    papers_dir = project_root / "papers"
    papers_dir.mkdir(exist_ok=True)

    # Iterate over all .bib files in the bib directory
    for bib_file in bib_dir.glob("*.bib"):
        md_file = papers_dir / (bib_file.stem + ".md")

        # Read the BibTeX file with UTF-8 encoding
        with bib_file.open(encoding="utf-8") as f:
            bib_database = bibtexparser.load(f)

        writer = BibTexWriter()

        # Open the markdown file for writing with UTF-8 encoding
        with md_file.open("w", encoding="utf-8") as md:
            # Derive header title by removing numeric prefix
            header_title = re.sub(r'^\d+-', '', bib_file.stem)
            md.write(f"# {header_title}\n\n")

            # Process each BibTeX entry
            for entry in bib_database.entries:
                # Write the title as a level-2 heading
                title = entry.get("title", "No Title")

                # Write metadata: authors, year, and source (journal or booktitle)
                authors = entry.get("author", "Unknown Author")
                # Get the publication year, leave blank if missing
                year = entry.get("year", "")
                # Year badge
                year_badge = ""
                if year:
                    year_badge = f"![year](https://img.shields.io/badge/year-{quote(year)}-blue)"
                source = entry.get("journal") or entry.get("booktitle") or "Unknown Source"

                # Source badge (extract acronym or uppercase letters)
                source_raw = source
                # Shorten arXiv abbreviation if applicable
                if source_raw.lower().startswith("arxiv"):
                    src_abbrev = "arxiv"
                else:
                    m = re.search(r'\(([^)]+)\)', source_raw)
                    if m:
                        src_abbrev = m.group(1)
                    else:
                        src_abbrev = "".join(re.findall(r'\b([A-Z])', source_raw))
                    src_abbrev = src_abbrev or source_raw.replace(" ", "")
                source_badge = f"![src](https://img.shields.io/badge/src-{quote(src_abbrev)}-orange)"
                # Compose link for title
                link_val = entry.get("link", "")
                if link_val.startswith("http"):
                    url = link_val
                elif link_val:
                    url = f"https://doi.org/{link_val}"
                else:
                    url = ""
                # Write list item with badges, year, title as a clickable link, and authors
                md.write(f"- {year_badge} {source_badge} [{title}]({url}) — {authors}\n\n")

if __name__ == "__main__":
    main()
