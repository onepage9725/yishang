import glob

html_files = ["index.html", "advisory.html"]

old_header = '<header class="flex justify-between items-center py-4 px-6 md:py-6 md:px-12 border-b border-gray-800 fixed md:absolute top-0 w-full z-50 bg-[#0a0a0a]/90 backdrop-blur-md md:bg-transparent">'
new_header = '<header class="flex justify-between items-center py-4 px-6 md:py-6 md:px-12 border-b border-gray-800 fixed top-0 w-full z-50 bg-[#0a0a0a]/90 backdrop-blur-md">'

for file_path in html_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if old_header in content:
            content = content.replace(old_header, new_header)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated header in {file_path}")
        else:
            print(f"Header not found in {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

