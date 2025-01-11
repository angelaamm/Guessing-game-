file_path="C:/Users/Angie/OneDrive/Desktop/read_file.txt"
#to read a file
with open(file_path, 'r')as file:
    content=file.read()
    print(content)

#to write a file
with open(file_path,'w')as file:
    file.write("Hello\n")
    file.write("I am Angela, a child of God this one. My favourite fast food is pizza.\n")
    file.write("Goodbye!\n")
    file.close()

#To append a file
with open(file_path, 'a') as file:
    file.write("Hello\n")
    file.write("I am John, a child of God this one. My favourite fast food is kebab.\n")
    file.write("Goodbye!\n")
    file.close()