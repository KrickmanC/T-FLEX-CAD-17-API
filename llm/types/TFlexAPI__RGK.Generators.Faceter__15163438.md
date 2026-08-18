# RGK.Generators.Faceter

Assembly: `TFlexAPI`
Namespace: `RGK.Generators`

## Constructors

### `Faceter`

ID: `M:RGK.Generators.Faceter.#ctor`

### `Faceter(RGK.Common.Context*)`

ID: `M:RGK.Generators.Faceter.#ctor(RGK.Common.Context*)`

Parameters:
- `iContext`: Контекст вычислений

### `Faceter(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.#ctor(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

## Methods

### `Faceter`

ID: `M:RGK.Generators.Faceter.#ctor`

### `Faceter(RGK.Common.Context*)`

ID: `M:RGK.Generators.Faceter.#ctor(RGK.Common.Context*)`

Parameters:
- `iContext`: Контекст вычислений

### `Faceter(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.#ctor(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `CheckEdgeForExclude(std.shared_ptr<RGK.Model.Edge>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.CheckEdgeForExclude(std.shared_ptr<RGK.Model.Edge>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iEdge`: Ребро

Returns: true - ребро должно исключаться

### `Create(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Generators.Faceter.Report*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Create(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Generators.Faceter.Report*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iData`: Parameters for the generation
- `oReport`: Result of the generation

Returns: Return resulting code

### `Create(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGK.Generators.Faceter.Report*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Create(RGK.Generators.Faceter.Data!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32,RGK.Generators.Faceter.Report*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iData`: Параметры генерации сетки
- `iStage`: Номер стадии. При значениях, не входящих в диапазон [0..N], сетка строится целиком
- `oReport`: Результаты построения сетки

### `Dispose`

ID: `M:RGK.Generators.Faceter.Dispose`

### `op_Assign(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.op_Assign(RGK.Generators.Faceter!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`
