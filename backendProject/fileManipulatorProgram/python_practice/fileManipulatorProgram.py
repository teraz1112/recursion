def reverse(input, output):
    with open(input) as file:
        contents=file.read()
    with open(output, "w") as file:
        file.write(contents[::-1])

def copy(input, output):
    with open(input) as file:
        contents=file.read()
    with open(output, "w") as file:
        file.write(contents)

def duplicateContents(input):
    with open(input) as file:
        contents=file.read()
    with open(input, "a") as file:
        file.write(contents*5)
    
def reverseString(input,string,newString):
    with open(input) as file:
        contents=file.read()
    with open(input, "w") as file:
        file.write(contents.replace(string,newString))
def main():
    reverse('text/test.txt','text/test2.txt')
    copy('text/test.txt','text/test3.txt')

if __name__ == "__main__":
    main()
