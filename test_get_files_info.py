from functions.get_files_info import get_files_info
import os
print("test 1")
print(get_files_info("calculator", "."))

print("test 2")
print(get_files_info("calculator", "pkg"))

print("test 3")
print(get_files_info("calculator", "/bin"))

print("test 4")
print(get_files_info("calculator", "../"))
