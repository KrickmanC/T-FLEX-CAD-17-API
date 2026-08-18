# TFlex.Model.Model3D.Geometry.SewGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор сшивки

## Constructors

### `SewGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body[],System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.SewGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body[],System.Double)`

Конструктор для задания сшивки

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `sheets`: Множество сшиваемых листовых тел
- `gap`: Минимальное значение ширины щели

Remarks: Все параметры обязятельные. 3D объект внешнего приложения должен быть связан с внешним объектом.

## Methods

### `SewGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body[],System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.SewGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body[],System.Double)`

Конструктор для задания сшивки

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `sheets`: Множество сшиваемых листовых тел
- `gap`: Минимальное значение ширины щели

Remarks: Все параметры обязятельные. 3D объект внешнего приложения должен быть связан с внешним объектом.

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.SewGenerator.Run`

Функция генерации сшивки
