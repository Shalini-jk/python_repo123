a = str(input("Enter the name of the file with .txt extension:\n "))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()