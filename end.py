from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Flask application in the browser
driver.get('http://localhost:5000')

# Find input fields and submit button
heightFeet_input = driver.find_element_by_id('heightFeet')
heightInches_input = driver.find_element_by_id('heightInches')
weightPounds_input = driver.find_element_by_id('weightPounds')
submitButton = driver.find_element_by_xpath('//button[@type="submit"]')

# Enter input values
heightFeet_input.send_keys('5')
heightInches_input.send_keys('11')
weightPounds_input.send_keys('150')

# Click the submit button
submitButton.click()

# Wait for the result page to load
time.sleep(2)

# Assert the result
result_bmi = driver.find_element_by_id('result-bmi').text
assert result_bmi == '25.7'

# Close the browser
driver.quit()