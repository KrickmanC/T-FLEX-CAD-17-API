# TFlex.Model.Model3D.LinearDimension3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Линейный размер на 3D

## Constructors

### `LinearDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ, в котором создаётся размер

## Methods

### `LinearDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ, в котором создаётся размер

### `CreateBaseDimensions(TFlex.Model.Model3D.DimensionUVCoords,System.Collections.Generic.List`1{TFlex.Model.Model3D.DimensionsChainElement},TFlex.Model.Model3D.Object3D,System.Collections.Generic.List`1{TFlex.Model.Model3D.LinearDimension3D})`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.CreateBaseDimensions(TFlex.Model.Model3D.DimensionUVCoords,System.Collections.Generic.List`1{TFlex.Model.Model3D.DimensionsChainElement},TFlex.Model.Model3D.Object3D,System.Collections.Generic.List`1{TFlex.Model.Model3D.LinearDimension3D})`

Создание цепочки размеров от базы

Parameters:
- `Coords`: Координаты для определения привязки размера
- `Elements`: Элементы, на которых строятся размеры от базы. Первый элемент (база) не должен быть точкой
- `Plane`: Плоская грань или рабочая плоскость для задания ориентации размеров
- `CreatedDimensions`: Список созданных размеров

### `CreateProjected(TFlex.Model.Model3D.Projection)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.CreateProjected(TFlex.Model.Model3D.Projection)`

Создание проекции размера

Parameters:
- `projection`: Проекция, на которую проецируется размер

### `SetElements(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.DimensionUVCoords)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.SetElements(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.DimensionUVCoords)`

Установка привязок размера к 3D элементам

Parameters:
- `Element1`: 1-й элемент размера (грань, ребро, узел)
- `Element1Type`: Тип 1-го элемента размера
- `Element2`: 2-й элемент размера (грань, ребро, узел)
- `Element2Type`: Тип 2-го элемента размера
- `Coords`: Координаты для определения привязки размера

### `SetLeaderNote(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.SetLeaderNote(System.Double,System.Double,System.Double)`

Установка привязок размера по относительным смещениям

Parameters:
- `Offset1`: Смещение размерной линии относительно начала первой выносной линии
- `dX`: Смещение по горизонтали конца выносной полки относительно середины размерной линии
- `dY`: Смещение по вертикали конца выносной полки относительно середины размерной линии

### `SetOffsets(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.SetOffsets(System.Double,System.Double,System.Double)`

Установка привязок размера по относительным смещениям

Parameters:
- `Offset1`: Смещение размерной линии относительно начала первой выносной линии
- `Offset2`: Смещение размерного числа относительно середины размерной линии
- `Offset3`: Смещение - длина полки размера

### `SetOrientationPlane(TFlex.Model.Model3D.Object3D)`

ID: `M:TFlex.Model.Model3D.LinearDimension3D.SetOrientationPlane(TFlex.Model.Model3D.Object3D)`

Установка плоскости ориентации 3D размера

Parameters:
- `Plane`: Плоская грань или рабочая плоскость

## Propertys

### `IsExternal`

ID: `P:TFlex.Model.Model3D.LinearDimension3D.IsExternal`

Управление параметром "Внешний" 3D-размера

Parameters:
- `value`: Значение параметра
