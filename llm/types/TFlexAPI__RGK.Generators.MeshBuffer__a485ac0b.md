# RGK.Generators.MeshBuffer

Assembly: `TFlexAPI`
Namespace: `RGK.Generators`

## Summary

Интерфейс класса, реализующего работу с данными сетки

## Methods

### `Copy(std.shared_ptr<RGK.Generators.MeshBuffer>,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:RGK.Generators.MeshBuffer.Copy(std.shared_ptr<RGK.Generators.MeshBuffer>,System.UInt32,System.UInt32,System.UInt32)`

Parameters:
- `iMeshBuffer`: Исходный буфер, из которого копируется информация
- `iOffsetSrc`: Смещение в байтах, с которого начинается копирование
- `iOffsetDst`: Первый байт, в который производится копирование
- `iSize`: Количество копируемых байтов

Returns: Common::Success - в случае успеха (информация была скопирована из входного буфера в текущий)

### `CopyToHost(System.Void*,System.UInt32)`

ID: `M:RGK.Generators.MeshBuffer.CopyToHost(System.Void*,System.UInt32)`

Parameters:
- `iHostBuffer`: Указатель на область оперативной памяти
- `iSize`: Количество копируемых байтов

Returns: Common::Success - в случае успеха (информация была скопирована из входного буфера в текущий)

### `CopyToHost(System.Void*,System.UInt32,System.UInt32,System.UInt32)`

ID: `M:RGK.Generators.MeshBuffer.CopyToHost(System.Void*,System.UInt32,System.UInt32,System.UInt32)`

Parameters:
- `iHostBuffer`: Указатель на область оперативной памяти
- `iOffsetSrc`: Смещение в байтах, с которого начинается копирование
- `iOffsetDst`: Первый байт, в который производится копирование
- `iSize`: Количество копируемых байтов

Returns: Common::Success - в случае успеха (информация была скопирована из входного буфера в текущий)

### `Dispose`

ID: `M:RGK.Generators.MeshBuffer.Dispose`

### `GetGLId`

ID: `M:RGK.Generators.MeshBuffer.GetGLId`

Returns: Идентификатор на графическом вычислительном устройстве

### `GetGPUPointer(RGK.Common.Context*)`

ID: `M:RGK.Generators.MeshBuffer.GetGPUPointer(RGK.Common.Context*)`

Returns: Адрес на данные в памяти устройства (GPU)

### `GetHostPointer`

ID: `M:RGK.Generators.MeshBuffer.GetHostPointer`

Returns: Адрес на данные в памяти CPU

### `GetSize`

ID: `M:RGK.Generators.MeshBuffer.GetSize`

Returns: Размер буфера

### `SetData(System.Void*,System.UInt32,System.UInt32)`

ID: `M:RGK.Generators.MeshBuffer.SetData(System.Void*,System.UInt32,System.UInt32)`

Parameters:
- `iData`: Данные для записи
- `iSize`: Размер данных
- `iOffset`: Смещение в буфере

### `SetSize(System.UInt32)`

ID: `M:RGK.Generators.MeshBuffer.SetSize(System.UInt32)`

Parameters:
- `iSize`: Размер буфера

Returns: - Result::Success в случае успешного выполнения - Result::MemoryFull в случае, если не удалось выделить запрошенный объём памяти
