# TFlex.Model.Model3D.PipePath3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Класс пути трубопровода

## Methods

### `AddBackSegment``1(TFlex.Model.Model3D.SegmentPipePathType)`

ID: `M:TFlex.Model.Model3D.PipePath3D.AddBackSegment``1(TFlex.Model.Model3D.SegmentPipePathType)`

Добавить участок в конец

### `AddFrontSegment``1(TFlex.Model.Model3D.SegmentPipePathType)`

ID: `M:TFlex.Model.Model3D.PipePath3D.AddFrontSegment``1(TFlex.Model.Model3D.SegmentPipePathType)`

Добавить участок в начало

### `AddSegment_back``1(TFlex.Model.Model3D.SegmentPipePathType)`

ID: `M:TFlex.Model.Model3D.PipePath3D.AddSegment_back``1(TFlex.Model.Model3D.SegmentPipePathType)`

Добавить участок в конец

### `AddSegment_front``1(TFlex.Model.Model3D.SegmentPipePathType)`

ID: `M:TFlex.Model.Model3D.PipePath3D.AddSegment_front``1(TFlex.Model.Model3D.SegmentPipePathType)`

Добавить участок в начало

### `BeginEdit`

ID: `M:TFlex.Model.Model3D.PipePath3D.BeginEdit`

Подготавливает объект к редактированию

### `EndEdit`

ID: `M:TFlex.Model.Model3D.PipePath3D.EndEdit`

Закончить редактирование объекта

### `GetBeginSegment`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetBeginSegment`

Получить первый участок

Remarks: Возвращаемое значение необходимо преобразовать к соответствующему типу сегмента

### `GetEndPoint`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetEndPoint`

Получить объект которым заканчивается путь

### `GetEndSegment`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetEndSegment`

Получить последний участок

Remarks: Возвращаемое значение необходимо преобразовать к соответствующему типу сегмента

### `GetNextSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetNextSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

Получить следующий участок

Remarks: Возвращаемое значение необходимо преобразовать к соответствующему типу сегмента

### `GetPrevSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetPrevSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

Получить предыдущий участок

Remarks: Возвращаемое значение необходимо преобразовать к соответствующему типу сегмента

### `GetSegment(System.Int32)`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetSegment(System.Int32)`

Получить участок

Remarks: Индекс indexSegment должен лежат в интервале от 0 до CountSegments. Возвращаемое значение необходимо преобразовать к соответствующему типу сегмента.

### `GetStartPoint`

ID: `M:TFlex.Model.Model3D.PipePath3D.GetStartPoint`

Получить объект с которого начинается путь

### `MakeSmoothness`

ID: `M:TFlex.Model.Model3D.PipePath3D.MakeSmoothness`

Делает сглаживание

Remarks: Создает гладкие межсегментные участки

### `RemoveSegment(System.Int32)`

ID: `M:TFlex.Model.Model3D.PipePath3D.RemoveSegment(System.Int32)`

Удалить участок по индексу

Remarks: Индекс indexSegment должен лежат в интервале от 0 до CountSegments

### `RemoveSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

ID: `M:TFlex.Model.Model3D.PipePath3D.RemoveSegment(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

Удалить участок

## Propertys

### `CountSegments`

ID: `P:TFlex.Model.Model3D.PipePath3D.CountSegments`

Возвращает количество участков

### `Smoothness`

ID: `P:TFlex.Model.Model3D.PipePath3D.Smoothness`

Управляет сглаживанием

Remarks: После установки сглаживания выполнить MakeSmoothness

### `Tube`

ID: `P:TFlex.Model.Model3D.PipePath3D.Tube`

Управляет опцией трубы

Remarks: Использовать совместно с TubeRadius. Используется только в режиме пользовательского редактирования

### `TubeRadius`

ID: `P:TFlex.Model.Model3D.PipePath3D.TubeRadius`

Управляет радиусом трубы

Remarks: Используется только в режиме пользовательского редактирования
