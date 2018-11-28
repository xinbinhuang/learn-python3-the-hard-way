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

## Basic Object-Oriented Analysis and Design

### [1] Bottom Up approach

 1. Take a small piece of the problem; hack on some code and get it to run barely.
 2. Refine the code into something more formal with classes and automated tests.
 3. Extract the key concepts you’re using and try to find research for them.
 4. Write a description of what’s really going on.
 5. Go back and refine the code, possibly throwing it out and starting over.
 6. Repeat, moving on to some other piece of the problem.

### [1] Top Down approach

 1. Write or draw about the problem.
 2. Extract key concepts from 1 and research them.
 3. Create a class hierarchy and object map for the concepts.
 4. Code the classes and a test to run them.
 5. Repeat and refine.

## Class Inheritance vs. Composition

### Inheritance

> In object-oriented programming, inheritance is the evil forest. Experienced programmers know to avoid this evil because they know that deep inside the Dark Forest Inheritance is the Evil Queen Multiple Inheritance. She likes to eat software and programmers with her massive complexity teeth, chewing on the flesh of the fallen. But the forest is so powerful and so tempting that nearly every programmer has to go into it and try to make it out alive with the Evil Queen’s head before they can call themselves real programmers. You just can’t resist the Inheritance Forest’s pull, so you go in. After the adventure you learn to just stay out of that stupid forest and bring an army if you are ever forced to go in again.

Actually:
**Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.**

Some simple rules:

1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
2. Use composition to package code into modules that are used in many different unrelated places and situations.
3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you’re using.

### Multiple inheritance

```python
class SuperFun(Child, BadStuff):
    pass
```

In this case, whenever you have implicit actions on any SuperFun instance, Python has to look-up the possible function in the class hierarchy for both `Child` and `BadStuff`, but it needs to do this in a consistent order --- uses ”method resolution order” (MRO) and an algorithm called `C3`.

To deal with this:

1. refactor your code to exclude multiple inheritance
2. use `super()`
    ```python
    class Child(Parent):
        # do `Child.__init__` first, then
        # do `Parent.__init__`
        def __init__(self, stuff):
            self.stuff = stuff
            super().__init__()
    ```

### Composition

Use other classes and modules to replace inheritance.

```python
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def overried(self):
        self.other.implicit()

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered())")


son = Child()
son.implicit()
son.override()
son.altered()
```