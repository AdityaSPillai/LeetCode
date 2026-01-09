class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        for str1 in strs:
            count=[0]*26
            for s in str1:
                count[ord(s)-ord("a")]=1+count[ord(s)-ord("a")]
            freq[tuple(count)].append(str1)
        return list(freq.values())