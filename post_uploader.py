from playwright.sync_api import sync_playwright
from pathlib import Path

import json
import time
import logging

INSTAGRAM_URL = 'https://www.instagram.com/'
INSTA_STATE_FILE = 'insta_state.json'
HEADLESS = True

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_post(login, pwd, file, caption):
    """
    Creates new post on Instagram.

    Parameters:
        login (str): The username for authentication.
        pwd (str): The password for authentication.
        file (str): The path to the image or video file to be posted (look at instagram requirements for posts).
        caption (str): The caption or description for the post.

    Returns:
        None

    This method creates new post on Instagram using the provided login credentials, file path, and caption.
    It opens headless browser instance, logs in to the Instagram account if not already logged in,
    and uploads the specified file with the given caption.
    Finally, it closes the browser.

    Example:
        create_post("username", "password", "/path/to/file.jpg", "Check out this awesome photo!")
    """
    with sync_playwright() as p:
        browser, page = _create_page(p)
        page.goto(INSTAGRAM_URL)
        _login_if_not(login, page, pwd)
        _create_post(caption, file, page)
        browser.close()


def _save_state(page_):
    with open(INSTA_STATE_FILE, 'w') as f:
        f.write(json.dumps(page_.context.storage_state()))


def _init_login(page, login, pwd):
    logging.info(f'start login {login}')
    page.wait_for_selector('input[name="username"]')
    page.query_selector('input[name="username"]').fill(login)
    page.query_selector('input[name="password"]').fill(pwd)
    page.query_selector("button[type='submit']").click()
    page.wait_for_selector('button[type="button"]')
    page.locator("xpath=//button[contains(text(), 'Save info')]").click()
    page.wait_for_selector("//*[contains(text(),'Not Now')]")
    page.locator("//*[contains(text(),'Not Now')]").click()
    logging.info(f'success login {login}')


def _is_logged_in(page, login):
    return page.locator("xpath=//span[contains(text(), 'Profile')]").is_visible() and page.locator(
        f"xpath=//span[contains(text(), '{login}')]").is_visible()


def _create_post(caption, file, page):
    page.get_by_text("Create").click()
    page.wait_for_selector("//*[contains(text(),'Drag photos and videos here')]")
    file_input = page.query_selector("input[type='file']")
    file_input.set_input_files(files=file)
    if page.locator("xpath=//span[contains(text(), 'Video posts are now shared as reels')]").is_visible():
        page.wait_for_selector("//button[contains(text(),'OK')]")
        page.locator("//button[contains(text(),'OK')]").click()
    page.get_by_text("Next").click()
    time.sleep(5)
    page.get_by_text("Next").click()
    page.wait_for_selector("div[aria-label='Write a caption...']").fill(caption)
    page.locator("xpath=//div[contains(text(), 'Share')]").click()
    page.wait_for_selector("img[alt='Animated checkmark']")
    page.keyboard.press('Escape')
    logging.info(f'post created for file: {file}, caption: {caption}')


def _login_if_not(login, page, pwd):
    if not _is_logged_in(page, login):
        _init_login(page, login, pwd)
    _save_state(page)
    time.sleep(5)


def _create_page(p):
    browser = p.firefox.launch(headless=HEADLESS)
    if Path(INSTA_STATE_FILE).exists():
        return browser, browser.new_context(storage_state=INSTA_STATE_FILE, locale="en-US").new_page()
    else:
        return browser, browser.new_context(locale="en-US").new_page()
