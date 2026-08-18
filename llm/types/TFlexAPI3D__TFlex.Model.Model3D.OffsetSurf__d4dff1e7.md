# TFlex.Model.Model3D.OffsetSurf

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Тело смещения

## Constructors

### `OffsetSurf(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetSurf.#ctor(TFlex.Model.Document)`

Конструктор для создания Тела смещения

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `OffsetSurf(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetSurf.#ctor(TFlex.Model.Document)`

Конструктор для создания Тела смещения

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.OffsetSurf.AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

Добавить грань с особым смещением

Parameters:
- `face`: Грань
- `offset`: Смещение грани

Remarks: Все грани задаваемые в операции должны быть с одного тела

### `GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref ,TFlex.Model.Parameterref )`

ID: `M:TFlex.Model.Model3D.OffsetSurf.GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@,TFlex.Model.Parameter@)`

Получить особую грань

Parameters:
- `faceIndex`: Номер грани
- `face`: Грань
- `offset`: Смещение особой грани

### `RemoveAllOffsetFaces`

ID: `M:TFlex.Model.Model3D.OffsetSurf.RemoveAllOffsetFaces`

Удалить все особые грани

### `RemoveOffsetFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.OffsetSurf.RemoveOffsetFace(System.Int32)`

Удалить особую грань

Parameters:
- `faceIndex`: Номер грани

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.OffsetSurf.GroupType`

Получить тип объекта

### `OffsetFaceCount`

ID: `P:TFlex.Model.Model3D.OffsetSurf.OffsetFaceCount`

Число особых граней

### `Outside`

ID: `P:TFlex.Model.Model3D.OffsetSurf.Outside`

Параметр построения оболочки наружу

### `StoreSourceBody`

ID: `P:TFlex.Model.Model3D.OffsetSurf.StoreSourceBody`

Параметр сохранения исходного тела

### `Value`

ID: `P:TFlex.Model.Model3D.OffsetSurf.Value`

Величина смещения
