from simplegmail.query import construct_query
import os


class Scenario:
    """

    A Class for handaling a scenario for automating gmail actions

    """

    def __init__(self, gmail, name: str, **kwrgs):
        self.name = name

        # construct the query params from kwrgs dictionary:
        query_params = kwrgs.pop("query_params")
        months_back = query_params.pop("months_back")
        query_params["newer_than"] = (months_back, "month")

        self.query_params = query_params

        self.messages = gmail.get_messages(query=construct_query(query_params))


class Downloader(Scenario):
    """

    A Class for scenarios that are ment to download any content from gmail messages.
    Use only through subclasses AttDownloader or

    """

    BASE_PATH = "./saves"

    def __init__(self, gmail, name: str, base_path: str = BASE_PATH, **kwrgs):
        self.base_path = base_path
        super().__init__(gmail, name, **kwrgs)

    @staticmethod
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


class AttDownloader(Downloader):
    """

    A Class for scenarios that are ment to download

    """

    BASE_PATH = Downloader.BASE_PATH

    def __init__(self, gmail, name: str, base_path: str = BASE_PATH, **kwrgs):
        super().__init__(gmail, name, base_path, **kwrgs)
        self.download_attachments()

    def download_attachments(self):
        for message in self.messages:
            if message.attachments:
                month = message.date[5:7]
                year = message.date[0:4]
                # path = BASE_PATH
                # path = f"{self.base_path}/{year}_{month}"
                path = f"{self.base_path}"
                if self.check_if_path_exists_or_create(path):
                    for attm in message.attachments:
                        # print("File: " + attm.filename)
                        attm.save(
                            filepath=(
                                f"{path}/"
                                f"{year}"
                                "_"
                                f"{month}"
                                " "
                                f"{self.name}"
                                f"{attm.filename[-4:]}"
                            )
                        )
