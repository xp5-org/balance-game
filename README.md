### Info
Python3 Selenium test for 2x 3x3 balance-game grid

Scenario: 
- Given 9 entries (Gold Bars), one entry weighs less than the others. 
- All gold bars are of unknown weight. 
- 8 out of the 9 bars weigh exactly the same. 


Objective: 
- Determine and test which gold bar weighs less than the rest

### easy-mode demo
Visit my REPL.it instance to view a live demo in a working x11-vnc browser environment:  
This is my link](https://repl.it/@qcm/REPL-Selenium-Balance-Solver)



### Requires

apt packages:
`python3
python3-pip
google-chrome`

Pip3 packages:
`selenium
selenium_manager`


### Setup

git clone command
`git clone https://github.com/xp5-org/balance-game.git`

check if chrome is installed
```bash
user@user:~$ google-chrome --version
Google Chrome 87.0.4280.88 
```

if it isnt  (Ubuntu/debian steps:)
`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
`sudo apt install ./google-chrome-stable_current_amd64.deb`

check if python3 is installed:
```bash
user@user:~$ python3 --version
Python 3.8.5
```

install python dependencies (pip3 packages:
`python3 -m pip install -r requirements.txt`


### Execute
As a non-root user (chrome does not like running-as-root), start the main.py file with python3 - output will be printed to the console.  if the client has a graphical environment, main.py can be edited to remove --headless-mode to view the browser window 

Running as headless: 
`$ python3 main.py`


```bash
user@user:~/PycharmProjects/balance-game$ python3 main.py
[WDM] - Current google-chrome version is 87.0.4280
[WDM] - Get LATEST driver version for 87.0.4280
[WDM] - Driver [/home/user/.wdm/drivers/chromedriver/linux64/87.0.4280.88/chromedriver] found in cache
main.py:38: DeprecationWarning: use options instead of chrome_options
  driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
Connecting to URL:  http://ec2-54-208-152-154.compute-1.amazonaws.com/
unexpected alert open: {Alert text : Yay! You find it!}
  (Session info: headless chrome=87.0.4280.88)
bar_select: Success


===============================
first run values:
entered value L - R :  [0, 1, 2] [3, 4, 5]
Game Result: Pass 1:  [0,1,2] < [3,4,5]
Output: secondrun_input_left:  [0, 1]
Output: secondrun_input_right  [2, 3]


second run values:
Game Result: Pass 2:  [1,2] > [0,3]
Output: secondrun_smallerlist:  [[0, 3]]
Output: secondrun_largerlist:  [[1, 2]]


third run values:
Game Result: Pass 3:  [3,1] > [0,2]
Output: thirdrun_smallerlist:  [[0, 2]]
Output: thirdrun_largerlist:  [[3, 1]]


Final Decision: bar 0 is the fake gold bar
===============================

```


