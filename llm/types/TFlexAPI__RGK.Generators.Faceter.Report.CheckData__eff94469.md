# RGK.Generators.Faceter.Report.CheckData

Assembly: `TFlexAPI`
Namespace: `RGK.Generators.Faceter.Report`

## Constructors

### `CheckData`

ID: `M:RGK.Generators.Faceter.Report.CheckData.#ctor`

### `CheckData(System.Double,System.Double,System.Double)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.#ctor(System.Double,System.Double,System.Double)`

## Methods

### `CheckData`

ID: `M:RGK.Generators.Faceter.Report.CheckData.#ctor`

### `CheckData(System.Double,System.Double,System.Double)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.#ctor(System.Double,System.Double,System.Double)`

### `Dispose`

ID: `M:RGK.Generators.Faceter.Report.CheckData.Dispose`

### `GetCheckAngularTolerance`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckAngularTolerance`

Returns: Флаг проверки, что угловое уклонение внутри параметрической области треугольника не больше максимально допустимого

### `GetCheckChordalMaximumLength`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckChordalMaximumLength`

Returns: Флаг проверки, что длина стороны треугольника не больше максимально допустимой

### `GetCheckDegeneratedFaces`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckDegeneratedFaces`

Returns: Флаг проверки вырожденных треугольников

### `GetCheckHoles`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckHoles`

Returns: Флаг проверки дырок

### `GetCheckIntersection`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckIntersection`

Returns: Флаг проверки пересечения треугольников в UV-области

### `GetCheckLinearTolerance`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckLinearTolerance`

Returns: Флаг проверки, что расстояние между треугольником и поверхностью не больше максимально допустимого

### `GetCheckSelfIntersections`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckSelfIntersections`

Returns: Флаг проверки самопересечений

### `GetCheckSideAngularTolerance`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetCheckSideAngularTolerance`

Returns: Флаг проверки, что угловое уклонение между соседними треугольниками одной грани не больше максимально допустимого

### `GetDegeneracyParameters(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetDegeneracyParameters(System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oArea`: Минимально допустимая площадь треугольника
- `oUVArea`: Минимально допустимая площадь треугольника в UV
- `oAngle`: Минимально допустимый угол

### `GetFaceterData`

ID: `M:RGK.Generators.Faceter.Report.CheckData.GetFaceterData`

Returns: Параметры сеточного разбиения

### `SetCheckAngularTolerance(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckAngularTolerance(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки, что угловое уклонение внутри параметрической области треугольника не больше максимально допустимого

### `SetCheckChordalMaximumLength(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckChordalMaximumLength(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки, что длина стороны треугольника не больше максимально допустимой

### `SetCheckDegeneratedFaces(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckDegeneratedFaces(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки вырожденных треугольников

### `SetCheckHoles(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckHoles(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки дырок

### `SetCheckIntersection(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckIntersection(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки пересечения треугольников в UV-области

### `SetCheckLinearTolerance(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckLinearTolerance(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки, что расстояние между треугольником и поверхностью не больше максимально допустимого

### `SetCheckSelfIntersection(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckSelfIntersection(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки дырок

### `SetCheckSideAngularTolerance(System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetCheckSideAngularTolerance(System.Boolean)`

Parameters:
- `iCheck`: Флаг проверки, что угловое уклонение между соседними треугольниками одной грани не больше максимально допустимого

### `SetDegeneracyParameters(System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetDegeneracyParameters(System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst,System.Double!System.Runtime.CompilerServices.IsConst)`

Parameters:
- `iArea`: Минимально допустимая площадь треугольника
- `iUVArea`: Минимально допустимая площадь треугольника в UV
- `iAngle`: Минимально допустимый угол

### `SetFaceterData(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Report.CheckData.SetFaceterData(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iFacetParameters`: Параметры сеточного разбиения
