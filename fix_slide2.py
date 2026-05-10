import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

old_string = """            <!-- Slide 2 -->
            <div class="slide absolute inset-0 w-full h-full flex items-center justify-center transition-opacity duration-1000 opacity-0 z-0 bg-[#060606] pointer-events-none">
                <div class="absolute inset-0 bg-cover bg-center blur-md opacity-20" style="background-image: url('images/顾问团队 最新.jpeg');"></div>
                <img src="images/顾问团队 最新.jpeg" alt="顾问团队" class="relative z-10 w-full max-h-full object-contain p-4 md:p-8 drop-shadow-2xl" />
            </div>"""

new_string = """            <!-- Slide 2 -->
            <div class="slide absolute inset-0 w-full h-full flex items-center justify-center transition-opacity duration-1000 opacity-0 z-0 bg-black pointer-events-none">
                <a href="advisory.html" class="w-full relative z-10 block cursor-pointer">
                    <img src="images/顾问团队 最新.jpeg" alt="顾问团队" class="w-full h-auto block" />
                </a>
            </div>"""

if old_string in content:
    content = content.replace(old_string, new_string)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Replacements successful.")
else:
    print("String not found. Trying regex...")
    # fallback
    pattern = re.compile(r'<!-- Slide 2 -->\s*<div class="slide[^>]+>\s*<div class="absolute inset-0[^>]+></div>\s*<img src="images/顾问团队 最新.jpeg"[^>]+>\s*</div>')
    if pattern.search(content):
        content = pattern.sub(new_string, content)
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("Regex replacement successful.")
    else:
        print("Regex also failed to find.")
