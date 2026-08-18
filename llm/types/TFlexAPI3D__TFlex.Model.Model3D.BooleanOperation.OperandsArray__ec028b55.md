# TFlex.Model.Model3D.BooleanOperation.OperandsArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.BooleanOperation`

## Summary

Операнды

## Methods

### `Add(TFlex.Model.Model3D.BooleanOperation.OperandsArray.Operand)`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.Add(TFlex.Model.Model3D.BooleanOperation.OperandsArray.Operand)`

Добавить операнд в конец списка

Parameters:
- `operand`: Добавляемый операнд

### `Clear`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.Clear`

Удалить все операнды

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.MoveNext`

Перейти к следующему элементу

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.RemoveAt(System.Int32)`

Удалить операнд по номеру

Parameters:
- `index`: Номер операции

Remarks: Операнды нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён

### `Reset`

ID: `M:TFlex.Model.Model3D.BooleanOperation.OperandsArray.Reset`

Сбросить перечислитель

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.BooleanOperation.OperandsArray.Count`

Количество элементов

### `Current`

ID: `P:TFlex.Model.Model3D.BooleanOperation.OperandsArray.Current`

Получить текущий элемент

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.BooleanOperation.OperandsArray.default(System.Int32)`

Получить элемент по номеру

Parameters:
- `index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён
