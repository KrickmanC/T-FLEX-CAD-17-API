# TFlex.Model.Model3D.SurfaceSetDevelopmentProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Развёртка набора граней

## Constructors

### `SurfaceSetDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки набора граней

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `SurfaceSetDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки набора граней

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `DeleteRedundant`

ID: `P:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.DeleteRedundant`

Параметр "удалять лишние рёбра"

### `DevelopmentFaces`

ID: `P:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.DevelopmentFaces`

Набор разворачиваемых граней

### `FixedEdges`

ID: `P:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.FixedEdges`

Набор неразрывных рёбер

### `PointOnFace`

ID: `P:TFlex.Model.Model3D.SurfaceSetDevelopmentProfile.PointOnFace`

Точка на наборе граней

Remarks: Эта точка задаёт начало развёртки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет
