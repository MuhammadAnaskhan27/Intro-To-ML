# File Reading

file = open("example.txt","r")
content = file.read()
print(content)
file.close()


file = open("example.txt","r")
line = file.readlines()
while line:
    print(line,end="")
    line = file.readlines() 
print(line)
file.close()


# File writing
file = open("example.txt","w")
file.write("jsx components props props destructuring usestate handling forms and events conditional rendering list and keys in react props vs state event handling api fetching useeffect context api routing in react nested routing dynamic routing Form validation using formik and yup")
file.close()

# File appending
file = open("example.txt","a")
file.write("I have learned above topics in react")
file.close()




