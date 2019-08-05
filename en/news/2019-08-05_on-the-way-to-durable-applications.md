Title: On the way to durable applications
Date: 2019-08-05 00:00
Category: News
Slug: on-the-way-to-durable-applications
Lang: en

![Pskov's veche][screenshot]

This article describes our first durable application for desktop PCs: PSKOV static site generator.

**Durability**

A durable application is an application that functions without a single change on operating systems released in years 2010-2030. In other words, a durable application has backward compatibility of 10 years and has the stability to run for 10 years. Actually, [PSKOV][pskov] runs even under Windows 2000, so PSKOV has backward compatibility of 19 years.

From technical side, PSKOV is a single HTML file with layout (HTML), styles (CSS), and code (JavaScript) packed inside. PSKOV runs strictly inside a web browser without connecting to any server.

Such an implementation gives PSKOV the following features:

* it can be copied without restrictions
* it can be hosted anywhere
* it can run locally
* it can operate without Internet

We can't guarantee stability for 10 years because we can't control the future. However, the history of HTML, CSS, and JavaScript evolution tells us these technologies are developed with maximum backward compatibility. First, new JavaScript features leave older ones still working. Second, web browser developers are interested in making their web browsers work with as many web sites as possible. For example, [&lt;center&gt; tag][center-tag], being declared deprecated in 2014, still works as expected 5 years since, in 2019.

At the same time, each web browser application has a serious restriction called sandbox, a deceptive name for a cage. The cage prevents access to both local file system of users and almost any Internet resource without its owner's explicit permission (CORS). As a result, the application can only communicate with users either through the distinct server, or by offering files to download manually. Downloading files one by one or as an archive is inconvenient, that's why nowadays server oriented approach reigns the world. We'll touch problems of that approach in a moment.

To free PSKOV from the cage, [LFSA][lfsa] was created, a tiny Python script that needs to be run manually while PSKOV is running. LFSA allows PSKOV to access the user’s local file system. Python was selected because Linux and macOS have Python installed by default, and users can easily install Python on Windows (even Windows 2000).

**Track record**

PSKOV has been successfully used to create the following small sites:

* [open game studio project site][ogs]
* [PSKOV itself][pskov]
* [LFSA][lfsa]
* [example of a simple blog][pskov-sample]

Now let's see why PSKOV was created as a durable application for web browsers.

**Reason №1: collect and keep knowledge in an accessible form**

We have been creating convenient game development tools for several years now. So far the collected knowledge was represented by [native applications][ogs-mahjong-1] for desktop PCs, [education articles][osgcpg] for related technologies, and [showcase videos][showcase]. Such forms of the collected knowledge are basically dead:

* few would download an unknown application
* few would watch some videos
* even fewer would read some articles

In many ways, this death is due to inaccessibility: one has to make an unknown amount of effort to achieve an unknown result. Hardly anyone would have interest in this. A web browser application, potentially accessible anywhere, is a totally different deal: you only need to make a known effort, click a link, to achieve an unknown result. The history of conducting [twitter revolutions][twitter-revolutions] proves that almost anyone can open a link and "like" the change of a "bloody regime".

**Reason №2: rule by people**

Nowadays any Internet activity is performed by the means of services that almost always belong to some company: [messages][msg], [maps][map], [search][search], [music][music], [source code][src], etc. Such power usurpation leads to [shutdowns][shutdown-01] of [services][shutdown-02] that their owning companies deem unprofitable. They usually do it without any consent with those users who brought life to these services in the first place.

Other times companies simply block competing browsers from accessing their service, as it was recently the [case with the web version of Skype][skype-block]. Luckily there are people who don’t agree with such politics. Thanks to them, [unlocking tools][skype-free] appear.

As for me, I deem such a way of handling things as inappropriate. However, savage business is not the only one to blame here; average users, every one of us is guilty, too. You may argue that users have no choice, that someone else (government, aliens, underline what you like) made this world unfair. Some people even blame government/aliens directly and believe that without them, life would be amazing. However, human history [tells us a different story][story]: "**the state** is not some enemy horde that occupied the society, but that which **grows out of society and mirrors it**".

Being part of the people, we decided to start with ourselves and use our power for the best: create applications that we need in such a way to make them usable and accessible to everyone everywhere. PSKOV is the first attempt, which already exceeded our expectations. Sure, PSKOV has limitations like LFSA and unencrypted HTTP; there's a lot to do to increase the accessibility of PSKOV, however, we're ready to dare anyone: current PSKOV version will keep functioning for 10 years to come without any maintenance.

That's it for describing our first durable application for desktop PCs: PSKOV static site generator.

[screenshot]: ../../images/2019-08-05_on-the-way-to-durable-applications.jpg

[pskov]: http://opengamestudio.org/pskov
[center-tag]: https://www.w3schools.com/tags/tag_center.asp
[lfsa]: http://opengamestudio.org/lfsa
[ogs]: http://opengamestudio.org
[pskov-sample]: http://opengamestudio.org/pskov/sample/03.Blog/en/blog/index.html
[ogs-mahjong-1]: ../game/ogs-mahjong-1.html
[osgcpg]: https://github.com/OGStudio/openscenegraph-cross-platform-guide
[showcase]: https://youtu.be/_t8TGhSgJG4
[twitter-revolutions]: https://en.wikipedia.org/wiki/Twitter_Revolution
[msg]: http://twitter.com
[map]: http://2gis.ru
[search]: http://google.com
[music]: http://music.yandex.ru
[src]: http://github.com
[shutdown-01]: https://techcrunch.com/2015/03/13/google-kills-off-google-code/
[shutdown-02]: https://www.reddit.com/r/sysadmin/comments/62orq9/codeplex_shutting_down_and_fosshub_is_sad/
[skype-block]: https://www.reddit.com/r/firefox/comments/aw1umv/skype_web_is_now_blocked_in_firefox/
[skype-free]: https://addons.mozilla.org/ru/firefox/addon/firefox-web-skype/
[story]: https://translate.google.com/translate?sl=ru&tl=en&u=https%3A%2F%2Fria.ru%2F20190723%2F1556775012.html
