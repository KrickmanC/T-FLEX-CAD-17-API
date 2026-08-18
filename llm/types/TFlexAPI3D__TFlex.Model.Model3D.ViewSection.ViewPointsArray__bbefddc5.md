# TFlex.Model.Model3D.ViewSection.ViewPointsArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.ViewSection`

## Summary

Множество точек. Возможно перечисление точек с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.ViewSection.ViewPointsArray.Add(TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Добавить точку в конец списка

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.ViewSection.ViewPointsArray.Delete(System.Int32)`

Удалить точку по номеру

Parameters:
- `Index`: Номер точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.ViewSection.ViewPointsArray.DeleteAll`

Удалить все точки

### `Insert(System.Int32,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

ID: `M:TFlex.Model.Model3D.ViewSection.ViewPointsArray.Insert(System.Int32,TFlex.Model.Model3D.Geometry.ModelPoint3D)`

Вставить точку перед номером

Parameters:
- `Index`: Номер точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

## Propertys

### `Length`

ID: `P:TFlex.Model.Model3D.ViewSection.ViewPointsArray.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.ViewSection.ViewPointsArray.default(System.Int32)`

Получить элемент по номеру

Parameters:
- `Index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён
