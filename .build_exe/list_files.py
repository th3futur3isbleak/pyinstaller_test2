import os

# files = [os.path.join(dp, f) for dp, dn, filenames in os.walk('.') for f in filenames]


script_dir = os.path.dirname(__file__)
curr_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
print(f"Cur dir {curr_dir}")
print(f"'.' directory: {os.path.dirname('.')}")

files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(curr_dir) for f in filenames]

print(f"__file__: {os.path.dirname(__file__)}")
for file in files:
    if "build_exe" in file:
        print(os.path.join(curr_dir, file))
    if "build" not in file and "venv" not in file and ".git" not in file:
        print(os.path.join(curr_dir, file))
