import math

while True:
    print("\n--- Area Calculator ---")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Trapezoid")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        s = float(input("Enter side length: "))
        print(f"Area = {s * s}")
    elif choice == "2":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        print(f"Area = {w * h}")
    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area = {0.5 * b * h}")
    elif choice == "4":
        r = float(input("Enter radius: "))
        print(f"Area = {math.pi * r * r}")
    elif choice == "5":
        a = float(input("Enter base a: "))
        b = float(input("Enter base b: "))
        h = float(input("Enter height: "))
        print(f"Area = {0.5 * (a + b) * h}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
