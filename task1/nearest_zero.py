def nearest_zero(len_array: int, array: str) -> str:
    array = (list(map(int, array.split())))
    result = [0 for i in range(len_array)]
    first_zero = array.index(0)
    last_zero = len(array) - 1 - array.index(0, list(reversed(array))[-1])
    for i in range(first_zero, len_array):
        result[i] = 0 if array[i] == 0 else result[i-1]+1
    for i in range(first_zero, 0, -1):
        result[i] = result[i+1]+1
    for i in range(last_zero-1, first_zero, -1):
        result[i] = 0 if array[i] == 0 else min(result[i], result[i+1]+1)
    return ' '.join(map(str, result))
