# Word Pair Finder

This project is a Python-based tool that finds pairs of words from a given set of characters. It's designed to solve word puzzles or games where you need to create two words using all the provided letters.

## Features

- Accepts four 3-character strings as input
- Constructs a Trie data structure from a dictionary of words
- Generates valid words from the input strings
- Finds pairs of words that use all the input characters
- Efficient search using depth-first search (DFS) algorithm

## Requirements

- Python 3.x
- `words_alpha.txt` file (a list of valid English words)
- poetry (for dependency management)

## Usage

Run the script from the command line with four 3-character strings as arguments:

```
poetry run python main.py <string1> <string2> <string3> <string4>
```

Example:

```
poetry run python main.py szq udn vei aho
```

## Running Tests

```
poetry run pytest tests/test_main.py
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
