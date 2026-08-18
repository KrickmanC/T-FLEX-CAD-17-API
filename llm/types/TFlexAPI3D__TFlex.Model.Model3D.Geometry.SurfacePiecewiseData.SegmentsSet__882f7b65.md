# TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SurfacePiecewiseData`

## Summary

Сетка сегментов. Упорядоченное по U множество строк сегментов

## Remarks

Возможно перечисление строк с использованием конструкции foreach

## Methods

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.DeleteAll`

Удалить все сегменты

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.Reset`

Сбросить перечислитель

### `SetSize(System.UInt32,System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.SetSize(System.UInt32,System.UInt32)`

Задать размер решётки

Parameters:
- `row`: Количество строк. Количество сегментов по U
- `columns`: Количество столбцов. Количество сегментов по V

### `UAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.UAdd`

Добавить строку в конец сетки

Remarks: Добавить новые сегменты по U с большим значением U

### `UDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.UDelete(System.UInt32)`

Удалить строку. Удалить сегменты по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён

### `UInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.UInsert(System.UInt32)`

Вставить строку. Вставить сегменты по U

Parameters:
- `Index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён

### `VAdd`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.VAdd`

Добавить столбец в конец сетки

Remarks: Добавить новые сегменты по V с большим значением V

### `VDelete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.VDelete(System.UInt32)`

Удалить столбец. Удалить сегменты по V

Parameters:
- `index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат не определён

### `VInsert(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.VInsert(System.UInt32)`

Вставить столбец. Вставить сегменты по V

Parameters:
- `Index`: Номер столбца

Remarks: Столбцы нумеруются от нуля. Если индекс отрицательный или превышает количество столбцов, то результат не определён

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.Current`

Получить текущий элемент

### `ULength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.ULength`

Количество строк. Количество сегментов по U

### `VLength`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.VLength`

Количество столбцов. Количество сегментов по V

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SurfacePiecewiseData.SegmentsSet.default(System.UInt32)`

Получить строку по номеру. Получить сегменты по U

Parameters:
- `index`: Номер строки

Remarks: Строки нумеруются от нуля. Если индекс отрицательный или превышает количество строк, то результат не определён
