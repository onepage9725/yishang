import re

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

with open("advisory.html", "r", encoding="utf-8") as f:
    advisory_content = f.read()

# Fix header index
old_header_idx = '<header class="flex justify-between items-center py-6 px-12 border-b border-gray-800 absolute top-0 w-full z-50">'
new_header_idx = '<header class="flex justify-between items-center py-4 px-6 md:py-6 md:px-12 border-b border-gray-800 fixed md:absolute top-0 w-full z-50 bg-[#0a0a0a]/90 backdrop-blur-md md:bg-transparent">'
if old_header_idx in index_content:
    index_content = index_content.replace(old_header_idx, new_header_idx)

# Fix header advisory
old_header_adv = '<header class="flex justify-between items-center py-6 px-12 border-b border-gray-800 absolute top-0 w-full z-50">'
new_header_adv = '<header class="flex justify-between items-center py-4 px-6 md:py-6 md:px-12 border-b border-gray-800 fixed md:absolute top-0 w-full z-50 bg-[#0a0a0a]/90 backdrop-blur-md md:bg-transparent">'
if old_header_adv in advisory_content:
    advisory_content = advisory_content.replace(old_header_adv, new_header_adv)

# Fix video in index
old_video = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover" controls playsinline></video>'
new_video = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover cursor-pointer" autoplay muted loop playsinline onclick="this.muted = !this.muted"></video>'
if old_video in index_content:
    index_content = index_content.replace(old_video, new_video)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

with open("advisory.html", "w", encoding="utf-8") as f:
    f.write(advisory_content)

print("Updates applied")
