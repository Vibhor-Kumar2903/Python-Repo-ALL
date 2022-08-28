*** Settings ***
Resource  ../Resources/CustomKeyword.robot
Library  SeleniumLibrary

Test Setup  Start Testcase2
Test Teardown  Finish Testcase

*** Test Cases ***
Testing Radio Button and Check Box

    Set Selenium Speed  1s
    Title Should Be  practice-form

    # Selecting Radio buttons
    Select Radio Button  sex    Female
    Select Radio Button  exp    5

    # Selecting Check Box
    Select Checkbox  BlackTea
    Select Checkbox  oolongtea
    Checkbox Should Be Selected  oolongtea

    #Unselecting Checkbox
    Unselect Checkbox  BlackTea
    Checkbox Should Not Be Selected  BlackTea
