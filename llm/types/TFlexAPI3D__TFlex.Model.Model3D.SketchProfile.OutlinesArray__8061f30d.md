# TFlex.Model.Model3D.SketchProfile.OutlinesArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.SketchProfile`

## Summary

Множество линий изображения

## Remarks

Возможно перечисление элементов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model2D.Outline)`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.Add(TFlex.Model.Model2D.Outline)`

Добавить линию изображения в конец списка

Parameters:
- `outline`: Добавляемая линия изображения

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.Delete(System.Int32)`

Удалить линию изображения по номеру

Parameters:
- `index`: Номер линии изображения

Remarks: Линии изображения нумеруются от нуля. Если индекс отрицательный или превышает количество линий изображения, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.DeleteAll`

Удалить все линии изображения

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.MoveNext`

Перейти к следующей линии изображения

### `Reset`

ID: `M:TFlex.Model.Model3D.SketchProfile.OutlinesArray.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.SketchProfile.OutlinesArray.Current`

Получить текущую линию изображения

### `Length`

ID: `P:TFlex.Model.Model3D.SketchProfile.OutlinesArray.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.SketchProfile.OutlinesArray.default(System.Int32)`

Линия изображения по номеру

Parameters:
- `index`: Номер линии изображения

Remarks: Линии изображения нумеруются от нуля. Если индекс отрицательный или превышает количество линий изображения, то результат не определён
