# TFlex.PickPointResult

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Выходные параметры метода PickPoint

## Propertys

### `IsOK`

ID: `P:TFlex.PickPointResult.IsOK`

Признак успешного завершения выбора точки или объекта. Если данный параметр равен false, то макрос или команда, вызвавшая метод PickPoint должен завершить работу. Иначе возможны сбои в работе системы.

### `Key`

ID: `P:TFlex.PickPointResult.Key`

Код клавиши, которая была нажата пользователем

Remarks: В случае нажатия левой кнопки мыши возвращается KeyKode.keyENTER. В случае нажатия правой кнопки мыши возвращается KeyKode.keyESCAPE. В последнем случае метод IsOK возвращает false.

### `ModelPoint`

ID: `P:TFlex.PickPointResult.ModelPoint`

Выбранная точка в системе координат модели, с учётом масштаба текущей страницы

Remarks: Данный параметр имеет смысл только в случае выбора точки в 2D виде или в 3D виде в режиме активизации страницы рабочей плоскости.

### `PaperPoint`

ID: `P:TFlex.PickPointResult.PaperPoint`

Выбранная точка в системе координат бумаги, без учёта масштаба текущей страницы

Remarks: Данный параметр имеет смысл только в случае выбора точки в 2D виде или в 3D виде в режиме активизации страницы рабочей плоскости.

### `Point`

ID: `P:TFlex.PickPointResult.Point`

Выбранная точка

### `SelectedObject`

ID: `P:TFlex.PickPointResult.SelectedObject`

Объект документа, который был выбран в процессе ввода точки

Remarks: При нулевом значении данного свойства пользователь просто указал точку

### `View`

ID: `P:TFlex.PickPointResult.View`

Вид документа, в котором был произведён ввод точки

### `X`

ID: `P:TFlex.PickPointResult.X`

Координата X выбранной точки

### `Y`

ID: `P:TFlex.PickPointResult.Y`

Координата Y выбранной точки
