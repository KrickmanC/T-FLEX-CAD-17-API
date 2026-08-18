# TFlex.Model.Model3D.RelationPoint

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Узел по наименьшему расстоянию между элементами

## Constructors

### `RelationPoint(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.RelationPoint.#ctor(TFlex.Model.Document)`

Конструктор для создания узла по наименьшему расстоянию между элементами

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `RelationPoint(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.RelationPoint.#ctor(TFlex.Model.Document)`

Конструктор для создания узла по наименьшему расстоянию между элементами

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddElement(TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.RelationPoint.AddElement(TFlex.Model.Model3D.Geometry.ModelTopol)`

Добавить элемент

### `AddElement(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.RelationPoint.AddElement(TFlex.Model.Model3D.Object3D)`

Добавить элемент

### `GetElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.RelationPoint.GetElement(System.Int32)`

Получить элемент

### `GetElementCount`

ID: `M:TFlex.Model.Model3D.RelationPoint.GetElementCount`

Получить количество элементов

### `RemoveElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.RelationPoint.RemoveElement(System.Int32)`

Удалить элемент

## Propertys

### `FirstElement`

ID: `P:TFlex.Model.Model3D.RelationPoint.FirstElement`

Первый элемент, на котором ищется ближайшая точка

### `Ratio`

ID: `P:TFlex.Model.Model3D.RelationPoint.Ratio`

Коэффициент

### `SecondElement`

ID: `P:TFlex.Model.Model3D.RelationPoint.SecondElement`

Второй элемент, относительно которого ищется ближайшая точка
