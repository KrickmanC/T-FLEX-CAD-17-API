# TFlex.Model.Model3D.Geometry.BaseSplineSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Интерфейс для свойств сплайновой поверхности

## Methods

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSplineSurface.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Получить описание сплайновой поверхности по набору сегментов

Parameters:
- `representation`: Требуемое представление сплайновой поверхности

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSplineSurface.Data`

Получить описание сплайновой поверхности

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSplineSurface.Splinewise`

Получить описание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Remarks: Не все сплайновые поверхности могут вернуть это представление
