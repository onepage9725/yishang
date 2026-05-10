with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1st card
old_img1 = 'img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-luminosity group-hover:opacity-30 transition-opacity duration-500"'
new_img1 = 'img src="images/3section.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-40 mix-blend-luminosity group-hover:opacity-50 transition-opacity duration-500"'
content = content.replace(old_img1, new_img1)

old_over1 = 'div class="absolute inset-0 bg-gradient-to-br from-[#0a0a0a]/20 to-[#0a0a0a]/20"'
new_over1 = 'div class="absolute inset-0 bg-gradient-to-br from-[#0a0a0a]/10 to-[#0a0a0a]/5"'
content = content.replace(old_over1, new_over1)

# 2nd card
old_img2_1 = 'img src="images/qimen.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-10 mix-blend-luminosity group-hover:opacity-20 transition-opacity duration-500"'
old_img2_2 = 'img src="images/qimen.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-20 mix-blend-luminosity group-hover:opacity-20 transition-opacity duration-500"'
new_img2 = 'img src="images/qimen.jpg" alt="Background" class="absolute inset-0 w-full h-full object-cover opacity-40 mix-blend-luminosity group-hover:opacity-50 transition-opacity duration-500"'
content = content.replace(old_img2_1, new_img2)
content = content.replace(old_img2_2, new_img2)

old_over2 = 'div class="absolute inset-0 bg-gradient-to-t from-[#0a0a0a]/20 to-[#0a0a0a]/20"'
new_over2 = 'div class="absolute inset-0 bg-gradient-to-t from-[#0a0a0a]/10 to-[#0a0a0a]/5"'
content = content.replace(old_over2, new_over2)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed")
