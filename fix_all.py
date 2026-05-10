import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix consulting services mobile layout (2 in a row)
old_mobile_wrap = """            <!-- Mobile Fallback Layout -->
            <div class="lg:hidden grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 mt-10">"""
new_mobile_wrap = """            <!-- Mobile Fallback Layout -->
            <div class="lg:hidden grid grid-cols-2 gap-3 md:gap-6 mt-10">"""
content = content.replace(old_mobile_wrap, new_mobile_wrap)

# 2. Fix Item 7 style on mobile
# Also make sure mobile cards have slightly smaller text so 2-in-a-row fits
old_item7_part1 = """                <!-- Item 7 -->
                <div class="md:col-span-2 bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 flex justify-center">"""
new_item7_part1 = """                <!-- Item 7 -->
                <div class="col-span-2 bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-4 md:p-6">"""
content = content.replace(old_item7_part1, new_item7_part1)

old_item7_part2 = """                    <div class="block text-left relative max-w-sm w-full">"""
new_item7_part2 = """                    <div class="block">"""
content = content.replace(old_item7_part2, new_item7_part2)

old_item_template = """<div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6">"""
new_item_template = """<div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-4 md:p-6">"""
content = content.replace(old_item_template, new_item_template)

# Make 2-in-a-row texts slightly smaller
content = content.replace("""<h4 class="text-[#e6c589] font-serif text-xl tracking-widest mb-4">""", """<h4 class="text-[#e6c589] font-serif text-sm md:text-xl tracking-widest mb-2 md:mb-4">""")
content = content.replace("""<ul class="text-gray-400 text-sm tracking-wider space-y-2">""", """<ul class="text-gray-400 text-xs md:text-sm tracking-wider space-y-1.5 md:space-y-2">""")
content = content.replace("""before:text-lg before:font-bold">""", """before:text-sm md:before:text-lg before:font-bold">""")


# 3. Bottom row updates:
old_bottom_row = """                <!-- Bottom Row: 3 Columns -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    <!-- Target Audience (Left Box spans 5 cols) -->
                    <div class="lg:col-span-4 bg-[#0f0e0c] border border-[#2a2118] rounded-xl p-8 relative overflow-hidden group hover:border-[#d4af37]/50 transition-colors">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#d4af37]/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                        <h4 class="text-2xl font-serif text-[#e6c589] tracking-widest mb-8 relative z-10">服务对象</h4>
                        <ul class="space-y-4 text-gray-300 text-sm tracking-wider relative z-10">
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 企业家</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 创业者</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 投资者</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👑</span> 高净值人士</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👔</span> 专业人士</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👨‍👩‍👧‍👦</span> 希望改善人生方向的个人与家庭</li>
                        </ul>
                    </div>

                    <!-- Mission (Middle Box spans 4 cols) -->
                    <div class="lg:col-span-4 bg-[#0f0e0c] border border-[#2a2118] rounded-xl p-8 md:p-12 flex flex-col items-center justify-center text-center relative hover:border-[#d4af37]/50 transition-colors">
                        <h4 class="text-2xl font-serif text-[#e6c589] tracking-widest mb-8">我们的使命</h4>
                        <p class="text-gray-300 text-base md:text-lg tracking-wider leading-loose mb-10">
                            以东方智慧为根，以现代思维为桥，<br/>
                            帮助更多人在复杂的时代中找到方向，<br/>
                            实现事业、财富、家庭与人生的<br/>
                            整体提升。
                        </p>
                        <div class="text-[#d4af37] text-3xl">🪷</div>
                    </div>

                    <!-- Right Box (Image spans 4 cols) -->
                    <div class="lg:col-span-4 border border-[#2a2118] rounded-xl overflow-hidden relative min-h-[300px] flex items-center justify-center bg-[#0a0a0a]">
                        <img src="images/qimen.jpg" alt="东方智慧" class="absolute inset-0 w-full h-full object-cover opacity-60 mix-blend-screen" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#0a0a0a] via-transparent to-transparent"></div>
                    </div>
                </div>"""

new_bottom_row = """                <!-- Bottom Row: 2 Columns -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <!-- Target Audience -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] rounded-xl p-8 md:p-12 relative overflow-hidden group hover:border-[#d4af37]/50 transition-colors">
                        <!-- Background Image -->
                        <img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-luminosity group-hover:opacity-30 transition-opacity duration-500" />
                        <div class="absolute inset-0 bg-gradient-to-br from-[#0a0a0a]/80 to-[#0a0a0a]/40"></div>
                        <div class="absolute inset-0 bg-gradient-to-br from-[#d4af37]/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                        
                        <h4 class="text-2xl font-serif text-[#e6c589] tracking-widest mb-8 relative z-10">服务对象</h4>
                        <ul class="space-y-4 text-gray-300 text-sm md:text-base tracking-wider relative z-10">
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 企业家</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 创业者</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👤</span> 投资者</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👑</span> 高净值人士</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👔</span> 专业人士</li>
                            <li class="flex items-center gap-3"><span class="text-[#d4af37] text-lg">👨‍👩‍👧‍👦</span> 希望改善人生方向的个人与家庭</li>
                        </ul>
                    </div>

                    <!-- Mission -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] rounded-xl p-8 md:p-12 relative overflow-hidden flex flex-col items-center justify-center text-center group hover:border-[#d4af37]/50 transition-colors">
                        <!-- Background Image -->
                        <img src="images/qimen.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-10 mix-blend-luminosity group-hover:opacity-20 transition-opacity duration-500" />
                        <div class="absolute inset-0 bg-gradient-to-t from-[#0a0a0a]/90 to-[#0a0a0a]/40"></div>
                        
                        <h4 class="text-2xl font-serif text-[#e6c589] tracking-widest mb-8 relative z-10">我们的使命</h4>
                        <p class="text-gray-300 text-base md:text-lg tracking-wider leading-loose mb-10 relative z-10">
                            以东方智慧为根，以现代思维为桥，<br/>
                            帮助更多人在复杂的时代中找到方向，<br/>
                            实现事业、财富、家庭与人生的<br/>
                            整体提升。
                        </p>
                        <div class="text-[#d4af37] text-3xl relative z-10">🪷</div>
                    </div>
                </div>"""

content = content.replace(old_bottom_row, new_bottom_row)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied")
