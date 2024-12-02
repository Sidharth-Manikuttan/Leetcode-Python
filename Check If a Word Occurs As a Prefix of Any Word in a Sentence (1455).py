class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence=sentence.split(' ')
        for word in sentence:
            if(word.startswith(searchWord)):
                return sentence.index(word)+1
        return -1
