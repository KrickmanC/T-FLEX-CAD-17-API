# ExpressionCompilerError

Assembly: `TFlexAPI3D`

## Constructors

### `ExpressionCompilerError`

ID: `M:ExpressionCompilerError.#ctor`

## Methods

### `ExpressionCompilerError`

ID: `M:ExpressionCompilerError.#ctor`

### `Clear`

ID: `M:ExpressionCompilerError.Clear`

Сбрасывает информацию об ошибках

### `HasError`

ID: `M:ExpressionCompilerError.HasError`

Возвращает флаг наличия ошибки

Returns: Возвращает true при наличии ошибки, false - при отсутствии

### `Length`

ID: `M:ExpressionCompilerError.Length`

Длина ошибки, выраженная в количестве символов(необходимо для подсветки ошибки)

Returns: Возвращает длину ошибочной части строки выражения, тип std::size_t

### `StartAt`

ID: `M:ExpressionCompilerError.StartAt`

Возвращает исходную позицию, с которой начинается ошибка, в переданном выражении(необходимо для подсветки ошибки)

Returns: Возвращает начальную позицию ошибки, тип std::size_t

### `What`

ID: `M:ExpressionCompilerError.What`

Возвращает строку с описанием ошибки компиляции выражения

Returns: Возвращает текст ошибки, тип std::wstring
