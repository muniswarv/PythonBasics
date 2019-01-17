
import sys

fp = sys.stdin
fo = sys.stdout
fe = sys.stderr

for line in fp.readlines():
    print("-- Print  :" , line, end=' ')
    fo.write("-- stdout : "+line)
    fe.write("-- stderr : "+line)
