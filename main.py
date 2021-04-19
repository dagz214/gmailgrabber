from simplegmail import Gmail
from simplegmail.query import construct_query
import os

BASE_PATH = "."


def check_if_path_exists_or_create(path: str) -> bool:
    """
    Check if a directory exists, and if not create it.

    Args:
        path: the path to check and create

    """
    if os.path.exists(path):
        return True
    else:
        os.mkdir(path)
        return True


def get_messages(gmail, download=True, **kwargs):
    """

    Main function to get messages and download attchments.

    Args:
        gmail: simplegmail.Gmail instance
        download (bool): determines if attachments are involved in the process
        **kwargs: query parameters as defined in the simplegmail documentation
        
    """
    query_params = {}
    for key, value in kwargs.items():
        query_params[key] = value

    messages = gmail.get_messages(query=construct_query(query_params))

    # check if attachment should be download an iterate messages:
    if download == True:
        for message in messages:
            download_attachments(message)

    return messages


def download_attachments(message):
    if message.attachments:
        for attm in message.attachments:
            print("File: " + attm.filename)
            attm.save()


gmail = Gmail()
messages = get_messages(
    gmail,
    download=True,
    newer_than=(3, "month"),
    sender="microsoft-noreply@microsoft.com",
    attachment=True,
)
# messages = get_microsoft_invoices(gmail)
# check_if_path_exists_or_create(f'{BASE_PATH}/saves/')
# download_attachments(messages)
# # Unread messages in your inbox
# messages = gmail.get_unread_inbox()

# # Starred messages
# messages = gmail.get_starred_messages()

# # ...and many more easy to use functions can be found in gmail.py!

# # Print them out!
# for message in messages:
#     print("To: " + message.recipient)
#     print("From: " + message.sender)
#     print("Subject: " + message.subject)
#     print("Date: " + message.date)
#     print("Preview: " + message.snippet)

#     print("Message Body: " + message.plain)  # or message.html
