Title: How I create browser applications inside browsers
Date: 2021-01-28 00:00
Category: News
Slug: gitjs-intro
Lang: en

![GitJS][снимок]

In this article Michael shares his experience of creating durable applications.

In 2013 Canonical [tried to crowdfund Ubuntu Edge smartphone][сбор-средств].
Its main feature could be the ability to use the smartphone as a full-fledged
PС. Unfortunatly, the crowdfunding campaign did not accumulate enough money,
so a dream of having a universal device remained to be the dream.

I've been searching for universality, too, on the software side,
not the hardware one. Today I can confidently say I found the necessary
combination: Git and JavaScript.

As you know, I have already described the benefits of browser applications
([nCKOB][псков] static site generator) and the benefits of using Git
instead of yet another back-end with API ([GitBudget][гит-бюджет] to track
personal spendings). Once GitBudget was out, I spent the remaining 2020
to build a system allowing one to create browser applications right inside
browsers. GitJS is the name of that system.

<cut/>

# GitJS

The system uses Git for:

* long-term data storage **outside** of device;
* talking to the outside world;
* delivering the application to a device over HTTP.

Thus, Git is not used for version control, Git is merely a
widespread technology to keep data with read (HTTP) and write permissions. This
might be somewhat counterintuitive. However, this allows everyone to decide
where and how to keep data: paid/free, locally/remotely.

You might argue that FTP/rsync could be used instead of Git if we only
need to keep data. However, there are no widespread services like
SourceForge/GitHub/BitBucket/GitLab for FTP/rsync. Also, there are no
implementations of FTP/rsync that work inside browsers, and Git has
[Isomorphic-Git][isomorphic-git].

JS (alongside HTML/CSS) is used for:

* user interface;
* logic;
* long-term data storage **on** device.

GitJS consists of the following three mandatory parts (in the order of execution):

1. [HTML page][страница-html]
    * introduces GitJS rules
    * has a tiny size to work for slow connections
    * is requested/delivered each time the page is completely refreshed
    * may be hosted locally to work without the Internet
1. [GitJS rules][правила-гитжс]
    * are essentially a chunk of JS code
    * introduce the concept of modules and their loading, saving, execution
    * introduce the concept of sequences: a way to structure source code in a reactive-event-based manner
    * are requested/delivered by HTML page only if they are absent or need an update
    * are saved by HTML page into LocalStorage to start faster next time
1. [Startup module][пусковой-модуль]
    * is located in the address string after `?` symbol
    * is executed after the loading of GitJS rules
    * does whatever is necessary, e.g., introduces dependent modules to be loaded before the main application should start
    * the linked example depicts JSZip library test

Startup module may introduce absolutely any additional rules to GitJS ones or
even replace them, so your fantasy here is only limited by what browsers
permit: e.g., you can't erase all hard drive files of a user.

I'd like to stress that having an HTML page and Git web service locally
lets you use GitJS without the Internet.

# GitJS application №1: editor of GitJS modules

Currently, the editor has very basic functionality:

**1.1. Editing of module's text files**

![][правка-текстовых-файлов]

**1.2. Publishing changes to Git**

![][публикация-изменений]

**Note**: browsers keep passwords.

**1.3. Editing the structure of a module**

![][правка-структуры]

**1.4. Opening previously loaded modules from LocalStorage/IndexedDB**

![][открытие-модуля]

**1.5. Saving changes locally into LocalStorage/IndexedDB**

Here's the editor's last version: [http://gitjs.org/📦](http://gitjs.org/📦).
The first run takes some time, be patient.

# GitJS application №2: Mahjong solitaire

Currently, the game has the following functionality:

**2.1. Selection and removal of tiles off the field according to Mahjong solitaire rules**

![][механика]

**2.2. Tile theme selection**

![][темы]

**2.3. Field layout selection**

![][раскладки]

**2.4. Victory/loss detection**

Here's the game's last version: [http://gitjs.org/🀄/1.0.14](http://gitjs.org/🀄/1.0.14).

In the end, this game will match the original [Mahjong][маджонг1] (released several
years ago) in terms of features.

# Limitations

GitJS limitations stem from browser ones.

**1. CORS**

To be able to publish changes to Git, we have to meet CORS restrictions.
Currently, major services [do not allow to publish Git changes easily][cors],
so one would have to use either a proxy, or a personal Git service.

**2. Full-screen surfing on mobile**

Nowadays, browsers collapse navigation and other controls when you scroll a
page that doesn't fit into available space. This leaves the space at the top
and the bottom of the screen free of controls but still unusable for touches
because these touches bring those controls back. Such behaviour is very
inconvenient for games.

Mahjong solitaire works around that problem by supporting portrait mode: you
can shift the field left/right. However, such a solution has its own drawbacks:
one cannot see the field at a single glance, which makes the game harder to play.

# Plans

[nCKOB][псков] mentioned earlier will be rewritten as GitJS application. This
would allow anyone to create statically generated sites without leaving a
browser. We'll see how this goes.

PS: The first image is "Bayan" picture created by Viktor Vasnetsov in 1910.

[isomorphic-git]: https://isomorphic-git.org
[сбор-средств]: https://techcrunch.com/2013/08/22/edge-crowdfunding-fail
[псков]: http://opengamestudio.org/en/news/on-the-way-to-durable-applications.html
[гит-бюджет]: http://opengamestudio.org/en/news/git-budget.html
[страница-html]: https://gitlab.com/gitjs/gitjs.gitlab.io/-/blob/master/index.html
[правила-гитжс]: https://bitbucket.org/gitjs/0000/src/master/0000.js
[пусковой-модуль]: https://git.opengamestudio.org/kornerr/nPOBEPuTb-JSZip
[маджонг1]: http://opengamestudio.org/en/game/ogs-mahjong-1.html
[правка-текстовых-файлов]: ../../images/2021_gitjs-intro_правка-текстовых-файлов.png
[публикация-изменений]: ../../images/2021_gitjs-intro_публикация-изменений.png
[правка-структуры]: ../../images/2021_gitjs-intro_правка-структуры.png
[открытие-модуля]: ../../images/2021_gitjs-intro_открытие-модуля.png
[механика]: ../../images/2021_gitjs-intro_механика.png
[темы]: ../../images/2021_gitjs-intro_темы.png
[раскладки]: ../../images/2021_gitjs-intro_раскладки.png
[снимок]: ../../images/2021_gitjs-intro_снимок.jpg
[cors]: https://github.com/isomorphic-git/isomorphic-git#cors-support

