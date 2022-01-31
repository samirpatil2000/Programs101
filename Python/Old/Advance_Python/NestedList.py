# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

students = [['Harry', 37.21], ['Berry', 37.21], ['Iris', 37.2], ['Catty', 41], ['Cisco', 39]]
# listNumber =[]


sorting =  lambda students : students[1]
students.sort(key=sorting)
print(students[1][0])
# listNumber = list()
# for i  in students:
#     a=i[1]
#     listNumber.append(a)
#     print(a)
#
# listNumber.sort
# print(listNumber)
a = (1, 11, 2)

x = sorted(a)

print(x)