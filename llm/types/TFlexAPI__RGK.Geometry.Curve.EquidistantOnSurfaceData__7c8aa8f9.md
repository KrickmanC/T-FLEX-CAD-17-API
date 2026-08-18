# RGK.Geometry.Curve.EquidistantOnSurfaceData

Assembly: `TFlexAPI`
Namespace: `RGK.Geometry.Curve`

## Summary

Параметры построения эквидистантной кривой

## Constructors

### `EquidistantOnSurfaceData(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

ID: `M:RGK.Geometry.Curve.EquidistantOnSurfaceData.#ctor(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

Parameters:
- `iOffset`: Положительная величина смещения
- `iInterval`: Параметрический интервал кривой, для которого строится смещение
- `iSurface`: Поверхность, по которой строится смещение
- `iMethod`: Метод смещения. По умолчанию, по геодезической линии
- `iTolerance`: Запрашиваемая точность построения эквидистанты. По умолчанию, 1.0e-5
- `iSide`: Выбираемая сторона. По умолчанию, Left

### `EquidistantOnSurfaceData(std.shared_ptr<RGK.Generators.ScalarLaw>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

ID: `M:RGK.Geometry.Curve.EquidistantOnSurfaceData.#ctor(std.shared_ptr<RGK.Generators.ScalarLaw>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

Parameters:
- `iOffsetLaw`: Кривая, задающая по X-компоненте переменную величину смещения. Параметризация кривой, для которой строится смещение, и кривой закона совпадают на интервале, на котором строится смещение
- `iInterval`: Параметрический интервал кривой, для которого строится смещение
- `iSurface`: Поверхность, по которой строится смещение
- `iMethod`: Метод смещения. По умолчанию, по геодезической линии
- `iTolerance`: Запрашиваемая точность построения эквидистанты. По умолчанию, 1.0e-5
- `iSide`: Выбираемая сторона. По умолчанию, Left

## Methods

### `EquidistantOnSurfaceData(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

ID: `M:RGK.Geometry.Curve.EquidistantOnSurfaceData.#ctor(System.Double,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

Parameters:
- `iOffset`: Положительная величина смещения
- `iInterval`: Параметрический интервал кривой, для которого строится смещение
- `iSurface`: Поверхность, по которой строится смещение
- `iMethod`: Метод смещения. По умолчанию, по геодезической линии
- `iTolerance`: Запрашиваемая точность построения эквидистанты. По умолчанию, 1.0e-5
- `iSide`: Выбираемая сторона. По умолчанию, Left

### `EquidistantOnSurfaceData(std.shared_ptr<RGK.Generators.ScalarLaw>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

ID: `M:RGK.Geometry.Curve.EquidistantOnSurfaceData.#ctor(std.shared_ptr<RGK.Generators.ScalarLaw>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Interval!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.shared_ptr<RGK.Geometry.Surface!System.Runtime.CompilerServices.IsConst>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetMethod,System.Double,RGK.Geometry.Curve.EquidistantOnSurfaceData.OffsetSide)`

Parameters:
- `iOffsetLaw`: Кривая, задающая по X-компоненте переменную величину смещения. Параметризация кривой, для которой строится смещение, и кривой закона совпадают на интервале, на котором строится смещение
- `iInterval`: Параметрический интервал кривой, для которого строится смещение
- `iSurface`: Поверхность, по которой строится смещение
- `iMethod`: Метод смещения. По умолчанию, по геодезической линии
- `iTolerance`: Запрашиваемая точность построения эквидистанты. По умолчанию, 1.0e-5
- `iSide`: Выбираемая сторона. По умолчанию, Left

### `Dispose`

ID: `M:RGK.Geometry.Curve.EquidistantOnSurfaceData.Dispose`
