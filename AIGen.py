import docker
import time

from selenium import webdriver

# Create a Docker client
client = docker.from_env()

# Start a Selenium Docker container
container = client.containers.run(
    "selenium/standalone-chrome:latest",
    detach=True,
    ports={'4444/tcp': '4444'}
)

# Wait for the container to start
time.sleep(10)

# Connect to the Selenium server running in the container
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
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