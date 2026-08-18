# TFlex.Model.Model3D.IntersectionPath

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Путь на пересечении

## Constructors

### `IntersectionPath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.#ctor(TFlex.Model.Document)`

Конструктор для создания пути на пересечении

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `IntersectionPath(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.#ctor(TFlex.Model.Document)`

Конструктор для создания пути на пересечении

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `AddSecondElement(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.AddSecondElement(TFlex.Model.Model3D.Object3D)`

Добавить второй элемент

### `CountSecondElements`

ID: `M:TFlex.Model.Model3D.IntersectionPath.CountSecondElements`

Количество вторых элементов

### `GetFirstElement`

ID: `M:TFlex.Model.Model3D.IntersectionPath.GetFirstElement`

Получить первый элемент

### `GetSecondElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.GetSecondElement(System.Int32)`

Получить второй элемент

Parameters:
- `index`: Индекс получаемого элемента (начинается с 0)

### `RemoveFirstElement`

ID: `M:TFlex.Model.Model3D.IntersectionPath.RemoveFirstElement`

Удалить первый элемент

### `RemoveSecondElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.RemoveSecondElement(System.Int32)`

Удалить второй элемент

Parameters:
- `index`: Индекс удаляемого элемента (начинается с 0)

### `SetFirstElement(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.IntersectionPath.SetFirstElement(TFlex.Model.Model3D.Object3D)`

Задать первый элемент

## Propertys

### `AsSurface`

ID: `P:TFlex.Model.Model3D.IntersectionPath.AsSurface`

Как поверхность

### `ExtendPath`

ID: `P:TFlex.Model.Model3D.IntersectionPath.ExtendPath`

Продлевать 3D путь

### `MergeAdjacent`

ID: `P:TFlex.Model.Model3D.IntersectionPath.MergeAdjacent`

Объединять смежные участки

### `SolutionIndex`

ID: `P:TFlex.Model.Model3D.IntersectionPath.SolutionIndex`

Индекс решения
