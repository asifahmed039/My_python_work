#project
#Restaurant Menu
print("Menu")
no_of_item=int(input('enter the no of total item.'))
item=[]
for i in range(no_of_item):
    item.append(input())
print(item)
price=[]
for i in range(no_of_item):
    price.append(int(input()))

for i in range(no_of_item):
    dash=20-(len(item[i]))-(len(price[i]))
    print(item+dash+price)