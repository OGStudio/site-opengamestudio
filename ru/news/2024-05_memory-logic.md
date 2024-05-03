Title: Игровая логика «Памяти»
Date: 2024-05-03 00:00
Category: News
Slug: memory-logic
Lang: ru

# Игровая логика «Памяти»

В апреле реализовал игровую логику игры «Память» на Python в виде модели ограниченного языка и успешно перевёл её инструментом в C++.

Модель ограниченного языка предполагает следующую архитектуру из двух частей:

1. контекст состояния
1. чистые функции без побочных эффектов, работающие лишь с контекстом

Контекст состояния игровой логики на Python получился следующим ([C++][ctx_cxx]):

```python
class memory_Context:
  def __init__(self):
    self.hiddenItems = []
    self.mismatchedItems = []
    self.playfieldItems = {}
    self.playfieldSize = 0
    self.recentField = "none"
    self.selectedId = -1
    self.selectedItems = []
    self.victory = False
```

Т.к. инструмент на текущий момент работает лишь с функциями, то контекст для Python и С++ пока пишем руками.

Функции получились примерно такими ([C++][func_cxx]):

```python
# Select item
@llm_by_value
def memory_selectItem(
  c: memory_Context
) -> memory_Context:
  if (
    len(c.selectedItems) == 2
  ):
    c.selectedItems.clear()
  #}
  c.selectedItems.append(c.selectedId)
  c.recentField = "selectedItems"
  return c
#}
```

Особенности функций для модели ограниченного языка:

* декоратор `@llm_by_value` в Python нужен для передачи аргументов по значению, а не по ссылке (по умолчанию - по ссылке)
* передача по значению обязательна для ограничения сферы действия функции ровно одним исходящим полем контекста, т.е. это реализация Принципа Единственной Ответственности (Single Responsibility Principle)
* контекст содержит поле `recentField`, представляющее собой хранимое «событие»; это поле позволяет функциям среагировать лишь в момент изменения значения интересующего поля
* функция обязана в поле `recentField` указать изменённое поле контекста либо `none` в случае отсутствия изменений
* функция принимает на вход контекст и выдаёт (изменённый) контекст на выход

Полный список фукций игровой логики «Памяти»:

| № | Функция | Инициатор вызова | Описание |
| --- | --- | --- | --- |
| 1 | `memory_generateConstPlayfield` | Пользователь | Генерируем упрощённое игровое поле, в котором последовательно парами идут элементы одной группы |
| 2 | `memory_selectItem` | Пользователь | Выбор элемента игрового поля |
| 3 | `memory_shouldDeselectMismatchedItems` | Система | Реакция снятия выделения с пары выбранных фишек различающихся групп |
| 4 | `memory_shouldDetectVictory` | Система | Реакция определения победы после скрытия всех фишек |
| 5 | `memory_shouldHideMatchingItems` | Система | Реакция скрытия пары выбранных фишек одной группы |

Для удостоверения работоспособности и идентичности работы этих функций как в Python, так и в C++, на каждую функцию ввёл минимум по одной функции проверки:

* `memory_test_generateConstPlayfield`
* `memory_test_selectItem_1x`
* `memory_test_selectItem_2x`
* `memory_test_selectItem_3x`
* `memory_test_shouldDeselectMismatchedItems`
* `memory_test_shouldDeselectMismatchedItems_itemTwice`
* `memory_test_shouldDetectVictory`
* `memory_test_shouldHideMatchingItems`

# Планы на май

Сделаю возможность сыграть одну партию игры «Память» в текстовом интерфейсе.

[ctx_cxx]: https://git.opengamestudio.org/kornerr/research-portable-memory/src/commit/6fcd542daa6242c8c23dddb88d04cda74a730328/v3/memory_Context.h
[func_cxx]: https://git.opengamestudio.org/kornerr/research-portable-memory/src/commit/6fcd542daa6242c8c23dddb88d04cda74a730328/v3/memory.cpp#L29
