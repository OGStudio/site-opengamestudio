Title: Git Budget is now finally a Qt application, too
Date: 2026-05-01
Category: News
Slug: git-budget-qt
Lang: en

<video controls width="700">
    <source src="../../vid/2026-04_git-budget-qt.mp4" type="video/mp4"/>
</video>

# April

In April I have finally updated Klin tool to generate C++ bindings. This allowed
me to have Git Budget as a Qt application for macOS using Kotlin Dialect.

The most interesting part is how many lines of code were saved when supporting
several platforms:

| Platform |  Saved lines of code | Saved % | Total lines of code |
| --- | --- | --- | --- |
| Android | 0 (Original code) | 0% | 652 |
| iOS | 333 | 58% | 569 |
| macOS | 340 | 44% | 761 |

Turns out the fact that you don't need to repeat the logic means additional
platforms require 44-58% less lines of code, i.e., once you have an Android
application any additional platform comes at only half the price.

# May

In May I plan to add the history of spendings to Git Budget.
