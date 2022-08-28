*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.actitime.com/login.do
${url1}  http://www.practiceselenium.com/practice-form.html

*** Keywords ***
Start TestCase
    Open Browser  ${url}    ${browser}
    Maximize Browser Window

Start TestCase2
    Open Browser  ${url1}    ${browser}
    Maximize Browser Window

Finish TestCase
    Close Browser

LoginToApplication
    Input Text  id:username    admin
    Input Text  name:pwd   manager
    Click Link  id:loginButton

LogoutToApplication
    Click Link  xpath://a[text()='Logout']