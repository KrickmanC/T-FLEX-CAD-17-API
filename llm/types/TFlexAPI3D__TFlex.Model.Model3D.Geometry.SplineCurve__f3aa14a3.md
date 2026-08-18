# TFlex.Model.Model3D.Geometry.SplineCurve

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Геометрический сплайн

## Constructors

### `SplineCurve(TFlex.Model.Model3D.Geometry.PiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.PiecewiseData)`

Создание сплайна по набору сегментов

Parameters:
- `data`: Описание сплайна

### `SplineCurve(TFlex.Model.Model3D.Geometry.SplineData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.SplineData)`

Создание сплайна по набору контрольных точек, весов и последовательности узлов параметризации

Parameters:
- `data`: Описание сплайна

### `SplineCurve(TFlex.Model.Model3D.Geometry.SplinewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.SplinewiseData)`

Создание интерполяционного сплайна по набору точек, через которые проходит сплайн, по параметрам кривой в этих точках и условиям на концах

Parameters:
- `data`: Описание сплайна

## Methods

### `SplineCurve(TFlex.Model.Model3D.Geometry.PiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.PiecewiseData)`

Создание сплайна по набору сегментов

Parameters:
- `data`: Описание сплайна

### `SplineCurve(TFlex.Model.Model3D.Geometry.SplineData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.SplineData)`

Создание сплайна по набору контрольных точек, весов и последовательности узлов параметризации

Parameters:
- `data`: Описание сплайна

### `SplineCurve(TFlex.Model.Model3D.Geometry.SplinewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.#ctor(TFlex.Model.Model3D.Geometry.SplinewiseData)`

Создание интерполяционного сплайна по набору точек, через которые проходит сплайн, по параметрам кривой в этих точках и условиям на концах

Parameters:
- `data`: Описание сплайна

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Описание сплайна по набору сегментов

Parameters:
- `representation`: Требуемое представление сплайна

### `SetPiecewise(TFlex.Model.Model3D.Geometry.PiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineCurve.SetPiecewise(TFlex.Model.Model3D.Geometry.PiecewiseData)`

Установить описание сплайна по набору сегментов

Parameters:
- `data`: Описание сплайна

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.SplineCurve.Data`

Описание сплайна

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.SplineCurve.Splinewise`

Описание интерполяционного сплайна по набору точек, через которые проходит сплайн, по параметрам кривой в этих точках и условиям на концах

Remarks: Не все сплайны могут вернуть это представление
