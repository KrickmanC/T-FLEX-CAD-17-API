# TFlex.Model.Model2D.Object2D

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс 2D объекта модели

## Methods

### `Draw(TFlex.Drawing.Graphics)`

ID: `M:TFlex.Model.Model2D.Object2D.Draw(TFlex.Drawing.Graphics)`

Нарисовать объект

Parameters:
- `graphics`: Объект класса Graphics, через который производится рисование.

### `GetDistance(TFlex.Drawing.Point)`

ID: `M:TFlex.Model.Model2D.Object2D.GetDistance(TFlex.Drawing.Point)`

Получение растояния до объекта

Parameters:
- `point`: Точка в единицах измерения модели

Returns: Растояние до объекта

### `GetPoint(System.UInt32)`

ID: `M:TFlex.Model.Model2D.Object2D.GetPoint(System.UInt32)`

Получение координат характерной точки объекта

Parameters:
- `id`: Уникальный для данного объекта идентификатор точки

Returns: Координаты характерной точки объекта с указанным идентификатором

### `GetPointCount`

ID: `M:TFlex.Model.Model2D.Object2D.GetPointCount`

Получение количества характерных точек объекта, в которых может быть построен узел

Returns: Количество точек

### `GetPointID(System.Int32)`

ID: `M:TFlex.Model.Model2D.Object2D.GetPointID(System.Int32)`

Получение идентификатора характерной точеки объекта с номером index

Parameters:
- `index`: Номер точки

Returns: Уникальный для данного объекта идентификатор точки

### `Transform(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Object2D.Transform(System.Double,System.Double,System.Double,System.Double,System.Double,System.Double)`

Применение преобразования.

Parameters:
- `scale`: Масштаб
- `angle`: Угол
- `OriginX`: Координата x центра вращения
- `OriginY`: Координата y центра вращения
- `OffsetX`: Координата x сдвига
- `OffsetY`: Координата y сдвига

### `Translate(System.Double,System.Double)`

ID: `M:TFlex.Model.Model2D.Object2D.Translate(System.Double,System.Double)`

Сдвиг объекта на данный вектор

Parameters:
- `dx`: Координта x
- `dy`: Координта y

## Propertys

### `BoundRect`

ID: `P:TFlex.Model.Model2D.Object2D.BoundRect`

Получение координат прямоугольника, обрамляющего объект

### `Page`

ID: `P:TFlex.Model.Model2D.Object2D.Page`

Страница, на которой размещается объект

Examples:
- `public static void SetPage(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Page p = new Page(document);//создание страницы p.Name = "страница1" ob.Page = p;//cтраница, на которой размещается элемент document.EndChanges();//Закрытие блока изменений документа }`
