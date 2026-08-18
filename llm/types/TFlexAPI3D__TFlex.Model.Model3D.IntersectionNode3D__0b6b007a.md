# TFlex.Model.Model3D.IntersectionNode3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Узел на пересечении элементов

## Constructors

### `IntersectionNode3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.IntersectionNode3D.#ctor(TFlex.Model.Document)`

Конструктор для создания узла на пересечении элементов

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `IntersectionNode3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.IntersectionNode3D.#ctor(TFlex.Model.Document)`

Конструктор для создания узла на пересечении элементов

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Propertys

### `FirstAxis`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.FirstAxis`

Первый элемент как ось

Remarks: В качестве первого элемента можно задавать или проволочную модель или ось

### `FirstWire`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.FirstWire`

Первый элемент как проволочная модель

Remarks: В качестве первого элемента можно задавать или проволочную модель или ось

### `Number`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.Number`

Получить номер пересечения

Remarks: В некоторых случаях может быть несколько пересечений и возможно явно задать номер пересечения

### `SecondAxis`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.SecondAxis`

Второй элемент как ось

Remarks: В качестве второго элемента можно задавать или проволочную модель, или ось, или солид, или листовое тело

### `SecondPlane`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.SecondPlane`

Второй элемент как листовое тело

Remarks: В качестве второго элемента можно задавать или проволочную модель, или ось, или солид, или листовое тело

### `SecondSheet`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.SecondSheet`

Второй элемент как листовое тело

Remarks: В качестве второго элемента можно задавать или проволочную модель, или ось, или солид, или листовое тело

### `SecondSolid`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.SecondSolid`

Второй элемент как твёрдое тело

Remarks: В качестве второго элемента можно задавать или проволочную модель, или ось, или солид, или листовое тело

### `SecondWire`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.SecondWire`

Второй элемент как проволочная модель

Remarks: В качестве второго элемента можно задавать или проволочную модель, или ось, или солид, или листовое тело

### `TotalNumber`

ID: `P:TFlex.Model.Model3D.IntersectionNode3D.TotalNumber`

Количество найденных пересечений во время последней регенерации

Remarks: Информация доступна только у пересчитанного узла
