with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Desktop Nav - Index
idx_desktop_events = """            <a href="#programs" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">活动</span>
                <span class="text-gray-200 text-xs tracking-wider">Events</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>"""

idx_desktop_advisory = """            <a href="advisory.html" class="flex flex-col items-center group opacity-70 hover:opacity-100 transition-opacity">
                <span class="text-gray-200 mb-1">顾问团队</span>
                <span class="text-gray-200 text-xs tracking-wider">Advisory</span>
                <div class="w-6 h-[2px] bg-transparent mt-1 group-hover:bg-gray-400 transition-colors"></div>
            </a>"""

idx_content = idx_content.replace(idx_desktop_events, idx_desktop_events + "\n" + idx_desktop_advisory)

# Mobile Nav - Index
idx_mobile_events = """            <a href="#programs" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">活动</span>
                <span class="text-gray-200 text-sm tracking-wider">Events</span>
            </a>"""

idx_mobile_advisory = """            <a href="advisory.html" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">顾问团队</span>
                <span class="text-gray-200 text-sm tracking-wider">Advisory</span>
            </a>"""

idx_content = idx_content.replace(idx_mobile_events, idx_mobile_events + "\n" + idx_mobile_advisory)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Index updated")
