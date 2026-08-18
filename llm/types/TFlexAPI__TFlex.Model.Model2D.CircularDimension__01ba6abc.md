# TFlex.Model.Model2D.CircularDimension

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Размер на окружности на 2D

## Constructors

### `CircularDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.CircularDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ

## Methods

### `CircularDimension(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.CircularDimension.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ

### `SetDiametral(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.DiametralDimensionType,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetDiametral(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.DiametralDimensionType,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка диаметрального размера

Parameters:
- `circle`: Окружность - линия построения или изображения, на которой устанавливается размер
- `type`: Тип отрисовки диаметрального размера
- `fixNode`: Узел привязки размерной стрелки
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixNode)
- `offset`: Расстояние от размерного числа до окружности (используется, если отсутствует fixNode)

### `SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

Установка размера, как диаметрального

Parameters:
- `type`: Тип отрисовки диаметрального размера

### `SetOffsets(TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetOffsets(TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка положения размера на окружности

Parameters:
- `fixNode`: Узел привязки размерной стрелки
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixNode)
- `offset`: Расстояние от размерного числа до окружности (используется, если отсутствует fixNode)

### `SetRadial(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.RadialDimensionType,TFlex.Model.Model2D.Node,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetRadial(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.RadialDimensionType,TFlex.Model.Model2D.Node,System.Double,System.Double)`

Установка радиального размера

Parameters:
- `circle`: Окружность - линия построения или изображения, на которой устанавливается размер
- `type`: Тип отрисовки радиального размера
- `fixNode`: Узел привязки размерной стрелки
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixNode)
- `offset`: Расстояние от размерного числа до окружности (используется, если отсутствует fixNode)

### `SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

Установка размера, как радиального

Parameters:
- `type`: Тип отрисовки радиального размера

### `SetShortenedRadial(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Node,System.Double,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

ID: `M:TFlex.Model.Model2D.CircularDimension.SetShortenedRadial(TFlex.Model.Model2D.Object2D,TFlex.Model.Model2D.Node,System.Double,System.Double,TFlex.Model.Model2D.Node,System.Double,TFlex.Model.Model2D.Node,System.Double)`

Установка радиального размера с изломом размерной линии

Parameters:
- `circle`: Окружность - линия построения или изображения, на которой устанавливается размер
- `fixAngleNode`: Узел привязки размерной стрелки (привязка угла положения и начала стрелки)
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixAngleNode)
- `offset`: Расстояние от начала размерной линии до окружности (используется, если отсутствует fixAngleNode)
- `fixRatioNode`: Узел привязки положения излома размерной стрелки
- `ratio`: Соотношение, суммарной длины стрелки и длины стрелки после излома (используется, если отсутствует fixRatioNode)
- `fixWidthNode`: Узел привязки ширины излома размерной стрелки
- `width`: Ширина излома размерной стрелки (используется, если отсутствует fixWidthNode)

## Propertys

### `SubType`

ID: `P:TFlex.Model.Model2D.CircularDimension.SubType`

Подтип размера
