Title: Rethinking
Date: 2024-08-12 00:00
Category: News
Slug: rethinking
Lang: en

![Game][game]

When July started my initial plan was to make the instrument support Python to
JavaScript code translation. However, this did not happen because tasks with
higher priority emerged.

Which task is more important than develpment of the instrument?
Development of a game, of course! Now, let's go back to the beginning of
July 2024...

# Gamejam

["Start the game"][jam] 3-day gamejam finished in the beginning of July 2024.
I participated in the jam to validate the instrument under development and
to get along with other gamedev hobbysts. Getting to know one of the hobbysts -
Eugene - lead to the creation of ["Tail and shadow"][tail] project,
a 2D adventure.

# July

As a result, I spent July to create a prototype with the single core mechanics -
mouse click.

Current technical details of the prototype look like this:

* INI-like format is used to configure the game prototype
* Python is used for game logic with elements of cross-language dialect
* Python Arcade is used for rendering
* the prototype runs on macOS, Linux, Windows
* the prototype is controlled only by mouse clicks
* every asset is first drawn by hand and then brought into digital world by GIMP + ImageMagick
* one can specify static elements to display floor, walls and similar environment
* one can specify active items like doors to have interaction with by mouse clicks
* one can specify comments when clicking on an active item to display hints

# August

I plan to implement scene switching in August.

[game]: ../../images/2024_rethinking.jpg
[jam]: https://dtf.ru/games/2783053-nachni-igru-ocenka-videorolikov
[tail]: https://t.me/Tail_and_shadow
