# TFlex.Model.Model2D.BetweenNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Узел между двумя узлами

## Constructors

### `BetweenNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.BetweenNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0, 0

Parameters:
- `document`: Документ объекта

### `BetweenNode(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.BetweenNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Double)`

Конструктор создающий узел по двум узлам и вещественному параметру.

Parameters:
- `document`: Документ объекта
- `first`: Первый узел
- `second`: Первый узел
- `coeff`: Коэффициент, определящий положение между двумя узлами

## Methods

### `BetweenNode(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.BetweenNode.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию. Координаты установлены в значение 0, 0

Parameters:
- `document`: Документ объекта

### `BetweenNode(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.BetweenNode.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Node,TFlex.Model.Model2D.Node,System.Double)`

Конструктор создающий узел по двум узлам и вещественному параметру.

Parameters:
- `document`: Документ объекта
- `first`: Первый узел
- `second`: Первый узел
- `coeff`: Коэффициент, определящий положение между двумя узлами

## Propertys

### `Coefficient`

ID: `P:TFlex.Model.Model2D.BetweenNode.Coefficient`

Коэффициент, определящий положение между двумя узлами

### `FirstNode`

ID: `P:TFlex.Model.Model2D.BetweenNode.FirstNode`

Первый узел

### `SecondNode`

ID: `P:TFlex.Model.Model2D.BetweenNode.SecondNode`

Второй узел

### `SubType`

ID: `P:TFlex.Model.Model2D.BetweenNode.SubType`

Подтип способа построения узла
