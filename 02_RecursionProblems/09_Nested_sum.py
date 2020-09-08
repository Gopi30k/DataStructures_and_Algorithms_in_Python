# Return sum of all even numbers in an nested object

def nestedSumFinder(object: dict, sum=0):
    for key, value in object.items():
        if type(value) is dict:
            sum += nestedSumFinder(value)
        elif type(value) is int and value % 2 == 0:
            sum += value
    return sum


if __name__ == "__main__":
    obj1 = {
        'outer': 2,
        'obj': {
            'inner': 2,
            'otherObj': {
                'superInner': 2,
                'notANumber': True,
                'alsoNotANumber': 'yup'
            }
        }
    }

    print(nestedSumFinder(obj1))

    print(nestedSumFinder({
        'a': 2,
        'b': {'b': 2, 'bb': {'b': 3, 'bb': {'b': 2}}},
        'c': {'c': {'c': 2}, 'cc': 'ball', 'ccc': 5},
        'd': 1,
        'e': {'e': {'e': 2}, 'ee': 'car'}
    }))
