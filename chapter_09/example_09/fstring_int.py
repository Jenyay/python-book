foo = 42
spam = f"""{{foo}}: {foo}
{{foo:d}}: {foo:d}
{{foo:b}}: {foo:b}
{{foo:o}}: {foo:o}
{{foo:x}}: {foo:x}
{{foo:X}}: {foo:X}
"""
print(spam)
