# TFlex.Model.Model3D.Offset

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Тело смещения

## Constructors

### `Offset(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Offset.#ctor(TFlex.Model.Document)`

Конструктор для создания Тела смещения

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `Offset(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Offset.#ctor(TFlex.Model.Document)`

Конструктор для создания Тела смещения

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Offset.AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

Добавить грань с особым смещением

Parameters:
- `face`: Грань
- `offset`: Смещение грани

Remarks: Все грани задаваемые в операции должны быть с одного тела

### `GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref ,TFlex.Model.Parameterref )`

ID: `M:TFlex.Model.Model3D.Offset.GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@,TFlex.Model.Parameter@)`

Получить особую грань

Parameters:
- `faceIndex`: Номер грани
- `face`: Грань
- `offset`: Смещение особой грани

### `RemoveAllOffsetFaces`

ID: `M:TFlex.Model.Model3D.Offset.RemoveAllOffsetFaces`

Удалить все особые грани

### `RemoveOffsetFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.Offset.RemoveOffsetFace(System.Int32)`

Удалить особую грань

Parameters:
- `faceIndex`: Номер грани

## Propertys

### `GroupType`

ID: `P:TFlex.Model.Model3D.Offset.GroupType`

Получить тип объекта

### `OffsetFaceCount`

ID: `P:TFlex.Model.Model3D.Offset.OffsetFaceCount`

Число особых граней

### `Outside`

ID: `P:TFlex.Model.Model3D.Offset.Outside`

Параметр построения оболочки наружу

### `StoreSourceBody`

ID: `P:TFlex.Model.Model3D.Offset.StoreSourceBody`

Параметр сохранения исходного тела

### `Value`

ID: `P:TFlex.Model.Model3D.Offset.Value`

Величина смещения
