fruits = ['apple','orange','banana']
#add
new_fruit = fruits.append('mango')
#remove
remove_fruit = fruits.remove('apple')
for i in range (len(fruits)):
    print(str(i+1)+'.'+fruits[i])
