# Excitel Complaint Bot

## What
A Python script I wrote to automate the lodging of complaints at [Excitel's website](https://my.excitel.com/). Excitel is my Internet Service Provider.

## Usage
### Requirements
1. [Selenium Python Bindings](https://selenium-python.readthedocs.io/installation.html). Install using pip:
```
pip install selenium
```
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (included in this repository)
3. Google Chrome browser

Note: Other browsers will work too. But will need some modifications in the code. More details [here](https://selenium-python.readthedocs.io/installation.html#drivers).

### How to use
```
python complain.py [-h] [--headless] username password

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
