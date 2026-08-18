# TFlex.Model.Model3D.Geometry.BooleanGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор булевой операции

## Constructors

### `BooleanGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body[],TFlex.Model.Model3D.BooleanOperation.FunctionType)`

ID: `M:TFlex.Model.Model3D.Geometry.BooleanGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body[],TFlex.Model.Model3D.BooleanOperation.FunctionType)`

Конструктор для задания вытлакивания по направлению на заданные длины в прямом и обратном направлении

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `target`: Тело, к котому применятся булева
- `tools`: Массив тел, которые используются для модификации тела
- `function`: Тип булевой

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `BooleanGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body[],TFlex.Model.Model3D.BooleanOperation.FunctionType)`

ID: `M:TFlex.Model.Model3D.Geometry.BooleanGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body[],TFlex.Model.Model3D.BooleanOperation.FunctionType)`

Конструктор для задания вытлакивания по направлению на заданные длины в прямом и обратном направлении

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `target`: Тело, к котому применятся булева
- `tools`: Массив тел, которые используются для модификации тела
- `function`: Тип булевой

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.BooleanGenerator.Run`

Функция генерации выталкивания
