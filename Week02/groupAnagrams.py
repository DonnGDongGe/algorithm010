# 方法一

class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())

# 方法二

def groupAnagrams(strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()
