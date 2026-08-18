# RGK.Instance

Assembly: `TFlexAPI`
Namespace: `RGK`

## Summary

Инициализация ядра

## Methods

### `CheckResult(RGK.Common.Context*,RGK.Common.Result)`

ID: `M:RGK.Instance.CheckResult(RGK.Common.Context*,RGK.Common.Result)`

Parameters:
- `iContext`: Контекст вычисления
- `iResult`: Значение кода ошибки

Returns: Ретранслированный код ошибки

### `CheckResult(RGK.Common.Context*,std.shared_ptr<RGK.Common.ErrorReport!System.Runtime.CompilerServices.IsConst>)`

ID: `M:RGK.Instance.CheckResult(RGK.Common.Context*,std.shared_ptr<RGK.Common.ErrorReport!System.Runtime.CompilerServices.IsConst>)`

Parameters:
- `iContext`: Контекст вычисления
- `iError`: Отчёт об ошибке

Returns: Ретранслированный код ошибки

### `CheckResult(RGK.Common.Result)`

ID: `M:RGK.Instance.CheckResult(RGK.Common.Result)`

Parameters:
- `iResult`: Значение кода ошибки

Returns: Ретранслированный код ошибки

### `End`

ID: `M:RGK.Instance.End`

Returns: - Result::Success в случае успешного выполнения - Result::KernelAlreadyStopped в случае, если ядро уже было остановлено - Result::KernelNotStarted в случае, если ядро не было запущено

### `GetCLPlatform`

ID: `M:RGK.Instance.GetCLPlatform`

### `GetDeviceType(RGK.Instance.DeviceType*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Instance.GetDeviceType(RGK.Instance.DeviceType*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oDeviceType`: Тип устройства для массовых параллельных вычислений

Returns: - Result::Success в случае успешного выполнения - Result::KernelNotStarted в случае, если ядро не было запущено - Result::KernelAlreadyStopped в случае, если ядро уже было остановлено

Remarks: Получение типа устройста имеет смысл только в конфигруации библиотеки, в которой поддерживается OpenCL

### `GetErrorChecking`

ID: `M:RGK.Instance.GetErrorChecking`

Returns: Класс обработки уведомлений об ошибках

### `GetMaxThreads(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Instance.GetMaxThreads(System.Int32*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oMaxThreads`: Максимальное количество потоков, выполняемых на центральном процессоре

Returns: - Result::Success в случае успешного выполнения - Result::KernelNotStarted в случае, если ядро не было запущено - Result::KernelAlreadyStopped в случае, если ядро уже было остановлено

### `GetMeshBufferFactory`

ID: `M:RGK.Instance.GetMeshBufferFactory`

Returns: Фабрика класса, реализующего работу с буфером, в который пишутся результаты работы сеточного генератора

### `GetResultString(RGK.Common.Result,System.Boolean)`

ID: `M:RGK.Instance.GetResultString(RGK.Common.Result,System.Boolean)`

Parameters:
- `iCode`: Значение кода результата
- `iGetID`: В строке возвращать код результата

Returns: Строка, соответствующая коду результата

### `GetState(RGK.Instance.State*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Instance.GetState(RGK.Instance.State*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `oState`: Состояние ядра

Returns: - Result::Success в случае успешного выполнения

### `GetVersion`

ID: `M:RGK.Instance.GetVersion`

Returns: Номер версии

### `IsCLInitialized`

ID: `M:RGK.Instance.IsCLInitialized`

### `SetDeviceType(RGK.Instance.DeviceType)`

ID: `M:RGK.Instance.SetDeviceType(RGK.Instance.DeviceType)`

Parameters:
- `iDeviceType`: Тип устройства для массовых параллельных вычислений

Returns: - Result::Success в случае успешного выполнения - Result::KernelAlreadyStarted в случае, если ядро уже запущено

Remarks: Параметры должны задаваться до старта ядра

### `SetErrorChecking(std.shared_ptr<RGK.Interfaces.ErrorChecking>)`

ID: `M:RGK.Instance.SetErrorChecking(std.shared_ptr<RGK.Interfaces.ErrorChecking>)`

Parameters:
- `iErrorChecking`: Класс обработки уведомлений об ошибках

### `SetMaxThreads(System.Int32)`

ID: `M:RGK.Instance.SetMaxThreads(System.Int32)`

Parameters:
- `iMaxThreads`: Максимальное количество потоков, выполняемых на центральном процессоре

Returns: - Result::Success в случае успешного выполнения - Result::KernelAlreadyStarted в случае, если ядро уже запущено

Remarks: Параметры должны задаваться до старта ядра

### `SetMeshBufferFactory(std.shared_ptr<RGK.Interfaces.MeshBufferFactory>)`

ID: `M:RGK.Instance.SetMeshBufferFactory(std.shared_ptr<RGK.Interfaces.MeshBufferFactory>)`

Parameters:
- `iFactory`: Фабрика класса, реализующего работу с буфером, в который пишутся результаты работы сеточного генератора

### `Start`

ID: `M:RGK.Instance.Start`

Returns: - Result::Success в случае успешного выполнения - Result::KernelAlreadyStarted в случае, если ядро уже запущено - Result::KernelStartError в случае ошибки инициализации ядра. Обычно проблемы могут быть связаны с инициализацией устройства для массовых параллельных вычислений - Result::KernelStartPartiallySuccessful в случае возникновения некритичной ошибки в процессе инициализации - Result::KernelAlreadyStartedPartiallySuccessful в случае, если ядро уже запущено с некритичной ошибкой - Result::KernelAlreadyStartedError в случае, если ядро уже запускалось и возникла ошибка критичная для выполнения ядра
