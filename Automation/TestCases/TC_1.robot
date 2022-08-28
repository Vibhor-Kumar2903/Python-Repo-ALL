*** Settings ***
Resource  ../Resources/CustomKeyword.robot
Library  SeleniumLibrary

Test Setup  Start Testcase
Test Teardown  Finish Testcase

*** Test Cases ***
LoginTest

    LoginToApplication
    Sleep  5s
    LogoutToApplication