*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     http://localhost:8080
${endpoint}     /app/videogames/100

*** Test Cases ***
Deleting A Video Game
    Create Session  mysession   ${base_url}
    ${response}=   Delete Request  mysession   ${endpoint}

    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # Validation
    ${status}=  Convert To String  ${response.status_code}
    Should Be Equal  ${status}      200

    ${msg}=    Convert To String  ${response.content}
    Should Contain  ${msg}  Record Deleted Successfully
