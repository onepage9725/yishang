with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_bg = """                    <!-- Background Images Split -->
                    <div class="absolute inset-0 flex justify-between pointer-events-none opacity-20 mix-blend-luminosity">
                        <img src="images/qimen.jpg" alt="Left Art" class="w-1/2 h-full object-cover [mask-image:linear-gradient(to_right,rgba(0,0,0,1)_30%,transparent_100%)]" />
                        <img src="images/3section.jpg" alt="Right Art" class="w-1/2 h-full object-cover [mask-image:linear-gradient(to_left,rgba(0,0,0,1)_30%,transparent_100%)]" />
                    </div>"""

new_bg = """                    <!-- Background Image -->
                    <img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-30 mix-blend-luminosity pointer-events-none group-hover:opacity-40 transition-opacity duration-500" />"""

content = content.replace(old_bg, new_bg)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CTA background updated")
