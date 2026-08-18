# TFlex.Model.Model3D.Simplification

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция удаления лишних геометрических элементов упрощения геометрии

## Constructors

### `Simplification(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Simplification.#ctor(TFlex.Model.Document)`

Конструктор для создания операции удаления лишних геометрических элементов упрощения геометрии

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `Simplification(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Simplification.#ctor(TFlex.Model.Document)`

Конструктор для создания операции удаления лишних геометрических элементов упрощения геометрии

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `Check`

ID: `M:TFlex.Model.Model3D.Simplification.Check`

Проверка корректности модели и частичная корректировка

### `EvTopolArrayAfterDeleteAll`

ID: `M:TFlex.Model.Model3D.Simplification.EvTopolArrayAfterDeleteAll`

Обработчики событий при измененении

## Propertys

### `DeleteRedundant`

ID: `P:TFlex.Model.Model3D.Simplification.DeleteRedundant`

Удалять лишние геометрические элементы

### `Faces`

ID: `P:TFlex.Model.Model3D.Simplification.Faces`

Множество граней, для которых выполняется упрощение геометрии

Remarks: Если множество граней пусто, то упрощение геометрии выполняется на всех гранях. Все грани должны относится к одной операции, которая возвращается в свойстве Operation

### `GroupType`

ID: `P:TFlex.Model.Model3D.Simplification.GroupType`

Получить тип объекта

### `Local`

ID: `P:TFlex.Model.Model3D.Simplification.Local`

Упрощять геометрию отдельно для каждого элемента

Remarks: Имеет смысл, если список упрощаемых граней пустой, то есть упрощение геометрии выполняется на всех гранях. Имеет смысл, если включен режим упрощения геометрии.

### `Operation`

ID: `P:TFlex.Model.Model3D.Simplification.Operation`

Операция, для которой выполняется упрощение

### `SimplifyGeometry`

ID: `P:TFlex.Model.Model3D.Simplification.SimplifyGeometry`

Упрощять геометрию

### `Topols`

ID: `P:TFlex.Model.Model3D.Simplification.Topols`

Множество геометрических элементов для удаления

Remarks: Если множество геометрических элементов пусто, то удаление выполняется на всех элементах. Все элементы должны относится к одной операции, которая возвращается в свойстве Operation
