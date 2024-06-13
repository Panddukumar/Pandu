*** Settings ***
Documentation    Datadriven testing login functionality page.
Resource    ../pom/generic.robot
Suite Setup    launching browser
Suite Teardown    Close All Browsers
Test Template    invalid credentials for login page
Library    DataDriver    file=D:/Robot_OrangeHRM/testdata/orangeHRM Login.xlsx

*** Test Cases ***    ${username}    ${password}
login with invalid username and password    ${username}    ${password}


*** Keywords ***
invalid credentials for login page
    [Arguments]    ${username}    ${password}
    Input Text    //input[@name="username"]    ${username}
    Input Password    //input[@name="password"]    ${password}
    Click Button    //button[@type="submit"]
    