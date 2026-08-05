Title: Building an Android speech recognition prototype
Date: 2026-08-05
Category: News
Slug: ai-speech
Lang: en

<video controls width="700">
    <source src="../../vid/2026-08_ai-speech.mp4" type="video/mp4"/>
</video>

# July

AI came firmly into my life because I started creating a prototype of
a speech recognition application for Android. So far, I have implemented
both Speech-to-text and Text-to-speech.

Speech-to-text is powered by [Vosk][vosk] and Text-to-speech by
[Sherpa-Onnx][sherpa]. Both libraries work on-device without sending data
to a server.

# August

I'll integrate an LLM between STT and TTS to enable the application to provide
voice consultations based on the provided dataset.

P.S. I publish weekly reports in the [TG channel][tg].

[sherpa]: https://k2-fsa.github.io/sherpa/onnx
[tg]: https://t.me/kotlindialect
[vosk]: https://alphacephei.com/vosk
