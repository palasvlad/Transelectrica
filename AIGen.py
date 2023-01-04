import time

from selenium import webdriver

# Connect to the Selenium server running in the container
driver = webdriver.Remote(
    command_executor='http://192.168.0.188:4444/wd/hub',
    desired_capabilities=webdriver.DesiredCapabilities.CHROME
)

# Navigate to a web page
driver.get("https://www.example.com")

# Wait for the page to load
time.sleep(10)

# Close the browser window
driver.quit()

# Stop and remove the container
container.stop()
container.remove()