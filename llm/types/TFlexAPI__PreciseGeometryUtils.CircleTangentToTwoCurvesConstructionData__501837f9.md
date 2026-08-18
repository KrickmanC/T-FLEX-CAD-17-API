# PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData

Assembly: `TFlexAPI`
Namespace: `PreciseGeometryUtils`

## Constructors

### `CircleTangentToTwoCurvesConstructionData(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Boolean,System.Double,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,System.Double)`

ID: `M:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData.#ctor(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Boolean,System.Double,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,System.Double)`

Конструктор

Parameters:
- `iDoc`: Ссылка на документ
- `iCalculateAddInterPoints`: true - рассчитывать дополнительные точки пересечения, false - не рассчитывать
- `iRadius`: Радиус окружности (в координатах TFlex)
- `iApproxCenter`: Приближённое значение центра окружности (в координатах TFlex)
- `iCurve1`: Первая кривая
- `iCurve2`: Вторая кривая
- `iToModelSpaceScale`: Коэффициент преобразования в координаты модели

## Methods

### `CircleTangentToTwoCurvesConstructionData(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Boolean,System.Double,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,System.Double)`

ID: `M:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData.#ctor(TFDocument!System.Runtime.CompilerServices.IsConst*,System.Boolean,System.Double,TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,std.shared_ptr<RGPlatform.Geometry.Curve2DGeometry>,System.Double)`

Конструктор

Parameters:
- `iDoc`: Ссылка на документ
- `iCalculateAddInterPoints`: true - рассчитывать дополнительные точки пересечения, false - не рассчитывать
- `iRadius`: Радиус окружности (в координатах TFlex)
- `iApproxCenter`: Приближённое значение центра окружности (в координатах TFlex)
- `iCurve1`: Первая кривая
- `iCurve2`: Вторая кривая
- `iToModelSpaceScale`: Коэффициент преобразования в координаты модели

## Fields

### `_curve1`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._curve1`

### `_curve2`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._curve2`

### `_doc`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._doc`

### `_pline1`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._pline1`

### `_pline2`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._pline2`

### `_toModelSpaceScale`

ID: `F:PreciseGeometryUtils.CircleTangentToTwoCurvesConstructionData._toModelSpaceScale`
