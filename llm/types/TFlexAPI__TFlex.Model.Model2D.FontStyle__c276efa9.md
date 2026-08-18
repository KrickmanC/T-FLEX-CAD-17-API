# TFlex.Model.Model2D.FontStyle

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Класс стиля шрифта

## Propertys

### `Bold`

ID: `P:TFlex.Model.Model2D.FontStyle.Bold`

Параметр "полужирный шрифт"

### `ClearBackground`

ID: `P:TFlex.Model.Model2D.FontStyle.ClearBackground`

Параметр "очистка фона"

### `DefaultTracing`

ID: `P:TFlex.Model.Model2D.FontStyle.DefaultTracing`

Использовать начертание из статуса

### `Extension`

ID: `P:TFlex.Model.Model2D.FontStyle.Extension`

Коэффициент расширения шрифта

Remarks: Коэффициент расширения шрифта учитывается только при прорисовке шрифтов типа SHX. Стандартное значение равно 1

### `Fill`

ID: `P:TFlex.Model.Model2D.FontStyle.Fill`

Параметр "заливка шрифта"

### `FontName`

ID: `P:TFlex.Model.Model2D.FontStyle.FontName`

Имя шрифта

Remarks: Шрифты SHX имеют расширение ".shx"

### `FontNameVariable`

ID: `P:TFlex.Model.Model2D.FontStyle.FontNameVariable`

Переменная, задающая имя шрифта или 0 если имя шрифта является константой

### `Interval`

ID: `P:TFlex.Model.Model2D.FontStyle.Interval`

Междустрочный интервал

Remarks: Междустрочный интервал задаётся коэффициентом относительно высоты шрифта. При значении равном 1 междустрочнй интервал равен высоте шрифта

### `Italic`

ID: `P:TFlex.Model.Model2D.FontStyle.Italic`

Параметр "наклонный шрифт"

### `LineWidth`

ID: `P:TFlex.Model.Model2D.FontStyle.LineWidth`

Толщина линий шрифта

Remarks: Толщина линий учитывается только при прорисовке шрифтов формата SHX

Examples:
- `public static void SetLineWidth(ModelObject ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("Установка толщины линии");//Открытие блока изменений документа ob.LineWidth = 3; document.EndChanges();//Закрытие блока изменений документа }`

### `Size`

ID: `P:TFlex.Model.Model2D.FontStyle.Size`

Размер (высота) шрифта

### `Spacing`

ID: `P:TFlex.Model.Model2D.FontStyle.Spacing`

Дополнитальный интервал между символами

Remarks: Интервал между символами измеряется коэффициентом относительно размера шрифта. Стандартное значение равно 0. При значении 1 интервал между символами равен высоте шрифта.

### `Tilt`

ID: `P:TFlex.Model.Model2D.FontStyle.Tilt`

Угол наклона шрифта

Remarks: Угол измеряется в градусах. Вертикальный шрифт имеет угол наклона, равный значению 90
