*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}     http://restapi.demoqa.com/customer      #(bad request 400 if there is HTTPS)

*** Test Cases ***
Post Request
    Create Session   mysession   ${base_url}
    ${body}=   Create Dictionary   FirstName=first919   LastName=last919    UserName=user919   Password=pass919   Email=mail919@gmail.com
    ${header}=   Create Dictionary   Content-Type=application/json
    ${response}=   Post Request  mysession   /register    data=${body}   headers=${header}

    Log To Console  ${response.status_code}
    Log To Console  ${response.content}

    # validation
    ${status_code}=    ${response.status_code}
    Should Be Equal   ${status_code}     201

    ${res_body}=    Convert To String  ${response.content}
    Should Contain   ${res_body}    OPERATION_SUCCESS
    Should Contain   ${res_body}    Operation completed successfully
