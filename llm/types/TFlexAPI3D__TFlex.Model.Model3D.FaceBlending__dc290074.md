# TFlex.Model.Model3D.FaceBlending

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Сглаживание граней

## Constructors

### `FaceBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания операции "Сглаживание граней"

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `FaceBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания операции "Сглаживание граней"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddConstraintEdge(TFlex.Model.Model3D.Geometry.ModelEdge,TFlex.Model.Model3D.FaceBlending.ConstraintEdgeType)`

ID: `M:TFlex.Model.Model3D.FaceBlending.AddConstraintEdge(TFlex.Model.Model3D.Geometry.ModelEdge,TFlex.Model.Model3D.FaceBlending.ConstraintEdgeType)`

Добавить ограничивающее ребро

Parameters:
- `edge`: Ребро
- `type`: Тип ограничения

### `AddLeftFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.FaceBlending.AddLeftFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить грань в левую стенку

Parameters:
- `face`: Грань

Remarks: Все левые грани должны образовывать G1-непрерывную поверхность. Все левые грани должны принадлежать одному телу.

### `AddRightFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.FaceBlending.AddRightFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить грань в правую стенку

Parameters:
- `face`: Грань

Remarks: Все правые грани должны образовывать G1-непрерывную поверхность. Все правые грани должны принадлежать одному телу.

### `GetLeftFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.GetLeftFace(System.Int32)`

Полуить левую грань

Parameters:
- `faceIndex`: Номер грани

Returns: Грань

### `GetRightFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.GetRightFace(System.Int32)`

Полуить правую грань

Parameters:
- `faceIndex`: Номер грани

Returns: Грань

### `RemoveAllConstraintEdges`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveAllConstraintEdges`

Удалить все ограничивающие рёбра

### `RemoveAllLeftFaces`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveAllLeftFaces`

Удалить грани образующие левую стенку

### `RemoveAllRightFaces`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveAllRightFaces`

Удалить грани образующие правую стенку

### `RemoveConstraintEdge(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveConstraintEdge(System.Int32)`

Удалить ограничивающее ребро

Parameters:
- `edgeIndex`: Номер ребра

### `RemoveLeftFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveLeftFace(System.Int32)`

Удалить левую грань

Parameters:
- `faceIndex`: Номер грани

### `RemoveRightFace(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.RemoveRightFace(System.Int32)`

Удалить правую грань

Parameters:
- `faceIndex`: Номер грани

## Propertys

### `Attribute`

ID: `P:TFlex.Model.Model3D.FaceBlending.Attribute`

Атрибут сглаживания

### `BlendTrim`

ID: `P:TFlex.Model.Model3D.FaceBlending.BlendTrim`

Тип торца

Parameters:
- `trimType`: Тип

### `BlendWalls`

ID: `P:TFlex.Model.Model3D.FaceBlending.BlendWalls`

Тип результата

### `ConstraintLimit1`

ID: `P:TFlex.Model.Model3D.FaceBlending.ConstraintLimit1`

Первая ограничивающая плоскость

### `ConstraintLimit2`

ID: `P:TFlex.Model.Model3D.FaceBlending.ConstraintLimit2`

Вторая ограничивающая плоскость

### `CrossSectionPlaneMethod`

ID: `P:TFlex.Model.Model3D.FaceBlending.CrossSectionPlaneMethod`

Тип плоскости пересечения секций

### `GroupType`

ID: `P:TFlex.Model.Model3D.FaceBlending.GroupType`

Получить тип объекта

### `HelpPoint`

ID: `P:TFlex.Model.Model3D.FaceBlending.HelpPoint`

Вспомогательная точка

### `LeftSense`

ID: `P:TFlex.Model.Model3D.FaceBlending.LeftSense`

Реверс левой стенки

### `NotchFlag`

ID: `P:TFlex.Model.Model3D.FaceBlending.NotchFlag`

Параметр "Вырез"

### `NumberOfConstraintEdges`

ID: `P:TFlex.Model.Model3D.FaceBlending.NumberOfConstraintEdges`

Получить число ограничивающих рёбер

Returns: Число ограничивающих рёбер

### `NumberOfLeftFaces`

ID: `P:TFlex.Model.Model3D.FaceBlending.NumberOfLeftFaces`

Получить число граней образующих левую стенку

### `NumberOfRightFaces`

ID: `P:TFlex.Model.Model3D.FaceBlending.NumberOfRightFaces`

Получить число граней образующих правую стенку

### `PropagateFlag`

ID: `P:TFlex.Model.Model3D.FaceBlending.PropagateFlag`

Параметр "Продолжить по касательной"

### `RightSense`

ID: `P:TFlex.Model.Model3D.FaceBlending.RightSense`

Реверс правой стенки

### `Spine`

ID: `P:TFlex.Model.Model3D.FaceBlending.Spine`

Путь

### `UseHelpPoint`

ID: `P:TFlex.Model.Model3D.FaceBlending.UseHelpPoint`

Параметр использования вспомогательной точки
