import re
import sys
from collections import Counter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("File name is not set", file=sys.stderr)
        exit(1)

    with open(sys.argv[1], mode="r") as file:
        content = file.read().lower()

    words = list(Counter(re.findall(r"\w+", content)).items())
    word, word_count = max(words, key=lambda item: item[1])

    print(f"word = {word}\nword_count = {word_count}")
