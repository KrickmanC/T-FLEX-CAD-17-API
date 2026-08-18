# TFlex.Model.Model3D.Sweep

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Базовый класс для кинематических операций. Общим для всех порожденных из него классов является способ задания образующего контура

## Propertys

### `BottomFitting`

ID: `P:TFlex.Model.Model3D.Sweep.BottomFitting`

Способ обработки рёбер на нижней грани

### `BottomRadius`

ID: `P:TFlex.Model.Model3D.Sweep.BottomRadius`

Радиус сглаживания или смещения для фаски на нижнем ребре

Remarks: Если значение нулевое или отрицательное, то сглаживание не строится

### `GapFillType`

ID: `P:TFlex.Model.Model3D.Sweep.GapFillType`

Способ обработки разрывов

Remarks: При построении тонкостенного выталкивания для плоского контура строится эквидистантный контур. Для границ контуров, состоящих из нескольких рёбер или имеющих изломы в вершинах, возможно возникновение разрывов между эквидистантами, построенными для каждого ребра. В этом случае задаётся способ обработки такого разрыва. По умолчанию используется метод продолжения по кривой

### `Profile`

ID: `P:TFlex.Model.Model3D.Sweep.Profile`

Множество образующих контуров

### `Reverse`

ID: `P:TFlex.Model.Model3D.Sweep.Reverse`

Параметр реверсирования направления

### `SideBlending`

ID: `P:TFlex.Model.Model3D.Sweep.SideBlending`

Сглаживание боковых рёбер

Remarks: Если значение нулевое или отрицательное, то сглаживание не строится

### `SideFitting`

ID: `P:TFlex.Model.Model3D.Sweep.SideFitting`

Способ обработки боковых рёбер

Remarks: Снятие фаски для боковых рёбер не поддерживается

### `Thickness1`

ID: `P:TFlex.Model.Model3D.Sweep.Thickness1`

Первое значение толщины стенок

Remarks: Первое значение используется для задания толщины стенки в случае односторонних или симметричных стенок

### `Thickness2`

ID: `P:TFlex.Model.Model3D.Sweep.Thickness2`

Второе значение толщины стенок

Remarks: Второе значение используется для задания толщины внутренней стенки в случае двусторонних стенок

### `ThicknessType`

ID: `P:TFlex.Model.Model3D.Sweep.ThicknessType`

Тип тонкостенного элемента

Remarks: Допустимые типы тонкостенного элемента зависит от типа контура

### `TopFitting`

ID: `P:TFlex.Model.Model3D.Sweep.TopFitting`

Способ обработки рёбер на верхней грани

### `TopRadius`

ID: `P:TFlex.Model.Model3D.Sweep.TopRadius`

Радиус сглаживания или смещения для фаски на верхнем ребре

Remarks: Если значение нулевое или отрицательное, то сглаживание не строится
