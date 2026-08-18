# TFlex.Model.Model2D.IntersectionNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс узла, построенного на пересечении линий построения

## Constructors

### `IntersectionNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0,0

Parameters:
- `document`: Документ объекта

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Конструктор, задающий линии построения, на пересечении которых находится узел

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Double,System.Double)`

Конструктор, задающий линии построения, на пересечении которых находится узел и координаты точки, ближайшей к требуемому варианту пересечения

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения
- `x`: Коордианата X точки
- `y`: Коордианата Y точки

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Конструктор, задающий линии построения, на пересечении которых находится узел и вариант пересечения

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения
- `variant`: Вариант исполнения

## Methods

### `IntersectionNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0,0

Parameters:
- `document`: Документ объекта

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction)`

Конструктор, задающий линии построения, на пересечении которых находится узел

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Double,System.Double)`

Конструктор, задающий линии построения, на пересечении которых находится узел и координаты точки, ближайшей к требуемому варианту пересечения

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения
- `x`: Коордианата X точки
- `y`: Коордианата Y точки

### `IntersectionNode(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

ID: `M:TFlex.Model.Model2D.IntersectionNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Construction,System.Int32)`

Конструктор, задающий линии построения, на пересечении которых находится узел и вариант пересечения

Parameters:
- `document`: Документ объекта
- `srcConstruction1`: Первая линия построения
- `srcConstruction2`: Вторая линия построения
- `variant`: Вариант исполнения

## Propertys

### `Construction1`

ID: `P:TFlex.Model.Model2D.IntersectionNode.Construction1`

Первая линия построения, к которой привязан узел

### `Construction2`

ID: `P:TFlex.Model.Model2D.IntersectionNode.Construction2`

Вторая линия построения, к которой будет привязан узел

### `SubType`

ID: `P:TFlex.Model.Model2D.IntersectionNode.SubType`

Подтип способа построения узла
