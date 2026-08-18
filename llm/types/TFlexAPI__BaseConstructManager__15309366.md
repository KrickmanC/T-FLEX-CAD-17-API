# BaseConstructManager

Assembly: `TFlexAPI`

## Methods

### `OnTooltipListSelection(CTFView*,SelectableObject*,System.Int64)`

ID: `M:BaseConstructManager.OnTooltipListSelection(CTFView*,SelectableObject*,System.Int64)`

Обработка выбора объекта из выпадающего списка (CTFTooltipCtrl)

Parameters:
- `view`: Указатель на активный вид
- `selectedObject`: Выбранный из списка объект
- `tf_param`: Входящие параметры

Returns: true - если обработал событие, false - иначе

Remarks: Если здесь событие не обрабатывается, то посылаются TFE_LBUTTONDOWN и TFE_LBUTTONUP
