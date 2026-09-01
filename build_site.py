# build_site.py
# تولیدکننده سایت ایستا برای گروه لایتنینگ استودیو

import os
import datetime

# ==========================================
# ۱. دیتا و اطلاعات گروه (این بخش رو ویرایش کن)
# ==========================================
SITE_TITLE = "لایتنینگ استودیو"
SITE_DESCRIPTION = "گروه برنامه‌نویسی و توسعه نرم‌افزار"
COPYRIGHT_YEAR = datetime.datetime.now().year

# اطلاعات اعضای گروه (لیست دیکشنری)
TEAM_MEMBERS = [
    {"name": "سبحان", "role": "مدیر", "skills": "Python, Django, React, Docker"},
    {"name": "محمد مهدی", "role": "مدیر", "skills": "Python, FastAPI, PostgreSQL"},
    {"name": "مانی کریمی", "role": "برنامه‌نویس", "skills": "React, Next.js, Tailwind CSS"},
    {"name": "پرهام", "role": "برنامه‌نویس سطح ۴ | فعال اجتماعی", "skills": "Python, HTML, CSS, JavaScript"},
]

# پروژه‌های انجام شده
PROJECTS = [
    {
        "title": "تماس‌های اضطراری",
        "desc": "دسترسی سریع به تماس‌های ضروری",
        "tech": "Django + React",
        "link": "https://myket.ir/app/appinventor.ai_mmastudio_s_m.tamas"
    },
    {"title": "هوش مصنوعی Star AI", "desc": "در دست توسعه", "tech": "TensorFlow, PyTorch, FastAPI"},
    {"title": "پیامرسان فوق پیشرفته", "desc": "پیامرسان امن و پرسرعت با قابلیت‌های پیشرفته ارتباطی", "tech": "FastAPI + WebSocket + React"},
]

# ==========================================
# ۲. لیست ویدیوها
# ==========================================
VIDEOS = [
    {
        "title": "آموزش اسکرچ جونیور پارت ۱: بازی خروس و طوفان",
        "desc": "آموزش برنامه‌نویسی کودکان با اسکرچ جونیور - ساخت بازی جذاب",
        "link": "https://www.aparat.com/v/bewg9bw",
    },
]

# ==========================================
# ۳. تابع تولید صفحه اصلی (index.html)
# ==========================================
def generate_index_html():
    css_style = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #0f0f1a;
        color: #e0e0e0;
        line-height: 1.7;
        padding: 20px;
        direction: rtl;
    }
    .container {
        max-width: 1100px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(5px);
        padding: 40px 50px;
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
        border: 1px solid rgba(255,255,255,0.08);
    }
    h1 {
        font-size: 3rem;
        background: linear-gradient(135deg, #f093fb, #f5576c, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .subtitle {
        text-align: center;
        color: #aaa;
        font-size: 1.2rem;
        border-bottom: 2px solid #333;
        padding-bottom: 20px;
        margin-bottom: 30px;
    }
    .nav-menu {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-bottom: 30px;
        padding: 15px;
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        border: 1px solid #2a2a3a;
    }
    .nav-btn {
        padding: 10px 25px;
        background: rgba(255,255,255,0.08);
        color: #e0e0e0;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    .nav-btn:hover {
        background: linear-gradient(135deg, #f5576c, #4facfe);
        color: #fff;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(79, 172, 254, 0.3);
        border-color: #4facfe;
    }
    .nav-btn.video-btn {
        background: linear-gradient(135deg, #f093fb, #f5576c);
        color: #fff;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
    }
    .nav-btn.video-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(245, 87, 108, 0.5);
        background: linear-gradient(135deg, #f5576c, #f093fb);
    }
    .section {
        margin-bottom: 40px;
    }
    .section h2 {
        font-size: 2rem;
        color: #fff;
        border-right: 5px solid #f5576c;
        padding-right: 15px;
        margin-bottom: 20px;
    }
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 20px;
    }
    .card {
        background: rgba(255,255,255,0.06);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #2a2a3a;
        transition: transform 0.3s ease, border-color 0.3s;
    }
    .card:hover {
        transform: translateY(-8px);
        border-color: #4facfe;
    }
    .card h3 {
        color: #f093fb;
        margin-bottom: 5px;
    }
    .card .role {
        color: #4facfe;
        font-weight: bold;
        font-size: 0.9rem;
    }
    .card .skills {
        color: #aaa;
        font-size: 0.85rem;
        margin-top: 10px;
        background: #1a1a2e;
        padding: 5px 12px;
        border-radius: 30px;
        display: inline-block;
    }
    .project-card {
        background: rgba(255,255,255,0.04);
        padding: 20px;
        border-radius: 16px;
        border-right: 4px solid #f5576c;
        margin-bottom: 15px;
    }
    .project-card h3 {
        color: #fff;
    }
    .project-card .tech {
        color: #f093fb;
        font-size: 0.8rem;
        background: #1a1a2e;
        padding: 3px 12px;
        border-radius: 30px;
        display: inline-block;
        margin-top: 8px;
    }
    .download-btn {
        display: inline-block;
        margin-top: 12px;
        padding: 8px 20px;
        background: linear-gradient(135deg, #f5576c, #f093fb);
        color: #fff;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.85rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
    }
    .download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 87, 108, 0.5);
        background: linear-gradient(135deg, #f5576c, #4facfe);
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #2a2a3a;
        color: #666;
        font-size: 0.9rem;
    }
    .contact-info {
        background: #1a1a2e;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        direction: ltr;
    }
    .contact-info span {
        color: #4facfe;
        font-weight: bold;
    }
    .contact-info a {
        color: #4facfe;
        text-decoration: none;
        font-weight: bold;
    }
    .contact-info a:hover {
        text-decoration: underline;
        color: #f093fb;
    }
    @media (max-width: 700px) {
        .container { padding: 20px; }
        h1 { font-size: 2rem; }
        .nav-menu { gap: 10px; }
        .nav-btn { padding: 8px 18px; font-size: 0.85rem; }
    }
    """

    members_html = ""
    for member in TEAM_MEMBERS:
        members_html += f"""
        <div class="card">
            <h3>{member['name']}</h3>
            <div class="role">{member['role']}</div>
            <div class="skills">{member['skills']}</div>
        </div>
        """

    projects_html = ""
    for proj in PROJECTS:
        download_btn = ""
        if "link" in proj and proj["link"]:
            download_btn = f'<a href="{proj["link"]}" target="_blank" class="download-btn">📥 دانلود از مایکت</a>'
            
        projects_html += f"""
        <div class="project-card">
            <h3>🔹 {proj['title']}</h3>
            <p>{proj['desc']}</p>
            <div class="tech">{proj['tech']}</div>
            {download_btn}
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{SITE_TITLE}</title>
    <style>{css_style}</style>
</head>
<body>
    <div class="container">
        <h1>⚡ {SITE_TITLE}</h1>
        <div class="subtitle">{SITE_DESCRIPTION}</div>

        <div class="nav-menu">
            <a href="#" class="nav-btn">🏠 صفحه اصلی</a>
            <a href="videos.html" class="nav-btn video-btn">🎥 ویدیوها</a>
        </div>

        <div class="section">
            <h2>درباره ما</h2>
            <p style="font-size:1.1rem; color:#ccc;">
                ما یک تیم جوان و خلاق از برنامه‌نویسان و مهندسان نرم‌افزار هستیم. 
                هدف ما ساخت محصولات باکیفیت، یادگیری مداوم و به‌اشتراک‌گذاری دانش است. 
                در «لایتنینگ استودیو» اعتقاد داریم که کد خوب، دنیای بهتری می‌سازد.
            </p>
        </div>

        <div class="section">
            <h2>👨‍💻 اعضای تیم</h2>
            <div class="card-grid">
                {members_html}
            </div>
        </div>

        <div class="section">
            <h2>🚀 پروژه‌های ما</h2>
            {projects_html}
        </div>

        <div class="section">
            <h2>📬 ارتباط با ما</h2>
            <div class="contact-info">
                <span>✉️</span> mmastudio.s.m@gmail.com &nbsp;|&nbsp; 
                <span>📱</span> <a href="https://ble.ir/mmastudio" target="_blank">https://ble.ir/mmastudio</a>
            </div>
        </div>

        <div class="footer">
            © {COPYRIGHT_YEAR} تمامی حقوق برای گروه {SITE_TITLE} محفوظ است.
        </div>
    </div>
</body>
</html>
"""
    return html_content

# ==========================================
# ۴. تابع تولید صفحه ویدیوها (videos.html)
# ==========================================
def generate_videos_html():
    css_style = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #0f0f1a;
        color: #e0e0e0;
        line-height: 1.7;
        padding: 20px;
        direction: rtl;
    }
    .container {
        max-width: 1100px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(5px);
        padding: 40px 50px;
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.8);
        border: 1px solid rgba(255,255,255,0.08);
    }
    h1 {
        font-size: 3rem;
        background: linear-gradient(135deg, #f093fb, #f5576c, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .subtitle {
        text-align: center;
        color: #aaa;
        font-size: 1.2rem;
        border-bottom: 2px solid #333;
        padding-bottom: 20px;
        margin-bottom: 30px;
    }
    .nav-menu {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        margin-bottom: 30px;
        padding: 15px;
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        border: 1px solid #2a2a3a;
    }
    .nav-btn {
        padding: 10px 25px;
        background: rgba(255,255,255,0.08);
        color: #e0e0e0;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    .nav-btn:hover {
        background: linear-gradient(135deg, #f5576c, #4facfe);
        color: #fff;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(79, 172, 254, 0.3);
        border-color: #4facfe;
    }
    .nav-btn.video-btn {
        background: linear-gradient(135deg, #f093fb, #f5576c);
        color: #fff;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
    }
    .nav-btn.video-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(245, 87, 108, 0.5);
        background: linear-gradient(135deg, #f5576c, #f093fb);
    }
    .section {
        margin-bottom: 40px;
    }
    .section h2 {
        font-size: 2rem;
        color: #fff;
        border-right: 5px solid #4facfe;
        padding-right: 15px;
        margin-bottom: 20px;
    }
    .video-card {
        background: rgba(255,255,255,0.04);
        padding: 20px;
        border-radius: 16px;
        border-right: 4px solid #4facfe;
        margin-bottom: 15px;
        transition: transform 0.3s ease, border-color 0.3s;
    }
    .video-card:hover {
        transform: translateX(-5px);
        border-color: #f093fb;
    }
    .video-card h3 {
        color: #fff;
        font-size: 1.2rem;
    }
    .video-card p {
        color: #ccc;
        margin: 8px 0;
    }
    .watch-btn {
        display: inline-block;
        margin-top: 10px;
        padding: 8px 25px;
        background: linear-gradient(135deg, #4facfe, #43e97b);
        color: #fff;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.85rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(79, 172, 254, 0.3);
    }
    .watch-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 172, 254, 0.5);
        background: linear-gradient(135deg, #43e97b, #4facfe);
    }
    .back-btn {
        display: inline-block;
        margin-top: 20px;
        padding: 10px 30px;
        background: linear-gradient(135deg, #f5576c, #f093fb);
        color: #fff;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
    }
    .back-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 87, 108, 0.5);
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #2a2a3a;
        color: #666;
        font-size: 0.9rem;
    }
    @media (max-width: 700px) {
        .container { padding: 20px; }
        h1 { font-size: 2rem; }
        .nav-menu { gap: 10px; }
        .nav-btn { padding: 8px 18px; font-size: 0.85rem; }
    }
    """

    videos_html = ""
    for video in VIDEOS:
        videos_html += f"""
        <div class="video-card">
            <h3>🎬 {video['title']}</h3>
            <p>{video['desc']}</p>
            <a href="{video['link']}" target="_blank" class="watch-btn">▶️ تماشا در آپارات</a>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ویدیوها - {SITE_TITLE}</title>
    <style>{css_style}</style>
</head>
<body>
    <div class="container">
        <h1>🎥 {SITE_TITLE}</h1>
        <div class="subtitle">ویدیوهای آموزشی گروه</div>

        <div class="nav-menu">
            <a href="index.html" class="nav-btn">🏠 صفحه اصلی</a>
            <a href="#" class="nav-btn video-btn">🎥 ویدیوها</a>
        </div>

        <div class="section">
            <h2>📹 ویدیوهای آموزشی</h2>
            {videos_html}
        </div>

        <div style="text-align: center;">
            <a href="index.html" class="back-btn">🔙 بازگشت به صفحه اصلی</a>
        </div>

        <div class="footer">
            © {COPYRIGHT_YEAR} تمامی حقوق برای گروه {SITE_TITLE} محفوظ است.
        </div>
    </div>
</body>
</html>
"""
    return html_content

# ==========================================
# ۵. تابع اصلی برای ذخیره فایل‌ها
# ==========================================
def main():
    print("⚡ در حال تولید سایت برای گروه لایتنینگ استودیو...")
    
    # تولید صفحه اصلی
    index_html = generate_index_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("✅ فایل index.html با موفقیت ساخته شد!")
    
    # تولید صفحه ویدیوها
    videos_html = generate_videos_html()
    with open("videos.html", "w", encoding="utf-8") as f:
        f.write(videos_html)
    print("✅ فایل videos.html با موفقیت ساخته شد!")
    
    print("📍 مسیر فایل‌ها:", os.path.abspath("."))
    print("🌐 حالا می‌توانید فایل‌ها را در مرورگر باز کنید.")

if __name__ == "__main__":
    main()