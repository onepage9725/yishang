import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 奇门遁甲咨询 Mobile
item7_old = """                <!-- Item 7 -->
                <div class="md:col-span-2 bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 flex justify-center">
                    <div class="flex gap-4 items-start max-w-sm">"""
item7_new = """                <!-- Item 7 -->
                <div class="md:col-span-2 bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6">
                    <div class="flex gap-4 items-start">"""
content = content.replace(item7_old, item7_new)

# Fix Why Choose Us Top Row for Mobile (2 columns)
top_row_old = """                <!-- Top Row: 4 Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
                    <!-- Card 1 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-8 flex flex-col items-center text-center group">
                        <div class="w-16 h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-3xl text-[#e6c589]">👤</span>
                        </div>
                        <h4 class="text-lg font-serif text-[#e6c589] tracking-wider mb-4">长卿老师亲自培养</h4>
                        <p class="text-gray-400 text-sm tracking-wider leading-relaxed">所有顾问老师均接受系统化培训，并在长卿老师指导下持续提升。</p>
                    </div>
                    
                    <!-- Card 2 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-8 flex flex-col items-center text-center group">
                        <div class="w-16 h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-3xl text-[#e6c589]">📖</span>
                        </div>
                        <h4 class="text-lg font-serif text-[#e6c589] tracking-wider mb-4">理论结合实战</h4>
                        <p class="text-gray-400 text-sm tracking-wider leading-relaxed">不仅懂传统文化，更具备企业与人生规划的实战经验。</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-8 flex flex-col items-center text-center group">
                        <div class="w-16 h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-3xl text-[#e6c589]">👥</span>
                        </div>
                        <h4 class="text-lg font-serif text-[#e6c589] tracking-wider mb-4">一对一精准服务</h4>
                        <p class="text-gray-400 text-sm tracking-wider leading-relaxed">根据个人或企业实际情况，提供针对性的建议与布局。</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-8 flex flex-col items-center text-center group">
                        <div class="w-16 h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-3xl text-[#e6c589]">🎯</span>
                        </div>
                        <h4 class="text-lg font-serif text-[#e6c589] tracking-wider mb-4">系统化解决方案</h4>
                        <p class="text-gray-400 text-sm tracking-wider leading-relaxed">从问题分析到具体执行，帮助客户真正落地。</p>
                    </div>
                </div>"""

top_row_new = """                <!-- Top Row: 4 Cards -->
                <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 md:gap-6 mb-6">
                    <!-- Card 1 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-4 md:p-8 flex flex-col items-center text-center group">
                        <div class="w-12 h-12 md:w-16 md:h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-4 md:mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-2xl md:text-3xl text-[#e6c589]">👤</span>
                        </div>
                        <h4 class="text-sm md:text-lg font-serif text-[#e6c589] tracking-wider mb-2 md:mb-4">长卿老师亲自培养</h4>
                        <p class="text-gray-400 text-xs md:text-sm tracking-wider leading-relaxed">所有顾问老师均接受系统化培训，并在长卿老师指导下持续提升。</p>
                    </div>
                    
                    <!-- Card 2 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-4 md:p-8 flex flex-col items-center text-center group">
                        <div class="w-12 h-12 md:w-16 md:h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-4 md:mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-2xl md:text-3xl text-[#e6c589]">📖</span>
                        </div>
                        <h4 class="text-sm md:text-lg font-serif text-[#e6c589] tracking-wider mb-2 md:mb-4">理论结合实战</h4>
                        <p class="text-gray-400 text-xs md:text-sm tracking-wider leading-relaxed">不仅懂传统文化，更具备企业与人生规划的实战经验。</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-4 md:p-8 flex flex-col items-center text-center group">
                        <div class="w-12 h-12 md:w-16 md:h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-4 md:mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-2xl md:text-3xl text-[#e6c589]">👥</span>
                        </div>
                        <h4 class="text-sm md:text-lg font-serif text-[#e6c589] tracking-wider mb-2 md:mb-4">一对一精准服务</h4>
                        <p class="text-gray-400 text-xs md:text-sm tracking-wider leading-relaxed">根据个人或企业实际情况，提供针对性的建议与布局。</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="bg-[#0f0e0c] border border-[#2a2118] hover:border-[#d4af37]/50 transition-colors duration-300 rounded-xl p-4 md:p-8 flex flex-col items-center text-center group">
                        <div class="w-12 h-12 md:w-16 md:h-16 flex items-center justify-center rounded-full bg-[#1a1714] border border-[#d4af37]/30 mb-4 md:mb-6 group-hover:bg-[#d4af37]/10 transition-colors">
                            <span class="text-2xl md:text-3xl text-[#e6c589]">🎯</span>
                        </div>
                        <h4 class="text-sm md:text-lg font-serif text-[#e6c589] tracking-wider mb-2 md:mb-4">系统化解决方案</h4>
                        <p class="text-gray-400 text-xs md:text-sm tracking-wider leading-relaxed">从问题分析到具体执行，帮助客户真正落地。</p>
                    </div>
                </div>"""

content = content.replace(top_row_old, top_row_new)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated successfully")
