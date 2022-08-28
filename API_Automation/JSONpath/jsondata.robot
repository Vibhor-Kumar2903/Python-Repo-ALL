*** Settings ***
Library  SeleniumLibrary
Library  os
Library  JSONLibrary

*** Variables ***

*** Test Cases ***
Test Case 1:
    ${json_obj}=  Load JSON From File  C:/Users/Vibhor/Desktop/JSONpython/jsondata.json

    ${value}=     Get Value From Json  ${json_obj}     $.phoneNumber[0].number
    Log To Console  ${value}
    Should Be Equal  ${value[0]}   8920097461       #always treat it as list

    ${value}=     Get Value From Json  ${json_obj}     $.phoneNumber[1].number
    Log To Console  ${value}
    Should Be Equal  ${value[0]}   9454737426

    ${value}=     Get Value From Json  ${json_obj}     $.Address.postalCode
    Log To Console  ${value}
    Should Be Equal  ${value[0]}   10021

    ${value}=     Get Value From Json  ${json_obj}     $.Address.streetAddress
    Log To Console  ${value}
    Should Be Equal  ${value[0]}   21 2nd Street

    ${value}=     Get Value From Json  ${json_obj}     $.Age
    Log To Console  ${value}
    Should Be Equal  ${value[0]}   25