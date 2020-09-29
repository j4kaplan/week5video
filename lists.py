def main():
    file = open("silly.txt",'r')
    all_of_file = file.readlines()
    print(all_of_file)


def reverser():
    rev_file= open("reversible.txt", 'r')
    all_lines = rev_file.readlines()
    print(all_lines)
    to_insert = all_lines [0]
    print(f"welcome to {to_insert}, fantastic student")

reverser()
main()
