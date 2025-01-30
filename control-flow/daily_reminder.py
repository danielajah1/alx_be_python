Task = input("Enter your task description: ")
Priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time-bound? (yes/no): ")

# Process task using match-case and conditionals
match Priority:
    case "high":
        reminder = f"'{Task}' is a high priority task."
    case "medium":
        reminder = f"'{Task}' is a medium priority task."
    case "low":
        reminder = f"'{Task}' is a low priority task. Consider completing it when you have free time."
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
                        

if Time_bound == "yes":
    reminder += " It requires immediate attention today!"
elif Time_bound != "no":
        print("Invalid response for time sensitivity. Please enter yes or no.")
        

