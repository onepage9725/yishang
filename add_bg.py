with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = """        <!-- Content below hero -->
        <section class="max-w-4xl mx-auto px-6 py-20 text-center">"""

new_text = """        <!-- Content below hero -->
        <section class="relative py-20 text-center bg-cover bg-center bg-no-repeat" style="background-image: url('images/Gemini_Generated_Image_2c69zr2c69zr2c69-2.png');">
            <div class="absolute inset-0 bg-[#0a0a0a]/60"></div>
            <div class="max-w-4xl mx-auto px-6 relative z-10">"""

content = content.replace(old_text, new_text)

old_close = """                </a>
            </div>
        </section>

        <!-- Professional Consulting Services Section -->"""

new_close = """                </a>
            </div>
            </div>
        </section>

        <!-- Professional Consulting Services Section -->"""

content = content.replace(old_close, new_close)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BG")
