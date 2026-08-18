# TFlex.Model.Model3D.MaterialLibrary

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс библиотеки материалов

## Constructors

### `MaterialLibrary`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.#ctor`

Конструктор по умолчанию

### `MaterialLibrary(System.String)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.#ctor(System.String)`

Конструктор с именем файла

Parameters:
- `FileName`: Имя файла

## Methods

### `MaterialLibrary`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.#ctor`

Конструктор по умолчанию

### `MaterialLibrary(System.String)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.#ctor(System.String)`

Конструктор с именем файла

Parameters:
- `FileName`: Имя файла

### `AddMaterial(TFlex.Model.Model3D.MaterialParameters)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.AddMaterial(TFlex.Model.Model3D.MaterialParameters)`

Добавить материал в библиотеку

Parameters:
- `Parameters`: Параметры материала

### `Dispose`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `GetAllOpenedLibraries`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.GetAllOpenedLibraries`

Получить открытые библиотеки

Returns: Библиотеки материалов

### `GetMaterial(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.GetMaterial(System.Int32)`

Получить параметры материала по индексу

Parameters:
- `Index`: Индекс материала

### `GetOpenedLibraries`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.GetOpenedLibraries`

Получить открытые библиотеки

Returns: Библиотеки материалов

### `Load(System.String)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.Load(System.String)`

Загрузить библиотеку материалов

Parameters:
- `FileName`: Имя файла

### `RemoveMaterial(System.Int32)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.RemoveMaterial(System.Int32)`

Удалить материал из библиотеки

Parameters:
- `Index`: Индекс материала

### `Save(System.String)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.Save(System.String)`

Сохранить библиотеку материалов

Parameters:
- `FileName`: Имя файла

### `TryAddLibrary(System.String)`

ID: `M:TFlex.Model.Model3D.MaterialLibrary.TryAddLibrary(System.String)`

Открыть библиотеку. Библиотеку будет добавлена в список открытых.

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.MaterialLibrary.Count`

Получить количество материалов в библиотеке

### `Default`

ID: `P:TFlex.Model.Model3D.MaterialLibrary.Default`

Библиотека материалов по умолчанию

### `FileName`

ID: `P:TFlex.Model.Model3D.MaterialLibrary.FileName`

Имя файла библиотеки материалов

### `PathName`

ID: `P:TFlex.Model.Model3D.MaterialLibrary.PathName`

Путь библиотеки материалов
