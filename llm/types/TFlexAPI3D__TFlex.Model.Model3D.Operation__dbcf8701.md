# TFlex.Model.Model3D.Operation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех операций

## Remarks

В текущей версии поддерживаются только листовые и твёрдотельные операции

## Methods

### `DeleteMateTransformation`

ID: `M:TFlex.Model.Model3D.Operation.DeleteMateTransformation`

Удалить текущее преобразование сопряжений

### `ExportGeometry(System.String,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Operation.ExportGeometry(System.String,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

Сохранение тел в файл в формате Parasolid

Parameters:
- `file`: Имя выходного файла
- `redundant`: Удалять избыточную геометрию
- `materials`: Выгружать с материалами
- `assembly`: Сохранять структуру сборки
- `binary`: Использовать бинарный формат

Returns: Результат экспорта

### `FindAssociatedTopols(TFlex.Model.Model3D.Hole)`

ID: `M:TFlex.Model.Model3D.Operation.FindAssociatedTopols(TFlex.Model.Model3D.Hole)`

Поиск топологических элементов, ассоциированных с отверстием

### `FindAssociatedTopols(TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Operation.FindAssociatedTopols(TFlex.Model.Model3D.LCS)`

Поиск топологических элементов, ассоциированных с системой координат

### `FindBodyOwner(System.Boolean)`

ID: `M:TFlex.Model.Model3D.Operation.FindBodyOwner(System.Boolean)`

Получить базовую операцию, в которой хранятся свойства тела

Parameters:
- `any`: Если базовой операции нет, то возвращать саму передаваемую операцию

### `LockMateTransformation`

ID: `M:TFlex.Model.Model3D.Operation.LockMateTransformation`

Заблокировать текущее преобразование сопряжений от дальнейших изменений

### `RadialRayTest(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,System.Collections.Generic.List`1{System.Double},System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BasePoint3D})`

ID: `M:TFlex.Model.Model3D.Operation.RadialRayTest(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BaseDirection,System.Collections.Generic.List`1{System.Double},System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BasePoint3D})`

Определение точек касания луча с операцией по расстоянию до перпендикуляра к лучу

Parameters:
- `operation`: Операция
- `rayOrigin`: Исходная точка луча
- `rayDir`: Направление луча
- `distances`: Растояние до перпендикуляра к лучу
- `points`: Точки касания

Returns: Результат поиска

### `RangePoint(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Operation.RangePoint(TFlex.Model.Model3D.Operation,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Найти точку на операции ближайшую к данной точке

Parameters:
- `operation`: Операция
- `point`: Точка

Returns: Точка на теле ближайшая к данной точке

## Propertys

### `Body`

ID: `P:TFlex.Model.Model3D.Operation.Body`

Тело, в которое входит операция

### `CoatingMaterial`

ID: `P:TFlex.Model.Model3D.Operation.CoatingMaterial`

Материал операции

### `Fixed`

ID: `P:TFlex.Model.Model3D.Operation.Fixed`

Свойство фиксации операции относительно сопряжений

### `Geometry`

ID: `P:TFlex.Model.Model3D.Operation.Geometry`

Геометрические данные операции

### `GroupType`

ID: `P:TFlex.Model.Model3D.Operation.GroupType`

Получить тип объекта

### `IsTransparencyOn`

ID: `P:TFlex.Model.Model3D.Operation.IsTransparencyOn`

Управление прозрачностью

### `Material`

ID: `P:TFlex.Model.Model3D.Operation.Material`

Материал операции

### `MeshDensity`

ID: `P:TFlex.Model.Model3D.Operation.MeshDensity`

Плотность сетки в диапазоне 0.0-1.0

### `Suppression`

ID: `P:TFlex.Model.Model3D.Operation.Suppression`

Свойство подавленности операции

### `TopLevel`

ID: `P:TFlex.Model.Model3D.Operation.TopLevel`

Признак верхней операции

Remarks: Именно геометрия верхних операций является текущей геометрией модели в целом

### `TopOperation`

ID: `P:TFlex.Model.Model3D.Operation.TopOperation`

Верхняя операция в теле

### `Transparency`

ID: `P:TFlex.Model.Model3D.Operation.Transparency`

Прозрачность

Remarks: Значение от 0 до 1

### `Wireframe`

ID: `P:TFlex.Model.Model3D.Operation.Wireframe`

Признак рёберной отрисовки операции
