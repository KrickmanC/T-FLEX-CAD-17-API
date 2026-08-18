# TFlex.Model.Model3D.FaceReplace

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция замены граней

## Constructors

### `FaceReplace(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceReplace.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Трансформация граней"

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `FaceReplace(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceReplace.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Трансформация граней"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Geometry.ModelSurface,System.Boolean)`

ID: `M:TFlex.Model.Model3D.FaceReplace.AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Geometry.ModelSurface,System.Boolean)`

Задать пару "заменяемая грань-заменяющая поверхность"

Remarks: surface должно быть равно 0 если задано листовое тело

### `GetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref ,TFlex.Model.Model3D.Geometry.ModelSurfaceref ,System.Booleanref )`

ID: `M:TFlex.Model.Model3D.FaceReplace.GetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@,TFlex.Model.Model3D.Geometry.ModelSurface@,System.Boolean@)`

Получить пару "заменяемая грань-заменяющая поверхность"

### `RemoveAllFaces`

ID: `M:TFlex.Model.Model3D.FaceReplace.RemoveAllFaces`

Удалить все пары "заменяемая грань-заменяющая поверхность"

## Propertys

### `FaceCount`

ID: `P:TFlex.Model.Model3D.FaceReplace.FaceCount`

Число пар "заменяемая грань-заменяющая поверхность"

### `GroupType`

ID: `P:TFlex.Model.Model3D.FaceReplace.GroupType`

Получить тип объекта

### `Sheet`

ID: `P:TFlex.Model.Model3D.FaceReplace.Sheet`

Заменяющее листовое тело. Заданные грани заменяются гранями листового тела.
