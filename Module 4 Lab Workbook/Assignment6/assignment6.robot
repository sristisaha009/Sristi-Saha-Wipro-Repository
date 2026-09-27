*** Settings ***
Library    SeleniumLibrary
Test Setup       Open Test Browser
Test Teardown    Close Browser

*** Variables ***
${URL}       https://the-internet.herokuapp.com
${BROWSER}   Chrome

*** Keywords ***
Open Test Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

*** Test Cases ***
Verify Home Page
    [Tags]    smoke    regression
    Go To    ${URL}
    Page Should Contain    Welcome to the-internet
    Sleep    5s

Verify Login Page
    [Tags]    smoke    login
    Go To    ${URL}/login
    Page Should Contain Element    id=username
    Page Should Contain Element    id=password
    Sleep    5s

Verify Checkboxes Page
    [Tags]    regression    checkbox
    Go To    ${URL}/checkboxes
    Page Should Contain Element    css=input[type='checkbox']
    Sleep    5s

Verify Dropdown Page
    [Tags]    regression    dropdown
    Go To    ${URL}/dropdown
    Page Should Contain Element    id=dropdown
    Sleep    5s