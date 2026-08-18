# TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData`

## Summary

Сетка интерполяционных точек. Каждая строка соответствует изопараметрической кривой по U

## Remarks

Возможно перечисление строк с использованием конструкции foreach

## Methods

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.DeleteAll`

Удалить все интерполяционные точки

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.Reset`

Сбросить перечислитель

### `SetSize(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.SetSize(System.UInt32,System.UInt32)`

Задать размер решётки

Parameters:
- `row`: Количество строк
- `columns`: Количество столбцов

### `UAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.UAdd`

Добавить строку в конец сетки

Remarks: Добавить новую изопараметрическую кривую по U с большим значением U

### `UDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.UDelete(System.UInt32)`

Удалить строку. Удалить изопараметрическую кривую по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён

### `UInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.UInsert(System.UInt32)`

Вставить строку. Вставить изопараметрическую кривую по U

Parameters:
- `Index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён

### `VAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.VAdd`

Добавить столбец в конец сетки

Remarks: Добавить новую изопараметрическую кривую по V с большим значением V

### `VDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.VDelete(System.UInt32)`

Удалить столбец. Удалить изопараметрическую кривую по V

Parameters:
- `index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат не определён

### `VInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.VInsert(System.UInt32)`

Вставить столбец. Вставить изопараметрическую кривую по V

Parameters:
- `Index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат не определён

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.Current`

Получить текущий элемент

### `ULength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.ULength`

Количество строк. Количество изопараметрических кривых по U

### `VLength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.VLength`

Количество столбцов. Количество изопараметрических кривых по V

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfaceSplinewiseData.Positions.default(System.UInt32)`

Получить строку по номеру. Получить изопараметрическую кривую по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён
