from functions.write_file import write_file
import os

print("test 1")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("test 2")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("test 3")
print(write_file("calculator", "/tmp/tmp.txt", "this should not be allowed"))

