
*** Settings ***
Library    MathLibrary.py
Library    BuiltIn

*** Variables ***
${FIRST_NUMBER}     25
${SECOND_NUMBER}    35
${TEXT}             robot framework automation

*** Test Cases ***
Custom Keyword And BuiltIn Operations
    ${result}=    Calculate Sum    ${FIRST_NUMBER}    ${SECOND_NUMBER}
    Should Be Equal As Numbers    ${result}    60

    ${product}=    Evaluate    ${FIRST_NUMBER} * ${SECOND_NUMBER}
    Should Be Equal As Numbers    ${product}    875

    # Convert string to uppercase using Python
    ${uppercase}=    Evaluate    $TEXT.upper()
    Should Be Equal    ${uppercase}    ROBOT FRAMEWORK AUTOMATION

    # Get string length
    ${length}=    Get Length    ${TEXT}
    Should Be Equal As Integers    ${length}    26

    Log To Console    Sum: ${result}
    Log To Console    Product: ${product}
    Log To Console    Uppercase: ${uppercase}
    Log To Console    Length: ${length}

    Sleep    5s