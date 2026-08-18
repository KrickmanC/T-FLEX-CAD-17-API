# TFlex.Model.DeleteOptions

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Опции удаления объектов модели

## Constructors

### `DeleteOptions`

ID: `M:TFlex.Model.DeleteOptions.#ctor`

Конструктор по умолчанию

### `DeleteOptions(System.Boolean)`

ID: `M:TFlex.Model.DeleteOptions.#ctor(System.Boolean)`

Конструктор

Parameters:
- `silent`: Режим "без вопроса". Если данный параметр имеет значение true, то вопрос об удалении зависимых элементов не задаётся

## Methods

### `DeleteOptions`

ID: `M:TFlex.Model.DeleteOptions.#ctor`

Конструктор по умолчанию

### `DeleteOptions(System.Boolean)`

ID: `M:TFlex.Model.DeleteOptions.#ctor(System.Boolean)`

Конструктор

Parameters:
- `silent`: Режим "без вопроса". Если данный параметр имеет значение true, то вопрос об удалении зависимых элементов не задаётся

## Propertys

### `DeleteObjectsOnLayer`

ID: `P:TFlex.Model.DeleteOptions.DeleteObjectsOnLayer`

Используется методом DeleteObjects

Remarks: Задаёт удаление слоя и всех элементов, находящихся на нем. Если false, слой будет удален, если только на нем нет элементов.

### `DeletePageObjects`

ID: `P:TFlex.Model.DeleteOptions.DeletePageObjects`

Используется методом DeletePage

Remarks: Задаёт удаление страницы и всех элементов, находящихся на ней. Если false, станица будет удалена, если только на ней нет элементов.

### `DisableMacrosSmartFragments`

ID: `P:TFlex.Model.DeleteOptions.DisableMacrosSmartFragments`

Отключить запуск макроса у смарт-фрагментов (событие удаления фрагмента)

### `Exclude`

ID: `P:TFlex.Model.DeleteOptions.Exclude`

Исключить удаляемые элементы из модели

### `Silent`

ID: `P:TFlex.Model.DeleteOptions.Silent`

Режим "без вопроса"
