# TFlex.Model.Model3D.Geometry.Body

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Класс хранения геометрических тел

## Constructors

### `Body(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BaseBody)`

Конструктор для создания тела как копии другого тела

Parameters:
- `body`: Тело с которого копируется данное тело

### `Body(TFlex.Model.Model3D.Geometry.BaseFace)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BaseFace)`

Конструктор для создания листового тела на основе грани

### `Body(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конструктор для создания листового прямоугольника(параллелограмма)

Parameters:
- `p0`: Первая точка контура
- `p1`: Вторая точка контура
- `p2`: Третья точка контура

### `Body(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конструктор для создания параллелепипеда

Parameters:
- `p0`: Первая точка - база
- `p1`: Вторая точка - размер по 'X'
- `p2`: Третья точка - размер по 'Y'
- `p3`: Четвёртая точка - размер по 'Z'

## Methods

### `Body(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BaseBody)`

Конструктор для создания тела как копии другого тела

Parameters:
- `body`: Тело с которого копируется данное тело

### `Body(TFlex.Model.Model3D.Geometry.BaseFace)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BaseFace)`

Конструктор для создания листового тела на основе грани

### `Body(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конструктор для создания листового прямоугольника(параллелограмма)

Parameters:
- `p0`: Первая точка контура
- `p1`: Вторая точка контура
- `p2`: Третья точка контура

### `Body(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.#ctor(TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D,TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конструктор для создания параллелепипеда

Parameters:
- `p0`: Первая точка - база
- `p1`: Вторая точка - размер по 'X'
- `p2`: Третья точка - размер по 'Y'
- `p3`: Четвёртая точка - размер по 'Z'

### `NormalizeIfPlanarClosedWire(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.Body.NormalizeIfPlanarClosedWire(TFlex.Model.Model3D.Geometry.BaseDirection)`

Если тело является плоским замкнутым контуром, то обход по нему можно ориентировать против часовой стрелки согласно нормали к этой плоскости

Parameters:
- `direction`: Нормаль к плоскости заданного контура

### `ReverseIfWire`

ID: `M:TFlex.Model.Model3D.Geometry.Body.ReverseIfWire`

Если тело является контуром, то можно изменить ориентацию контура

## Propertys

### `Edges`

ID: `P:TFlex.Model.Model3D.Geometry.Body.Edges`

Множество рёбер

### `Existence`

ID: `P:TFlex.Model.Model3D.Geometry.Body.Existence`

Признак существования тела

### `Faces`

ID: `P:TFlex.Model.Model3D.Geometry.Body.Faces`

Множество граней

### `Loops`

ID: `P:TFlex.Model.Model3D.Geometry.Body.Loops`

Множество циклов

### `Vertices`

ID: `P:TFlex.Model.Model3D.Geometry.Body.Vertices`

Множество вершин
