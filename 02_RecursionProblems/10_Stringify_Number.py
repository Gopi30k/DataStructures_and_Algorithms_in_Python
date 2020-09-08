def stringifyNumbers(object: dict):
    for key, value in object.items():
        if isinstance(value, int):
            object[key] = str(value)
        elif isinstance(value, dict):
            object[key] = stringifyNumbers(value)
        else:
            object[key] = value
    return object


if __name__ == "__main__":
    print(stringifyNumbers({
        'a': 2,
        'b': {'b': 2, 'bb': {'b': 3, 'bb': {'b': 2}}},
        'c': {'c': {'c': 2}, 'cc': 'ball', 'ccc': 5},
        'd': 1,
        'e': {'e': {'e': 2}, 'ee': 'car'}}))

    print(stringifyNumbers({
        'num': 1,
        'test': [],
        'data': {
            'val': 4,
            'info': {
                'isRight': True,
                'random': 66
            }
        }
    }))
