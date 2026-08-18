# TFlex.Model.ReferenceDatabase

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс для создания базы данных по ссылке(файл)

## Constructors

### `ReferenceDatabase(TFlex.Model.Document,TFlex.Model.FileLink,System.String)`

ID: `M:TFlex.Model.ReferenceDatabase.#ctor(TFlex.Model.Document,TFlex.Model.FileLink,System.String)`

Конструктор для создания базы данных по ссылке(файл)

Parameters:
- `document`: Документ базы данных
- `fileLink`: Ссылка на файл базы данных
- `tableName`: Имя таблицы

## Methods

### `ReferenceDatabase(TFlex.Model.Document,TFlex.Model.FileLink,System.String)`

ID: `M:TFlex.Model.ReferenceDatabase.#ctor(TFlex.Model.Document,TFlex.Model.FileLink,System.String)`

Конструктор для создания базы данных по ссылке(файл)

Parameters:
- `document`: Документ базы данных
- `fileLink`: Ссылка на файл базы данных
- `tableName`: Имя таблицы

### `ConvertToInternal(TFlex.Model.ReferenceDatabase)`

ID: `M:TFlex.Model.ReferenceDatabase.ConvertToInternal(TFlex.Model.ReferenceDatabase)`

Конвертировать базу данных во внутреннюю базу данных

Parameters:
- `sourceDatabase`: База данных по ссылке

Returns: Внутренняя база данных

Remarks: При конвертации исходный объект разрушается

### `GetColumnComment(System.Int32)`

ID: `M:TFlex.Model.ReferenceDatabase.GetColumnComment(System.Int32)`

Получить комментарий столбца

Parameters:
- `index`: Номер столбца

Returns: Комментарий столбца

### `GetColumnCount`

ID: `M:TFlex.Model.ReferenceDatabase.GetColumnCount`

Получить количество столбцов

Returns: Количество столбцов

### `GetColumnName(System.Int32)`

ID: `M:TFlex.Model.ReferenceDatabase.GetColumnName(System.Int32)`

Получить имя столбца

Parameters:
- `index`: Номер столбца

Returns: Имя столбца

### `GetIntValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.ReferenceDatabase.GetIntValue(System.Int32,System.Int32)`

Получить целое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

### `GetRealValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.ReferenceDatabase.GetRealValue(System.Int32,System.Int32)`

Получить вещественное значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

### `GetRecordCount`

ID: `M:TFlex.Model.ReferenceDatabase.GetRecordCount`

Получить количество строк

Returns: Количество строк

### `GetTextValue(System.Int32,System.Int32)`

ID: `M:TFlex.Model.ReferenceDatabase.GetTextValue(System.Int32,System.Int32)`

Получить текстовое значение в таблице

Parameters:
- `column`: Номер столбца
- `row`: Номер строки

## Propertys

### `Delimiter`

ID: `P:TFlex.Model.ReferenceDatabase.Delimiter`

Тип разделителя

### `FileLink`

ID: `P:TFlex.Model.ReferenceDatabase.FileLink`

Путь к файлу базы данных по ссылке

### `SubType`

ID: `P:TFlex.Model.ReferenceDatabase.SubType`

Подтип базы данных

### `TableName`

ID: `P:TFlex.Model.ReferenceDatabase.TableName`

Имя таблицы базы данных по ссылке

### `UpdateMode`

ID: `P:TFlex.Model.ReferenceDatabase.UpdateMode`

Режим обновления

### `UseDosEncoding`

ID: `P:TFlex.Model.ReferenceDatabase.UseDosEncoding`

Кодировка DOS
