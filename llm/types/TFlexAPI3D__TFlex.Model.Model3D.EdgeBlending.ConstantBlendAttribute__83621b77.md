# TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.EdgeBlending`

## Summary

Класс для задания свойств с постоянным радиусом скругления

## Remarks

ConstantBlendAttribute является временным объектом используемым для облегчения задания свойств операции сглаживания

## Constructors

### `ConstantBlendAttribute(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.#ctor(TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius`: Радиус скругления

### `ConstantBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius`: Радиус скругления
- `setbackStart`: Параметр используемый для задания чемоданного угла от начала ребра, может быть равен 0
- `setbackEnd`: Параметр используемый для задания чемоданного угла от конца ребра, может быть равен 0

## Methods

### `ConstantBlendAttribute(TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.#ctor(TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius`: Радиус скругления

### `ConstantBlendAttribute(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.#ctor(TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Конструктор

Parameters:
- `radius`: Радиус скругления
- `setbackStart`: Параметр используемый для задания чемоданного угла от начала ребра, может быть равен 0
- `setbackEnd`: Параметр используемый для задания чемоданного угла от конца ребра, может быть равен 0

## Propertys

### `Radius`

ID: `P:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.Radius`

Получить значение радиуса

### `SetbackEnd`

ID: `P:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.SetbackEnd`

Получить значение отступа от конца ребра

### `SetbackStart`

ID: `P:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.SetbackStart`

Получить значение отступа от начала ребра

### `Type`

ID: `P:TFlex.Model.Model3D.EdgeBlending.ConstantBlendAttribute.Type`

Тип свойств ребра
