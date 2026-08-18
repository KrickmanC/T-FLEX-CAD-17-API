# TFlex.Model.Model3D.MassCenterNode3D.OperationsArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.MassCenterNode3D`

## Summary

Множество операций

## Remarks

Возможно перечисление операций с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Add(TFlex.Model.Model3D.Operation)`

Добавить операцию в конец списка

Parameters:
- `operation`: Операция

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Delete(System.Int32)`

Удалить операцию по номеру

Parameters:
- `index`: Номер операции

Remarks: Операции нумеруются от нуля. Если индекс отрицательный или превышает количество операций, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.DeleteAll`

Удалить все операции

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,TFlex.Model.Model3D.Operation)`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Insert(System.Int32,TFlex.Model.Model3D.Operation)`

Вставить операцию перед номером

Parameters:
- `index`: Номер операции
- `operation`: Вставляемая операция

Remarks: Операции нумеруются от нуля. Если индекс отрицательный или превышает количество операций, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.MassCenterNode3D.OperationsArray.Length`

Количество элементов
