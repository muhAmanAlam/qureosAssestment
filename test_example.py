import re
import allure
from playwright.sync_api import Page, expect

def attach_screenshot(page, name):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )

def test_search_for_a_job(page: Page):
    page.goto("https://www.qureos.com/")
    
    job_title = "Qa Engineer"
    location = "Pakistan"

    page.get_by_placeholder("Enter Job Title, Skills, etc.").fill(job_title)
    page.get_by_placeholder("Enter Location").fill(location)
    
    page.get_by_role("button", name="Find Jobs").click()
    
    expect(page.get_by_role("heading", name = job_title + " Jobs In " + location)).to_be_visible()
    
    attach_screenshot(page, "Final Screen")
    
def test_empty_fields_show_error(page: Page):
    page.goto("https://www.qureos.com/")
    
    page.get_by_role("button", name="Find Jobs").click()
    
    expect(page.get_by_text("Please fill the field.")).to_be_visible()
    attach_screenshot(page, "Final Screen")
