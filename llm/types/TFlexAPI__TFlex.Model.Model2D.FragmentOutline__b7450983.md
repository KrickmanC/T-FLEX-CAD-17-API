# TFlex.Model.Model2D.FragmentOutline

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс линии изображения, поднятой с фрагмента

## Methods

### `Create(TFlex.Model.Document,TFlex.Model.Model2D.Fragment[],TFlex.Model.Model2D.Outline)`

ID: `M:TFlex.Model.Model2D.FragmentOutline.Create(TFlex.Model.Document,TFlex.Model.Model2D.Fragment[],TFlex.Model.Model2D.Outline)`

Создание элемента в указанном документе, соответствующего заданному элементу, находящегося на вложенном фрагменте

Parameters:
- `doc`: Документ
- `arrPath`: Массив вложенных фрагментов
- `sourceElement`: Заданный элемент

Returns: Созданный объект

Remarks: 0-й фрагмент в массиве - должен быть вложен в указанный документ. Заданный объект должен находиться на последнем фрагменте массива.

## Propertys

### `FragmentPath`

ID: `P:TFlex.Model.Model2D.FragmentOutline.FragmentPath`

Исходный объект - путь к исходному элементу

### `SubType`

ID: `P:TFlex.Model.Model2D.FragmentOutline.SubType`

Подтип линии изображения
