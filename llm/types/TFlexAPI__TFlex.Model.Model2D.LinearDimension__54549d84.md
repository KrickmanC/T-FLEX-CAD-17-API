# TFlex.Model.Model2D.LinearDimension

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс линейного размера на 2D

## Constructors

### `LinearDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LinearDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

## Methods

### `LinearDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LinearDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

### `ForceCenter`

ID: `M:TFlex.Model.Model2D.LinearDimension.ForceCenter`

Принудительное центрирование размера

### `Link(TFlex.Model.Model2D.LinearDimension.LinkedObject,TFlex.Model.Model2D.LinearDimension.LinkedObject)`

ID: `M:TFlex.Model.Model2D.LinearDimension.Link(TFlex.Model.Model2D.LinearDimension.LinkedObject,TFlex.Model.Model2D.LinearDimension.LinkedObject)`

Привязать размер к объектам

Parameters:
- `start`: Начальный объект привязки
- `end`: Конечный объект привязки

### `SetArcLength(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Boolean)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetArcLength(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Boolean)`

Установка параметров размера - длины дуги

Parameters:
- `arcOrCircle`: Измеряемая дуга, либо окружность, часть которой меряется
- `node1`: Узел, с которого (против часовой стрелки) начинается измерение
- `node2`: Узел, на котором (против часовой стрелки) заканчивается измерение
- `linesAreRadial`: Указывает на то, что выносныме линии размера должны быть радиальными (иначе - параллельны друг другу)

### `SetConstructionAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetConstructionAndNode(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Установка параметров размера между линией построения и узлом

Parameters:
- `line1`: Прямая
- `node1`: Узел, задающий положение начала выносной линии на прямой
- `node2`: Узел, до которого измеряется расстояние

### `SetConstructionAndOutline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,System.Boolean)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetConstructionAndOutline(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,System.Boolean)`

Установка параметров размера между линией построения и линией изображения

Parameters:
- `line1`: Прямая
- `node1`: Узел, задающий положение начала выносной линии на прямой
- `line2`: Отрезок
- `isOnEnd2`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)

### `SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetLeaderNote(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задает положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixLeaderNode`: Второй узел привязки, задает положение выносной полки
- `dX`: Смещение по горизонтали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)
- `dY`: Смещение по вертикали конца выносной полки относительно середины размерной линии (используется, если fixLeaderNode не задан)

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

Установка привязок размера к узлам, либо по относительным смещениям

Parameters:
- `fixNode1`: Первый узел привязки, задает положение размерной линии
- `offset1`: Смещение размерной линии относительно начала первой выносной линии (используется, если fixNode1 не задан)
- `fixNode2`: Второй узел привязки, задает положение размерного числа
- `offset2`: Смещение размерного числа относительно середины размерной линии (используется, если fixNode2 не задан)
- `fixNode3`: Третий узел привязки, задает положения конца полки размера
- `offset3`: Смещение длины полки размера (используется, если fixNode3 не задан)

### `SetOutlineAndNode(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetOutlineAndNode(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Node)`

Установка параметров размера между линией изображения и узлом

Parameters:
- `line1`: Отрезок
- `isOnEnd1`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `node2`: Узел, до которого измеряется расстояние

### `SetSegment(TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.DimensionAlignType)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetSegment(TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.DimensionAlignType)`

Установка параметров размера на отрезке

Parameters:
- `line1`: Отрезок
- `align`: Тип измерения

### `SetTwoConstructions(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetTwoConstructions(TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Node)`

Установка параметров размера между двумя линиями построения

Parameters:
- `line1`: Первая прямая
- `node1`: Узел, задающий положение начала выносной линии на прямой
- `line2`: Вторая прямая
- `node2`: Узел, задающий положение начала выносной линии на прямой

### `SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Установка параметров размера между двумя узлами

Parameters:
- `node1`: Первый узел
- `node2`: Второй узел

### `SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.DimensionAlignType)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetTwoNodes(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.DimensionAlignType)`

Установка параметров размера между двумя узлами

Parameters:
- `node1`: Первый узел
- `node2`: Второй узел
- `align`: Тип измерения

### `SetTwoNodesAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetTwoNodesAndLine(TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Object2D)`

Установка параметров размера между двумя узлами, перпендикулярно линии

Parameters:
- `node1`: Первый узел
- `node2`: Второй узел
- `guideLine`: Направляющая линия (построения или изображения)

### `SetTwoOutlines(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Outline,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.LinearDimension.SetTwoOutlines(TFlex.Model.Model2D.Outline,System.Boolean,TFlex.Model.Model2D.Outline,System.Boolean,System.Boolean)`

Установка параметров размера между двумя линиями изображения

Parameters:
- `line1`: Первый отрезок
- `isOnEnd1`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `line2`: Второй отрезок
- `isOnEnd2`: Указывает на то, что размер прикреплен к концу отрезка (иначе - к началу)
- `isConusDim`: Параметр, показывающий что размер ставится на конусе, ребрами которого являются отрезки, иначе - размер берётся как расстояние между отрезками

## Propertys

### `LinearDimType`

ID: `P:TFlex.Model.Model2D.LinearDimension.LinearDimType`

Подтип размера

### `LinkedEnd`

ID: `P:TFlex.Model.Model2D.LinearDimension.LinkedEnd`

Конечный объект привязки размера

### `LinkedStart`

ID: `P:TFlex.Model.Model2D.LinearDimension.LinkedStart`

Начальный объект привязки размера

### `SubType`

ID: `P:TFlex.Model.Model2D.LinearDimension.SubType`

Подтип размера
