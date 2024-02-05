import os
from re import sub

file_name = input("Type in the name of your file: ")

file_content = input("Type in the content of your file: ")

print(os.getcwd)

def string_to_snake_case(string):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        string.replace('-', ' '))).split()).lower()

with open("{}.txt".format(string_to_snake_case(file_name)), mode='w') as f:
    f.write(file_content)
    f.close