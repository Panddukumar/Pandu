*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Test Cases ***
Example Test
    Open Browser    https://testautomationpractice.blogspot.com/    Chrome
    Maximize Browser Window

    @{checkboxes}=    Get WebElements    xpath://input[@class='form-check-input' and contains(@id,'day')]

    FOR    ${index}    IN RANGE    4
        ${checkbox}=    Get From List    ${checkboxes}    ${index}
        Click Element    ${checkbox}
    END

    [Teardown]    Close All Browsers
