# TFlex.Model.Model2D.ConstructionContourSegment

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Сегмент контура штриховки/заливки, созданный на основе линии построения и/или узлов

## Constructors

### `ConstructionContourSegment(TFlex.Model.Model2D.Contour)`

ID: `M:TFlex.Model.Model2D.ConstructionContourSegment.#ctor(TFlex.Model.Model2D.Contour)`

Конструктор, добавляющий сегмент в конец контура

Parameters:
- `source`: Контур, к которому добавляется сегмент

### `ConstructionContourSegment(TFlex.Model.Model2D.Contour,System.Int32)`

ID: `M:TFlex.Model.Model2D.ConstructionContourSegment.#ctor(TFlex.Model.Model2D.Contour,System.Int32)`

Конструктор, вставляющий сегмент в контур по указанному индексу

Parameters:
- `source`: Контур, к которому добавляется сегмент
- `index`: Номер сегмента, перед которым необходимо вставить данный сегмент

## Methods

### `ConstructionContourSegment(TFlex.Model.Model2D.Contour)`

ID: `M:TFlex.Model.Model2D.ConstructionContourSegment.#ctor(TFlex.Model.Model2D.Contour)`

Конструктор, добавляющий сегмент в конец контура

Parameters:
- `source`: Контур, к которому добавляется сегмент

### `ConstructionContourSegment(TFlex.Model.Model2D.Contour,System.Int32)`

ID: `M:TFlex.Model.Model2D.ConstructionContourSegment.#ctor(TFlex.Model.Model2D.Contour,System.Int32)`

Конструктор, вставляющий сегмент в контур по указанному индексу

Parameters:
- `source`: Контур, к которому добавляется сегмент
- `index`: Номер сегмента, перед которым необходимо вставить данный сегмент

## Propertys

### `Construction`

ID: `P:TFlex.Model.Model2D.ConstructionContourSegment.Construction`

Линия построения, задающая сегмент контура или 0 если линия построения не задана

### `Direction`

ID: `P:TFlex.Model.Model2D.ConstructionContourSegment.Direction`

Направление сегмента контура

Returns: true если сегмент контура направлен по положительному направлению линии построения, false в противном случае

Remarks: Параметр имеет смысл только в случае если заданы одновременно два узла и линия построения. Если любой из элементов не задан, то параметр имеет значение true.

### `EndNode`

ID: `P:TFlex.Model.Model2D.ConstructionContourSegment.EndNode`

Конечный узел сегмента контура

### `StartNode`

ID: `P:TFlex.Model.Model2D.ConstructionContourSegment.StartNode`

Начальный узел или 0 если узел не задан
