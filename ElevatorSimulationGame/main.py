print("***************************************************************************************************************************************************")
print("-Hi, My name is Michael Marsillo and this is my third solo python project.")
print()
print("-I was riding in the elevator one day and i thought oh wow this elevator system could be replicated by a simple python project")
print("-So i decided to try and replicate it myself using my coding experience")
print()
print("-I tried to make it as realistic as possible by adding multiple passengers, a max capacity limit, and adding a wait time between floor transitions")
print()
print("-Hope you find my project fun and exciting!")
print("***************************************************************************************************************************************************")
print()

import time

def elevator_system():
    current_floor = 1  # The elevator starts on floor 1
    max_weight = 500  # Maximum weight the elevator can hold (in kg)
    max_passengers = 10  # Maximum number of passengers allowed in the elevator
    passengers = []  # List to store each passenger's weight
    total_weight = 0  # Keep track of the total weight of passengers

    print(f"Welcome to the Elevator! You are currently on floor {current_floor}.")

    # Add passengers and check weight
    def add_passengers():
        nonlocal total_weight
        while len(passengers) < max_passengers:  # Check if there is room for more passengers
            try:
                weight = float(input("Enter the weight of the passenger (or type 0 to stop adding passengers): "))
                if weight == 0:  # Exit if the user types 0
                    break
                if total_weight + weight > max_weight: # Weight exceeds maximum weight
                    print(f"Cannot add this passenger. Total weight would exceed {max_weight} kg.")
                else:
                    passengers.append(weight) # Add passengers weight to list and store each item in list as a passenger index (ex. [45, 35] 45 would be passenger 1 and 35 would be passenger 2)
                    total_weight += weight # Update the total weight each time a person is added
                    print(
                        f"Passenger added. Current total weight: {total_weight} kg, {len(passengers)} passengers on board.")
            except ValueError: # Error case
                print("Invalid input. Please enter a valid number.")

    # Remove passengers when they get off
    def remove_passengers():
        nonlocal total_weight
        while len(passengers) > 0:
            try:
                passengers_off = int(input(f"How many passengers are getting off (0 to stop): "))
                if passengers_off == 0:
                    break
                elif passengers_off > len(passengers):
                    print("You cannot remove more passengers than are on the elevator.")
                else:
                    for _ in range(passengers_off): # Removes the passenger at index 0 including their weight from total weight
                        weight_of_removed = passengers.pop(0)  # Remove the first passenger in the list (FIFO order)
                        total_weight -= weight_of_removed
                    print(
                        f"{passengers_off} passengers got off. {len(passengers)} passengers remain, total weight: {total_weight} kg.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Add passengers initially
    add_passengers()

    while True:
        target_floor = int(input("Enter the floor number you want to go to (1-10), or type 0 to exit: "))

        if target_floor == 0:
            print("Exiting the elevator. Have a great day!")
            break

        if target_floor == current_floor:
            print(f"You're already on floor {current_floor}.")
        elif target_floor > current_floor:
            print("Going up...")
            for floor in range(current_floor + 1, target_floor + 1):
                time.sleep(1.5)
                print(f"Arrived at floor {floor}")
            current_floor = target_floor
        else:
            print("Going down...")
            for floor in range(current_floor - 1, target_floor - 1, -1):
                time.sleep(1.5)
                print(f"Arrived at floor {floor}")
            current_floor = target_floor

        # let passengers off or on
        remove_passengers()
        if len(passengers) < max_passengers:
            add_more = input("Would you like to add more passengers (y/n)? ").lower()
            if add_more == 'y':
                add_passengers() # Run the add passengers function if they choose yes


# Run
elevator_system()
