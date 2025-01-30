while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Use nested loops to draw the pattern
row = 0
while row < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line
        row += 1