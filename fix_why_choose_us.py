import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

section_html = """
        <!-- Why Choose Us Section -->
        <section class="w-full relative py-24 bg-[#0a0a0a]">
            <div class="max-w-7xl mx-auto px-4 relative z-10">
                <!-- Header -->
                <div class="text-center mb-16 relative">
                    <div class="flex items-center justify-center gap-4 mb-2">
                        <div class="w-16 h-[1px] bg-gradient-to-r from-transparent to-[#d4af37]"></div>
                        <div class="w-2 h-2 rotate-45 border border-[#d4af37]"></div>
                        <h3 class="text-3xl md:text-4xl font-serif text-[#e6c589] tracking-widest px-4">为什么选择易商顾问团队</h3>
                        <div class="w-2 h-2 rotate-45 border border-[#d4af37]"></div>
                        <div class="w-16 h-[1px] bg-gradient-to-l from-transparent to-[#d4af37]"></div>
                    </div>
                    <div class="text-[#b08d28] text-xs md:text-sm tracking-[0.3em] uppercase">WHY CHOOSE US</div>
                </div>

                <!-- Top Row: 4 Cards -->
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
                </div>

                <!-- Bottom Row: 3 Columns -->
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
                </div>
            </div>
        </section>
"""

# Insert right before </main>
parts = content.split('    </main>')
if len(parts) > 1:
    new_content = parts[0] + section_html + '    </main>' + parts[1]
    with open('advisory.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Section inserted.")
else:
    print("Could not find </main>")

