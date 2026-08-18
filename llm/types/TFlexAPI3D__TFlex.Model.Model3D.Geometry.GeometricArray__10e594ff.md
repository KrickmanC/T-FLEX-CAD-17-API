# TFlex.Model.Model3D.Geometry.GeometricArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Множество геометрических данных

## Remarks

Возможно перечисление элементов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.Geometry)`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.Add(TFlex.Model.Model3D.Geometry.Geometry)`

Добавить элемент в конец списка

Parameters:
- `geom`: Добавляемый элемент

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.Delete(System.Int32)`

Удалить элемент по номеру

Parameters:
- `index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.DeleteAll`

Удалить все элементы

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,TFlex.Model.Model3D.Geometry.Geometry)`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.Insert(System.Int32,TFlex.Model.Model3D.Geometry.Geometry)`

Вставить элемент перед номером

Parameters:
- `index`: Номер элемента
- `geom`: Элемент

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.GeometricArray.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.GeometricArray.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.GeometricArray.Length`

Количество элементов
