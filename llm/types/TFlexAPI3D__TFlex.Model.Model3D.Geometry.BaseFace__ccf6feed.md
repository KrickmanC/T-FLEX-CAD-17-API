# TFlex.Model.Model3D.Geometry.BaseFace

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый интерфейс для геометрических и модельных граней

## Methods

### `OutputSurfTrimmed(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseFace.OutputSurfTrimmed(System.Double)`

Возвращает обрезанную поверхность

Parameters:
- `tolerance`: Максимально допустимое расстояние между поверхностью грани и аппроксимирующей сплайновой поверхностью

Remarks: Рекомендуемая точность = 0.00001

## Propertys

### `Edges`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.Edges`

Множество рёбер

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.Loops`

Множество циклов

### `Sense`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.Sense`

Получить признак совпадения ориентации поверхности и грани

### `Surface`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.Surface`

Получить поверхность, на которой лежит грань

### `UVBox`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.UVBox`

Получить UVbox грани

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.BaseFace.Vertices`

Множество вершин
