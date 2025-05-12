def search(my_list, value):
    if value in my_list:
        return my_list.index(value)
    else:
        return -1
my_list = [15, 16, 17, 18, 19, 20, 21]
result = search(my_list, 18)
print(f"Index: {result}")



