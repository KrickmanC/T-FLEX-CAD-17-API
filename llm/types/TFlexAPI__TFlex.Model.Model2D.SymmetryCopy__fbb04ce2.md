# TFlex.Model.Model2D.SymmetryCopy

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Копия-симметрия

## Constructors

### `SymmetryCopy(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.SymmetryCopy.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

## Methods

### `SymmetryCopy(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.SymmetryCopy.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

### `SetLine(TFlex.Model.Model2D.Object2D)`

ID: `M:TFlex.Model.Model2D.SymmetryCopy.SetLine(TFlex.Model.Model2D.Object2D)`

Установка оси симметрии по линии построения-прямой

Parameters:
- `axisLine`: Линия, задающая ось

### `SetNodeAndOffset(TFlex.Model.Model2D.Node,System.Double,System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.SymmetryCopy.SetNodeAndOffset(TFlex.Model.Model2D.Node,System.Double,System.Double,System.Double,System.Double)`

Установка оси симметрии по узлу и смещению

Parameters:
- `baseNode`: Базовый узел - первая точка, определяющая ось
- `baseX`: X-координата базовой точки
- `baseY`: Y-координата базовой точки
- `dX`: Смещение по оси X для второй точки, определяющей ось
- `dY`: Смещение по оси Y для второй точки, определяющей ось

Remarks: Если базовый узел не задан (NULL), то привязка происходит по точке с заданными координатами. В противном случае - координаты игнорируются

### `SetNodes(TFlex.Model.Model2D.Node,System.Double,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.SymmetryCopy.SetNodes(TFlex.Model.Model2D.Node,System.Double,System.Double,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка оси симметрии по двум узлам

Parameters:
- `firstNode`: Первый узел, определяющий ось
- `firstX`: X-координата первой точи, определяющей ось
- `firstY`: Y-координата первой точи, определяющей ось
- `secondNode`: Второй узел, определяющий ось
- `secondX`: X-координата второй точи, определяющей ось
- `secondY`: Y-координата второй точи, определяющей ось

Remarks: Если какой-либо из узлов не задан (NULL), то привязка происходит по точке с заданными координатами. В противном случае - координаты игнорируются

## Propertys

### `CopyType`

ID: `P:TFlex.Model.Model2D.SymmetryCopy.CopyType`

Подтип операции копирования

### `SymmetryType`

ID: `P:TFlex.Model.Model2D.SymmetryCopy.SymmetryType`

Тип задания оси симметрии
