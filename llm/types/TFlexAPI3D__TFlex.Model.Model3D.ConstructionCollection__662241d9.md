# TFlex.Model.Model3D.ConstructionCollection

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Коллекция элементов построения

## Remarks

В целом, похоже на OperationCollection

## Methods

### `Add(TFlex.Model.Model3D.Construction3D)`

ID: `M:TFlex.Model.Model3D.ConstructionCollection.Add(TFlex.Model.Model3D.Construction3D)`

Добавить операнд в конец списка

Parameters:
- `operand`: Добавляемый операнд

### `Clear`

ID: `M:TFlex.Model.Model3D.ConstructionCollection.Clear`

Удалить все операнды

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.ConstructionCollection.GetEnumerator`

Получить перечислитель

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.ConstructionCollection.RemoveAt(System.Int32)`

Удалить операнд по номеру

Parameters:
- `index`: Номер операнда

Remarks: Операнды нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.ConstructionCollection.Count`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.ConstructionCollection.default(System.Int32)`

Элемент по номеру

Parameters:
- `index`: Номер элемента
