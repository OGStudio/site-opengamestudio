Title: The turn to cross-platform solutions
Date: 2025-09-09
Category: News
Slug: kotlin-cross
Lang: en

![][splash]

# The clash with git push limitations

In August I've added `git commit` and `git push` commands to PSKOV.
However, it became clear that Vercel (we use the service to host CORS
proxy) does not allow `git push` requests for a moderately sized
repository (50M) of this very site.

Thus, to support `git push` for moderately sized repositories, I would
need to run my own server with CORS proxy. I have neither money, nor
time to do that at the moment, unfortunately.

That's why, having stumpled upon the wall of reality once again, I have to
retreat: let's first create PSKOV as a Node.js application to generate sites
locally. A user can manager Git himself.

# September

In September I plan to create the first version of PSKOV for Node.js
using Kotlin Multiplatform.

[splash]: ../../images/2025-09_push-error.jpg
