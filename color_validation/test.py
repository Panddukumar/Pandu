from robot.api.deco import library,keyword
from robot.libraries.BuiltIn import BuiltIn

@keyword
def color(element_locator):
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    background_color = seleniumlib.get_webelement(element_locator).value_of_css_property('background-color')
    return background_color

           