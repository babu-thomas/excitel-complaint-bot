# Excitel Complaint Bot

## What
A Python script I wrote to automate the lodging of complaints at [Excitel's website](https://my.excitel.com/). Excitel is my Internet Service Provider.

## Usage
### Requirements
1. [Selenium Python Bindings](https://selenium-python.readthedocs.io/installation.html). Install using pip:
```
pip install selenium
```
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
3. Google Chrome browser

Note: Other browsers will work too. But will need some modifications in the code. More details [here](https://selenium-python.readthedocs.io/installation.html#drivers).

### How to use
`$ python complain.py --help`

```
usage: python complain.py [-h] [--headless] [username] [password]

A script to automate the logding of complaints at "https://my.excitel.com".
Takes username and password as command line arguments. If they are not present
looks for a file named "creds" in the current directory. The first line in
that file is taken as the username and the second line is taken as the
password.

positional arguments:
  username    Excitel username
  password    Excitel password

optional arguments:
  -h, --help  show this help message and exit
  --headless  Use Chrome in headless mode
```

## Why
Sadly, my internet connection is down so much that I had to make this to lodge complaints quickly.

## Resources
- [XPath Cheatsheet](https://devhints.io/xpath)
- [Selenium documentation](https://selenium-python.readthedocs.io/index.html)
- Chrome extension to show XPath of any element on a webpage - [XPath Helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)
