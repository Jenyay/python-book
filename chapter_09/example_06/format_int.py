foo = 42
spam = """{{foo}}: {foo}
{{foo:d}}: {foo:d}
{{foo:g}}: {foo:g}
{{foo:b}}: {foo:b}
{{foo:o}}: {foo:o}
{{foo:x}}: {foo:x}
{{foo:X}}: {foo:X}
""".format(foo=foo)
print(spam)
