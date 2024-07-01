*** Settings ***
Documentation    color validation in login page
Library    SeleniumLibrary
Library    test.py

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome
${exp_color}    rgba(29, 255, 247, 1)

*** Test Cases ***
launching
    Open Browser    ${url}    ${browser}
    Sleep    5s
element 
    ${element}=    Get WebElement    //button[@type='submit']
    Set Global Variable    ${element}
Verify Background Color
    ${result}=    Color    ${element}
    log    ${result}
    Should Be Equal    ${result}    ${exp_color}

   
