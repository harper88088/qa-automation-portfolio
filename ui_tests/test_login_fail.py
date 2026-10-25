from playwright.sync_api import Page, expect

URL = "https://practicetestautomation.com/practice-test-login/"

def test_login_wrong_username(page: Page):
    page.goto(URL)
    page.fill("#username", "wronguser")
    page.fill("#password", "Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")

def test_login_wrong_password(page: Page):
    page.goto(URL)
    page.fill("#username", "student")
    page.fill("#password", "Password1234")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")

def test_login_username_empty(page: Page):
    page.goto(URL)
    page.fill("#username", "")
    page.fill("#password", "Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")

def test_login_password_empty(page: Page):
    page.goto(URL)
    page.fill("#username", "student")
    page.fill("#password", "")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_contain_text("Your password is invalid!")
