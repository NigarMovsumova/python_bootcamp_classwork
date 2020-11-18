def average(array):
    heights = set()
    for i in array:
        heights.add(i)
    return sum(heights) / len(heights)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
