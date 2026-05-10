with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = """                    </div>
                </div>
            </div>
        </section>"""

new_text = """                    </div>
                </div>

                <!-- Call to Action -->
                <div class="mt-8 border border-[#2a2118] rounded-xl overflow-hidden relative bg-[#0a0a0a] group hover:border-[#d4af37]/50 transition-colors">
                    <!-- Background Images Split -->
                    <div class="absolute inset-0 flex justify-between pointer-events-none opacity-20 mix-blend-luminosity">
                        <img src="images/qimen.jpg" alt="Left Art" class="w-1/2 h-full object-cover [mask-image:linear-gradient(to_right,rgba(0,0,0,1)_30%,transparent_100%)]" />
                        <img src="images/3section.jpg" alt="Right Art" class="w-1/2 h-full object-cover [mask-image:linear-gradient(to_left,rgba(0,0,0,1)_30%,transparent_100%)]" />
                    </div>
                    <div class="absolute inset-0 bg-gradient-to-r from-[#0a0a0a]/90 via-[#0a0a0a]/70 to-[#0a0a0a]/90"></div>
                    
                    <div class="relative z-10 p-8 md:p-12 flex flex-col lg:flex-row items-center justify-between gap-8 text-center lg:text-left">
                        <div class="flex-1">
                            <h3 class="text-3xl lg:text-4xl font-serif text-[#e6c589] tracking-widest mb-3">预约专属咨询</h3>
                            <p class="text-[#b08d28] text-xs lg:text-sm tracking-[0.2em] uppercase mb-6">Book Your Private Consultation</p>
                            <p class="text-gray-400 text-sm lg:text-base tracking-wider leading-relaxed">
                                如果您希望获得更精准的个人或企业方向建议，<br class="hidden lg:block" />
                                欢迎预约易商顾问团队的一对一专属咨询服务。
                            </p>
                        </div>
                        <div class="flex-none">
                            <a href="index.html" class="inline-flex bg-[#cca66b] hover:bg-[#e8cfa1] text-[#0a0a0a] font-serif font-bold tracking-widest px-8 md:px-10 py-4 items-center justify-center gap-4 transition-colors duration-300 rounded group">
                                立即预约咨询
                                <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

content = content.replace(old_text, new_text)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added CTA successfully")
