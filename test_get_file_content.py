from functions.get_file_content import get_file_content
import os

print("test 1")
print(get_file_content("calculator", "lorem.txt"))

print("test 2")
print(get_file_content("calculator", "main.py"))

print("test 3")
print(get_file_content("calculator", "pkg/calculator.py"))

print("test 4")
print(get_file_content("calculator", "/bin/cat"))

print("test 5")
print(get_file_content("calculator", "pkg/does_not_exist.py"))