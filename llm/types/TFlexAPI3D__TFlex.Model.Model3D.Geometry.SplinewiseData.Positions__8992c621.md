# TFlex.Model.Model3D.Geometry.SplinewiseData.Positions

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SplinewiseData`

## Summary

Упорядоченное множество интерполяционных точек - координаты точки и параметр, если используется

## Remarks

Возможно перечисление точек с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Position)`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Add(TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Position)`

Добавить интерполяционную точку в конец списка

Parameters:
- `point`: Интерполяционная точка

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Delete(System.UInt32)`

Удалить интерполяционную по номеру

Parameters:
- `index`: Номер интерполяционной точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.DeleteAll`

Удалить все интерполяционные точки

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Position)`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Position)`

Вставить интерполяционную точку перед номером

Parameters:
- `Index`: Номер интерполяционной точки
- `point`: Координаты точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.Length`

Количество интерполяционных точек

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SplinewiseData.Positions.default(System.UInt32)`

Интерполяционная точка по номеру

Parameters:
- `index`: Номер интерполяционной точки

Remarks: Интерполяционные точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён
