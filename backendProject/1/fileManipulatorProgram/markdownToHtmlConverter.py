import markdown

def markdown(input, output):
    with open(input) as file:
        contents=file.read()
    with open(output, "w") as file:
        file.write(markdown.markdown(contents))

def main():
    markdown('test.md','test.html')

if __name__ == "__main__":
    main()
    