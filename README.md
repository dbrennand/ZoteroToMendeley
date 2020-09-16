# ZoteroToMendeleyFixes

Fix an issue with BibTex Zotero export to Mendeley Desktop

## Use Case

This scripts attempts to fix two similar issues with the BibTex Zotero export:

1. Titles of BibTex entries containing the characters: `{, }, \textbar, \&amp;`.

2. Booktitles also containing the same characters as above.

## Dependencies

```pipfile
[packages]
bibtexparser = "*"
fire = "*"

[requires]
python_version = "3.8"
```

## Usage

`python migrate.py /path/to/Zotero/Export/MyLibrary.bib`
