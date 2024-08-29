import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv(
        'selene.base_url', 'https://todomvc.com/examples/emberjs/todomvc/dist/')

    browser.config.browser_name = os.getenv('browser_name', 'chrome')
    browser.config.hold_browser_open = (os.getenv('hold_browser_open', 'false').lower() == 'true')
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_height', '768')
    browser.config.timeout = float(os.getenv('timeout', '3.0'))

    yield