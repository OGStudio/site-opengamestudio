Title: Первая рабочая версия Local Host Access
Date: 2024-12-10 00:00
Category: News
Slug: lha-jvm-macos
Lang: ru

![web-test][web-test]

# Local Host Access

На текущий момент мне удалось поддержать всю функциональность
Local File System Access в рамках крошечного веб-сервера Local Host Access
на платформах JVM и macOS. К примеру, вот эту самую статью я уже
генерировал с помощью Local Host Access на macOS.

Выбор Kotlin себя вполне оправдал, хотя вскрылись и недостатки:

1. Kotlin чаще всего используется для JVM, поэтому найти информацию по Kotlin Native (Linux, macOS, Windows) крайне сложно из-за малой растространённости Kotlin на перечисленных платформах
1. Синтаксис вызова функций C внутри языка Kotlin настолько неочевиден, что без помощи Интернета не обойтись
1. Мой [вопрос на форуме Kotlin Native][question] по вызову функции stat() в C ждёт ответа с 18-го ноября

# Декабрь

В декабре я планирую добавить поддержку Linux и Windows для Local Host Access.

[web-test]: ../../images/2024_web-test.jpg
[question]: https://discuss.kotlinlang.org/t/how-to-call-stat-c-function-to-get-file-type/29541
