# TFlex.Model.Model3D.Geometry.FacetMesh

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Множество треугольников

## Remarks

Возможно перечисление треугольников с использованием конструкции foreach

## Methods

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Geometry.FacetMesh.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Geometry.FacetMesh.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Geometry.FacetMesh.Reset`

Сбросить перечислитель

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.Geometry.FacetMesh.Count`

Количество треугольников

### `Current`

ID: `P:TFlex.Model.Model3D.Geometry.FacetMesh.Current`

Получить текущий элемент

### `Max`

ID: `P:TFlex.Model.Model3D.Geometry.FacetMesh.Max`

Максимальная точка

### `Min`

ID: `P:TFlex.Model.Model3D.Geometry.FacetMesh.Min`

Минимальная точка

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.Geometry.FacetMesh.default(System.Int32)`

Получить грань по номеру

Parameters:
- `Index`: Номер грани

Remarks: Грани нумеруются от нуля. Если индекс отрицательный или превышает количество граней, то результат не определён
