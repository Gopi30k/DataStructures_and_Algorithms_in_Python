def flattenArray(arr:list):
    flatArray=[]
    for i in arr:
        # if isinstance(i,list):
        if type(i) is list:
            flatArray.extend(flattenArray(i))
        else:
            flatArray.append(i)
    return flatArray

if __name__ == "__main__":
    print(flattenArray([1, 2, 3, [4, 5] ]))
    print(flattenArray([1, [2, [3, 4], [[5]]]]))
    print(flattenArray([[1],[2],[3]]))
    print(flattenArray([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))