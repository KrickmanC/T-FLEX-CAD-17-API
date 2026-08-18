# TFlex.Model.Model3D.ProjectedLinearDimension

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Спроецированный линейный размер

## Methods

### `SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.ProjectedLinearDimension.SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задаёт положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixLeaderNode`: Второй узел привязки, задаёт положение выносной полки
- `dX`: Смещение по горизонтали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)
- `dY`: Смещение по вертикали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model3D.ProjectedLinearDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задаёт положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixNode2`: Второй узел привязки, задаёт положение размерного числа
- `offset2`: Смещение размерного числа относительно середины размерной линии (используется, если fixNode2 не задан)
- `fixNode3`: Третий узел привязки, задаёт положения конца полки размера
- `offset3`: Смещение длины полки размера (используется, если fixNode3 не задан)

## Propertys

### `SubType`

ID: `P:TFlex.Model.Model3D.ProjectedLinearDimension.SubType`

Подтип размера
