# TFlex.Model.Model3D.ThreeFaceBlending

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Сглаживание 3-х граней

## Constructors

### `ThreeFaceBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания объекта ThreeFaceBlending

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `ThreeFaceBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания объекта ThreeFaceBlending

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddCenterFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.AddCenterFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить центральную грань

Parameters:
- `face`: Грань

### `AddLeftFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.AddLeftFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить левую грань

Parameters:
- `face`: Грань

### `AddRightFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.AddRightFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить правой грань

Parameters:
- `face`: Грань

### `GetCenterFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.GetCenterFace(System.Int32)`

Получить центральную грань

Parameters:
- `faceIndex`: Номер грани

Returns: Грань

### `GetLeftFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.GetLeftFace(System.Int32)`

Получить левую грань

Parameters:
- `faceIndex`: Номер грани

Returns: Грань

### `GetRightFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.GetRightFace(System.Int32)`

Получить правую грань

Parameters:
- `faceIndex`: Номер грани

Returns: Грань

### `RemoveAllCenterFaces`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveAllCenterFaces`

Удалить все центральные грани

### `RemoveAllLeftFaces`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveAllLeftFaces`

Удалить все левые грани

### `RemoveAllRightFaces`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveAllRightFaces`

Удалить все правые грани

### `RemoveCenterFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveCenterFace(System.Int32)`

Удалить центральную грань

Parameters:
- `faceIndex`: Номер грани

### `RemoveLeftFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveLeftFace(System.Int32)`

Удалить левую грань

Parameters:
- `faceIndex`: Номер грани

### `RemoveRightFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreeFaceBlending.RemoveRightFace(System.Int32)`

Удалить правую грань

Parameters:
- `faceIndex`: Номер грани

## Propertys

### `CenterFaceReverse`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.CenterFaceReverse`

Тип реверса для центральных граней

### `GroupType`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.GroupType`

Получить тип объекта

### `LeftFaceReverse`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.LeftFaceReverse`

Тип реверса для левых граней

### `NumberOfCenterFaces`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.NumberOfCenterFaces`

Получить число центральных граней

### `NumberOfLeftFaces`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.NumberOfLeftFaces`

Число левых граней

### `NumberOfRightFaces`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.NumberOfRightFaces`

Число правых граней

### `Path`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.Path`

Путь

### `PropagateFlag`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.PropagateFlag`

Параметр "продолжить по касательной"

### `RightFaceReverse`

ID: `P:TFlex.Model.Model3D.ThreeFaceBlending.RightFaceReverse`

Тип реверса для правых граней
