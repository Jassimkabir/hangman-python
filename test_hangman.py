import os
import hangman

def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")

def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")
