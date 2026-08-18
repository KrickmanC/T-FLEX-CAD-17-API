# TFlex.Model.Model2D.RevolveArray

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Круговой массив

## Constructors

### `RevolveArray(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RevolveArray.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

## Methods

### `RevolveArray(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model2D.RevolveArray.#ctor(TFlex.Model.Document)`

Стандартный конструктор

Parameters:
- `document`: Документ

### `SetRowParameters(TFlex.Model.Model2D.RevolveArrayParameters,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model2D.RevolveArray.SetRowParameters(TFlex.Model.Model2D.RevolveArrayParameters,TFlex.Model.Parameter,TFlex.Model.Parameter,TFlex.Model.Parameter)`

Установка параметров массива

Parameters:
- `paramsSet`: Набор параметров, которые устанавливаются функцией
- `arrFullAngle`: Общая угол массива
- `arrStepAngle`: Шаг угла для элементов
- `arrNumber`: Количество элементов

Remarks: В зависимости от заданного набора задаваемых параметров (paramsSet), оставшийся параметр будет автоматически рассчитываться по заданным двум (его значение, переданное в функцию будет проигнорировано).

## Propertys

### `CenterNode`

ID: `P:TFlex.Model.Model2D.RevolveArray.CenterNode`

Центральный узел

### `CenterX`

ID: `P:TFlex.Model.Model2D.RevolveArray.CenterX`

X-координата центра массива

Remarks: Если установлен центральный узел - изменения координат будет проигнорировано

### `CenterY`

ID: `P:TFlex.Model.Model2D.RevolveArray.CenterY`

Y-координата центра массива

Remarks: Если установлен центральный узел - изменения координат будет проигнорировано

### `CopyType`

ID: `P:TFlex.Model.Model2D.RevolveArray.CopyType`

Подтип операции копирования
