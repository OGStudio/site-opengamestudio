AMLEO Loop
for language in self.LANGUAGES:
    self.INPUT_DIR = "{0}/data/page-{1}".format(self.DIR, language)
    self.OUTPUT_DIR = "{0}/{1}/page".format(self.DIR, language)

AMLEO Run
self.setLanguageLinks(self.pageFiles, language, "../../{0}/page/{1}")
