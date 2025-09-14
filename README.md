# LSEG Challenge 2

## How to run

```python3
python3 challenge.py
```

```
Example Object: {"a": {"b": {"c": "d"}}}
Please enter Object: {"a": {"b": {"c": "d"}}}

Example Key: a/b/c
Please enter Key: a/b/c

Value: d
```

## Unit tests

Unit tests are inside `challenge.py`

```
# Unit tests
s = Solution()
assert s.solve({"a": {"b": {"c": "d"}}}, 'a/b/c') == 'd'
assert s.solve({"x": {"y": {"z": "a"}}}, 'x/y/z') == 'a'
```
