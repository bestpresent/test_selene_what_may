from selene import browser, have, be


def test_add_todos_and_complete_one():
 browser.open('https://todomvc.com/examples/emberjs/todomvc/dist/')
 browser.element('.new-todo').should(be.blank)
 browser.element('.new-todo').type('First').press_enter()
 browser.element('.new-todo').type('Second').press_enter()
 browser.element('.new-todo').type('Thirst').press_enter()
 browser.all('.todo-list>li').should(have.size(3)).wait_until(800)






