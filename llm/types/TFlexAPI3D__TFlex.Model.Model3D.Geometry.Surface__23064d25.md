# TFlex.Model.Model3D.Geometry.Surface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Геометрическая поверхность

## Constructors

### `Surface`

ID: `M:TFlex.Model.Model3D.Geometry.Surface.#ctor`

Конструктор

## Methods

### `Surface`

ID: `M:TFlex.Model.Model3D.Geometry.Surface.#ctor`

Конструктор

### `CreateSpin(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseAxis,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.BaseInterval)`

ID: `M:TFlex.Model.Model3D.Geometry.Surface.CreateSpin(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseAxis,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.BaseInterval)`

Создать поверхность вращения

Parameters:
- `curve`: Вращаемая кривая
- `axis`: Ось вращения
- `simplify`: Для результирующей поверхности подбирать аналитическое решение
- `confine`: Поверхность вращения создаётся только для части кривой, границы которой задаются интервалом
- `interval`: Параметрический интервал на кривой, если поверхность вращения создаётся только для части кривой

### `CreateSweep(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.Surface.CreateSweep(TFlex.Model.Model3D.Geometry.BaseCurve,TFlex.Model.Model3D.Geometry.BaseDirection)`

Создать поверхность выталкивания

Parameters:
- `curve`: Выталкиваемая кривая
- `direction`: Направление выталкивания
