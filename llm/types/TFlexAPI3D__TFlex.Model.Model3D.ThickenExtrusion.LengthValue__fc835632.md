# TFlex.Model.Model3D.ThickenExtrusion.LengthValue

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.ThickenExtrusion`

## Summary

Способ определения длины выталкивания в прямом и обратном направлениях

## Fields

### `AutoNo`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.AutoNo`

Длина в прямом направлении берётся с вектора выталкивания. Если вектор выталкивания не задан или он не определяет длину выталкивания, то длина задаётся числовым значением или значением переменной. В противном случае значение длины игнорируется. В обратном направлении контур не выталкивается.

### `AutoSymmetric`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.AutoSymmetric`

Длина в прямом направлении берётся с вектора выталкивания. Если вектор выталкивания не задан или он не определяет длину выталкивания, то длина задаётся числовым значением или значением переменной. В противном случае значение длины игнорируется. В обратном направлении контур выталкивается на такое же значение, что и в прямом направлении.

### `AutoValue`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.AutoValue`

Длина в прямом направлении берётся с вектора выталкивания. Если вектор выталкивания не задан или он не определяет длину выталкивания, то длина задаётся числовым значением или значением переменной. В противном случае значение длины игнорируется. В обратном направлении длина задаётся числовым значением или значением переменной.

### `Unlimited`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.Unlimited`

Контур выталкивается в обоих направлениях на бесконечную длину

### `UnlimitedByDirection`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.UnlimitedByDirection`

Контур выталкивается в заданном направлении на бесконечную длину.

### `ValueNo`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.ValueNo`

В прямом направлении длина задаётся числовым значением или значением переменной. В обратном направлении контур не выталкивается.

### `ValueSymmetric`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.ValueSymmetric`

В прямом направлении длина задаётся числовым значением или значением переменной. В обратном направлении контур выталкивается на такое же значение, что и в прямом направлении.

### `ValueValue`

ID: `F:TFlex.Model.Model3D.ThickenExtrusion.LengthValue.ValueValue`

Длина в обоих направлениях задаётся числовыми значениями или значениями переменных
