*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    OperatingSystem

*** Variables ***
${URL}          https://the-internet.herokuapp.com/login
${API_URL}      https://jsonplaceholder.typicode.com
${BROWSER}      Chrome
${SCREENSHOT_DIR}    screenshots

*** Test Cases ***
Verify Login Using Assertions
    [Documentation]    Verify login using Selenium assertions.
    Create Directory    ${SCREENSHOT_DIR}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Wait for the login form to load
    Wait Until Element Is Visible    id=username    20s
    Wait Until Element Is Visible    id=password    20s

    Log    Login page loaded successfully.

    # Enter credentials
    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!

    # Screenshot 1: filled login form
    Capture Page Screenshot
    ...    ${SCREENSHOT_DIR}/login_form.png

    # Submit login form
    Click Button    css=button[type='submit']

    # Wait for successful login confirmation
    Wait Until Element Is Visible    id=flash    20s
    Wait Until Page Contains
    ...    You logged into a secure area!
    ...    10s

    # Verify expected result
    ${actual}=    Get Text    id=flash
    Should Contain    ${actual}
    ...    You logged into a secure area!

    Log    Login assertion passed.

    # Screenshot 2: successful login
    Capture Page Screenshot
    ...    ${SCREENSHOT_DIR}/successful_login.png

    Log To Console    Login test completed successfully.

    [Teardown]    Close Browser


Verify API Response
    [Documentation]    Verify API status and response fields.
    Create Session    jsonplaceholder    ${API_URL}
    ${response}=    GET On Session
    ...    jsonplaceholder
    ...    /posts/1

    # Verify HTTP status code
    Should Be Equal As Integers
    ...    ${response.status_code}
    ...    200

    # Verify response body
    ${body}=    Set Variable    ${response.json()}

    Should Be Equal As Strings    ${body}[userId]    1
    Should Be Equal As Strings    ${body}[id]    1
    Should Be Equal As Strings
    ...    ${body}[title]
    ...    sunt aut facere repellat provident occaecati excepturi optio reprehenderit

    Log To Console    API Status: ${response.status_code}
    Log To Console    API Title: ${body}[title]
    Log    API response verification passed.