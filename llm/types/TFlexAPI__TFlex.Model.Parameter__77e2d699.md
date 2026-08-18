# TFlex.Model.Parameter

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс для хранения чиcловых переменных или констант

## Remarks

В отличие от класса хранения переменных и выражений данный класс не является экземпляром модели. Этот инструментальный класс используется для упрощения работы с параметрами объектов модели, которые могут задаваться как переменными, так и константами

## Constructors

### `Parameter(System.Double)`

ID: `M:TFlex.Model.Parameter.#ctor(System.Double)`

Конструктор для создания параметра, заданного вещественной константой

Parameters:
- `value`: Вещественная константа

### `Parameter(System.Int32)`

ID: `M:TFlex.Model.Parameter.#ctor(System.Int32)`

Конструктор для создания параметра, заданного целочисленной константой

Parameters:
- `value`: Целочисленная константа

### `Parameter(TFlex.Model.Variable)`

ID: `M:TFlex.Model.Parameter.#ctor(TFlex.Model.Variable)`

Конструктор для создания параметра, заданного переменной

Parameters:
- `var`: Переменная

## Methods

### `Parameter(System.Double)`

ID: `M:TFlex.Model.Parameter.#ctor(System.Double)`

Конструктор для создания параметра, заданного вещественной константой

Parameters:
- `value`: Вещественная константа

### `Parameter(System.Int32)`

ID: `M:TFlex.Model.Parameter.#ctor(System.Int32)`

Конструктор для создания параметра, заданного целочисленной константой

Parameters:
- `value`: Целочисленная константа

### `Parameter(TFlex.Model.Variable)`

ID: `M:TFlex.Model.Parameter.#ctor(TFlex.Model.Variable)`

Конструктор для создания параметра, заданного переменной

Parameters:
- `var`: Переменная

### `Default`

ID: `M:TFlex.Model.Parameter.Default`

Возвращает параметр с данными "из статуса"

## Propertys

### `IntValue`

ID: `P:TFlex.Model.Parameter.IntValue`

Константное значение в виде целого числа

### `Value`

ID: `P:TFlex.Model.Parameter.Value`

Константное значение в виде вещественного числа

### `Variable`

ID: `P:TFlex.Model.Parameter.Variable`

Ссылка на переменную
