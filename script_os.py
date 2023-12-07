import os.path

CURRENT_DIR = os.path.abspath(__file__)
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)

if not os.path.exists("tmp2"):
    os.mkdir("tmp2")
    print("Create")
else:
    print("not create")
