# TFlex.Model.Model3D.FaceDelete

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция удаления граней

## Constructors

### `FaceDelete(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceDelete.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Удаление граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Methods

### `FaceDelete(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.FaceDelete.#ctor(TFlex.Model.Document)`

Конструктор для создания операция "Удаление граней"

Parameters:
- `doc`: Документ, в котором создаётся новый объект

## Propertys

### `Faces`

ID: `P:TFlex.Model.Model3D.FaceDelete.Faces`

Удаляемые грани

### `GroupType`

ID: `P:TFlex.Model.Model3D.FaceDelete.GroupType`

Получить тип объекта

### `HealingMethod`

ID: `P:TFlex.Model.Model3D.FaceDelete.HealingMethod`

Способ обработки граней

### `IndependentHealing`

ID: `P:TFlex.Model.Model3D.FaceDelete.IndependentHealing`

Независимая обработка циклов

Remarks: Если установлено в true, то каждый замкнутый цикл образуемый гранями обрабатывается независимо. В противном случае обрабатываются совместно.
