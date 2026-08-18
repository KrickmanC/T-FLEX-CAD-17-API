# TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор трёхгранного сглаживания

## Constructors

### `ThreeFaceBlendGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,System.Boolean)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание
- `leftSense`: Параметр ориентации левой стенки
- `centerSense`: Параметр ориентации центральной стенки
- `rightSense`: Параметр ориентации правой стенки
- `propagateBlend`: Продолжать ли сглаживание на гладкую последовательность граней

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `ThreeFaceBlendGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,TFlex.Model.Model3D.Geometry.SenseOfFace,System.Boolean)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание
- `leftSense`: Параметр ориентации левой стенки
- `centerSense`: Параметр ориентации центральной стенки
- `rightSense`: Параметр ориентации правой стенки
- `propagateBlend`: Продолжать ли сглаживание на гладкую последовательность граней

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

### `AddFaceToCenterWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.AddFaceToCenterWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция добавляет грань в список для центральной стенки

Parameters:
- `face`: Добавляемая грань

### `AddFaceToLeftWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.AddFaceToLeftWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция добавляет грань в список для левой стенки

Parameters:
- `face`: Добавляемая грань

### `AddFaceToRightWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.AddFaceToRightWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция добавляет грань в список для правой стенки

Parameters:
- `face`: Добавляемая грань

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.Run`

Функция генерации сглаживания

## Propertys

### `Spine`

ID: `P:TFlex.Model.Model3D.Geometry.ThreeFaceBlendGenerator.Spine`

Направляющая кривая
