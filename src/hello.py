def greet(name: str):
    print(f"hello, {name}")


def main():
    for name in "James", "Subscriber", "other":
        greet(name)


if __name__ == "__main__":
    main()
