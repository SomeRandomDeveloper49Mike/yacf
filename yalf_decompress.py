import sys, zlib, base64

f = open(sys.argv[1], "r")

print("File to decompress: " + sys.argv[1])

f2 = open(sys.argv[1] + ".yalf", "w")

f2.write(zlib.decompress(base64.b64decode(f.read())).decode('utf-8'))

f2.close()

print("Successfully decompressed file: " + sys.argv[1] + ".yalf")
