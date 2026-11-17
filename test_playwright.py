"""End-to-end tests of the AGH Faculty of Computer Science website."""
import re

from playwright.sync_api import Page, expect

HOME_URL = "https://www.informatyka.agh.edu.pl/pl/"


def open_menu_item(page: Page, section: str, item: str) -> None:
    """Open a drop-down section of the main menu and click one of its links."""
    menu = page.get_by_role("navigation")
    menu.get_by_role("link", name=section).click()
    menu.get_by_role("link", name=item).click()


def test_open_agh_website(page: Page):
    """The home page loads and its title names the faculty."""
    page.goto(HOME_URL)
    expect(page).to_have_title(re.compile("Wydział Informatyki AGH"))


def test_about_faculty(page: Page):
    """The menu leads to the About the Faculty page with its main heading."""
    page.goto(HOME_URL)
    open_menu_item(page, "Wydział", "O Wydziale")
    expect(page.get_by_role("heading", name="O Wydziale", level=1)).to_be_visible()


def test_study_programmes(page: Page):
    """The study programmes page lists the programmes offered."""
    page.goto(HOME_URL)
    open_menu_item(page, "Kandydaci", "Nasze kierunki")
    expect(page.get_by_role("heading", name="Nasze kierunki", level=1)).to_be_visible()
    expect(page.get_by_role("heading", name="Data Science")).to_be_visible()


def test_url_changes_after_navigation(page: Page):
    """Opening About the Faculty changes the address to its subpage."""
    page.goto(HOME_URL)
    open_menu_item(page, "Wydział", "O Wydziale")
    expect(page).to_have_url(re.compile(r"/pl/wydzial/o-wydziale/?$"))
