# TFlex.Model.SelectionContainer

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс контейнера выбранных объектов.

## Remarks

Объект данного класса является членом класса документа и создаётся только для документов, открытых для редактирования. Т.е. такой невозможно получить у документа фрагмента или временного документа.

## Methods

### `BeginSelection`

ID: `M:TFlex.Model.SelectionContainer.BeginSelection`

Начать блок селекции

Remarks: Пока не завершится блок селекции уведомления выбора объектов не будут приходить

### `DelayedSelect(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.SelectionContainer.DelayedSelect(TFlex.Model.ModelObject)`

Выбрать объект

Parameters:
- `obj`: Объект, который требуется выбрать (поместить в контейнер выбранных объектов

Remarks: Данная функция помещает указанный объект в контейнер выбранных объектов. При этом объект помечается на всех видах документа, на которых объект является видимым. Для отмены выбора объекта можно воспользоваться функцией Deselect или DeselectAll

### `Deselect(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.SelectionContainer.Deselect(TFlex.Model.ModelObject)`

Отменить выбор объекта

Parameters:
- `obj`: Объект, выбор которого требуется отменить (удалить из контейнера выбранных объектов.

Remarks: Данная функция удаляет указанный объект из контейнера выбранных объектов. При этом отменяется пометка этого объекта на всех видах документа, на которых он является видимым.

### `DeselectAll`

ID: `M:TFlex.Model.SelectionContainer.DeselectAll`

Отменить выбор всех выбранных объектов

Remarks: Функция отменяет выбор всех выбранных объектов (производится очистка контейнера выбранных объектов)

### `EndSelection`

ID: `M:TFlex.Model.SelectionContainer.EndSelection`

Завершить блок селекции

### `GetAllObjects`

ID: `M:TFlex.Model.SelectionContainer.GetAllObjects`

Получить список выбранных объектов

Returns: Список выбранных объектов

### `GetAt(System.Int32)`

ID: `M:TFlex.Model.SelectionContainer.GetAt(System.Int32)`

Получить выбранный объект по индексу

Parameters:
- `i`: Индекс

Returns: Объект, находящийся в контейнере выбранных объектов с указанным индексом. 0 в случае ошибки

### `GetSize`

ID: `M:TFlex.Model.SelectionContainer.GetSize`

Получить количество выбранных объектов

Returns: Текущий размер контейнера выбранных объектов

### `IsSelected(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.SelectionContainer.IsSelected(TFlex.Model.ModelObject)`

Проверка, является ли объект выбранным

Parameters:
- `obj`: Объект для которого производится проверка

Returns: True, если данный объект является выбранным, то есть находится в контейнере выбранных объектов

Remarks: Данная функция выполняет проверку на наличие указанного объекта в контейнере выбранных объектов

### `Mark(TFlex.Model.ModelObject,TFlex.Model.SelectionContainer.MarkType)`

ID: `M:TFlex.Model.SelectionContainer.Mark(TFlex.Model.ModelObject,TFlex.Model.SelectionContainer.MarkType)`

Маркировать объект

Parameters:
- `obj`: Объект, который требуется маркировать
- `style`: Стиль маркировки

Remarks: Данная функция помещает указанный объект в контейнер маркированных объектов. Для отмены маркирования объекта можно воспользоваться функцией Unmark

### `Select(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.SelectionContainer.Select(TFlex.Model.ModelObject)`

Выбрать объект

Parameters:
- `obj`: Объект, который требуется выбрать (поместить в контейнер выбранных объектов

Remarks: Данная функция помещает указанный объект в контейнер выбранных объектов. При этом объект помечается на всех видах документа, на которых объект является видимым. Для отмены выбора объекта можно воспользоваться функцией Deselect или DeselectAll

### `Select(TFlex.Model.ModelObject,TFlex.Model.SelectionContainer.MarkType)`

ID: `M:TFlex.Model.SelectionContainer.Select(TFlex.Model.ModelObject,TFlex.Model.SelectionContainer.MarkType)`

Выбрать объект

Parameters:
- `obj`: Объект, который требуется выбрать (поместить в контейнер выбранных объектов
- `style`: Стиль маркировки объекта

Remarks: Данная функция помещает указанный объект в контейнер выбранных объектов. При этом объект помечается на всех видах документа, на которых объект является видимым. Для отмены выбора объекта можно воспользоваться функцией Deselect или DeselectAll

### `Unmark(TFlex.Model.ModelObject)`

ID: `M:TFlex.Model.SelectionContainer.Unmark(TFlex.Model.ModelObject)`

Отменить маркирования объекта

Parameters:
- `obj`: Объект, выбор которого требуется отменить (удалить из контейнера выбранных объектов.

Remarks: Данная функция удаляет указанный объект из контейнера маркированных объектов.
