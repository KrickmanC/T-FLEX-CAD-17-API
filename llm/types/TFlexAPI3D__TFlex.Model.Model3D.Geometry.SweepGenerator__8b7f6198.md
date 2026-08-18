# TFlex.Model.Model3D.Geometry.SweepGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор тела по траектории

## Constructors

### `SweepGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Vertex)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Vertex)`

Конструктор для задания тела по траектории

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `profile`: Образующий контур. Этот контур превращается в тело по траектории и возращается в списке резльтирующих тел или удаляется
- `path`: Траектория
- `start`: Стартовая точка на траектории

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `SweepGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Vertex)`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.Vertex)`

Конструктор для задания тела по траектории

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `profile`: Образующий контур. Этот контур превращается в тело по траектории и возращается в списке резльтирующих тел или удаляется
- `path`: Траектория
- `start`: Стартовая точка на траектории

Remarks: Все параметры обязательные. 3D объект внешнего приложения должен быть связан с внешним объектом

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.SweepGenerator.Run`

Функция генерации тела по траектории

## Propertys

### `Alignment`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Alignment`

Ориентация контура

Remarks: По умолчанию установлен тип Normal

### `AllowRationals`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.AllowRationals`

Параметр построения боковых поверхностей в форме рациональных сплайнов

Remarks: По умолчанию параметр установлен

### `Fair`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Fair`

Параметр улучшения формы результирующего тела в случае пространственной траектории

Remarks: По умолчанию параметр установлен

### `Ignorable`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Ignorable`

Получить множество игнорируемых вершин траектории.

Remarks: В некоторых случаях при формировании граней можно в местах сочленения сегментов тела, соответсвующих вершинам траектории, избежать построения рёбер, сшивая грани в одну. Если не задан тип разбиения результирущего тела на грани Grid, то такая обработка выполняется автоматически. Если задан тип Grid, то можно задать набор вершин траектории, для которых будет выполняться такая обработка. В данный список нельзя добавлять первую и последнюю вершины размкутой траектории или вершины, где смежные рёбра траектории не G1 - непрерывны

### `MinimiseTolerance`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.MinimiseTolerance`

Параметр минимизации точности, где это возможно

Remarks: По умолчанию параметр не установлен

### `Scale`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Scale`

Получить закон масштабирования

### `ScalePoint`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.ScalePoint`

Точка масштабирования для способов масштабирования Posn и Size

### `ScaleType`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.ScaleType`

Способ масштабирования

Remarks: По умолчанию установлен тип Both

### `Simplify`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Simplify`

Параметр упрощения геометрии

Remarks: По умолчанию параметр упрощения установлен

### `Tolerance`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Tolerance`

Точность геометрии

Remarks: По умолчанию 1.0e-5

### `TopologyForm`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.TopologyForm`

Тип разбиения

Remarks: По умолчанию установлен тип Minimal

### `Twist`

ID: `P:TFlex.Model.Model3D.Geometry.SweepGenerator.Twist`

Получить закон кручения
