# DrawDimUtils

Assembly: `TFlexAPI`

## Methods

### `AsPoint(TFM.SSE.Vector2d!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:DrawDimUtils.AsPoint(TFM.SSE.Vector2d!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Получить TF2D::Point как TFPoint

Parameters:
- `iPoint`: Конвертируемая точка типа TF2D::Point

Returns: Сконвертированная точка типа TFPoint

### `Transform(TFPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFM.SSE.Matrix3d!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:DrawDimUtils.Transform(TFPoint*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,TFM.SSE.Matrix3d!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Трансформировать точку

Parameters:
- `ioPoint`: Точка, к которой применяются преобразования
- `iMap`: Карта преобразований
