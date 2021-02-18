# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c: list):
    jump = -1
    i = 0
    while i < len(c):
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1
        jump += 1
    return jump


if __name__ == '__main__':
    print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
    print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
