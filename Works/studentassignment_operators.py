#student enter mrarks of 5subjects and takeaverage and total

Name=input("Enter the Name of Student\n")
E=int(input("Enter the mark of English\n"))
M=int(input("Enterthe marks of Maths\n"))
P=int(input("Enter the marks of physics\n"))
C=int(input("enter the marks of Chemistry\n"))
B=int(input("Enter the mark of Biology\n"))
Total=E+M+P+C+B
Avg = Total/5
print("Name of Student",Name)
print("Total marks is",Total)
print("Average Marks is",Avg)


