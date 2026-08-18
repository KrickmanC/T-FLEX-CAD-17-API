# TFlex.Model.Model3D.BodyTaper.MethodType

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.BodyTaper`

## Summary

Метод построения уклона

## Fields

### `Curve`

ID: `F:TFlex.Model.Model3D.BodyTaper.MethodType.Curve`

По кривой

### `Default`

ID: `F:TFlex.Model.Model3D.BodyTaper.MethodType.Default`

Только для рёбер. Используется метод операции

### `Isocline`

ID: `F:TFlex.Model.Model3D.BodyTaper.MethodType.Isocline`

Стандартный

Remarks: Produces ruled isocline surfaces satisfying the taper condition. If the angle between the taper direction and the curve tangent happens to be smaller than the taper angle anywhere along the curve, this method will fail to construct the taper surface. This method produces taper surfaces for mould design

### `Surface`

ID: `F:TFlex.Model.Model3D.BodyTaper.MethodType.Surface`

По поверхности
