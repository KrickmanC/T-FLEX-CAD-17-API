# RGK.Generators.Faceter.Data

Assembly: `TFlexAPI`
Namespace: `RGK.Generators.Faceter`

## Constructors

### `Data`

ID: `M:RGK.Generators.Faceter.Data.#ctor`

### `Data(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Data.#ctor(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

## Methods

### `Data`

ID: `M:RGK.Generators.Faceter.Data.#ctor`

### `Data(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Data.#ctor(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `AddBody(std.shared_ptr<RGK.Model.Body>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Data.AddBody(std.shared_ptr<RGK.Model.Body>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iBody`: Тело, на котором строится сетка

### `AddFace(std.shared_ptr<RGK.Model.Face>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Data.AddFace(std.shared_ptr<RGK.Model.Face>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iFace`: Грань, на которой строится сетка

### `Dispose`

ID: `M:RGK.Generators.Faceter.Data.Dispose`

### `GetMaxAspectRatio`

ID: `M:RGK.Generators.Faceter.Data.GetMaxAspectRatio`

Returns: Предельно допустимое значение aspect ratio треугольников сетки

### `GetMeshGeneratorMode`

ID: `M:RGK.Generators.Faceter.Data.GetMeshGeneratorMode`

Returns: Признак сшивки граневых сеток

### `GetMeshGeneratorType`

ID: `M:RGK.Generators.Faceter.Data.GetMeshGeneratorType`

Returns: Тип сетки

### `GetNormalAngleTolerance`

ID: `M:RGK.Generators.Faceter.Data.GetNormalAngleTolerance`

Returns: Максимальное значение угла между нормалями

### `GetSideLengthTolerance`

ID: `M:RGK.Generators.Faceter.Data.GetSideLengthTolerance`

Returns: Максимально допустимая длина стороны треугольника

### `GetSurfaceDistanceTolerance`

ID: `M:RGK.Generators.Faceter.Data.GetSurfaceDistanceTolerance`

Returns: Максимальная дистанция между треугольником и поверхностью

### `SetMaxAspectRatio(System.Double)`

ID: `M:RGK.Generators.Faceter.Data.SetMaxAspectRatio(System.Double)`

Parameters:
- `iValue`: Предельно допустимое значение aspect ratio треугольников сетки

### `SetMeshGeneratorMode(RGK.Generators.Faceter.MeshGeneratorMode)`

ID: `M:RGK.Generators.Faceter.Data.SetMeshGeneratorMode(RGK.Generators.Faceter.MeshGeneratorMode)`

Parameters:
- `iDoLinkage`: Признак сшивки граневых сеток: true - сшивать, false - не сшивать

### `SetMeshGeneratorType(RGK.Generators.Faceter.MeshGeneratorType)`

ID: `M:RGK.Generators.Faceter.Data.SetMeshGeneratorType(RGK.Generators.Faceter.MeshGeneratorType)`

Parameters:
- `iMeshGeneratorType`: Тип сетки

### `SetNormalAngleTolerance(System.Double)`

ID: `M:RGK.Generators.Faceter.Data.SetNormalAngleTolerance(System.Double)`

Parameters:
- `iValue`: Максимальное значение угла между нормалями

### `SetSideLengthTolerance(System.Double)`

ID: `M:RGK.Generators.Faceter.Data.SetSideLengthTolerance(System.Double)`

Parameters:
- `iValue`: Максимально допустимая длина стороны треугольника

### `SetSurfaceDistanceTolerance(System.Double)`

ID: `M:RGK.Generators.Faceter.Data.SetSurfaceDistanceTolerance(System.Double)`

Parameters:
- `iValue`: Максимальная дистанция между треугольником и поверхностью
