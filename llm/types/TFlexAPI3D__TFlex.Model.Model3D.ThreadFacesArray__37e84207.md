# TFlex.Model.Model3D.ThreadFacesArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Коллекция граней на которые накладывается резьба

## Methods

### `Add(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.Add(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить операнд в конец списка

Parameters:
- `item`: Добавляемый операнд

### `Clear`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.Clear`

Удалить все операнды

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.GetEnumerator`

Вернуть перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.MoveNext`

Перейти к следующему элементу

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.RemoveAt(System.Int32)`

Удалить операнд по номеру

Parameters:
- `index`: Номер операции

Remarks: Операнды нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён

### `Reset`

ID: `M:TFlex.Model.Model3D.ThreadFacesArray.Reset`

Сбросить перечислитель

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.ThreadFacesArray.Count`

Количество элементов

### `Current`

ID: `P:TFlex.Model.Model3D.ThreadFacesArray.Current`

Вернуть текущий элемент

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.ThreadFacesArray.default(System.Int32)`

Элемент по номеру

Parameters:
- `index`: Номер элемента
