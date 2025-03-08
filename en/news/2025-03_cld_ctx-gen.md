Title: CLD: Context generation
Date: 2025-03-11 00:00
Category: News
Slug: cld_ctx-gen
Lang: en

![splash][splash]

# Context generation

In February I've updated the **C**ross-**l**anguage **d**ialect (CLD) translator to
generate Context out of YML. The generated Contexts have already been
applied to all three currently active projects:

* CLD (the CLD translator generated its own Context)
* LHA
* PSKOV

I never really took time to explain what Context is, so here's
a very short explanation: Context is very close to the concept
of [a store in Redux][store]. I'm afraid this is not yet the time
to explain Context in details because I have not yet achieved anything
to showcase why one would need to use Context. Once that time comes
I do it.



Now back to the Context generation. Let's take the Context of LHA ([entities.yml][entities]):

```
# Application state context
Context:
    type: context
    fields:
        # Command line arguments
        arguments: [String]
        consoleOutput: String
        defaultDir: String
        didLaunch: Bool
        dir: String
        httpDefaultPort: Int
        httpLaunch: Bool
        httpPort: Int
        httpReply: String
        httpRequest: NetRequest
```

The translator converts it to the following Kotin code ([entities.kt][entities-result]):

```
// Application state context
data class Context(
    // Command line arguments
    var arguments: Array<String> = arrayOf(),
    var consoleOutput: String = "",
    var defaultDir: String = "",
    var didLaunch: Boolean = false,
    var dir: String = "",
    var httpDefaultPort: Int = 0,
    var httpLaunch: Boolean = false,
    var httpPort: Int = 0,
    var httpReply: String = "",
    var httpRequest: NetRequest = NetRequest(),
    override var recentField: String = "",
): CLDContext {
    override fun <T> field(name: String): T {
        if (name == "arguments") {
            return arguments as T
        } else if (name == "consoleOutput") {
            return consoleOutput as T
        } else if (name == "defaultDir") {
            return defaultDir as T
        } else if (name == "didLaunch") {
            return didLaunch as T
        } else if (name == "dir") {
            return dir as T
        } else if (name == "httpDefaultPort") {
            return httpDefaultPort as T
        } else if (name == "httpLaunch") {
            return httpLaunch as T
        } else if (name == "httpPort") {
            return httpPort as T
        } else if (name == "httpReply") {
            return httpReply as T
        } else if (name == "httpRequest") {
            return httpRequest as T
        }
        return "unknown-field-name" as T
    }

    override fun selfCopy(): CLDContext {
        return this.copy()
    }

    override fun setField(
        name: String,
        value: Any?
    ) {
        if (name == "arguments") {
            arguments = value as Array<String>
        } else if (name == "consoleOutput") {
            consoleOutput = value as String
        } else if (name == "defaultDir") {
            defaultDir = value as String
        } else if (name == "didLaunch") {
            didLaunch = value as Boolean
        } else if (name == "dir") {
            dir = value as String
        } else if (name == "httpDefaultPort") {
            httpDefaultPort = value as Int
        } else if (name == "httpLaunch") {
            httpLaunch = value as Boolean
        } else if (name == "httpPort") {
            httpPort = value as Int
        } else if (name == "httpReply") {
            httpReply = value as String
        } else if (name == "httpRequest") {
            httpRequest = value as NetRequest
        }
    }
}
```

# Kotlin problems

Here comes the second part why Context concept has not yet been covered.
That's because the strong dependency of Kotlin requires the tools to
require tool users to have Kotlin compiler because I don't have one.
And I don't want to have one, it's just too many dependencies.
And what I want is just a JavaScript tool that runs in a Web Browser
and, when necessary, can produce Kotlin code which in turn would
require those lots of Kotlin dependencies.


# March

That's why in March I'm going to rething the usage of Kotlin as the
primary language of all the curently active projects.
I'll try to create a web browser tool that is useful to me
and see if Kotlin, Context, CLD are good for it. May be I'll
come with something better and easier? Let's see!

[entities]: https://github.com/OGStudio/local-host-access/blob/main/cld/entities.yml
[entities-result]: https://github.com/OGStudio/local-host-access/blob/main/src/entities.kt#L3

[splash]: ../../images/??.png
[store]: https://redux.js.org/introduction/getting-started#basic-example
