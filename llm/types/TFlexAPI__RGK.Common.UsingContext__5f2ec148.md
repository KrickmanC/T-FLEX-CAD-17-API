# RGK.Common.UsingContext

Assembly: `TFlexAPI`
Namespace: `RGK.Common`

## Remarks

Инструментальный класс для автоматического освобождения контекста по завершении использования. Объекты данного класса удобно создавать в виде автоматических переменных при входе в метод или функцию. При выходе из функции или метода, при вызове деструктора объекта, контекст автоматически освобождается. Таким образом, отпадает необходимость ручного вызова методов Lock, Unlock

## Constructors

### `UsingContext(RGK.Common.Context*,System.Boolean)`

ID: `M:RGK.Common.UsingContext.#ctor(RGK.Common.Context*,System.Boolean)`

Parameters:
- `iContext`: Контекст
- `lock`: Необходимость автоматической блокировки контекста непосредственно в конструкторе

## Methods

### `UsingContext(RGK.Common.Context*,System.Boolean)`

ID: `M:RGK.Common.UsingContext.#ctor(RGK.Common.Context*,System.Boolean)`

Parameters:
- `iContext`: Контекст
- `lock`: Необходимость автоматической блокировки контекста непосредственно в конструкторе

### `Dispose`

ID: `M:RGK.Common.UsingContext.Dispose`

### `GetContext`

ID: `M:RGK.Common.UsingContext.GetContext`

### `op_MemberSelection`

ID: `M:RGK.Common.UsingContext.op_MemberSelection`
