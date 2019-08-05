#!/usr/bin/python

import os
import pypandoc
import pypandoc
import re
import glob
import glob
import pypandoc

class File(object):
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents
    def __str__(self):
        return (
            "File( " +
            "name: '{0}' ".format(self.name) +
            "contents length: '{0}' ".format(len(self.contents)) +
            ")"
        )
class NewsItem(object):
    def __init__(self):
        self.title = None
        self.date = None
        self.slug = None
        self.contents = ""
    def __str__(self):
        return (
            "NewsItem( " +
            "title: '{0}' ".format(self.title) +
            "date: '{0}' ".format(self.date) +
            "slug: '{0}' ".format(self.slug) +
            "contents length: '{0}' ".format(len(self.contents)) +
            ")"
        )
    def parse(self, fileContents):
        lines = fileContents.splitlines()
        for ln in lines:
            # Technical information.
            if (ln.startswith("Title:")):
                self.title = ln.replace("Title:", "").strip()
            elif (ln.startswith("Date:")):
                self.date = ln.replace("Date:", "").strip()
            elif (ln.startswith("Slug:")):
                self.slug = ln.replace("Slug:", "").strip()
            # Ignore unused technical information.
            elif (ln.startswith("Lang:")):
                pass
            elif (ln.startswith("Category:")):
                pass
            # Contents.
            else:
                self.contents += ln + "\n"
class PreviewPage(object):
    def __init__(self, newsItems, newsPreviews, newsFiles):
        self.items = newsItems
        self.previews = newsPreviews
        self.files = newsFiles
PageItem = NewsItem

class SiteTool(object):
    # Configuration.
    def __init__(self):
        self.DIR = os.path.dirname(__file__)
        self.LANGUAGES = ["en", "ru"]
        self.PREVIEW_LIMIT = 250
        self.PREVIEWS_PER_PAGE = 9
        self.PREVIEW_PAGE_NAME = "index"
    # Main execution sequence.
    def run(self):
        self.printDIR()
        for language in self.LANGUAGES:
            self.INPUT_DIR = "{0}/data/news-{1}".format(self.DIR, language)
            self.OUTPUT_DIR = "{0}/{1}/news".format(self.DIR, language)
            print("Language: '{0}'".format(language))
            self.ITEM_TEMPLATE_FILE_NAME = "{0}.news.item.html".format(language)
            self.readNews()
            self.printNews()
            self.readItemTemplate()
            self.sortNewsItemsDesc()
            self.convertNews()
            self.printConvertedNews()
            self.setLanguageLinks(self.newsFiles, language, "../../{0}/news/{1}")
            self.saveConvertedNews()

            self.PREVIEW_TEMPLATE_FILE_NAME = "{0}.news.preview.html".format(language)
            self.readPreviewTemplate()
            self.createNewsPreviews()
            self.INDEX_TEMPLATE_FILE_NAME = "{0}.news.index.html".format(language)
            self.readIndexTemplate()
            self.createPreviewPages()
            self.convertPreviewPages()
            self.printConvertedPreviewPages()
            self.PAGINATION_TEMPLATE_FILE_NAME = "{0}.news.pagination.html".format(language)
            self.PAGINATION_PREV_TEMPLATE_FILE_NAME = "{0}.news.pagination.prev.html".format(language)
            self.PAGINATION_NEXT_TEMPLATE_FILE_NAME = "{0}.news.pagination.next.html".format(language)
            self.readPaginationTemplates()
            self.paginatePreviewPages()
            self.setLanguageLinks(self.previewPageFiles, language, "../../{0}/news/{1}")
            self.saveConvertedPreviewPages()

        for language in self.LANGUAGES:
            self.INPUT_DIR = "{0}/data/page-{1}".format(self.DIR, language)
            self.OUTPUT_DIR = "{0}/{1}/page".format(self.DIR, language)
            print("Language: '{0}'".format(language))
            self.readPages()
            self.printPages()
            self.PAGE_TEMPLATE_FILE_NAME = "{0}.page.html".format(language)
            self.readPageTemplate()
            self.convertPages()
            self.printConvertedPages()
            self.setLanguageLinks(self.pageFiles, language, "../../{0}/page/{1}")
            self.saveConvertedPages()
    # Implementation.
    def printDIR(self):
        print("DIR: '{0}'".format(self.DIR))
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

    def readNews(self):
        self.newsItems = []
        fileNames = glob.glob(self.INPUT_DIR + "/*.md")
        for fileName in fileNames:
            with (open(fileName, "r")) as f:
                contents = f.read()
                item = NewsItem()
                item.parse(contents)
                self.newsItems.append(item)
    def printNews(self):
        print("News items:")
        for item in self.newsItems:
            print(str(item))
    def readItemTemplate(self):
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.ITEM_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.itemTemplate = f.read()
    def convertNews(self):
        self.newsFiles = []
        for newsItem in self.newsItems:
            name = "{0}.html".format(newsItem.slug)
            contents = self.convertNewsItem(newsItem, name)
            file = File(name, contents)
            self.newsFiles.append(file)
    
    def convertNewsItem(self, item, fileName):
        contents = self.itemTemplate
    
        contents = contents.replace("NEWS_ITEM_URL", fileName)
        contents = contents.replace("NEWS_ITEM_TITLE", item.title)
        contents = contents.replace("NEWS_ITEM_DATE", item.date)
    
        html = pypandoc.convert_text(item.contents, "html", format = "md")
        html = html.encode("utf-8")
        contents = contents.replace("NEWS_ITEM_CONTENTS", html)
        
        return contents
    
    def sortNewsItemsDesc(self):
        # Sort news by date descending.
        # Topic: How do I sort this list in Python, if my date is in a String?
        # Source: https://stackoverflow.com/a/2589662
        ascending = sorted(self.newsItems, key = lambda x: x.date)
        # Save reversed list.
        self.newsItems = ascending[::-1]
    
    def printConvertedNews(self):
        print("Converted news items as files:")
        for item in self.newsFiles:
            print(str(item))
    def saveConvertedNews(self):
        for file in self.newsFiles:
            fileName = "{0}/{1}".format(self.OUTPUT_DIR, file.name)
            with (open(fileName, "w")) as f:
                f.write(file.contents)

    def readPreviewTemplate(self):
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.PREVIEW_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.previewTemplate = f.read()
    def createNewsPreviews(self):
        self.newsPreviews = []
        for newsItem in self.newsItems:
            preview = self.previewNewsItem(newsItem)
            self.newsPreviews.append(preview)
    
    def previewNewsItem(self, item):
        # 1. Get first lines from markdown content that almost fit 400 characters.
        # 2. Append `...` at the end to signify `more`
        # 3. Append links section of markdown content
        # 4. Convert resulting content to HTML
        lines = item.contents.splitlines(True)
        # Compose preview section.
        preview = ""
        for ln in lines:
            preview += ln
            if (len(preview ) >= self.PREVIEW_LIMIT):
                break
        preview += "..."
        # Compose links section.
        links = ""
        for ln in lines:
            if re.match("\[.+\]:.+", ln):
                links += ln
    
        contents = preview + "\n\n\n" + links
        html = pypandoc.convert_text(contents, "html", format = "md")
        html = html.encode("utf-8")
        return html
    
    def printNewsPreviews(self):
        print("News previews:")
        for item in self.newsPreviews:
            print(str(item))
    def readIndexTemplate(self):
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.INDEX_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.indexTemplate = f.read()
    def createPreviewPages(self):
        self.previewPages = []
    
        newsItems = []
        newsPreviews = []
        newsFiles = []
        # Paginate.
        for i in range(len(self.newsItems)):
            newsItem = self.newsItems[i]
            newsItems.append(newsItem)
            newsPreview = self.newsPreviews[i]
            newsPreviews.append(newsPreview)
            newsFile = self.newsFiles[i]
            newsFiles.append(newsFile)
            # Create page.
            if (len(newsItems) == self.PREVIEWS_PER_PAGE):
                page = PreviewPage(newsItems, newsPreviews, newsFiles)
                self.previewPages.append(page)
                # Reset.
                newsItems = []
                newsPreviews = []
                newsFiles = []
        # Create the last page.
        if (len(newsItems) > 0):
            page = PreviewPage(newsItems, newsPreviews, newsFiles)
            self.previewPages.append(page)
    def convertPreviewPages(self):
        self.previewPageFiles = []
        id = 1
        for page in self.previewPages:
            contents = self.convertPreviewPage(page)
            sid = id if id != 1 else ""
            id += 1
            name = "{0}{1}.html".format(self.PREVIEW_PAGE_NAME, sid)
            file = File(name, contents)
            self.previewPageFiles.append(file)
    
    def convertPreviewPage(self, page):
        previewsContents = ""
        for i in range(len(page.items)):
            item = page.items[i]
            preview = page.previews[i]
            file = page.files[i]
            previewsContents += self.convertPreview(item, preview, file)
    
        contents = self.indexTemplate
        contents = contents.replace("NEWS_PREVIEWS", previewsContents)
        
        return contents
    
    def convertPreview(self, newsItem, preview, file):
        contents = self.previewTemplate
    
        contents = contents.replace("NEWS_ITEM_URL", file.name)
        contents = contents.replace("NEWS_ITEM_TITLE", newsItem.title)
        contents = contents.replace("NEWS_ITEM_DATE", newsItem.date)
        contents = contents.replace("NEWS_PREVIEW_CONTENTS", preview)
    
        return contents
    
    def printConvertedPreviewPages(self):
        print("Converted preview pages as files:")
        for item in self.previewPageFiles:
            print(str(item))
    def readPaginationTemplates(self):
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.PAGINATION_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.paginationTemplate = f.read()
    
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.PAGINATION_PREV_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.paginationPrevTemplate = f.read()
    
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.PAGINATION_NEXT_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.paginationNextTemplate = f.read()
    def paginatePreviewPages(self):
        count = len(self.previewPageFiles)
        for i in range(count):
            nextPageExists = (count - i > 1)
            prevPageExists = (i - 1 >= 0)
            contents = ""
            if (prevPageExists and nextPageExists):
                filePrev = self.previewPageFiles[i - 1]
                fileNext = self.previewPageFiles[i + 1]
                contents = self.paginationTemplate
                contents = contents.replace("PREV_PAGE_URL", filePrev.name)
                contents = contents.replace("NEXT_PAGE_URL", fileNext.name)
            elif (prevPageExists):
                filePrev = self.previewPageFiles[i - 1]
                contents = self.paginationPrevTemplate
                contents = contents.replace("PREV_PAGE_URL", filePrev.name)
            elif (nextPageExists):
                fileNext = self.previewPageFiles[i + 1]
                contents = self.paginationNextTemplate
                contents = contents.replace("NEXT_PAGE_URL", fileNext.name)
    
            file = self.previewPageFiles[i]
            file.contents = file.contents.replace("NEWS_PAGINATION", contents)
            if (len(contents)):
                file.contents = file.contents.replace("PAGE_ID", str(i + 1))
                file.contents = file.contents.replace("PAGES_COUNT", str(count))
    def saveConvertedPreviewPages(self):
        for file in self.previewPageFiles:
            fileName = "{0}/{1}".format(self.OUTPUT_DIR, file.name)
            with (open(fileName, "w")) as f:
                f.write(file.contents)

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
    def readPageTemplate(self):
        fileName = "{0}/{1}".format(self.INPUT_DIR, self.PAGE_TEMPLATE_FILE_NAME)
        with (open(fileName, "r")) as f:
            self.pageTemplate = f.read()
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
    def saveConvertedPages(self):
        for file in self.pageFiles:
            fileName = "{0}/{1}".format(self.OUTPUT_DIR, file.name)
            with (open(fileName, "w")) as f:
                f.write(file.contents)

tool = SiteTool()
tool.run()
