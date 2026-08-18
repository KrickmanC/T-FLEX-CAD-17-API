# TFlex.Model.Model3D.ProjectionProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Проекция контура на листовое или твёрдое тело

## Constructors

### `ProjectionProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ProjectionProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания проекции контура на листовое или твёрдое тело

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `ProjectionProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ProjectionProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания проекции контура на листовое или твёрдое тело

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `FirstPoint`

ID: `P:TFlex.Model.Model3D.ProjectionProfile.FirstPoint`

Первая точка, задающая направление проецирования

Remarks: Направление проецирования задаётся двумя взаимоисключающими методами: двумя точками или направлением. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет. Если направление не задано, то выполняется проецирование по нормали к поверхности

### `ProjectedContour`

ID: `P:TFlex.Model.Model3D.ProjectionProfile.ProjectedContour`

Проецируемый контур

Remarks: В настоящей версии в качестве контура можно выбирать только листовой профиль. В остальных случаях профиль строится не будет

### `ProjectionDirection`

ID: `P:TFlex.Model.Model3D.ProjectionProfile.ProjectionDirection`

Направление проецирования

Remarks: Направление проецирования задаётся двумя взаимоисключающими методами: двумя точками или направлением. В настоящей версии в качестве направления можно выбирать только оси системы координат. В остальных случаях профиль строится не будет. Если направление не задано, то выполняется проецирование по нормали к поверхности

### `ProjectionSurface`

ID: `P:TFlex.Model.Model3D.ProjectionProfile.ProjectionSurface`

Поверхность проецирования

Remarks: В настоящей версии в качестве поверхности можно выбирать только операции и грани. В остальных случаях профиль строится не будет

### `SecondPoint`

ID: `P:TFlex.Model.Model3D.ProjectionProfile.SecondPoint`

Вторая точка, задающая направление проецирования

Remarks: Направление проецирования задаётся двумя взаимоисключающими методами: двумя точками или направлением. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет. Если направление не задано, то выполняется проецирование по нормали к поверхности
