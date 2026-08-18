# TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfaceSplineData`

## Summary

Сетка контрольных точек

## Remarks

Каждая строка соответствует изопараметрической кривой по U. Возможно перечисление строк с использованием конструкции foreach

## Methods

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.DeleteAll`

Удалить все контрольные точки

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.Reset`

Сбросить перечислитель

### `SetSize(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.SetSize(System.UInt32,System.UInt32)`

Задать размер решётки

Parameters:
- `row`: Количество строк
- `columns`: Количество столбцов

### `UAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.UAdd`

Добавить строку в конец сетки. Добавить новую изопараметрическую кривую по U с большим значением U

### `UDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.UDelete(System.UInt32)`

Удалить строку. Удалить изопараметрическую кривую по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён

### `UInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.UInsert(System.UInt32)`

Вставить строку. Вставить изопараметрическую кривую по U

Parameters:
- `Index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат неопределён

### `VAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.VAdd`

Добавить столбец в конец сетки. Добавить новую изопараметрическую кривую по V с большим значением V

### `VDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.VDelete(System.UInt32)`

Удалить столбец. Удалить изопараметрическую кривую по V

Parameters:
- `index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат неопределён

### `VInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.VInsert(System.UInt32)`

Вставить столбец. Вставить изопараметрическую кривую по V

Parameters:
- `Index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат неопределён

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.Current`

Получить текущий элемент

### `ULength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.ULength`

Количество строк. Количество изопараметрических кривых по U

### `VLength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.VLength`

Количество столбцов. Количество изопараметрических кривых по V

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplineData.ControlNet.default(System.UInt32)`

Получить строку по номеру. Получить изопараметрическую кривую по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат неопределён
