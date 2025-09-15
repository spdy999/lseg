from typing import List
import json


class Solution:
    def solve(self, obj: dict | str, key: str):
        key = [c for c in str(key).strip().split('/')]

        def dfs(obj: dict, key: List[str]) -> str:
            if key[0] not in obj:
                return "Sorry, we can't find the value from the key. Please recheck the key"
            if len(key) == 1:
                return obj[key[0]]
            key1 = key.pop(0)
            return dfs(obj[key1], key)
        return dfs(obj, key)


# Unit tests
print('Running unit tests...')
s = Solution()
assert s.solve({"a": {"b": {"c": "d"}}}, 'a/b/c') == 'd'
assert s.solve({"x": {"y": {"z": "a"}}}, 'x/y/z') == 'a'
assert s.solve({"x": {"y": {"z": "a"}}}, 'x/y') == {'z': 'a'}
assert s.solve({"x": {"y": {"z": "a"}}},
               'x/y/r') == "Sorry, we can't find the value from the key. Please recheck the key"
assert s.solve({"x": {"y": {"z": "a"}}},
               'x/y/z/r') == "Sorry, we can't find the value from the key. Please recheck the key"
print('All passed')
print()

# User tests
while True:
    print('Example Object: {"a": {"b": {"c": "d"}}}')
    obj = json.loads(input('Please enter Object: '))
    print()
    print('Example Key: a/b/c')
    key = input('Please enter Key: ')
    print()

    s = Solution()
    print('Value:', s.solve(obj, key))
    print()
