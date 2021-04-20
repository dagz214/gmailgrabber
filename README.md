# GmailGrabber

An automation tool that utilizes the [simplegmail](https://github.com/jeremyephron/simplegmail) repo. The goal was/is to enable downloading and manipulating email attachments that are repetitive in nature such as bills. The goal now has expanded to more automation possibilities such as deleting, tagging, etc, and all with a very simple ```.yaml``` input.  
Please join and contribute!

## Use Case

Let's say you need to get all your receipts from Microsoft, from the last 6 months, and send it to your accountant.
You have a Microsoft 365 Standard account + a Microsoft 365 Basic account.
Fetch all of those receipts with this SIMPLE ```.yaml```:

```yaml
- Office 365 Basic:
    scenario_class: attdownloader
    query_params:
      sender: microsoft-noreply@microsoft.com
      attachment: True
      exact_phrase: microsoft 365 business basic
      months_back: 6
      
- Office 365 Standart:
    scenario_class: attdownloader
    query_params:
      sender: microsoft-noreply@microsoft.com
      attachment: True
      exact_phrase: microsoft 365 business standard
      months_back: 6
```

This would not only download your attachment, but will also rename the files to easy to understandable, and date-sortable filenames.

## Usage

1. Create ```client_secret.json``` and ```gmail_token.json``` file as described in [simplegmail](https://github.com/jeremyephron/simplegmail) GitHub documentation

2. Add a ```scenarios.yaml``` file with a structure similar to the example in ```scenarios.ADD_HERE.yaml```

## Todo

- [ ] Add ability to scrape links from messages that contains links to download document class ```linkDownloder(Downloader)```
- [ ] Implement seamlessly all the time related queries link in [simplegmail/query.py](https://github.com/jeremyephron/simplegmail/blob/master/simplegmail/query.py).
- [ ] Add templating for filenames.
- [ ] Other functionality, for example: delete emails from ```sender older than X months```
- [ ] Add ability to remove un-needed pages from pdf downloaded attachment, and save original alongside the manipulated pdf file.
- [ ] Add ability to remove passwords from documents where not needed.
