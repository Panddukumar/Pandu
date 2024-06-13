*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${username}    Admin
${password}    admin123

*** Keywords ***
login to application
    Input Text    //input[@name="username"]    ${username}
    Input Password    //input[@name="password"]    ${password}
    Click Button    //button[@type="submit"]
    Wait Until Element Is Visible    //span[text()='Dashboard']
    Element Text Should Be    //span[text()='Dashboard']    Dashboard
