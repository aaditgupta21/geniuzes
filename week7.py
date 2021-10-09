student_list = ['pam','rob','joe','greg','bob','amy','matt']

print(student_list[0:3])

print(student_list[5:6])

print(student_list[0:6])

for i in range(len(student_list)):
  if(student_list[i] == "rob"):
      print("Rob is in list")

p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]

for i in range(len(list_of_people)):
    for key in i:
        print(i[key])