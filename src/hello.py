def greet(name: str):
    print(f"hello, {name}")
    print("nice to meet you!")


def main():
    for name in "James", "Subscriber", "other":
        greet(name)


if __name__ == "__main__":
    main()
