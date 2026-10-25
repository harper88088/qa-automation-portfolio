from playwright.sync_api import Page, expect

URL = "https://practicetestautomation.com/practice-test-table/"

def test_filter_result(page: Page):
    page.goto(URL)
    page.get_by_role("radio", name="Python").check()

    expect(page.get_by_role("radio", name="Python")).to_be_checked()

    rows = page.locator("table tbody tr").filter(visible=True)
    expect(rows).to_have_count(2)

    for row in rows.all():
        expect(row.locator("td").nth(2)).to_have_text("Python")