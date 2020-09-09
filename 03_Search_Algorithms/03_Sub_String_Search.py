def subStringSearch(long_string: str, short_string: str):
    counter = 0
    for i in range(0, len(long_string)):
        for j in range(0, len(short_string)):
            if short_string[j] != long_string[i+j]:
                break
            if j == len(short_string)-1:
                counter += 1
    print('{0} occurances of "{1}" in "{2}" '.format(
        counter, short_string, long_string))


if __name__ == "__main__":
    subStringSearch("asdomgjasdomg", "omg")
