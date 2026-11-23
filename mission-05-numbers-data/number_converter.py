try:
    number = int(input("Enter a decimal whole number: "))
except ValueError:
    print("Please enter a whole number, such as 13.")
    raise SystemExit(1)

print("Binary:", bin(number))
print("Hexadecimal:", hex(number))
