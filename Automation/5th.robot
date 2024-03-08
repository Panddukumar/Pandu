*** Settings ***
Library    SeleniumLibrary

*** Variables ***

${URL}    https://demo.guru99.com/test/newtours/
${browser}    Chrome
*** Test Cases ***
TC1 demo tour
    Open Browser    ${URL}    ${browser} 
    Input Text    //input[@name="userName"]    tutorial
    Input Text    //input[@name="password"]   
    Click Element        //input[@name="submit"]



*** Keywords ***