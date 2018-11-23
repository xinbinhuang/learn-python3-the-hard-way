# Some notes

## `pydoc`

- documentation generator

> examples

```bash
pydoc print

pydoc sys

pydoc numpy.mean
```

## ex23 - UTF-8, UTF-16, ASCII

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

### ex35

**What does exit(0) do?** On many operating systems a program can abort with exit(0), and the number passed in will indicate an error or not. If you do exit(1) then it will be an error, but exit(0) will be a good exit. The reason it’s backward from normal Boolean logic (with 0==False) is that you can use different numbers to indicate different error results. You can do exit(100) for a different error result than exit(2) or exit(1).

### ex36

#### *Rules for If-Statements*

1. Every if-statement must have an else.
2. If this else should never run because it doesn’t make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.
3. Never nest if-statements more than two deep and always try to do them one deep.
4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
5. Your Boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.

#### *Rules for Loops*

1. Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.

**WARNING!** Never be a slave to the rules in real life. If you think a rule is stupid, try not using it.

#### *Tips for Debugging*

1. Do not use a ”debugger.” A debugger is like doing a full-body scan on a sick person. You do not get any specific useful information, and you find a whole lot of information that doesn’t help and is just confusing.
2. The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.
3. Make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little.

#### Writing software in small chunks

- Break up the whole software into pieces, and List out all the components you need in the software
- start to write small component first, then **run** it and **test** it
- go for the next component and repeat

## ex37

### String formatting rule of thumbs

[Python f-string documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
[link](https://realpython.com/python-string-formatting/)
![string-flow-chart](https://files.realpython.com/media/python-string-formatting-flowchart.4ecf0148fd87.png)

1. old-style formatting
    ```python
    >>> 'Hey %s, there is a 0x%x error!' % (name, errno)
    'Hey Bob, there is a 0xbadc0ffee error!'
    ```
2. new-style formatting
    ```python
    >>> 'Hey {name}, there is a 0x{errno:x} error!'.format(
    ...     name=name, errno=errno)
    'Hey Bob, there is a 0xbadc0ffee error!'
    ```
3. String Interpolation/f-string
    ```python
    >>> f"Hey {name}, there's a {errno:#x} error!"
    "Hey Bob, there's a 0xbadc0ffee error!"
    ```
4. template
    ```python
    >>> from string import Template
    >>> templ_string = 'Hey $name, there is a $error error!'
    >>> Template(templ_string).substitute(
    ...     name=name, error=hex(errno))
    'Hey Bob, there is a 0xbadc0ffee error!'
    ```