from selene import browser, have, be

def test_complete_todo():
 browser.open('https://todomvc-emberjs-app.autotest.how')
 browser.element('#new-todo').should(be.blank)
 browser.element('#new-todo').type('First').press_enter()
 browser.element('#new-todo').type('Second').press_enter()
 browser.element('#new-todo').type('Thirst').press_enter()
 browser.all('#todo-list>li').should(have.size(3)).wait_until(800)





