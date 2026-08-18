# TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.FaceTransform`

## Summary

Контейнер хранения преобразований для граней

## Methods

### `AddMoveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer.AddMoveTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

Добавить трансформацию "Перемещение"

Parameters:
- `direction`: ось, по которой производится перемещение
- `offset`: отступ перемещения

### `AddRotateTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer.AddRotateTransf(TFlex.Model.Model3D.TransformationCoordinate,TFlex.Model.Parameter)`

Добавить трансформацию "Вращение"

Parameters:
- `direction`: ось, вокруг которой производится вращение
- `angle`: arc of rotation

### `RemoveAllTransf`

ID: `M:TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer.RemoveAllTransf`

Удалить все преобразования

## Propertys

### `CoordinatSystem`

ID: `P:TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer.CoordinatSystem`

Система координат

### `Type`

ID: `P:TFlex.Model.Model3D.FaceTransform.FacesTransformationsContainer.Type`

Тип исходной системы координат преобразования
