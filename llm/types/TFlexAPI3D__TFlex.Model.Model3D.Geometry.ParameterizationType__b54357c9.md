# TFlex.Model.Model3D.Geometry.ParameterizationType

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Тип последовательности узлов

## Fields

### `BezierEnds`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.BezierEnds`

Первый и последний узлы кратности = Степень сплайна + 1. Остальные узлы расположены неравномерно

### `NonUniform`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.NonUniform`

Неравномерная параметризация

### `PiecewiseBezier`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.PiecewiseBezier`

Первый и последний узлы кратности = Степень сплайна + 1, остальные узлы имеют кратность = Степень сплайна, с разбиением на равные промежутки

### `QuasiUniform`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.QuasiUniform`

Первый и последний узлы кратности = Степень сплайна + 1, остальные узлы имеют кратность = 1, с разбиением на равные промежутки

### `SmoothSeam`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.SmoothSeam`

Параметризация для замкнутых периодических сплайнов

### `Uniform`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.Uniform`

Равномерная параметризация

### `Unset`

ID: `F:TFlex.Model.Model3D.Geometry.ParameterizationType.Unset`

Тип последовательности не определён
