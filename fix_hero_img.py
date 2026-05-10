with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_hero = """        <div class="w-full flex items-center justify-center bg-black min-h-[60vh] md:min-h-[80vh]">
            <img src="images/顾问团队 最新.jpeg" alt="顾问团队" class="w-full h-full object-contain max-h-[80vh]" />
        </div>"""

new_hero = """        <div class="w-full bg-black">
            <img src="images/顾问团队 最新.jpeg" alt="顾问团队" class="w-full h-auto block" />
        </div>"""

content = content.replace(old_hero, new_hero)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero updated")
