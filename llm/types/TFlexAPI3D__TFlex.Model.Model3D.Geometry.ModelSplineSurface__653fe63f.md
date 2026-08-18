# TFlex.Model.Model3D.Geometry.ModelSplineSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Сплайновая поверхность с модели

## Constructors

### `ModelSplineSurface(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineSurface.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной поверхности. Модельные поверхности не могут создаваться пользователем, так как возвращаются как свойства объектов модели

## Methods

### `ModelSplineSurface(TFlex.Model.Model3D.Object3D,System.IntPtr)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineSurface.#ctor(TFlex.Model.Model3D.Object3D,System.IntPtr)`

Конструкторы для модельной поверхности. Модельные поверхности не могут создаваться пользователем, так как возвращаются как свойства объектов модели

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.ModelSplineSurface.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Получить описание сплайновой поверхности по набору сегментов

Parameters:
- `representation`: Требуемое представление сплайновой поверхности

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.ModelSplineSurface.Data`

Получить описание сплайновой поверхности

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.ModelSplineSurface.Splinewise`

Получить описание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Remarks: Не все сплайновые поверхности могут вернуть это представление
