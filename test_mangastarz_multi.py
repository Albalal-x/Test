import pytest
from seleniumbase import BaseCase

BaseCase.main(__name__, __file__, "--uc", "-n2")

@pytest.mark.parametrize("", [[]] * 2)
def test_open_mangastarz(sb):
    sb.open("https://manga-starz.net/manga/")
    sb.assert_element("body", timeout=10)
    sb.save_screenshot_to_logs()
