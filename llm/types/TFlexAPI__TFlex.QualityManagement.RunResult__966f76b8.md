# TFlex.QualityManagement.RunResult

Assembly: `TFlexAPI`
Namespace: `TFlex.QualityManagement`

## Summary

Класс с информациией о результате проверки

## Constructors

### `RunResult`

ID: `M:TFlex.QualityManagement.RunResult.#ctor`

Конструктор по умолчанию

### `RunResult(System.Collections.Generic.IEnumerable`1{TFlex.Model.ModelObject},System.Boolean)`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.Model.ModelObject},System.Boolean)`

Конструктор с добавлением коллекции записей и indicating the possibility of fix

### `RunResult(System.Collections.Generic.IEnumerable`1{TFlex.QualityManagement.RunResultEntry})`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.QualityManagement.RunResultEntry})`

Конструктор с добавлением коллекции записей

### `RunResult(TFlex.QualityManagement.RunResultEntry)`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(TFlex.QualityManagement.RunResultEntry)`

Конструктор с добавлением записи

## Methods

### `RunResult`

ID: `M:TFlex.QualityManagement.RunResult.#ctor`

Конструктор по умолчанию

### `RunResult(System.Collections.Generic.IEnumerable`1{TFlex.Model.ModelObject},System.Boolean)`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.Model.ModelObject},System.Boolean)`

Конструктор с добавлением коллекции записей и indicating the possibility of fix

### `RunResult(System.Collections.Generic.IEnumerable`1{TFlex.QualityManagement.RunResultEntry})`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(System.Collections.Generic.IEnumerable`1{TFlex.QualityManagement.RunResultEntry})`

Конструктор с добавлением коллекции записей

### `RunResult(TFlex.QualityManagement.RunResultEntry)`

ID: `M:TFlex.QualityManagement.RunResult.#ctor(TFlex.QualityManagement.RunResultEntry)`

Конструктор с добавлением записи

## Propertys

### `Entries`

ID: `P:TFlex.QualityManagement.RunResult.Entries`

Коллекция записей результата проверки

### `FullMessage`

ID: `P:TFlex.QualityManagement.RunResult.FullMessage`

Полное описание результата проверки(отображается во второй колонке)

### `IsEditable`

ID: `P:TFlex.QualityManagement.RunResult.IsEditable`

Можно ли редактировать результат проверки

### `IsFixable`

ID: `P:TFlex.QualityManagement.RunResult.IsFixable`

Исправим ли результат проверки

### `ShortMessage`

ID: `P:TFlex.QualityManagement.RunResult.ShortMessage`

Краткое описание результата проверки(отображается в первой колонке)

### `State`

ID: `P:TFlex.QualityManagement.RunResult.State`

Состояние результата проверки
