# TFlex.Model.Model3D.OffsetProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Смещение к плоскому контуру

## Constructors

### `OffsetProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания смещения к плоскому контуру

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `OffsetProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OffsetProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания смещения к плоскому контуру

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `BreakFillType`

ID: `P:TFlex.Model.Model3D.OffsetProfile.BreakFillType`

Способ обработки разрывов

Remarks: Для границ контуров, состоящих из нескольких рёбер или имеющих изломы в вершинах, возможно возникновение разрывов между эквидистантами, построенными для каждого ребра. В этом случае задаётся способ обработки такого разрыва. По умолчанию используется метод продолжения по кривой

### `InnerContourType`

ID: `P:TFlex.Model.Model3D.OffsetProfile.InnerContourType`

Способ обработки внутреннего контура

### `Offset`

ID: `P:TFlex.Model.Model3D.OffsetProfile.Offset`

Значение смещения

Remarks: Значение смещения задаётся двумя взаимоисключающими способами: по точке или по значению

### `OffsetPoint`

ID: `P:TFlex.Model.Model3D.OffsetProfile.OffsetPoint`

Точка, определяющая значение смещения

Remarks: В настоящей версии в качестве точки можно выбирать только 3D узел. В остальных случаях профиль строится не будет. Значение смещения задаётся двумя взаимоисключающими способами : по точке или по значению

### `SourceContour`

ID: `P:TFlex.Model.Model3D.OffsetProfile.SourceContour`

Плоский контур, для которого строится смещение

Remarks: В настоящей версии в качестве контура можно выбирать только плоские листовые профили. В остальных случаях профиль строится не будет
