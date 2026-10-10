
def phone_book():
    while True:
        print("\n===== PHONE BOOK =====")
        print("1. Search")
        print("2. Service Nos")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Copy")
        print("7. Assign tone")
        print("8. Send business card")
        print("9. Options")
        print("10. Speed dials")
        print("11. Voice tags")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Search.")
            case "2":
                print("You selected Service Nos.")
            case "3":
                print("You selected Add name.")
            case "4":
                print("You selected Erase.")
            case "5":
                print("You selected Edit.")
            case "6":
                print("You selected Copy.")
            case "7":
                print("You selected Assign tone.")
            case "8":
                print("You selected Send business card.")
            case "9":
                print("You selected Options.")
            case "10":
                print("You selected Speed dials.")
            case "11":
                print("You selected Voice tags.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def messages():
    while True:
        print("\n===== MESSAGES =====")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smileys")
        print("7. Message settings")
        print("8. Info service")
        print("9. Voice mailbox number")
        print("10. Service command editor")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Write messages.")
            case "2":
                print("You selected Inbox.")
            case "3":
                print("You selected Outbox.")
            case "4":
                print("You selected Picture messages.")
            case "5":
                print("You selected Templates.")
            case "6":
                print("You selected Smileys.")
            case "7":
                print("You selected Message settings.")
            case "8":
                print("You selected Info service.")
            case "9":
                print("You selected Voice mailbox number.")
            case "10":
                print("You selected Service command editor.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def call_register():
    while True:
        print("\n===== CALL REGISTER =====")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call cost")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Missed calls.")
            case "2":
                print("You selected Received calls.")
            case "3":
                print("You selected Dialled numbers.")
            case "4":
                print("You selected Erase recent call lists.")
            case "5":
                print("You selected Show call duration.")
            case "6":
                print("You selected Show call cost.")
            case "7":
                print("You selected Call cost settings.")
            case "8":
                print("You selected Prepaid credit.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def tones():
    while True:
        print("\n===== TONES =====")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Message alert tones")
        print("5. Keypad tones")
        print("6. Warning tones")
        print("7. Vibrating alert")
        print("8. Screen saver")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Ringing tone.")
            case "2":
                print("You selected Ringing volume.")
            case "3":
                print("You selected Incoming call alert.")
            case "4":
                print("You selected Message alert tones.")
            case "5":
                print("You selected Keypad tones.")
            case "6":
                print("You selected Warning tones.")
            case "7":
                print("You selected Vibrating alert.")
            case "8":
                print("You selected Screen saver.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def settings():
    while True:
        print("\n===== SETTINGS =====")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Call settings.")
            case "2":
                print("You selected Phone settings.")
            case "3":
                print("You selected Security settings.")
            case "4":
                print("You selected Restore factory settings.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def music():
    while True:
        print("\n===== MUSIC =====")
        print("1. Music player")
        print("2. Radio")
        print("3. Recorder")
        print("4. Track list")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Music player.")
            case "2":
                print("You selected Radio.")
            case "3":
                print("You selected Recorder.")
            case "4":
                print("You selected Track list.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def clock():
    while True:
        print("\n===== CLOCK =====")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date settings")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("You selected Alarm clock.")
            case "2":
                print("You selected Clock settings.")
            case "3":
                print("You selected Date settings.")
            case "4":
                print("You selected Stopwatch.")
            case "5":
                print("You selected Countdown timer.")
            case "6":
                print("You selected Auto update of date and time.")
            case "99":
                return
            case _:
                print("Invalid choice.")


def simple_menu(title):
    while True:
        print(f"\n===== {title.upper()} =====")
        print("99. Home")

        choice = input("Enter your choice: ")

        match choice:
            case "99":
                return
            case _:
                print("Invalid choice.")


def main_menu():
    while True:
        print("\n========== NOKIA MENU ==========")
        print("1. Phone book")
        print("2. Messages")
        print("3. Chat")
        print("4. Call register")
        print("5. Tones")
        print("6. Settings")
        print("7. Call divert")
        print("8. Music")
        print("9. Games")
        print("10. Calculator")
        print("11. Reminder")
        print("12. Clock")
        print("13. Profiles")
        print("14. Services")
        print("15. SIM services")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                phone_book()
            case "2":
                messages()
            case "3":
                simple_menu("Chat")
            case "4":
                call_register()
            case "5":
                tones()
            case "6":
                settings()
            case "7":
                simple_menu("Call divert")
            case "8":
                music()
            case "9":
                simple_menu("Games")
            case "10":
                simple_menu("Calculator")
            case "11":
                simple_menu("Reminder")
            case "12":
                clock()
            case "13":
                simple_menu("Profiles")
            case "14":
                simple_menu("Services")
            case "15":
                simple_menu("SIM services")
            case "0":
                print("Thank you for using Nokia!")
                return
            case _:
                print("Invalid choice. Try again.")


main_menu()

