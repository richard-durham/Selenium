from selenium import webdriver

driver = webdriver.Firefox()

driver.implicitly_wait(15)

driver.get("http:google.com")

searchField = driver.find_element_by_css_selector("input[name=d]")

driver.


'''
Richard (master) Selenium_Code $ python implicit_wait.py
Traceback (most recent call last):
  File "implicit_wait.py", line 9, in <module>
    searchField = driver.find_element_by_css_selector("input[name=d]")
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 376, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 664, in find_element
    {'using': by, 'value': value})['value']
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 175, in execute
    self.error_handler.check_response(response)
  File "/Library/Python/2.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 166, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"css selector","selector":"input[name=d]"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpKbuDPr/extensions/fxdriver@googlecode.com/components/driver-component.js:10271)
    at fxdriver.Timer.prototype.setTimeout/<.notify (file:///var/folders/2z/xhkbl3b16wj38q47xxjyw0pw0000gn/T/tmpKbuDPr/extensions/fxdriver@googlecode.com/components/driver-component.js:603)
'''