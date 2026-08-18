# TFlex.Model.Model2D.OutlineContourSegment

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Сегмент контура штриховки/заливки, созданный на основе линии изображения

## Constructors

### `OutlineContourSegment(TFlex.Model.Model2D.Contour)`

ID: `M:TFlex.Model.Model2D.OutlineContourSegment.#ctor(TFlex.Model.Model2D.Contour)`

Конструктор, добавляющий сегмент в конец контура

Parameters:
- `source`: Контур, к которому добавляется сегмент

### `OutlineContourSegment(TFlex.Model.Model2D.Contour,System.Int32)`

ID: `M:TFlex.Model.Model2D.OutlineContourSegment.#ctor(TFlex.Model.Model2D.Contour,System.Int32)`

Конструктор, вставляющий сегмент в контур по указанному индексу

Parameters:
- `source`: Контур, к которому добавляется сегмент
- `index`: Номер сегмента, перед которым необходимо вставить данный сегмент

## Methods

### `OutlineContourSegment(TFlex.Model.Model2D.Contour)`

ID: `M:TFlex.Model.Model2D.OutlineContourSegment.#ctor(TFlex.Model.Model2D.Contour)`

Конструктор, добавляющий сегмент в конец контура

Parameters:
- `source`: Контур, к которому добавляется сегмент

### `OutlineContourSegment(TFlex.Model.Model2D.Contour,System.Int32)`

ID: `M:TFlex.Model.Model2D.OutlineContourSegment.#ctor(TFlex.Model.Model2D.Contour,System.Int32)`

Конструктор, вставляющий сегмент в контур по указанному индексу

Parameters:
- `source`: Контур, к которому добавляется сегмент
- `index`: Номер сегмента, перед которым необходимо вставить данный сегмент

## Propertys

### `Direction`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.Direction`

Направление сегмента контура

Remarks: True если сегмент контура направлен по положительному направлению линии изображения, false в противном случае

### `EndIntersectionNumber`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.EndIntersectionNumber`

Номер пересечения в конце сегмента контура

### `EndIntersectionOutline`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.EndIntersectionOutline`

Линия изображения, задающая конец сегмента контура

### `Outline`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.Outline`

Исходная линия изображения

### `StartIntersectionNumber`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.StartIntersectionNumber`

Номер пересечения в начале сегмента контура

### `StartIntersectionOutline`

ID: `P:TFlex.Model.Model2D.OutlineContourSegment.StartIntersectionOutline`

Линия изображения, задающая начало сегмента контура
