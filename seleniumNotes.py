# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser (you can replace Chrome with Firefox, Edge, etc.)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://example.com")

# Maximize the browser window
driver.maximize_window()

# Get the page title
print(driver.title)

# Get the current URL
print(driver.current_url)

# Navigate back and forward
driver.back()  # Go to the previous page
driver.forward()  # Go to the next page

# --------- Locating elements ---------

# Locate by ID
element = driver.find_element(By.ID, "element_id")

# Locate by NAME
element = driver.find_element(By.NAME, "element_name")

# Locate by CLASS_NAME
element = driver.find_element(By.CLASS_NAME, "element_class")

# Locate by TAG_NAME
element = driver.find_element(By.TAG_NAME, "tag_name")

# Locate by LINK_TEXT (full link text)
element = driver.find_element(By.LINK_TEXT, "Full Link Text")

# Locate by PARTIAL_LINK_TEXT (partial link text)
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Link Text")

# Locate by XPATH
element = driver.find_element(By.XPATH, "//tag[@attribute='value']")

# Locate by CSS_SELECTOR
element = driver.find_element(By.CSS_SELECTOR, "tag.classname")

# --------- Interacting with elements ---------

# Type text in an input field
element.send_keys("Sample text")

# Simulate a keyboard key (ENTER, TAB, etc.)
element.send_keys(Keys.ENTER)

# Click a button or link
element.click()

# Clear an input field
element.clear()

# --------- Waits ---------

# Implicit wait (general wait)
driver.implicitly_wait(10)  # Wait up to 10 seconds

# Explicit wait (wait for specific conditions)
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "element_id"))
)

# --------- Screenshots ---------

# Take a screenshot
driver.save_screenshot("screenshot.png")

# --------- Handling alerts ---------

# Accept an alert
alert = driver.switch_to.alert
alert.accept()

# Dismiss an alert
alert.dismiss()

# Get the text of an alert
alert_text = driver.switch_to.alert.text

# --------- Handling windows and tabs ---------

# Get the current window handle
main_window = driver.current_window_handle

# Switch to a new window
driver.switch_to.window(driver.window_handles[1])

# Close the current window
driver.close()

# --------- Handling iframes ---------

# Switch to an iframe
driver.switch_to.frame("iframe_id")

# Exit the iframe and return to the main content
driver.switch_to.default_content()

# --------- Handling cookies ---------

# Get all cookies
cookies = driver.get_cookies()

# Add a cookie
driver.add_cookie({"name": "test", "value": "12345"})

# Delete a specific cookie
driver.delete_cookie("test")

# Delete all cookies
driver.delete_all_cookies()

# --------- Handling JavaScript ---------

# Execute a JavaScript script on the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# --------- Closing the browser ---------

# Close the current tab
driver.close()

# Close all windows and end the session
driver.quit()
