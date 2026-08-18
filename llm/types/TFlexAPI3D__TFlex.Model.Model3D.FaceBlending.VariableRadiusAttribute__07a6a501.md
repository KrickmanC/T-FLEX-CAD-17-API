# TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.FaceBlending`

## Summary

Класс свойств используемый для создания сглаживания с переменным радиусом

## Constructors

### `VariableRadiusAttribute(TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.#ctor(TFlex.Model.Model3D.FaceBlending.PositionData)`

Конструктор

Parameters:
- `data`: Параметры переменного сглаживания в начальной и конечной позиции

### `VariableRadiusAttribute(TFlex.Model.Model3D.FaceBlending.PositionData,TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.#ctor(TFlex.Model.Model3D.FaceBlending.PositionData,TFlex.Model.Model3D.FaceBlending.PositionData)`

Конструктор

Parameters:
- `first`: Параметры переменного сглаживания в начальной позиции
- `last`: Параметры переменного сглаживания в конечной позиции

## Methods

### `VariableRadiusAttribute(TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.#ctor(TFlex.Model.Model3D.FaceBlending.PositionData)`

Конструктор

Parameters:
- `data`: Параметры переменного сглаживания в начальной и конечной позиции

### `VariableRadiusAttribute(TFlex.Model.Model3D.FaceBlending.PositionData,TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.#ctor(TFlex.Model.Model3D.FaceBlending.PositionData,TFlex.Model.Model3D.FaceBlending.PositionData)`

Конструктор

Parameters:
- `first`: Параметры переменного сглаживания в начальной позиции
- `last`: Параметры переменного сглаживания в конечной позиции

### `AddPosition(TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.AddPosition(TFlex.Model.Model3D.FaceBlending.PositionData)`

Добавить позицию

Parameters:
- `data`: Параметры заданные в позиции

Returns: Номер добавленной позиции

Remarks: Всегда существуют две позиции со значениями 0 и 100. Позиции всегда располагаются в порядке возрастания значения, добавление новых позиций может привести к изменению порядкового индекса ранее добавленных позиций

### `GetPosition(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.GetPosition(System.Int32)`

Удалить позицию

Parameters:
- `positionIndex`: Номер позиции, должен быть в диапазоне 1..последняя позиция-1

Returns: Новый номер позиции

### `RemovePosition(System.Int32)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.RemovePosition(System.Int32)`

Удалить позицию

Parameters:
- `positionIndex`: Номер позиции, должен быть в диапазоне 1..последняя позиция-1

Remarks: Первая и последняя позиции не могут быть удалены

### `SetPosition(System.Int32,TFlex.Model.Model3D.FaceBlending.PositionData)`

ID: `M:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.SetPosition(System.Int32,TFlex.Model.Model3D.FaceBlending.PositionData)`

Удалить позицию

Parameters:
- `positionIndex`: Номер позиции, должен быть в диапазоне 1..последняя позиция-1
- `data`: Параметры заданные в позиции

Returns: Новый номер позиции

## Propertys

### `PositionCount`

ID: `P:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.PositionCount`

Число позиций

Remarks: Число позиций всегда больше или равно 2

### `ShapeMethod`

ID: `P:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.ShapeMethod`

Тип поверхности

### `Type`

ID: `P:TFlex.Model.Model3D.FaceBlending.VariableRadiusAttribute.Type`

Получить тип атрибута
