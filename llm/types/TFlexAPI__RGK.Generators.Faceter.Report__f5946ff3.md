# RGK.Generators.Faceter.Report

Assembly: `TFlexAPI`
Namespace: `RGK.Generators.Faceter`

## Constructors

### `Report`

ID: `M:RGK.Generators.Faceter.Report.#ctor`

## Methods

### `Report`

ID: `M:RGK.Generators.Faceter.Report.#ctor`

### `BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Report.BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `ioData`: Информация о буферах, в которые пишется сетка

Returns: - Result::Success в случае успешного выполнения - Result::MemoryFull в случае, если не удалось выделить запрошенный объём памяти

### `BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Report.BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `ioData`: Информация о буферах, в которые пишется сетка
- `oBounds`: Ограничивающий параллелепипед

Returns: - Result::Success в случае успешного выполнения - Result::MemoryFull в случае, если не удалось выделить запрошенный объём памяти

### `BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*,System.Boolean)`

ID: `M:RGK.Generators.Faceter.Report.BuildMeshData(RGK.Common.Context*,RGK.Generators.BufferedMeshData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Math.BoundingBox*,System.Boolean)`

### `Check(RGK.Common.Context*,RGK.Generators.Faceter.Report.CheckData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Generators.Faceter.Report.CheckReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.Faceter.Report.Check(RGK.Common.Context*,RGK.Generators.Faceter.Report.CheckData!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,RGK.Generators.Faceter.Report.CheckReport*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iData`: Данные для проверки
- `oReport`: Результат проверки

Returns: - Result::Success в случае успешного выполнения

### `Dispose`

ID: `M:RGK.Generators.Faceter.Report.Dispose`

### `GetErrorStage`

ID: `M:RGK.Generators.Faceter.Report.GetErrorStage`

Returns: Номер стадии

### `GetMesh`

ID: `M:RGK.Generators.Faceter.Report.GetMesh`

### `GetMeshPtr`

ID: `M:RGK.Generators.Faceter.Report.GetMeshPtr`

### `GetRetCode`

ID: `M:RGK.Generators.Faceter.Report.GetRetCode`

Returns: Результат построения сетки

### `ResetRetCode(RGK.Generators.Faceter.Report.RetCode,System.UInt32)`

ID: `M:RGK.Generators.Faceter.Report.ResetRetCode(RGK.Generators.Faceter.Report.RetCode,System.UInt32)`

Parameters:
- `iRetCode`: Результат построения сетки
- `iErrorStage`: Номер стадии, на котором произошла ошибка

## Fields

### `_errorStage`

ID: `F:RGK.Generators.Faceter.Report._errorStage`

### `_mesh`

ID: `F:RGK.Generators.Faceter.Report._mesh`

### `_retCode`

ID: `F:RGK.Generators.Faceter.Report._retCode`
