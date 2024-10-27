def flatten_array(arr):
    flattened = []
    for item in arr:
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            flattened.append(item)
    return flattened

a = eval(input("Enter a list: "))
print("The Flattened list is:", flatten_array(a))

