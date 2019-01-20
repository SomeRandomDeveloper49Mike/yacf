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
