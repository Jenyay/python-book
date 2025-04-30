foo = 42
spam = """%%d: %d
%%o: %o
%%x: %x
%%X: %X
%%f: %f
%%e: %e
%%E: %E
%%g: %g
""" % ((foo,) * 8)
print(spam)
