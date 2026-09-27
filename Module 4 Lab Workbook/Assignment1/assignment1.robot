*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://the-internet.herokuapp.com/login
${BROWSER}   Chrome

*** Test Cases ***
Open Browser And Fill Login Form
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    # Verify the username field exists
    Page Should Contain Element    id=username

    # Enter username and password
    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!

    # Pause to take screenshot
    Sleep    10s

    # Submit the form
    Click Button    css=button[type='submit']
    Sleep    3s

    # Verify successful login
    Page Should Contain    You logged into a secure area!

    # Pause to capture the result
    Sleep    10s
    Close Browser