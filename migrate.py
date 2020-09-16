import fire
import bibtexparser


def load_bibtex_file(file_path: str):
    """
    Load the contents of the BibTex (.bib) file and parse it using bibtexparser.
    :param file_path: The PATH to the BibTex (.bib) file.
    :return: Parsed BibTex (.bib) file as a Python dictionary.
    """
    with open(file_path, encoding="utf-8") as bibtex_file:
        return bibtexparser.bparser.BibTexParser(common_strings=True, ignore_nonstandard_types=False).parse_file(bibtex_file)


def main(bibtex_path: str):
    """
    Entrypoint for migrate.py
    :params bibtex_path: The PATH to the BibTex (.bib) file on the local machine.
    """
    # Load BibTex file and parse it
    bibtex_db = load_bibtex_file(
        file_path=bibtex_path)
    # Obtain every entry key name
    bibtex_keys = bibtex_db.entries_dict.keys()
    # For all entires in the BibTex file. Remove or replace the "{", "}", "\\textbar" and "\\&amp;" characters in the title field
    for key in bibtex_keys:
        bibtex_entry = bibtex_db.entries_dict[key]
        print(f"Entry before update: {bibtex_entry}")
        # Update title
        print(f"Old title: {bibtex_entry['title']}\nUpdating title.")
        new_title = bibtex_entry["title"].replace("{", "").replace(
            "}", "").replace("\\textbar", "|").replace("\\&amp;", "&")
        bibtex_entry["title"] = new_title
        print(f"New title: {bibtex_entry['title']}")
        try:
            # Make sure booktitle doesn't contain "{", "}" characters
            new_book_title = bibtex_entry["booktitle"].replace("{", "").replace(
                "}", "")
            bibtex_entry["booktitle"] = new_book_title
        except KeyError:
            print(
                f"BibTex entry: {bibtex_entry['title']} isn't a book. Continuing...")
            continue
        # Update the top level dictionary
        bibtex_db.entries_dict[key].update(bibtex_entry)
        print(f"After update: {bibtex_db.entries_dict[key]}")
    # Write out new BibTex file
    with open("bibtex.bib", "w", encoding="utf-8") as bibtex_file:
        bibtexparser.dump(bibtex_db, bibtex_file)


if __name__ == "__main__":
    __version__ = "0.0.1"
    fire.Fire(main)
