# TFlex.Model.Model3D.Profile.GeometryData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Profile`

## Summary

Множество геометрических данных профиля

## Propertys

### `Curve`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.Curve`

Получить кривую, на которой лежит профиль

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelCurve` , хранящий кривую и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких рёбер, кривая может быть не определена

### `CurveAxis`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.CurveAxis`

Если профиль лежит на окружности или эллипсе, то можно получить их ось

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelAxis` , хранящий координаты оси и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, ось может быть не определена

### `CurveDirection`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.CurveDirection`

Если профиль лежит на окружности или эллипсе, то можно получить направление их осей

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelDirection` , хранящий координаты вектора и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, направление может быть не определено

### `CurvePoint`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.CurvePoint`

Если профиль лежит на окружности или эллипсе, можно получить центр окружности или эллипса

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelPoint3D` , хранящий координаты точки и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, точка может быть не определена

### `CylinderAxis`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.CylinderAxis`

Если профиль лежит на цилиндре, то можно получить его ось

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelAxis` , хранящий координаты оси и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, ось может быть не определена

### `CylinderDirection`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.CylinderDirection`

Если профиль лежит на цилиндре, то можно получить направление его оси

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelDirection` , хранящий координаты вектора и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, направление может быть не определено

### `LaminarContour`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.LaminarContour`

Получить контур - границы профиля

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelContour` , хранящий контуры и ссылку на эти геометрические данные профиля

### `LineAxis`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.LineAxis`

Если профиль лежит на прямой, то можно получить эту прямую

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelAxis` , хранящий координаты оси и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, ось может быть не определена

### `LineDirection`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.LineDirection`

Если профиль лежит на прямой, то можно получить направление этой прямой

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelDirection` , хранящий координаты вектора и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, направление может быть не определено

### `Plane`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.Plane`

Получить плоскость

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelPlane` , хранящий координаты плоскости и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или одного прямого ребра, плоскость может быть не определена

### `PlaneDirection`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.PlaneDirection`

Если профиль лежит на плоскости, то можно получить направление нормали к этой плоскости

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelDirection` , хранящий координаты вектора и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, направление может быть не определено

### `Sheet`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.Sheet`

Получить листовое тело профиля

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelSheet` , хранящий листовое тело и ссылку на эти геометрические данные профиля

### `SheetBox`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.SheetBox`

Получить границы листового профиля

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelBox` , хранящий границы и ссылку на эти геометрические данные профиля

### `SheetContour`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.SheetContour`

Получить контур - листовое тело

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelContour` , хранящий контуры и ссылку на эти геометрические данные профиля

### `SphereCenter`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.SphereCenter`

Если профиль лежит на сфере, то можно получить центр сферы

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelPoint3D` , хранящий координаты точки и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, точка может быть не определена

### `Surface`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.Surface`

Получить поверхность, на которой лежит профиль

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelSurface` , хранящий поверхность и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или состоящих только из рёбер (проволочные профили), поверхность может быть не определена

### `ToreAxis`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.ToreAxis`

Если профиль лежит на торе, то можно получить его ось

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelAxis` , хранящий координаты оси и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, ось может быть не определена

### `ToreCenter`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.ToreCenter`

Если профиль лежит на торе, то можно получить центр тора

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelPoint3D` , хранящий координаты точки и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, точка может быть не определена

### `ToreDirection`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.ToreDirection`

Если профиль лежит на торе, то можно получить направление его оси

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelDirection` , хранящий координаты вектора и ссылку на эти геометрические данные профиля

Remarks: Для профилей, состоящих из нескольких граней или рёбер, направление может быть не определено

### `WireBox`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.WireBox`

Получить границы проволчного профиля

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelBox` , хранящий границы и ссылку на эти геометрические данные профиля

### `WireContour`

ID: `P:TFlex.Model.Model3D.Profile.GeometryData.WireContour`

Получить контур для проволочного профиля

Returns: Объект класса `T:TFlex.Model.Model3D.Geometry.ModelContour` , хранящий контуры и ссылку на эти геометрические данные профиля
