# TFlex.Model.Model2D.ArrowViewSymbol

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс обозначения вида по стрелке

## Constructors

### `ArrowViewSymbol(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ArrowViewSymbol.#ctor(TFlex.Model.Document)`

Конструктор

## Methods

### `ArrowViewSymbol(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.ArrowViewSymbol.#ctor(TFlex.Model.Document)`

Конструктор

### `SetAbsolutePosition(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.ArrowViewSymbol.SetAbsolutePosition(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка привязки стрелки по абсолютным координатам

Parameters:
- `x`: Координата x вершины стрелки
- `y`: Координата y вершины стрелки
- `angle`: Угол наклона линии стрелки

### `SetNodeAndAngle(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.ArrowViewSymbol.SetNodeAndAngle(TFlex.Model.Model2D.Node,TFlex.Model.Parameter)`

Установка привязки по узлу и углу

Parameters:
- `node`: Узел вершины стрелки
- `angle`: Угол наклона стрелки

### `SetNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.ArrowViewSymbol.SetNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Установка привязки к узлам

Parameters:
- `node1`: Первый узел (позиция стрелки)
- `node2`: Второй узел (определяет направление стрелки)

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.Angle`

Угол наклона стрелки

### `ArrowLength`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.ArrowLength`

Длина стрелки

### `ArrowLineWidth`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.ArrowLineWidth`

Толщина линий стрелки

### `ArrowSize`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.ArrowSize`

Размер стрелки

### `ArrowType`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.ArrowType`

Тип стрелки

### `AttachmentType`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.AttachmentType`

Тип привязки

### `Node1`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.Node1`

Первый узел привязки

### `Node2`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.Node2`

Второй узел привязки

### `Note`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.Note`

Надпись

### `NoteOffset1`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.NoteOffset1`

Смещение надписи перпендикулярно полке

### `NoteOffset2`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.NoteOffset2`

Смещение надписи вдоль полки

### `NotePosition`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.NotePosition`

Положение надписи

### `Point`

ID: `P:TFlex.Model.Model2D.ArrowViewSymbol.Point`

Координаты точки привязки стрелки
