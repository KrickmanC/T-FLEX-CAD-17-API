# TFlex.Model.Model3D.Geometry.SplineData.KnotSequence

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SplineData`

## Summary

Последовательность узлов - значение параметра и кратность

## Remarks

Возможно перечисление узлов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Knot)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Add(TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Knot)`

Добавить узел в конец списка

Parameters:
- `knot`: Узел

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Delete(System.UInt32)`

Удалить узел по номеру

Parameters:
- `index`: Номер узла

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат неопределён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.DeleteAll`

Удалить все узлы

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Knot)`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Knot)`

Вставить узел перед номером

Parameters:
- `Index`: Номер узла, перед которым будет вставлен данный узел
- `knot`: Узел

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат неопределён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.Length`

Количество узлов

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SplineData.KnotSequence.default(System.UInt32)`

Узел по номеру

Parameters:
- `index`: Номер узла

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат неопределён
