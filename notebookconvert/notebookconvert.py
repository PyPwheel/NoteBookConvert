import os

[os.system("jupyter nbconvert --to pdf " + f) for f in os.listdir(".") if f.endswith("ipynb")]