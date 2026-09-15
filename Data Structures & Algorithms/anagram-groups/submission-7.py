class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listHashs = defaultdict(list)

        for word in strs:
            hashWord = [0] * 26
            for w in word:
                hashWord[ord(w) - ord("a")] += 1
            listHashs[tuple(hashWord)].append(word)

        return list(listHashs.values())
