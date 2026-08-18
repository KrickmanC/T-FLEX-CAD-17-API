# TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.BodyGenerator`

## Summary

Множество результирующих тел. Возможно перечисление тел с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.Geometry.BodyGenerator.ResultBodies.default(System.Int32)`

Получить тело по номеру

Parameters:
- `index`: Номер тела

Remarks: Тела нумеруются от нуля. Если индекс отрицательный или превышает количество тел, то результат не определён
