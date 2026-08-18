# TFlex.Model.Model3D.OnAxisWorkplane

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Рабочая плоскость по оси или плоскому ребру

## Constructors

### `OnAxisWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OnAxisWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `OnAxisWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.OnAxisWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Methods

### `OnAxisWorkplane(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.OnAxisWorkplane.#ctor(TFlex.Model.Document)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект

Remarks: Рабочая плоскость создаётся на активной странице

### `OnAxisWorkplane(TFlex.Model.Document,TFlex.Model.Page)`

ID: `M:TFlex.Model.Model3D.OnAxisWorkplane.#ctor(TFlex.Model.Document,TFlex.Model.Page)`

Конструктор для создания рабочей плоскости

Parameters:
- `document`: Документ, в котором создаётся новый объект
- `page`: Страница, на которой создаётся рабочая плоскость

## Propertys

### `Angle`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.Angle`

Угол поворота

Remarks: Доворот рабочей плоскости задаётся тремя взаимоисключающими способами : - точкой, через которую проходит рабочая плоскость; - параметром угла поворота; - поверхностью, которой касается рабочая плоскость.

### `AxisOnWorkplane`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.AxisOnWorkplane`

Ось, которая лежит на рабочей плоскости

Remarks: Положение рабочей плоскости задаётся двумя взаимоисключающими способами : плоским ребром или осью

### `BasePlane`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.BasePlane`

Плоскость, относительно которой задаётся доворот рабочей плоскости

Remarks: В случае выбора плоскости доворот задаётся параметром угла поворота

### `EdgeOnWorkplane`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.EdgeOnWorkplane`

Плоское ребро, которое лежит на рабочей плоскости

Remarks: Положение рабочей плоскости задаётся двумя взаимоисключающими способами : плоским ребром или осью. Если ребро прямое, то также как и в случае выбора оси можно дополнительно задавать доворот рабочей плоскости относительно оси или ребра

### `FaceTangentToWorkplane`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.FaceTangentToWorkplane`

Поверхность, которой касается рабочая плоскость

Remarks: Доворот рабочей плоскости задаётся тремя взаимоисключающими способами : - точкой, через которую проходит рабочая плоскость; - параметром угла поворота; - поверхностью, которой касается рабочая плоскость.

### `PointOnWorkplane`

ID: `P:TFlex.Model.Model3D.OnAxisWorkplane.PointOnWorkplane`

Точка, задающая доворот рабочей плоскости

Remarks: Доворот рабочей плоскости задаётся тремя взаимоисключающими способами : - точкой, через которую проходит рабочая плоскость; - параметром угла поворота; - поверхностью, которой касается рабочая плоскость.
