def calculate_square(side_square: int) -> tuple:
    perimeter = 4 * side_square
    diagonal = side_square * pow(2, 0.5)
    area = pow(side_square, 2)
    return perimeter, diagonal, area


if __name__ == "__main__":
    side = int(input("Enter square side length: "))
    perimeter_res, area_res, diagonal_res = calculate_square(side)
    print("Perimeter:", perimeter_res)
    print("Area:", area_res)
    print("Diagonal:", diagonal_res)
