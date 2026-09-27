*** Settings ***
Library    SeleniumLibrary
Test Setup       Login Before Each Test
Test Teardown    Logout And Close Browser

*** Variables ***
${URL}       https://the-internet.herokuapp.com/login
${BROWSER}   Chrome

*** Keywords ***
Login Before Each Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id=username    tomsmith
    Input Text    id=password    SuperSecretPassword!
    Click Button    css=button[type='submit']

    Wait Until Page Contains    You logged into a secure area!    10s

Logout And Close Browser
    # Log out if the browser is still on the secure area
    ${logout_visible}=    Run Keyword And Return Status
    ...    Page Should Contain Element    css=a[href='/logout']

    IF    ${logout_visible}
        Click Link    css=a[href='/logout']
        Wait Until Page Contains    You logged out of the secure area!    10s
        # Screenshot checkpoint: logout confirmation
        Sleep    5s
    END

    Close Browser

*** Test Cases ***
Verify Secure Area
    Page Should Contain    Secure Area
    # Screenshot checkpoint: logged-in secure area
    Sleep    5s

Verify Logout Link
    Page Should Contain Element    css=a[href='/logout']
    # Screenshot checkpoint: logout link visible
    Sleep    5s