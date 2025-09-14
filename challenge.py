from typing import List
import json


class Solution:
    def solve(self, obj: dict | str, key: str):
        key = [c for c in str(key).strip().split('/')]

        def dfs(obj: dict, key: List[str]) -> str:
            if len(key) == 1:
                return obj[key[0]]
            key1 = key.pop(0)
            return dfs(obj[key1], key)
        return dfs(obj, key)


# Unit tests
s = Solution()
assert s.solve({"a": {"b": {"c": "d"}}}, 'a/b/c') == 'd'
assert s.solve({"x": {"y": {"z": "a"}}}, 'x/y/z') == 'a'

# User tests
print('Example object: {"a": {"b": {"c": "d"}}}')
obj = json.loads(input('Please enter object:'))
print()
print('Example key: a/b/c')
key = input('Please enter key:')

s = Solution()
print('value: ', s.solve(obj, key))
