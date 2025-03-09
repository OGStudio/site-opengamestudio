Title: CLD: Context generation
Date: 2025-03-11 00:00
Category: News
Slug: cld_ctx-gen
Lang: en

![splash][splash]

# Context generation

In February I've updated the **C**ross-**l**anguage **d**ialect (CLD) translator to
generate Context out of YML. The generated Contexts have already been
used for the following projects:

* CLD (the CLD translator generated its own Context)
* LHA
* PSKOV

I never really took time to explain what Context is, so here's
a very short explanation: Context is very close to
[a store in Redux][store]. I'm afraid this is not yet the time
to explain Context in details because I don't yet have a good
argument why you need Context. Once that time comes I do it.

Now let's get back to the Context generation. Here's how LHA's YML for Context looks like: ([entities.yml][entities]):

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

CLD translator converts it to the following code in Kotlin ([entities.kt][entities-result]):

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

# March

Kotlin is currently the anchor programming language of CLD. Thus, to use Kotlin,
one would have to install related Java tools (Gradle, Android Studio or JVM itself).
Such a requirement makes it impossible to have a web browser only development
tool. And being able to code in a web browser is something that I consider
obligatory.

That's why in March I'm plan to create the draft of a tool that runs in a web browser.

[entities]: https://github.com/OGStudio/local-host-access/blob/main/cld/entities.yml
[entities-result]: https://github.com/OGStudio/local-host-access/blob/main/src/entities.kt#L3
[splash]: ../../images/??.png
[store]: https://redux.js.org/introduction/getting-started#basic-example
