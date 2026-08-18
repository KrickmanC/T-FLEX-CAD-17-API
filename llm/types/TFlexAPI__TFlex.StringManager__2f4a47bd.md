# TFlex.StringManager

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Менеджер строк для локализации

## Methods

### `GetString(System.String)`

ID: `M:TFlex.StringManager.GetString(System.String)`

Получает строку локализации

Returns: Переведённая строка, либо key если не найдена

### `GetString(System.String,System.Stringref )`

ID: `M:TFlex.StringManager.GetString(System.String,System.String@)`

Получает строку локализации

### `LoadResourceFile(System.String)`

ID: `M:TFlex.StringManager.LoadResourceFile(System.String)`

Загружает строки из файла в формате Microsoft ResX

Parameters:
- `fullPath`: Полный путь к .resx файлу

### `LoadResourceFile(System.String,System.String)`

ID: `M:TFlex.StringManager.LoadResourceFile(System.String,System.String)`

Загружает строки из файла в формате Microsoft ResX

Parameters:
- `baseName`: Название файла локализации
- `path`: Путь к файлу .resx

Remarks: Загружает строки из файла "path/baseName.LC.resx" в формате Microsoft ResX. Здесь LC - двухбуквенное обозначение текущего языка. Если файл с таким именем отсутствует, будет произведена попытка загрузки с именем без обозначения кода языка.

### `SetString(System.String,System.String)`

ID: `M:TFlex.StringManager.SetString(System.String,System.String)`

Установить строку локализации

## Propertys

### `default(System.String)`

ID: `P:TFlex.StringManager.default(System.String)`

Получить или установить строку локализации
