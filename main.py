# -*- coding: utf8 -*-
from simplegmail import Gmail

import yaml

from gmailgrabber import AttDownloader

gmail = Gmail()

# load the external scenarios yaml file
with open(r".\scenarios.yaml", encoding="utf8") as file:
    scenarios_constructors = yaml.load(file, Loader=yaml.FullLoader)


scenarios = []
for sc in scenarios_constructors:
    scenarios.append(AttDownloader(gmail, list(sc.keys())[0], **list(sc.values())[0]))
