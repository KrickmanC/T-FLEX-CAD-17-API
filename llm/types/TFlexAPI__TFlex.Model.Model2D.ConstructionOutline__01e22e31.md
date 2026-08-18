# TFlex.Model.Model2D.ConstructionOutline

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс линии изображения, основанной на узлах и линиях построения

## Remarks

Геометрия линии изображения данного класса определяется положением конечных узлов и/или геометрией подложенной линии построения.

## Constructors

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction)`

Конструктор, задающий линию построения по которой будет построена новая линия.

Parameters:
- `document`: Документ объекта
- `srcConstruction`: Линия построения

Remarks: В качестве линии построения не может быть задана прямая

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор, задающий узлы между которыми будет проведён отрезок

Parameters:
- `document`: Документ объекта
- `startNode`: Первый узел
- `endNode`: Второй узел

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Конструктор, задающий узлы, между которыми пройдет линия, и линию построения

Parameters:
- `document`: Документ объекта
- `startNode`: Первый узел
- `endNode`: Второй узел
- `srcConstruction`: Линия построения

Remarks: При отсутствии линии построения будет создан отрезок между узлами

## Methods

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction)`

Конструктор, задающий линию построения по которой будет построена новая линия.

Parameters:
- `document`: Документ объекта
- `srcConstruction`: Линия построения

Remarks: В качестве линии построения не может быть задана прямая

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор, задающий узлы между которыми будет проведён отрезок

Parameters:
- `document`: Документ объекта
- `startNode`: Первый узел
- `endNode`: Второй узел

### `ConstructionOutline(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.ConstructionOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction)`

Конструктор, задающий узлы, между которыми пройдет линия, и линию построения

Parameters:
- `document`: Документ объекта
- `startNode`: Первый узел
- `endNode`: Второй узел
- `srcConstruction`: Линия построения

Remarks: При отсутствии линии построения будет создан отрезок между узлами

## Propertys

### `AnchorNode`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.AnchorNode`

Узел привязки

Remarks: Для свойства Construction c типом ConstructionType.CircleConstruction и свойства GeometryType с типом ObjectGeometryType.CircleArc, или для свойства Construction c типом ConstructionType.EllipseConstruction и свойства GeometryType с типом ObjectGeometryType.EllipseArc

### `Construction`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.Construction`

Линия построения, по которой проходит линия изображения

### `EndNode`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.EndNode`

Конечный узел линии изображения

### `GeometryType`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.GeometryType`

Тип геометрии линии изображения

### `StartNode`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.StartNode`

Начальный узел линии изображения

### `SubType`

ID: `P:TFlex.Model.Model2D.ConstructionOutline.SubType`

Подтип линии изображения
