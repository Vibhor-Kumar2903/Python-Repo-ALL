*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     http://localhost:8080
${end_point}    /app/videogames

*** Test Cases ***
Get All Video Games
    Create Session  mysession   ${base_url}
    ${response}=     GET On Session  mysession   ${end_point}
    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # Validation
    ${status_code}=     Convert To String  ${response.status_code}
    Should Be Equal  ${status_code}     200

