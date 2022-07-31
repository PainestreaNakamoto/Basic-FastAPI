# data = [1,1,3,4,5]

# def find(x , sets):
#     count = 0
#     for i in sets:
#         if i == x:
#             count += 1
#     return count 

# print(find(1,data))
# open()
# with open():
# for i in range(10):
#     file = open("ggez.txt","a")
#     file.write(f"{i} \n")
#     file.close()

file = open("ggez.txt","r")
a = file.readlines()
print(a)

b = "33364644"
print(b.split("6"))

print(b.replace("6",""))
for i in [1,2,3]:
    print('s')

a = "the STANDADSDD"

print(a.capitalize())
print(a.upper())
print(a.lower())
dd = "ssss56dd585d5d5"

for i in dd:
    if i.isdigit():
        print(i)
