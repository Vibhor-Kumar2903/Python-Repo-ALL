*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     http://localhost:8080
${end_point}    /app/videogames

*** Test Cases ***
Creating A Video Game
    Create Session   mysession   ${base_url}
    ${body}=    Create Dictionary       id=103  name=Iron-Man   releaseDate=2021-08-25T02:56:56.882Z    reviewScore=5   category=Avengers   rating=5
    ${header}=  Create Dictionary   Content-Type=application/json
    ${response}=    Post Request  mysession   ${end_point}     data=${body}    headers=${header}

    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # validation
    ${status}=    Convert To String  ${response.status_code}
    Should Be Equal   ${status}     200

    ${res_body}=    Convert To String  ${response.content}
    Should Contain   ${res_body}    Record Added Successfully
