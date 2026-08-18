# TFlex.Model.Model3D.Operation.GeometryData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Operation`

## Summary

Множество геометрических данных операции

## Propertys

### `AABoundBox`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.AABoundBox`

Получить параллельный осям ограничивающий прямоугольник

### `Axis`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Axis`

Получить ось

Remarks: Возвращаемая ось зависит от типа операции. Операция Ось Вращение Ось вращения Круговой массив Ось вращения Спираль Ось спирали Пружина Ось пружины

### `BoundBox`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.BoundBox`

Получить bound box

### `Box`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Box`

Получить границы операции

### `ContourLaminar`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.ContourLaminar`

Получить границы листовой операции

### `ContourSheet`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.ContourSheet`

Получить контур листовой операции

### `Curve`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Curve`

Получить кривую, на которой лежит граница листовой операции

Remarks: Для операций, состоящих из нескольких рёбер, кривая может быть не определена

### `Direction`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Direction`

Получить направление

Remarks: Возвращаемое направление зависит от типа операции. Операция Направление Выталкивание Направление выталкивания Вращение Ось вращения Линейный массив Направление копирования Круговой массив Ось вращения Спираль Ось спирали Пружина Ось пружины Уклон Направление уклона

### `Plane`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Plane`

Получить плоскость плоского листового тела

### `Sheet`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Sheet`

Получить тело листовой операции

### `Solid`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Solid`

Получить тело для твердотельной операции

### `Surface`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Surface`

Получить поверхность, на которой лежит листовая операция

Remarks: Для операций, состоящих из нескольких граней, поверхность может быть не определена

### `Wire`

ID: `P:TFlex.Model.Model3D.Operation.GeometryData.Wire`

Получить рёберные границы листовой операции
