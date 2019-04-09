Title: November 2016 recap
Date: 2016-12-15 00:00
Category: News
Slug: 2016-november-recap
Lang: en

![Construction of a building][screenshot]


This article describes the start of MJIN library separation into modules.

Once we built OpenSceneGraph for Android, it became obvious that some MJIN functionality is not suitable for Android. For example, UIQt provides a basis for OGS Editor UI. Since OGS Editor is a desktop application, we don't need UIQt for Android.

We decided to have a look at two approaches to separate MJIN into modules: build-time separation and run-time one. 
**Build-time** separation means MJIN becomes highly configurable and each platform gets specifically tailored MJIN build.
**Run-time** separation means MJIN is divided into smaller libraries that are connected at run-time, which makes it easy to change functionality without rebuilding.

**Run-time separation research.**

Since run-time separation has more benefits, we started researching it first. The easiest way to achieve it was to use C API, because C ABI rules are much simpler than C++ one's.

We created a sample project consisting of the application, library, and plugin:

* **The application** has been linked to the library and used it to load the plugin.
* **The library** provided functions to register plugins and call their functions.
* **The plugin** provided functions for the library and called library functions.

The research was successful: the sample project worked correctly under Linux and Windows. However, since MJIN is currently a single large entity, we postponed C API application until we finish build-time separation.

**Build-time separation start.**

We extracted the following modules from MJIN:

* Android: provides Java Native Interface (JNI) to MJIN
* Sound: provides access to OpenAL
* UIQt: provides access to Qt UI




Sound and UIQt modules are currently statically linked into MJIN library, while Android module is already a separate library due to JNI requirements.

In the coming year, we're going to significantly restructure MJIN so that it suits as many platforms as possible.

That's it for describing the start of MJIN library separation into modules.

[screenshot]: ../../images/2016-12-15_2016-november-recap.png
