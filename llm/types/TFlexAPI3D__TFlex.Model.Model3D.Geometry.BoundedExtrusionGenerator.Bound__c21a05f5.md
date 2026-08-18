# TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator`

## Summary

Класс задания границы

## Remarks

Граница может задаваться четырьмя взаимоисключающими способами : листовым или твёрдым телом, гранью, поверхностью, отступом

## Constructors

### `Bound(System.Boolean,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,System.Double)`

Конструктор для задания границы значением отступа

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `distance`: Расстояние до границы в заданном направлении. Расстояние должно задаваться неотрицательным значением

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы телом

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `body`: Граничное тело. Может быть листовым или твёрдым телом
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона ограничивающего тела, пересекающая профиль, считается первым разбиением. Для первого и последнего разбиений твёрдого тела допустимыми значениями являются только In и Out

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseFace,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseFace,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы гранью

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `face`: Граничная грань
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона ограничивающей грани, пересекающая профиль, считается первым разбиением. Для первого и последнего разбиений грани с твёрдого тела допустимыми значениями являются только In и Out

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы поверхностью

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `surface`: Граничная поверхность
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона поверхности, пересекающая профиль, считается первым разбиением

## Methods

### `Bound(System.Boolean,System.Double)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,System.Double)`

Конструктор для задания границы значением отступа

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `distance`: Расстояние до границы в заданном направлении. Расстояние должно задаваться неотрицательным значением

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseBody,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы телом

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `body`: Граничное тело. Может быть листовым или твёрдым телом
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона ограничивающего тела, пересекающая профиль, считается первым разбиением. Для первого и последнего разбиений твёрдого тела допустимыми значениями являются только In и Out

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseFace,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseFace,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы гранью

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `face`: Граничная грань
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона ограничивающей грани, пересекающая профиль, считается первым разбиением. Для первого и последнего разбиений грани с твёрдого тела допустимыми значениями являются только In и Out

### `Bound(System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

ID: `M:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.#ctor(System.Boolean,TFlex.Model.Model3D.Geometry.BaseSurface,System.Boolean,System.UInt32,TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.SideType)`

Конструктор для задания границы поверхностью

Parameters:
- `forward`: Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )
- `surface`: Граничная поверхность
- `nearest`: Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю
- `division`: Номер разбиения. Разбиения нумеруются от 1
- `side`: Какая сторона поверхности, пересекающая профиль, считается первым разбиением

## Propertys

### `BoundBody`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.BoundBody`

Граничное тело

Remarks: Граница может задаваться четырьмя взаимоисключающими способами : листовым или твёрдым телом, гранью, поверхностью, отступом. Граничное тело можно задавать если выбран тип границы Body или Sheet. Соответсвенно тело должно быть заданного типа.

### `BoundDistance`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.BoundDistance`

Значение отступа

Remarks: Граница может задаваться четырьмя взаимоисключающими способами : листовым или твёрдым телом, гранью, поверхностью, отступом. Значение отступа можно задавать если выбран тип границы Distance.

### `BoundFace`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.BoundFace`

Граничная грань

Remarks: Граница может задаваться четырьмя взаимоисключающими способами : листовым или твёрдым телом, гранью, поверхностью, отступом. Граничную грань можно задавать если выбран тип границы Face.

### `BoundSurface`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.BoundSurface`

Граничная поверхность

Remarks: Граница может задаваться четырьмя взаимоисключающими способами : листовым или твёрдым телом, гранью, поверхностью, отступом. Граничную поверхность можно задавать если выбран тип границы Surface.

### `BoundType`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.BoundType`

Тип границы

### `Division`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.Division`

Номер разбиения. Разбиения нумеруются от 1

### `Forward`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.Forward`

Граница задаётся в направлении вектора выталкивания ( true ) или в обратном направлении ( false )

### `Nearest`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.Nearest`

Если true, то разбиения нумеруются начиная с первого и увеличиваясь в направлении движения от профиля. Если false, то первое разбиение наиболее удалено от профиля и номер разбиения увеличивается в направлении движения к профилю.

### `Side`

ID: `P:TFlex.Model.Model3D.Geometry.BoundedExtrusionGenerator.Bound.Side`

Какая сторона ограничивающего тела, пересекающая профиль, считается первым разбиением
