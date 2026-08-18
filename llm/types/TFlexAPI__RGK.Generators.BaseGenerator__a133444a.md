# RGK.Generators.BaseGenerator

Assembly: `TFlexAPI`
Namespace: `RGK.Generators`

## Summary

Базовый класс генераторов

## Constructors

### `BaseGenerator`

ID: `M:RGK.Generators.BaseGenerator.#ctor`

### `BaseGenerator(RGK.Common.Context*)`

ID: `M:RGK.Generators.BaseGenerator.#ctor(RGK.Common.Context*)`

Конструктор

Parameters:
- `iContext`: Контекст вычисления

### `BaseGenerator(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.#ctor(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

## Methods

### `BaseGenerator`

ID: `M:RGK.Generators.BaseGenerator.#ctor`

### `BaseGenerator(RGK.Common.Context*)`

ID: `M:RGK.Generators.BaseGenerator.#ctor(RGK.Common.Context*)`

Конструктор

Parameters:
- `iContext`: Контекст вычисления

### `BaseGenerator(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.#ctor(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

### `CanHandleEvent(RGK.Generators.EventType)`

ID: `M:RGK.Generators.BaseGenerator.CanHandleEvent(RGK.Generators.EventType)`

Parameters:
- `iType`: Тип события

Returns: true - событие данного типа обрабатывается

### `Dispose`

ID: `M:RGK.Generators.BaseGenerator.Dispose`

### `GetID`

ID: `M:RGK.Generators.BaseGenerator.GetID`

Returns: Идентификатор операции

### `GetIdentify`

ID: `M:RGK.Generators.BaseGenerator.GetIdentify`

Returns: Режим идентификации топологических элементов

### `GetInterruptInfo`

ID: `M:RGK.Generators.BaseGenerator.GetInterruptInfo`

Returns: Информация о причине прерывания генератора

### `GetInterrupted`

ID: `M:RGK.Generators.BaseGenerator.GetInterrupted`

Returns: true если выполнение генератора было прервано

### `GetMonitor`

ID: `M:RGK.Generators.BaseGenerator.GetMonitor`

Returns: Монитор для отслеживания процесса выполнения генератора

### `GetTiming`

ID: `M:RGK.Generators.BaseGenerator.GetTiming`

Returns: Текущее время выполнения операции генератора

### `GetTolerance`

ID: `M:RGK.Generators.BaseGenerator.GetTolerance`

Returns: Точность вычислений

### `GetTracking`

ID: `M:RGK.Generators.BaseGenerator.GetTracking`

Returns: Режим идентификации топологических элементов

### `GetVersion`

ID: `M:RGK.Generators.BaseGenerator.GetVersion`

Returns: Номер версии

### `Init`

ID: `M:RGK.Generators.BaseGenerator.Init`

Инициализация генератора

### `Interrupt(std.shared_ptr<RGK.Generators.InterruptionInfo>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.Interrupt(std.shared_ptr<RGK.Generators.InterruptionInfo>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Прервать выполнение генератора

Parameters:
- `iInfo`: Информация о причине прерывания генератора

### `SendEvent(RGK.Generators.Event!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.SendEvent(RGK.Generators.Event!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iEvent`: Обрабатываемое событие

### `SendTimeEvent`

ID: `M:RGK.Generators.BaseGenerator.SendTimeEvent`

### `SetID(System.UInt32)`

ID: `M:RGK.Generators.BaseGenerator.SetID(System.UInt32)`

Parameters:
- `iID`: Идентификатор операции

### `SetIdentify(System.Boolean)`

ID: `M:RGK.Generators.BaseGenerator.SetIdentify(System.Boolean)`

Parameters:
- `iIdentify`: true-включить;false-выключить режим идентификации топологических элементов

### `SetMonitor(std.shared_ptr<RGK.Interfaces.MonitoringOfGenerator>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.SetMonitor(std.shared_ptr<RGK.Interfaces.MonitoringOfGenerator>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iMonitor`: Класс управления процессом выполнения генератора

Returns: Результат выполнения метода. Common::Success в случае успешного выполнения

Remarks: Генератор не удаляет объект монитора при завершении

### `SetTiming(System.Double)`

ID: `M:RGK.Generators.BaseGenerator.SetTiming(System.Double)`

Parameters:
- `iTiming`: Примерный временной интервал вызова монитора по событию временной синхронизации. Задаётся в секундах

Returns: Результат выполнения метода. Common::Success в случае успешного выполнения

### `SetTolerance(System.Double)`

ID: `M:RGK.Generators.BaseGenerator.SetTolerance(System.Double)`

Parameters:
- `iTolerance`: Точность вычислений

### `SetTracking(System.Boolean)`

ID: `M:RGK.Generators.BaseGenerator.SetTracking(System.Boolean)`

Parameters:
- `iTracking`: true-включить;false-выключить режим вывода подробной информации в класс Report генератора

### `SetVersion(RGK.Common.Version)`

ID: `M:RGK.Generators.BaseGenerator.SetVersion(RGK.Common.Version)`

Parameters:
- `iVersion`: Номер версии

### `op_Assign(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Generators.BaseGenerator.op_Assign(RGK.Generators.BaseGenerator!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`
