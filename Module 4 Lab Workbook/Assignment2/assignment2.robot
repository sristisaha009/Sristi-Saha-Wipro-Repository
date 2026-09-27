*** Settings ***
Library    SeleniumLibrary
Library    CSVlibrary.py

*** Variables ***
${URL}       https://the-internet.herokuapp.com/login
${BROWSER}   Chrome
${DATA_FILE}    testdata.csv

*** Test Cases ***
Data Driven Login Test
    ${test_data}=    read_test_data    ${DATA_FILE}

    FOR    ${row}    IN    @{test_data}
        ${username}=    Set Variable    ${row}[0]
        ${password}=    Set Variable    ${row}[1]
        ${expected}=    Set Variable    ${row}[2]

        Open Browser    ${URL}    ${BROWSER}
        Maximize Browser Window

        Input Text    id=username    ${username}
        Input Text    id=password    ${password}

        # Screenshot checkpoint: filled form
        Sleep    5s

        Click Button    css=button[type='submit']
        Sleep    2s

        IF    '${expected}' == 'success'
            Page Should Contain    You logged into a secure area!
        ELSE
            ${actual}=    Get Text    id=flash
            Should Contain    ${actual}    invalid
        END

        # Screenshot checkpoint: result of each data set
        Sleep    5s

        Close Browser
    END