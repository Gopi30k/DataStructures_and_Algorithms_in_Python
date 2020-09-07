def anagramFinder(word1: str, word2: str):  # O(n)
    if len(word2) != len(word1):
        return False
    wordCounter = {}
    for i in word1.lower():
        wordCounter[i] = wordCounter[i] + 1 if i in wordCounter.keys() else 1
    for i in wordCounter.keys():
        if word2.lower().count(i) != wordCounter[i]:
            return False
    return True


if __name__ == "__main__":
    print(anagramFinder('anagram', 'nagaram'))
    print(anagramFinder('aaz', 'zza'))
    print(anagramFinder('texttwistTime', 'timetwistText'))
