from simplegmail.query import construct_query
import os


class Scenario:
    """

    A Class for handaling a scenario for automating gmail actions

    """

    BASE_PATH = "./saves"

    def __init__(self, gmail, name: str, base_path: str = BASE_PATH, **kwrgs):
        self.name = name
        self.base_path = base_path

        # For all keywords whose values are not booleans, you can indicate you'd
        # like to "and" multiple values by placing them in a tuple (), or "or"
        # multiple values by placing them in a list [].
        query_params = {}
        for param in kwrgs.pop("query_params"):
            if "and" in param:
                param = list(param.values())[0]
                poped = param.popitem()
                query_params.setdefault(poped[0], tuple(poped[1]))
            elif "or" in param:
                param = list(param.values())[0]
                poped = param.popitem()
                query_params.setdefault(poped[0], poped[1])

            else:
                # remove a key value pair as 2-tuple and add to query_params:
                poped = param.popitem()
                query_params.setdefault(poped[0], poped[1])

        self.query_params = query_params
        # get the query params from kwrgs dictionary:
        # self.query_params = kwrgs.pop("query_params")
        self.messages = gmail.get_messages(query=construct_query(self.query_params))
        print(
            f"the query for {self.name} has resulted in {len(self.messages)} messages"
        )

        try:
            actions = kwrgs.pop("scenario")
        except:
            pass

        func_dic = {
            "download attachment": getattr(self, "download_attachments"),
            "mark as important": getattr(self, "mark_as_important"),
            "mark as not important": getattr(self, "mark_as_not_important"),
            "star messages": getattr(self, "star"),
            "unstar messages": getattr(self, "unstar"),
            "send to trash": getattr(self, "trash"),
            "remove from trash": getattr(self, "untrash"),
            "do nothing": getattr(self, "do_nothing"),
        }
        for action in actions:
            func_dic[action]()

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

    def do_nothing(self):
        pass

    def download_attachments(self):
        for message in self.messages:
            if message.attachments:
                day = message.date[8:10]
                month = message.date[5:7]
                year = message.date[0:4]
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
                                "_"
                                f"{day}"
                                " "
                                f"{self.name}"
                                f"{attm.filename[-4:]}"
                            )
                        )

    def mark_as_important(self):
        for message in self.messages:
            message.mark_as_important()

    def mark_as_not_important(self):
        for message in self.messages:
            message.mark_as_not_important()

    def star(self):
        for message in self.messages:
            message.star()

    def unstar(self):
        for message in self.messages:
            message.unstar()

    def trash(self):
        for message in self.messages:
            message.trash()

    def untrash(self):
        for message in self.messages:
            message.untrash()
