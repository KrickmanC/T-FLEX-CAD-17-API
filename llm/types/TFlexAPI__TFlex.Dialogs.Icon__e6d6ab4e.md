# TFlex.Dialogs.Icon

Assembly: `TFlexAPI`
Namespace: `TFlex.Dialogs`

## Summary

Иконка

## Constructors

### `Icon(System.Drawing.Icon)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.Drawing.Icon)`

Parameters:
- `drawingIcon`: Источник иконки

### `Icon(System.String)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String)`

Parameters:
- `id`: Идентификатор иконки

### `Icon(System.String,System.String)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String,System.String)`

Parameters:
- `id`: Идентификатор иконки
- `path`: Пути к файлу иконки

### `Icon(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String,System.String,System.Boolean)`

Parameters:
- `id`: Идентификатор иконки
- `path`: Пути к файлу иконки
- `cache`: Кэшировать

## Methods

### `Icon(System.Drawing.Icon)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.Drawing.Icon)`

Parameters:
- `drawingIcon`: Источник иконки

### `Icon(System.String)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String)`

Parameters:
- `id`: Идентификатор иконки

### `Icon(System.String,System.String)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String,System.String)`

Parameters:
- `id`: Идентификатор иконки
- `path`: Пути к файлу иконки

### `Icon(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Dialogs.Icon.#ctor(System.String,System.String,System.Boolean)`

Parameters:
- `id`: Идентификатор иконки
- `path`: Пути к файлу иконки
- `cache`: Кэшировать

### `CreateByImagePath(System.String)`

ID: `M:TFlex.Dialogs.Icon.CreateByImagePath(System.String)`

Создать объект Icon по пути к изображению

Parameters:
- `relativeFilePath`: Относительный путь к изображению

### `CreateByImagePath(System.String,System.String)`

ID: `M:TFlex.Dialogs.Icon.CreateByImagePath(System.String,System.String)`

Создать объект Icon по пути к изображению

Parameters:
- `relativeFilePath`: Относительный путь к изображению
- `rootFolderPath`: Пути к файлу изображения

### `CreateByImagePath(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Dialogs.Icon.CreateByImagePath(System.String,System.String,System.Boolean)`

Создать объект Icon по пути к изображению

Parameters:
- `relativeFilePath`: Относительный путь к изображению
- `rootFolderPath`: Пути к файлу изображения
- `cache`: Кэшировать

### `op_Equality(TFlex.Dialogs.Icon,TFlex.Dialogs.Icon)`

ID: `M:TFlex.Dialogs.Icon.op_Equality(TFlex.Dialogs.Icon,TFlex.Dialogs.Icon)`

Сравнить две иконки

### `op_Inequality(TFlex.Dialogs.Icon,TFlex.Dialogs.Icon)`

ID: `M:TFlex.Dialogs.Icon.op_Inequality(TFlex.Dialogs.Icon,TFlex.Dialogs.Icon)`

Сравнить две иконки

## Propertys

### `IsValid`

ID: `P:TFlex.Dialogs.Icon.IsValid`

Возвращает True для непустых иконок
