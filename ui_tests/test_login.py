from playwright.sync_api import Page, expect

HOME_URL = "https://practicetestautomation.com"

def test_go_to_practice_page (page :Page):
    # 홈 -> Practice 페이지
    page.goto(HOME_URL)
    page.click("#menu-item-20")

    expect(page).to_have_url("https://practicetestautomation.com/practice/")

    # Practice 페이지 -> Test Login Page
    page.get_by_role("link", name="Test Login Page").click()

    expect(page).to_have_url("https://practicetestautomation.com/practice-test-login/")

    # Login 페이지
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.locator("h1")).to_contain_text("Logged In Successfully")
