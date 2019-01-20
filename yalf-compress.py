import sys, time, zlib, base64

f = open(sys.argv[1], "r")

print("File to compress: " + sys.argv[1])

code = base64.b64encode(zlib.compress(f.read().encode('utf-8'), 9))
code = code.decode('utf-8')

f2 = open(sys.argv[1] + ".yaclf", "w")
f2.write(code)
f2.close()


print("File compressed " + sys.argv[1] + ".yaclf")
