def collect_strings(object: dict):
    stringArr = []

    def helper_method(dict_obj: dict):
        for key, value in dict_obj.items():
            if isinstance(value, str):
                stringArr.append(value)
            else:
                helper_method(value)
    helper_method(object)
    return stringArr


def collect_strings_recursive(object: dict):
    stringArr = []
    for key, value in object.items():
        if isinstance(value, dict):
            stringArr.extend(collect_strings_recursive(value))
        elif isinstance(value, str):
            stringArr.append(value)
    return stringArr


if __name__ == "__main__":
    obj = {
        'stuff': 'foo',
        'data': {
            'val': {
                'thing': {
                    'info': 'bar',
                    'moreInfo': {
                        'evenMoreInfo': {
                            'weMadeIt': 'baz'
                        }
                    }
                }
            }
        }
    }

    print(collect_strings(obj))
    print(collect_strings_recursive(obj))
