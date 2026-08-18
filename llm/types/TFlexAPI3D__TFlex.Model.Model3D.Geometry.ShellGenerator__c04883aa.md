# TFlex.Model.Model3D.Geometry.ShellGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор сглаживания рёбер

## Constructors

### `ShellGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ShellGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Double)`

Конструктор для задания базовых объектов построения оболочки

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится оболочка
- `isEquid`: Параметр режима построения оболочка или эквидистантное тело
- `defDist`: Толщина стенки по умолчанию в метрах

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `ShellGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ShellGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Double)`

Конструктор для задания базовых объектов построения оболочки

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится оболочка
- `isEquid`: Параметр режима построения оболочка или эквидистантное тело
- `defDist`: Толщина стенки по умолчанию в метрах

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

### `AddFace(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.ShellGenerator.AddFace(TFlex.Model.Model3D.Geometry.BaseTopol,System.Double)`

Функция задаёт параметры отступа индивидуально для грани

Parameters:
- `face`: Грань, для которой устанавливается отступ
- `dist`: величина отступа в метрах

### `AddPiercedFace(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.ShellGenerator.AddPiercedFace(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция задаёт пробиваемые грани

Parameters:
- `face`: Грань, которая должна быть удалена в оболочке

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.ShellGenerator.Run`

Функция генерации оболочки
