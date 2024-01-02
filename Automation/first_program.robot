*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${URL}    https://www.facebook.com/
${browser}    Chrome
*** Test Cases ***
TC1 Facebook Login
    Open Browser    ${URL}    ${browser}  



*** Keywords ***