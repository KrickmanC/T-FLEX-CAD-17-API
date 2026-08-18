# TFlex.Model.Model3D.TransformationGroupBase

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс групп трансформаций

## Methods

### `AddDirectAxisByAxisToDirectionTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelDirection)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddDirectAxisByAxisToDirectionTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelDirection)`

Добавить трансформацию "Повернуть ось вокруг оси по направлению" к группе трансформаций.

Parameters:
- `stationaryAxis`: неподвижная ось
- `rotatingAxis`: направляемая ось
- `direction`: направление для rotatingAxis

### `AddDirectAxisByAxisToPointTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddDirectAxisByAxisToPointTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить трансформацию "Повернуть ось вокруг оси по направлению к точке" к группе трансформаций.

Parameters:
- `stationaryAxis`: неподвижная ось
- `rotatingAxis`: направляемая ось
- `point`: точка, на которую направляется rotatingAxis ось

### `AddDirectAxisToPointTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddDirectAxisToPointTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить трансформацию "Направить ось на точку" к группе трансформаций.

Parameters:
- `axis`: направляемая ось
- `point`: точка, на которую направляется ось

### `AddMap(TFlex.Model.Model3D.Geometry.AffineTransformation)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMap(TFlex.Model.Model3D.Geometry.AffineTransformation)`

Добавить матрицу преобразований к группе трансформаций

### `AddMoveToCurveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelCurve)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMoveToCurveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelCurve)`

Добавить трансформацию "Перемещение до кривой" к группе трансформаций

Parameters:
- `axis`: ось, вдоль которой производится перемещение
- `curve`: кривая, до которой производится перемещение

### `AddMoveToNodeTransf(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMoveToNodeTransf(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить трансформации "Перемещение до точки" к группе трансформаций. Трансформации добавляются для всех осей.

Parameters:
- `point`: точка, до которой производится перемещение

### `AddMoveToNodeTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMoveToNodeTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить трансформацию "Перемещение до точки" к группе трансформаций

Parameters:
- `axis`: ось, вдоль которой производится перемещение
- `point`: точка, до которой производится перемещение

### `AddMoveToSurfaceTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelSurface)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMoveToSurfaceTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelSurface)`

Добавить трансформацию "Перемещение до плоскости" к группе трансформаций

Parameters:
- `axis`: ось, вдоль которой производится перемещение
- `surface`: плоскость, до которой производится перемещение

### `AddMoveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddMoveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

Добавить трансформацию "Перемещение" к группе трансформаций

Parameters:
- `direction`: Ось, по которой производится перемещение
- `offset`: отступ перемещения

### `AddRotateTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddRotateTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

Добавить трансформацию "Вращение" к группе трансформаций

Parameters:
- `direction`: ось, вокруг которой производится вращение
- `angle`: угл вращения

### `AddSetAxisDirectionTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelDirection)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddSetAxisDirectionTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelDirection)`

Добавить трансформацию "Повернуть параллельно направлению" к группе трансформаций.

Parameters:
- `axis`: Поворачиваемая ось
- `direction`: Направление, с которым должна совпасть ось

### `AddSetAxisTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelAxis)`

ID: `M:TFlex.Model.Model3D.TransformationGroupBase.AddSetAxisTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Model3D.Geometry.ModelAxis)`

Добавить трансформацию "Совместить ось полностью" к группе трансформаций.

Parameters:
- `axisType`: Поворачиваемая ось
- `axis`: Ось, с которым должна совпасть поворачиваемая ось

## Propertys

### `IsValid`

ID: `P:TFlex.Model.Model3D.TransformationGroupBase.IsValid`

true - группа трансформаций все еще находится в контейнере трансформаций. false - объект устарел. Использование приведет к исключениям.

### `Name`

ID: `P:TFlex.Model.Model3D.TransformationGroupBase.Name`

Имя группы

### `Suppressed`

ID: `P:TFlex.Model.Model3D.TransformationGroupBase.Suppressed`

Параметр подавления группы трансформаций. Если больше 0 - группа подавлена.

### `TransfContainer`

ID: `P:TFlex.Model.Model3D.TransformationGroupBase.TransfContainer`

Контейнер групп трансформаций, которому принадлежит данная группа
