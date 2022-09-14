
print("Hello World!")
name = {'a': 100, 'b': 200, 'c': 300}
number = {'a': 300, 'b': 200, 'd': 400}
def pr4():
    print("Enter the number of items")
    numItems = int(input())
    index = 0
    dictionary = {}
    while(index < numItems):
        fruit, price = input("Enter a item and price: ").split()
        
        dictionary.update({fruit: price})
        
        index = index + 1
    for key, value in dictionary.items():
        print(key, ' : ', value)

pr4()


