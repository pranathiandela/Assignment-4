#write and append data to a file
with open("output.txt","w") as fh:
    s=input(" Enter text to write to the file:")
    fh.write(s)
    print("Data successfully written to output.txt")
#n=int(input("Enter the number of lines you want to write:"))
with open("output.txt","a") as fh:
    #for i in range(n):
        s= input("Enter additional text to append: ")
        fh.writelines("\n"+s+"\n")
        print("Data successfully appended.")
with open("output.txt","r") as fh:
    print(" Final content of output.txt.")
    lines = fh.readlines()
    for line in lines:
        print(line)
