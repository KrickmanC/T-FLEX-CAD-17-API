# TFlex.Model.Model3D.BodyTaper

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция уклона тела

## Constructors

### `BodyTaper(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.BodyTaper.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Изменение граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `BodyTaper(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.BodyTaper.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Изменение граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddBottomEdge(TFlex.Model.Model3D.Geometry.ModelEdge,System.Boolean,System.Boolean,TFlex.Model.Model3D.BodyTaper.MethodType)`

ID: `M:TFlex.Model.Model3D.BodyTaper.AddBottomEdge(TFlex.Model.Model3D.Geometry.ModelEdge,System.Boolean,System.Boolean,TFlex.Model.Model3D.BodyTaper.MethodType)`

Добавить нижнее ребро

### `AddBottomFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.BodyTaper.AddBottomFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить нижнюю грань

### `AddTopEdge(TFlex.Model.Model3D.Geometry.ModelEdge,System.Boolean,System.Boolean,TFlex.Model.Model3D.BodyTaper.MethodType)`

ID: `M:TFlex.Model.Model3D.BodyTaper.AddTopEdge(TFlex.Model.Model3D.Geometry.ModelEdge,System.Boolean,System.Boolean,TFlex.Model.Model3D.BodyTaper.MethodType)`

Добавить верхнее ребро

### `AddTopFace(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.BodyTaper.AddTopFace(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить верхнюю грань

### `GetBottomEdge(System.Int32,TFlex.Model.Model3D.Geometry.ModelEdgeref ,System.Booleanref ,System.Booleanref ,TFlex.Model.Model3D.BodyTaper.MethodTyperef )`

ID: `M:TFlex.Model.Model3D.BodyTaper.GetBottomEdge(System.Int32,TFlex.Model.Model3D.Geometry.ModelEdge@,System.Boolean@,System.Boolean@,TFlex.Model.Model3D.BodyTaper.MethodType@)`

Получить нижнее ребро

### `GetBottomFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref )`

ID: `M:TFlex.Model.Model3D.BodyTaper.GetBottomFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@)`

Получить нижнюю грань

### `GetTopEdge(System.Int32,TFlex.Model.Model3D.Geometry.ModelEdgeref ,System.Booleanref ,System.Booleanref ,TFlex.Model.Model3D.BodyTaper.MethodTyperef )`

ID: `M:TFlex.Model.Model3D.BodyTaper.GetTopEdge(System.Int32,TFlex.Model.Model3D.Geometry.ModelEdge@,System.Boolean@,System.Boolean@,TFlex.Model.Model3D.BodyTaper.MethodType@)`

Получить верхнее ребро

### `GetTopFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFaceref )`

ID: `M:TFlex.Model.Model3D.BodyTaper.GetTopFace(System.Int32,TFlex.Model.Model3D.Geometry.ModelFace@)`

Получить верхнюю грань

### `RemoveAllBottomEdges`

ID: `M:TFlex.Model.Model3D.BodyTaper.RemoveAllBottomEdges`

Удалить все нижние рёбра

### `RemoveAllBottomFaces`

ID: `M:TFlex.Model.Model3D.BodyTaper.RemoveAllBottomFaces`

Удалить все нижние грани

### `RemoveAllTopEdges`

ID: `M:TFlex.Model.Model3D.BodyTaper.RemoveAllTopEdges`

Удалить все верхние рёбра

### `RemoveAllTopFaces`

ID: `M:TFlex.Model.Model3D.BodyTaper.RemoveAllTopFaces`

Удалить все верхние грани

## Propertys

### `BottomAngle`

ID: `P:TFlex.Model.Model3D.BodyTaper.BottomAngle`

Нижний угол

### `BottomEdgeCount`

ID: `P:TFlex.Model.Model3D.BodyTaper.BottomEdgeCount`

Получить число нижних рёбер

### `BottomFaceCount`

ID: `P:TFlex.Model.Model3D.BodyTaper.BottomFaceCount`

Получить число нижних граней

### `Concave`

ID: `P:TFlex.Model.Model3D.BodyTaper.Concave`

Исправление внутренних углов

### `ConcaveRadius`

ID: `P:TFlex.Model.Model3D.BodyTaper.ConcaveRadius`

Радиус исправления внутренних углов

### `Corner`

ID: `P:TFlex.Model.Model3D.BodyTaper.Corner`

Обработка стыкующихся углов уклоняемых граней

### `Direction`

ID: `P:TFlex.Model.Model3D.BodyTaper.Direction`

Направление

### `DirectionReverse`

ID: `P:TFlex.Model.Model3D.BodyTaper.DirectionReverse`

Реверс направления

### `GroupType`

ID: `P:TFlex.Model.Model3D.BodyTaper.GroupType`

Получить тип объекта

### `KeepSourceBody`

ID: `P:TFlex.Model.Model3D.BodyTaper.KeepSourceBody`

Оставлять исходное тело

### `Method`

ID: `P:TFlex.Model.Model3D.BodyTaper.Method`

Метод

### `Miter`

ID: `P:TFlex.Model.Model3D.BodyTaper.Miter`

Двухстороннее соединение

### `PartingBody`

ID: `P:TFlex.Model.Model3D.BodyTaper.PartingBody`

Разделящее тело

### `PartingSheet`

ID: `P:TFlex.Model.Model3D.BodyTaper.PartingSheet`

Разделящее листовое тело

### `Point1`

ID: `P:TFlex.Model.Model3D.BodyTaper.Point1`

Первая точка задающая направление

### `Point2`

ID: `P:TFlex.Model.Model3D.BodyTaper.Point2`

Вторая точка задающая направление

### `SourceBody`

ID: `P:TFlex.Model.Model3D.BodyTaper.SourceBody`

Исходное тело

### `TopAngle`

ID: `P:TFlex.Model.Model3D.BodyTaper.TopAngle`

Верхний угол

### `TopEdgeCount`

ID: `P:TFlex.Model.Model3D.BodyTaper.TopEdgeCount`

Получить число верхних рёбер

### `TopFaceCount`

ID: `P:TFlex.Model.Model3D.BodyTaper.TopFaceCount`

Получить число верхних граней
