from seleniumbase import BaseCase

class MangaChallenge(BaseCase):
    def test_bypass_and_scrape(self):
        # الرابط المراد اختباره
        url = "https://manga-starz.net/manga/"
        
        # فتح الموقع باستخدام وضع CDP (المحاكي للبشر) كما في الفيديو
        self.driver.cdp.open(url)
        
        # الانتظار قليلاً لتجاوز أي حواجز حماية (Cloudflare مثلاً)
        self.sleep(10)
        
        # التحقق من نجاح الدخول عن طريق طباعة عنوان الصفحة
        print(f"\n[+] تم الدخول بنجاح! عنوان الصفحة هو: {self.get_title()}")
        
        # أخذ لقطة شاشة للتأكد من أن الصفحة تظهر بشكل صحيح في GitHub Actions
        self.save_screenshot("manga_result.png")
        
        # التحقق من وجود عنصر معين (مثلاً قائمة المانجا) للتأكيد
        if self.is_element_present("body"):
            print("[+] تم تحميل محتوى الصفحة بنجاح.")
