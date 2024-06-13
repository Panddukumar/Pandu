*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}    chrome

*** Keywords ***
launching browser
    Set Selenium Implicit Wait    5s
    Open Browser    ${url}    ${browser}
    Maximize Browser Window