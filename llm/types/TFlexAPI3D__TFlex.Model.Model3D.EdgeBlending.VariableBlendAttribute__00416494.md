# TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.EdgeBlending`

## Summary

Класс для задания свойств с переменным радиусом скругления

## Remarks

VariableBlendAttribute является временным объектом используемым для облегчения задания свойств операции сглаживания

## Constructors

### `VariableBlendAttribute(TFlex.Model.Model3D.EdgeBlending.PositionData,TFlex.Model.Model3D.EdgeBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Model3D.EdgeBlending.PositionData,TFlex.Model.Model3D.EdgeBlending.PositionData)`

Конструктор

Parameters:
- `first`: Параметры первой позиции
- `last`: Параметры второй позиции

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й радиус эллипса
- `radius2`: 2-й радиус эллипса

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола
- `setbackStart`: Отступ от начала ребра
- `setbackEnd`: Отступ от конца ребра

## Methods

### `VariableBlendAttribute(TFlex.Model.Model3D.EdgeBlending.PositionData,TFlex.Model.Model3D.EdgeBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Model3D.EdgeBlending.PositionData,TFlex.Model.Model3D.EdgeBlending.PositionData)`

Конструктор

Parameters:
- `first`: Параметры первой позиции
- `last`: Параметры второй позиции

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й радиус эллипса
- `radius2`: 2-й радиус эллипса

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола

### `VariableBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius1`: 1-й параметр
- `radius2`: 2-й параметр
- `rho`: Параметр задающий кривизну: меньше 0.5 - эллипс, 0.5 - парабола, больше 0.5 - гипербола
- `setbackStart`: Отступ от начала ребра
- `setbackEnd`: Отступ от конца ребра

### `AddPosition(TFlex.Model.Model3D.EdgeBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.AddPosition(TFlex.Model.Model3D.EdgeBlending.PositionData)`

Добавить позицию

Parameters:
- `data`: Данные позиции

### `GetPosition(System.Int32)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.GetPosition(System.Int32)`

Добавить позицию

Remarks: Удаляет позиции с номерами 1..PositionCount-2

### `RemoveAllPositions`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.RemoveAllPositions`

Добавить позицию

Remarks: Удаляет позиции с номерами 1..PositionCount-2

### `RemovePosition(System.Int32)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.RemovePosition(System.Int32)`

Добавить позицию

Parameters:
- `positionIndex`: Номер позиции, должен быть в диапазоне 1..PositionCount-2

Remarks: Первая и последняя позиции не могут быть удалены

### `SetPosition(System.Int32,TFlex.Model.Model3D.EdgeBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.SetPosition(System.Int32,TFlex.Model.Model3D.EdgeBlending.PositionData)`

Установить данные позиции

Parameters:
- `positionIndex`: Номер позиции
- `data`: Новые данные позиции

## Propertys

### `PositionCount`

ID: `P:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.PositionCount`

Число позиций

### `SetbackEnd`

ID: `P:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.SetbackEnd`

Отступ от конца ребра

### `SetbackStart`

ID: `P:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.SetbackStart`

Отступ от начала ребра

### `Type`

ID: `P:TFlex.Model.Model3D.EdgeBlending.VariableBlendAttribute.Type`

Тип свойства
