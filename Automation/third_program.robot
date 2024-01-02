*** settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.facebook.com/login/

${browser}    chrome


*** Test Cases ***
TC_01 open login page
    Open Browser    ${url}    ${browser}   
    Maximize Browser Window
    Input Text    //*[@id="email"]    pandukumarnagendra@gmai.com
    Input Password    //*[@id="passContainer"]   panj@kl1457
    Sleep    30s
    Close Browser   



*** Keywords ***