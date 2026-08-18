# TFlex.Model.Model3D.Material

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Объект "Материал"

## Constructors

### `Material(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document)`

Конструктор для объекта "Материал"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Material(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document,System.String)`

Создать объект "Материал" из материала библиотеки

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `name`: Имя материала

### `Material(TFlex.Model.Document,TFlex.Model.Model3D.MaterialParameters)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.MaterialParameters)`

Конструктор для объекта "Материал"

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `parameters`: Параметры материала

## Methods

### `Material(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document)`

Конструктор для объекта "Материал"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Material(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document,System.String)`

Создать объект "Материал" из материала библиотеки

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `name`: Имя материала

### `Material(TFlex.Model.Document,TFlex.Model.Model3D.MaterialParameters)`

ID: `M:TFlex.Model.Model3D.Material.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.MaterialParameters)`

Конструктор для объекта "Материал"

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `parameters`: Параметры материала

### `AddToLibrary`

ID: `M:TFlex.Model.Model3D.Material.AddToLibrary`

Добавить объект "Материал" в библиотеку

### `CopyParameters(TFlex.Model.Model3D.MaterialParameters)`

ID: `M:TFlex.Model.Model3D.Material.CopyParameters(TFlex.Model.Model3D.MaterialParameters)`

Копировать свойства материала

Parameters:
- `parameters`: Параметры материала

### `GetFromLibrary(TFlex.Model.Document,System.String)`

ID: `M:TFlex.Model.Model3D.Material.GetFromLibrary(TFlex.Model.Document,System.String)`

Получить объект "Материал" с указанным именем из библиотеки

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `name`: Имя материала

Returns: Материал

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.Material.GroupType`

Получить тип объекта

### `Parameters`

ID: `P:TFlex.Model.Model3D.Material.Parameters`

Получить свойства материала
