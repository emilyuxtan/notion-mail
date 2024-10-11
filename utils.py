from notion_client import Client
from datetime import datetime
from config import NOTION_API_KEY, DATABASE_ID

notion = Client(auth=NOTION_API_KEY)

def send_message(sender, recipient, message):
    try:
        response = notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "Message": {"title": [{"text": {"content": message}}]},
                "Sender": {"rich_text": [{"text": {"content": sender}}]},
                "Recipient": {"rich_text": [{"text": {"content": recipient}}]},
            }
        )
        print(f"Message from {sender} to {recipient} sent successfully!\n")
    
    except Exception as e:
        print(f"Error sending message: {e}\n")


def read_messages(recipient):
    try:
        query = {
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Recipient",
                "rich_text": {"contains": recipient}
            }
        }
        response = notion.databases.query(**query)
        results = response.get("results", [])
        
        if results:
            print(f"\nMessages for {recipient}:\n")
            for result in results:
                formatted = format_message(result)
                print(f"  From: {formatted['sender']}\n  Message: {formatted['message']}\n  Sent: {formatted['timestamp']}\n")
        else:
            print(f"No messages found for {recipient}.\n")
    
    except Exception as e:
        print(f"Error reading messages: {e}\n")


def delete_message(sender=None, recipient=None, message=None):
    try:
        filters = []
        
        if sender:
            filters.append({
                "property": "Sender", 
                "rich_text": {
                    "contains": sender
                }
            })
        if recipient:
            filters.append({
                "property": "Recipient", 
                "rich_text": {
                    "contains": recipient
                }
            })
        if message:
            filters.append({
                "property": "Message", 
                "title": {
                    "contains": message
                }
            })
        
        if not filters:
            print("Please specify at least one of sender, recipient, or message content.\n")
            return
        
        query = {
            "database_id": DATABASE_ID,
            "filter": {"and": filters}
        }

        response = notion.databases.query(**query)
        results = response.get("results", [])

        if not results:
            print("No matching messages found.\n")
            return

        if len(results) == 1:
            result = results[0]
            formatted = format_message(result)
            print(f"Found one match\n   From: {formatted['sender']}\n   To: {formatted['recipient']}\n   Message: {formatted['message']}\n   Sent: {formatted['timestamp']}\n")
            
            confirm = input(f"Do you want to delete this message? [y/n]: ").strip().lower()

            if confirm == 'y':
                notion.blocks.delete(block_id=message_id)
                print(f"Message from {formatted['sender_name']} to {formatted['recipient_name']} deleted successfully.\n")
            
            elif confirm == 'n':
                print("Deletion canceled; no message was deleted.\n")
            
            else:
                print("Invalid choice. No messages were deleted.\n")

        else:
            print(f"\nFound {len(results)} matching messages:\n")

            for idx, result in enumerate(results, 1):
                formatted = format_message(result)
                print(f"{idx}. From: {formatted['sender']}\n   To: {formatted['recipient']}\n   Message: {formatted['message']}\n   Sent: {formatted['timestamp']}\n")
            
            choice = int(input(f"Enter the number of the message you want to delete (1-{len(results)}), or 0 to delete all: "))
            
            if choice == 0:
                confirm_all = input(f"Are you sure you want to delete all {len(results)} messages? [y/n]: ").strip().lower()
                if confirm_all == 'y':
                    for result in results:
                        message_id = result["id"]
                        notion.blocks.delete(block_id=message_id)
                    print(f"All {len(results)} messages deleted successfully.\n")
                else:
                    print("Deletion was canceled. No messages were deleted.\n")
            
            elif 1 <= choice <= len(results):
                message_id = results[choice - 1]["id"]
                notion.blocks.delete(block_id=message_id)
                print(f"Message {choice} deleted successfully.\n")
            
            else:
                print("Invalid choice. No messages were deleted.\n")

    except Exception as e:
        print(f"Error deleting message: {e}\n")



def format_message(result):
    sender_name = result["properties"]["Sender"]["rich_text"][0]["text"]["content"]
    recipient_name = result["properties"]["Recipient"]["rich_text"][0]["text"]["content"]
    msg_content = result["properties"]["Message"]["title"][0]["text"]["content"]
    timestamp = result["properties"]["Timestamp"]["created_time"]
    timestamp_obj = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    formatted_timestamp = timestamp_obj.strftime("%B %d, %Y at %I:%M %p UTC")

    return {
        "sender": sender_name,
        "recipient": recipient_name,
        "message": msg_content,
        "timestamp": formatted_timestamp
    }


def print_menu():
    print("\nOptions:")
    print("- send: Send a message to a user.")
    print("- read: Read message(s) for a user.")
    print("- delete: Delete specific message(s)")
    print("- exit: Exit Notion Mail")
