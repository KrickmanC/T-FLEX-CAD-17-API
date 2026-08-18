# TFlex.Model.Model3D.ConeDevelopmentProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Развёртка грани на конической поверхности

## Constructors

### `ConeDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ConeDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки грани на конической поверхности

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `ConeDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.ConeDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки грани на конической поверхности

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `Face`

ID: `P:TFlex.Model.Model3D.ConeDevelopmentProfile.Face`

Разворачиваемая грань

### `PointOnFace`

ID: `P:TFlex.Model.Model3D.ConeDevelopmentProfile.PointOnFace`

Точка на грани

Remarks: Эта точка задаёт начало развёртки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет

### `SectionIsolinePoint`

ID: `P:TFlex.Model.Model3D.ConeDevelopmentProfile.SectionIsolinePoint`

Точка, через которую проходит изопараметрическая прямая, вдоль которой разрезается замкнтуая грань

Remarks: В настоящей версии в качестве точки можно выбирать только 3D узел. В остальных случаях профиль строится не будет
