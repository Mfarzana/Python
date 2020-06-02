print("Hello World")
# ..........vairable and datatypes...............
name="Farzana"
print("Name "+name);
val1=2
val2=3

print(val1+val2)
#......If else................
if val1%2==0:
    print(" even")
else:print("odd")

#............ list..............
list=[]
list.append("One")
list.append("Two")
list.append("Three")

for i in list:
    print(i);

list1=[1,3,5]
list2=[2,4,6]
list3=list1+list2 # join two list

print("numeric list ",list3)


# function
def sum(a,b):
    return a+b

sum=sum(10,20)
print("sum of two number ",sum)

# class and object

class HelloClass:
    str="Hello class variable "
    def helloFn(self):
        print("Hello Class Function")
        return "first"

objHello=HelloClass()
print(".......Hello class...")
print(objHello.helloFn());
print(objHello.str)

# Dictionaries
phoneBook={}
phoneBook["Farzana"]="345465465"
phoneBook["Tanbir"]="09458043968456"
print(phoneBook)

addressList={
    "farzana":{"houseNO":"43453","road":"4456"},
    "Tanbir": {"houseNO": "5645", "road": "4499956"}
}
print(addressList)
