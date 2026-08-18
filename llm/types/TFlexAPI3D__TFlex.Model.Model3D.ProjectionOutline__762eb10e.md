# TFlex.Model.Model3D.ProjectionOutline

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс линии изображения, принадлежащей 2D проекции

## Remarks

Линия изображения данного класса может быть создана только при проецировании трёхмерных элементов и не может быть создана приложением

## Methods

### `GetBodyObjectID`

ID: `M:TFlex.Model.Model3D.ProjectionOutline.GetBodyObjectID`

Идентификатор операции, в которой создан элемент

## Propertys

### `ParentObject3D`

ID: `P:TFlex.Model.Model3D.ProjectionOutline.ParentObject3D`

Получение родительского объекта, от которого построена линия

Returns: Родительский объект 3D

### `Projection`

ID: `P:TFlex.Model.Model3D.ProjectionOutline.Projection`

Получение родительского объекта проекции

Returns: Родительский объект (2D проекция)

Remarks: В 2D версии системы данный метод возвращает 0

### `SubType`

ID: `P:TFlex.Model.Model3D.ProjectionOutline.SubType`

Подтип линии изображения
