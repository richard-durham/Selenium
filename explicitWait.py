from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http:google.com")

fLocator = "input[name=d]"

try:
	searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))
finally:
	driver.quit





'''
Richard (master) Selenium_Code $ python explicitWait.py
Traceback (most recent call last):
  File "explicitWait.py", line 16, in <module>
    searchField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))
  File "/Library/Python/2.7/site-packages/selenium/webdriver/support/wait.py", line 75, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message: 
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpsCouPo/extensions/fxdriver@googlecode.com/components/driver-component.js:10271)
    at FirefoxDriver.prototype.findElement (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpsCouPo/extensions/fxdriver@googlecode.com/components/driver-component.js:10280)
    at DelayedCommand.prototype.executeInternal_/h (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpsCouPo/extensions/fxdriver@googlecode.com/components/command-processor.js:12274)
    at DelayedCommand.prototype.executeInternal_ (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpsCouPo/extensions/fxdriver@googlecode.com/components/command-processor.js:12279)
    at DelayedCommand.prototype.execute/< (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpsCouPo/extensions/fxdriver@googlecode.com/components/command-processor.js:12221)
'''