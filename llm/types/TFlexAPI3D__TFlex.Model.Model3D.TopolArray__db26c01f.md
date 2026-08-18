# TFlex.Model.Model3D.TopolArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Множество топологиеских данных

## Remarks

Возможно перечисление топологических элементов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.TopolArray.Add(TFlex.Model.Model3D.Geometry.ModelTopol)`

Добавить элемент в конец списка

Parameters:
- `geom`: Добавляемый элемент

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.TopolArray.Delete(System.Int32)`

Удалить элемент по номеру

Parameters:
- `Index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.TopolArray.DeleteAll`

Удалить все элементы

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.TopolArray.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

ID: `M:TFlex.Model.Model3D.TopolArray.Insert(System.Int32,TFlex.Model.Model3D.Geometry.ModelTopol)`

Вставить элемент перед номером

Parameters:
- `Index`: Номер элемента
- `geom`: Вставляемый элемент

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.TopolArray.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.TopolArray.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.TopolArray.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.TopolArray.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.TopolArray.default(System.Int32)`

Элемент по номеру

Parameters:
- `Index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество элементов, то результат не определён
