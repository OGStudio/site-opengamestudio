Title: ПСКОВ 2 на JVM
Date: 2025-02-12 00:00
Category: News
Slug: psk-jvm-item
Lang: ru

![pks-jvm-item][pks-jvm-item]

# Генерация одной страницы

В январе сделал часть функциональности ПСКОВа на Kotlin для JVM, а именно:
сделал генерацию отдельных страницы из Markdown в HTML.
Сгенерированные файлы HTML в веб-браузере отображаются идентично тому,
что генерирует ПСКОВ 1. А вот непосредственное содержимое генерированных
файлов HTML заметно отличается.
Причина в том, что ПСКОВ 1 использует [Showdown][showdown] для перевода
Markdown в HTML. А вот ПСКОВ 2 использует [intellij-markdown][intellij-markdown].

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


ПСКОВ 2 (JVM) генерирует следующий файл HTML:

```
<body><p>Simple page in <strong>Markdown</strong> to convert to <strong>HTML</strong>.</p><table><thead><tr><th>№</th><th>Parser</th><th>Language</th></tr></thead><tbody><tr><td>1</td><td><a href="https://github.com/showdownjs/showdown">Showdown</a></td><td>JavaScript</td></tr><tr class="intellij-row-even"><td>2</td><td><a href="https://github.com/JetBrains/markdown">intellij-markdown</a></td><td>Kotlin</td></tr></tbody></table></body>
```

А вот как оба файла отображаются в веб-браузере:

![result][result]

Т.е. отображение идентичное, а файлы разные, ибо парсеры
по-разному работают с переносом строк.
Мой внутренний перфекционист, конечно, возмущён несоответствием, но мой внутренний практик считает эту разницу содержимого файлов несущественной.

# Февраль

В феврале доведу конвертер YML -> Kotlin до возможности генерировать Context,
после чего подключу Context к Local Host Access и ПСКОВу.

[intellij-markdown]: https://github.com/JetBrains/markdown
[result]: ../../images/2025_psk-jvm-item_result.png
[showdown]: https://github.com/showdownjs/showdown
