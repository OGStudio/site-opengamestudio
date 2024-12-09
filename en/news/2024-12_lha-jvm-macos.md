Title: The first Local Host Access working version
Date: 2024-12-09 00:00
Category: News
Slug: lha-jvm-macos
Lang: en

![web-test][web-test]

# Local Host Access

Tiny web server called Local Host Access (**LHA**) is ready to replace
Local File System Access (**LFSA**) on JVM and macOS: I've generated this
very article with LHA on macOS. Thus, Kotlin prooved to be a good choice for
cross-platform development with a minor limitation.

The minor limitation is the fact that 99% of Kotlin is used on JVM. The
remaining 1% is so-called Kotlin Native for iOS, Linux, macOS, and Windows.
Thus, when one needs something as simple as to find out if a symlink
points to a file or directory, that's a dead end, there's no article for
that on the Internet. For C, there are numerous articles telling to call `stat()`
function. For Kotlin Native, it's unclear how to properly make such a simple call.

I've actually asked [this specific question][question] in November,
and still wait for an answer.
In the meantime, I had to resort to calling `stat` in the shell (aka `system()`).

# December

I plan to implement the first Kotlin -> Python translator to let LHA
cover as many platforms as the original LFSA in Python.

[web-test]: ../../images/2024_web-test.jpg
[question]: https://discuss.kotlinlang.org/t/how-to-call-stat-c-function-to-get-file-type/29541
