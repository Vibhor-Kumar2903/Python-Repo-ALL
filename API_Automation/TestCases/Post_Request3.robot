*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     http://localhost:8084/      #(bad request 400 if there is HTTPS)
${end_point}    /addProject

*** Test Cases ***
Post Request
    Create Session   mysession   ${base_url}
    ${body}=   Create Dictionary   createdBy=vibhor_api1   projectName=Avengers  status=completed   teamSize=4
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   POST On Session  mysession   ${end_point}    data=${body}   headers=${header}

    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # validation
    ${status_code}=    ${response.status_code}
    Should Be Equal   ${status_code}     201

    ${res_body}=    Convert To String  ${response.content}
    Should Contain   ${res_body}    Successfully Added
    Should Contain   ${res_body}    Completed
