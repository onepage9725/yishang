import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update navigation to match Home Page.
new_desktop_nav = """        <nav class="hidden md:flex gap-10">
            <a href="index.html#home" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">首页</span>
                <span class="text-gray-200 text-xs tracking-wider">Home</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>
            <a href="index.html#about" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">关于我们</span>
                <span class="text-gray-200 text-xs tracking-wider">About Us</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>
            <a href="index.html#services" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">课程与产品</span>
                <span class="text-gray-200 text-xs tracking-wider">Programs</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>
            <a href="index.html#programs" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">活动</span>
                <span class="text-gray-200 text-xs tracking-wider">Events</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>
            <a href="advisory.html" class="flex flex-col items-center group">
                <span class="text-brand-lightGold font-semibold mb-1">顾问团队</span>
                <span class="text-brand-lightGold text-xs tracking-wider">Advisory</span>
                <div class="w-6 h-[2px] bg-brand-lightGold mt-1"></div>
            </a>
            <a href="index.html#registration" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">联系我们</span>
                <span class="text-gray-200 text-xs tracking-wider">Contact</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>
        </nav>"""

# Using regex to replace the desktop nav
content = re.sub(r'<nav class="hidden md:flex gap-10">.*?</nav>', new_desktop_nav, content, flags=re.DOTALL)

# Mobile Nav
new_mobile_nav = """        <nav class="flex flex-col items-center gap-8 w-full">
            <a href="index.html#home" class="mobile-nav-link flex flex-col items-center group w-full text-center opacity-80 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1 text-xl">首页</span>
                <span class="text-gray-200 text-sm tracking-wider">Home</span>
            </a>
            <a href="index.html#about" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">关于我们</span>
                <span class="text-gray-200 text-sm tracking-wider">About Us</span>
            </a>
            <a href="index.html#services" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">课程与产品</span>
                <span class="text-gray-200 text-sm tracking-wider">Programs</span>
            </a>
            <a href="index.html#programs" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">活动</span>
                <span class="text-gray-200 text-sm tracking-wider">Events</span>
            </a>
            <a href="advisory.html" class="mobile-nav-link flex flex-col items-center group w-full text-center">
                <span class="text-brand-lightGold font-semibold mb-1 text-xl">顾问团队</span>
                <span class="text-brand-lightGold text-sm tracking-wider">Advisory</span>
            </a>
            <a href="index.html#registration" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">联系我们</span>
                <span class="text-gray-200 text-sm tracking-wider">Contact</span>
            </a>
        </nav>"""

content = re.sub(r'<nav class="flex flex-col items-center gap-8 w-full">.*?</nav>', new_mobile_nav, content, flags=re.DOTALL)

# 2. Remove dark overlay for the advisor team section
# From:
# <section class="relative py-20 text-center bg-cover bg-center bg-no-repeat" style="background-image: url('images/Gemini_Generated_Image_2c69zr2c69zr2c69-2.png');">
#     <div class="absolute inset-0 bg-[#0a0a0a]/60"></div>

old_advising_intro = """        <section class="relative py-20 text-center bg-cover bg-center bg-no-repeat" style="background-image: url('images/Gemini_Generated_Image_2c69zr2c69zr2c69-2.png');">
            <div class="absolute inset-0 bg-[#0a0a0a]/60"></div>
            <div class="max-w-4xl mx-auto px-6 relative z-10">"""
            
new_advising_intro = """        <section class="relative py-20 text-center bg-cover bg-center bg-no-repeat" style="background-image: url('images/Gemini_Generated_Image_2c69zr2c69zr2c69-2.png');">
            <div class="max-w-4xl mx-auto px-6 relative z-10">"""

content = content.replace(old_advising_intro, new_advising_intro)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Advisory updated")
