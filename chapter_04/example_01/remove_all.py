foo = [10, 20, 35, -5, 42, 1, 42, 2, 42, 16]
removed_val = 42
while removed_val in foo:
    foo.remove(removed_val)
    
print("foo:", foo)
