# TFlex.Model.Model3D.Geometry.ThickenExtrusionGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор придания толщины

## Constructors

### `ThickenExtrusionGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ThickenExtrusionGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

Конструктор для задания придания толщины

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `sheet`: Листовое тело. Этот лист возращается в списке результирующих тел или удаляется
- `thickness`: Величина толщины в лицевом направлении
- `backThickness`: Величина толщины в изнаночном направлении

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `ThickenExtrusionGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ThickenExtrusionGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Double,System.Double)`

Конструктор для задания придания толщины

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `sheet`: Листовое тело. Этот лист возращается в списке результирующих тел или удаляется
- `thickness`: Величина толщины в лицевом направлении
- `backThickness`: Величина толщины в изнаночном направлении

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.ThickenExtrusionGenerator.Run`

Функция генерации придания толщины
