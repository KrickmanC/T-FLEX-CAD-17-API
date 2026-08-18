# TFlex.Model.Model3D.Geometry.BaseGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Базовый класс для всех генераторов

## Constructors

### `BaseGenerator(TFlex.Model.Model3D.ProxyObject3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D)`

Конструктор для задания генератора

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат

Remarks: Ссылка на 3D объект внешнего приложения является обязательным параметром. 3D объект внешнего приложения должен быть связан с внешним объектом.

## Methods

### `BaseGenerator(TFlex.Model.Model3D.ProxyObject3D)`

ID: `M:TFlex.Model.Model3D.Geometry.BaseGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D)`

Конструктор для задания генератора

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат

Remarks: Ссылка на 3D объект внешнего приложения является обязательным параметром. 3D объект внешнего приложения должен быть связан с внешним объектом.

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.BaseGenerator.Run`

Основная функция генерации геометрических результатов

## Propertys

### `LastResult`

ID: `P:TFlex.Model.Model3D.Geometry.BaseGenerator.LastResult`

Результат

### `Proxy`

ID: `P:TFlex.Model.Model3D.Geometry.BaseGenerator.Proxy`

Получить внешнее приложение, для которого генерируется результат
