# Medicine Reminder System

reminders = []

while True:
    print("\n===== Medicine Reminder =====")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Delete Medicine")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        medicine = input("Enter Medicine Name: ")
        time = input("Enter Time (e.g., 8:00 AM): ")

        reminders.append({
            "Medicine": medicine,
            "Time": time
        })

        print("Medicine reminder added successfully!")

    elif choice == "2":

        if len(reminders) == 0:
            print("No medicine reminders found.")

        else:
            print("\nToday's Reminders")
            print("---------------------------")

            for i, reminder in enumerate(reminders, start=1):
                print(f"{i}. {reminder['Medicine']} - {reminder['Time']}")

    elif choice == "3":

        if len(reminders) == 0:
            print("No reminders to delete.")

        else:
            for i, reminder in enumerate(reminders, start=1):
                print(f"{i}. {reminder['Medicine']} - {reminder['Time']}")

            delete = int(input("Enter reminder number to delete: "))

            if 1 <= delete <= len(reminders):
                reminders.pop(delete - 1)
                print("Reminder deleted successfully!")
            else:
                print("Invalid reminder number.")

    elif choice == "4":
        print("Thank you for using Medicine Reminder!")
        break

    else:
        print("Invalid choice. Please try again.")