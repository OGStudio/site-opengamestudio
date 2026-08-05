Title: Разработка прототипа голосового приложения для Android
Date: 2026-08-05
Category: News
Slug: ai-speech
Lang: ru

<video controls width="700">
    <source src="../../vid/2026-08_ai-speech.mp4" type="video/mp4"/>
</video>

# Июль

В июле ИИ плотно вошёл в мою жизнь, так как я начал создание прототипа приложения
Android для распознавания голоса. На текущий момент я сделал как распознавание
текста (Speech-to-text), так и произношение текста (Text-to-speech).

Распознавание голоса сделал с помощью [Vosk][vosk]. Произношение текста —
с помощью [Sherpa-Onnx][sherpa]. Обе библиотеки работают прямо на устройстве
без обращения к серверу.

# Август

В августе между STT и TTS добавлю LLM, чтобы приложение Android могло
консультировать человека голосом по предоставленному набору данных.

PS: Еженедельные отчёты по этой разработке публикую в [канале ТГ][tg].

[sherpa]: https://k2-fsa.github.io/sherpa/onnx
[tg]: https://t.me/kotlindialect
[vosk]: https://alphacephei.com/vosk
