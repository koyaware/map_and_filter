list_1 = ['apple', 'banana', "cherry"]
list_2 = ['orange', 'lemon', 'pineapple']

def lists(list1,list2):
    return list(map(lambda x, y: x + y,list1, list2))

print(lists(list_1,list_2))