import urllib.parse
with open('advisory.html', 'r', encoding='utf-8') as f:
    content = f.read()

msg = "你好，要了解易商企业与个人咨询服务，谢谢"
encoded_msg = urllib.parse.quote(msg)
wa_link = f"https://wa.me/601153911319?text={encoded_msg}"

old_btn = """<a href="index.html" class="inline-flex bg-[#cca66b] hover:bg-[#e8cfa1] text-[#0a0a0a] font-serif font-bold tracking-widest px-8 md:px-10 py-4 items-center justify-center gap-4 transition-colors duration-300 rounded group">
                                立即预约咨询"""

new_btn = f"""<a href="{wa_link}" target="_blank" rel="noopener noreferrer" class="inline-flex bg-[#cca66b] hover:bg-[#e8cfa1] text-[#0a0a0a] font-serif font-bold tracking-widest px-8 md:px-10 py-4 items-center justify-center gap-4 transition-colors duration-300 rounded group">
                                立即预约咨询"""

content = content.replace(old_btn, new_btn)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("CTA link updated")
