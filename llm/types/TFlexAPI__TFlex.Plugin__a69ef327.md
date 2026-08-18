# TFlex.Plugin

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Данный класс реализует функциональность приложения для T-FLEX CAD. Он обеспечивает свою регистрацию, регистрацию своих команд, создание панелей инструментов и формирование текстового меню.

## Constructors

### `Plugin(TFlex.PluginFactory)`

ID: `M:TFlex.Plugin.#ctor(TFlex.PluginFactory)`

Конструктор

Parameters:
- `Factory`: Объект класса регистрации приложения

## Methods

### `Plugin(TFlex.PluginFactory)`

ID: `M:TFlex.Plugin.#ctor(TFlex.PluginFactory)`

Конструктор

Parameters:
- `Factory`: Объект класса регистрации приложения

### `AfterUndoActionEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.AfterUndoActionEventHandler(TFlex.DocumentEventArgs)`

Обработчик события, возникающего после отката действия

Parameters:
- `args`: Аргументы события

### `AlterColorButtonPressedHandler(TFlex.AlterColorButtonPressedEventArgs)`

ID: `M:TFlex.Plugin.AlterColorButtonPressedHandler(TFlex.AlterColorButtonPressedEventArgs)`

Обработчик события, при нажатии кнопки альтернативного выбора цвета

Parameters:
- `args`: Аргументы события

### `BlockChangesActionEventHandler(TFlex.BlockChangesEventArgs)`

ID: `M:TFlex.Plugin.BlockChangesActionEventHandler(TFlex.BlockChangesEventArgs)`

Обработчик события, возникающего перед открытием блока изменений и после закрытия блока изменений

Parameters:
- `args`: Аргументы события

### `CircuitLinkBreakAddEventHandler(TFlex.CircuitLinkSplitMergeEventArgs)`

ID: `M:TFlex.Plugin.CircuitLinkBreakAddEventHandler(TFlex.CircuitLinkSplitMergeEventArgs)`

Обработчик добавления линии связи в разрыв

### `CircuitLinkSplitMergeEventHandler(TFlex.CircuitLinkSplitMergeEventArgs)`

ID: `M:TFlex.Plugin.CircuitLinkSplitMergeEventHandler(TFlex.CircuitLinkSplitMergeEventArgs)`

Обработчик объединения/разделения линий связи

### `ClosingDocumentEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.ClosingDocumentEventHandler(TFlex.DocumentEventArgs)`

Обработчик события, возникающего перед закрытием документа

Parameters:
- `args`: Аргументы события

### `CopyPropertiesCommandEventHandler(TFlex.CopyPropertiesCommandEventArgs)`

ID: `M:TFlex.Plugin.CopyPropertiesCommandEventHandler(TFlex.CopyPropertiesCommandEventArgs)`

Класс, содержащий данные о событии - вызвана команда

Parameters:
- `args`: Аргументы события

### `CreateFloatingWindow(System.UInt32,System.String)`

ID: `M:TFlex.Plugin.CreateFloatingWindow(System.UInt32,System.String)`

Создать плавающее окно приложения

Parameters:
- `id`: Идентификатор окна
- `title`: Заголовок окна

### `CreateFloatingWindow(System.UInt32,System.String,TFlex.FloatingWindowParameters)`

ID: `M:TFlex.Plugin.CreateFloatingWindow(System.UInt32,System.String,TFlex.FloatingWindowParameters)`

Создать плавающее окно приложения

Parameters:
- `id`: Идентификатор окна
- `title`: Заголовок окна
- `parameters`: Параметры окна

### `CreateFloatingWindowControl(System.UInt32)`

ID: `M:TFlex.Plugin.CreateFloatingWindowControl(System.UInt32)`

Создать клиентскую часть плавающего окна приложения

Parameters:
- `id`: Идентификатор плавающего окна

### `CreateHelpMenuItem(System.String,System.Int32,System.Int32)`

ID: `M:TFlex.Plugin.CreateHelpMenuItem(System.String,System.Int32,System.Int32)`

Создать пункт меню в меню справки

Parameters:
- `caption`: Название пункта
- `commandId`: Идентификатор команды
- `position`: Позиция пункта в меню

### `CreateMainBarPanel(System.String,System.Int32[],System.Guid,System.Boolean)`

ID: `M:TFlex.Plugin.CreateMainBarPanel(System.String,System.Int32[],System.Guid,System.Boolean)`

Создать панель инструментов

Parameters:
- `caption`: Название панели
- `cmdIDs`: Массив идентификаторов команд приложения
- `panelGuid`: GUID панели, которую необходимо присоединить к MainBar-у
- `showDefaultSet`: флаг, который отвечает за показ/скрытие набора иконок основных команд

### `CreateObject(TFlex.Model.Document,System.IntPtr,System.Int32)`

ID: `M:TFlex.Plugin.CreateObject(TFlex.Model.Document,System.IntPtr,System.Int32)`

Приложение переопределяет эту функцию для создания объекта модели указанного типа

Parameters:
- `OwnerHandle`: 
- `TypeID`: 

### `CreateSubMenu(TFlex.Menu,System.String,System.Int32)`

ID: `M:TFlex.Plugin.CreateSubMenu(TFlex.Menu,System.String,System.Int32)`

Создать подменю в меню приложения

Parameters:
- `menu`: Меню для добавления
- `caption`: Название панели
- `position`: Позиция подменю в системном меню

### `CreateToolbar(System.String,System.Int32[])`

ID: `M:TFlex.Plugin.CreateToolbar(System.String,System.Int32[])`

Создать панель инструментов

Parameters:
- `Caption`: Название панели
- `CmdIDs`: Массив идентификаторов команд приложения

### `CreateToolbar(System.String,System.Int32[],System.Boolean)`

ID: `M:TFlex.Plugin.CreateToolbar(System.String,System.Int32[],System.Boolean)`

Создать панель инструментов

Parameters:
- `Caption`: Название панели
- `CmdIDs`: Массив идентификаторов команд приложения
- `Visible`: Отображать при запуске

### `DeletingObjectEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.DeletingObjectEventHandler(TFlex.ObjectEventArgs)`

Обработчик события, возникающего перед удалением объекта модели

Parameters:
- `args`: Аргументы события

### `DeletingObjectParentsEventHandler(TFlex.DeletingObjectParentsEventArgs)`

ID: `M:TFlex.Plugin.DeletingObjectParentsEventHandler(TFlex.DeletingObjectParentsEventArgs)`

Обработчик события, возникающего перед удалением объекта модели для получания дополнтиельных зависимых объектов для удаления

Parameters:
- `args`: Аргументы события

### `DestroyingViewEventHandler(TFlex.ViewEventArgs)`

ID: `M:TFlex.Plugin.DestroyingViewEventHandler(TFlex.ViewEventArgs)`

Обработчик события, возникающего перед разрушенем окна документа

Parameters:
- `args`: Аргументы события

### `DocumentDrawnEventHandler(TFlex.DrawingDocumentEventArgs)`

ID: `M:TFlex.Plugin.DocumentDrawnEventHandler(TFlex.DrawingDocumentEventArgs)`

Обработчик события, возникающего после отрисовки документа

Parameters:
- `args`: Аргументы события

### `DocumentOpenEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.DocumentOpenEventHandler(TFlex.DocumentEventArgs)`

Обработчик события открытия документа

Parameters:
- `args`: Аргументы события

### `DocumentRegeneratedEventHandler(TFlex.RegenerateDocumentEventArgs)`

ID: `M:TFlex.Plugin.DocumentRegeneratedEventHandler(TFlex.RegenerateDocumentEventArgs)`

Обработчик события, возникающего после пересчета документа

Parameters:
- `args`: Аргументы события

### `DocumentSavedEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.DocumentSavedEventHandler(TFlex.DocumentEventArgs)`

Обработчик события, возникающего после сохранения документа

Parameters:
- `args`: Аргументы события

### `DrawingDocumentEventHandler(TFlex.DrawingDocumentEventArgs)`

ID: `M:TFlex.Plugin.DrawingDocumentEventHandler(TFlex.DrawingDocumentEventArgs)`

Обработчик события, возникающего перед отрисовкой документа

Parameters:
- `args`: Аргументы события

### `DynamicAnalysisSteppedEventHandler(TFlex.DynamicAnalysisEventArgs)`

ID: `M:TFlex.Plugin.DynamicAnalysisSteppedEventHandler(TFlex.DynamicAnalysisEventArgs)`

Обработчик события, возникающего при решении задач динамического анализа

Parameters:
- `args`: Аргументы события

### `ExportDialogShownEventHandler(TFlex.ImportExportDialogShownEventArgs)`

ID: `M:TFlex.Plugin.ExportDialogShownEventHandler(TFlex.ImportExportDialogShownEventArgs)`

Обработчик события, возникающего после показа диалога экспорта

Parameters:
- `args`: Аргументы события

### `FileDroppedEventHandler(TFlex.FileDroppedEventArgs)`

ID: `M:TFlex.Plugin.FileDroppedEventHandler(TFlex.FileDroppedEventArgs)`

Обработчик события, возникающего при перемещении и отпускании файла в одном из видов документа

Parameters:
- `args`: Аргументы события

### `HelpWindowOpeningEventHandler(TFlex.HelpWindowOpeningEventArgs)`

ID: `M:TFlex.Plugin.HelpWindowOpeningEventHandler(TFlex.HelpWindowOpeningEventArgs)`

Обработчик события, возникающего перед показом окна справки

Parameters:
- `args`: Аргументы события

### `ImportDialogShownEventHandler(TFlex.ImportExportDialogShownEventArgs)`

ID: `M:TFlex.Plugin.ImportDialogShownEventHandler(TFlex.ImportExportDialogShownEventArgs)`

Обработчик события, возникающего после показа диалога импорта

Parameters:
- `args`: Аргументы события

### `ImportFile(System.String)`

ID: `M:TFlex.Plugin.ImportFile(System.String)`

Приложение переопределяет данный метод для импорта указанного файла

Returns: Документ, в который был импортирован указанный файл, либо `null` , если формат файла не поддерживается данным приложением

Remarks: В отличие от `M:TFlex.Plugin.ShowingImportDialogEventHandler(TFlex.ShowingImportExportDialogEventArgs)` и `M:TFlex.Plugin.ImportDialogShownEventHandler(TFlex.ImportExportDialogShownEventArgs)` , этот метод вызывается при передаче имён файлов через параметры командной строки или перетаскивании файлов на главное окно T-FLEX CAD.

### `MeasureResultsUpdatingEventHandler(TFlex.MeasureResultsUpdatingEventArgs)`

ID: `M:TFlex.Plugin.MeasureResultsUpdatingEventHandler(TFlex.MeasureResultsUpdatingEventArgs)`

Обработчик обновления результатов измерения. Приложение может добавить свои результаты в нее.

Parameters:
- `args`: Аргументы события

### `MoveSelectedObjectsActionEventHandler(TFlex.MoveSelectedObjectsEventArgs)`

ID: `M:TFlex.Plugin.MoveSelectedObjectsActionEventHandler(TFlex.MoveSelectedObjectsEventArgs)`

Parameters:
- `args`: Аргументы события

### `NewDocumentCreatedEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.NewDocumentCreatedEventHandler(TFlex.DocumentEventArgs)`

Обработчик события создания нового документа

Parameters:
- `args`: Аргументы события

### `ObjectChangedEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.ObjectChangedEventHandler(TFlex.ObjectEventArgs)`

Обработчик события, возникающего после изменения объекта

Parameters:
- `args`: Аргументы события

### `ObjectCreatedEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.ObjectCreatedEventHandler(TFlex.ObjectEventArgs)`

Обработчик события, возникающего после создания объекта модели

Parameters:
- `args`: Аргументы события

### `ObjectDeletedEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.ObjectDeletedEventHandler(TFlex.ObjectEventArgs)`

Обработчик события, возникающего после удаления объекта модели

Parameters:
- `args`: Аргументы события

### `ObjectPropertiesDialogCompletedEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.ObjectPropertiesDialogCompletedEventHandler(TFlex.ObjectEventArgs)`

Обработчик завершения редактирования объекта в окне "Параметры".

Parameters:
- `args`: Аргументы события

### `ObjectPropertiesDialogCompletedEventHandler(TFlex.ObjectPropertiesDialogCompletedEventArgs)`

ID: `M:TFlex.Plugin.ObjectPropertiesDialogCompletedEventHandler(TFlex.ObjectPropertiesDialogCompletedEventArgs)`

Обработчик завершения редактирования объекта в окне "Параметры".

Parameters:
- `args`: Аргументы события

Remarks: В этой версии виртульного метода параметры более специфичны. Старая версия оставлена для совместимости.

### `ObjectSelectionChangedEventHandler(TFlex.ObjectEventArgs)`

ID: `M:TFlex.Plugin.ObjectSelectionChangedEventHandler(TFlex.ObjectEventArgs)`

Обработчик события, возникающего при изменения селекции документа

Parameters:
- `args`: Аргументы события

### `OnCallRestCallback(TFlex.Rest.Request)`

ID: `M:TFlex.Plugin.OnCallRestCallback(TFlex.Rest.Request)`

Событие вызова RESTful сервиса плагина. Формат входных/выходных данных зависит от конкретного плагина.

### `OnCommand(TFlex.CommandEventArgs)`

ID: `M:TFlex.Plugin.OnCommand(TFlex.CommandEventArgs)`

Приложение переопределяет эту функцию для получения команд, которые этим приложением зарегистрированы

Parameters:
- `args`: Аргументы команды

### `OnCommand(TFlex.Model.Document,System.Int32)`

ID: `M:TFlex.Plugin.OnCommand(TFlex.Model.Document,System.Int32)`

Приложение переопределяет эту функцию для получения команд, которые этим приложением зарегистрированы

Parameters:
- `pDocument`: Документ, который является активным в момент выполнения данной команды
- `id`: Идентификатор команды, под которым приложение эту команду зарегестрировало

### `OnCreateTools`

ID: `M:TFlex.Plugin.OnCreateTools`

В данной функции приложение должно создать свои панели инструментов, зарегистрировать свои пункты меню, а также создать другие средства пользовательского интерфейса (немодальные окна и др.).

### `OnExited`

ID: `M:TFlex.Plugin.OnExited`

Событие после закрытия главного окна

### `OnExiting(System.ComponentModel.CancelEventArgs)`

ID: `M:TFlex.Plugin.OnExiting(System.ComponentModel.CancelEventArgs)`

Событие перед закрытием главного окна. Закрытие окна может быть отменено.

Parameters:
- `args`: Аргументы события

### `OnFullRegenerationEventHandler(TFlex.FullRegenerationEventArgs)`

ID: `M:TFlex.Plugin.OnFullRegenerationEventHandler(TFlex.FullRegenerationEventArgs)`

Обработчик события, возникающего при полном пересчёте

Parameters:
- `args`: Аргументы события

### `OnInitialize`

ID: `M:TFlex.Plugin.OnInitialize`

Функция инициализации приложения. Приложение должно переопределить данную функцию для того, чтобы получить управление в момент его запуска.

### `OnModelConfigurationEventHandler(TFlex.ModelConfigurationEventArgs)`

ID: `M:TFlex.Plugin.OnModelConfigurationEventHandler(TFlex.ModelConfigurationEventArgs)`

Событие конфигурации модели

Parameters:
- `args`: Аргументы события

### `OnSessionInitialized(TFlex.SessionInitializedEventArgs)`

ID: `M:TFlex.Plugin.OnSessionInitialized(TFlex.SessionInitializedEventArgs)`

Событие возникает, когда инициализация T-FLEX CAD завершена

Parameters:
- `args`: Аргументы события

### `OnSystemCommand(TFlex.Model.Document,System.Int32)`

ID: `M:TFlex.Plugin.OnSystemCommand(TFlex.Model.Document,System.Int32)`

Обработка системной команды

### `OnUpdateCommand(TFlex.Command.CommandUI)`

ID: `M:TFlex.Plugin.OnUpdateCommand(TFlex.Command.CommandUI)`

Приложение переопределяет данную функцию для того, чтобы запрещать или разрешать выполнение своих команд, а также устанавливать переключатели в меню и инструментальнй панели

### `OnUpdateSystemCommand(TFlex.Command.CommandUI)`

ID: `M:TFlex.Plugin.OnUpdateSystemCommand(TFlex.Command.CommandUI)`

Обновление состояния системной команды

### `PlaneChangedEventHandler(TFlex.PlaneEventArgs)`

ID: `M:TFlex.Plugin.PlaneChangedEventHandler(TFlex.PlaneEventArgs)`

Обработчик события, возникающего при перемещении рабочей плоскости на линейке

Parameters:
- `args`: Аргументы события

### `PlaneCreateEventHandler(TFlex.PlaneCreateEventArgs)`

ID: `M:TFlex.Plugin.PlaneCreateEventHandler(TFlex.PlaneCreateEventArgs)`

Обработчик события, возникающего при создании рабочей плоскости на линейке

Parameters:
- `args`: Аргументы события

### `PluginCommandEventHandler(TFlex.PluginCommandEventArgs)`

ID: `M:TFlex.Plugin.PluginCommandEventHandler(TFlex.PluginCommandEventArgs)`

Класс, содержащий данные о событии - вызвана команда

Parameters:
- `args`: Аргументы события

### `ProductStructureUpdatingEventHandler(TFlex.ProductStructureUpdatingEventArgs)`

ID: `M:TFlex.Plugin.ProductStructureUpdatingEventHandler(TFlex.ProductStructureUpdatingEventArgs)`

Обработчик обновления структуры изделия. Приложение может добавить свои записи в нее.

Parameters:
- `args`: Аргументы события

### `RegeneratingDocumentEventHandler(TFlex.RegenerateDocumentEventArgs)`

ID: `M:TFlex.Plugin.RegeneratingDocumentEventHandler(TFlex.RegenerateDocumentEventArgs)`

Обработчик события, возникающего перед пересчетом документа

Parameters:
- `args`: Аргументы события

### `RegisterAutomenuCommand(System.Int32,System.String,System.Drawing.Icon)`

ID: `M:TFlex.Plugin.RegisterAutomenuCommand(System.Int32,System.String,System.Drawing.Icon)`

Регистрация команды автоменю

Parameters:
- `id`: Идентификатор команды автоменю
- `hint`: Комментарии, отображающиеся при наведении курсора на иконку команды автоменю и в статусной строке
- `icon`: Иконка команды автоменю (16х16 пикселей)

### `RegisterCommand(System.Int32,System.String,System.Drawing.Icon,System.Drawing.Icon)`

ID: `M:TFlex.Plugin.RegisterCommand(System.Int32,System.String,System.Drawing.Icon,System.Drawing.Icon)`

Регистрации команды приложения

Parameters:
- `id`: Идентификатор команды. Он должен быть уникальным в пределах приложения и не требует проверки на несовпадение с командами других приложения и самого T-FLEX CAD
- `prompt`: Название команды
- `smallIcon`: Маленькая иконка команды (16х16 пикселей)
- `largeIcon`: Большая иконка команды (24х24 пикселя)

### `RegisterCommand(System.Int32,TFlex.Command.CommandParameters)`

ID: `M:TFlex.Plugin.RegisterCommand(System.Int32,TFlex.Command.CommandParameters)`

Регистрации команды приложения

Parameters:
- `id`: Идентификатор команды. Он должен быть уникальным в пределах приложения и не требует проверки на несовпадение с командами других приложения и самого T-FLEX CAD
- `parameters`: Параметры команды

### `RegisterObjectCommand(System.Int32,System.String,System.Drawing.Icon,System.Drawing.Icon)`

ID: `M:TFlex.Plugin.RegisterObjectCommand(System.Int32,System.String,System.Drawing.Icon,System.Drawing.Icon)`

Регистрация команды объекта

Parameters:
- `id`: Идентификатор команды объекта. Он должен быть уникальным в пределах приложения и не требует проверки на несовпадение с командами других приложения и самого T-FLEX CAD
- `prompt`: Название команды объекта
- `smallIcon`: Маленькая иконка команды (16х16 пикселей)
- `largeIcon`: Большая иконка команды (24х24 пикселя)

### `RegisterObjectTypeIcon(System.Int32,System.Drawing.Icon)`

ID: `M:TFlex.Plugin.RegisterObjectTypeIcon(System.Int32,System.Drawing.Icon)`

Регистрация иконку объекта модели приложения

Parameters:
- `ID`: Идентификатор иконки
- `TypeIcon`: Иконка (16х16 пикселей)

### `RegisterSystemCommand(System.Int32)`

ID: `M:TFlex.Plugin.RegisterSystemCommand(System.Int32)`

Регистрация необходимости обработки одной из системных команд

### `SavingDocumentEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.SavingDocumentEventHandler(TFlex.DocumentEventArgs)`

Обработчик события, возникающего перед сохранением документа

Parameters:
- `args`: Аргументы события

### `SelectionChangedEventHandler(TFlex.DocumentEventArgs)`

ID: `M:TFlex.Plugin.SelectionChangedEventHandler(TFlex.DocumentEventArgs)`

Обработчик события, возникающего после изменения списка выбранных объектов без команды

Parameters:
- `args`: Аргументы события

### `ShowingExportDialogEventHandler(TFlex.ShowingImportExportDialogEventArgs)`

ID: `M:TFlex.Plugin.ShowingExportDialogEventHandler(TFlex.ShowingImportExportDialogEventArgs)`

Обработчик события, возникающего перед показом диалога экспорта

Parameters:
- `args`: Аргументы события

### `ShowingFullRegenerationWindowEventHandler(TFlex.ShowingFullRegenerationDialogEventArgs)`

ID: `M:TFlex.Plugin.ShowingFullRegenerationWindowEventHandler(TFlex.ShowingFullRegenerationDialogEventArgs)`

Обработчик события, возникающего перед показом диалога полного пересчёта

Parameters:
- `args`: Аргументы события

### `ShowingImportDialogEventHandler(TFlex.ShowingImportExportDialogEventArgs)`

ID: `M:TFlex.Plugin.ShowingImportDialogEventHandler(TFlex.ShowingImportExportDialogEventArgs)`

Обработчик события, возникающего перед показом диалога импорта

Parameters:
- `args`: Аргументы события

### `TrackingContextPopupMenuEventHandler(TFlex.TrackingContextPopupMenuEventArgs)`

ID: `M:TFlex.Plugin.TrackingContextPopupMenuEventHandler(TFlex.TrackingContextPopupMenuEventArgs)`

Обработчик события, возникающего перед показом контекстного меню объекта

Parameters:
- `args`: Аргументы события

### `ViewActivatedEventHandler(TFlex.ViewEventArgs)`

ID: `M:TFlex.Plugin.ViewActivatedEventHandler(TFlex.ViewEventArgs)`

Обработчик события, возникающего после активизации окна документа

Parameters:
- `args`: Аргументы события

### `ViewCreatedEventHandler(TFlex.ViewEventArgs)`

ID: `M:TFlex.Plugin.ViewCreatedEventHandler(TFlex.ViewEventArgs)`

Обработчик события, возникающего после создания окна документа

Parameters:
- `args`: Аргументы события

### `ViewDeactivatedEventHandler(TFlex.ViewEventArgs)`

ID: `M:TFlex.Plugin.ViewDeactivatedEventHandler(TFlex.ViewEventArgs)`

Обработчик события, возникающего после деактивизации окна документа

Parameters:
- `args`: Аргументы события

### `ViewRulerContextMenuCommandEventHandler(TFlex.ViewRulerContextMenuCommandEventArgs)`

ID: `M:TFlex.Plugin.ViewRulerContextMenuCommandEventHandler(TFlex.ViewRulerContextMenuCommandEventArgs)`

Обработчик события - вызвана локальная команда из контекстного меню линейки вида

Parameters:
- `args`: Аргументы события

### `WorkplaneCommandEventHandler(TFlex.WorkplaneCommandEventArgs)`

ID: `M:TFlex.Plugin.WorkplaneCommandEventHandler(TFlex.WorkplaneCommandEventArgs)`

Класс, содержащий данные о событии - вызвана команда управления рабочими плоскостями

Parameters:
- `args`: Аргументы события

## Propertys

### `ID`

ID: `P:TFlex.Plugin.ID`

Глобальный уникальный идентификатор приложения (GUID)

### `Name`

ID: `P:TFlex.Plugin.Name`

Название приложения
