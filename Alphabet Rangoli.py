def print_rangoli(size):
    # your code goes here
    width: int = 4 * size - 3
    ascii_start: int = ord("a") - 1 # 97 - 1

    pattern_list: list[str] = []

    for i in range(1, size + 1):
        half_part: list[str] = [chr(ascii_start + size - j) for j in range(i)]
        line: str = "-".join(half_part + half_part[-2::-1])
        pattern_list.append(line.center(width, "-"))

    print(*pattern_list, sep="\n")
    print(*pattern_list[-2::-1],sep="\n")
