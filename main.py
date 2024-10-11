from utils import send_message, read_messages, delete_message, print_menu

def main():
    # flag to check if the program is being run for the first time
    first_time = True
    
    while True:
        # display welcome message and menu if it's the user's first time running the program
        if first_time:
            print("\n* * * * * * * * * * *\n")
            print("Welcome to NotionMail!")
            print_menu()
            first_time = False
        else:
            continue_prompt = input("Is there anything else NotionMail can help you with? [y/n]: ").strip().lower()
            if continue_prompt == "n": # exit the program
                print("\nThank you for using NotionMail. Take care!")
                print("\n* * * * * * * * * * * * * * * * * * * * *\n")
                break
            elif continue_prompt != "y": # if input isn't 'y' or 'n', return back to main menu
                print("Invalid command! Returning to the main menu")
            
            print_menu()

        command = input("\nPlease choose an option: ")
        
        if command == "exit":
            print("\nThank you for using NotionMail. Take care!")
            print("\n* * * * * * * * * * * * * * * * * * * * *\n")
            break

        elif command == "send":
            sender = input("\nEnter your name: ")
            recipient = input("Enter recipient's name: ")
            message = input("Enter your message: ")
            # Potential improvement: could add input validation here to ensure that 'sender', 'recipient', and 'message'
            # are not empty, and handle cases where the user provides invalid input (e.g., only spaces).
            send_message(sender, recipient, message)

        elif command == "read":
            recipient = input("\nEnter the recipient's name: ")
            # Edge case: handles if the user enters an empty recipient name or a recipient that doesn't exist.
            read_messages(recipient)
        
        elif command == "delete":
            sender = input("\nEnter the sender's name, or leave blank: ") or None
            recipient = input("Enter recipient's name, or leave blank: ") or None
            message = input("Enter a specified keyword, or leave blank: ") or None
            delete_message(sender, recipient, message)

        else:
            print("\nInvalid command! Please choose either 'send', 'read', or 'delete'.")

if __name__ == "__main__":
    main()
