Title: Project's list of files
Date: 2025-10-01
Category: News
Slug: display-files
Lang: en

<video controls width="700">
    <source src="../../images/2025-10_display-files.mp4" type="video/mp4"/>
</video>

# Displaying project's files

In September I created the new draft version of PSKOV 2, which now consists of two parts: web client + web server:

* the web server provides access to files on disk using [Local Host Access][lha] format to the web client
* the web client provides UI for a human to manage site's contents

Logic is in Kotlin. Then Kotlin code is translated to JavaScript for
both Node.js and web browser. Using Kotlin as an [anchor language][year24]
finally started to bare fruits.

# October

In October I plan to add Markdown file viewer functionality.

[lha]: lha-jvm-macos.html
[year24]: year24.html
