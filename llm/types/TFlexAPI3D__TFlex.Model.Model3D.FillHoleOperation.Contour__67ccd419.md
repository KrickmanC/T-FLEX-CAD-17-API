# TFlex.Model.Model3D.FillHoleOperation.Contour

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.FillHoleOperation`

## Summary

Класс контура

## Methods

### `AddElement(TFlex.Model.Model3D.Geometry.ModelWire)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.AddElement(TFlex.Model.Model3D.Geometry.ModelWire)`

Добавить элемент в контур

### `CountElements`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.CountElements`

Количество элементов в контуре

### `GetElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.GetElement(System.Int32)`

Получить элемент из контура

Parameters:
- `index`: Индекс получаемого элемента (начинается с 0)

### `GetSmoothnessElementType(System.Int32)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.GetSmoothnessElementType(System.Int32)`

Получить граничное условие для ребра

Parameters:
- `index`: Индекс получаемого элемента (начинается с 0)

### `RemoveElement(System.Int32)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.RemoveElement(System.Int32)`

Удалить элемент

Parameters:
- `index`: Индекс удаляемого элемента (начинается с 0)

### `SetSmoothnessElementType(System.Int32,TFlex.Model.Model3D.FillHoleOperation.SmoothnessType)`

ID: `M:TFlex.Model.Model3D.FillHoleOperation.Contour.SetSmoothnessElementType(System.Int32,TFlex.Model.Model3D.FillHoleOperation.SmoothnessType)`

Установить граничное условие для ребра

Parameters:
- `index`: Индекс получаемого элемента (начинается с 0)

## Propertys

### `Form`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.Contour.Form`

Форма

### `Method`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.Contour.Method`

Метод

### `Smoothness`

ID: `P:TFlex.Model.Model3D.FillHoleOperation.Contour.Smoothness`

Гладкость
