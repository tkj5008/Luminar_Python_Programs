employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]



# for employee in employees:
#     print(employee["e_name"])
#
# for employee in employees:
#     print(employee["e_name"].upper())


# employee with department developer
# for employee in employees:
#     if(employee["department"]=="developer"):
#         print("developer",employee["e_name"])


#Sum of salary
# total=0
# for employee in employees:
#     total+=employee["salary"]
# print(total)

#1 case map
#2 case filter
#3 case reduce

lst=[2,3,4,5,6,7,8]

# def square(num):
#     return num**2
# squares=list(map(square,lst))
#
# print(squares)

# cube =lambda num:num**3
# print(cube)

# def cube(num):
#     return num**2
# cubes=list(map(lambda num:num**3,lst))
# print(cubes)

# cubes=list(map(lambda num:num**3,lst))
# print(cubes)

# squares=list(map(lambda num:num**2,lst))
# print(squares)

e_names=list(map(lambda employee:employee["e_name"],employees))
print(e_names)
e_upper=list(map(lambda emp:emp["e_name"].upper(),employees))
print(e_upper)

