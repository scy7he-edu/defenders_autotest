import pytest
import allure
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}


@pytest.fixture(autouse=True)
def attach_failure_screenshot(request, page: Page):
    yield

    rep_setup = getattr(request.node, "rep_setup", None)
    rep_call = getattr(request.node, "rep_call", None)

    failed_on_setup = rep_setup and rep_setup.failed
    failed_on_call = rep_call and rep_call.failed

    if failed_on_setup or failed_on_call:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="failed setup/call screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
