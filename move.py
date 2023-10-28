import glob
from os import makedirs
import shutil

for i in glob.glob("*.py"):
    if i == "move.py":
        continue
    dir = i[:-4]
    makedirs(dir, exist_ok=True)
    shutil.move(i, dir + "/" + i[-4:])
