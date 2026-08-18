# TFlex.Model.Model3D.Shell.PierceFacesArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Shell`

## Summary

Коллекция удаляемых граней оболочки

## Methods

### `Add(TFlex.Model.Model3D.Geometry.ModelFace)`

ID: `M:TFlex.Model.Model3D.Shell.PierceFacesArray.Add(TFlex.Model.Model3D.Geometry.ModelFace)`

Добавить операнд в конец списка

Parameters:
- `operand`: Добавляемый операнд

### `Clear`

ID: `M:TFlex.Model.Model3D.Shell.PierceFacesArray.Clear`

Удалить все операнды

### `RemoveAt(System.Int32)`

ID: `M:TFlex.Model.Model3D.Shell.PierceFacesArray.RemoveAt(System.Int32)`

Удалить операнд по номеру

Parameters:
- `index`: Номер операции

Remarks: Операнды нумеруются от нуля. Если индекс отрицательный или превышает количество операндов, то результат не определён

## Propertys

### `Count`

ID: `P:TFlex.Model.Model3D.Shell.PierceFacesArray.Count`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.Shell.PierceFacesArray.default(System.Int32)`

Элемент по номеру

Parameters:
- `index`: Номер элемента
