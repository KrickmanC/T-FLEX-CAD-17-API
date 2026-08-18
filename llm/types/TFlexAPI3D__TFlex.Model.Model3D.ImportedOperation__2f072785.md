# TFlex.Model.Model3D.ImportedOperation

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция "Внешняя модель"

## Constructors

### `ImportedOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ImportedOperation.#ctor(TFlex.Model.Document)`

Конструктор для операции "Внешняя модель"

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `ImportedOperation(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ImportedOperation.#ctor(TFlex.Model.Document)`

Конструктор для операции "Внешняя модель"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Create(TFlex.Model.Document,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BaseCurve},System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BaseInterval},System.Collections.Generic.List`1{TFlex.Drawing.Point})`

ID: `M:TFlex.Model.Model3D.ImportedOperation.Create(TFlex.Model.Document,System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BaseCurve},System.Collections.Generic.List`1{TFlex.Model.Model3D.Geometry.BaseInterval},System.Collections.Generic.List`1{TFlex.Drawing.Point})`

Конструктор для операции "Внешняя модель"

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `curves`: Коллекция кривых
- `intervals`: Коллекция интервалов

### `Create(TFlex.Model.Document,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.ImportedOperation.Create(TFlex.Model.Document,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конструктор для операции "Внешняя модель"

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `OpenSource`

ID: `M:TFlex.Model.Model3D.ImportedOperation.OpenSource`

Открыть файл-источник

## Propertys

### `FileName`

ID: `P:TFlex.Model.Model3D.ImportedOperation.FileName`

Имя файла внешней модели

### `GroupType`

ID: `P:TFlex.Model.Model3D.ImportedOperation.GroupType`

Получить тип объекта

### `MaterialsFromSource`

ID: `P:TFlex.Model.Model3D.ImportedOperation.MaterialsFromSource`

Значение свойства "С учётом материалов"

### `PathName`

ID: `P:TFlex.Model.Model3D.ImportedOperation.PathName`

Путь к файлу внешней модели

### `SaveGeometry`

ID: `P:TFlex.Model.Model3D.ImportedOperation.SaveGeometry`

Значение свойства "Сохранять геометрию"

### `SourceLCS`

ID: `P:TFlex.Model.Model3D.ImportedOperation.SourceLCS`

Исходная система коодинат

### `SourcePath`

ID: `P:TFlex.Model.Model3D.ImportedOperation.SourcePath`

Путь к файлу-источнику, из которого выгружена в обменный файл внешняя модель

### `TargetLCS`

ID: `P:TFlex.Model.Model3D.ImportedOperation.TargetLCS`

Целевая система коодинат
