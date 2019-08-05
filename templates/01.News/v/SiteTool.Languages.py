AMLEO Cfg
self.LANGUAGES = ["en", "ru"]

AMLEO Loop
for language in self.LANGUAGES:
    self.INPUT_DIR = "{0}/data/news-{1}".format(self.DIR, language)
    self.OUTPUT_DIR = "{0}/{1}/news".format(self.DIR, language)

AMLEO RunItem
self.setLanguageLinks(self.newsFiles, language, "../../{0}/news/{1}")

AMLEO RunPreview
self.setLanguageLinks(self.previewPageFiles, language, "../../{0}/news/{1}")

AMLEO Debug
print("Language: '{0}'".format(language))

AMLEO Impl
def setLanguageLinks(self, files, currentLanguage, linkFormat):
    for file in files:
        contents = file.contents
        for language in self.LANGUAGES:
            token = "{0}_{1}".format("LANGUAGE", language)
            # The same language.
            if (language == currentLanguage):
                path = file.name
            # Another language.
            else:
                path = linkFormat.format(language, file.name)
            contents = contents.replace(token, path)
        file.contents = contents
