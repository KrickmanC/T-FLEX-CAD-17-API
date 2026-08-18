# TFlex.Model.Model3D.PipePath3D.BaseSegment

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.PipePath3D`

## Summary

Базовый класс участок пути

## Methods

### `Equal(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.Equal(TFlex.Model.Model3D.PipePath3D.BaseSegment)`

Сравнить два сегмента

Remarks: Если оба объекта представляют одну и туже сущность (участок пути) вернет "истину"

### `IsBeginTangentPossible(System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.IsBeginTangentPossible(System.Boolean)`

Возможность касательной в начале участка

### `IsEndTangentPossible(System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.IsEndTangentPossible(System.Boolean)`

Возможность касательной в конце участка

### `RemovePoint(System.Int32)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.RemovePoint(System.Int32)`

Удалить точку по индексу

Remarks: Индекс indexPoint должен лежать в интервале от 0 до CountPoints

### `RemovePoint(TFlex.Model.Model3D.PipePath3D.BasePoint)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.RemovePoint(TFlex.Model.Model3D.PipePath3D.BasePoint)`

Удалить точку

### `SetBeginTangent(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.SetBeginTangent(System.Boolean,System.Boolean)`

Управление касательной в начале участка

### `SetBeginTangent(System.Double,System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.SetBeginTangent(System.Double,System.Boolean)`

Управление акмплитудой касательной в начале участка

### `SetEndTangent(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.SetEndTangent(System.Boolean,System.Boolean)`

Управление касательной в конце участка

### `SetEndTangent(System.Double,System.Boolean)`

ID: `M:TFlex.Model.Model3D.PipePath3D.BaseSegment.SetEndTangent(System.Double,System.Boolean)`

Управление акмплитудой касательной в конце участка

## Propertys

### `CountPoints`

ID: `P:TFlex.Model.Model3D.PipePath3D.BaseSegment.CountPoints`

Количество точке в участке

### `Reverse`

ID: `P:TFlex.Model.Model3D.PipePath3D.BaseSegment.Reverse`

Разворачивает участок пути

### `Type`

ID: `P:TFlex.Model.Model3D.PipePath3D.BaseSegment.Type`

Тип участка пути
