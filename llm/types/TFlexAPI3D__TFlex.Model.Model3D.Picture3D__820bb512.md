# TFlex.Model.Model3D.Picture3D

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция "3D изображение"

## Constructors

### `Picture3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Picture3D.#ctor(TFlex.Model.Document)`

Конструктор для операции 3D изображения

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Picture3D(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model3D.Picture3D.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла картинки

Parameters:
- `link`: Ссылка на файл картинки

## Methods

### `Picture3D(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Picture3D.#ctor(TFlex.Model.Document)`

Конструктор для операции 3D изображения

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `Picture3D(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model3D.Picture3D.#ctor(TFlex.Model.FileLink)`

Конструктор с именем файла картинки

Parameters:
- `link`: Ссылка на файл картинки

### `FixByPictureLCS(System.String,TFlex.Model.Model3D.LCS)`

ID: `M:TFlex.Model.Model3D.Picture3D.FixByPictureLCS(System.String,TFlex.Model.Model3D.LCS)`

Привязать 3D изображение по системе координат созданной в документе фрагмента в систему координат сборки

Parameters:
- `sourceLCSName`: Имя системы координат, созданной в документе фрагмента
- `targetLCS`: Система координат, созданная в документе сборки

### `FixByWorkplane(TFlex.Model.Model3D.Workplane)`

ID: `M:TFlex.Model.Model3D.Picture3D.FixByWorkplane(TFlex.Model.Model3D.Workplane)`

Привязать 3D изображение по расположению соответствующего 2D фрагмента на Рабочей плоскости

Parameters:
- `workplane`: Рабочая плоскость

## Propertys

### `FileLink`

ID: `P:TFlex.Model.Model3D.Picture3D.FileLink`

Ссылка на файл картинки

### `FileName`

ID: `P:TFlex.Model.Model3D.Picture3D.FileName`

Имя файла 3D изображения

### `Fixing`

ID: `P:TFlex.Model.Model3D.Picture3D.Fixing`

Получить способ привязки 3D изображения

### `GroupType`

ID: `P:TFlex.Model.Model3D.Picture3D.GroupType`

Получить тип объекта

### `PathName`

ID: `P:TFlex.Model.Model3D.Picture3D.PathName`

Получить путь к файлу 3D изображения

### `SourceLCSName`

ID: `P:TFlex.Model.Model3D.Picture3D.SourceLCSName`

Получить имя системы координат созданной в документе фрагмента, используемой для привязки 3D изображения

### `TargetLCS`

ID: `P:TFlex.Model.Model3D.Picture3D.TargetLCS`

Получить целевую систему координат созданную в документе сборки, используемую для привязки 3D изображения

### `Workplane`

ID: `P:TFlex.Model.Model3D.Picture3D.Workplane`

Получить рабочую плоскость, используемую для привязки 3D изображения
