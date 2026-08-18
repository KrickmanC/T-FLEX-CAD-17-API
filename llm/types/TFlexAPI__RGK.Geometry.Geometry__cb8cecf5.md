# RGK.Geometry.Geometry

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry`

## Methods

### `AsCircle`

ID: `M:RGK.Geometry.Geometry.AsCircle`

Returns: Окружность или nullptr в случае если объект не является окружностью

### `AsCompositeSpline`

ID: `M:RGK.Geometry.Geometry.AsCompositeSpline`

Returns: Составная кривая или nullptr в случае если объект не является составной кривой

### `AsCone`

ID: `M:RGK.Geometry.Geometry.AsCone`

Returns: Конус или nullptr в случае если объект не является конусом

### `AsCurve`

ID: `M:RGK.Geometry.Geometry.AsCurve`

Returns: Кривая или nullptr в случае если объект не является кривой

### `AsCylinder`

ID: `M:RGK.Geometry.Geometry.AsCylinder`

Returns: Цилиндр или nullptr в случае если объект не является цилиндром

### `AsCylinderCylinderIntersection`

ID: `M:RGK.Geometry.Geometry.AsCylinderCylinderIntersection`

Returns: Кривая пересечения Цилиндра с Цилиндром или nullptr в случае если объект не является точкой

### `AsCylinderSphereIntersection`

ID: `M:RGK.Geometry.Geometry.AsCylinderSphereIntersection`

Returns: Кривая пересечения Цилиндра со Сферой или nullptr в случае если объект не является точкой

### `AsEllipse`

ID: `M:RGK.Geometry.Geometry.AsEllipse`

Returns: Эллипс или nullptr в случае если объект не является эллипсом

### `AsIntersectionCurve`

ID: `M:RGK.Geometry.Geometry.AsIntersectionCurve`

Returns: Кривая пересечения или nullptr в случае если объект не является кривой пересечения

### `AsIsoclineCurve`

ID: `M:RGK.Geometry.Geometry.AsIsoclineCurve`

Returns: Изоклин-кривая или nullptr в случае если объект не является изоклин-кривой

### `AsIsoclineSurface`

ID: `M:RGK.Geometry.Geometry.AsIsoclineSurface`

Returns: Изоклин-поверхность или nullptr в случае если объект не является изоклин-поверхностью

### `AsLine`

ID: `M:RGK.Geometry.Geometry.AsLine`

Returns: Отрезок или nullptr в случае если объект не является отрезком

### `AsMultipleSurfacesBlending`

ID: `M:RGK.Geometry.Geometry.AsMultipleSurfacesBlending`

Returns: Поверхность сглаживания или nullptr в случае если объект не является поверхностью сглаживания

### `AsNURBSCurve`

ID: `M:RGK.Geometry.Geometry.AsNURBSCurve`

Returns: NURBS-кривая или nullptr в случае если объект не является NURBS-кривой

### `AsNURBSSurface`

ID: `M:RGK.Geometry.Geometry.AsNURBSSurface`

Returns: NURBS-поверхность или nullptr в случае если объект не является NURBS-поверхностью

### `AsOffsetSurface`

ID: `M:RGK.Geometry.Geometry.AsOffsetSurface`

Returns: Эквидистантная поверхность или nullptr в случае если объект не является эквидистантной поверхность

### `AsParametricCurve`

ID: `M:RGK.Geometry.Geometry.AsParametricCurve`

Returns: Параметрическая кривая или nullptr в случае если объект не является параметрической кривой

### `AsPlane`

ID: `M:RGK.Geometry.Geometry.AsPlane`

Returns: Плоскость или nullptr в случае если объект не является плоскостью

### `AsPoint`

ID: `M:RGK.Geometry.Geometry.AsPoint`

Returns: Точка или nullptr в случае если объект не является точкой

### `AsPolylineCurve`

ID: `M:RGK.Geometry.Geometry.AsPolylineCurve`

Returns: Полилиния или nullptr в случае если объект не является полилинией

### `AsSilhouetteCurve`

ID: `M:RGK.Geometry.Geometry.AsSilhouetteCurve`

Returns: Очерковая или nullptr в случае если объект не является очерковой

### `AsSphere`

ID: `M:RGK.Geometry.Geometry.AsSphere`

Returns: Сфера или nullptr в случае если объект не является сферой

### `AsSphereConeIntersection`

ID: `M:RGK.Geometry.Geometry.AsSphereConeIntersection`

Returns: Кривая пересечения Сферы с Конусом или nullptr в случае если объект не является точкой

### `AsSurface`

ID: `M:RGK.Geometry.Geometry.AsSurface`

Returns: Поверхность или nullptr в случае если объект не является поверхностью

### `AsTorus`

ID: `M:RGK.Geometry.Geometry.AsTorus`

Returns: Тор или nullptr в случае если объект не является тором

### `AsTorusSphereIntersection`

ID: `M:RGK.Geometry.Geometry.AsTorusSphereIntersection`

Returns: Кривая пересечения Тора со Сферой или nullptr в случае если объект не является точкой

### `Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Geometry.Copy(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `oCopy`: Копия геометрического объекта

Returns: - Result::Success в случае успешного выполнения

### `GetType`

ID: `M:RGK.Geometry.Geometry.GetType`

Returns: Тип геометрии объекта

### `IsCoincident(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Geometry.IsCoincident(RGK.Common.Context*,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `iGeometry`: Геометрический объект, с которым выполняется сравнение
- `iData`: Выполнять сравнение по данным. То есть объекты считаются одинаковыми в случае совпадения всех параметров объектов
- `oCoincident`: Результат сравнения

Returns: - Result::Success в случае успешного выполнения

### `IsCurve`

ID: `M:RGK.Geometry.Geometry.IsCurve`

Returns: true если объект является кривой

### `IsSurface`

ID: `M:RGK.Geometry.Geometry.IsSurface`

Returns: true если объект является поверхностью

### `Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Geometry.Geometry.Transform(RGK.Common.Context*,RGK.Math.AffineMap3D!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double,std.shared_ptr<RGK.Geometry.Geometry!System.Runtime.CompilerServices.IsConst>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iContext`: Контекст создания линии
- `iMap`: Аффинное преобразование
- `iTolerance`: Допустимая точность преобразований
- `oCopy`: Возвращается трансформированная геометрия
- `oExact`: Возвращается true-для точного преобразования

Returns: - Result::Success в случае успешного выполнения

## Members

### `TypeSet`

ID: `D:RGK.Geometry.Geometry.TypeSet`
