*** Settings ***
Library    SeleniumLibrary



*** Variables ***
${url}    https://www.youtube.com/
${browser}    chrome



*** Test Cases ***
TC_01 play you tube video
    Open Browser    ${url}    ${browser}   
    Maximize Browser Window
    Input Text    //*[@name="search_query"]   yajamana songs      
    Click Button    //*[@id="search-icon-legacy"]
    Sleep    1m
    Click Element    //yt-formatted-string[contains(text(),'Yajamana Title Track 4K Video Song | Darshan | V H')]
    Sleep    1m
    Close Browser



*** Keywords ***