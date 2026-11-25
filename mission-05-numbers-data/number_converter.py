def main():
    raw_value = input("Enter a positive decimal whole number: ").strip()

    try:
        number = int(raw_value)
        if number <= 0:
            print("Please enter a positive whole number.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Binary: {bin(number)[2:]}")
    print(f"Hexadecimal: {hex(number)[2:].upper()}")


if __name__ == "__main__":
    main()
