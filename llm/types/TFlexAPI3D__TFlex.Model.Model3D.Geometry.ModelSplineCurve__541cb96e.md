# TFlex.Model.Model3D.Geometry.ModelSplineCurve

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Сплайн с модели

## Constructors

### `ModelSplineCurve(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineCurve.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной кривой. Модельные кривые не могут создаваться пользователем, так как возвращаются как свойства объектов модели

## Methods

### `ModelSplineCurve(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineCurve.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной кривой. Модельные кривые не могут создаваться пользователем, так как возвращаются как свойства объектов модели

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineCurve.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Получить описание сплайна по набору сегментов

Parameters:
- `representation`: Требуемое представление сплайна

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.ModelSplineCurve.Data`

Получить описание сплайна

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.ModelSplineCurve.Splinewise`

Получить описание интерполяционного сплайна по набору точек, через которые проходит сплайн, по параметрам кривой в этих точках и условиям на концах

Remarks: Не все сплайны могут вернуть это представление
