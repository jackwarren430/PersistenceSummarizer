from taipy.gui import Markdown
from taipy import Gui

Gui(page = "# This is my page title")

testPage = Markdown("""
#Test Title
                    
Any [*Markdown*](https://www.youtube.com/watch?v=OpHAncCb8Zo) content can be used here.
""")