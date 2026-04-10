import json
import sys

def load_index(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def search_term(index, term):
    return index.get(term.lower(), [])


def main():
    # TODO: Check that a file path was given as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python lab1_2026_IR_search_inverted_index.py <path_to_inverted_index.json>")
        sys.exit(1)
    # TODO: Load the inverted index using the given path
    index = load_index(sys.argv[1])

    while True:
        # TODO: Prompt the user for a search term
        term = input("Enter a search term (or 'exit' to quit): ")
        # TODO: Break the loop if the user types 'exit'
        if term == 'exit':
            break
        # TODO: Search for the term in the index
        doc_ids = search_term(index, term)
        # TODO: Print which documents (if any) contain the term
        if doc_ids:
            print(f"Documents containing '{term}': {doc_ids}")
        else:
            print(f"No documents contain '{term}'")

        # (optional) TODO: Add support for searching multiple words in the same query (e.g., apple banana should return documents containing both words).
        # TODO: Extend your search program with Boolean operators like AND, OR, and NOT.
        # TODO: Show actual filenames (instead of document IDs) in the search results.
        # TODO: Count how many documents each word appears in (document frequency), and use this to rank results (hint: look up TF or TF-IDF).
        # TODO: Add functionality that prints the top 10 most frequent terms in the entire index.
        # TODO: Visualize word frequencies using matplotlib or seaborn.
        # TODO: Implement wildcard search (e.g., comput* should match computer, computing, etc.).
        # TODO: Try building the inverted index using a different tokenization strategy (e.g., regex, or filtering out stop words).
        if ' ' in term:
            terms = term.split()
            doc_ids = set(search_term(index, terms[0]))
            for t in terms[1:]:
                doc_ids.intersection_update(search_term(index, t))
            if doc_ids:
                print(f"Documents containing all terms '{term}': {sorted(doc_ids)}")
            else:
                print(f"No documents contain all terms '{term}'")  
                   


if __name__ == '__main__':
    main()

