import os
import os.path as op

dir_1 = "examples"
if not op.exists(dir_1):
    os.mkdir(dir_1)

dir_2 = op.join(dir_1, "data")
if not op.exists(dir_2):
    os.mkdir(dir_2)

dir_3 = op.join(dir_2, "example_001")
if not op.exists(dir_3):
    os.mkdir(dir_3)
