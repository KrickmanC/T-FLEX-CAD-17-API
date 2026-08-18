# TFlex.Model.Model3D.View3D.LightParameters

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.View3D`

## Summary

Параметры освещения 3D вида

## Remarks

Освещение складывается из рассеянного освещения и направленных источников света. Наличие направленных источников необязательно. Их максимальное число зависит от используемой видеокарты и драйверов OpenGL.

## Constructors

### `LightParameters`

ID: `M:TFlex.Model.Model3D.View3D.LightParameters.#ctor`

Конструктор по умолчанию

Remarks: Создаётся один направленный источник света с параметрами по умолчанию

## Methods

### `LightParameters`

ID: `M:TFlex.Model.Model3D.View3D.LightParameters.#ctor`

Конструктор по умолчанию

Remarks: Создаётся один направленный источник света с параметрами по умолчанию

### `AddDirectionalLight(TFlex.Model.Model3D.View3D.DirectionalLight)`

ID: `M:TFlex.Model.Model3D.View3D.LightParameters.AddDirectionalLight(TFlex.Model.Model3D.View3D.DirectionalLight)`

Добавляет новый источник света

Parameters:
- `value`: Новый источник света

### `Clone`

ID: `M:TFlex.Model.Model3D.View3D.LightParameters.Clone`

Возвращает копию объекта

### `DeleteDirectionalLight(System.Int32)`

ID: `M:TFlex.Model.Model3D.View3D.LightParameters.DeleteDirectionalLight(System.Int32)`

Удаляет источник света с заданным индексом

Parameters:
- `index`: Индекс источника света

## Propertys

### `DirectionalLight(System.Int32)`

ID: `P:TFlex.Model.Model3D.View3D.LightParameters.DirectionalLight(System.Int32)`

Направленный источник света с заданным индексом

### `EnvironmentLight`

ID: `P:TFlex.Model.Model3D.View3D.LightParameters.EnvironmentLight`

Параметры рассеянного освещения

### `NumDirectionalLights`

ID: `P:TFlex.Model.Model3D.View3D.LightParameters.NumDirectionalLights`

Количество направленных источников света
