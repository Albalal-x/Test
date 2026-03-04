from seleniumbase import BaseCase

class MangaTest(BaseCase):
    def test_open_manga_starz(self):
        # 1. إعدادات الرابط
        url = "https://manga-starz.net/manga/"
        
        print(f"\n[1] جاري محاولة الدخول إلى: {url}")

        # 2. استخدام وضع CDP (Chrome DevTools Protocol) 
        # هذا الوضع هو السر في تجاوز الحماية كما ذُكر في الفيديو
        try:
            self.driver.cdp.open(url)
            
            # 3. الانتظار لتجاوز صفحة الفحص (Cloudflare/Turnstile)
            # ننتظر 10 ثوانٍ للتأكد من انتهاء أي تحديات تقنية خلف الكواليس
            self.sleep(10)

            # 4. محاولة التفاعل مع الصفحة لإثبات أننا "بشر"
            self.driver.cdp.scroll_down(500) # التمرير للأسفل قليلاً
            self.sleep(2)

            # 5. التحقق من نجاح الدخول
            page_title = self.driver.title
            print(f"[2] عنوان الصفحة المستخرج: {page_title}")

            # إذا كان العنوان يحتوي على "Just a moment" أو "Cloudflare" فهذا يعني أننا لم نتجاوز الحماية بعد
            if "Cloudflare" in page_title or "Just a moment" in page_title:
                print("[!] تنبيه: يبدو أن الحماية لا تزال نشطة، جاري محاولة التقاط صورة للتحقق.")
            else:
                print("[+] نجاح: تم الدخول إلى الموقع وتجاوز الحماية بنجاح.")

            # 6. حفظ النتيجة كصورة (Artifact) لرؤيتها في GitHub Actions
            self.save_screenshot("manga_result.png")
            print("[3] تم حفظ لقطة شاشة باسم: manga_result.png")

        except Exception as e:
            print(f"[-] حدث خطأ أثناء التشغيل: {e}")
            self.save_screenshot("error_screenshot.png")
            raise e

# ملاحظة: تأكد من تشغيل هذا الملف باستخدام الأمر التالي في الـ Workflow:
# pytest test_bot.py --uc --headless -s
