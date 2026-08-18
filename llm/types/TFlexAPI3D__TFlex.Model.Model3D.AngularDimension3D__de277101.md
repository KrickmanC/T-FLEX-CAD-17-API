# TFlex.Model.Model3D.AngularDimension3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Угловой размер на 3D

## Constructors

### `AngularDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ углового размера

## Methods

### `AngularDimension3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `Doc`: Документ углового размера

### `CreateProjected(TFlex.Model.Model3D.Projection)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.CreateProjected(TFlex.Model.Model3D.Projection)`

Создание проекции размера

Parameters:
- `projection`: Проекция, на которую проецируется размер

### `SetElements(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.DimensionUVCoords)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.SetElements(TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.Object3D,TFlex.Model.Model3D.Dimension3DElementType,TFlex.Model.Model3D.DimensionUVCoords)`

Установка привязок размера к 3D элементам

Parameters:
- `Element1`: 1-й элемент размера (грань, ребро, узел)
- `Element1Type`: Тип 1-го элемента размера
- `Element2`: 2-й элемент размера (грань, ребро, узел)
- `Element2Type`: Тип 2-го элемента размера
- `Coords`: Координаты для определения привязки размера

### `SetLeaderNote(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.SetLeaderNote(System.Double,System.Double,System.Double)`

Установка привязок размера по относительным смещениям

Parameters:
- `Offset1`: Смещение размерной линии относительно начала первой выносной линии
- `dX`: Смещение по горизонтали конца выносной полки относительно середины размерной линии
- `dY`: Смещение по вертикали конца выносной полки относительно середины размерной линии

### `SetOffsets(System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.AngularDimension3D.SetOffsets(System.Double,System.Double,System.Double)`

Установка привязок размера по относительным смещениям

Parameters:
- `Offset1`: Смещение размерной линии относительно начала первой выносной линии
- `Offset2`: Смещение размерного числа относительно середины размерной линии
- `Offset3`: Смещение - длина полки размера

## Propertys

### `IsExternal`

ID: `P:TFlex.Model.Model3D.AngularDimension3D.IsExternal`

Управление параметром "Внешний" 3D-размера

Parameters:
- `value`: Значение параметра

### `SubType`

ID: `P:TFlex.Model.Model3D.AngularDimension3D.SubType`

Подтип размера
