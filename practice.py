def main():
    name = input("Enter a  name: ")
    a = name.capitalize()
    lst = []
    for i in a:
        lst.append(i)
    print(lst)

def modifyName(lst):
    lst[0] = "Z"
    print(lst)



main()
