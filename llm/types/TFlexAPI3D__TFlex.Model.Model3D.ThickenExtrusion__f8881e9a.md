# TFlex.Model.Model3D.ThickenExtrusion

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция выталкивания по вектору или приданием толщины

## Constructors

### `ThickenExtrusion(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ThickenExtrusion.#ctor(TFlex.Model.Document)`

Конструктор для создания выталкивания

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `ThickenExtrusion(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ThickenExtrusion.#ctor(TFlex.Model.Document)`

Конструктор для создания выталкивания

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Propertys

### `BackwardLength`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.BackwardLength`

Длина выталкивания в обратном направлении

### `Bedplate`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.Bedplate`

Параметр построения донышка

Remarks: Толщина донышка должна задаваться положительным значением. Донышко строится только для плоских листовых контуров при построении стенок ненулевой длины.

### `BedplateThickness`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.BedplateThickness`

Получить толщину донышка

### `Cover`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.Cover`

Параметр построения крышки

Remarks: Толщина крышки должна задаваться положительным значением. Крышка строится только для плоских листовых контуров при построении стенок ненулевой длины.

### `CoverThickness`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.CoverThickness`

Толщина крышки

### `ForwardLength`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.ForwardLength`

Длина выталкивания в прямом направлении

### `LengthType`

ID: `P:TFlex.Model.Model3D.ThickenExtrusion.LengthType`

Способ определения длины выталкивания в прямом и обратном направлениях
