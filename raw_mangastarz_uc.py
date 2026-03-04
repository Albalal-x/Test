from seleniumbase import SB

with SB(uc=True, test=True, headless=True) as sb:
    url = "https://manga-starz.net/manga/"
    sb.open(url)
    sb.sleep(3)

    # تحقق أن الصفحة تم تحميلها
    sb.assert_element("body", timeout=10)

    # اطبع عنوان الصفحة
    print("Page Title:", sb.get_title())

    # احفظ لقطة شاشة
    sb.save_screenshot_to_logs()
