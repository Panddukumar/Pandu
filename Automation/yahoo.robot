*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem

*** Variables ***
${url}      https://login.yahoo.com/?.intl=in
${Browser}  chrome


*** Test Cases ***
TC_01 yahoo mail Login
    Open Browser    ${url}    ${browser}  
    Maximize Browser Window
    Input Text  //input[@name="username"]    pandukumarbr@yahoo.com
    Click Button    //input[@id="login-signin"] 
    Sleep   10s
    Input Password  //input[@type="password"]   Nagendra@1008
    Click Button    //button[@type="submit"]
    Click Element   //a[@id="ybarMailLink"]
    Click Element   //a[text()="Compose"]
    Input Text       //input[@id="message-to-field"]    pandukumarbr@gmail.com
    Input Text       //input[@id="compose-subject-input"]   Resume
    Click Button     //button[@title="Attach files"]
    Choose File    //span[text()="Attach files from computer"]  /home/pandu/Downloads/Pandu Kumar. python tester Resume (3).pdf

          


*** Keywords ***





