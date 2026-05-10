import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure that there are no rogue divs in the structure from previous edits
print("Validating divs...")
blocks = html.split('<section class="w-full relative py-20 bg-cover bg-center bg-no-repeat"')
if len(blocks) > 1:
    section_part = blocks[1].split('</section>')[0]
    div_opens = section_part.count('<div')
    div_closes = section_part.count('</div')
    print(f"Section 1 opens: {div_opens}, closes: {div_closes}")

