# TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfaceSplineData`

## Summary

Последовательность узлов - значение параметра и кратность

## Remarks

Возможно перечисление узлов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Knot)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Add(TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Knot)`

Добавить узел в конец списка

Parameters:
- `knot`: Добавляемый узел

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Delete(System.UInt32)`

Удалить узел по номеру

Parameters:
- `index`: Номер узла

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.DeleteAll`

Удалить все узлы

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.GetEnumerator`

Получить перечислитель

### `Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Knot)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Insert(System.UInt32,TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Knot)`

Вставить узел перед номером

Parameters:
- `Index`: Номер узла
- `knot`: Вставляемый узел

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат неопределён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.Length`

Количество узлов

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.KnotSequence.default(System.UInt32)`

Узел по номеру

Parameters:
- `index`: Номер узла

Remarks: Узлы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат не определён
