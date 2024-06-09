*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${url}    https://accounts.google.com/servicelogin?hl=en-gb
${browser}    chrome

*** Test Cases ***
TC_01 open Gmail Login page
    Open Browser    ${url}    ${browser}  
    Input Text    //input[@type="email"]    emailid
    Sleep    1s
    Click Element    //*[@id="identifierNext"]/div/button
    Sleep    1m
    #Input Password    //*[@id="password"]    password
    
    
    
  
*** Keywords ***
