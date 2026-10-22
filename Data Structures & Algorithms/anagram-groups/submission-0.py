class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 0: return []

        groups = {}
        for index, value in enumerate(strs):
            key = ''.join(sorted(value))
            if key not in groups:
                groups[key] = []
            groups[key].append(value)
        
        print(groups)
        return list(groups.values())

