from seleniumbase import SB

with SB(uc=True, test=True, headless=True) as sb:
    url = "https://manga-starz.net/manga/"
    sb.activate_cdp_mode(url)
    sb.sleep(3)

    sb.assert_element("body", timeout=10)

    print("Page Title:", sb.get_title())

    sb.save_screenshot_to_logs()
