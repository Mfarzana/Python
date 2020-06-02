import random
print(random.random())
print("random range ",random.randint(0,20))
color_list=["blue","red","yello","green"]
print("Random choice color from list > ",random.choice(color_list))
print("Randomly choose 2 color from list > ",random.choices(color_list,k=2))
random.shuffle(color_list)
print("Color list after shuffle > ",color_list)
