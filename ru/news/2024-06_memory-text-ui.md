Title: Текстовый интерфейс «Памяти»
Date: 2024-06-14 00:00
Category: News
Slug: memory-text-ui
Lang: ru

# Текстовый интерфейс «Памяти»

В мае реализовал текстовый интерфейс игры «Память» на Python. В C++ перевёл инструментом.

Реализация логического игрового цикла привела к появлению контроллера, управляющего
контекстом. Создание контроллера на Python прошло без происшествий, а вот с версией
для C++ пришлось помучиться. Мучения были вызваны тем, что контроллер использует
[std::any][any] из C++17, а инструмент ограничен C++11 с целью поддержки OpenWrt.

Что касается объёма кода, то картина получилась следующей (в строках):

* (Python) Портируемый код логики: 360
* (Python) Портируемый код тестов: 565
* (Python) Непортируемый код контроллера, ввода-вывода и т.п.: 350
* (C++) Портированный код логики: 360
* (C++) Портированный код тестов: 586
* (C++) Непортируемый код контроллера, ввода-вывода и т.п.: 565

В процентах выглядит это так:

| Язык | Всего строк кода | Портируемого | Непортируемого |
| --- | --- | --- | --- |
| Python | 1275 (**100%**) | 925 (**72%**) | 350 (**28%**) |
| C++ | 1511 (**100%**) | 946 (**62%**) | 565 (**38%**) |

Выходит, что разработка версии игры «Память» на языке С++ оказалась на
62% строк кода дешевле, чем была бы без использования инструмента. Цифры
приятные.

Сам текстовый интерфейс игры «Память» на текущий момент выглядит следующим образом:

<iframe width="560" height="315" src="https://www.youtube.com/embed/tChSjw5W8KQ?si=WO5MYLCBhgstVshl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Планы на июнь

В июне сделаю простейший графический интерфейс для версии Python.

[any]: https://en.cppreference.com/w/cpp/utility/any
