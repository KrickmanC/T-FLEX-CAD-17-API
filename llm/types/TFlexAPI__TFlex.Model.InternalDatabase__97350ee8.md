# TFlex.Model.InternalDatabase

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Внутренняя база данных

## Constructors

### `InternalDatabase(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.InternalDatabase.#ctor(TFlex.Model.Document,System.String)`

Конструктор

Parameters:
- `document`: Документ базы данных
- `name`: Имя базы данных

## Methods

### `InternalDatabase(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.InternalDatabase.#ctor(TFlex.Model.Document,System.String)`

Конструктор

Parameters:
- `document`: Документ базы данных
- `name`: Имя базы данных

### `AppendRow`

ID: `M:TFlex.Model.InternalDatabase.AppendRow`

Добавить строку

### `DeleteColumn(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.DeleteColumn(System.Int32)`

Удалить столбец

Parameters:
- `index`: Номер столбца

### `DeleteContents`

ID: `M:TFlex.Model.InternalDatabase.DeleteContents`

Удалить все строки

### `DeleteRow(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.DeleteRow(System.Int32)`

Удалить строку

Parameters:
- `index`: Номер строки

### `GetColumnComment(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetColumnComment(System.Int32)`

Получить комментарий столбца

Parameters:
- `index`: Номер столбца

Returns: Комментарий столбца

### `GetColumnCount`

ID: `M:TFlex.Model.InternalDatabase.GetColumnCount`

Получить количество столбцов

Returns: Количество столбцов

### `GetColumnName(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetColumnName(System.Int32)`

Получить имя столбца

Parameters:
- `index`: Номер столбца

Returns: Имя столбца

### `GetColumnOrder`

ID: `M:TFlex.Model.InternalDatabase.GetColumnOrder`

Получить упорядоченные индексы столбцов

### `GetColumnType(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetColumnType(System.Int32)`

Получить тип столбца

Parameters:
- `index`: Номер столбца

Returns: Тип столбца

### `GetIntValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetIntValue(System.Int32,System.Int32)`

Получить целое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

### `GetRealValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetRealValue(System.Int32,System.Int32)`

Получить вещественное значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

### `GetRecordCount`

ID: `M:TFlex.Model.InternalDatabase.GetRecordCount`

Получить количество строк

Returns: Количество строк

### `GetTextValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.GetTextValue(System.Int32,System.Int32)`

Получить текстовое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

### `InsertColumn(System.Int32,TFlex.Model.DatabaseColumnType,System.String)`

ID: `M:TFlex.Model.InternalDatabase.InsertColumn(System.Int32,TFlex.Model.DatabaseColumnType,System.String)`

Вставить столбец

Parameters:
- `index`: Номер столбца
- `type`: Тип столбца базы данных
- `name`: Название столбца

### `InsertRow(System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.InsertRow(System.Int32)`

Вставить строку

Parameters:
- `index`: Номер строки

### `InsertTextColumn(System.Int32,System.String,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.InsertTextColumn(System.Int32,System.String,System.Int32)`

Вставить текстовый столбец с указанием длины текста

Parameters:
- `index`: Номер столбца
- `name`: Название столбца
- `length`: Количество символов

### `SetColumnName(System.Int32,System.String)`

ID: `M:TFlex.Model.InternalDatabase.SetColumnName(System.Int32,System.String)`

Установить имя столбца

Parameters:
- `column`: Номер столбца
- `name`: Имя столбца

### `SetIntValue(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.SetIntValue(System.Int32,System.Int32,System.Int32)`

Установить целое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки
- `value`: Целое значение

### `SetRealValue(System.Int32,System.Int32,System.Double)`

ID: `M:TFlex.Model.InternalDatabase.SetRealValue(System.Int32,System.Int32,System.Double)`

Установить вещественное значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки
- `value`: Вещественное значение

### `SetRealValueFormat(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.SetRealValueFormat(System.Int32,System.Int32,System.Int32)`

Установить формат вещественного значения

Parameters:
- `column`: Номер столбца
- `total`: Общая длина
- `decimal`: После запятой

### `SetTextValue(System.Int32,System.Int32,System.String)`

ID: `M:TFlex.Model.InternalDatabase.SetTextValue(System.Int32,System.Int32,System.String)`

Установить текстовое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки
- `value`: Текстовое значение

### `SetTextValueLength(System.Int32,System.Int32)`

ID: `M:TFlex.Model.InternalDatabase.SetTextValueLength(System.Int32,System.Int32)`

Установить длину текстового значения

Parameters:
- `column`: Номер столбца
- `length`: Количество символов

## Propertys

### `SubType`

ID: `P:TFlex.Model.InternalDatabase.SubType`

Подтип базы данных
