# NURBSBuilder

Assembly: `TFlexAPI`

## Methods

### `GenerateSplineGeometry31(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:NURBSBuilder.GenerateSplineGeometry31(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Общий метод создания геометрии сплайна начиная с 31 версии(

Parameters:
- `iContext`: Контекст
- `iVersion`: Версия объекта
- `iDoc`: Документ
- `iToModelSpaceScale`: Масштаб отображение из модельного пространства в RGP
- `iData`: Постановка задачи
- `oResult`: Результат

### `GenerateSplineGeometryCommon(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:NURBSBuilder.GenerateSplineGeometryCommon(RGPlatform.Geometry.Context*,System.Int32,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Общий метод создания геометрии сплайна

Parameters:
- `iContext`: Контекст
- `iVersion`: Версия объекта
- `iDoc`: Документ
- `iToModelSpaceScale`: Масштаб отображение из модельного пространства в RGP
- `iData`: Постановка задачи
- `oResult`: Результат

### `GenerateSplineGeometryOld(RGPlatform.Geometry.Context*,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.unique_ptr<NURBSCurve,std.default_delete<NURBSCurve>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:NURBSBuilder.GenerateSplineGeometryOld(RGPlatform.Geometry.Context*,TFDocument!System.Runtime.CompilerServices.IsConst*,System.Int32,System.Double,SplineImageData*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.unique_ptr<NURBSCurve,std.default_delete<NURBSCurve>>*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Общий метод создания геометрии сплайна (до 31 версии)

Parameters:
- `iContext`: Контекст
- `iVersion`: Версия объекта
- `iDoc`: Документ
- `iToModelSpaceScale`: Масштаб отображение из модельного пространства в RGP
- `iData`: Постановка задачи
- `oResult`: Результат
- `iScaleInterval`: Масштабировать интервал
