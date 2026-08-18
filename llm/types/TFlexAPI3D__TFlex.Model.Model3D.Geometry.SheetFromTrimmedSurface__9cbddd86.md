# TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор листового тела на поверхности, обрезанной набором параметрических составных кривых

## Constructors

### `SheetFromTrimmedSurface(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseSurface,TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump[])`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseSurface,TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump[])`

Конструктор для задания листового тела на поверхности по набору параметрических составных кривых

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `surface`: Поверхность, на которой лежит листовое тело
- `lumps`: Множество связанных областей

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `SheetFromTrimmedSurface(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseSurface,TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump[])`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseSurface,TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Lump[])`

Конструктор для задания листового тела на поверхности по набору параметрических составных кривых

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `surface`: Поверхность, на которой лежит листовое тело
- `lumps`: Множество связанных областей

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.SheetFromTrimmedSurface.Run`

Функция генерации листового тела
