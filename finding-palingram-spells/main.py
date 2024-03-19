from collections import defaultdict
from pathlib import Path
from typing import cast


def load_words(filepath: Path) -> list[str]:
    """Load words from a file and return them as a list of strings."""
    with open(filepath, 'r') as file:
        return file.read().splitlines()


def find_anagrams(words: list[str]) -> list[list[str]]:
    """Find anagrams in a list of words and return them as a list of lists."""
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return [words for words in anagrams.values() if len(words) > 1]


def find_palindromes(words: list[str]) -> list[str]:
    """Find palindromes in a list of words and return them as a list."""
    return [word for word in words if word == word[::-1]]


def find_palingrams(words: list[str]) -> list[tuple[str, str]]:
    """Find palingrams in a list of words and return them as a list."""
    palingrams = []
    words = cast(set, set(words))
    for word in words:
        w_length = len(word)
        reversed_w = word[::-1]
        if w_length <= 1:
            continue

        for i in range(w_length):
            if word[i:] == reversed_w[:w_length - 1] and reversed_w[w_length - 1:] in words:
                palingrams.append((word, reversed_w[w_length - 1:]))
            if word[:i] == reversed_w[w_length - 1:] and reversed_w[:w_length - 1] in words:
                palingrams.append((reversed_w[:w_length - 1], word))

    return palingrams


if __name__ == '__main__':
    words = load_words(Path('words.txt'))

    anagrams = find_anagrams(words)
    print(f"Number of anagrams found: {len(anagrams)}")
    print(f"Anagrams: {anagrams}")

    palindromes = find_palindromes(words)
    print(f"Number of palindromes found: {len(palindromes)}")
    print(f"Palindromes: {palindromes}")

    palingrams = find_palingrams(words)
    print(f"Number of palingrams found: {len(palingrams)}")
    print(f"Palingrams: {palingrams}")
