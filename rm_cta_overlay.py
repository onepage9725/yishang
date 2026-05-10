with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

overlay = '                    <div class="absolute inset-0 bg-gradient-to-r from-[#0a0a0a]/80 via-[#0a0a0a]/50 to-[#0a0a0a]/80"></div>\n'
content = content.replace(overlay, '')

# Also let's pump up the opacity of the master background image slightly so it pops without the gradient hiding it
img_old = 'img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-30'
img_new = 'img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-50'
content = content.replace(img_old, img_new)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Overlay removed")
