# TFlex.Model.Model3D.CircularDimension3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Размер на окружности на 3D

## Constructors

### `CircularDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ размера на окружности

## Methods

### `CircularDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ размера на окружности

### `CreateProjected(TFlex.Model.Model3D.Projection)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.CreateProjected(TFlex.Model.Model3D.Projection)`

Создание проекции размера

Parameters:
- `projection`: Проекция, на которую проецируется размер

### `SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.SetDiametralDimensionType(TFlex.Model.Model2D.DiametralDimensionType)`

Установка размера, как диаметрального

Parameters:
- `type`: Тип отрисовки диаметрального размера

### `SetElement(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.DimensionUVCoords,System.Boolean,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.SetElement(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.DimensionUVCoords,System.Boolean,System.Double,System.Double)`

Установка привязок размера к 3D элементам

Parameters:
- `CircleElement`: Элемент для привязки размера (грань, ребро)
- `Coords`: Координаты для определения привязки размера
- `Diameter`: Ставим диаметр, если true, иначе - радиус
- `Angle`: Угол, на котором находится размерная стрелка
- `Offset`: Расстояние от размерного числа до окружности

### `SetOffsets(System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.SetOffsets(System.Double,System.Double)`

Установка положения размера на окружности

Parameters:
- `angle`: Угол, на котором находится размерная стрелка (используется, если отсутствует fixNode)
- `offset`: Расстояние от размерного числа до окружности (используется, если отсутствует fixNode)

### `SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

ID: `M:TFlex.Model.Model3D.CircularDimension3D.SetRadialDimensionType(TFlex.Model.Model2D.RadialDimensionType)`

Установка размера, как радиального

Parameters:
- `type`: Тип отрисовки радиального размера

## Propertys

### `IsExternal`

ID: `P:TFlex.Model.Model3D.CircularDimension3D.IsExternal`

Управление параметром "Внешний" 3D-размера

Parameters:
- `value`: Значение параметра

### `SubType`

ID: `P:TFlex.Model.Model3D.CircularDimension3D.SubType`

Подтип размера
