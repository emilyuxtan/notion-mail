# NotionMail CLI

## Description

**NotionMail CLI** is a command-line application that allows users to send, read, and delete messages directly in a connected database by through Notion’s API. This application stores sender names, recipient names, and messages in the Notion databases, simulating a basic mail system.

### Core Features:
- **Send Messages:** Users can send messages from one user to another by specifying the sender’s name, recipient’s name, and message content. The date and time the message was sent is automatically generated into the database. 
- **Read Messages:** Users can read all the messages sent to a specified recipient

  
### Additional Improvements:
- **Delete Messages:** Users can delete messages by filtering by sender, recipient, or keywords in the message's content. All matches are listed,and users can choose to delete one or all matched messages.
- **Timestamp Formatting:** The timestamp of each message is formatted to mimic Notion’s date format (e.g., "October 10, 2024 at 10:18 PM").
- **Confirmation Prompts for Deletion:** To prevent accidental deletion, confirmation prompts were added. Users must confirm before deleting a message or all matched messages.



## Installation and Setup

### Prerequisites
To run NotionMail CLI, you need:
- **Python 3.6+** installed on your machine.
- A **Notion Integration** with access to a specific database for storing the messages.
- Your **Notion API Key** and **Database ID**.
- This official Notion tutorial may be helpful: [Build your first integration](https://developers.notion.com/docs/create-a-notion-integration#next-steps)

### Installation Steps

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/emilyuxtan/notion-mail.git
   cd notion-mail

2. **Install required dependencies**
   
   ```bash
   pip install -r requirements.txt

3. **Set up your environment variables in .env**
   
   ```bash
   NOTION_KEY=<your_notion_api_key>
   NOTION_PAGE_ID=<your_database_id>

4. **Run the program**
   
   ```bash
   python3 main.py

## References and Resources

### Official Notion Resources
- [Build your first integration](https://developers.notion.com/docs/create-a-notion-integration#next-steps)
- [Notion SDK in Python](https://github.com/ramnes/notion-sdk-py)
- [Working with databases](https://developers.notion.com/docs/working-with-databases)
- [Property values](https://developers.notion.com/reference/property-value-object#title-property-values)

### Other References
- [Notion API Crash Course](https://thomasjfrank.com/notion-api-crash-course/#what-is-the-notion-api)
- [Using Python Environment Variables with python dotenv](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/)
- [Python datetime formatting](https://stackoverflow.com/questions/55021984/python-3-how-to-format-to-yyyy-mm-ddthhmmssz)


## Future Improvements

1. **Comprehensive Test Suite**

   Develop a complete test suite to ensure that all functionality, including message sending, reading, deleting, and error handling, work as expected under various conditions, espeically edge cases.



2. **Read/Unread Status**

   Implement a system to mark messages as read or unread using a single select property, allowing users to track which messages they’ve already viewed.



3. **Check New Messages**

   Add a feature to show only unread messages when a user logs in, improving efficiency by highlighting new, unread communications.



4. **Access Control**

   Introduce user-specific authentication (eg: with a username) to restrict message access, ensuring users can only send and view messages associated with their own username.



5. **Support for Drafts**

   Allow users to save messages as drafts that can be edited or sent later (eg: by adding a draft tag property) for increased functionality



6. **Message Forwarding**

   Enable users to forward received messages to other users, improving flexibility in message sharing and collaboration.



7. **Tagging Organization System**

   Create a tagging system where users can label messages (e.g., "Work", "Personal", "Urgent") to help organize and filter messages based on categories.


8. **Read message improvements**

   Currently lack advanced filters for searching messages (e.g., searching by date range, tags, or keywords within the message body); implement advanced search features to make the application more powerful and user-friendly



## Product and Technical Decisions
Several product and technical choices were made during development:

1. **Continuous Execution:**

   The CLI runs in a loop, allowing users to perform multiple actions without restarting the program, thus streamlining the user experience. A straightforward exit option was also added, allowing users to cleanly exit the program once they have finished. 


2. **Confirmation for Deletion:**

   Deleting messages is a destructive action, so confirmation prompts were added to ensure that users don’t accidentally delete important messages.


3. **Dependency Management:**

   The program uses python-dotenv to handle environment variables securely to avoid exposing sensitive information, like the Notion API key, directly in the code.


## Contributions and Feedback

Contributions to NotionMail CLI are welcome! Feel free to get involved, whether it be reporting bugs, submitting PRs, etc. Any feedback or ideas for future improvements will help make this project better.

Thank you for checking out NotionMail CLI, and we hope it helps you manage your messages!