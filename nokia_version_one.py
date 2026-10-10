
print("===== NOKIA MENU =====")
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

choice = input("\nEnter your choice: ")

match choice:

    case "1":
        print("\n--- Phone book ---")
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

    case "2":
        print("\n--- Messages ---")
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

    case "3":
        print("\n--- Chat ---")

    case "4":
        print("\n--- Call register ---")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("6. Show call cost")
        print("7. Call cost settings")
        print("8. Prepaid credit")

    case "5":
        print("\n--- Tones ---")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Message alert tones")
        print("5. Keypad tones")
        print("6. Warning tones")
        print("7. Vibrating alert")
        print("8. Screen saver")

    case "6":
        print("\n--- Settings ---")
        print("1. Call settings")
        print("2. Phone settings")
        print("3. Security settings")
        print("4. Restore factory settings")

    case "7":
        print("\n--- Call divert ---")

    case "8":
        print("\n--- Music ---")
        print("1. Music player")
        print("2. Radio")
        print("3. Recorder")
        print("4. Track list")

    case "9":
        print("\n--- Games ---")

    case "10":
        print("\n--- Calculator ---")

    case "11":
        print("\n--- Reminder ---")

    case "12":
        print("\n--- Clock ---")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("3. Date settings")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Auto update of date and time")

    case "13":
        print("\n--- Profiles ---")

    case "14":
        print("\n--- Services ---")

    case "15":
        print("\n--- SIM services ---")

    case _:
        print("\nInvalid choice. Please select a number from 1 to 15.")

