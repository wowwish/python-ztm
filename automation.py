from selenium import webdriver # Drive the Web through code
from selenium.webdriver.common.by import By # For HTML Element Selectors
# IMPORTANT: To use Selenium for Automation Testing:
# Download the corresponding Browser Driver from the Selenium Documentation Page (geckodriver in our case for Mozila)
# and unzip the zip archive into the same directory where this script resides.
# REFER https://pypi.org/project/selenium/ FOR PROPER INSTALLATION
# REFER http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/ FOR THINGS YOU CAN DO WITH SELENIUM

# browser = webdriver.Firefox()
# You can also add the 'geckodriver.exe' file to another directory and add it to the PATH variable
browser = webdriver.Firefox()
print(browser)
browser.maximize_window() # Automatically Maximize the Browser Window


browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') # Automatically make Browser to go to this url

assert('Selenium Easy Demo' in browser.title) # Test if Title of the Web Page is correct
# REFER https://www.selenium.dev/documentation/webdriver/elements/finders/ for ways to get HTML elements
button = browser.find_element(By.CLASS_NAME, "btn-default") # Using Selectors to access the Page HTML tags (Class Selector in this case)
print(button)
print(button.get_attribute('innerHTML')) # Get the inner Content of the HTML Tag we just captured
assert('Show Message' in browser.page_source) # assert that 'Show Message' text is somewhere in the HTML content of the Page
# Automate typing into an input box
user_message = browser.find_element(By.ID, "user-message") # Grab the input text box
user_message.clear() # Clear any values present in the grabbed input box
user_message.send_keys('I AM COOL') # Send key strokes to the input box to mimic a user typing
# Automate clicking a button
show_message_button = browser.find_element(By.CLASS_NAME, "btn-default") # Grab the button of interest
show_message_button.click() # Simulate the click of the button that was grabbed
# Grab the displayed message
output_message = browser.find_element(By.ID, "display") 
assert('I AM COOL' in output_message.text) # Grab the text from the span and check if it is same as the user message


# Finding Elements by CSS Selectors
# Grab 'Show Message' Button from the form in the page using CSS selectors
user_button2 = browser.find_element(By.CSS_SELECTOR, "#get-input > .btn")
print(user_button2) 

# Close the Browser - call twice to make sure it closes properly
browser.close()
# browser.close()

# Close the entire Selenium Driver
browser.quit() # closes all sessions opened using the current Web Driver instance

# Pause between actions to prevent Websites from Blocking your Activity thinking you are an Illegal Bot
# Make the Web Driver wait for a few seconds
# REFER https://www.selenium.dev/documentation/webdriver/waits/ FOR IMPLEMENTING WAITS