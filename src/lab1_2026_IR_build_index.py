import glob
import json
import sys
import os
from collections import defaultdict
import nltk
nltk.download('punkt')
nltk.download('reuters')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

class InvertedIndex:
    
    def __init__(self, file_list):
        # TODO: Initialize data structures for the inverted index
        self.file_list = file_list
        self.inverted_index = defaultdict(set)
        
    def get_inverted_indexes(self):
        # TODO: For each file:
        #   - Assign a unique ID
        #   - Read file contents
        #   - Tokenize the text
        #   - Add each token (lowercased) to the index with the file ID
        for file_id, file_path in enumerate(self.file_list, start=1):
            text = self.get_data(file_path)
            tokens = self.get_tokens(text)
            for token in tokens:
                self.inverted_index[token.lower()].add(file_id)
        return self.inverted_index

    def get_sorted_ids(self):
        # TODO: Convert sets of document IDs to sorted lists
        # TODO: Return the inverted index as a dictionary
        sorted_index = {token: sorted(list(ids)) for token, ids in self.inverted_index.items()}
        return sorted_index

    @staticmethod
    def get_data(path):
        # TODO: Open and read the contents of the file at 'path'
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def get_tokens(text):
        # TODO: Tokenize the text using nltk.word_tokenize
        return word_tokenize(text)

def main():
    # TODO: Get path from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python lab1_2026_IR_build_index.py <directory_path>")
        sys.exit(1)

    # TODO: Get all files in the directory
    directory_path = sys.argv[1]
    file_list = glob.glob(f"{directory_path}/*")
    
    # print("Number of files:", len(file_list))
    # print("First few files:", file_list[:5])
    
    # TODO: Create an InvertedIndex instance
    index = InvertedIndex(file_list)

    # TODO: Build the inverted index
    index.get_inverted_indexes()
    sorted_index = index.get_sorted_ids()

    # TODO: Write the result to a JSON file
    os.makedirs('./index', exist_ok=True)
    output_path = './index/inverted_index.json'

    with open(output_path, "w") as f:
        json.dump(sorted_index, f)


if __name__ == '__main__':
    main()

