# TFlex.Model.Model3D.Geometry.RotateGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор вращения

## Constructors

### `RotateGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseAxis,TFlex.Model.Model3D.Geometry.Body,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.RotateGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseAxis,TFlex.Model.Model3D.Geometry.Body,System.Double)`

Конструктор для задания вращения

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `axis`: Ось вращения
- `profile`: Вращаемый контур. Этот контур превращается во вращение и возращается в списке результирующих тел или удаляется
- `angle`: Угол поворота

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `RotateGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseAxis,TFlex.Model.Model3D.Geometry.Body,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.RotateGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseAxis,TFlex.Model.Model3D.Geometry.Body,System.Double)`

Конструктор для задания вращения

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `axis`: Ось вращения
- `profile`: Вращаемый контур. Этот контур превращается во вращение и возращается в списке результирующих тел или удаляется
- `angle`: Угол поворота

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.RotateGenerator.Run`

Функция генерации вращения
