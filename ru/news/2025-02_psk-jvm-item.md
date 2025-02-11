Title: ПСКОВ 2 на JVM
Date: 2025-02-11 00:00
Category: News
Slug: psk-jvm-item
Lang: ru

![splash][splash]

# Генерация отдельных страниц

В январе сделал половину функциональности оригинального ПСКОВа на Kotlin для JVM,
а именно: генерацию отдельных страницы HTML из Markdown.
И ПСКОВ 1, и ПСКОВ 2 генерируют файлы HTML, которые отображаются идентично
в веб-браузерах. Тем не менее, содержимое этих сгенерированных файлов отличается,
т.к. ПСКОВ 1 использует [Showdown][showdown] для конвертации Markdown в HTML,
а ПСКОВ 2 - [intellij-markdown][intellij-markdown].

Взглянем на описываемую разницу. Допустим, у нас есть следующая страница Markdown:

```
Simple page in **Markdown** to convert to **HTML**.

| № | Parser | Language |
|---|---     |---       |
| 1 | [Showdown][showdown] | JavaScript |
| 2 | [intellij-markdown][intellij-markdown] | Kotlin |

[intellij-markdown]: https://github.com/JetBrains/markdown
[showdown]: https://github.com/showdownjs/showdown
```

ПСКОВ 1 генерирует следующий файл HTML:

```
<p>Simple page in <strong>Markdown</strong> to convert to <strong>HTML</strong>.</p>
<table>
<thead>
<tr>
<th>№</th>
<th>Parser</th>
<th>Language</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><a href="https://github.com/showdownjs/showdown">Showdown</a></td>
<td>JavaScript</td>
</tr>
<tr>
<td>2</td>
<td><a href="https://github.com/JetBrains/markdown">intellij-markdown</a></td>
<td>Kotlin</td>
</tr>
</tbody>
</table>
```


ПСКОВ 2:

```
<body><p>Simple page in <strong>Markdown</strong> to convert to <strong>HTML</strong>.</p><table><thead><tr><th>№</th><th>Parser</th><th>Language</th></tr></thead><tbody><tr><td>1</td><td><a href="https://github.com/showdownjs/showdown">Showdown</a></td><td>JavaScript</td></tr><tr class="intellij-row-even"><td>2</td><td><a href="https://github.com/JetBrains/markdown">intellij-markdown</a></td><td>Kotlin</td></tr></tbody></table></body>
```

А вот как оба файла отображаются в веб-браузере:

![result][result]

Таким обрбазом, у нас идентичное отображение двух различающихся файлов.
Мой внутренний перфекционист, конечно, возмущён несоответствием, но мой
внутренний прагматик считает эту разницу несущественной.

# Февраль

В феврале доведу конвертер межъязыкового диалекта до генерации Context.

[intellij-markdown]: https://github.com/JetBrains/markdown
[result]: ../../images/2025_psk-jvm-item_result.png
[showdown]: https://github.com/showdownjs/showdown
[splash]: ../../images/2025_psk-jvm-item.png
