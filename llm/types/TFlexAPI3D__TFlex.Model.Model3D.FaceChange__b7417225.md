# TFlex.Model.Model3D.FaceChange

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция изменения граней

## Constructors

### `FaceChange(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceChange.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Изменение граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `FaceChange(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceChange.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Изменение граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter,TFlex.Model.Parameter,System.Boolean)`

ID: `M:TFlex.Model.Model3D.FaceChange.AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Parameter,TFlex.Model.Parameter,System.Boolean)`

Задать грань и параметры

### `GetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref ,TFlex.Model.Parameterref ,TFlex.Model.Parameterref ,System.Booleanref )`

ID: `M:TFlex.Model.Model3D.FaceChange.GetFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@,TFlex.Model.Parameter@,TFlex.Model.Parameter@,System.Boolean@)`

Получить грань и параметры

### `RemoveAllFaces`

ID: `M:TFlex.Model.Model3D.FaceChange.RemoveAllFaces`

Удалить все грани

## Propertys

### `CommonParameter1`

ID: `P:TFlex.Model.Model3D.FaceChange.CommonParameter1`

Первый общий параметр (используется для граней с установленным флагом commonParameter)

### `CommonParameter2`

ID: `P:TFlex.Model.Model3D.FaceChange.CommonParameter2`

Второй общий параметр (используется для граней с установленным флагом commonParameter)

### `FaceCount`

ID: `P:TFlex.Model.Model3D.FaceChange.FaceCount`

Получить число граней

### `GroupType`

ID: `P:TFlex.Model.Model3D.FaceChange.GroupType`

Получить тип объекта

### `RelativeParameter`

ID: `P:TFlex.Model.Model3D.FaceChange.RelativeParameter`

Флаг относительного изменения размеров
