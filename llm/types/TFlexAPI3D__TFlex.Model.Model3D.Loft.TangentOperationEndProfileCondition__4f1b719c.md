# TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Loft`

## Summary

Класс для задания касательных условий к профилю берущихся с граней тела

## Constructors

### `TangentOperationEndProfileCondition(TFlex.Model.Model3D.Operation,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition.#ctor(TFlex.Model.Model3D.Operation,TFlex.Model.Parameter)`

Конструктор для создания условий касательных к граням операции

Parameters:
- `magnitude`: Коэффициент граничного условия

Remarks: Формируется набор векторных условий, касательных к профилю и направленных по боковым граням операции. Торцевая грань операции должна прилегать к профилю.

## Methods

### `TangentOperationEndProfileCondition(TFlex.Model.Model3D.Operation,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition.#ctor(TFlex.Model.Model3D.Operation,TFlex.Model.Parameter)`

Конструктор для создания условий касательных к граням операции

Parameters:
- `magnitude`: Коэффициент граничного условия

Remarks: Формируется набор векторных условий, касательных к профилю и направленных по боковым граням операции. Торцевая грань операции должна прилегать к профилю.

## Propertys

### `Magnitude`

ID: `P:TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition.Magnitude`

Получить коэффициент граничного условия

### `Operation`

ID: `P:TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition.Operation`

Получить операцию

### `Type`

ID: `P:TFlex.Model.Model3D.Loft.TangentOperationEndProfileCondition.Type`

Получить тип граничного условия
