import random

def main():
    file = open("silly.txt",'r')
    all_of_file = file.readlines()
    random_line= random.choice(all_of_file)
    print(random_line)


def reverser():
    rev_file= open("reversible.txt", 'r')
    all_lines = rev_file.readlines()
    print(all_lines)
    to_insert = all_lines[0]
    print(f"welcome to {to_insert}, fantastic student")

#reverser()
#main()

def string_formatting_demo():
    result= 100/3
    formatted_number = "{:5.3f}".format(result)
    print(formatted_number)


string_formatting_demo()

