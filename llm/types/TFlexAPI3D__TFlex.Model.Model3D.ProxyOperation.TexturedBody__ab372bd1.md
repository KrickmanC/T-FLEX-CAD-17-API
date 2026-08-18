# TFlex.Model.Model3D.ProxyOperation.TexturedBody

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.ProxyOperation`

## Summary

Класс для задания параметров рисования тела

## Constructors

### `TexturedBody(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.TexturedBody.#ctor(TFlex.Model.Model3D.Geometry.BaseBody)`

Конструктор для задания тела с параметрами рисования из общих свойств внешней операции

Parameters:
- `solid`: Тело

### `TexturedBody(TFlex.Model.Model3D.Geometry.BaseBody,TFlex.Model.Model3D.Material,System.Int32,System.Double)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.TexturedBody.#ctor(TFlex.Model.Model3D.Geometry.BaseBody,TFlex.Model.Model3D.Material,System.Int32,System.Double)`

Конструктор для задания тела с индивидуальными параметрами рисования

Parameters:
- `solid`: Тело
- `material`: Материал
- `color`: Цвет
- `complexity`: 

## Methods

### `TexturedBody(TFlex.Model.Model3D.Geometry.BaseBody)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.TexturedBody.#ctor(TFlex.Model.Model3D.Geometry.BaseBody)`

Конструктор для задания тела с параметрами рисования из общих свойств внешней операции

Parameters:
- `solid`: Тело

### `TexturedBody(TFlex.Model.Model3D.Geometry.BaseBody,TFlex.Model.Model3D.Material,System.Int32,System.Double)`

ID: `M:TFlex.Model.Model3D.ProxyOperation.TexturedBody.#ctor(TFlex.Model.Model3D.Geometry.BaseBody,TFlex.Model.Model3D.Material,System.Int32,System.Double)`

Конструктор для задания тела с индивидуальными параметрами рисования

Parameters:
- `solid`: Тело
- `material`: Материал
- `color`: Цвет
- `complexity`: 

## Propertys

### `Color`

ID: `P:TFlex.Model.Model3D.ProxyOperation.TexturedBody.Color`

Номер цвета, если он задан

### `Complexity`

ID: `P:TFlex.Model.Model3D.ProxyOperation.TexturedBody.Complexity`

Плотность сетки, если она задана

Remarks: Плотность сетки задаётся значением в интервале от 0.0 до 1.0.

### `Material`

ID: `P:TFlex.Model.Model3D.ProxyOperation.TexturedBody.Material`

Материал, если он задан

### `Solid`

ID: `P:TFlex.Model.Model3D.ProxyOperation.TexturedBody.Solid`

Тело
