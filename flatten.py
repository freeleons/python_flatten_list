

#list to be flattened
list = [[1, 2, [3, [10]]], [4, 5, 6], [7], [8, 9]]
#flattened list
flatten_list = []
print("Before flattened list:")
print(list)


def flatten(list):
    if hasCountMethod(list):
        for item in list:
            # print(item)
            if hasCountMethod(item):
                flatten(item)
            else:
                flatten_list.append(item)
    else:
        flatten_list.append(list)

#numbers do not have build-in count attribute
def hasCountMethod(item):
    for methodname in dir(item):
        if methodname == 'count':
            # print(item)
            return True
    return False

flatten(list)
print("After flattened list:")
print(flatten_list)
