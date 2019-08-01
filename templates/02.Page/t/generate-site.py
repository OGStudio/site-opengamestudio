#!/usr/bin/python

AMLEO SiteTool.DIR/Import
AMLEO NewsTool.ConvertNews/Import
AMLEO NewsTool.PreviewNews/Import
AMLEO NewsTool.ReadNews/Import
AMLEO SiteTool.ReadPages/Import
AMLEO SiteTool.ConvertPages/Import

AMLEO File/Impl
AMLEO NewsItem/Impl
AMLEO PreviewPage/Impl
AMLEO PageItem/Impl

AMLEO SiteTool/Cfg
        AMLEO SiteTool.DIR/Cfg
        AMLEO SiteTool.Languages/Cfg
        AMLEO NewsTool.PreviewNews/Cfg
        AMLEO NewsTool.CreatePreviewPages/Cfg
        AMLEO NewsTool.ConvertPreviewPages/Cfg
AMLEO SiteTool/Run
        AMLEO SiteTool.DIR/Debug
        AMLEO SiteTool.Languages/Loop
            AMLEO SiteTool.Languages/Debug
            AMLEO SiteTool.ReadItemTemplate/Cfg
            AMLEO NewsTool.ReadNews/Run
            AMLEO NewsTool.ReadNews/Debug
            AMLEO NewsTool.ReadItemTemplate/Run
            AMLEO NewsTool.ConvertNews/Run
            AMLEO NewsTool.ConvertNews/Debug
            AMLEO SiteTool.Languages/RunItem
            AMLEO NewsTool.SaveConvertedNews/Run

            AMLEO SiteTool.ReadPreviewTemplate/Cfg
            AMLEO NewsTool.ReadPreviewTemplate/Run
            AMLEO NewsTool.PreviewNews/Run
            AMLEO SiteTool.ReadIndexTemplate/Cfg
            AMLEO NewsTool.ReadIndexTemplate/Run
            AMLEO NewsTool.CreatePreviewPages/Run
            AMLEO NewsTool.ConvertPreviewPages/Run
            AMLEO NewsTool.ConvertPreviewPages/Debug
            AMLEO SiteTool.ReadPaginationTemplates/Cfg
            AMLEO NewsTool.ReadPaginationTemplates/Run
            AMLEO NewsTool.PaginatePreviewPages/Run
            AMLEO SiteTool.Languages/RunPreview
            AMLEO NewsTool.SaveConvertedPreviewPages/Run

        AMLEO SiteTool.PageLanguages/Loop
            AMLEO SiteTool.Languages/Debug
            AMLEO SiteTool.ReadPages/Run
            AMLEO SiteTool.ReadPages/Debug
            AMLEO SiteTool.ReadPageTemplate/Cfg
            AMLEO SiteTool.ReadPageTemplate/Run
            AMLEO SiteTool.ConvertPages/Run
            AMLEO SiteTool.ConvertPages/Debug
            AMLEO SiteTool.PageLanguages/Run
            AMLEO SiteTool.SaveConvertedPages/Run
AMLEO SiteTool/Impl
    AMLEO SiteTool.DIR/Impl
    AMLEO SiteTool.Languages/Impl

    AMLEO NewsTool.ReadNews/Impl
    AMLEO NewsTool.ReadItemTemplate/Impl
    AMLEO NewsTool.ConvertNews/Impl
    AMLEO NewsTool.SaveConvertedNews/Impl

    AMLEO NewsTool.ReadPreviewTemplate/Impl
    AMLEO NewsTool.PreviewNews/Impl
    AMLEO NewsTool.ReadIndexTemplate/Impl
    AMLEO NewsTool.CreatePreviewPages/Impl
    AMLEO NewsTool.ConvertPreviewPages/Impl
    AMLEO NewsTool.ReadPaginationTemplates/Impl
    AMLEO NewsTool.PaginatePreviewPages/Impl
    AMLEO NewsTool.SaveConvertedPreviewPages/Impl

    AMLEO SiteTool.ReadPages/Impl
    AMLEO SiteTool.ReadPageTemplate/Impl
    AMLEO SiteTool.ConvertPages/Impl
    AMLEO SiteTool.SaveConvertedPages/Impl

AMLEO main/Impl
