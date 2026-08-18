# TFlex.Model.Model3D.CylinderDevelopmentProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Развёртка грани на цилиндрической поверхности

## Constructors

### `CylinderDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.CylinderDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки грани на цилиндрической поверхности

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `CylinderDevelopmentProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.CylinderDevelopmentProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания развёртки грани на цилиндрической поверхности

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `Face`

ID: `P:TFlex.Model.Model3D.CylinderDevelopmentProfile.Face`

Разворачиваемая грань

### `PointOnFace`

ID: `P:TFlex.Model.Model3D.CylinderDevelopmentProfile.PointOnFace`

Точка на грани

Remarks: Эта точка задаёт начало развёртки. В настоящей версии в качестве точки можно выбирать только 3D узлы. В остальных случаях профиль строится не будет

### `SectionCurve`

ID: `P:TFlex.Model.Model3D.CylinderDevelopmentProfile.SectionCurve`

Кривая, вдоль которой разрезается замкнутая грань

Remarks: В настоящей версии в качестве кривой можно выбирать только ребро. В остальных случаях профиль строится не будет. Линия разреза может задаваться тремя взаимоисключающими путями: кривой на грани; изопараметрической прямой, проходящей через точку на поверхности; углом разрезающей прямой.

### `SectionIsolineAngle`

ID: `P:TFlex.Model.Model3D.CylinderDevelopmentProfile.SectionIsolineAngle`

Угол, определяющий изопараметрическую прямую, вдоль которой разрезается замкнутая грань

Remarks: Линия разреза может задаваться тремя взаимоисключающими путями: кривой на грани; изопараметрической прямой, проходящей через точку на поверхности; углом разрезающей прямой.

### `SectionIsolinePoint`

ID: `P:TFlex.Model.Model3D.CylinderDevelopmentProfile.SectionIsolinePoint`

Точка, через которую проходит изопараметрическая прямая, вдоль которой разрезается замкнутая грань

Remarks: В настоящей версии в качестве точки можно выбирать только 3D узел. В остальных случаях профиль строится не будет. Линия разреза может задаваться тремя взаимоисключающими путями: кривой на грани; изопараметрической прямой, проходящей через точку на поверхности; углом разрезающей прямой.
