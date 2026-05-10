import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make titles even bigger and restore tracking, fix the flex wrappers
html = re.sub(
    r'<div class="flex gap-4 items-start">\s*<div>\s*<h4 class="text-\[#e6c589\] font-serif text-xl mb-4">',
    r'<div>\n                            <h4 class="text-[#e6c589] font-serif text-2xl tracking-widest mb-4">',
    html
)

html = re.sub(
    r'<div class="flex gap-4 items-start max-w-sm">\s*<div>\s*<h4 class="text-\[#e6c589\] font-serif text-xl mb-4">',
    r'<div>\n                            <h4 class="text-[#e6c589] font-serif text-2xl tracking-widest mb-4">',
    html
)

html = re.sub(
    r'<div class="flex gap-4 items-start">\s*<div>\s*<h4 class="text-\[#e6c589\] font-serif text-lg mb-4">',
    r'<div>\n                            <h4 class="text-[#e6c589] font-serif text-xl tracking-widest mb-4">',
    html
)

html = re.sub(
    r'<div class="flex gap-4 items-start max-w-sm">\s*<div>\s*<h4 class="text-\[#e6c589\] font-serif text-lg mb-4">',
    r'<div>\n                            <h4 class="text-[#e6c589] font-serif text-xl tracking-widest mb-4">',
    html
)

html = html.replace('                        <div class="flex gap-4 items-start">\n                            \n                            <div>', '                        <div class="block">\n')
html = html.replace('                    <div class="flex gap-4 items-start max-w-sm">\n                        \n                        <div>', '                    <div class="block max-w-sm mx-auto">\n')
html = html.replace('                    <div class="flex gap-4 items-start">\n                        \n                        <div>', '                    <div class="block">\n')



with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Titles enlarged and wrappers cleaned!")
