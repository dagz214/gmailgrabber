# gmailGrabber [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Get%20control%20of%20your%20Gmail%20account%204&url=https://github.com/dagz214/gmailgrabber&hashtags=gmail,python,github,developers) 


An automation tool that utilizes the [simplegmail](https://github.com/jeremyephron/simplegmail) repo. The goal was/is to enable downloading and manipulating email attachments that are repetitive in nature such as bills. The goal now has expanded to more automation possibilities such as deleting, tagging, etc, and all with a very simple ```.yaml``` input.  
Please join and contribute!

## Use Cases


### Downloading Attachments

Let's say you need to get all your receipts from Microsoft, from the last 6 months, and send it to your accountant.
You have a Microsoft 365 Standard account + a Microsoft 365 Basic account.
Fetch all of those receipts with this SIMPLE ```.yaml```:

```yaml
- Hooli un-needed items:
    scenario:
      - send to trash
    query_params:
      - sender: no_replies@hooli.com
      - older_than: [45, day]
      - or:
          exact_phrase: 
              - Hello Mr. Belson, Your daily report from Hooli.com services is ready
              - Hooli newsletter - Get the most out of your Hooli.com account

- Hooli manage monthly report:
    scenario:
      - mark as important
      - mark as ready
    query_params:
      - sender: no_replies@hooli.com
      - exact_phrase: Your monthly report from Hooli.com is here
```

This would not only download your attachment, but will also rename the files to easy to understand, and date-sortable filenames.

### Keeping Your Inbox Tidy

gmailGrabber Can use multiple actions in scenarios, and also query using and/or for parameters that are not booleans. 
Lets consider a scenario that we have a subscription to a service that sends us periodically the following reports:

1. Once a day - a very long and detailed report
2. Once a month - a monthly summery of all the events in the daily reports.
3. Every once in a while - a newsletter with tips and tricks.

In this example, I decided I want to keep the monthly summaries in my mailbox for good. The daily reports and the newsletter are useless for me in the long term, so I've decided to keep them only for 45 days.  
Also I want all of the monthly reports to be marked as 'Read' and 'Important'.  
I will add this to ```scenarios.yaml```:

```yaml
- Hooli - un-needed items:
    scenario:
      - send to trash
    query_params:
      - sender: no_replies@hooli.com
      - older_than: [45, day]
      - or:
          exact_phrase: 
              - Hello Mr. Belson, Your daily report from Hooli.com services is ready
              - Hooli newsletter - Get the most out of your Hooli.com account

- Hooli - manage monthly report:
    scenario:
      - mark as important
      - mark as ready
    query_params:
      - sender: no_replies@hooli.com
      - exact_phrase: Your monthly report from Hooli.com is here
```

Notice the structure of the 'or' parameter, every message that will contain at least one of the phrases in the 'exact_phrase' dictionary - will be returned.

Additional functionality for ```query_params``` mentioned in [simplegmail/query.py](https://github.com/jeremyephron/simplegmail/blob/master/simplegmail/query.py). Not all options have been implemented yet in gmailGrabber.

## Usage

1. ```https://github.com/dagz214/gmailgrabber.git```

2. ```pip install -r requirements.txt```

1. Create ```client_secret.json``` and ```gmail_token.json``` file as described in [simplegmail](https://github.com/jeremyephron/simplegmail) GitHub documentation

2. Add a ```scenarios.yaml``` file with a structure similar to the example in ```scenarios.ADD_HERE.yaml```

3. Until better implementation is developed, could be used with "Task Scheduler" in Windows or cron in other operating systems.

## Todo

- [ ] Add ability to scrape links from messages that contains links to download document
- [ ] Add templating for filenames.
- [ ] Add ability to remove un-needed pages from pdf downloaded attachment, and save original alongside the manipulated pdf file.
- [ ] Add ability to remove passwords from documents where not needed.
- [ ] Labels management.
