*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     https://reqres.in
${end_point}    /api/users/2

*** Test Cases ***
Get Request
    Create Session  mysession   ${base_url}
    ${response}=   GET On Session  mysession  ${end_point}

    #Log To Console  ${response.status_code}
    #Log To Console  ${response.content}
    #Log To Console  ${response.headers}

    #Validations
    ${status_code}=     Convert To String  ${response.status_code}
    Should Be Equal     ${status_code}  200

    ${body}=    Convert To String  ${response.content}
    Should Contain  ${body}     Janet

    ${content_type}=   Get From Dictionary  ${response.headers}    Content-Type
    Should Be Equal  ${content_type}    application/json; charset=utf-8

