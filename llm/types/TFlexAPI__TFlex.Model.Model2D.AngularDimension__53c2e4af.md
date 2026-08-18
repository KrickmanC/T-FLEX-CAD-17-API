# TFlex.Model.Model2D.AngularDimension

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Угловой размер на 2D

## Constructors

### `AngularDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.AngularDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

## Methods

### `AngularDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.AngularDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

### `SetConstructionAndOutline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.AnglePosition)`

ID: `M:TFlex.Model.Model2D.AngularDimension.SetConstructionAndOutline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.AnglePosition)`

Установка параметров размера между линией построения и линией изображения

Parameters:
- `line1`: Прямая
- `node1`: Узел, задающий положение начала выносной линии на прямой
- `line2`: Отрезок
- `isOnEnd2`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `position`: Между какими направлениями измеряется угол

### `SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.AngularDimension.SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задает положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixLeaderNode`: Второй узел привязки, задает положение выносной полки
- `dX`: Смещение по горизонтали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)
- `dY`: Смещение по вертикали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.AngularDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задает положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixNode2`: Второй узел привязки, задает положение размерного числа
- `offset2`: Смещение размерного числа по дуге относительно середины размерной линии (используется, если fixNode2 не задан)
- `fixNode3`: Третий узел привязки, задает положения конца полки размера
- `offset3`: Смещение длина полки размера (используется, если fixNode3 не задан)

### `SetTwoConstructions(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.AnglePosition)`

ID: `M:TFlex.Model.Model2D.AngularDimension.SetTwoConstructions(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.AnglePosition)`

Установка параметров размера между двумя линиями построения

Parameters:
- `line1`: Первая прямая
- `node1`: Узел, задающий положение начала выносной линии на прямой
- `line2`: Вторая прямая
- `node2`: Узел, задающий положение начала выносной линии на прямой
- `position`: Между какими направлениями измеряется угол

### `SetTwoOutlines(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.AnglePosition)`

ID: `M:TFlex.Model.Model2D.AngularDimension.SetTwoOutlines(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.AnglePosition)`

Установка параметров размера между двумя линиями изображения

Parameters:
- `line1`: Первый отрезок
- `isOnEnd1`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `line2`: Второй отрезок
- `isOnEnd2`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `position`: Между какими направлениями измеряется угол

## Propertys

### `AngularDimType`

ID: `P:TFlex.Model.Model2D.AngularDimension.AngularDimType`

Подтип углового размера

### `SubType`

ID: `P:TFlex.Model.Model2D.AngularDimension.SubType`

Подтип размера

### `TextOnLine`

ID: `P:TFlex.Model.Model2D.AngularDimension.TextOnLine`

Текст вдоль линии, а не по дуге
