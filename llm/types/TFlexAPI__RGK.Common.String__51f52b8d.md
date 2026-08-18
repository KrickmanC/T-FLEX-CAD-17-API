# RGK.Common.String

Assembly: `TFlexAPI`
Namespace: `RGK.Common`

## Remarks

Если класс объявить как DLLEXPORT и поместить реализацию в cpp-файл, то возникает проблема, описанная здесь: http://social.msdn.microsoft.com/Forums/en/vclanguage/thread/191de00a-53c9-4bd9-9cb6-e844eb224ca2 Поэтому String сделан inline-классом. Но в этом случае код для методов String будет сгенерирован в разных модулях. Чтобы избежать связанных с этим LNK4217 и LNK4049 в MSVC, нужно включить Function-level linking опцией /Gy.

## Constructors

### `String`

ID: `M:RGK.Common.String.#ctor`

### `String(RGK.Common.String!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(RGK.Common.String!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iSource`: Исходная строка для создания копии

### `String(System.Char!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Common.String.#ctor(System.Char!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `str`: Исходная строка в формате wchar_t для создания копии

### `String(System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Common.String.#ctor(System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `str`: Исходная строка в формате UTF-8 для создания копии

### `String(std.basic_string<System.Char,std.char_traits{System.Char},std.allocator<System.Char>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(std.basic_string<System.Char,std.char_traits{System.Char},std.allocator<System.Char>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `str`: Исходная строка в формате wchar_t для создания копии

### `String(std.basic_string<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte,std.char_traits{System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte},std.allocator<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(std.basic_string<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte,std.char_traits{System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte},std.allocator<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `str`: Исходная строка в формате UTF-8 для создания копии

## Methods

### `String`

ID: `M:RGK.Common.String.#ctor`

### `String(RGK.Common.String!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(RGK.Common.String!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `iSource`: Исходная строка для создания копии

### `String(System.Char!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Common.String.#ctor(System.Char!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `str`: Исходная строка в формате wchar_t для создания копии

### `String(System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte!System.Runtime.CompilerServices.IsConst*)`

ID: `M:RGK.Common.String.#ctor(System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte!System.Runtime.CompilerServices.IsConst*)`

Parameters:
- `str`: Исходная строка в формате UTF-8 для создания копии

### `String(std.basic_string<System.Char,std.char_traits{System.Char},std.allocator<System.Char>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(std.basic_string<System.Char,std.char_traits{System.Char},std.allocator<System.Char>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `str`: Исходная строка в формате wchar_t для создания копии

### `String(std.basic_string<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte,std.char_traits{System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte},std.allocator<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

ID: `M:RGK.Common.String.#ctor(std.basic_string<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte,std.char_traits{System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte},std.allocator<System.SByte!System.Runtime.CompilerServices.IsSignUnspecifiedByte>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced)`

Parameters:
- `str`: Исходная строка в формате UTF-8 для создания копии

## Members

### `codecvt_utf8`

ID: `D:RGK.Common.String.codecvt_utf8`

### `utf8_wstring_convert`

ID: `D:RGK.Common.String.utf8_wstring_convert`
