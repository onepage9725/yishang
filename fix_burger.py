import re

with open("advisory.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Right Actions to add Burger Button
old_actions = """        <!-- Right Actions -->
        <div class="flex items-center gap-4 md:gap-6">
            <a href="index.html#registration" class="hidden md:flex bg-[#d4b98c] hover:bg-brand-lightGold text-black flex-col items-center py-2 px-6 rounded-sm transition-colors">
                <span class="font-bold text-sm">立即报名</span>
                <span class="text-xs">Join Now</span>
            </a>
        </div>
    </header>"""

new_actions = """        <!-- Right Actions -->
        <div class="flex items-center gap-4 md:gap-6">
            <a href="index.html#registration" class="hidden md:flex bg-[#d4b98c] hover:bg-brand-lightGold text-black flex-col items-center py-2 px-6 rounded-sm transition-colors">
                <span class="font-bold text-sm">立即报名</span>
                <span class="text-xs">Join Now</span>
            </a>
            <!-- Mobile Menu Toggle -->
            <button id="menuBtn" class="md:hidden text-brand-lightGold focus:outline-none flex items-center justify-center">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path id="menuIcon" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div id="mobileMenu" class="fixed inset-0 bg-[#050505] z-40 hidden flex-col items-center justify-center pt-16 transition-all duration-300 opacity-0">
        <nav class="flex flex-col items-center gap-6 w-full max-h-[80vh] overflow-y-auto pb-10">
            <a href="index.html#home" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">首页</span>
                <span class="text-gray-200 text-sm tracking-wider">Home</span>
            </a>
            <a href="index.html#about" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">关于我们</span>
                <span class="text-gray-200 text-sm tracking-wider">About Us</span>
            </a>
            <a href="index.html#services" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">课程与产品</span>
                <span class="text-gray-200 text-sm tracking-wider">Programs</span>
            </a>
            <a href="index.html#programs" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">活动</span>
                <span class="text-gray-200 text-sm tracking-wider">Events</span>
            </a>
            <a href="advisory.html" class="mobile-nav-link flex flex-col items-center group w-full text-center">
                <span class="text-brand-lightGold font-semibold mb-1 text-xl">顾问团队</span>
                <span class="text-brand-lightGold text-sm tracking-wider">Advisory</span>
            </a>
            <a href="index.html#registration" class="mobile-nav-link flex flex-col items-center group opacity-80 hover:opacity-100 transition-opacity w-full text-center">
                <span class="text-gray-200 mb-1 text-xl">联系我们</span>
                <span class="text-gray-200 text-sm tracking-wider">Contact</span>
            </a>
            
            <a href="index.html#registration" class="mt-8 bg-[#d4b98c] hover:bg-[#c4a471] text-black flex flex-col items-center py-3 px-12 rounded-sm transition-colors">
                <span class="font-bold text-lg">立即报名</span>
                <span class="text-sm">Join Now</span>
            </a>
        </nav>
    </div>"""

if old_actions in content:
    content = content.replace(old_actions, new_actions)

with open("advisory.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Added mobile menu HTML")


with open("advisory.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add JS logic to advisory.html if not present
js_logic = """
    <script>
        const menuBtn = document.getElementById('menuBtn');
        const mobileMenu = document.getElementById('mobileMenu');
        const menuIcon = document.getElementById('menuIcon');
        const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
        let isMenuOpen = false;

        function toggleMenu() {
            isMenuOpen = !isMenuOpen;
            if (isMenuOpen) {
                mobileMenu.classList.remove('hidden');
                setTimeout(() => mobileMenu.classList.remove('opacity-0'), 10);
                menuIcon.setAttribute('d', 'M6 18L18 6M6 6l12 12'); // X icon
            } else {
                mobileMenu.classList.add('opacity-0');
                setTimeout(() => mobileMenu.classList.add('hidden'), 300);
                menuIcon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16'); // Hamburger
            }
        }

        if (menuBtn) {
            menuBtn.addEventListener('click', toggleMenu);
        }
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', toggleMenu);
        });
    </script>
</body>"""

if "function toggleMenu()" not in content:
    content = content.replace("</body>", js_logic)
    with open("advisory.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Added Mobile Menu JS Logic")
