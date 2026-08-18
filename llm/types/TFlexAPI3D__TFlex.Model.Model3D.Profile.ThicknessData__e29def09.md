# TFlex.Model.Model3D.Profile.ThicknessData

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Profile`

## Summary

Свойства толщины

## Propertys

### `CornerFillType`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.CornerFillType`

Способ обработки концов

Remarks: Имеет смысл только для плоских контуров

### `GapFillType`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.GapFillType`

Способы обработки разрывов

Remarks: При построении тонкостенного выталкивания для плоского контура строится эквидистантный контур. Для границ контуров, состоящих из нескольких рёбер или имеющих изломы в вершинах, возможно возникновение разрывов между эквидистантами, построенными для каждого ребра. В этом случае задаётся способ обработки такого разрыва. По умолчанию используется метод продолжения по кривой

### `SeparateLoopType`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.SeparateLoopType`

Способ обработки замкнутых контуров

Remarks: Имеет смысл только для плоских контуров

### `Thickness1`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.Thickness1`

Первое значение толщины стенок

Remarks: Первое значение используется для задания толщины стенки в случае односторонних или симметричных стенок

### `Thickness2`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.Thickness2`

Получить второе значение толщины стенок

Remarks: Второе значение используется для задания толщины внутренней стенки в случае двусторонних стенок

### `ThicknessType`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.ThicknessType`

Тип тонкостенного элемента

Remarks: Имеет смысл только для плоских контуров

### `ThinWalled`

ID: `P:TFlex.Model.Model3D.Profile.ThicknessData.ThinWalled`

Параметр придания толщины

Remarks: Имеет смысл только для плоских контуров
