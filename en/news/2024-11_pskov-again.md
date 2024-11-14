Title: Back to the development of "PSKOV"
Date: 2024-11-14 00:00
Category: News
Slug: pskov-again
Lang: en

![lha][lha]

# "PSKOV" today

Now, we have an old "PSKOV" version and we need an improved one.

First, we should recall what "PSKOV" consists of:

1. The [generator][pskov-en] itself in the form of HTML page with JavaScript
1. Helper [Python script][lfsa-en] to save generated files to disk

Helper script is used to bypass web page restriction to access
local file system.

The script itself is a tiny web server with the following commands:

| № | Command | Details |
|---|---|---|
| 1 | `GET /path` | Get current working directory path |
| 2 | `POST /list` | Get a list of files in the requested directory  |
| 3 | `POST /read` | Get file's contents |
| 4 | `POST /write` | Write file's contents |

# "PSKOV" tomorrow

Thus, the simplest way to get back to "PSKOV" development is to rewrite the
helper script. I decided to replace Python with Kotlin because:

1. Kotlin can be compiled for desktop, mobile, and web
1. Kotlin is strictly typed

These two factors simplify future work with portable code.

As of now, I have `GET /path` implemented for JVM, macOS, and Windows (image
in the beginning).

# November

I plan to implement the following commands in November:
* `POST /list`
* `POST /read`

[lha]: ../../images/2024_lha-path.gif
[pskov-en]: https://opengamestudio.org/pskov/en/pskov_1.0.0.html
[lfsa-en]: https://opengamestudio.org/lfsa/en/index.html
