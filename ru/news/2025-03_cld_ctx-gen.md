Title: CLD: Генерация контекста
Date: 2025-03-11 00:00
Category: News
Slug: cld_ctx-gen
Lang: ru

![splash][splash]

# Генерация контекста

В феврале доработал транслятор Межъязыкового диалекта
(**C**ross-**l**anguage **d**ialect) (CLD) до генерации
Контекста на основе описания в YML. Сгенерированные Контексты уже использованы
в следующих проектах:

* CLD (транслятор CLD генерирует свой собственный Контекст)
* LHA
* PSKOV

Доселе я никогда прежде не тратил время на объяснение сути Контекста, поэтому
сейчас самое время для очень краткого описания: Контекст очень близок
к понятию [Store в Redux][store]. К сожалению, на этом месте пояснение заканчиваю,
т.к. без каких-либо весомых доказательств пользы Контекста не готов
доказывать его применимость. Как только придёт таковое время, так я сразу
расскажу детали.

Теперь вернёмся к генерации Контекста. Вот как выглядит YML Контекста в проекте LHA
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

Транслятор CLD преобразует его в следующий код на Kotlin ([entities.kt][entities-result]):

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

# Март

На текущий момент Kotlin является якорным языком CLD. Для использования
Kotlin необходимо установить соответствующие инструменты Java (Gradle,
Android Studio либо сама JVM). Такое требование делает создание инструмента
разработки чисто для браузера невозможным. Однако, я считаю работу инструмента
в браузере ключевой особенностью для достижения портируемости кода.

Поэтому в марте я планирую создать заготовку инструмента, работающего в браузере.

[entities]: https://github.com/OGStudio/local-host-access/blob/main/cld/entities.yml
[entities-result]: https://github.com/OGStudio/local-host-access/blob/main/src/entities.kt#L3
[splash]: ../../images/2025-03_redux-data-flow.jpg
[store]: https://redux.js.org/introduction/getting-started#basic-example
