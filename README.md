# confScript

don't think it is another \*script language!!

It can do a lot..

install via pip
```
pip install confscript
```

let's get started!

some basic concepts:

1. headers have this syntax:
```
== name ==
```
headers must always be alphanumeric and without spaces and other symbols

2. keyword and value have this syntax:
```
keyword : value
```
here, value can be a string or number or True or False..

3. What about lists?
lists values are separated by a ","
example:
```
== header ==
key : value1,value2,value3
```

4. what separated data headers?
all headers are separated by a ---
okay?
look at this data:
```
== Python ==
extensions : .py,.pyc,.pyw,etc,etc
command    : python (filepath)
---
== JavaC ==
extensions : .java,.class
command    : javac (filepath) && java (filebasename)
```

Example data:
```
== TestingData ==
lucky word              	  : python
lucky number                  : 83
is lucky-number really lucky? : True
```
it will become:
```python
{'TestingDataSet': {'lucky word': 'python', 'lucky number': 83, 'is lucky-number really lucky?': True}}
```

## so what's in this module?

there are 3 functions:
```
read(data_as_string)
readFile(data_containing_file_path)
dump(python_dictonary)
```

simple! isn't it?