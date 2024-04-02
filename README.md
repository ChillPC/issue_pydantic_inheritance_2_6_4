# Reproduce issue on pydantic v2.6.4

Reproduce a bug with inheritance between `BaseModel` in pydantic `v2.6.4` (`v2.6.3` works fine).

Run :
```shell
poetry shell
mypy
```

To get the error :
```
issue_pydantic.py:15: error: Incompatible types in assignment (expression has type "None", variable has type "int")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```
