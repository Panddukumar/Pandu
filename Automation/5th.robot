*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${URL}    https://www.orangehrm.com/en/orangehrm-starter-open-source-software/
${browser}    Chrome
*** Test Cases ***
TC1 Facebook Login
    Open Browser    ${URL}    ${browser}  
    



*** Keywords ***