from functions.run_python_file import run_python_file
import os

print("test 1, print calculator instructions")
print(run_python_file("calculator", "main.py"))

print("test 2, run calculator")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("test 3, run calcluator tests")
print(run_python_file("calculator", "tests.py"))

print("test 4, should return error")
print(run_python_file("calculator", "../main.py"))

print("test 5, should return error")
print(run_python_file("calculator", "nonexistent.py"))

print("test 6, should return error")
print(run_python_file("calculator", "lorem.txt"))