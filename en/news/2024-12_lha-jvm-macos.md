Title: The first Local Host Access working version
Date: 2024-12-10 00:00
Category: News
Slug: lha-jvm-macos
Lang: en

![web-test][web-test]

# Local Host Access

I implemented Local Fle System Access' functionality in
Local Host Access for JVM and macOS platforms. For example, this
very article has been generated with the help of Local Host Access.
Thus, Kotlin turned out to be a good choice.

The biggest downside of Kotlin is that it's primarily used for JVM.
That means that 99% of Kotlin code and articles on the Internet are
dedicated to JVM. Thus, Kotlin Native (Linux, macOS, Windows) examples
are absurdly hard to find and as absurdly hard to translate from plain C.

Take, for example, one specific function: `POST /list`. It is used
to list files and directories of the requested path. I managed to find
a [dedicated example][opendir] on how to call C's `opendir()`/`readdir()` and
traverse the directory.

However, since there are symlinks an additional call to C's `stat()` is necessary
to see what's behind the symlink. I couldn't find an example on using `stat()`
on the Internet. My attempts to write anything meaningul failed, too.
[My question][question] of how to do it is still waiting for an answer since
November 18. I'm not sure it will ever get answered. 

# December

I plan to support Linux and Windows platforms for Local Host Access.

[web-test]: ../../images/2024_web-test.jpg
[opendir]: https://gist.github.com/kesslern/743d5a3c07b8cfbd52e78ec5268a1dc8
[question]: https://discuss.kotlinlang.org/t/how-to-call-stat-c-function-to-get-file-type/29541
