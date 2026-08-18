# TFlex.Control

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Класс визуального элемент управления, позволяющего отображать документы T-FLEX CAD в окне приложения

## Constructors

### `Control`

ID: `M:TFlex.Control.#ctor`

Конструктор

## Methods

### `Control`

ID: `M:TFlex.Control.#ctor`

Конструктор

### `Dispose`

ID: `M:TFlex.Control.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `GetModelPoint(System.Drawing.Point)`

ID: `M:TFlex.Control.GetModelPoint(System.Drawing.Point)`

Получить точку в системе координат модели

### `IsPageTypeVisible(TFlex.Model.PageType)`

ID: `M:TFlex.Control.IsPageTypeVisible(TFlex.Model.PageType)`

Возвращает видимость страницы с заданным типом

### `LoadImageFile(System.String)`

ID: `M:TFlex.Control.LoadImageFile(System.String)`

Загрузить изображение

Parameters:
- `fileName`: Имя файла

### `OnMouseDoubleClick(System.Windows.Forms.MouseEventArgs)`

ID: `M:TFlex.Control.OnMouseDoubleClick(System.Windows.Forms.MouseEventArgs)`

Событие, происходящее, когда визуальный элемент управления дважды щелкается мышью

Parameters:
- `e`: Аргументы события

### `OnMouseDown(System.Windows.Forms.MouseEventArgs)`

ID: `M:TFlex.Control.OnMouseDown(System.Windows.Forms.MouseEventArgs)`

Cобытие, происходящеe при нажатии кнопки мыши, если указатель мыши находится на визуальном элементе управления

Parameters:
- `e`: Аргументы события

### `OnMouseMove(System.Windows.Forms.MouseEventArgs)`

ID: `M:TFlex.Control.OnMouseMove(System.Windows.Forms.MouseEventArgs)`

Событие, происходящее при перемещении указателя мыши по визуальному элементу управления

Parameters:
- `e`: Аргументы события

### `OnMouseUp(System.Windows.Forms.MouseEventArgs)`

ID: `M:TFlex.Control.OnMouseUp(System.Windows.Forms.MouseEventArgs)`

Cобытие, происходящее при отпускании кнопки мыши, когда указатель мыши находится на визуальном элементе управления

Parameters:
- `e`: Аргументы события

### `OnMouseWheel(System.Windows.Forms.MouseEventArgs)`

ID: `M:TFlex.Control.OnMouseWheel(System.Windows.Forms.MouseEventArgs)`

Событие, происходящее при прокрутке колеса мыши в поле визуального элемента управления

Parameters:
- `e`: Аргументы события

### `OnPaint(System.Windows.Forms.PaintEventArgs)`

ID: `M:TFlex.Control.OnPaint(System.Windows.Forms.PaintEventArgs)`

Событие, происходящее при перерисовке визуального элемента управления

Parameters:
- `e`: Аргументы события

### `OnResize(System.EventArgs)`

ID: `M:TFlex.Control.OnResize(System.EventArgs)`

Событие, происходящее при изменении размеров визуального элемента управления

Parameters:
- `e`: Аргументы события

### `Print`

ID: `M:TFlex.Control.Print`

Печатать содержимое окна элемента управления

### `Redraw`

ID: `M:TFlex.Control.Redraw`

Перерисовать окно

### `RefreshTabs`

ID: `M:TFlex.Control.RefreshTabs`

Обновить закладки текущего документа

### `Select(System.Drawing.Point,TFlex.Model.SelectionFilter)`

ID: `M:TFlex.Control.Select(System.Drawing.Point,TFlex.Model.SelectionFilter)`

Выбор элемента модели, ближайшего к заданной точке

Parameters:
- `point`: Точка на экране
- `filter`: Фильтр выбора объектов

### `Select(System.Int32,System.Int32,TFlex.Model.SelectionFilter)`

ID: `M:TFlex.Control.Select(System.Int32,System.Int32,TFlex.Model.SelectionFilter)`

Выбор элемента модели, ближайшего к точке с заданными координатами

Parameters:
- `x`: Координата X в экранной системе координат
- `y`: Координата Y в экранной системе координат
- `filter`: Фильтр выбора объектов

### `SetPageTypeVisibility(TFlex.Model.PageType,System.Boolean)`

ID: `M:TFlex.Control.SetPageTypeVisibility(TFlex.Model.PageType,System.Boolean)`

Управление видимостью страницы

### `SetViewPoint(TFlex.Control.ViewPoint)`

ID: `M:TFlex.Control.SetViewPoint(TFlex.Control.ViewPoint)`

Установка точки взгляда

Parameters:
- `point`: Точка взгляда

### `SetZoomRectangle(TFlex.Drawing.Rectangle)`

ID: `M:TFlex.Control.SetZoomRectangle(TFlex.Drawing.Rectangle)`

Установить текущее окно вывода (только 2D)

Parameters:
- `rect`: Прямоугольник окна вывода

### `ZoomLimits`

ID: `M:TFlex.Control.ZoomLimits`

Показать всё изображение

## Propertys

### `AutoSelectViewType`

ID: `P:TFlex.Control.AutoSelectViewType`

Выбирать тип вида (2D/3D) по умолчанию

### `AutoZoom`

ID: `P:TFlex.Control.AutoZoom`

Режим автоматического масштабирования

### `Border`

ID: `P:TFlex.Control.Border`

Рамка

### `DefaultWindowsBackground`

ID: `P:TFlex.Control.DefaultWindowsBackground`

Использовать цвет фона Windows по умолчанию

### `Document`

ID: `P:TFlex.Control.Document`

Текущий документ

### `DrawAnnotations`

ID: `P:TFlex.Control.DrawAnnotations`

Выводить аннотации

### `DrawPaperBorder`

ID: `P:TFlex.Control.DrawPaperBorder`

Рисовать рамку страницы

### `EnableFragmentEditing`

ID: `P:TFlex.Control.EnableFragmentEditing`

Разрешить редактирование фрагментов

### `EnablePrintButton`

ID: `P:TFlex.Control.EnablePrintButton`

Параметр "Разрешить печатать"

### `ExplodeMode`

ID: `P:TFlex.Control.ExplodeMode`

Параметр "Режим разборки (3D)"

### `GlobalLcsVisible`

ID: `P:TFlex.Control.GlobalLcsVisible`

Показать или скрыть глобальную систему координат

### `Graphics`

ID: `P:TFlex.Control.Graphics`

Получение текущего графического контекста (только 2D)

### `Hide3DAnnotations`

ID: `P:TFlex.Control.Hide3DAnnotations`

Параметр "Скрыть элементы оформления"

### `HideConstructions`

ID: `P:TFlex.Control.HideConstructions`

Параметр "Скрыть линии построения"

### `Image`

ID: `P:TFlex.Control.Image`

Параметр "изображение"

### `Page`

ID: `P:TFlex.Control.Page`

Текущая страница

### `ProductName`

ID: `P:TFlex.Control.ProductName`

Название визуального элемента управления

### `ProductVersion`

ID: `P:TFlex.Control.ProductVersion`

Версия визульного элемента управления

### `ShowAllPages`

ID: `P:TFlex.Control.ShowAllPages`

Параметр "Показывать все страницы"

### `ShowControlButtons`

ID: `P:TFlex.Control.ShowControlButtons`

Параметр "Показывать кнопки управления видом"

### `ShowPageTabs`

ID: `P:TFlex.Control.ShowPageTabs`

Параметр "Показывать закладки страниц"

### `ShowVariablesButton`

ID: `P:TFlex.Control.ShowVariablesButton`

Показать кнопку "Переменные"

### `ShowView3D`

ID: `P:TFlex.Control.ShowView3D`

Параметр "Показывать 3D вид"

### `TabAlignment`

ID: `P:TFlex.Control.TabAlignment`

Параметр "Показывать закладки страниц снизу"

### `ViewStyle`

ID: `P:TFlex.Control.ViewStyle`

Параметр "Стиль отображения (3D)"

### `ViewType`

ID: `P:TFlex.Control.ViewType`

Получить тип текущего вида: false - 2D, true - 3D

### `ZoomRectangle`

ID: `P:TFlex.Control.ZoomRectangle`

Прямоугольник, который отображается в данном виде (только для 2D)

## Events

### `ContextMenu`

ID: `E:TFlex.Control.ContextMenu`

Событие, происходящее при вызове контекстного меню

### `FinishPaint`

ID: `E:TFlex.Control.FinishPaint`

Cобытие, происходящеe при завершении отрисовки визуального элемента управления.

### `MouseDblClick`

ID: `E:TFlex.Control.MouseDblClick`

Событие, происходящее, когда визуальный элемент управления дважды щелкается мышью.

### `MouseDown`

ID: `E:TFlex.Control.MouseDown`

Cобытие, происходящеe при нажатии кнопки мыши, если указатель мыши находится на визуальном элементе управления.

### `MouseMoved`

ID: `E:TFlex.Control.MouseMoved`

Событие, происходящее при перемещении указателя мыши по визуальному элементу управления.

### `MouseUp`

ID: `E:TFlex.Control.MouseUp`

Cобытие, происходящее при отпускании кнопки мыши, когда указатель мыши находится на визуальном элементе управления.

### `ObjectChanged`

ID: `E:TFlex.Control.ObjectChanged`

Событие, происходящее при изменении объекта

### `PageChanged`

ID: `E:TFlex.Control.PageChanged`

Событие, происходящее при изменении активной страницы

### `RMouseDown`

ID: `E:TFlex.Control.RMouseDown`

Событие, происходящеe при нажатии правой кнопки мыши, если указатель мыши находится на визуальном элементе управления.

### `RMouseUp`

ID: `E:TFlex.Control.RMouseUp`

Событие, происходящее при отпускании правой кнопки мыши, когда указатель мыши находится на визуальном элементе управления.
