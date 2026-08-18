# TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор сглаживания рёбер

## Constructors

### `EdgeBlendingGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body)`

ID: `M:TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `EdgeBlendingGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body)`

ID: `M:TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

### `AddConstantBlendData(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double,System.Double,System.Double,System.Double,System.Int32)`

ID: `M:TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator.AddConstantBlendData(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double,System.Double,System.Double,System.Double,System.Int32)`

Функция задаёт параметры для сглаживания ребра постоянного радиуса

Parameters:
- `entity`: Топологический элемент для установки параметров сглаживания (ребро, грань, цикл или вершина)
- `RF`: Радиус сглаживания/смещение по первой грани для фаски
- `RS`: Смещение по второй грани для фаски
- `startsetback`: Смещение от вершины в начале ребра для создания "чемоданного угла"
- `endsetback`: Смещение от вершины в конце ребра для создания "чемоданного угла"
- `BlndStatus`: Параметр режима сглаживания

### `AddVariableBlendData(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double,System.Double,System.Int32,System.Int32,System.Double[],System.Double[],System.Double[],System.Double[])`

ID: `M:TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator.AddVariableBlendData(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double,System.Double,System.Int32,System.Int32,System.Double[],System.Double[],System.Double[],System.Double[])`

Функция задаёт параметры для сглаживания ребра переменного радиуса

Parameters:
- `entity`: Ребро для установки параметров сглаживания
- `szvardata`: Количество точек для задания радиус-функции
- `varBlndParam`: Массив значений параметров на ребре в процентах
- `vradDataL`: Массив значений радиусов/смещений по "левой" грани (по направлению ребра)
- `vradDataR`: Массив значений радиусов/смещений по "правой" грани (по направлению ребра)
- `vradDataRHO`: Массив значений параметров параметров формы сечения сглаживания на ребре (0. - круговое, ]0,0.5[ - эллиптическое, 0.5 - параболическое, ]0.5,1.[ - гиперболическое
- `startsetback`: Смещение от вершины в начале ребра для создания "чемоданного угла"
- `endsetback`: Смещение от вершины в конце ребра для создания "чемоданного угла"
- `BlndStatus`: Параметр режима сглаживания

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.EdgeBlendingGenerator.Run`

Функция генерации сглаживания
