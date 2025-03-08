Title: CLD: Генерация контекста
Date: 2025-03-11 00:00
Category: News
Slug: cld_ctx-gen
Lang: ru

![splash][splash]

# Генерация контекста

В феврале доработал конвертер Межъязыкового диалекта
(**C**ross-**l**anguage **d**ialect) (CLD) для генерации
Контекста на основе описания в YML и уже применил его для проектов
Local Host Access, самого конвертера, ПСКОВа.

Если очень кратко, то Контекст представляет из себя полное состояние
приложения, по сути аналог [store в Redux][store].

Для примера возьмём описание Контекста из Local Host Access
([entities.yml][entities]):

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

Конвертер преобразует его в следующий код на Kotlin ([entities.kt][entities-result]):

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

# Проблемы

Тем не менее, на текущий момент ощутил огромный минус Котлина для
проекта CLD - необходимость оригинального компилятора Котлин, т.к.
без него я не могу валидировать код. Могу транслировать, но не валидировать.
Выходит, я не смогу написать чисто браузерный транслятор, чтобы в браузере
писать Котлин, а он чтобы мне выдавал, скажем, Питон, т.к. в этом случае
я в браузере не могу проверить ни Котлин, ни Питон.

Поэтому в марте я рассмотрю возможность использования всё-таки чистого
JavaScript в качестве якорного языка для CLD, хоть в JS и не строгой типизации,
зато браузер уже содержит компилятор JS.
А типы можно комментом ведь написать!

# Март

В марте начну создание нового инструмента для решения своих
хобби-задач на основе Isomorphic-Git.

[entities]: https://github.com/OGStudio/local-host-access/blob/main/cld/entities.yml
[entities-result]: https://github.com/OGStudio/local-host-access/blob/main/src/entities.kt#L3

[splash]: ../../images/??.png
[store]: https://redux.js.org/introduction/getting-started#basic-example
