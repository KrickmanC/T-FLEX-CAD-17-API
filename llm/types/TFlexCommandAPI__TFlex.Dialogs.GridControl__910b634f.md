# TFlex.Dialogs.GridControl

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Сетка с элементами управления

## Constructors

### `GridControl(System.String)`

ID: `M:TFlex.Dialogs.GridControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

### `GridControl(System.String,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.#ctor(System.String,System.Int32,System.Int32)`

Parameters:
- `id`: Идентификатор элемента
- `rowCount`: Количество строк
- `columnCount`: Количество столбцов

## Methods

### `GridControl(System.String)`

ID: `M:TFlex.Dialogs.GridControl.#ctor(System.String)`

Parameters:
- `id`: Идентификатор элемента

### `GridControl(System.String,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.#ctor(System.String,System.Int32,System.Int32)`

Parameters:
- `id`: Идентификатор элемента
- `rowCount`: Количество строк
- `columnCount`: Количество столбцов

### `GetColumnSpan(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.GetColumnSpan(System.Int32,System.Int32)`

Получить ширину данной ячейки в клетках

### `GetControl(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.GetControl(System.Int32,System.Int32)`

Получить элемент управления в заданной ячейке

### `GetRowSpan(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.GetRowSpan(System.Int32,System.Int32)`

Получить высоту данной ячейки в клетках

### `SetAutoHeight(System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.SetAutoHeight(System.Int32)`

Задать автоподбор высоты для строки

Parameters:
- `rowIndex`: Индекс строки

### `SetAutoWidth(System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.SetAutoWidth(System.Int32)`

Задать автоподбор ширины для колонки

Parameters:
- `columnIndex`: Индекс колонки

### `SetColumnSpan(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.SetColumnSpan(System.Int32,System.Int32,System.Int32)`

Установить ширину данной ячейки в клетках

### `SetControl(System.Int32,System.Int32,TFlex.Dialogs.BaseControl)`

ID: `M:TFlex.Dialogs.GridControl.SetControl(System.Int32,System.Int32,TFlex.Dialogs.BaseControl)`

Установить элемент управления заданной ячейки

### `SetDimensions(System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.SetDimensions(System.Int32,System.Int32)`

Установить размер сетки

### `SetRowSpan(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Dialogs.GridControl.SetRowSpan(System.Int32,System.Int32,System.Int32)`

Установить высоту данной ячейки в клетках

## Propertys

### `AutoRatioValue`

ID: `P:TFlex.Dialogs.GridControl.AutoRatioValue`

Автоподбор пропорции по содержимому. Используется в HeightRatios и WidthRatios.

### `ColumnCount`

ID: `P:TFlex.Dialogs.GridControl.ColumnCount`

Количество столбцов

### `HeightRatios`

ID: `P:TFlex.Dialogs.GridControl.HeightRatios`

Коллекция, хранящая отношения высоты для строк

### `RowCount`

ID: `P:TFlex.Dialogs.GridControl.RowCount`

Количество строк

### `WidthRatios`

ID: `P:TFlex.Dialogs.GridControl.WidthRatios`

Коллекция, хранящая отношения ширины для столбцов
