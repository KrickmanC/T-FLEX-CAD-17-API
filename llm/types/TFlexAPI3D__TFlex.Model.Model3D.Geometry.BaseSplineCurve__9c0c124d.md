# TFlex.Model.Model3D.Geometry.BaseSplineCurve

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Интерфейс для свойств сплайна

## Methods

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseSplineCurve.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Получить описание сплайна по набору сегментов

Parameters:
- `representation`: Требуемое представление сплайна

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSplineCurve.Data`

Получить описание сплайна

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.BaseSplineCurve.Splinewise`

Получить описание интерполяционного сплайна по набору точек, через которые проходит сплайн, по параметрам кривой в этих точках и условиям на концах

Remarks: Не все сплайны могут вернуть это представление
