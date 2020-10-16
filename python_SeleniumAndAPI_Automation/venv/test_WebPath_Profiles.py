from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import sys
import random

#Testcase 1 : Login to the APM Application
def test_Login():
    #Invoke the Chrome Driver from Specific location
    global driver
    driver = webdriver.Chrome('C:\xxxxxxxx\chromedriver.exe')
    #Maximize the window
    driver.maximize_window()
    #Navigate to the URL
    driver.get('https://xxxxx.com')
    browserTitle = driver.title
    print(browserTitle)

    # Provide UserId to the User Id Text Box having id 'username-input'
    #weElementUserIdTxt = driver.find_element_by_id('username-input')
    weElementUserIdTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username-input')))
    weElementUserIdTxt.clear()
    weElementUserIdTxt.send_keys('testuser')

    # Provide Password to the Password TextBox having id 'password-input'
    #weElementPasswordTxt = driver.find_element_by_id('password-input')
    weElementPasswordTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password-input')))
    weElementPasswordTxt.clear()
    weElementPasswordTxt.send_keys('123xhxhxh123')

    #Click on Login Button having id 'login-button'
    #weElementLoginBtn = driver.find_element_by_id('login-button')
    weElementLoginBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-button')))
    weElementLoginBtn.click()

#Testcase 2: Navigate to Settings -> Manage Alert Profiles -> WebPath page
def test_navigateToSettings_webPathPage():
    # Click on Settings Button using CSS Selector
    weElementSettings = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alertProfile')))
    weElementSettings.click()

    #Click on Manage Alert Profiles Link using CSS Selector
    weElementManageAlertProfileLnk = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="Manage Alert Profiles"]')))
    weElementManageAlertProfileLnk.click()

    #Verify the Title of Manage Alert Profiles Page
    alertPageTitle = driver.title
    print(alertPageTitle)
    assert alertPageTitle.__eq__("Manage Alert Profiles")

    #Click on Web Path Button using xpath
    weElementWebPathBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yuyiyi"]/button[contains(text(),"Web Path")]')))
    weElementWebPathBtn.click()

#Testcase 3 : Create a New 'Custom Alert Profile'
def test_createNew_customAlertProfile():
    #Click on New Button with ID 'yuyuyuyu'
    weElementNewBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'yuyuyuyu')))
    weElementNewBtn.click()

    #Verify the Title of Edit Alert Profile Page
    alertPageTitle = driver.title
    print(alertPageTitle)
    assert alertPageTitle.__eq__("Edit Alert Profile")

    #Provide Alert Name : Text Box
    #weElementAlertNameTxt = driver.find_element_by_id('alertName')
    weElementAlertNameTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'alertName')))
    weElementAlertNameTxt.clear()
    global strProfileName
    strProfileName = 'TestAlertProfile_'+str(random.randint(99999, 987699999))
    print(strProfileName)
    weElementAlertNameTxt.send_keys(strProfileName)

    #Select Condition Creation : Dropdown by ID : select-condition-input
    weElementSelectConditionList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'select-condition-input')))
    selectConditionList = Select(weElementSelectConditionList)
    selectConditionList.select_by_visible_text('ioioioio')

    # Provide value for Violates When 'less than' Text Box
    weElementViolatesWhenLessThanTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hkhkhk')))
    weElementViolatesWhenLessThanTxt.clear()
    value = '60'
    weElementViolatesWhenLessThanTxt.send_keys(value)

    # Provide value for Violates When 'for' Text Box
    weElementViolatesWhenForTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hjhkhkhkhk')))
    weElementViolatesWhenForTxt.clear()
    weElementViolatesWhenForTxt.send_keys('5')

    # Verify Clears When greater than
    weElementClearsWhenGreaterThanTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hkhhkhkhkh')))
    txt = weElementClearsWhenGreaterThanTxt.text
    print(txt)
    #assert txt == '5'

    # Provide value for Clears When 'for' Text Box
    weElementClearsWhenForTxt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.hkhkhkhk')))
    weElementClearsWhenForTxt.clear()
    weElementClearsWhenForTxt.send_keys('6')

    #Click on Add Condition Button
    weElementAddConditionBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-button.ui-button-success')))
    weElementAddConditionBtn.click()

    # Click on Create Button with title 'Create'
    weElementCreateBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Create"]')))
    weElementCreateBtn.click()

    #Verify Profile with existing name. If name already exists cancel the operation
    try:
        weElementExistingProfileMsg = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert_alert_msgItem')))
        strExistingProfileAlertMsg = weElementExistingProfileMsg.getText()
        print(strExistingProfileAlertMsg)
        # Click on Cancel Button with title 'Cancel'
        weElementCancelBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Cancel"]')))
        weElementCancelBtn.click()

    except:
            print('Already Existing Profile')


#Testcase 4 : Cancel the Alert Profile
def test_cancelAnEdit_AlertProfile():
    # Select the Alert Profile for Edit
    weElementSelectProfileName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sqdTemplateList > optgroup:nth-child(1) > option:nth-child(1)')))
    weElementSelectProfileName.click()
    # Click on Edit Button
    weElementEditBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'editSQDButton')))
    weElementEditBtn.click()
    # Click on Cancel Button with title 'Cancel'
    weElementCancelBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Cancel"]')))
    weElementCancelBtn.click()

#Testcase 5: Edit Custom Alert Profile
def test_Edit_AlertProfile():
    #Select the Alert Profile for Edit
    weElementSelectProfileName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#uiuiuiui')))
    weElementSelectProfileName.click()

    #Click on Edit Button
    weElementEditBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'editSQDButton')))
    weElementEditBtn.click()

    # Select Condition Creation : Dropdown by ID : select-condition-input
    weElementSelectConditionList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'select-condition-input')))
    selectConditionList = Select(weElementSelectConditionList)
    selectConditionList.select_by_visible_text('HTTP Errors')

    # Click on Add Condition Button
    weElementAddConditionBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-button.ui-button-success')))
    weElementAddConditionBtn.click()

    # Click on Create Button with title 'Update'
    weElementUpdateBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Update"]')))
    weElementUpdateBtn.click()

    # Verify if any error occurs. If any error message is displayed cancel the operation
    try:
        weElementExistingProfileMsg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.alert_alert_msgItem')))
        strExistingProfileAlertMsg = weElementExistingProfileMsg.getText()
        print(strExistingProfileAlertMsg)
        # Click on Cancel Button with title 'Cancel'
        weElementCancelBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Cancel"]')))
        weElementCancelBtn.click()

    except:
        print('Some problem with profile')

#Testcase 6: Copy Custom Alert Profile
def test_Copy_AlertProfile():
    # Select the Alert Profile for Edit
    weElementSelectProfileName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ghghghgh)')))
    weElementSelectProfileName.click()

    # Click on Copy Button
    weElementCopyBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'copyDButton')))
    weElementCopyBtn.click()

    # Select Condition Creation : Dropdown by ID : select-condition-input
    weElementSelectConditionList = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'select-condition-input')))
    selectConditionList = Select(weElementSelectConditionList)
    selectConditionList.select_by_visible_text('Page Load Time')

    # Click on Add Condition Button
    weElementAddConditionBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-button.ui-button-success')))
    weElementAddConditionBtn.click()

    # Click on Create Button with title 'Create'
    weElementCreateBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Create"]')))
    weElementCreateBtn.click()

    # Verify if any error occurs. If any error message is displayed cancel the operation
    try:
        weElementExistingProfileMsg = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.alert_alert_msgItem')))
        strExistingProfileAlertMsg = weElementExistingProfileMsg.getText()
        print(strExistingProfileAlertMsg)
        # Click on Cancel Button with title 'Cancel'
        weElementCancelBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[title="Cancel"]')))
        weElementCancelBtn.click()

    except:
        print('Some problem with profile')

#Testcase 7: Delete Custom Alert Profile
def test_delete_AlertProfile():
    # Select the Alert Profile for Edit
    weElementSelectProfileName = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#uiuiuiu')))
    weElementSelectProfileName.click()

    # Click on Delete Button
    weElementDeleteBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'deleteDButton')))
    weElementDeleteBtn.click()

    #Verify 'Please confirm' modal pop up appears for Delete
    """
    weElementPlsConfirmModal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-dialog-title-confirm-dialog')))
    strMsg = weElementPlsConfirmModal.getText();
    print(strMsg)
    """
    #Click on OK Button
    weElementOkBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"OK")]')))
    weElementOkBtn.click()

#Testcase 8: Log out of the Application
def test_Logout():
    # Click on User Image Button
    weElementUserBadgeImg = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.yuyuyuyu')))
    actions = ActionChains(driver)
    actions.move_to_element(weElementUserBadgeImg)
    # perform the operation on the element
    actions.perform()
    #Click on Log Out Link
    weElementLogOutLink = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="Log Out"')))
    weElementLogOutLink.click()
    #Close or quit the browser
    driver.quit()
