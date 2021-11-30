from mario import generate_mario_pyramid


if __name__ == "__main__":
    height = None

    while height == None or generate_mario_pyramid(height) == None:
        try:
            height = int(input("Height: "))
        except ValueError:
            continue

    print(generate_mario_pyramid(height))