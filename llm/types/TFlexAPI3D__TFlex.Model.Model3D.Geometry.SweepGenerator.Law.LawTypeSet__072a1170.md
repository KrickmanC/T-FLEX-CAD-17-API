# TFlex.Model.Model3D.Geometry.SweepGenerator.Law.LawTypeSet

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.SweepGenerator.Law`

## Summary

Тип задания закона

## Fields

### `Curve`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.LawTypeSet.Curve`

Закон задаётся непрерывной скалярной фукнцией пропорционально длине вдоль траектории. Закон задаётся одномерной сплайновой кривой, параметризованной от 0.0 до 1.0.

### `Discrete`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.LawTypeSet.Discrete`

Интерполяция таблично заданной функции. Значения функции задаются в вершинах траектории

### `Inv`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.LawTypeSet.Inv`

Закон задаётся непрерывной скалярной фукнцией пропорционально длине вдоль траектории. Закон задаётся одномерной сплайновой кривой, обратной к задающей функции. То есть кривая параметризована на интервале значений, принимаемых законом и область значений кривой лежит в иентрале от 0.0 до 1.0

### `None`

ID: `F:TFlex.Model.Model3D.Geometry.SweepGenerator.Law.LawTypeSet.None`

Закон не используется
