import os

tests = [str(x / 10) + str(x % 10) for x in range(1,55)]
for test in tests:
  # reads from 01 and writes to 01.a
  os.system("some_file.exe <" + test + " >" + test + ".a")