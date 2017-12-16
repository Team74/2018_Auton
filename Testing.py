file = open("TestFile.py","w")

file.write("Hello, World!\n")
file.write("This, is, our, new, text, file., \n")
file.write("and, this, is, another, line., \n")
file.write("Why?, Because, we, can., \n")
file.close()

with open("TestFile.py", "r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        print(words)
file.close()
