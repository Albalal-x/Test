from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://gitlab.com/users/sign_in"
    
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    
    sb.uc_gui_click_captcha()

    # الحصول على كود HTML للصفحة
    html = sb.get_page_source()

    # طباعة جزء من HTML
    print(html[:2000])   # يطبع أول 2000 حرف فقط

    sb.post_message("HTML captured successfully", duration=4)

    print("Success! HTML data extracted.")
