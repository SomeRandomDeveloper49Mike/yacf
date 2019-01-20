# yacf
Yet Another Config File.

simple config file, that looks like this:

```
! Comment.

*name: http-server-config ! Name of file.
*version: 1.0 ! Version of file.
*info: ? ! Info is ? (No info.)
*addcompressedlib: %config-http.yaclf ! Adding compressed library to config file. (% means filename)
*addlib: %config-math.yalf ! Adding library to config file.

*start ! Config goes below *start
host: 5000
port: 90
entry: %index.html
*end

```

## yalf-compress and yalf-decompress

These py scripts are made to compress (.yaclf) and decompress (.yalf) Yet Another Library Files.

#### Usage:

`python yalf-compress.py <lib filename>` creates <lib filename>.yaclf file.
  
`python yalf-decompress.py <compressed lib filename>` creates <compressed lib filename>.yalf file.

# Usage
You can insert this into python code.

```python
from YACF import Yacf

config = Yacf("config.yacf")

config.props # Properties of file. (*name, *start, etc.) {"name": name, "value": value}
config.final # Properties. {"name": name, "value": value}
```
