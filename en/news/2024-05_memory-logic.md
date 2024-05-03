Title: "Memory" game logic
Date: 2024-05-03 00:00
Category: News
Slug: memory-logic
Lang: en

# "Memory" game logic

In April I implemented "Memory" game logic in Python as limited language model and successfully converted the code to C++ by the instrument under development.

Limited language model assumes the following architecture of two parts:

1. state context
1. pure functions without side effects working only with the context

Game logic state context in Python currently looks like this ([C++][ctx_cxx]):

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

Since the instrument only works with functions at the moment, I had to write C++ context code manually.

Functions look like this ([C++][func_cxx]):

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

Limited language model functions have the following features:

* `@llm_by_value` Python decorator is used to pass arguments by value instead of by reference (which is default in Python)
* passing arguments by value is mandatory to limit function scope to only single context field, it's formalized Single Responsibility Principle
* context contains `recentField` representing a stored "event"; this allows functions to run only when necessary field changes
* function must use `recentField` to specify which field it changed or provide `none` if no action was performed
* function takes only context as an input and only returns (an updated) context as an output


"Memory" game logic has the following functions:

| № | Function | Caller| Description |
| --- | --- | --- | --- |
| 1 | `memory_generateConstPlayfield` | User | Generate simplified playfield with items of the same group following each other sequentially |
| 2 | `memory_selectItem` | User | Select playfield item |
| 3 | `memory_shouldDeselectMismatchedItems` | System | Reaction to deselect a pair of the selected items of different groups |
| 4 | `memory_shouldDetectVictory` | System | Reaction to detect victory when all items got hidden |
| 5 | `memory_shouldHideMatchingItems` | System | Reaction to hide a pair of the selected items of the same group |

To verify functions work identically in both Python and C++, I cover each function with at least one test:

* `memory_test_generateConstPlayfield`
* `memory_test_selectItem_1x`
* `memory_test_selectItem_2x`
* `memory_test_selectItem_3x`
* `memory_test_shouldDeselectMismatchedItems`
* `memory_test_shouldDeselectMismatchedItems_itemTwice`
* `memory_test_shouldDetectVictory`
* `memory_test_shouldHideMatchingItems`

# May plans

I'll make a text UI for "Memory" game.

[ctx_cxx]: https://git.opengamestudio.org/kornerr/research-portable-memory/src/commit/6fcd542daa6242c8c23dddb88d04cda74a730328/v3/memory_Context.h
[func_cxx]: https://git.opengamestudio.org/kornerr/research-portable-memory/src/commit/6fcd542daa6242c8c23dddb88d04cda74a730328/v3/memory.cpp#L29
