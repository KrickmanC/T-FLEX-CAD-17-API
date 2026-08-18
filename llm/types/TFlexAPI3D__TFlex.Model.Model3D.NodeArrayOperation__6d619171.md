# TFlex.Model.Model3D.NodeArrayOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс операции "Массив по точкам"

## Constructors

### `NodeArrayOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.#ctor(TFlex.Model.Document)`

Конструктор для операции "Массив по точкам"

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

Remarks: Тип копируемых объектов изначально не определён и определяется автоматически (как операции или элементы построения), при добавлении объектов

### `NodeArrayOperation(TFlex.Model.Document,TFlex.Model.Model3D.ArrayOperation.Type)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.ArrayOperation.Type)`

Конструктор для операции "Массив по точкам"

Parameters:
- `Doc`: Документ, в котором создаётся новый объект
- `type`: Тип копируемых элементов

## Methods

### `NodeArrayOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.#ctor(TFlex.Model.Document)`

Конструктор для операции "Массив по точкам"

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

Remarks: Тип копируемых объектов изначально не определён и определяется автоматически (как операции или элементы построения), при добавлении объектов

### `NodeArrayOperation(TFlex.Model.Document,TFlex.Model.Model3D.ArrayOperation.Type)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.#ctor(TFlex.Model.Document,TFlex.Model.Model3D.ArrayOperation.Type)`

Конструктор для операции "Массив по точкам"

Parameters:
- `Doc`: Документ, в котором создаётся новый объект
- `type`: Тип копируемых элементов

### `AddTargetPoint(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.AddTargetPoint(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить целевую точку для построения массива

Parameters:
- `Point`: Целевая точка, которую необходимо добавить

### `GetTargetPoint(System.Int32)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.GetTargetPoint(System.Int32)`

Получить целевую точку массива по номеру

Parameters:
- `Index`: Номер целевой точки

Remarks: Целевые точки нумеруются с нуля. Если индекс отрицательный или превышает количество целевых точек, то результат не определён

### `RemoveTargetPoint(System.Int32)`

ID: `M:TFlex.Model.Model3D.NodeArrayOperation.RemoveTargetPoint(System.Int32)`

Удалить целевую точку по индексу

Parameters:
- `Index`: Номер целевой точки, которую необходимо удалить

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.NodeArrayOperation.GroupType`

Получить тип объекта

### `SourcePoint`

ID: `P:TFlex.Model.Model3D.NodeArrayOperation.SourcePoint`

Исходная точка

### `TargetPointCount`

ID: `P:TFlex.Model.Model3D.NodeArrayOperation.TargetPointCount`

Получить количество целевых точек массива

### `TargetPoints`

ID: `P:TFlex.Model.Model3D.NodeArrayOperation.TargetPoints`

Получить перечисление базовых элементов для построения массива
