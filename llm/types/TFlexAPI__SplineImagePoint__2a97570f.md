# SplineImagePoint

Assembly: `TFlexAPI`

## Methods

### `DerivativeDataExist`

ID: `M:SplineImagePoint.DerivativeDataExist`

Блок производных инициализирован

### `DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

ID: `M:SplineImagePoint.DetachNode(CTFObject!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean,TFDocument!System.Runtime.CompilerServices.IsConst*)`

Отвязаться от узла (обновляет координаты из узла)

Parameters:
- `srcDoc`: Документ
- `setNodeCoords`: false, если не требуется обновление координат

Returns: true - если удалось получить узел, обновить координаты и отвязаться от него

### `GetAnyDerivativeUsed`

ID: `M:SplineImagePoint.GetAnyDerivativeUsed`

Признак использования производных в точке

### `GetFirstDerivativeUsed`

ID: `M:SplineImagePoint.GetFirstDerivativeUsed`

Признак использования производных в точке

### `GetImageUID`

ID: `M:SplineImagePoint.GetImageUID`

Получить уникальный идентификатор точки

### `GetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

ID: `M:SplineImagePoint.GetPoint(TFDocument!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Double!System.Runtime.CompilerServices.IsConst)`

Получить точку в системе координат страницы

Parameters:
- `iDoc`: Документ
- `iPageScale`: Масштаб страницы

Returns: Точка в системе координат страницы

### `GetSecondDerivative`

ID: `M:SplineImagePoint.GetSecondDerivative`

Получить вторую производную в точке

### `GetUID`

ID: `M:SplineImagePoint.GetUID`

Получить уникальный идентификатор точки

### `GetUpperConstrainedDerivativeOrder`

ID: `M:SplineImagePoint.GetUpperConstrainedDerivativeOrder`

Получить макс. указанную степень производной в точке сплайна

### `InitDerivativeData`

ID: `M:SplineImagePoint.InitDerivativeData`

Инициализировать блок производных (если они не инициализирован)

### `IsCurvatureConstraint`

ID: `M:SplineImagePoint.IsCurvatureConstraint`

Кривизна ограничена

### `IsDerivativesConstraint`

ID: `M:SplineImagePoint.IsDerivativesConstraint`

Есть огранчиения производных

### `IsFirstDerivativeConstraint`

ID: `M:SplineImagePoint.IsFirstDerivativeConstraint`

Первая производная ограничена

### `IsSuppressed`

ID: `M:SplineImagePoint.IsSuppressed`

Признак подавления точки

### `IsThirdDerivativeConstraint`

ID: `M:SplineImagePoint.IsThirdDerivativeConstraint`

Третья производная ограничена

### `IsTolerant`

ID: `M:SplineImagePoint.IsTolerant`

Признак толерантной точки

### `SetForwardDirection(TFModelDirection!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:SplineImagePoint.SetForwardDirection(TFModelDirection!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Установить первую производную в точке, поднимает только флаг ограничения первой производной

Parameters:
- `iSecondDerivative`: Документ

### `SetSecondDerivative(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

ID: `M:SplineImagePoint.SetSecondDerivative(TFPoint!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Boolean)`

Установить вторую производную в точке, поднимает только флаг ограничения кривизны

Parameters:
- `iSecondDerivative`: Документ

### `Skip`

ID: `M:SplineImagePoint.Skip`

Точка подавлена, Не допустимое состояние в результате интерактивного ввода, +не допустимое состояние после препроцессинга
