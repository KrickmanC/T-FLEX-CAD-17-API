# TFlex.Model.Model2D.Connector

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс коннектора

## Constructors

### `Connector(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Connector.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `Connector(TFlex.Model.Document,TFlex.Model.Model2D.Fragment,System.String)`

ID: `M:TFlex.Model.Model2D.Connector.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Fragment,System.String)`

Конструктор, создающий ссылочный коннектор фрагмента

Parameters:
- `document`: Документ объекта
- `fragment`: Фрагмент, содержащий коннектор, который требуется перевести в сборку
- `connectorComment`: Имя коннектора в документе фрагмента, который требуется перевести в сборку

## Methods

### `Connector(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.Connector.#ctor(TFlex.Model.Document)`

Конструктор по умолчанию

Parameters:
- `document`: Документ объекта

### `Connector(TFlex.Model.Document,TFlex.Model.Model2D.Fragment,System.String)`

ID: `M:TFlex.Model.Model2D.Connector.#ctor(TFlex.Model.Document,TFlex.Model.Model2D.Fragment,System.String)`

Конструктор, создающий ссылочный коннектор фрагмента

Parameters:
- `document`: Документ объекта
- `fragment`: Фрагмент, содержащий коннектор, который требуется перевести в сборку
- `connectorComment`: Имя коннектора в документе фрагмента, который требуется перевести в сборку

### `AddVariable(System.String,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.Connector.AddVariable(System.String,TFlex.Model.Parameter)`

Добавить переменную в список переменных коннектора

Parameters:
- `name`: Имя переменной
- `value`: Значение переменной

## Propertys

### `ParentFragment`

ID: `P:TFlex.Model.Model2D.Connector.ParentFragment`

Родительский фрагмент
