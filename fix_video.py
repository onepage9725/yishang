import re

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

old_video = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover cursor-pointer" autoplay muted loop playsinline onclick="this.muted = !this.muted"></video>'
new_video = '<video id="heroVideo" src="https://video.wixstatic.com/video/4c6e32_b1389e038add482a9b90f76329b2a1c7/1080p/mp4/file.mp4" class="w-full h-full object-cover cursor-pointer" autoplay muted loop playsinline onmouseover="this.muted=false" onmouseout="this.muted=true" onclick="this.muted = !this.muted"></video>'

if old_video in index_content:
    index_content = index_content.replace(old_video, new_video)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("Video updated with hover events")
