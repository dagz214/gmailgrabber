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
    scenario_name=list(sc.keys())[0]
    scenario_kwrgs=list(sc.values())[0]

    scenario_class=sc[scenario_name].pop('scenario_class')
    
    if scenario_class=='attdownloader':
        scenarios.append(AttDownloader(gmail, scenario_name, **scenario_kwrgs))
    elif 1==2:
        pass
    else:
        print(f'The scenario {scenario_name} did not matched any scenario class and was not processed')
