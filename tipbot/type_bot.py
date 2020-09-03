from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def bot():  # automatically finishes the type test but you cant share the highscore because the bot gets detected
    driver = webdriver.Chrome("C:/Users/lukas.kraft.SW/Desktop/Selenium/chromedriver.exe")  # chromedriver path
    driver.get("https://10fastfingers.com/typing-test/german")  # website the bot will work on
    time.sleep(10)  # short break so the website can load properly

    for x in range(1, 330):
        timer = driver.find_element_by_xpath('//*[@id="timer"]').text

        if str(timer) != "0:01":  # keeps track of the timer. The program stops if timer == 0:01
            try:
                word = driver.find_element_by_xpath('//*[@id="row1"]/span[{}]'.format(x)).text  # scrapes for the word
                inputfield = driver.find_element_by_xpath('//*[@id="inputfield"]')  # searches for the inputbox
                inputfield.send_keys(word + " ")  # enters the word into the input box and a "space" to send the word
            except:
                print("no more words")
                break

        else:
            print("bot stopped")  # stops the bot after the one minute time ran out
            break

    time.sleep(200)  # gives you time to admire your highscore


def undetectedbot():  # slower than the other bot but much cooler
    driver = webdriver.Chrome("C:/Users/lukas.kraft.SW/Desktop/Selenium/chromedriver.exe")  # chromedriver path
    driver.get("https://10fastfingers.com/typing-test/german")  # website the bot will work on
    time.sleep(10)  # short break so the website can load properly

    for x in range(1, 330):
        timer = driver.find_element_by_xpath('//*[@id="timer"]').text

        if str(timer) != "0:01":  # keeps track of the timer. The program stops if timer == 0:01
            word = driver.find_element_by_xpath('//*[@id="row1"]/span[{}]'.format(x)).text  # scrapes for the word
            inputfield = driver.find_element_by_xpath('//*[@id="inputfield"]')  # searches for the inputbox

            for letter in word:  # enters every letter of the searched word one by one
                inputfield.send_keys(letter)
            inputfield.send_keys(" ")

        else:
            print("bot stopped")  # stops the bot after the one minute time ran out
            break

    time.sleep(200)  # gives you time to admire your highscore


undetectedbot()