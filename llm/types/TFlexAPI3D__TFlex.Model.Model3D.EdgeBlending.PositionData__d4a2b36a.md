# TFlex.Model.Model3D.EdgeBlending.PositionData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.EdgeBlending`

## Summary

Класс используемый для задания данных позиций в переменном сглаживании

## Remarks

VariableBlendAttribute является временным объектом используемым для облегчения задания свойств операции сглаживания

## Constructors

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius`: Радиус окружности

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius1`: 1-й радиус эллипса
- `radius2`: 2-й радиус эллипса

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну кривой: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола

## Methods

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius`: Радиус окружности

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius1`: 1-й радиус эллипса
- `radius2`: 2-й радиус эллипса

### `PositionData(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.PositionData.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `position`: Позиция, задаётся в диапазоне 0..100
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну кривой: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола

## Propertys

### `Position`

ID: `P:TFlex.Model.Model3D.EdgeBlending.PositionData.Position`

Позиция

### `Radius1`

ID: `P:TFlex.Model.Model3D.EdgeBlending.PositionData.Radius1`

Первый радиус

### `Radius2`

ID: `P:TFlex.Model.Model3D.EdgeBlending.PositionData.Radius2`

Второй радиус

### `Rho`

ID: `P:TFlex.Model.Model3D.EdgeBlending.PositionData.Rho`

Кривизна
