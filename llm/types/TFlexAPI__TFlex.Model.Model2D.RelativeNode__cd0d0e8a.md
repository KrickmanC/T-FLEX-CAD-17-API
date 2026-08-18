# TFlex.Model.Model2D.RelativeNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс узла, заданного относительно другого элемента

## Constructors

### `RelativeNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RelativeNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

## Methods

### `RelativeNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RelativeNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `SetByParameter(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RelativeNode.SetByParameter(TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

Установка привязки к линии построения (Окружность, Эллипс, Полилиния) по параметру

Parameters:
- `srcConstruction`: Исходная линия построения
- `param`: Параметр для определения положения узла

### `SetEndOfPolyline(TFlex.Model.Model2D.Construction,System.Boolean)`

ID: `M:TFlex.Model.Model2D.RelativeNode.SetEndOfPolyline(TFlex.Model.Model2D.Construction,System.Boolean)`

Установка привязки к одному из концов линии построения - полилинии

Parameters:
- `srcConstruction`: Исходная линия построения
- `alignToStart`: Параметр для определения положения узла

### `SetOffset(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RelativeNode.SetOffset(TFlex.Model.Model2D.Node,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка смещения относительно родительского узла

Parameters:
- `parentNode`: Родительский узел
- `dX`: Смещение по оси X (без учёта масштаба текущей страницы)
- `dY`: Смещение по оси Y (без учёта масштаба текущей страницы)

### `SetOnConstruction(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RelativeNode.SetOnConstruction(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Parameter)`

Установка смещения относительно родительского узла по линии построения

Parameters:
- `parentNode`: Родительский узел
- `srcConstruction`: Исходная линия построения
- `distance`: Параметр смещения

## Propertys

### `IsEndOfPolylineAlignToStart`

ID: `P:TFlex.Model.Model2D.RelativeNode.IsEndOfPolylineAlignToStart`

Параметр для определения положения узла - для RelativeType.EndOfPolyline

### `ParameterX`

ID: `P:TFlex.Model.Model2D.RelativeNode.ParameterX`

Параметр(в зависимости от значения RelationType)

Returns: Смещение по оси X (без учёта масштаба текущей страницы) - для RelativeType.Offset. Параметр смещения - для RelativeType.OnConstruction. Параметр для определения положения узла - для RelativeType.ByParameter.

### `ParameterY`

ID: `P:TFlex.Model.Model2D.RelativeNode.ParameterY`

Смещение по оси Y (без учёта масштаба текущей страницы) - для RelativeType.Offset

### `RelationType`

ID: `P:TFlex.Model.Model2D.RelativeNode.RelationType`

Тип привязки узла

### `SubType`

ID: `P:TFlex.Model.Model2D.RelativeNode.SubType`

Подтип способа построения узла
