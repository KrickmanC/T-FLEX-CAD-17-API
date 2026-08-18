# TFlex.Dialogs.ListItemRole

Assembly: `TFlexCommandAPI`
Namespace: `TFlex.Dialogs`

## Summary

Роль данных элемента ListControl

## Fields

### `AlignmentRole`

ID: `F:TFlex.Dialogs.ListItemRole.AlignmentRole`

Выравнивание. Ожидается ListItemAlignment

### `BgColorRole`

ID: `F:TFlex.Dialogs.ListItemRole.BgColorRole`

Цвет фона

### `CheckIsEnabledRole`

ID: `F:TFlex.Dialogs.ListItemRole.CheckIsEnabledRole`

Доступность чекбокса для редактирования. Ожидается bool.

### `CheckIsThreeState`

ID: `F:TFlex.Dialogs.ListItemRole.CheckIsThreeState`

Чекбокс работает в режиме ThreeState. Ожидается bool.

### `CheckStateRole`

ID: `F:TFlex.Dialogs.ListItemRole.CheckStateRole`

Состояние чекбокса. Ожидается CheckState

### `ColorRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColorRole`

Цвет текста. Ожидается System.Drawing.Color

### `ColumnIsGroupRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColumnIsGroupRole`

Колонка является группирующей. Ожидается bool. Если задан флаг, колонка будет группирующей по тексту.

### `ColumnIsInitiallyVisibleRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColumnIsInitiallyVisibleRole`

Видимость колонки при первом показе. Ожидается bool.

### `ColumnIsSortableRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColumnIsSortableRole`

Колонка поддерживает сортировку. Ожидается bool. Если задан флаг, у колонки будет доступна сортировка.

### `ColumnIsTreeRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColumnIsTreeRole`

Колонка используется для отображения дерева. Ожидается bool.

### `ColumnNameRole`

ID: `F:TFlex.Dialogs.ListItemRole.ColumnNameRole`

Имя колонки. Если задано, используется при настройке колонок вместо DefaultRole.

### `DefaultRole`

ID: `F:TFlex.Dialogs.ListItemRole.DefaultRole`

Роль по умолчанию. Ожидается строка, double или int

### `EditableRole`

ID: `F:TFlex.Dialogs.ListItemRole.EditableRole`

Поддерживает редактирование. Ожидается bool.

### `IconRole`

ID: `F:TFlex.Dialogs.ListItemRole.IconRole`

Иконка. Ожидается Icon

### `IdRole`

ID: `F:TFlex.Dialogs.ListItemRole.IdRole`

Роль идентификатор. Ожидается System.Int64 или int

### `ParentIdRole`

ID: `F:TFlex.Dialogs.ListItemRole.ParentIdRole`

Роль идентификатор родительского элемента. Ожидается System.Int64 или int

### `ParentIndexRole`

ID: `F:TFlex.Dialogs.ListItemRole.ParentIndexRole`

Роль индекс родительского элемента. Ожидается int

### `PrecisionRole`

ID: `F:TFlex.Dialogs.ListItemRole.PrecisionRole`

Точность. Ожидается double

### `ToolTipRole`

ID: `F:TFlex.Dialogs.ListItemRole.ToolTipRole`

Всплывающая подсказка. Ожидается строка

### `WidthCoefficientRole`

ID: `F:TFlex.Dialogs.ListItemRole.WidthCoefficientRole`

Коэффициент ширины колонки.

Remarks: Отрицательный коэффициент означет, что колонка имеет фиксированную ширину, равную модулю этого значения.
