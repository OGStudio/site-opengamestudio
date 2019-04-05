AMLEO Import
import glob

AMLEO Run
self.readPages()

AMLEO Debug
self.printPages()

AMLEO Impl
def readPages(self):
    self.pageItems = []
    fileNames = glob.glob(self.INPUT_DIR + "/*.md")
    for fileName in fileNames:
        with (open(fileName, "r")) as f:
            contents = f.read()
            item = PageItem()
            item.parse(contents)
            self.pageItems.append(item)

def printPages(self):
    print("Page items:")
    for item in self.pageItems:
        print(str(item))
