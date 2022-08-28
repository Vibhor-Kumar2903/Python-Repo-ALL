*** Settings ***
Resource  ../Resources/CustomKeyword.robot
Library  SeleniumLibrary

Test Setup  Start Testcase
Test Teardown  Finish Testcase

*** Test Cases ***
TestingInputBox

    Title Should Be  actiTIME - Login
    ${"username"}   Set Variable  id:username

    Element Should Be Visible  ${"username"}
    Element Should Be Enabled  ${"username"}

    Input Text  ${"username"}   admin
    Sleep  4s
    Clear Element Text  ${"username"}
    Sleep  4s
