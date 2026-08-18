# TFlex.Dialogs.ListControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Элемент управления, отображающий данные в виде списка

## Constructors

### `ListControl(System.String)`

ID: `M:TFlex.Dialogs.ListControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор контрола

### `ListControl(System.String,TFlex.Dialogs.ListControlModel)`

ID: `M:TFlex.Dialogs.ListControl.#ctor(System.String,TFlex.Dialogs.ListControlModel)`

Parameters:
- `id`: Идентификатор контрола
- `model`: Модель данных

## Methods

### `ListControl(System.String)`

ID: `M:TFlex.Dialogs.ListControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор контрола

### `ListControl(System.String,TFlex.Dialogs.ListControlModel)`

ID: `M:TFlex.Dialogs.ListControl.#ctor(System.String,TFlex.Dialogs.ListControlModel)`

Parameters:
- `id`: Идентификатор контрола
- `model`: Модель данных

### `CollapseAll`

ID: `M:TFlex.Dialogs.ListControl.CollapseAll`

Свернуть все строки. IsHierarchyOn должно быть true.

### `ExpandAll`

ID: `M:TFlex.Dialogs.ListControl.ExpandAll`

Развернуть все строки. IsHierarchyOn должно быть true.

### `ExpandAllTheWayTo(System.Int32)`

ID: `M:TFlex.Dialogs.ListControl.ExpandAllTheWayTo(System.Int32)`

Развернуть все строки до row. IsHierarchyOn должно быть true.

### `ExpandAllTheWayTo(System.Int64)`

ID: `M:TFlex.Dialogs.ListControl.ExpandAllTheWayTo(System.Int64)`

Развернуть все строки до строки с идентификатором rowId. IsHierarchyOn должно быть true.

### `GetRowById(System.Int64)`

ID: `M:TFlex.Dialogs.ListControl.GetRowById(System.Int64)`

Получить идекс строки по идентификатору. IsIdMappingOn должно быть true.

### `IsExpanded(System.Int32)`

ID: `M:TFlex.Dialogs.ListControl.IsExpanded(System.Int32)`

Развернута ли строка.

### `IsExpanded(System.Int64)`

ID: `M:TFlex.Dialogs.ListControl.IsExpanded(System.Int64)`

Развернута ли строка.

### `SetExpanded(System.Int32,System.Boolean)`

ID: `M:TFlex.Dialogs.ListControl.SetExpanded(System.Int32,System.Boolean)`

Развернута ли строка. IsHierarchyOn должно быть true.

### `SetExpanded(System.Int64,System.Boolean)`

ID: `M:TFlex.Dialogs.ListControl.SetExpanded(System.Int64,System.Boolean)`

Развернута ли строка. IsHierarchyOn должно быть true.

## Propertys

### `Buttons`

ID: `P:TFlex.Dialogs.ListControl.Buttons`

Коллекция кнопок, отображаемых контролом

### `EditMode`

ID: `P:TFlex.Dialogs.ListControl.EditMode`

Режим редактирования ячеек ListControl-а

### `GridLinesVisibility`

ID: `P:TFlex.Dialogs.ListControl.GridLinesVisibility`

Режим отображения линий сетки

### `IsHierarchyOn`

ID: `P:TFlex.Dialogs.ListControl.IsHierarchyOn`

Включить поддержку иерархии строк. Для задания вложенность задается родительская строка.

### `IsIdMappingOn`

ID: `P:TFlex.Dialogs.ListControl.IsIdMappingOn`

Включить поддержку идентификации строк по id

### `IsStretchHeight`

ID: `P:TFlex.Dialogs.ListControl.IsStretchHeight`

Элемент управления растянут по вертикали, чтобы заполнить все доступное пространство.

### `Model`

ID: `P:TFlex.Dialogs.ListControl.Model`

Модель данных списка

### `SelectedRow`

ID: `P:TFlex.Dialogs.ListControl.SelectedRow`

Возвращает индекс первой выбранной строки или -1

### `SelectedRows`

ID: `P:TFlex.Dialogs.ListControl.SelectedRows`

Коллекция индексов выбранных элементов

## Events

### `ContextMenuClicked`

ID: `E:TFlex.Dialogs.ListControl.ContextMenuClicked`

Событие о нажатии в контекстном меню

### `ContextMenuOpening`

ID: `E:TFlex.Dialogs.ListControl.ContextMenuOpening`

Событие об открытии контекстного меню

### `IconClicked`

ID: `E:TFlex.Dialogs.ListControl.IconClicked`

Событие при клике в иконку списка

### `ItemExpandChanged`

ID: `E:TFlex.Dialogs.ListControl.ItemExpandChanged`

Событие о смене развернутости элементов списка

### `ItemHighlighted`

ID: `E:TFlex.Dialogs.ListControl.ItemHighlighted`

Событие наведения указателя мыши на объект в списке

### `SelectionChanged`

ID: `E:TFlex.Dialogs.ListControl.SelectionChanged`

Событие о смене выбранных элементов списка
