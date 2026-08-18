# TFlex.Model.Model3D.ApproximatedSplinePath3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс сплайна, построенного по ломаной

## Constructors

### `ApproximatedSplinePath3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.#ctor(TFlex.Model.Document)`

Конструктор для создания сплайна по ломаной

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `ApproximatedSplinePath3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.#ctor(TFlex.Model.Document)`

Конструктор для создания сплайна по ломаной

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `GetKnot(System.Int32)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.GetKnot(System.Int32)`

Получить значение узла параметризации

Parameters:
- `index`: Номер узла

### `GetWeight(System.Int32)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.GetWeight(System.Int32)`

Получить вес точки

Parameters:
- `index`: Номер точки

### `SetKnot(System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.SetKnot(System.Int32,TFlex.Model.Parameter)`

Установить значение узла параметризации

Parameters:
- `index`: Номер узла
- `param`: Значение

Remarks: Значения могут задаваться только для параметризации вручную

### `SetWeight(System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.ApproximatedSplinePath3D.SetWeight(System.Int32,TFlex.Model.Parameter)`

Установить вес точки

Parameters:
- `index`: Номер точки
- `weight`: Вес точки

Remarks: Вес должен быть больше нуля

## Propertys

### `Degree`

ID: `P:TFlex.Model.Model3D.ApproximatedSplinePath3D.Degree`

Степень сплайна

Remarks: Значение степени округляется до ближайшего целого. Степень должна быть больше нуля и меньше числа точек.

### `Parameterization`

ID: `P:TFlex.Model.Model3D.ApproximatedSplinePath3D.Parameterization`

Тип параметризации
