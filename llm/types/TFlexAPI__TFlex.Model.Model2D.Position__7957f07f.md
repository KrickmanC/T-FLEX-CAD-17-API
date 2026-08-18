# TFlex.Model.Model2D.Position

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Положение курсора в тексте

## Constructors

### `Position(System.Int32)`

ID: `M:TFlex.Model.Model2D.Position.#ctor(System.Int32)`

Конструктор

Parameters:
- `ch`: Порядковый номер символа

### `Position(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model2D.Position.#ctor(System.Int32,System.Int32,System.Int32)`

Конструктор

Parameters:
- `ch`: Порядковый номер символа
- `tableIndex`: Порядковый номер таблицы относительно начала текста
- `cellIndex`: Порядковый номер ячейки таблицы

## Methods

### `Position(System.Int32)`

ID: `M:TFlex.Model.Model2D.Position.#ctor(System.Int32)`

Конструктор

Parameters:
- `ch`: Порядковый номер символа

### `Position(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model2D.Position.#ctor(System.Int32,System.Int32,System.Int32)`

Конструктор

Parameters:
- `ch`: Порядковый номер символа
- `tableIndex`: Порядковый номер таблицы относительно начала текста
- `cellIndex`: Порядковый номер ячейки таблицы

### `InTable`

ID: `M:TFlex.Model.Model2D.Position.InTable`

Получение информации о положении в таблице

Returns: true, если положение в таблице задано

## Fields

### `Character`

ID: `F:TFlex.Model.Model2D.Position.Character`

Порядковый номер символа

Remarks: Если положение курсора в таблице заданно то рассматривается относительно начала ячейки таблицы. В противном случае - относительно начала текста.

### `Table`

ID: `F:TFlex.Model.Model2D.Position.Table`

Положение курсора в таблице
