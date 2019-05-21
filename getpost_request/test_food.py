import mlab
from food import Food

mlab.connect()

#1 Create 
#1.1 Create a food data
f = Food(title="Bánh gạo", link="<<Link sai>>")
#1.2 Save it
# f.save()

#2 Read
#2.1 Get cursor
f_objects = Food.objects()  #Lazy loading  #Same a list
#2.1 Process cursor
# f_first = f_objects[0]  #Actual data transfering
# print(f_first)
# print(f_first.link)

# print(len(f_objects))
# print(f_objects.count())

# for f in f_objects:
#     print(f.title)
#     print(f.link)
#     print("------------")

# f = f_objects[3]
# f.update(set__title="Bánh rất rất dầy", set__link="http://banhdayngon.vn/wp-content/uploads/2015/04/banh-giay-chay.jpg")
# f.reload()
# print(f.title)

# f.delete()

f = f_objects.with_id("5ce0db8e78540ca6ea76bdd9")
if f != None:
    f.delete()
else:
    print("Not found")



