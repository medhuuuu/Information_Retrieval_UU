import os
from nltk.corpus import reuters
# nltk.download('reuters')  # TODO: Uncomment if needed

def main():
    os.makedirs('../reuters', exist_ok=True)  # This creates a directory unless you already have one.
    # Make sure the path is correct (i.e., is in accordance with the structure of directories and files under Section 8 
    #in the lab instructions

    # TODO: Get the list of Reuters file IDs
    file_list = reuters.fileids()
    
    # TODO: For each file ID:
    #   - Get the raw text
    #   - Create a filename based on the file ID
    #   - Write the text to a .txt file in './reuters'
    #   - Optionally: print the filename
    for file_id in file_list:
        raw_text = reuters.raw(file_id)
        filename =  file_id.replace('/', '_') + ".txt" # Replace '/' with '_' to create a valid filename
        with open(f'./reuters/{filename}', 'w', encoding='utf-8') as f:
            f.write(raw_text)
        print(f'Created file: {filename}')
    pass

if __name__ == '__main__':
    main()

