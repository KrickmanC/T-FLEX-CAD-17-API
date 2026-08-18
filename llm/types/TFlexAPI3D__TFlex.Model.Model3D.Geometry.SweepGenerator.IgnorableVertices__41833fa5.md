# TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SweepGenerator`

## Summary

Класс хранения множества игнорируемых вершин траектории. Возможно перечисление вершин с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.Vertex)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.Add(TFlex.Model.Model3D.Geometry.Vertex)`

Добавить вершину

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.Delete(System.UInt32)`

Удалить вершину

Parameters:
- `index`: Номер вершины

Remarks: Вершины нумеруются от нуля. Если индекс отрицательный или превышает количество вершин, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.DeleteAll`

Удалить все вершины

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.Length`

Количество вершин

### `default(System.UInt32)`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.IgnorableVertices.default(System.UInt32)`

Вершина по номеру

Parameters:
- `index`: Номер вершины

Remarks: Вершины нумеруются от нуля. Если индекс отрицательный или превышает количество вершин, то результат не определён
