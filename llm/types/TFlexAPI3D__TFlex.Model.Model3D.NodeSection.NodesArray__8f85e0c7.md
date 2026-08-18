# TFlex.Model.Model3D.NodeSection.NodesArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.NodeSection`

## Summary

Множество 2D узлов. Возможно перечисление узлов с использованием конструкции foreach

## Methods

### `Add(TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model3D.NodeSection.NodesArray.Add(TFlex.Model.Model2D.Node)`

Добавить узел в конец списка

### `Delete(System.Int32)`

ID: `M:TFlex.Model.Model3D.NodeSection.NodesArray.Delete(System.Int32)`

Удалить узел по номеру

Parameters:
- `Index`: Номер точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

### `DeleteAll`

ID: `M:TFlex.Model.Model3D.NodeSection.NodesArray.DeleteAll`

Удалить все узлы

### `Insert(System.Int32,TFlex.Model.Model2D.Node)`

ID: `M:TFlex.Model.Model3D.NodeSection.NodesArray.Insert(System.Int32,TFlex.Model.Model2D.Node)`

Вставить узел перед номером

Parameters:
- `Index`: Номер точки

Remarks: Точки нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

## Propertys

### `Length`

ID: `P:TFlex.Model.Model3D.NodeSection.NodesArray.Length`

Количество элементов

### `default(System.Int32)`

ID: `P:TFlex.Model.Model3D.NodeSection.NodesArray.default(System.Int32)`

Элемент по номеру

Parameters:
- `Index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество узлов, то результат неопределён
