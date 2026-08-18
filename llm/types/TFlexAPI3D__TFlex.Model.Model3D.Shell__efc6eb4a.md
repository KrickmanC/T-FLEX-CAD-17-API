# TFlex.Model.Model3D.Shell

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Оболочка

## Constructors

### `Shell(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Shell.#ctor(TFlex.Model.Document)`

Конструктор для создания Оболочки

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `Shell(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Shell.#ctor(TFlex.Model.Document)`

Конструктор для создания Оболочки

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Shell.AddOffsetFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter)`

Добавить грань с особой толщиной

Parameters:
- `face`: Грань
- `offset`: Толщина грани

Remarks: Все грани задаваемые в операции должны быть с одного тела

### `GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref ,TFlex.Model.Parameterref )`

ID: `M:TFlex.Model.Model3D.Shell.GetOffsetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@,TFlex.Model.Parameter@)`

Получить особую грань

Parameters:
- `faceIndex`: Номер грани
- `face`: Грань
- `offset`: Толщина особой грани

### `RemoveAllOffsetFaces`

ID: `M:TFlex.Model.Model3D.Shell.RemoveAllOffsetFaces`

Удалить все особые грани

### `RemoveOffsetFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.Shell.RemoveOffsetFace(System.Int32)`

Удалить особую грань

Parameters:
- `faceIndex`: Номер грани

## Propertys

### `EquidistantBody`

ID: `P:TFlex.Model.Model3D.Shell.EquidistantBody`

Параметр создания эквидистантного тела

### `GroupType`

ID: `P:TFlex.Model.Model3D.Shell.GroupType`

Получить тип объекта

### `Offset`

ID: `P:TFlex.Model.Model3D.Shell.Offset`

Толщина оболочки

### `OffsetFaceCount`

ID: `P:TFlex.Model.Model3D.Shell.OffsetFaceCount`

Число особых граней

### `Outside`

ID: `P:TFlex.Model.Model3D.Shell.Outside`

Параметр построения оболочки наружу

### `PierceSmoothingSurfaces`

ID: `P:TFlex.Model.Model3D.Shell.PierceSmoothingSurfaces`

Пробивать касательные грани

### `StoreSourceBody`

ID: `P:TFlex.Model.Model3D.Shell.StoreSourceBody`

Параметр сохранения исходного тела
