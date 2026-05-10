import os
import glob

html_files = glob.glob("*.html")

script_to_inject = """
    <!-- Disable Right Click and Developer Tools -->
    <script>
        // Disable right-click
        document.addEventListener('contextmenu', event => event.preventDefault());

        // Disable keyboard shortcuts
        document.addEventListener('keydown', function(event) {
            // F12
            if (event.code === 'F12') {
                event.preventDefault();
            }
            // Ctrl+Shift+I / Cmd+Option+I
            if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.code === 'KeyI') {
                event.preventDefault();
            }
            // Ctrl+Shift+J / Cmd+Option+J
            if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.code === 'KeyJ') {
                event.preventDefault();
            }
            // Ctrl+U / Cmd+Option+U
            if ((event.ctrlKey || event.metaKey) && event.code === 'KeyU') {
                event.preventDefault();
            }
            // Ctrl+Shift+C / Cmd+Option+C
            if ((event.ctrlKey || event.metaKey) && event.shiftKey && event.code === 'KeyC') {
                event.preventDefault();
            }
        });
        
        // Disable drag on images
        document.addEventListener('dragstart', function(e) {
            if (e.target.nodeName.toUpperCase() === "IMG") {
                e.preventDefault();
            }
        });
    </script>
</head>
"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "Disable Right Click and Developer Tools" not in content:
        content = content.replace("</head>", script_to_inject)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected into {file_path}")

