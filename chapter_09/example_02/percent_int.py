foo = 42
spam = """%%d: %d
%%o: %o
%%x: %x
%%X: %X
%%f: %f
%%e: %e
%%E: %E
%%g: %g
""" % (foo, foo, foo, foo, foo, foo, foo, foo)
print(spam)
