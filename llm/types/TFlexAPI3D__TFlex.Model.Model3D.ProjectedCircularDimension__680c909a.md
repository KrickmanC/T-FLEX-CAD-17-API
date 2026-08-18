# TFlex.Model.Model3D.ProjectedCircularDimension

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Спроецированный размер на окружности

## Methods

### `SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

ID: `M:TFlex.Model.Model3D.ProjectedCircularDimension.SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

Установка размера, как диаметрального

Parameters:
- `type`: Тип отрисовки диаметрального размера

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.ProjectedCircularDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка положения размера на окружности

Parameters:
- `fixNode`: Узел привязки размерной стрелки
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixNode)
- `offset`: Расстояние от размерного числа до окружности (используется, если отсутствует fixNode)

### `SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

ID: `M:TFlex.Model.Model3D.ProjectedCircularDimension.SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

Установка размера, как радиального

Parameters:
- `type`: Тип отрисовки радиального размера

## Propertys

### `SubType`

ID: `P:TFlex.Model.Model3D.ProjectedCircularDimension.SubType`

Подтип размера
