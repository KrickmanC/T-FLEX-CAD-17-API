# TFlex.Model.Model2D.Table

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс для работы с таблицей

## Methods

### `Clear(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.Clear(System.UInt32)`

Очистка одержимого ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

### `Delete`

ID: `M:TFlex.Model.Model2D.Table.Delete`

Удаление таблицы

Remarks: Курсор будет установлен на следующем после таблицы символе. Параметры выделения фрагмента будут потеряны

### `DeleteColumn(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.DeleteColumn(System.UInt32)`

Удаление столбца

Parameters:
- `cell`: Порядковый номер ячейки, находящейся в удаляемом столбце

### `DeleteRow(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.DeleteRow(System.UInt32)`

Удаление строки

Parameters:
- `cell`: Порядковый номер ячейки, находящейся в удаляемой строке

### `GetCellData(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellData(System.UInt32)`

Получение данных ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

### `GetCellHeight(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellHeight(System.UInt32)`

Получение высоты ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

Returns: Высота ячейки

### `GetCellProperties(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellProperties(System.UInt32)`

Получение параметров ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

Returns: Параметры ячейки таблицы

Remarks: Курсор будет перемещён в начало заданной ячейки таблицы. Параметры выделения фрагмента будут потеряны

### `GetCellRectangle(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellRectangle(System.UInt32)`

Получение прямоугольника ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

### `GetCellText(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellText(System.UInt32)`

Получение текста в ячейке

Parameters:
- `cell`: Порядковый номер ячейки таблицы

Returns: Строка с текстом

### `GetCellText(System.UInt32,System.Boolean)`

ID: `M:TFlex.Model.Model2D.Table.GetCellText(System.UInt32,System.Boolean)`

Получение текста в ячейке

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `useBraces`: Указывает, содержит ли строка символы форматирования

Returns: Строка с текстом

### `GetCellTextLength(System.IntPtr)`

ID: `M:TFlex.Model.Model2D.Table.GetCellTextLength(System.IntPtr)`

Получение количества символов в ячейке

Parameters:
- `cellHandle`: Дескриптор ячейки таблицы

Returns: Количество символов в ячейке

### `GetCellTextLength(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellTextLength(System.UInt32)`

Получение количества символов в ячейке

Parameters:
- `cell`: Порядковый номер ячейки таблицы

Returns: Количество символов в ячейке

### `GetCellWidth(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellWidth(System.UInt32)`

Получение ширины ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы

Returns: Ширина ячейки

### `GetCellsProperties(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.GetCellsProperties(System.UInt32,System.UInt32)`

Получение параметров прямоугольного фрагмента таблицы

Parameters:
- `cell1`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента
- `cell2`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента

Returns: Параметры прямоугольного фрагмента таблицы

Remarks: Курсор будет перемещён в начало левой верхней ячейки таблицы. Параметры выделения фрагмента будут потеряны

### `InsertColumns(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.InsertProperties)`

ID: `M:TFlex.Model.Model2D.Table.InsertColumns(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.InsertProperties)`

Вставка столбцов

Parameters:
- `count`: Количество столбцов
- `cell`: Порядковый номер ячейки таблицы, находящейся в столбце, относительно которого надо вставить новые столбцы
- `props`: Параметр вставки

### `InsertRows(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.InsertProperties)`

ID: `M:TFlex.Model.Model2D.Table.InsertRows(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.InsertProperties)`

Вставка строк

Parameters:
- `count`: Количество строк
- `cell`: Порядковый номер ячейки таблицы, находящейся в строке, относительно которой надо вставить новые строки
- `props`: Параметр вставки

### `InsertText(System.UInt32,System.UInt32,System.String)`

ID: `M:TFlex.Model.Model2D.Table.InsertText(System.UInt32,System.UInt32,System.String)`

Вставка текста с использованием формата символа по умолчанию

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `position`: Порядковый номер символа относительно начала ячейки, перед которым надо вставить текст
- `text`: Текст

Remarks: После вставки курсор будет перемещён в конец вставленного текста Параметры выделения фрагмента будут потеряны

### `InsertText(System.UInt32,System.UInt32,System.String,TFlex.Model.Model2D.CharFormat)`

ID: `M:TFlex.Model.Model2D.Table.InsertText(System.UInt32,System.UInt32,System.String,TFlex.Model.Model2D.CharFormat)`

Вставка текста с использованием заданного формата символов

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `position`: Порядковый номер символа относительно начала ячейки, перед которым надо вставить текст
- `text`: Текст
- `format`: Формат символов

Remarks: После вставки курсор будет перемещён в конец вставленного текста Параметры выделения фрагмента будут потеряны

### `InsertTextWithHyperlinks(System.UInt32,System.UInt32,System.String)`

ID: `M:TFlex.Model.Model2D.Table.InsertTextWithHyperlinks(System.UInt32,System.UInt32,System.String)`

Вставка текста с использованием формата символа по умолчанию

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `position`: Порядковый номер символа относительно начала ячейки, перед которым надо вставить текст
- `text`: Текст содержащий гиперссылоки аналогичные гиперссылкам в html

Remarks: После вставки курсор будет перемещён в конец вставленного текста Параметры выделения фрагмента будут потеряны Примеры ссылки SomeText

### `MergeCells`

ID: `M:TFlex.Model.Model2D.Table.MergeCells`

Объединение выделенных ячеек

Remarks: После объединения курсор будет перемещён в начало образовавшейся ячейки Текст ячеек, находящихся в выделенном фрагменте будет также объединён

### `MergeCells(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.MergeCells(System.UInt32,System.UInt32)`

Объединение ячеек, лежащих в прямоугольном фрагменте, заданном диагональю

Parameters:
- `cell1`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента
- `cell2`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента

Remarks: После объединения курсор будет перемещён в начало образовавшейся ячейки Текст ячеек, находящихся во фрагменте будет также объединён Параметры выделения фрагмента будут потеряны

### `SelectAll`

ID: `M:TFlex.Model.Model2D.Table.SelectAll`

Выделение всей таблицы

### `SetCellData(System.UInt32,System.IntPtr)`

ID: `M:TFlex.Model.Model2D.Table.SetCellData(System.UInt32,System.IntPtr)`

Выставление данных ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `data`: Данные ячейки

### `SetCellHeight(System.UInt32,System.Double,TFlex.Model.Model2D.SizeMode)`

ID: `M:TFlex.Model.Model2D.Table.SetCellHeight(System.UInt32,System.Double,TFlex.Model.Model2D.SizeMode)`

Установка высоты ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `height`: Новая высота ячейки
- `mode`: Режим высоты ячейки

Remarks: Будет изменена высота всей строки, содержащей данную ячейку

### `SetCellProperties(System.UInt32,TFlex.Model.Model2D.Table.CellProperties)`

ID: `M:TFlex.Model.Model2D.Table.SetCellProperties(System.UInt32,TFlex.Model.Model2D.Table.CellProperties)`

Установка параметров ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `props`: Новые параметры ячейки таблицы

Remarks: Курсор будет перемещён в начало заданной ячейки таблицы. Параметры выделения фрагмента будут потеряны

### `SetCellWidth(System.UInt32,System.Double)`

ID: `M:TFlex.Model.Model2D.Table.SetCellWidth(System.UInt32,System.Double)`

Установка ширины ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `width`: Новая ширина ячейки

Remarks: Будет изменена ширина всего столбца, содержащего данную ячейку

### `SetCellWidth(System.UInt32,System.Double,TFlex.Model.Model2D.ColumnSizeMode)`

ID: `M:TFlex.Model.Model2D.Table.SetCellWidth(System.UInt32,System.Double,TFlex.Model.Model2D.ColumnSizeMode)`

Установка ширины ячейки

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `width`: Новая ширина ячейки
- `mode`: Режим задания ширины ячейки

Remarks: Будет изменена ширина всего столбца, содержащего данную ячейку

### `SetCellsProperties(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.CellProperties)`

ID: `M:TFlex.Model.Model2D.Table.SetCellsProperties(System.UInt32,System.UInt32,TFlex.Model.Model2D.Table.CellProperties)`

Установка параметров прямоугольного фрагмента таблицы

Parameters:
- `cell1`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента
- `cell2`: Порядковый номер ячейки таблицы, которая лежит на концах диагонали прямоугольного фрагмента
- `props`: Новые параметры прямоугольного фрагмента таблицы

Remarks: Курсор будет перемещён в начало левой верхней ячейки таблицы Параметры выделения фрагмента будут потеряны

### `SetCursorPosition(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.SetCursorPosition(System.UInt32,System.UInt32)`

Установка положения курсора

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `character`: Порядковый номер символа относительно начала ячейки

Remarks: Параметры выделения фрагмента будут потеряны

### `SetSelection(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.SetSelection(System.UInt32,System.UInt32)`

Выделение прямоугольного фрагмента таблицы по заданной диагонали

Parameters:
- `cell1`: Порядковый номер ячейки таблицы, которая лежат на концах диагонали выделяемого прямоугольного фрагмента
- `cell2`: Порядковый номер ячейки таблицы, которая лежат на концах диагонали выделяемого прямоугольного фрагмента

### `SplitCell(System.UInt32,System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model2D.Table.SplitCell(System.UInt32,System.UInt32,System.UInt32)`

Разбивка ячейки на строки и столбцы

Parameters:
- `cell`: Порядковый номер ячейки таблицы
- `rows`: Количество строк
- `columns`: Количество столбцов

Remarks: После разбиения курсор будет перемещён в начало левой верхней ячейки (из образовавшихся), в которую так же будет перенесён весь текст разбиваемой ячейки Параметры выделения фрагмента будут потеряны

## Propertys

### `CellCount`

ID: `P:TFlex.Model.Model2D.Table.CellCount`

Количество ячеек

### `ColumnCount`

ID: `P:TFlex.Model.Model2D.Table.ColumnCount`

Количество столбцов. Если в таблице есть разбитые или объединённые ячейки возвращает -1

### `IsRegular`

ID: `P:TFlex.Model.Model2D.Table.IsRegular`

Количество столбцов строк в таблице неизменно. Если в таблице есть разбитые или объединённые ячейки возвращает false

### `Properties`

ID: `P:TFlex.Model.Model2D.Table.Properties`

Параметры таблицы

Remarks: При установке курсор будет перемещён в начало левой верхней ячейки таблицы. Параметры выделения фрагмента будут потеряны

### `RowCount`

ID: `P:TFlex.Model.Model2D.Table.RowCount`

Количество строк. Если в таблице есть разбитые или объединённые ячейки возвращает -1
