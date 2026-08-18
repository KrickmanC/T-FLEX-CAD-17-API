# TFlex.Model.Model2D.FragmentNode

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс узла, построенного на основе элемента фрагмента

## Methods

### `Create(TFlex.Model.Document,TFlex.Model.Model2D.Fragment[],TFlex.Model.Model2D.Object2D,System.Int32)`

ID: `M:TFlex.Model.Model2D.FragmentNode.Create(TFlex.Model.Document,TFlex.Model.Model2D.Fragment[],TFlex.Model.Model2D.Object2D,System.Int32)`

Создание узла в указанном документе, соответствующего заданному узлу элемента, находящегося на вложенном фрагменте

Parameters:
- `document`: Документ
- `arrPath`: Массив вложенных фрагментов
- `sourceElement`: Заданный элемент
- `id`: Идентификатор узла элемента

Returns: Созданный объект

Remarks: 0-й фрагмент в массиве - должен быть вложен в указанный документ. Заданный объект должен находиться на последнем фрагменте массива. В данный момент возможно создание узла на конце (id=1) или в начале (id=0) линии построения.

## Propertys

### `FragmentPath`

ID: `P:TFlex.Model.Model2D.FragmentNode.FragmentPath`

Объект, задающий путь к исходному элементу

### `SubType`

ID: `P:TFlex.Model.Model2D.FragmentNode.SubType`

Подтип узла
