# TFlex.Dialogs.SimpleListControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Упрощённый вариант ListControl, позволяющий избежать явного создания класса модели данных для простых списков

## Constructors

### `SimpleListControl(System.String)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор контрола

### `SimpleListControl(System.String,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String,System.Int32)`

Parameters:
- `id`: Идентификатор контрола
- `columnCount`: Количество столбцов

### `SimpleListControl(System.String,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String,System.Int32,System.Int32)`

Parameters:
- `id`: Идентификатор контрола
- `rowCount`: Количество строк
- `columnCount`: Количество столбцов

## Methods

### `SimpleListControl(System.String)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор контрола

### `SimpleListControl(System.String,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String,System.Int32)`

Parameters:
- `id`: Идентификатор контрола
- `columnCount`: Количество столбцов

### `SimpleListControl(System.String,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.#ctor(System.String,System.Int32,System.Int32)`

Parameters:
- `id`: Идентификатор контрола
- `rowCount`: Количество строк
- `columnCount`: Количество столбцов

### `AddRow`

ID: `M:TFlex.Dialogs.SimpleListControl.AddRow`

Вставить строку в конец списка

### `AddRow(System.Collections.IList)`

ID: `M:TFlex.Dialogs.SimpleListControl.AddRow(System.Collections.IList)`

Вставить строку в конец списка

### `AddRow(System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.AddRow(System.Object)`

Вставить строку в конец списка

### `AddRow(System.Object[])`

ID: `M:TFlex.Dialogs.SimpleListControl.AddRow(System.Object[])`

Вставить строку в конец списка

### `AddRows(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.AddRows(System.Int32)`

Вставить строки в конец списка

### `GetAlignment(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetAlignment(System.Int32,System.Int32)`

Возвращает выравние для ячейки

### `GetCheckState(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetCheckState(System.Int32,System.Int32)`

Возвращает CheckState элемента списка

### `GetContent(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetContent(System.Int32,System.Int32)`

Возвращает содержимое ячейки списка

### `GetDefaultAlignment(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetDefaultAlignment(System.Int32)`

Возвращает выравние по умолчанию для колонки

### `GetHeader(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetHeader(System.Int32)`

Возвращает данные заголовка списка

### `GetIcon(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetIcon(System.Int32,System.Int32)`

Возвращает иконку элемента списка

### `GetParentRow(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetParentRow(System.Int32)`

Получить индекс родительской строки. Должен быть включен режим IsHierarchyOn.

### `GetRowId(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetRowId(System.Int32)`

Получить идентификатор строки. Должен быть включен режим IsIdMappingOn.

### `GetToolTip(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetToolTip(System.Int32,System.Int32)`

Возвращает подсказку элемента списка

### `GetWidthCoefficient(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.GetWidthCoefficient(System.Int32)`

Возвращает коэффициент ширины столбца

Remarks: См. ListItemRole.WidthCoefficientRole для дополнительой информации о значении данного свойства

### `HasAlignment(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.HasAlignment(System.Int32,System.Int32)`

Возвращает true, если выставлено выравние для ячейки

### `HasDefaultAlignment(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.HasDefaultAlignment(System.Int32)`

Возвращает true, если выставлено выравние по умолчанию для колонки

### `InsertRow(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.InsertRow(System.Int32)`

Вставить строку в список

### `InsertRow(System.Int32,System.Collections.IList)`

ID: `M:TFlex.Dialogs.SimpleListControl.InsertRow(System.Int32,System.Collections.IList)`

Вставить строку в список

### `InsertRow(System.Int32,System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.InsertRow(System.Int32,System.Object)`

Вставить строку в список

### `InsertRow(System.Int32,System.Object[])`

ID: `M:TFlex.Dialogs.SimpleListControl.InsertRow(System.Int32,System.Object[])`

Вставить строку в список

### `InsertRows(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.InsertRows(System.Int32,System.Int32)`

Вставить строки в список

### `IsColumnTree(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.IsColumnTree(System.Int32)`

Колонка для отображения структуры дерева

### `RemoveAll`

ID: `M:TFlex.Dialogs.SimpleListControl.RemoveAll`

Удалить все строки из списка

### `RemoveRow(System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.RemoveRow(System.Int32)`

Удалить строку из списка

### `RemoveRows(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.RemoveRows(System.Int32,System.Int32)`

Удалить строки из списка

### `SetAlignment(System.Int32,System.Int32,System.Nullable`1{TFlex.Dialogs.ListItemAlignment})`

ID: `M:TFlex.Dialogs.SimpleListControl.SetAlignment(System.Int32,System.Int32,System.Nullable`1{TFlex.Dialogs.ListItemAlignment})`

Устанавливает выравнимание ячейки

### `SetCheckState(System.Int32,System.Int32,System.Nullable`1{TFlex.Dialogs.CheckState})`

ID: `M:TFlex.Dialogs.SimpleListControl.SetCheckState(System.Int32,System.Int32,System.Nullable`1{TFlex.Dialogs.CheckState})`

Устанавливает CheckState элемента списка

### `SetColumnTree(System.Int32,System.Boolean)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetColumnTree(System.Int32,System.Boolean)`

Колонка для отображения структуры дерева

### `SetContent(System.Int32,System.Int32,System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetContent(System.Int32,System.Int32,System.Object)`

Устанавливает содержимое ячейки списка

### `SetDefaultAlignment(System.Int32,System.Nullable`1{TFlex.Dialogs.ListItemAlignment})`

ID: `M:TFlex.Dialogs.SimpleListControl.SetDefaultAlignment(System.Int32,System.Nullable`1{TFlex.Dialogs.ListItemAlignment})`

Устанавливает выравнимание ячейки по умолчанию для колонки

### `SetHeader(System.Int32,System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeader(System.Int32,System.Object)`

Устанавливает данные заголовка списка

### `SetHeader(System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeader(System.Object)`

Устанавливает данные заголовка списка

### `SetHeaderIcon(System.Int32,TFlex.Dialogs.Icon)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeaderIcon(System.Int32,TFlex.Dialogs.Icon)`

Устанавливает иконку для заголовка колонки

### `SetHeaderToolTip(System.Int32,System.String)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeaderToolTip(System.Int32,System.String)`

Устанавливает подсказку для заголовка колонки

### `SetHeaders(System.Collections.IList)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeaders(System.Collections.IList)`

Устанавливает данные всех заголовков списка

### `SetHeaders(System.Object[])`

ID: `M:TFlex.Dialogs.SimpleListControl.SetHeaders(System.Object[])`

Устанавливает данные всех заголовков списка

### `SetIcon(System.Int32,System.Int32,TFlex.Dialogs.Icon)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetIcon(System.Int32,System.Int32,TFlex.Dialogs.Icon)`

Устанавливает иконку элемента списка

### `SetParentRow(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetParentRow(System.Int32,System.Int32)`

Установить индекс родительской строки. Должен быть включен режим IsHierarchyOn.

### `SetParentRowId(System.Int32,System.Int64)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetParentRowId(System.Int32,System.Int64)`

Установить индекс родительской строки. Должены быть включены режим IsHierarchyOn и IsIdMappingOn.

### `SetRowContent(System.Int32,System.Collections.IList)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetRowContent(System.Int32,System.Collections.IList)`

Устанавливает содержимое ячеек в строке списка

### `SetRowContent(System.Int32,System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetRowContent(System.Int32,System.Object)`

Устанавливает содержимое ячеек в строке списка

### `SetRowContent(System.Int32,System.Object[])`

ID: `M:TFlex.Dialogs.SimpleListControl.SetRowContent(System.Int32,System.Object[])`

Устанавливает содержимое ячеек в строке списка

### `SetRowId(System.Int32,System.Int64)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetRowId(System.Int32,System.Int64)`

Установить идентификатор строки. Должен быть включен режим IsIdMappingOn.

### `SetToolTip(System.Int32,System.Int32,System.Object)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetToolTip(System.Int32,System.Int32,System.Object)`

Устанавливает подсказку элемента списка

### `SetWidthCoefficient(System.Int32,System.Double)`

ID: `M:TFlex.Dialogs.SimpleListControl.SetWidthCoefficient(System.Int32,System.Double)`

Устанавливает коэффициент ширины столбца

Remarks: См. ListItemRole.WidthCoefficientRole для дополнительой информации о значении данного свойства

### `SetWidthCoefficients(System.Collections.Generic.IList`1{System.Double})`

ID: `M:TFlex.Dialogs.SimpleListControl.SetWidthCoefficients(System.Collections.Generic.IList`1{System.Double})`

Устанавливает коэффициенты ширины всех столбцов

Remarks: См. ListItemRole.WidthCoefficientRole для дополнительой информации о значении данного свойства

### `SetWidthCoefficients(System.Double[])`

ID: `M:TFlex.Dialogs.SimpleListControl.SetWidthCoefficients(System.Double[])`

Устанавливает коэффициенты ширины всех столбцов

Remarks: См. ListItemRole.WidthCoefficientRole для дополнительой информации о значении данного свойства

## Propertys

### `ColumnCount`

ID: `P:TFlex.Dialogs.SimpleListControl.ColumnCount`

Количество столбцов в списке

### `RowCount`

ID: `P:TFlex.Dialogs.SimpleListControl.RowCount`

Количество строк в списке

## Events

### `CheckStateChanged`

ID: `E:TFlex.Dialogs.SimpleListControl.CheckStateChanged`

Событие смены значения чекбокса
