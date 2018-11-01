#

## `pydoc`

- documentation generator

> examples

```bash
pydoc print

pydoc sys

pydoc numpy.mean
```

## UTF-8, UTF-16, ASCII

- 1 byte = 8 bits

`utf-8`: "Unicode Transformation Format 8 Bits."    - use `Unicode` to represent text (not just english)

`ASCII` (8 bits): American Standard Code for Information Interchange

Python convetion: "utf-8"

```python
ord("q")
# 113

chr(113)
# q

"你好".encode()
# b'\xe4\xbd\xa0\xe5\xa5\xbd'

"b'\xe4\xbd\xa0\xe5\xa5\xbd'".decode()
# 你好
```
