# RGK.Common.Version

Assembly: `TFlexAPI`
Namespace: `RGK.Common`

## Summary

Номер версии ядра

## Constructors

### `Version`

ID: `M:RGK.Common.Version.#ctor`

### `Version(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Version.#ctor(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVersion`: Номер версии

### `Version(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:RGK.Common.Version.#ctor(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

Parameters:
- `iMajor`: Номер основной версии ядра
- `iMinor`: Номер вспомогательной версии ядра
- `iBuild`: Номер сборки
- `iRevision`: Номер исправлений в сборке

Remarks: Используется для задания текущей версии ядра в Instance

## Methods

### `Version`

ID: `M:RGK.Common.Version.#ctor`

### `Version(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Version.#ctor(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVersion`: Номер версии

### `Version(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:RGK.Common.Version.#ctor(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

Parameters:
- `iMajor`: Номер основной версии ядра
- `iMinor`: Номер вспомогательной версии ядра
- `iBuild`: Номер сборки
- `iRevision`: Номер исправлений в сборке

Remarks: Используется для задания текущей версии ядра в Instance

### `GetSubVersion(RGK.Common.Version.Type)`

ID: `M:RGK.Common.Version.GetSubVersion(RGK.Common.Version.Type)`

Получить часть номера версии по типу

Parameters:
- `iType`: Тип части версии

Returns: Номер версии

### `GetVersion(System.UInt32*)`

ID: `M:RGK.Common.Version.GetVersion(System.UInt32*)`

Получить номер версии

Parameters:
- `oVersion`: Номер версии

### `SetVersion(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:RGK.Common.Version.SetVersion(System.UInt32,System.UInt32,System.UInt32,System.UInt32)`

Установить номер версии

Parameters:
- `iMajor`: Номер основной версии ядра
- `iMinor`: Номер вспомогательной версии ядра
- `iBuild`: Номер сборки
- `iRevision`: Номер исправлений в сборке

Returns: - Result::Success в случае успешного выполнения - Result::BadVersion - недопустимый номер версии

Remarks: Используется для выбора версии генератора

### `op_Assign(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Version.op_Assign(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVersion`: Номер версии

Returns: Ссылка на сам объект

### `op_Equality(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Version.op_Equality(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVersion`: Номер версии

Returns: true-версии совпадают

### `op_LessThan(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.Version.op_LessThan(RGK.Common.Version!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iVersion`: Номер версии

Returns: true-версия более ранняя по сравнению с передаваемой в параметре
