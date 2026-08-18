# TFlex.Model.Model3D.Geometry.UnitConverter

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Конвертер единиц измерения модели

## Remarks

В модели результирующая геометрия объектов хранится в метрах. Данный класс позволяет конвертировать геометрию в единицы модели и обратно

## Constructors

### `UnitConverter(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ, единицы которого учитываются

## Methods

### `UnitConverter(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.#ctor(TFlex.Model.Document)`

Конструктор

Parameters:
- `document`: Документ, единицы которого учитываются

### `FromMeter(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.FromMeter(System.Double)`

Конвертация из метров в единицы модели

Parameters:
- `scale`: Величина геометрического объекта в метрах

### `FromMeter(TFlex.Model.Model3D.Geometry.BaseAxis)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.FromMeter(TFlex.Model.Model3D.Geometry.BaseAxis)`

Конвертировать координаты оси из метров в единицы модели

Parameters:
- `axis`: Ось

### `FromMeter(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.FromMeter(TFlex.Model.Model3D.Geometry.BaseDirection)`

Конвертировать координаты вектора направления из метров в единицы модели

Parameters:
- `vector`: Вектор направления

### `FromMeter(TFlex.Model.Model3D.Geometry.BasePlane)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.FromMeter(TFlex.Model.Model3D.Geometry.BasePlane)`

Конвертировать координаты плоскости из метров в единицы модели

Parameters:
- `plane`: Плоскость

### `FromMeter(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.FromMeter(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конвертировать координаты точки из метров в единицы модели

Parameters:
- `point`: Точка

### `ToMeter(System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.ToMeter(System.Double)`

Конвертация из единиц модели в метры

Parameters:
- `scale`: Величина геометрического объекта в единицах модели

### `ToMeter(TFlex.Model.Model3D.Geometry.BaseAxis)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.ToMeter(TFlex.Model.Model3D.Geometry.BaseAxis)`

Конвертировать координаты оси из единиц модели в метры

Parameters:
- `axis`: Ось

### `ToMeter(TFlex.Model.Model3D.Geometry.BaseDirection)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.ToMeter(TFlex.Model.Model3D.Geometry.BaseDirection)`

Конвертировать координаты вектора направления из единиц модели в метры

Parameters:
- `vector`: Вектор направления

### `ToMeter(TFlex.Model.Model3D.Geometry.BasePlane)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.ToMeter(TFlex.Model.Model3D.Geometry.BasePlane)`

Конвертировать координаты плоскости из единиц модели в метры

Parameters:
- `plane`: Плоскость

### `ToMeter(TFlex.Model.Model3D.Geometry.BasePoint3D)`

ID: `M:TFlex.Model.Model3D.Geometry.UnitConverter.ToMeter(TFlex.Model.Model3D.Geometry.BasePoint3D)`

Конвертировать координаты точки из единиц модели в метры

Parameters:
- `point`: Точка

## Propertys

### `Scale`

ID: `P:TFlex.Model.Model3D.Geometry.UnitConverter.Scale`

Коэффициент преобразования из единиц модели в метры
