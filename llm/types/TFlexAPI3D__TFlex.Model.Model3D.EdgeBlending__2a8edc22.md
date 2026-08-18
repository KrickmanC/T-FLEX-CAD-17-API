# TFlex.Model.Model3D.EdgeBlending

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Сглаживание рёбер

## Constructors

### `EdgeBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания сглаживания рёбер

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `EdgeBlending(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.#ctor(TFlex.Model.Document)`

Конструктор для создания сглаживания рёбер

Parameters:
- `doc`: Документ, в котором создаётся новый объект

### `AddEdgesByVertex(TFlex.Model.Model3D.Geometry.ModelVertex,TFlex.Model.Parameter,System.Boolean)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.AddEdgesByVertex(TFlex.Model.Model3D.Geometry.ModelVertex,TFlex.Model.Parameter,System.Boolean)`

Для всех рёбер, инцидентных данной вершине, задаются отступы

Parameters:
- `vertex`: Вершина
- `distance`: Значение отступа
- `common`: Параметр установлен для всех вершин

### `AddTopol(TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.AddTopol(TFlex.Model.Model3D.Geometry.ModelTopol)`

Добавить топологию с общими атрибутами

Parameters:
- `topol`: Топология

Remarks: Топология должна быть ребром, циклом или гранью

### `AddTopol(TFlex.Model.Model3D.Geometry.ModelTopol,TFlex.Model.Model3D.EdgeBlending.Attribute)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.AddTopol(TFlex.Model.Model3D.Geometry.ModelTopol,TFlex.Model.Model3D.EdgeBlending.Attribute)`

Добавить топологию со своими атрибутами

Parameters:
- `topol`: Топология

Remarks: Топология должна быть ребром, циклом или гранью. Независимо от типа топологии, у топологии используются только рёбра. Гладкосопряженные рёбра должны быть определены с одинаковыми атрибутами, в противном случае результат не специфицирован

### `GetAttrib(System.Int32)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.GetAttrib(System.Int32)`

Получить атрибуты топологии

Parameters:
- `topolIndex`: Номер топологии

Remarks: Если атрибут равен 0, тогда топология использует общие атрибуты

### `SetAttrib(System.Int32,TFlex.Model.Model3D.EdgeBlending.Attribute)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.SetAttrib(System.Int32,TFlex.Model.Model3D.EdgeBlending.Attribute)`

Установить атрибуты топологии

Parameters:
- `topolIndex`: Номер топологии
- `attrib`: Атрибуты

Remarks: Если attrib равно 0, тогда топология использует общие атрибуты. Параметр Position для первой и последней позиции, не используется и изменяется

### `getTopol(System.Int32)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.getTopol(System.Int32)`

Получить топологию

Parameters:
- `topolIndex`: Номер топологии

Returns: Топология

Remarks: Топология может быть ребром, циклом или гранью

## Propertys

### `CommonAttrib`

ID: `P:TFlex.Model.Model3D.EdgeBlending.CommonAttrib`

Общие атрибуты

### `GroupType`

ID: `P:TFlex.Model.Model3D.EdgeBlending.GroupType`

Получить тип объекта

### `OverflowCliff`

ID: `P:TFlex.Model.Model3D.EdgeBlending.OverflowCliff`

Параметр "Сохранять острые рёбра"

### `OverflowNotch`

ID: `P:TFlex.Model.Model3D.EdgeBlending.OverflowNotch`

Параметр "Вырез"

### `OverflowSmooth`

ID: `P:TFlex.Model.Model3D.EdgeBlending.OverflowSmooth`

Параметр "Учитывать гладкие перекрытия"

### `Propagate`

ID: `P:TFlex.Model.Model3D.EdgeBlending.Propagate`

Параметр "Продолжить по касательной"

### `RemoveTopologyFlag`

ID: `P:TFlex.Model.Model3D.EdgeBlending.RemoveTopologyFlag`

Параметр "Удалять элементы"

### `TopolCount`

ID: `P:TFlex.Model.Model3D.EdgeBlending.TopolCount`

Получить число топологий
