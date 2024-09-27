import argparse
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def __str__(self):
        return f"TrieNode(children={self.children}, is_end_of_word={self.is_end_of_word})"

def construct_trie(word_list):
    '''
    Construct the Trie.
    word_list: list of words that are used to construct the Trie.
    Return the root of the Trie.
    '''
    root = TrieNode()
    for word in word_list:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def search_word(trie, word):
    '''
    Search for a word in the Trie.
    trie: the Trie that is used to search for the word.
    word: the word that is being searched for.
    Return True if the word is found, False otherwise.
    '''
    node = trie
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word


def dfs(trie, words, current_word, str_list, current_index):
    """
    Recursively search for valid words in the Trie.
    words: list of words that are generated from the Trie.
    current_word: the current word being formed.
    str_list: list of strings that are used to form the current word.
    current_index: the index of the current string that is being used to form the current word.
    """
    # If we found a valid word, add it to the list of words.
    if trie.is_end_of_word and len(current_word) >= 4:
        words.append(current_word)
    
    # If we are at a leaf node, return.
    if not trie.children:  # Leaf node
        return
    
    # If we are not at a leaf node, continue searching.
    for i, str in enumerate(str_list):
        if i != current_index:
            # Continue the search with each of these characters
            for char in str:
                if char in trie.children:
                    dfs(trie.children[char], words, current_word + char, str_list, i)
    
        

def read_words_file(filename='words_alpha.txt'):
    '''
    Read the words from the words_alpha.txt file.
    Return a list of words.
    '''
    try:
        with open(filename, 'r') as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except IOError:
        print(f"Error: Unable to read file '{filename}'.")
        return []

def generate_words(strings, trie):
    '''
    Generate words from the Trie.
    strings: list of strings that are used to form the current word.
    trie: the Trie that is used to search for valid words.
    Return a list of valid words.
    '''
    valid_words = []
    for i in range(len(strings)):
        for c in strings[i]:
            if c in trie.children:
                dfs(trie.children[c], valid_words, c, strings, i)
    return valid_words

def find_optional_solutions(words, all_chars):
    '''
    Find optional solutions from the list of words.
    words: list of words that are generated from the Trie.
    all_chars: list of characters that are used to form the words.
    Return a list of optional solutions.
    '''
    sorted_words = sorted(words, key=len, reverse=True)
    word_pairs = []
    optional_solutions = []
    for i in range(len(sorted_words)):
        for j in range(len(sorted_words)):
            if i != j and sorted_words[i][-1] == sorted_words[j][0]:
                if len(sorted_words[i]) + len(sorted_words[j]) >= len(all_chars):
                    word_pairs.append((sorted_words[i], sorted_words[j]))
    print(word_pairs)
    # Filter pairs to ensure they use all characters
    for pair in word_pairs:
        combined_chars = set(pair[0] + pair[1])
        if combined_chars == set(all_chars):
            optional_solutions.append(pair)
    return optional_solutions



def validate_input(arg):
    '''
    Validate the input.
    arg: the input that is being validated.
    Return the input if it is valid.
    '''
    if len(arg) != 3:
        raise argparse.ArgumentTypeError(f"'{arg}' is not a valid 3-character string.")
    return arg

def main():
    parser = argparse.ArgumentParser(description="Accept 4 strings of three characters each.")
    parser.add_argument('strings', type=validate_input, nargs=4, 
                        help="Four 3-character strings")

    try:
        args = parser.parse_args()
    except argparse.ArgumentTypeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print("The four strings are:")
    for string in args.strings:
        print(string)

    words = read_words_file()
    print(f"Total words in the file: {len(words)}")

    trie = construct_trie(words)

    valid_words = generate_words(args.strings, trie)
    all_chars = [char for string in args.strings for char in string]
    print(f"All characters: {all_chars}")
    optional_solutions = find_optional_solutions(valid_words, all_chars)
    
    print("Optional solutions:")
    for word in optional_solutions:
        print(word)

if __name__ == "__main__":
    main()

