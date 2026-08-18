# TFlex.Model.Model2D.CenterAxisOutline

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линия изображения - ось окружности или эллипса

## Constructors

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,System.Boolean)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,System.Boolean)`

Конструктор для создания горизонтальной или вертикальной оси окружности

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `horizontal`: true, если ось является горизонтальной

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра, заданного окружностью построения

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerConstruction`: Окружность, определяющая центр
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра в узле

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerNode`: Узел центра
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра, заданного дугой или окружностью изображения

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerOutline`: Окружность или дуга, определяющая центр
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

## Methods

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,System.Boolean)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,System.Boolean)`

Конструктор для создания горизонтальной или вертикальной оси окружности

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `horizontal`: true, если ось является горизонтальной

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Construction,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра, заданного окружностью построения

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerConstruction`: Окружность, определяющая центр
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра в узле

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerNode`: Узел центра
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

### `CenterAxisOutline(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model2D.CenterAxisOutline.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.CenterAxisOutline.CenterAxisType,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Outline,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node)`

Конструктор для создания оси от центра, заданного дугой или окружностью изображения

Parameters:
- `document`: Документ
- `source`: Обозначаемая линия изображения
- `axisType`: Тип оси
- `centerOutline`: Окружность или дуга, определяющая центр
- `limit1Outline`: Первая ограничивающая линия изображения (допускается значение null)
- `limit2Outline`: Вторая ограничивающая линия изображения (допускается значение null)
- `limit1Node`: Первый ограничивающий узел (допускается значение null)
- `limit2Node`: Второй ограничивающий узел (допускается значение null)

## Propertys

### `AxisType`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.AxisType`

Тип оси

### `CenterConstruction`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.CenterConstruction`

Линия построения, определяющая центр

### `CenterNode`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.CenterNode`

Центральный узел

### `CenterOutline`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.CenterOutline`

Линия изображения, определяющая центр

### `Limit1Node`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.Limit1Node`

Первый ограничивающий узел

### `Limit1Outline`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.Limit1Outline`

Первая ограничивающая линия изображения

### `Limit2Node`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.Limit2Node`

Второй ограничивающий узел

### `Limit2Outline`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.Limit2Outline`

Вторая ограничивающая линия изображения

### `SourceOutline`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.SourceOutline`

Исходная линия изображения

### `SubType`

ID: `P:TFlex.Model.Model2D.CenterAxisOutline.SubType`

Тип линии изображения
