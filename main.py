# -*- coding: utf8 -*-
from simplegmail import Gmail

import yaml
from gmailgrabber import Scenario

gmail = Gmail()

# load the external scenarios yaml file
with open(r".\scenarios.yaml", encoding="utf8") as file:
    scenarios_constructors = yaml.load(file, Loader=yaml.FullLoader)


scenarios = []
for sc in scenarios_constructors:
    scenario_name=list(sc.keys())[0]
    scenario_kwrgs=list(sc.values())[0]
    scenarios.append(Scenario(gmail, scenario_name, **scenario_kwrgs))
