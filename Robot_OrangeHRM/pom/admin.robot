*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    login.robot
Library    ExcelLibrary

*** Variables ***
${file}    C:\\Users\\tika-btm-ltp158\\Desktop\\Selenium-in-DDT.xlsx
${sheetname}    Sheet1

*** Keywords ***
admin page
    # validate how many employees are in 'Enabled status'
    Click Element    //span[text()='Admin']
    ${row_count}=    Get Element Count    //div[@role="row"]
    ${enabled_count}=    Set Variable    0
    FOR    ${index}    IN RANGE    1    ${row_count}+1
        ${status}=    Get Text    (//div[@role="row"])[${index}]/div[5]
        IF    '${status}'=='Enabled'
            ${employee_name}=    Get Text    (//div[@role="row"])[${index}]/div[4]
            ${enabled_count}=    Evaluate    ${enabled_count}+1
        END
    END
    log    ${enabled_count}


    # validation
    @{admin}=    Create List  
    ${row_count}=    Get Element Count    //div[@role="row"]
    FOR  ${index}  IN RANGE    2    ${row_count}+1
        ${admin_text}=    Get Text    (//div[@role="row"])[${index}]/div[3]
        Append To List    ${admin}    ${admin_text}
        Open Excel Document    ${file}    2
        Get Sheet    ${sheetname}
        Write Excel Row    7    ${admin}
        Save Excel Document    ${file}
        Close All Excel Documents
    END
    ${expect_list}=    Create List    Admin    Admin    Admin
    log    ${admin}     

    # validating dropdown in admin page
    Click Element    (//div[@class="oxd-select-text-input"])[1]
    Click Element    (//span[text()='Admin'])[2]
    Click Element    //button[@type="submit"]

    Set Test Documentation    uploading a file
    Click Element    //span[text()='My Info']
    Sleep    5s
    Click Element    //button[@class="oxd-button oxd-button--medium oxd-button--text"]
    # Sleep    5s
    Choose File    //*[@type="file"]    ${CURDIR}\\testdata\\selenium-screenshot-1.png
    Sleep    5s
    Click Button    //button[@type="submit"]
    Run Keyword And Ignore Error    Capture Page Screenshot

    # downloading a file
    Set Test Documentation    downloading a file
    Click Button    (//button[normalize-space()='Save'])[3]
    Click Button    (//button[@class="oxd-icon-button oxd-table-cell-action-space"])[3]

    Sleep    10s
    Close All Browsers