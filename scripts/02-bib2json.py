#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bib2json.py

Convert all BibTeX entries under the 'bib/' directory into a single JSON file 'index.json'.
Each entry in the JSON includes:
  - id:      BibTeX key
  - title:   Paper title
  - authors: Author list string
  - year:    Publication year
  - source:  Conference or journal name
  - url:     Link or DOI
  - category: Derived from the BibTeX file name (stripping numeric prefix)
  - keywords: list of keywords taken from the BibTeX ‘keywords’ field (empty list if absent)

Usage:
    python scripts/bib2json.py
"""
import re
import json
import pathlib
import bibtexparser

def derive_category(bib_file: pathlib.Path) -> str:
    """
    Derive a category name from the BibTeX file stem by removing leading digits and hyphens.
    Example: '01-survey.bib' -> 'survey'
    """
    stem = bib_file.stem
    # Remove leading numeric prefix and hyphens
    return re.sub(r'^\d+-', '', stem)

def load_entries_from_bib(bib_path: pathlib.Path) -> list:
    """
    Parse the given .bib file and return a list of entry dictionaries.
    """
    with open(bib_path, encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)
    return bib_database.entries, bib_path.read_text(encoding='utf-8')

def main():
    # Project root is one level up from this script directory
    project_root = pathlib.Path(__file__).resolve().parent.parent
    bib_dir = project_root / 'bib'
    output_json = project_root / 'scripts' / 'index.json'

    all_entries = []

    # Iterate over all .bib files sorted by name
    for bib_path in sorted(bib_dir.glob('*.bib')):
        category = derive_category(bib_path)
        entries, raw_bib = load_entries_from_bib(bib_path)
        for entry in entries:
            # Parse keywords into a clean list; accept comma or semicolon separators
            keywords_raw = entry.get('keywords', '')
            keywords = [kw.strip() for kw in re.split(r'[;,]', keywords_raw) if kw.strip()]
            record = {
                'id': entry.get('ID', ''),
                'title': entry.get('title', ''),
                'authors': entry.get('author', ''),
                'year': entry.get('year', ''),
                'source': entry.get('booktitle', entry.get('journal', '')),
                'category': category,
                'keywords': keywords,
                'bibtex': (
                    lambda db: (setattr(db, 'entries', [entry]) or bibtexparser.dumps(db))
                )(bibtexparser.bibdatabase.BibDatabase())
            }
            all_entries.append(record)

    # Write out the combined JSON file
    with open(output_json, 'w', encoding='utf-8') as json_file:
        json.dump(all_entries, json_file, ensure_ascii=False, indent=2)

    print(f"Generated {output_json} with {len(all_entries)} entries.")

if __name__ == "__main__":
    main()
