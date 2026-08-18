# TFlex.Model.Model2D.SplineConstruction

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия построения - сплайн

## Constructors

### `SplineConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `SplineConstruction(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddPoint(TFlex.Drawing.Point,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.AddPoint(TFlex.Drawing.Point,TFlex.Model.Parameter)`

Добавить точку

Parameters:
- `point`: Добавляемая точка
- `weight`: Вес точки

Returns: Индекс точки

### `AddPoint(TFlex.Drawing.Point,TFlex.Model.Parameter,System.Boolean)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.AddPoint(TFlex.Drawing.Point,TFlex.Model.Parameter,System.Boolean)`

Добавить точку

Parameters:
- `point`: Добавляемая точка
- `weight`: Вес точки
- `tolerant`: Является ли точка с допуском

Returns: Индекс точки

### `AddPoint(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.AddPoint(TFlex.Model.Model2D.Node)`

Добавить точку

Parameters:
- `node`: Добавляемый узел

Returns: Индекс узла

### `AddPoint(TFlex.Model.Model2D.Node,System.Boolean)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.AddPoint(TFlex.Model.Model2D.Node,System.Boolean)`

Добавить точку

Parameters:
- `node`: Добавляемый узел
- `tolerant`: Является ли точка с допуском

Returns: Индекс узла

### `DeletePoint(System.Int32)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.DeletePoint(System.Int32)`

Удалить точку

Parameters:
- `index`: Индекс удаляемой точки

### `GetPointWeight(System.Int32)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.GetPointWeight(System.Int32)`

Получить вес точки

Parameters:
- `index`: Индекс точки

### `InsertPoint(System.Int32,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.InsertPoint(System.Int32,TFlex.Model.Model2D.Node)`

Вставить точку

Parameters:
- `index`: Индекс точки, перед которой будет добавлена данная точка
- `node`: Добавляемый узел

### `SetDegree(System.Int32)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.SetDegree(System.Int32)`

Установить степень сплайна (может игнорироваться)

### `SetPointWeight(System.Int32,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.SetPointWeight(System.Int32,TFlex.Model.Parameter)`

Установить вес точки

Parameters:
- `index`: Индекс точки
- `weight`: Вес точки

### `SetTolerance(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.SplineConstruction.SetTolerance(TFlex.Model.Parameter)`

Точность

Remarks: В единицах документа

## Propertys

### `Closed`

ID: `P:TFlex.Model.Model2D.SplineConstruction.Closed`

Замкнутый сплайн

### `EndExtension`

ID: `P:TFlex.Model.Model2D.SplineConstruction.EndExtension`

Управление удлинением в конце сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `EndExtensionType`

ID: `P:TFlex.Model.Model2D.SplineConstruction.EndExtensionType`

Тип управления удлинением в конце сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `EndExtensionValue`

ID: `P:TFlex.Model.Model2D.SplineConstruction.EndExtensionValue`

Значение смещения в конце сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `EndTangentNode`

ID: `P:TFlex.Model.Model2D.SplineConstruction.EndTangentNode`

Узел, задающий касание в конце

### `GeometryType`

ID: `P:TFlex.Model.Model2D.SplineConstruction.GeometryType`

Тип геометрии линии построения

### `Interpolating`

ID: `P:TFlex.Model.Model2D.SplineConstruction.Interpolating`

Интерполяционный сплайн

Remarks: Данное свойство позволяет задать тип сплайна. true, если необходимо установить тип сплайна "По ломаной", false - определяет тип "Через узлы"

### `IsPolyline`

ID: `P:TFlex.Model.Model2D.SplineConstruction.IsPolyline`

Сплайн - полилиния

### `PointCount`

ID: `P:TFlex.Model.Model2D.SplineConstruction.PointCount`

Количество точек сплайна

### `StartExtension`

ID: `P:TFlex.Model.Model2D.SplineConstruction.StartExtension`

Управление удлинением в начале сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `StartExtensionType`

ID: `P:TFlex.Model.Model2D.SplineConstruction.StartExtensionType`

Тип управления удлинением в начале сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `StartExtensionValue`

ID: `P:TFlex.Model.Model2D.SplineConstruction.StartExtensionValue`

Значение смещения в начале сплайна

Remarks: Параметры смещения не доступны для замкнутых сплайнов

### `StartTangentNode`

ID: `P:TFlex.Model.Model2D.SplineConstruction.StartTangentNode`

Узел, задающий касание в начале

### `SubType`

ID: `P:TFlex.Model.Model2D.SplineConstruction.SubType`

Подтип линии построения
