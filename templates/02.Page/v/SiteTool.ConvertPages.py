AMLEO Import
import pypandoc

AMLEO Run
self.convertPages()

AMLEO Debug
self.printConvertedPages()

AMLEO Impl
def convertPages(self):
    self.pageFiles = []
    for pageItem in self.pageItems:
        name = "{0}.html".format(pageItem.slug)
        contents = self.convertPageItem(pageItem, name)
        file = File(name, contents)
        self.pageFiles.append(file)

def convertPageItem(self, item, fileName):
    contents = self.pageTemplate

    contents = contents.replace("PAGE_ITEM_TITLE", item.title)

    html = pypandoc.convert_text(item.contents, "html", format = "md")
    html = html.encode("utf-8")
    contents = contents.replace("PAGE_ITEM_CONTENTS", html)
    
    return contents

def printConvertedPages(self):
    print("Converted page items as files:")
    for item in self.pageFiles:
        print(str(item))
