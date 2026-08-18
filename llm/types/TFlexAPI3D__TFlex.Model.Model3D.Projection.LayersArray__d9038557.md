# TFlex.Model.Model3D.Projection.LayersArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Projection`

## Summary

Множество слоёв

## Remarks

Возможно перечисление слоёв с использованием конструкции foreach

## Methods

### `Add(System.String)`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.Add(System.String)`

Добавить слой в конец списка

Parameters:
- `layer`: Слой

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.Delete(System.Int32)`

Удалить слой по номеру

Parameters:
- `index`: Номер слоя

Remarks: Слои нумеруются от нуля. Если индекс отрицательный или превышает количество слоёв, то результат не определён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.DeleteAll`

Удалить все слои

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.GetEnumerator`

Получить перечислитель

### `Insert(System.Int32,System.String)`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.Insert(System.Int32,System.String)`

Вставить слой перед номером

Parameters:
- `index`: Номер слоя
- `layer`: Вставляемый слой

Remarks: Слои нумеруются от нуля. Если индекс отрицательный или превышает количество слоёв, то результат не определён

### `MoveNext`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.MoveNext`

Перейти к следующему элементу

### `Reset`

ID: `M:TFlex.Model.Model3D.Projection.LayersArray.Reset`

Сбросить перечислитель

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.Projection.LayersArray.Current`

Получить текущий элемент

### `Length`

ID: `P:TFlex.Model.Model3D.Projection.LayersArray.Length`

Количество слоёв
