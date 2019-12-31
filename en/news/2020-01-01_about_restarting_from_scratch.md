Title: The pros and cons of restarting from scratch
Date: 2020-01-01 00:00
Category: News
Slug: the-pros-and-cons-of-restarting-from-scratch
Lang: en

![Happy 2020][screenshot]

Anyone, who watches our progress long enough, can say that we restarted the development from scratch plenty of times.

Even before releasing ["OGS Mahjong"][ogs-mahjong-1], we changed the underlying technology more than once. After that, we did it again several times, throwing away already completed features.
It seems that right now we have less completed features than before the release of ["OGS Mahjong"][ogs-mahjong-1]. It's true, but not entirely.

When ["OGS Mahjong"][ogs-mahjong-1] was released, we had a descent looking (for that moment) open-source game, that worked under Windows and Linux. With some luck and effort it still works today, but not out of the box.
Some parts of the underlying technology did not age very well. And fixing these problems today will require us to invest a lot of time into it.
Even setting the building environment for the game is time-consuming, because the game had some very particular dependencies.

So, as Michael stated before, we are trying to find the set of technologies, that will resolve two problems at the same time:

* greatly decrease the amount of effort needed to setup a building environment;
* age better.

During this year, Michel, who has some experience with teaching kids to code, added one more goal - making the simple game should be easy enough for the kid to understand.

So, we divided everything we wanted in two parts.

The first part is making an easy to use instrument that a child can use to create a simple game, and a professional or hobbyist can use to test new ideas quickly. This instrument should require zero time to setup the working environment, but should still be highly customizable. After many hours of arguing, we decided that this instrument should be web-based (self-hosted, preferably working locally). This instrument is [MUROM][murom] (named after one famous Russian city), and right now it highly customizable and works in the browser with zero setup time. [MUROM][murom] can be used to create simple games, but it's far from ready. And the third goal is also ahead.

We will start to work on the second part after completing the first part. It will include the native part of the engine. We'll try to let the web-based engine and the native engine use the same code for game logic, but we haven't decided on how exactly will we achieve this feature. Probably, we will have to use meta-language that can be translated into both JavaScript and C++. Also, creating separate plugins for something that is impossible in the web version (for example, using specific hardware or accessing a local file system) will still be required.

Will we ever start to work on the second part? We hope so. We're planning to use [MUROM][murom] to remake ["OGS Mahjong"][ogs-mahjong-1], so some things will be done just in order to make it possible.
And even if we will complete only the first part and [MUROM][murom] will just be a quick&dirty prototyping tool, it will be a tool we use, and we'll try to make it useful.

When you throw away all the code, one thing remains. That's experience. Every restart will make you slightly better at understanding what you are actually doing. But it's important to complete something from time to time. Otherwise, you can find yourself stuck in the endless loop of new beginnings.

And our own main goal for 2020 will be to break out of this loop and complete something. 

Happy new year, everyone! Stay tuned!

[screenshot]: ../../images/2020-01-01-ny.jpg
[ogs-mahjong-1]: ../game/ogs-mahjong-1.html
[murom]: http://opengamestudio.org/murom
