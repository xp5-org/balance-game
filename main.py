from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import time



url = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')   # comment this line out to get browser GUI
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get(url)
print(driver.title)
print(driver.current_url)


# static init stuff, game looks like this
A = [0,1,2]
B = [3,4,5]
C = [6,7,8]

# lists
firstrun_goodlist = []
firstrun_badlist = []
secondrun_input_left = []
secondrun_input_right = []
secondrun_smallerlist = []
secondrun_largerlist = []
thirdrun_smallerlist = []
thirdrun_largerlist = []
gameoutput = []






def weighfirstround():
    # A VS B
    # A = (0, 1, 2)
    # B = (3, 4, 5,)

    # A goes to left top 3
    box0 = driver.find_element_by_id("left_0")
    box0.send_keys(A[0])
    box2 = driver.find_element_by_id("left_1")
    box2.send_keys(A[1])
    box3 = driver.find_element_by_id("left_2")
    box3.send_keys(A[2])

    # B goes to right top 3
    box1 = driver.find_element_by_id("right_0")
    box1.send_keys(B[0])
    box1 = driver.find_element_by_id("right_1")
    box1.send_keys(B[1])
    box1 = driver.find_element_by_id("right_2")
    box1.send_keys(B[2])

    # weigh it
    weigh = driver.find_element_by_id("weigh")
    weigh.click()

    # get result
    result = driver.find_element_by_xpath("//div[contains(@class, 'game-info')]")
    #print(str(result.text))
    if '>' in str(result.text):
        #print('DEBUG: weighfirstround: greater than found, B has the fake bar')
        firstrun_badlist.append(B)
        firstrun_goodlist.append(A)
        firstrun_goodlist.append(C)
        return
    if '<' in str(result.text):
        #print('DEBUG: weighfirstround: less than found, A has the fake bar')
        firstrun_badlist.append(A)
        firstrun_goodlist.append(B)
        firstrun_goodlist.append(C)

        return
    if '=' in str(result.text):
        #print('DEBUG: weighfirstround: equals found, C has the fake bar')
        firstrun_goodlist.append(A)
        firstrun_goodlist.append(B)
        firstrun_badlist.append(C)
        return
    return result


def weighsecondround(val1, val2):
    # find if val1 is less than or greater than val2
    # put val1 into smaller list if its smaller

    # val1 goes to left top 3
    leftbox = []
    box0 = driver.find_element_by_id("left_0")
    box0.send_keys(Keys.BACKSPACE)
    print('sending',  val1[1])
    box0.send_keys(str(val1[1]))
    leftbox.append(val1[1])
    box0 = driver.find_element_by_id("left_1")
    box0.send_keys(Keys.BACKSPACE)
    box0.send_keys(str(val2[0]))
    leftbox.append(val2[0])
    box0 = driver.find_element_by_id("left_2")
    box0.send_keys(Keys.BACKSPACE)

    # val2 goes to right top 3
    rightbox = []
    box1 = driver.find_element_by_id("right_0")
    box1.send_keys(Keys.BACKSPACE)
    box1.send_keys(str(val1[0]))
    rightbox.append(val1[0])
    box1 = driver.find_element_by_id("right_1")
    box1.send_keys(Keys.BACKSPACE)
    box1.send_keys(str(val2[1]))
    rightbox.append(val2[1])
    box1 = driver.find_element_by_id("right_2")
    box1.send_keys(Keys.BACKSPACE)
    weigh = driver.find_element_by_id("weigh")
    weigh.click()
    result = driver.find_element_by_xpath("//div[contains(@class, 'game-info')]")
    print('second time result: ,', str(result.text))

    multiline = result.text.split('\n')
    print('value of secondrun multiline: ', multiline[2])

    if '>' in multiline[2]:
        print('2rd run: left box greater than righter - boxleft value is: - ', leftbox)
        secondrun_largerlist.append(leftbox)  # val1 in boxleft is greater than val2
        secondrun_smallerlist.append(rightbox)  # val2 in boxright is less than val1
        return
    if '<' in multiline[2]:
        print('2rd run: left box less than right box')
        secondrun_largerlist.append(rightbox)  # val2 in boxright is greater than val1
        secondrun_smallerlist.append(leftbox)  # val1 in boxleft is less than val2
        return
    if '=' in multiline[2]:
        print('error - they are the same')
        return
    return


def weighthirdround(val1, val2):
    # A VS B
    # D = ('0', '1', '2',)
    # E = ('3', '4', '5',)

    #clear = driver.find_element_by_id("reset") # doesnt work
    # clear.click() # doesnt work
    #print('weighj another one function val1 debug', val1, len(val1[0]))
    #print('weighj another one function val2 debug', val2, len(val2[0]))

   # print('val2,1, ', val2[1])

    # val1 goes to left top 3
    leftbox = []
    box0 = driver.find_element_by_id("left_0")
    box0.send_keys(Keys.BACKSPACE)
    #print('sending',  val1[0][1])
    box0.send_keys(str(val1[0][1]))
    leftbox.append(val1[0][1])
    box0 = driver.find_element_by_id("left_1")
    box0.send_keys(Keys.BACKSPACE)
    box0.send_keys(str(val2[0][0]))
    leftbox.append(val2[0][0])
    box0 = driver.find_element_by_id("left_2")
    box0.send_keys(Keys.BACKSPACE)

    # val2 goes to right top 3
    rightbox = []
    box1 = driver.find_element_by_id("right_0")
    box1.send_keys(Keys.BACKSPACE)
    box1.send_keys(str(val1[0][0]))
    rightbox.append(val1[0][0])
    box1 = driver.find_element_by_id("right_1")
    box1.send_keys(Keys.BACKSPACE)
    box1.send_keys(str(val2[0][1]))
    rightbox.append(val2[0][1])
    box1 = driver.find_element_by_id("right_2")
    box1.send_keys(Keys.BACKSPACE)

    weigh = driver.find_element_by_id("weigh")
    weigh.click()
    result = driver.find_element_by_xpath("//div[contains(@class, 'game-info')]")

    # looking for line with '2. ' as output grows each run need to pick 3rd row down
    # first row says "weighings"
    # second row is result1
    multiline = result.text.split('\n')
    for entry in multiline:
        gameoutput.append(entry)

    #print('value of thirdrun multiline: ', multiline[3], len(multiline))

    if '>' in multiline[3]:
        #print('3rd run: left box greater than righter - found > in output  - ', result.text)
        thirdrun_largerlist.append(leftbox) # val1 in boxleft is greater than val2
        thirdrun_smallerlist.append(rightbox) # val2 in boxright is less than val1
        return multiline
    if '<' in multiline[3]:
        #print('3rd run: left box less than right box')
        thirdrun_smallerlist.append(leftbox) # val1 in boxleft is less than val2
        thirdrun_largerlist.append(rightbox) # val2 in boxright is greater than val1
        return multiline
    if '=' in multiline[3]:
        #print('3rd run: error - they are the same')
        exit()
        return multiline
    return




def set_bad_bar():
    for element in secondrun_smallerlist[0]:
        if element in thirdrun_smallerlist[0]:
            #print('element finder debug: ', str(element))
            return str(element)


def bar_select(number):
    print('coin select input number is ', number, type(number))
    barname = 'coin_{0}'.format(number)

    try:
        barpress = driver.find_element_by_id(barname)
        barpress.click()
        barpress = driver.find_element_by_id(barname)
        alert = barpress.switch_to.alert
        alert.accept()
        alert.dismiss()

    except UnexpectedAlertPresentException as e:
        outputmsg = e.__dict__["msg"]
        print(outputmsg)
        var = 'You find it'
        if var in outputmsg:
            print('bar_select: Success')
        if var not in outputmsg:
            print('bar_select: fail')


def debug_output():
    print('\n')
    print('===============================')
    print('first run values:')
    print('entered value L - R : ',A, B)
    print('Game Result: Pass 1: ', gameoutput[1])
    print('Output: secondrun_input_left: ', secondrun_input_left)
    print('Output: secondrun_input_right ', secondrun_input_right)
    print('\n')
    print('second run values:')
    print('Game Result: Pass 2: ', gameoutput[2])
    print('Output: secondrun_smallerlist: ', secondrun_smallerlist)
    print('Output: secondrun_largerlist: ', secondrun_largerlist)
    print('\n')
    print('third run values:')
    print('Game Result: Pass 3: ', gameoutput[3])
    print('Output: thirdrun_smallerlist: ', thirdrun_smallerlist)
    print('Output: thirdrun_largerlist: ', thirdrun_largerlist)
    print('\n')
    print('Found the following in Round-2 and Round-3 smaller-lists: ', finalchoice)






# first run through
weighfirstround()
print('good: ', firstrun_goodlist, 'bad: ', firstrun_badlist)
print('num of entries in badlist0', len(firstrun_badlist[0]))

# what is going on here?
secondrun_input_left.append(firstrun_badlist[0][0])
secondrun_input_left.append(firstrun_badlist[0][1])
secondrun_input_right.append(firstrun_badlist[0][2])
secondrun_input_right.append(firstrun_goodlist[0][0])

# info
print('2 bad list: ', secondrun_input_left, secondrun_input_left[0], secondrun_input_left[1])
print('2 good list: ', secondrun_input_right)

# second run through, for some reason getting nested lists
weighsecondround(secondrun_input_left, secondrun_input_right)


# third round
weighthirdround(secondrun_smallerlist, secondrun_largerlist)


# compare 2nd run and 3rd run common entry in smaller-than output lists
finalchoice = set_bad_bar()

# click the bar num found in
bar_select(finalchoice)

debug_output()




