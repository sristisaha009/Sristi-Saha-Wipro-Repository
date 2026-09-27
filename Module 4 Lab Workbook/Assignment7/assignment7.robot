
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://the-internet.herokuapp.com/login
${BROWSER}   Chrome

*** Test Cases ***
Login Test With Detailed Logs
    Log    Test execution started.    INFO

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Log    Browser opened successfully.    INFO

    # Verify login form elements
    Page Should Contain Element    id=username
    Page Should Contain Element    id=password
    Log    Login form elements verified.    INFO

    # Enter credentials
    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!
    Log    Username and password entered.    INFO

    # Screenshot checkpoint
    Sleep    5s

    # Submit login form
    Click Button    css=button[type='submit']
    Log    Login form submitted.    INFO

    # Verify successful login
    Wait Until Page Contains    You logged into a secure area!    10s
    Log    Login successful.    INFO

    # Screenshot checkpoint
    Sleep    10s

    # Log final result
    Log    Test completed successfully.    INFO

    Close Browser
    Log    Browser closed.    INFO

Verify Page Title
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    ${title}=    Get Title
    Log    Current page title: ${title}    INFO

    Should Be Equal    ${title}    The Internet

    # Screenshot checkpoint
    Sleep    5s

    Close Browser
    Log    Page title verification completed.    INFO