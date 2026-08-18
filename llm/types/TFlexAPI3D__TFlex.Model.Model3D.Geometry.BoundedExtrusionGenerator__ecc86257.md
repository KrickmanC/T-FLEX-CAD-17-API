# TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор выталкивания от границы до границы

## Constructors

### `BoundedExtrusionGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound)`

Конструктор для задания выталкивания от границы до границы

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `profile`: Выталкиваемый контур. Этот контур превращается в выталкивание и возращается в списке резльтирующих тел или удаляется
- `vector`: Вектор направления выталкивания
- `start`: Первая граница выталкивания
- `end`: Вторая граница выталкивания

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом.

## Methods

### `BoundedExtrusionGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.BaseDirection,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound)`

Конструктор для задания выталкивания от границы до границы

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `profile`: Выталкиваемый контур. Этот контур превращается в выталкивание и возращается в списке резльтирующих тел или удаляется
- `vector`: Вектор направления выталкивания
- `start`: Первая граница выталкивания
- `end`: Вторая граница выталкивания

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом.

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Run`

Функция генерации выталкивания от границы до границы

## Propertys

### `Disjoint`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Disjoint`

Результирующее тело может иметь несвязанные разбиения

### `End`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.End`

Вторая граница выталкивания

### `Start`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Start`

Первая граница выталкивания
