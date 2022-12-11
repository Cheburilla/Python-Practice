def sleight_of_hand(k: int, field: str) -> int:
    able = k*2
    counter = 0
    for k in range(1, 10):
        if field.count(str(k)) <= able and field.count(str(k)) != 0:
            counter += 1
    return counter
