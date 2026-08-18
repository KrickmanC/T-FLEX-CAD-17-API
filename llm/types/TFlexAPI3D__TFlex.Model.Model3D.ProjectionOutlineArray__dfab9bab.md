# TFlex.Model.Model3D.ProjectionOutlineArray

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Множество линий изображения проекции. Возможно перечисление линий с использованием конструкции foreach

## Constructors

### `ProjectionOutlineArray(TFlex.Model.Model3D.Projection)`

ID: `M:TFlex.Model.Model3D.ProjectionOutlineArray.#ctor(TFlex.Model.Model3D.Projection)`

Конструктор итератора по массиву линий проекции

## Methods

### `ProjectionOutlineArray(TFlex.Model.Model3D.Projection)`

ID: `M:TFlex.Model.Model3D.ProjectionOutlineArray.#ctor(TFlex.Model.Model3D.Projection)`

Конструктор итератора по массиву линий проекции

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.ProjectionOutlineArray.GetEnumerator`

Получить перечислитель

### `MoveNext`

ID: `M:TFlex.Model.Model3D.ProjectionOutlineArray.MoveNext`

Перейти к следующему элементу

Returns: Возвращает false если массив исчерпан, true - в противном случае

### `Reset`

ID: `M:TFlex.Model.Model3D.ProjectionOutlineArray.Reset`

Переинициализация итератора - переход на начало массива

## Propertys

### `Current`

ID: `P:TFlex.Model.Model3D.ProjectionOutlineArray.Current`

Текущий элемент массива

### `Item(System.Int32)`

ID: `P:TFlex.Model.Model3D.ProjectionOutlineArray.Item(System.Int32)`

Получить элемент по номеру

Parameters:
- `Index`: Номер элемента

Remarks: Элементы нумеруются от нуля. Если индекс отрицательный или превышает количество точек, то результат неопределён

### `Length`

ID: `P:TFlex.Model.Model3D.ProjectionOutlineArray.Length`

Количество элементов
