# TFlex.Model.Model3D.Geometry.SplineSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Геометрическая сплайновая поверхность

## Constructors

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

Создание сплайновой поверхности по набору сегментов

Parameters:
- `data`: Описание сплайновой поверхности

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfaceSplineData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfaceSplineData)`

Создание сплайновой поверхности по набору контрольных точек, весов и последовательности узлов параметризации

Parameters:
- `data`: Описание сплайновой поверхности

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData)`

Создание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Parameters:
- `data`: Описание сплайновой поверхности

## Methods

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

Создание сплайновой поверхности по набору сегментов

Parameters:
- `data`: Описание сплайновой поверхности

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfaceSplineData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfaceSplineData)`

Создание сплайновой поверхности по набору контрольных точек, весов и последовательности узлов параметризации

Parameters:
- `data`: Описание сплайновой поверхности

### `SplineSurface(TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.#ctor(TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData)`

Создание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Parameters:
- `data`: Описание сплайновой поверхности

### `Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.Piecewise(TFlex.Model.Model3D.Geometry.PiecewiseRepresentation)`

Получить описание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Remarks: Не все сплайновые поверхности могут вернуть это представление

### `SetPiecewise(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineSurface.SetPiecewise(TFlex.Model.Model3D.Geometry.SurfacePiecewiseData)`

Установить описание сплайновой поверхности по набору сегментов

## Propertys

### `Data`

ID: `P:TFlex.Model.Model3D.Geometry.SplineSurface.Data`

Описание сплайновой поверхности

### `Splinewise`

ID: `P:TFlex.Model.Model3D.Geometry.SplineSurface.Splinewise`

Получить описание интерполяционной сплайновой поверхности по набору точек, через которые проходит сплайновая поверхность, по параметрам поверхности в этих точках и условиям на концах

Remarks: Не все сплайновые поверхности могут вернуть это представление
