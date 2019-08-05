AMLEO Run
self.saveConvertedPages()

AMLEO Impl
def saveConvertedPages(self):
    for file in self.pageFiles:
        fileName = "{0}/{1}".format(self.OUTPUT_DIR, file.name)
        with (open(fileName, "w")) as f:
            f.write(file.contents)
