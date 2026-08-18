# TFlex.Model.Model3D.Geometry.ExtrudeGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор выталкивания

## Constructors

### `ExtrudeGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ExtrudeGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

Конструктор для задания выталкивания по направлению на заданные длины в прямом и обратном направлении

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `vector`: Вектор направления выталкивания
- `profile`: Выталкиваемый контур. Этот контур превращается в выталкивание и возращается в списке результирующих тел или удаляется
- `length`: Величина длины выталкивания в прямом направлении
- `backLength`: Величина длины выталкивания в обратном направлении

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `ExtrudeGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ExtrudeGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

Конструктор для задания выталкивания по направлению на заданные длины в прямом и обратном направлении

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `vector`: Вектор направления выталкивания
- `profile`: Выталкиваемый контур. Этот контур превращается в выталкивание и возращается в списке результирующих тел или удаляется
- `length`: Величина длины выталкивания в прямом направлении
- `backLength`: Величина длины выталкивания в обратном направлении

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.ExtrudeGenerator.Run`

Функция генерации выталкивания
