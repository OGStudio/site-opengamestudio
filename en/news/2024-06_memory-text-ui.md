Title: "Memory" text UI
Date: 2024-06-14 00:00
Category: News
Slug: memory-text-ui
Lang: en

# "Memory" text UI

In May I implemented text UI for "Memory" game in Python. And converted it to C++
by the instrument under development.

Game logic cycle implementation lead to the creation of a controller that manages
context. Creating the controller in Python was straightforward. C++ version took
some time, because the controller needs [std::any][any], which is part of C++17.
The instrument under development is limited to C++11 in order to support OpenWrt.

Here's how much code I wrote (in lines):

* (Python) Portable logic code: 360
* (Python) Portable testing code: 565
* (Python) Unportable code of controller, input/output, etc.: 350
* (C++) Ported logic code: 360
* (C++) Ported testing code: 586
* (C++) Unportable code of controller, input/output, etc.: 565

Here's the same data in per cent:

| Language | Total lines of code | Portable/ported | Unportable |
| --- | --- | --- | --- |
| Python | 1275 (**100%**) | 925 (**72%**) | 350 (**28%**) |
| C++ | 1511 (**100%**) | 946 (**62%**) | 565 (**38%**) |

Thus, the development of C++ version of "Memory" game was 62% lines
of code cheaper than if it would be without the instrument. Nice figures.

Here's how "Memory" text UI looks like now:

<iframe width="560" height="315" src="https://www.youtube.com/embed/tChSjw5W8KQ?si=WO5MYLCBhgstVshl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# June plans

I'll make a graphical UI for Python version of "Memory" game.

[any]: https://en.cppreference.com/w/cpp/utility/any
