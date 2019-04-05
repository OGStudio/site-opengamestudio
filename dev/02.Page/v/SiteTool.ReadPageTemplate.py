AMLEO Cfg
self.PAGE_TEMPLATE_FILE_NAME = "{0}.page.html".format(language)

AMLEO Run
self.readPageTemplate()

AMLEO Impl
def readPageTemplate(self):
    fileName = "{0}/{1}".format(self.INPUT_DIR, self.PAGE_TEMPLATE_FILE_NAME)
    with (open(fileName, "r")) as f:
        self.pageTemplate = f.read()
