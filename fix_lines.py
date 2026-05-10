import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Left Column lines
left_col_old = """                        <div class="absolute right-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -right-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>"""

left_col_new = """                        <!-- Connecting Line to Center -->
                        <div class="hidden lg:block absolute right-0 top-1/2 w-16 lg:w-24 xl:w-32 h-[1px] bg-gradient-to-r from-[#d4af37]/0 via-[#d4af37]/50 to-[#d4af37] translate-x-full z-[-1]"></div>
                        <div class="hidden lg:block absolute -right-[4.25rem] lg:-right-[6.25rem] xl:-right-[8.25rem] top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_15px_3px_rgba(212,175,55,0.8)]"></div>"""

content = content.replace(left_col_old, left_col_new)

# Replace Right Column lines
right_col_old = """                        <div class="absolute left-0 top-1/2 w-8 h-[1px] bg-[#d4af37]/30 -translate-x-full lg:block hidden"></div>
                        <div class="hidden lg:block absolute -left-9 top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_10px_#d4af37]"></div>"""

right_col_new = """                        <!-- Connecting Line to Center -->
                        <div class="hidden lg:block absolute left-0 top-1/2 w-16 lg:w-24 xl:w-32 h-[1px] bg-gradient-to-l from-[#d4af37]/0 via-[#d4af37]/50 to-[#d4af37] -translate-x-full z-[-1]"></div>
                        <div class="hidden lg:block absolute -left-[4.25rem] lg:-left-[6.25rem] xl:-left-[8.25rem] top-1/2 w-2 h-2 rounded-full bg-[#d4af37] translate-y-[-50%] shadow-[0_0_15px_3px_rgba(212,175,55,0.8)]"></div>"""

content = content.replace(right_col_old, right_col_new)

# Replace Bottom Center lines
center_col_old = """                        <div class="absolute left-1/2 -top-8 w-[1px] h-8 bg-[#d4af37]/30 -translate-x-1/2 lg:block hidden"></div>
                        <div class="hidden lg:block absolute left-1/2 -top-9 w-2 h-2 rounded-full bg-[#d4af37] -translate-x-1/2 shadow-[0_0_10px_#d4af37]"></div>"""

center_col_new = """                        <!-- Connecting Line to Center -->
                        <div class="hidden lg:block absolute left-1/2 -top-16 lg:-top-24 xl:-top-32 w-[1px] h-16 lg:h-24 xl:h-32 bg-gradient-to-t from-[#d4af37]/0 via-[#d4af37]/50 to-[#d4af37] -translate-x-1/2 z-[-1]"></div>
                        <div class="hidden lg:block absolute left-1/2 -top-[4.25rem] lg:-top-[6.25rem] xl:-top-[8.25rem] w-2 h-2 rounded-full bg-[#d4af37] -translate-x-1/2 -translate-y-1/2 shadow-[0_0_15px_3px_rgba(212,175,55,0.8)]"></div>"""

content = content.replace(center_col_old, center_col_new)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Lines modified")

