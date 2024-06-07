
*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}    https://demo.guru99.com/test/newtours/
${browser}    chrome
${username}

*** Test Cases ***    
TC_01
    Open Browser     ${url}    ${browser}
    enter name    ${username}          


*** Keywords ***
enter name
    [Arguments]    ${username} 
    Input Text    //input[@name='userName']    ${username}

        

    