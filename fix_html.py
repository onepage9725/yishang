import re

with open('advisory.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's completely recreate the content of the grid to ensure standard layout without extra closing divs.

print("Fixing broken divs...")

def remove_extra_divs(match):
    # This matches the inside of the card from `<div class="absolute...` to the end of the item `</div><!-- Item X -->`
    content = match.group(0)
    # The structure has `<div><h4...</ul></div></div></div>` -> 3 closing divs
    # We should only have `<div><h4...</ul></div></div>` -> 2 closing divs (one for the wrapper, one for the outer card)
    content = re.sub(r'                            </div>\n                        </div>\n                    </div>', 
                     r'                        </div>\n                    </div>', content)
    
    return content

# Let's just fix the mismatched divs first
text = text.replace(
    '''                            </div>
                        </div>
                    </div>''',
    '''                        </div>
                    </div>'''
)

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
