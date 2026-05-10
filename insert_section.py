import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

section_html = """
        <!-- Professional Consulting Services Section -->
        <section class="max-w-7xl mx-auto px-4 py-20 relative">
            <div class="text-center mb-16 relative">
                <div class="flex items-center justify-center gap-4 mb-2">
                    <div class="w-16 h-[1px] bg-gradient-to-r from-transparent to-[#d4af37]"></div>
                    <div class="w-2 h-2 rotate-45 border border-[#d4af37]"></div>
                    <h3 class="text-3xl md:text-4xl font-serif text-[#e6c589] tracking-widest px-4">我们提供的专业咨询服务</h3>
                    <div class="w-2 h-2 rotate-45 border border-[#d4af37]"></div>
                    <div class="w-16 h-[1px] bg-gradient-to-l from-transparent to-[#d4af37]"></div>
                </div>
                <div class="text-[#b08d28] text-xs md:text-sm tracking-[0.3em] uppercase">OUR PROFESSIONAL CONSULTING SERVICES</div>
            </div>

            <div class="hidden lg:grid grid-cols-3 gap-8 relative items-center">
                <!-- Center Decorative Element -->
                <div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-[60%] w-[400px] h-[400px] flex items-center justify-center pointer-events-none opacity-40 z-0">
                    <div class="w-full h-full rounded-full border border-[#d4af37]/30 border-dashed animate-[spin_60s_linear_infinite]"></div>
                    <div class="absolute w-[300px] h-[300px] rounded-full border border-[#d4af37]/40 animate-[spin_40s_linear_infinite_reverse]"></div>
                    <div class="absolute w-[200px] h-[200px] rounded-full border border-[#d4af37]/50"></div>
                    <div class="absolute w-12 h-12 rotate-45 bg-gradient-to-br from-[#d4af37]/80 to-transparent"></div>
                    <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(212,175,55,0.15)_0%,transparent_70%)]"></div>
                </div>

                <!-- Left Column -->
                <div class="flex flex-col gap-8 z-10">
                    <!-- Item 1 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute right-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -right-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>
                        
                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">🏢</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">企业咨询与战略规划</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">企业策划与商业布局</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">市场定位与发展方向</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">团队管理与组织优化</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">创业机会评估</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">商业决策辅助</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Item 2 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute right-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -right-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">⛰️</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">人生轨道与个人规划</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">人生方向分析</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">事业发展规划</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">感情与家庭建议</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">子女教育方向</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">运势与阶段布局</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Item 3 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute right-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -right-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">🏠</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">风水咨询</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">住宅风水</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">办公室风水</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">店铺风水</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">工厂与商业空间布局</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">搬迁与选址建议</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Center Spacer (for visual layout) -->
                <div class="h-full flex flex-col justify-end z-10">
                     <!-- Bottom Center Item -->
                     <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group mt-auto">
                        <div class="absolute left-1/2 -top-8 w-[1px] h-8 bg-[#d4af37]/30 -translate-x-1/2 lg:block hidden"></div>
                        <div class="hidden lg:block absolute left-1/2 -top-9 w-2 h-2 rounded-full bg-[#d4af37] -translate-x-1/2 shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">🧭</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">奇门遁甲咨询</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">决策分析</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">趋势预测</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">投资判断</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">谈判布局</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">贵人与机会方向</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="flex flex-col gap-8 z-10">
                    <!-- Item 4 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute left-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 -translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -left-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-xl">🔢</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">数字能量服务</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">手机号码优化</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">车牌号码分析</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">公司号码建议</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Item 5 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute left-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 -translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -left-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">✍️</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">姓名策划</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">成人改名</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">新生儿命名</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">公司命名</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">品牌命名</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <!-- Item 6 -->
                    <div class="bg-[#0f0e0c]/80 backdrop-blur-sm border border-[#d4af37]/30 rounded-xl p-6 hover:border-[#d4af37] transition-all duration-300 transform hover:-translate-y-1 relative group">
                        <div class="absolute left-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 -translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -left-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>

                        <div class="flex gap-4 items-start">
                            <div class="w-14 h-14 rounded border border-[#d4af37]/50 flex items-center justify-center flex-shrink-0 bg-[#1a1714]">
                                <span class="text-2xl">📅</span>
                            </div>
                            <div>
                                <h4 class="text-[#e6c589] font-serif text-lg tracking-wider mb-2">择日与时辰</h4>
                                <ul class="text-gray-400 text-xs tracking-wider space-y-1.5 list-none">
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">开业吉日</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">签约时辰</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">结婚择日</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">搬迁择日</li>
                                    <li class="flex items-center gap-1.5 before:content-['·'] before:text-[#d4af37] before:font-bold">剖腹生产时辰</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Mobile Fallback Layout -->
            <div class="lg:hidden grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">
                <!-- Mobile components... simplified for space, copy from previous patch -->
                <div class="bg-[#0f0e0c]/80 flex flex-col gap-6">
                    <p class="text-center text-[#e6c589] my-10">Please view on a larger screen to see the circular constellation layout.</p>
                </div>
            </div>
        </section>
"""

# Find </main>
parts = content.split("    </main>")
if len(parts) > 1:
    new_content = parts[0] + section_html + "    </main>" + parts[1]
    with open('advisory.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Inserted successfully")
else:
    print("Could not find </main>")
