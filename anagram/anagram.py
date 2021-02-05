
def find_anagrams(word, candidates):
    word_letters = ''.join(sorted([x.lower() for x in word]))
    anagrams = []
    for candidate in candidates:
        if word.lower() != candidate.lower():
            candidate_letters = ''.join(sorted([x.lower() for x in candidate]))
            if len(candidate_letters) == len(word_letters):
                if candidate_letters in word_letters:
                    anagrams.append(candidate)
    return anagrams


candidates = ["dog", "goody"]
print(find_anagrams("good", candidates))
