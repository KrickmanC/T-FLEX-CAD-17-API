# TFlex.Model.Model3D.Path3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для всех типов 3D путей

## Constructors

### `Path3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Path3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `Path3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Path3D.#ctor(TFlex.Model.Document)`

Конструктор для создания нового пути

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

### `TestCompatibility(TFlex.Model.Model3D.Path3D,TFlex.Model.Model3D.Path3D)`

ID: `M:TFlex.Model.Model3D.Path3D.TestCompatibility(TFlex.Model.Model3D.Path3D,TFlex.Model.Model3D.Path3D)`

Проверить совместимость типов, трасса и трасса

## Propertys

### `ConvertToSpline`

ID: `P:TFlex.Model.Model3D.Path3D.ConvertToSpline`

Получить параметры для преобразования пути в сплайн

### `CutIndex`

ID: `P:TFlex.Model.Model3D.Path3D.CutIndex`

Индекс решения

Remarks: 0 или 1

### `FirstCutPoint`

ID: `P:TFlex.Model.Model3D.Path3D.FirstCutPoint`

Первая точка обрезки

### `Geometry`

ID: `P:TFlex.Model.Model3D.Path3D.Geometry`

Получить геометрические данные пути

### `GroupType`

ID: `P:TFlex.Model.Model3D.Path3D.GroupType`

Получить тип объекта

### `Path3DSegments`

ID: `P:TFlex.Model.Model3D.Path3D.Path3DSegments`

Возвращает информацию об участках пути

### `Reverse`

ID: `P:TFlex.Model.Model3D.Path3D.Reverse`

Реверисровать направление пути

### `SecondCutPoint`

ID: `P:TFlex.Model.Model3D.Path3D.SecondCutPoint`

Вторая точка обрезки
