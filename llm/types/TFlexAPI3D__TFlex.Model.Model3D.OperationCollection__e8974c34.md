# TFlex.Model.Model3D.OperationCollection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Коллекция операций

## Methods

### `Add(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.OperationCollection.Add(TFlex.Model.Model3D.Operation)`

Добавить операнд в конец списка

Parameters:
- `operand`: Добавляемый операнд

### `Clear`

ID: `M:TFlex.Model.Model3D.OperationCollection.Clear`

Удалить все операнды

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.OperationCollection.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.OperationCollection.MoveNext`

Перейти к следующему операнду

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.OperationCollection.RemoveAt(System.Int32)`

Удалить операнд по номеру

Parameters:
- `index`: Номер операнда

Remarks: Операнды нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён

### `Reset`

ID: `M:TFlex.Model.Model3D.OperationCollection.Reset`

Сбросить перечислитель

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.OperationCollection.Count`

Количество элементов

### `Current`

ID: `P:TFlex.Model.Model3D.OperationCollection.Current`

Получить текущий операнд

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.OperationCollection.default(System.Int32)`

Элемент по номеру

Parameters:
- `index`: Номер элемента
