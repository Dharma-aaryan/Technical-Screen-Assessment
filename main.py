def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    print(sort(100, 100, 100, 10))
    print(sort(200, 50, 20, 10))
    print(sort(50, 50, 50, 25))
    print(sort(200, 200, 200, 30))
    print(sort(150, 50, 50, 10))
