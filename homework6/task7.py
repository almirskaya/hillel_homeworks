def display_box(width: int, height: int, character='x'):
    print(character * width)
    for i in range(height - 2):
        print(character + " " * (width - 2) + character)
    print(character * width)


if __name__ == '__main__':
    display_box(3, 3)
    display_box(3, 4)
    display_box(4, 4)
    display_box(5, 4)
    display_box(5, 5)
