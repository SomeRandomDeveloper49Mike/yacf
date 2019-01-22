## old repsirory. go to yacf-master

# yacf
Yet Another Config File.

example of simple config file, that looks like this:

```
*name: sample-file
*version: 1.0.4
*info %info.txt
*lib: http-server-info.yalf
*start: ?
host: 5000
port: 80
entry: index.html
*end: ?
```

## yalf-compress and yalf-decompress

##### not implemented yet, in yacf you can use only "lib" property. ("clib" is for adding compressed lib)
These py scripts are made to compress (.yaclf) and decompress (.yalf) Yet Another Library Files.

#### Usage:

`python yalf-compress.py <lib filename>` creates <lib filename>.yaclf file.
  
`python yalf-decompress.py <compressed lib filename>` creates <compressed lib filename>.yalf file.

# Usage
You can insert this into python code.

```python
from yacf import Yacf, Property

Yacf.compile("filename.yacf")

Yacf.config   # Property(name, value)
Yacf.props    # Property(name, value) (witch start with *)

```
# YALF

yalf or Yet Another Library File, is used to make sure that all properties are correct for some usage. (TODO: rewrite this line)

for example, if you did not import lib into file, you could not add properties witch aren't specified in lib file.

syntax of yalf is prettty simple, because it uses python code to generate main lib.
```
name: sample-lib
version: 1.0.6
start: ?
```
```python

AddProperty("name") # Add property (in yacf start from *)
AddConfiguration("name") # Adding configuration to yacf file.

Debug("Hello, world!") # alternative tp print. (actually print.)
```
this is in one file (test.yalf)
