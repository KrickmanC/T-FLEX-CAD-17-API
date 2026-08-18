# RGK.Common.Context

Assembly: `TFlexAPI`
Namespace: `RGK.Common`

## Summary

Контекст вычислений в модели

## Remarks

Контекст передаётся всем функциям, работающим с моделью. Контекст используется для решения следующих задач: - Протоколирование изменений в модели; - Синхронизация параллельных вычислений; - Доступ к активному набору данных (сессии) ядра; - Получение параметров точности и других настроек ядра;

## Methods

### `BeginChanges(RGK.Common.ContextState*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Context.BeginChanges(RGK.Common.ContextState*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oState`: Метка текущего состояния контекста, перед началом изменений. Метка становится неактуальной(точнее переносится в сессиию) при разблокировании тел.

Returns: - Result::Success в случае успешного выполнения

### `CanLockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Context.CanLockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iModified`: Список тел, предполагаемых к модификации
- `iCalculated`: Список тел, используемых для вычислений

Returns: - Result::Success в случае, если блокировка возможна - Result::CannotCalculateModifiedBody тело нельзя блокировать для вычислений, так как оно заблокировано для редактирования - Result::CannotModifyModifiedBody Тело нельзя блокировать для редактирования, так как оно заблокировано для редактирования в другом контексте. - Result::CannotModifyCalculatedBody Тело нельзя блокировать для редактирования, так как оно заблокировано для вычислений.

### `GetAngularPrecision`

ID: `M:RGK.Common.Context.GetAngularPrecision`

Угловая точность сессии ядра

Returns: Угловая точность вычислений в текущей сессии ядра

### `GetChangeLog`

ID: `M:RGK.Common.Context.GetChangeLog`

Returns: Текущий журнал изменений

### `GetLinearPrecision`

ID: `M:RGK.Common.Context.GetLinearPrecision`

Линейная точность сессии ядра

Returns: Линейная точность вычислений в текущей сессии ядра

### `GetMaxThreads`

ID: `M:RGK.Common.Context.GetMaxThreads`

Returns: Максимальное количество потоков, которое может запускаться внутри ядра для данного контекста

### `GetSession`

ID: `M:RGK.Common.Context.GetSession`

Returns: Сессия контекста

### `GetSizeBox`

ID: `M:RGK.Common.Context.GetSizeBox`

Максимально допустимые габариты модели

Returns: Максимально допустимые габариты модели в текущей сессии ядра

### `GetUnitPrecision`

ID: `M:RGK.Common.Context.GetUnitPrecision`

### `IsErrorCheckingSuppressed`

ID: `M:RGK.Common.Context.IsErrorCheckingSuppressed`

Returns: Подавить вывод диагностики об ошибках

### `LockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Context.LockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iModified`: Список тел, предполагаемых к модификации
- `iCalculated`: Список тел, используемых для вычислений

Returns: - Result::Success в случае, если блокировка выполнена - Result::CannotCalculateModifiedBody тело нельзя блокировать для вычислений, так как оно заблокировано для редактирования - Result::CannotModifyModifiedBody Тело нельзя блокировать для редактирования, так как оно заблокировано для редактирования в другом контексте. - Result::CannotModifyCalculatedBody Тело нельзя блокировать для редактирования, так как оно заблокировано для вычислений.

### `SetLock`

ID: `M:RGK.Common.Context.SetLock`

### `SetMaxThreads(System.UInt32)`

ID: `M:RGK.Common.Context.SetMaxThreads(System.UInt32)`

Parameters:
- `iMaxThreads`: Максимальное количество потоков, которое может запускаться внутри ядра для данного контекста

### `SuppressErrorChecking(System.Boolean)`

ID: `M:RGK.Common.Context.SuppressErrorChecking(System.Boolean)`

Parameters:
- `iSuppress`: Подавить вывод диагностики об ошибках

Returns: Предыдущее значение

### `Undo(RGK.Common.ContextState!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Context.Undo(RGK.Common.ContextState!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iState`: Метка, до которой выполняется откат. Все изменения удаляются. То есть повторить изменения не получится

### `UnlockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Context.UnlockParts(std.vector<std.shared_ptr<RGK.Model.Part>,std.allocator<std.shared_ptr<RGK.Model.Part>>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iParts`: Список ранее заблокированных в данном контексте тел

Returns: - Result::Success в случае, если разблокировка выполнена - Result::CannotUnlockBody Тело не было блокировано контекстом или количество разблокировок больше количества блокировок.

### `UnsetLock`

ID: `M:RGK.Common.Context.UnsetLock`

## Members

### `ChangeList`

ID: `D:RGK.Common.Context.ChangeList`
