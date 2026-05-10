import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's fix the mobile view which might also have broken divs
text = text.replace(
    '''                        </div>
                    </div>
                </div>''',
    '''                    </div>
                </div>'''
)

with open('advisory.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
