*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     https://reqres.in/       #bad request 400 due to HTTPS
${end_point}    /api/users

*** Test Cases ***
    # import requests
    # from requests.packages.urllib3.exceptions import InsecureRequestWarning
    # requests.package.urllib3.disable_warnings(InsecureRequestWarning)

Post Request
    Create Session  mysession   ${base_url}
    ${body}=    Create Dictionary   name=morpheus   job=leader
    ${header}=  Create Dictionary   Content-Type=application/json
    ${response}=    POST On Session  mysession  ${end_point}    data=${body}    headers=${header}

    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # validation
    ${status_code}=     ${response.status_code}
    Should Be Equal  ${status_code}     201

    ${res_body}=    Convert To String  ${response.content}
    Should Contain  ${res_body}     morpheus
    Should Contain  ${res_body}     leader


