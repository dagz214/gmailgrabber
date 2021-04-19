from simplegmail import Gmail
from simplegmail.query import construct_query
import yaml
import os

BASE_PATH = "./saves"


def check_if_path_exists_or_create(path: str) -> bool:
    """
    Check if a directory exists, and if not create it.

    Args:
        path: the path to check and create

    """
    if os.path.exists(path):
        return True
    else:
        os.makedirs(path, exist_ok=True)
        return True


def get_messages(gmail, description, download=True, **kwargs):
    """

    Main function to get messages and download attchments.

    Args:
        gmail: simplegmail.Gmail instance
        download (bool): determines if attachments are involved in the process
        **kwargs: query parameters as defined in the simplegmail documentation
        
    """
    query_params = {}

    # get the months to look back and add to query
    months_back=kwargs.pop('months_back')
    query_params['newer_than']=(months_back, "month")

    # parse the remaining kwargs for the query
    for key, value in kwargs.items():
        query_params[key] = value

    messages = gmail.get_messages(query=construct_query(query_params))
    
    # check if attachment should be download an iterate messages:
    if download == True:
        for message in messages:
            download_attachments(message, description)

    return messages


def download_attachments(message, description):
    """

    Downloads attachments from a single message

    """
    if message.attachments:
        month=message.date[5:7]
        year=message.date[0:4]
        # path = BASE_PATH
        path = f'{BASE_PATH}/{year}_{month}'
        if check_if_path_exists_or_create(path):
            for attm in message.attachments:
                # print("File: " + attm.filename)
                attm.save(filepath=(
                    f'{path}/'
                    f'{year}'
                    '_'
                    f'{month}'
                    ' '
                    f'{description}'
                    f'{attm.filename[-4:]}'
                ))


gmail = Gmail()

#open the external profiles yaml file
with open(r'.\profiles.yaml') as file:
    profile_list = yaml.load(file, Loader=yaml.FullLoader)

for profile in profile_list:
    get_messages(gmail, list(profile.keys())[0], **list(profile.values())[0])

