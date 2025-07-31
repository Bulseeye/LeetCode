class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a map for each itteration.
        
        res = defaultdict(list)

        # words = ["act","pots","tops","cat","stop","hat"]
        # using ascii

        for word in strs:
            # for each word create a alphabet filled with 0
            ascii_alpha = [0] * 26
            for char in word:
                # ord changes letter to ascii number
                ascii_alpha[ord(char) - ord("a")] += 1
            # looks like key={0, 1, 0, 0, 1}(26 numbers), value=[word].append s [act, cat]
            res[tuple(ascii_alpha)].append(word)
        # print(list(res.values()))
        return list(res.values())
