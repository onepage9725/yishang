import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

old_str = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover cursor-pointer" autoplay muted loop playsinline onmouseover="this.muted=false" onmouseout="this.muted=true" onclick="this.muted = !this.muted"></video>'
new_str = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover" autoplay muted loop playsinline></video>'

if old_str in content:
    content = content.replace(old_str, new_str)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Video updated to autoplay without sound successfully.")
else:
    print("Could not find the exact video string.")
