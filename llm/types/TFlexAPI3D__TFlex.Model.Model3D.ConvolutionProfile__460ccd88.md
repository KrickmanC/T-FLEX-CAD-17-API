# TFlex.Model.Model3D.ConvolutionProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Свёртка плоского контура на поверхность

## Constructors

### `ConvolutionProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ConvolutionProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания свёртки плоского профиля на поверхность

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `ConvolutionProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ConvolutionProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания свёртки плоского профиля на поверхность

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `ConvolutionSurface`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.ConvolutionSurface`

Набор граней, образующих поверхность, на которую выполняется свёртка

Remarks: В настоящей версии в качестве поверхности можно выбирать только конические и цилиндрические грани. В остальных случаях профиль строится не будет. В настоящей версии при свёртке учитываются границы граней. То есть, если границы свёртки пересекают границы грани или не лежат на грани, то профиль строится не будет

### `DirectionPointOnPlane`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.DirectionPointOnPlane`

Вторая точка в плоскости сворачиваемго контура

Remarks: Эта точка и вторая точка на поверхности задают направление свертки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет

### `DirectionPointOnSurface`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.DirectionPointOnSurface`

Вторая точка на поверхности

Remarks: Эта точка и вторая точка в плоскости контура задают направление свертки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет

### `Orientation`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.Orientation`

Ориентация направления свёртки

### `PlanarContour`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.PlanarContour`

Сворачиваемый плоский контур

Remarks: В настоящей версии в качестве контура можно выбирать только плоские листовые профили. В остальных случаях профиль строится не будет

### `StartPointOnPlane`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.StartPointOnPlane`

Первая точка в плоскости сворачиваемго контура

Remarks: Эта точка и первая точка на поверхности задают начало свёртки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет

### `StartPointOnSurface`

ID: `P:TFlex.Model.Model3D.ConvolutionProfile.StartPointOnSurface`

Первая точка на поверхности

Remarks: Эта точка и первая точка в плоскости контура задают начало свертки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет
