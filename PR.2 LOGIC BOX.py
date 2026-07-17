# Project : Logic Box

print("Welcome to the Pattern Generator and Number Analyzer!")
print("Select an option.")
print("1. Generate Right-Angled Triangle Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

while True:
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        rows = int(input("Enter the number of rows: "))
        if rows <= 0:
            print("Invalid row count!")
            continue
            
        print("Generated Pattern")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == "2":
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        
        if end < start:
            print("Error! End number must be greater than or equal to start.")
            continue
            
        total = 0
        print("Number Analysis")
        for num in range(start, end + 1):
            if num == 0:
                pass
            if num % 2 == 0:
                print(f"{num} is even")
            else:
                print(f"{num} is odd")
            total += num
            
        print("Sum of all numbers from", start, "to", end, "=", total)

    elif choice == "3":
        print("Thank you for using the Pattern Generator and Number Analyzer")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please Enter 1, 2, or 3.")
