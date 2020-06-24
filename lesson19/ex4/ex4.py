import sys
from collections import defaultdict


# Well done - loved it


def build_anagrams_dict():
    filename = sys.argv[1]  # words
    anagrams_dict = defaultdict(set)
    with open(filename, "r") as f:
        for word in f:
            clean_word = word.strip()
            key = (''.join(sorted(clean_word)))
            anagrams_dict[key].add(clean_word)
        return anagrams_dict


try:
    anagram_sets = build_anagrams_dict()
except Exception:
    print("Illegal input file name")
    exit(1)

for anagram_words in anagram_sets.values():
    anagrams_list = list(anagram_words)
    print(' '.join(anagrams_list))
