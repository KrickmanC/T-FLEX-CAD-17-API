# TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry`

## Summary

Генератор сглаживания граней

## Constructors

### `FaceFaceBlendGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.TFBlendMode,TFlex.Model.Model3D.Geometry.TFCutMode,TFlex.Model.Model3D.Geometry.TFPlaneOrientation)`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.TFBlendMode,TFlex.Model.Model3D.Geometry.TFCutMode,TFlex.Model.Model3D.Geometry.TFPlaneOrientation)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание
- `leftSense`: Параметр ориентации левой стенки
- `rightSense`: Параметр ориентации правой стенки
- `bm`: Режим сглаживания
- `cm`: Режим обрезки результата
- `po`: Режим ориентации плоскости сечения сглажиавния

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

## Methods

### `FaceFaceBlendGenerator(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.TFBlendMode,TFlex.Model.Model3D.Geometry.TFCutMode,TFlex.Model.Model3D.Geometry.TFPlaneOrientation)`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.#ctor(TFlex.Model.Model3D.ProxyObject3D,TFlex.Model.Model3D.Geometry.Body,System.Boolean,System.Boolean,TFlex.Model.Model3D.Geometry.TFBlendMode,TFlex.Model.Model3D.Geometry.TFCutMode,TFlex.Model.Model3D.Geometry.TFPlaneOrientation)`

Конструктор для задания базовых объектов сглаживания

Parameters:
- `object`: 3D объект внешнего приложения, для которого генерируется результат
- `body`: Тело на котором строится сглаживание
- `leftSense`: Параметр ориентации левой стенки
- `rightSense`: Параметр ориентации правой стенки
- `bm`: Режим сглаживания
- `cm`: Режим обрезки результата
- `po`: Режим ориентации плоскости сечения сглажиавния

Remarks: 3D объект внешнего приложения должен быть связан с внешним объектом

### `AddEdgeToBorder(TFlex.Model.Model3D.Geometry.BaseTopol,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.AddEdgeToBorder(TFlex.Model.Model3D.Geometry.BaseTopol,System.Boolean,System.Boolean,System.Boolean,System.Boolean)`

Функция добавляет ограничительное ребро в список таких рёбер

Parameters:
- `edge`: Добавляемое ребро
- `invert`: Признак использования ребра для задания обратного касания
- `useCliff`: Признак использования ребра для задания обрезки
- `invConic`: Признак использования ребра для задания обратного конического касания
- `сonic`: Признак использования ребра для задания прямого конического касания

### `AddFaceToLeftWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.AddFaceToLeftWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция добавляет грань в левую стенку

Parameters:
- `face`: Добавляемая грань

### `AddFaceToRightWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.AddFaceToRightWall(TFlex.Model.Model3D.Geometry.BaseTopol)`

Функция добавляет грань в правую стенку

Parameters:
- `face`: Добавляемая грань

### `FlushFacesAndEdges`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.FlushFacesAndEdges`

Функция сбрасывает заданные данные

### `Run`

ID: `M:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.Run`

Функция генерации сглаживания

## Propertys

### `RF`

ID: `P:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.RF`

Радиус сглаживания для сглаживания с постоянным радиусом

### `Ratio`

ID: `P:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.Ratio`

Отношение сторон для сглаживания постоянной ширины

### `Softness`

ID: `P:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.Softness`

Коэффициент "мягкости" для сглаживания с непрерывностью по кривизне

### `Spine`

ID: `P:TFlex.Model.Model3D.Geometry.FaceFaceBlendGenerator.Spine`

Направляющая кривая
