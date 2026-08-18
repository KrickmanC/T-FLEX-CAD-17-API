# TFlex.Model.FileLink

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс ссылки на файл

## Constructors

### `FileLink(TFlex.Model.BackFileLinkParameters)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.BackFileLinkParameters)`

Конструктор обратной ссылки

Parameters:
- `parameters`: Параметры конструктора

### `FileLink(TFlex.Model.Document)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document)`

Конструктор пустой ссылки на файл

Parameters:
- `document`: Документ ссылки

### `FileLink(TFlex.Model.Document,System.IntPtr)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.IntPtr)`

Конструктор ссылки на файл по внутреннему идентификатору

Parameters:
- `document`: Документ ссылки
- `internalID`: Внутренней идентификатор

### `FileLink(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String)`

Конструктор ссылки на файл по пути

Parameters:
- `document`: Документ ссылки
- `filePath`: Путь к ссылке

### `FileLink(TFlex.Model.Document,System.String,System.Boolean)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String,System.Boolean)`

Конструктор ссылки на внутренний файл по пути

Parameters:
- `document`: Документ ссылки
- `filePath`: Путь к ссылке
- `embedded`: true, если файл вложенный

### `FileLink(TFlex.Model.Document,System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String,TFlex.Model.Document)`

Конструктор ссылки на внутренний файл по документу в памяти

Parameters:
- `document`: Документ, в котором будет создана ссылка
- `nameFormat`: Имя ссылки
- `fragment`: Внутренний документ, на который указывает ссылка

### `FileLink(TFlex.Model.Document,TFlex.Model.FileLink)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,TFlex.Model.FileLink)`

Конструктор копии ссылки на файл

Parameters:
- `document`: Документ ссылки
- `link`: Ссылка на файл

### `FileLink(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.FileLink)`

Конструктор копии ссылки на файл

Parameters:
- `link`: Ссылка на файл

### `FileLink(TFlex.Model.TempFileLinkParameters)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.TempFileLinkParameters)`

Конструктор ссылки на временный файл

Parameters:
- `parameters`: Параметры конструктора

## Methods

### `FileLink(TFlex.Model.BackFileLinkParameters)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.BackFileLinkParameters)`

Конструктор обратной ссылки

Parameters:
- `parameters`: Параметры конструктора

### `FileLink(TFlex.Model.Document)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document)`

Конструктор пустой ссылки на файл

Parameters:
- `document`: Документ ссылки

### `FileLink(TFlex.Model.Document,System.IntPtr)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.IntPtr)`

Конструктор ссылки на файл по внутреннему идентификатору

Parameters:
- `document`: Документ ссылки
- `internalID`: Внутренней идентификатор

### `FileLink(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String)`

Конструктор ссылки на файл по пути

Parameters:
- `document`: Документ ссылки
- `filePath`: Путь к ссылке

### `FileLink(TFlex.Model.Document,System.String,System.Boolean)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String,System.Boolean)`

Конструктор ссылки на внутренний файл по пути

Parameters:
- `document`: Документ ссылки
- `filePath`: Путь к ссылке
- `embedded`: true, если файл вложенный

### `FileLink(TFlex.Model.Document,System.String,TFlex.Model.Document)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,System.String,TFlex.Model.Document)`

Конструктор ссылки на внутренний файл по документу в памяти

Parameters:
- `document`: Документ, в котором будет создана ссылка
- `nameFormat`: Имя ссылки
- `fragment`: Внутренний документ, на который указывает ссылка

### `FileLink(TFlex.Model.Document,TFlex.Model.FileLink)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.Document,TFlex.Model.FileLink)`

Конструктор копии ссылки на файл

Parameters:
- `document`: Документ ссылки
- `link`: Ссылка на файл

### `FileLink(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.FileLink)`

Конструктор копии ссылки на файл

Parameters:
- `link`: Ссылка на файл

### `FileLink(TFlex.Model.TempFileLinkParameters)`

ID: `M:TFlex.Model.FileLink.#ctor(TFlex.Model.TempFileLinkParameters)`

Конструктор ссылки на временный файл

Parameters:
- `parameters`: Параметры конструктора

### `Dispose`

ID: `M:TFlex.Model.FileLink.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `MakeEmbedded`

ID: `M:TFlex.Model.FileLink.MakeEmbedded`

Преобразовать ссылку во вложенную. Будут преобразованы все ссылки в документе на данный файл.

### `MakeExternal(System.String)`

ID: `M:TFlex.Model.FileLink.MakeExternal(System.String)`

Преобразовать ссылку во внешнюю. Будут преобразованы все ссылки в документе на данный файл.

## Propertys

### `Document`

ID: `P:TFlex.Model.FileLink.Document`

Документ объекта

### `FilePath`

ID: `P:TFlex.Model.FileLink.FilePath`

Путь файла

### `FullFilePath`

ID: `P:TFlex.Model.FileLink.FullFilePath`

Полный путь файла

### `InternalID`

ID: `P:TFlex.Model.FileLink.InternalID`

Внутренний идентификатор

### `IsDisposed`

ID: `P:TFlex.Model.FileLink.IsDisposed`

Возвращает true, если вызывался Dispose()

### `IsEmbedded`

ID: `P:TFlex.Model.FileLink.IsEmbedded`

Возвращает true, если ссылка внутренняя

### `IsEmpty`

ID: `P:TFlex.Model.FileLink.IsEmpty`

Возвращает true, если ссылка пустая

### `IsOriginalFormat`

ID: `P:TFlex.Model.FileLink.IsOriginalFormat`

Возвращает true, если ссылка на документ T-FLEX CAD
