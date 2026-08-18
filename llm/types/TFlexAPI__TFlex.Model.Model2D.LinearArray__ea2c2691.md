# TFlex.Model.Model2D.LinearArray

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Линейный массив

## Constructors

### `LinearArray(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LinearArray.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

## Methods

### `LinearArray(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.LinearArray.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

### `GetColumnEditVariable(TFlex.Model.Variableref ,TFlex.Model.Model2D.LinearArray.EditVariableTyperef )`

ID: `M:TFlex.Model.Model2D.LinearArray.GetColumnEditVariable(TFlex.Model.Variable@,TFlex.Model.Model2D.LinearArray.EditVariableType@)`

Получить информацию о переменной строки

Parameters:
- `variable`: Переменная
- `type`: Тип

### `GetRowEditVariable(TFlex.Model.Variableref ,TFlex.Model.Model2D.LinearArray.EditVariableTyperef )`

ID: `M:TFlex.Model.Model2D.LinearArray.GetRowEditVariable(TFlex.Model.Variable@,TFlex.Model.Model2D.LinearArray.EditVariableType@)`

Получить информацию о переменной строки

Parameters:
- `variable`: Переменная
- `type`: Тип

### `SetColumnEditVariable(TFlex.Model.Variable,TFlex.Model.Model2D.LinearArray.EditVariableType)`

ID: `M:TFlex.Model.Model2D.LinearArray.SetColumnEditVariable(TFlex.Model.Variable,TFlex.Model.Model2D.LinearArray.EditVariableType)`

Установить переменную столбца

Parameters:
- `variable`: Переменная
- `type`: Тип

### `SetColumnParameters(TFlex.Model.Model2D.LinearArrayParameters,TFlex.Model.Model2D.NodeNeeds,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LinearArray.SetColumnParameters(TFlex.Model.Model2D.LinearArrayParameters,TFlex.Model.Model2D.NodeNeeds,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров столбцов массива

Parameters:
- `paramsSet`: Набор параметров, которые устанавливаются функцией
- `nodeNeed`: Указывает способ использования конечной точка
- `colsLength`: Общая длина массива в направлении столбцов
- `colsStep`: Шаг столбцов
- `colsNumber`: Количество столбцов

Remarks: В зависимости от заданного набора задаваемых параметров (paramsSet), оставшийся параметр будет автоматически рассчитываться по заданным двум (его значение, переданное в функцию будет проигнорировано). В зависимости от заданного флага узла (nodeNeed), переданное в функцию значение параметра, получаемого с узла, будет проигнорировано. При попытке указать для получения по конечной точке привязки расчитываемого значения, nodeNeed будет автоматически установлен в None.

### `SetRowEditVariable(TFlex.Model.Variable,TFlex.Model.Model2D.LinearArray.EditVariableType)`

ID: `M:TFlex.Model.Model2D.LinearArray.SetRowEditVariable(TFlex.Model.Variable,TFlex.Model.Model2D.LinearArray.EditVariableType)`

Установить переменную строки

Parameters:
- `variable`: Переменная
- `type`: Тип

### `SetRowParameters(TFlex.Model.Model2D.LinearArrayParameters,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.LinearArray.SetRowParameters(TFlex.Model.Model2D.LinearArrayParameters,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров рядов массива

Parameters:
- `paramsSet`: Набор параметров, которые устанавливаются функцией
- `rowsLength`: Общая длина массива в направлении рядов
- `rowsStep`: Шаг рядов
- `rowsNumber`: Количество рядов

Remarks: В зависимости от заданного набора задаваемых параметров (paramsSet), оставшийся параметр будет автоматически рассчитываться по заданным двум (его значение, переданное в функцию будет проигнорировано).

## Propertys

### `CopyType`

ID: `P:TFlex.Model.Model2D.LinearArray.CopyType`

Подтип операции копирования

### `EndNode`

ID: `P:TFlex.Model.Model2D.LinearArray.EndNode`

Конечный узел

### `EndX`

ID: `P:TFlex.Model.Model2D.LinearArray.EndX`

X-координата конечной точки

Remarks: Если установлен начальный узел - изменения координат будет проигнорировано

### `EndY`

ID: `P:TFlex.Model.Model2D.LinearArray.EndY`

Y-координата конечной точки

Remarks: Если установлен начальный узел - изменения координат будет проигнорировано

### `StartNode`

ID: `P:TFlex.Model.Model2D.LinearArray.StartNode`

Начальный узел

### `StartX`

ID: `P:TFlex.Model.Model2D.LinearArray.StartX`

X-координата начальной точки

Remarks: Если установлен начальный узел - изменения координат будет проигнорировано

### `StartY`

ID: `P:TFlex.Model.Model2D.LinearArray.StartY`

Y-координата начальной точки

Remarks: Если установлен начальный узел - изменения координат будет проигнорировано
