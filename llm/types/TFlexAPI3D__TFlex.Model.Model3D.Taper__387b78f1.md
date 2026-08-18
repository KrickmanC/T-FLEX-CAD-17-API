# TFlex.Model.Model3D.Taper

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Уклон

## Constructors

### `Taper(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Taper.#ctor(TFlex.Model.Document)`

Конструктор для создания Уклона

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `Taper(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Taper.#ctor(TFlex.Model.Document)`

Конструктор для создания Уклона

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddFace(TFlex.Model.Model3D.Geometry.ModelEdge,TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.Taper.AddFace(TFlex.Model.Model3D.Geometry.ModelEdge,TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить пару опорное ребро - уклоняемая грань

Parameters:
- `referenceEdge`: Ребро используемое в качестве опоры для поворота уклоняемой грани
- `draftFace`: Уклоняемая грань

Remarks: Ребро должно принадлежать уклоняемой грани

### `AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.Taper.AddFace(TFlex.Model.Model3D.Geometry.ModelFace,TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить пару опорная грань - уклоняемая грань

Parameters:
- `referenceFace`: Грань используемая в качестве опоры для поворота уклоняемой грани
- `draftFace`: Уклоняемая грань

Remarks: Грани должны иметь общее ребро

### `AddStepEdge(TFlex.Model.Model3D.Geometry.ModelEdge)`

ID: `M:TFlex.Model.Model3D.Taper.AddStepEdge(TFlex.Model.Model3D.Geometry.ModelEdge)`

Добавить ребро задающее шаг

Parameters:
- `edge`: Ребро

Remarks: Рёбра не могут быть добавлены, если задан путь

### `GetStepEdge(System.Int32)`

ID: `M:TFlex.Model.Model3D.Taper.GetStepEdge(System.Int32)`

Получить ребро

Parameters:
- `stepEdgeIndex`: индекс ребра

Returns: Ребро

### `GetStepPath(System.Int32)`

ID: `M:TFlex.Model.Model3D.Taper.GetStepPath(System.Int32)`

Получить путь связанный с уклоняемой гранью

Parameters:
- `faceIndex`: Номер уклоняемой грани

Returns: Путь

### `RemoveAllFaces`

ID: `M:TFlex.Model.Model3D.Taper.RemoveAllFaces`

Удалить все грани

### `RemoveAllStepEdges`

ID: `M:TFlex.Model.Model3D.Taper.RemoveAllStepEdges`

Удалить все рёбра

### `RemoveStepEdge(System.Int32)`

ID: `M:TFlex.Model.Model3D.Taper.RemoveStepEdge(System.Int32)`

Удалить ребро

Parameters:
- `stepEdgeIndex`: Номер ребра

### `SetStepPath(System.Int32,TFlex.Model.Model3D.Path3D)`

ID: `M:TFlex.Model.Model3D.Taper.SetStepPath(System.Int32,TFlex.Model.Model3D.Path3D)`

Задать путь связанный с уклоняемой гранью

Parameters:
- `faceIndex`: Номер уклоняемой грани
- `path`: Путь

Remarks: Путь не может быть задан, если задано ступенчатое ребро

## Propertys

### `AnalyzeFlag`

ID: `P:TFlex.Model.Model3D.Taper.AnalyzeFlag`

Параметр разбиения грани

### `Angle`

ID: `P:TFlex.Model.Model3D.Taper.Angle`

Угол

### `CoprocessingFlag`

ID: `P:TFlex.Model.Model3D.Taper.CoprocessingFlag`

Параметр совместной обработки граней

### `Direction`

ID: `P:TFlex.Model.Model3D.Taper.Direction`

Направление

### `FixedPlane`

ID: `P:TFlex.Model.Model3D.Taper.FixedPlane`

Плоскость

### `GroupType`

ID: `P:TFlex.Model.Model3D.Taper.GroupType`

Получить тип объекта

### `Method`

ID: `P:TFlex.Model.Model3D.Taper.Method`

Метод

### `NumberOfFaces`

ID: `P:TFlex.Model.Model3D.Taper.NumberOfFaces`

Получить число уклоняемых граней

### `NumberOfStepEdges`

ID: `P:TFlex.Model.Model3D.Taper.NumberOfStepEdges`

Получить число рёбер

Returns: Число рёбер

### `OffsetFace`

ID: `P:TFlex.Model.Model3D.Taper.OffsetFace`

Грань смещения

### `ReverseFlag`

ID: `P:TFlex.Model.Model3D.Taper.ReverseFlag`

Реверс угла

### `SmoothFlag`

ID: `P:TFlex.Model.Model3D.Taper.SmoothFlag`

Параметр учёта гладкости

### `StepEdges`

ID: `P:TFlex.Model.Model3D.Taper.StepEdges`

Тип рёбер ступенчатого уклона
