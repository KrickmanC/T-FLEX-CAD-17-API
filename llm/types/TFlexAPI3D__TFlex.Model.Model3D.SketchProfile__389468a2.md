# TFlex.Model.Model3D.SketchProfile

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Профиль, построенный по эскизу

## Constructors

### `SketchProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SketchProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания профиля по эскизу

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Methods

### `SketchProfile(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.SketchProfile.#ctor(TFlex.Model.Document)`

Конструктор для создания профиля по эскизу

Parameters:
- `Doc`: Документ, в котором создаётся новый объект

## Propertys

### `Color`

ID: `P:TFlex.Model.Model3D.SketchProfile.Color`

Цвет линий изображения, по которым строится эскиз

### `OnHatch`

ID: `P:TFlex.Model.Model3D.SketchProfile.OnHatch`

2D узел, задающий перемещение узла контура в 3D узел

### `Outlines`

ID: `P:TFlex.Model.Model3D.SketchProfile.Outlines`

Линии изображения, по которым строится эскиз

### `Target`

ID: `P:TFlex.Model.Model3D.SketchProfile.Target`

3D узел для привязки плоскости контура

### `WorkSurface`

ID: `P:TFlex.Model.Model3D.SketchProfile.WorkSurface`

Рабочая поверхность, с которой берётся эскиз

Remarks: В настоящей версии в качестве рабочей поверхности можно выбирать только рабочую плоскость. В остальных случаях профиль строится не будет
