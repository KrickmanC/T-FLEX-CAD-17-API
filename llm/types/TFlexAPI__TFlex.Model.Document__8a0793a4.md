# TFlex.Model.Document

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Класс документа T-FLEX CAD

## Methods

### `Activate`

ID: `M:TFlex.Model.Document.Activate`

Активизировать документ

### `ApplyChanges`

ID: `M:TFlex.Model.Document.ApplyChanges`

Применить изменения без закрытия блока изменения документа

Returns: Результат применения изменений

Remarks: Функция применяет изменения, сделаные после вызова функции `M:TFlex.Model.Document.BeginChanges(System.String)`

### `ApplyChanges(System.Boolean)`

ID: `M:TFlex.Model.Document.ApplyChanges(System.Boolean)`

Применить изменения без закрытия блока изменения документа

Parameters:
- `regenerate3D`: Переcчитать 3D документ

Returns: Результат применения изменений

Remarks: Функция применяет изменения, сделаные после вызова функции `M:TFlex.Model.Document.BeginChanges(System.String)` . В зависимости от параметра regenerate3D пересчитывает или нет 3D документ

### `AssignParametersToDOCs(System.IntPtr)`

ID: `M:TFlex.Model.Document.AssignParametersToDOCs(System.IntPtr)`

Cвязать переменные T-Flex CAD с параметрами документа DOCs

Parameters:
- `hDOCsHandle`: Идентификатор документа DOCs

### `AttachPlugin(TFlex.Plugin)`

ID: `M:TFlex.Model.Document.AttachPlugin(TFlex.Plugin)`

Подписаться на приход уведомлений о событиях для данного документа.

Parameters:
- `plugin`: Объект класса приложения

Remarks: Использование данного метода касается всех уведомлений, которые связаны с конкретным документом, а именно: `M:TFlex.Plugin.SavingDocumentEventHandler(TFlex.DocumentEventArgs)` - вызывается перед сохранением документа `M:TFlex.Plugin.DocumentSavedEventHandler(TFlex.DocumentEventArgs)` - вызывается после успешного сохранения документа `M:TFlex.Plugin.ClosingDocumentEventHandler(TFlex.DocumentEventArgs)` - вызывается перед закрытием документа `M:TFlex.Plugin.ViewActivatedEventHandler(TFlex.ViewEventArgs)` - вызывается после активизации окна документа `M:TFlex.Plugin.ViewDeactivatedEventHandler(TFlex.ViewEventArgs)` - вызывается после деактивизации окна документа `M:TFlex.Plugin.DynamicAnalysisSteppedEventHandler(TFlex.DynamicAnalysisEventArgs)` - вызывается при выполнении различных задач динамического анализа `M:TFlex.Plugin.ObjectCreatedEventHandler(TFlex.ObjectEventArgs)` - вызывается после создания объекта `M:TFlex.Plugin.DeletingObjectEventHandler(TFlex.ObjectEventArgs)` - вызывается перед удалением объекта `M:TFlex.Plugin.ObjectDeletedEventHandler(TFlex.ObjectEventArgs)` - вызывается после удаления объекта `M:TFlex.Plugin.ObjectChangedEventHandler(TFlex.ObjectEventArgs)` - вызывается после изменения объекта `M:TFlex.Plugin.ObjectSelectionChangedEventHandler(TFlex.ObjectEventArgs)` - вызывается при изменении селекции объекта `M:TFlex.Plugin.RegeneratingDocumentEventHandler(TFlex.RegenerateDocumentEventArgs)` - вызывается перед пересчётом документа `M:TFlex.Plugin.DocumentRegeneratedEventHandler(TFlex.RegenerateDocumentEventArgs)` - вызывается после пересчёта документа `M:TFlex.Plugin.TrackingContextPopupMenuEventHandler(TFlex.TrackingContextPopupMenuEventArgs)` - вызывается перед показом контекстного меню объекта `M:TFlex.Plugin.DrawingDocumentEventHandler(TFlex.DrawingDocumentEventArgs)` - вызывается перед отрисовкой документа `M:TFlex.Plugin.DocumentDrawnEventHandler(TFlex.DrawingDocumentEventArgs)` - вызывается после отрисовки документа

### `BeginChanges(System.String)`

ID: `M:TFlex.Model.Document.BeginChanges(System.String)`

Открытие блока изменения документа

Parameters:
- `name`: Задаёт имя блока изменения документа

Remarks: Для выполнения любых изменений в документе (создание новых объектов, удаление объектов, изменение объектов) необходимо открыть блок действий по изменению документа (блок изменения документа) Одновременно может быть открыт только один блок изменения документа. Вложение блоков изменения документа не допускается. Для закрытия блока изменения документа необходимо вызвать `M:TFlex.Model.Document.EndChanges` или `M:TFlex.Model.Document.CancelChanges` . Имя блока изменения документа отображается в диалоге отмены и повтора действий.

### `CancelChanges`

ID: `M:TFlex.Model.Document.CancelChanges`

Отменить все изменения и закрыть блок изменения документа

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` с отменой всех произведённых изменений.

### `CancelChanges(System.Boolean)`

ID: `M:TFlex.Model.Document.CancelChanges(System.Boolean)`

Отменить все изменения и закрыть блок изменения документа

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` с отменой всех произведённых изменений.

### `Close`

ID: `M:TFlex.Model.Document.Close`

Закрыть документ

Remarks: После выполнения операции, с документом нельзя производить никакие операции

### `ConvertLibraryFileLinksToDOCs(System.IntPtr)`

ID: `M:TFlex.Model.Document.ConvertLibraryFileLinksToDOCs(System.IntPtr)`

Переназначить ссылки на файлы в библиотеке T-Flex CAD на ссылки в библиотеке DOCs

Parameters:
- `hDOCsHandle`: Идентификатор документа DOCs

### `CopyObjects(System.Collections.Generic.List`1{TFlex.Model.ModelObject},TFlex.Model.CopyObjectsOptions)`

ID: `M:TFlex.Model.Document.CopyObjects(System.Collections.Generic.List`1{TFlex.Model.ModelObject},TFlex.Model.CopyObjectsOptions)`

Копирование модельных объектов с учётом афинного преобразования на заданную страницу

Parameters:
- `sourceObjects`: Список копируемых модельных объектов
- `options`: Настройки

Remarks: Данный метод позволяет копировать в текущий документ модельные объекты из другого документа

### `CopyObjects(TFlex.Model.Page,System.Collections.Generic.List`1{TFlex.Model.ModelObject},TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Model.Document.CopyObjects(TFlex.Model.Page,System.Collections.Generic.List`1{TFlex.Model.ModelObject},TFlex.Drawing.AffineMap)`

Копирование модельных объектов с учётом афинного преобразования на заданную страницу

Parameters:
- `targetPage`: Страница на которую копируются объекты
- `sourceObjects`: Список копируемых модельных объектов
- `affineMap`: Аффинное преобразование

Remarks: Данный метод позволяет копировать в текущий документ модельные объекты из другого документа

### `CreateRealVariable(System.String,System.Double)`

ID: `M:TFlex.Model.Document.CreateRealVariable(System.String,System.Double)`

Создает новую вещественную переменную

### `CreateRealVariable(System.String,System.Doubleref ,TFlex.Model.CreateVariableMode)`

ID: `M:TFlex.Model.Document.CreateRealVariable(System.String,System.Double@,TFlex.Model.CreateVariableMode)`

Создает новую вещественную переменную

### `CreateTextVariable(System.String,System.String)`

ID: `M:TFlex.Model.Document.CreateTextVariable(System.String,System.String)`

Создает новую текстовую переменную

### `CreateVariable(System.String)`

ID: `M:TFlex.Model.Document.CreateVariable(System.String)`

Создает новую переменную

### `DeleteObjects(TFlex.Model.ObjectArray,TFlex.Model.DeleteOptions)`

ID: `M:TFlex.Model.Document.DeleteObjects(TFlex.Model.ObjectArray,TFlex.Model.DeleteOptions)`

Удаление объектов документа

Parameters:
- `objects`: Массив удаляемых объектов модели
- `options`: Опции удаления объектов модели

Returns: true в случае успешного удаления, иначе false

### `DeletePage(TFlex.Model.Page,TFlex.Model.DeleteOptions)`

ID: `M:TFlex.Model.Document.DeletePage(TFlex.Model.Page,TFlex.Model.DeleteOptions)`

Удаление страницы

Parameters:
- `page`: Удаляемая страница
- `options`: Опции удаления

Returns: true в случае успешного удаления, иначе false

### `DeletePages(System.Collections.Generic.ICollection`1{TFlex.Model.Page},TFlex.Model.DeleteOptions)`

ID: `M:TFlex.Model.Document.DeletePages(System.Collections.Generic.ICollection`1{TFlex.Model.Page},TFlex.Model.DeleteOptions)`

Удаление страниц документа

Parameters:
- `pages`: Массив удаляемых страниц
- `options`: Опции удаления страниц

Returns: true в случае успешного удаления, иначе false

### `DeleteUnusedObjects(TFlex.Model.DeleteUnusedOptions)`

ID: `M:TFlex.Model.Document.DeleteUnusedObjects(TFlex.Model.DeleteUnusedOptions)`

Удаление неиспользуемых объектов документа

Parameters:
- `options`: Опции удаления объектов модели

Returns: true в случае успешного удаления, иначе false

### `DetachPlugin(TFlex.Plugin)`

ID: `M:TFlex.Model.Document.DetachPlugin(TFlex.Plugin)`

Отписаться от прихода уведомлений о событиях для данного документа

Parameters:
- `plugin`: Объект класса приложения

### `Dispose`

ID: `M:TFlex.Model.Document.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `Draw(TFlex.Drawing.Graphics,TFlex.Model.Page)`

ID: `M:TFlex.Model.Document.Draw(TFlex.Drawing.Graphics,TFlex.Model.Page)`

Прорисовка указанной страниницы документа в указанный объект вывода графичесого изображения

Parameters:
- `graphics`: Объект вывода графичекого изображения
- `pg`: Страница документа, которую необходимо вывести

### `EndChanges`

ID: `M:TFlex.Model.Document.EndChanges`

Применить изменения и закрыть блок изменения документа

Returns: Результат применения изменений

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` Функция автоматически применяет все изменения блока если они являются корректными. В таком случае возвращаемое значение равно OK. Иначе все изменения отменяются.

### `EndChanges(System.Boolean)`

ID: `M:TFlex.Model.Document.EndChanges(System.Boolean)`

Применить изменения и закрыть блок изменения документа

Parameters:
- `Unconditionally`: Условие корректности модели с ошибками пересчёта

Returns: Результат применения изменений

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` . Функция автоматически применяет все изменения блока если они являются корректными. В таком случае возвращаемое значение равно OK. Иначе все изменения отменяются. В данном случае модель с ошибками пересчёта является корректной

### `EndChanges(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Document.EndChanges(System.Boolean,System.Boolean)`

Применить изменения и закрыть блок изменения документа

Parameters:
- `Unconditionally`: Условие корректности модели с ошибками пересчёта
- `Regenerate`: Пересчитывать модель

Returns: Результат применения изменений

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` . Функция автоматически применяет все изменения блока если они являются корректными. В таком случае возвращаемое значение равно OK. Иначе все изменения отменяются. В данном случае модель с ошибками пересчёта является корректной

### `EndChanges(System.Boolean,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Document.EndChanges(System.Boolean,System.Boolean,System.Boolean)`

Применить изменения и закрыть блок изменения документа

Parameters:
- `Unconditionally`: Условие корректности модели с ошибками пересчета
- `Regenerate`: Пересчитывать модель
- `Merge`: Объединить Undo-блок с верхним Undo-блоком

Returns: Результат применения изменений

Remarks: Функция закрывает блок изменения документа, открытый при помощи функции `M:TFlex.Model.Document.BeginChanges(System.String)` . Функция автоматически применяет все изменения блока если они являются корректными. В таком случае возвращаемое значение равно OK. Иначе все изменения отменяются. В данном случае модель с ошибками пересчёта является корректной

### `EndChanges(TFlex.Model.EndChangesOptions)`

ID: `M:TFlex.Model.Document.EndChanges(TFlex.Model.EndChangesOptions)`

Применить изменения и закрыть блок изменения документа

Parameters:
- `options`: Параметры

Returns: Результат применения изменений

### `ExportIcon(System.String)`

ID: `M:TFlex.Model.Document.ExportIcon(System.String)`

Экспорт иконки

Parameters:
- `pathName`: Имя выходного файла

Returns: Результат экспорта

### `FindVariable(System.String)`

ID: `M:TFlex.Model.Document.FindVariable(System.String)`

Найти переменную по имени

Parameters:
- `name`: Имя переменной

Returns: Переменная

### `Get2DObjects`

ID: `M:TFlex.Model.Document.Get2DObjects`

Контейнер всех 2D объектов документа

### `GetAssemblyContextData2D`

ID: `M:TFlex.Model.Document.GetAssemblyContextData2D`

### `GetAttributes`

ID: `M:TFlex.Model.Document.GetAttributes`

Получить контейнер атрибутов документа

Returns: Контейнер атрибутов документа

Remarks: Приложение может использовать данный контейнер для хранения своих данных, связанных с документом

### `GetClosestObject(TFlex.Drawing.Point,TFlex.Model.Page,TFlex.Model.SelectionFilter)`

ID: `M:TFlex.Model.Document.GetClosestObject(TFlex.Drawing.Point,TFlex.Model.Page,TFlex.Model.SelectionFilter)`

Получить объект, ближайший к заданной точке на заданной странице с учётом фильтра

Parameters:
- `point`: Точка на чертеже
- `page`: Страница чертежа
- `filter`: Фильтр объектов

Returns: Найденный объект или null если объект не найден

### `GetClosestObject(TFlex.Drawing.Point,TFlex.Model.Page,TFlex.Model.SelectionFilter,System.Double)`

ID: `M:TFlex.Model.Document.GetClosestObject(TFlex.Drawing.Point,TFlex.Model.Page,TFlex.Model.SelectionFilter,System.Double)`

Получить объект, ближайший к заданной точке на заданной странице с учётом фильтра

Parameters:
- `point`: Точка на чертеже
- `page`: Страница чертежа
- `filter`: Фильтр объектов
- `maxdistance`: Максимальное расстояние

Returns: Найденный объект или null если объект не найден

### `GetDrawingNotes`

ID: `M:TFlex.Model.Document.GetDrawingNotes`

Получение объекта технических требований

Returns: Найденный объект или null если объект не найден

### `GetObjectByID(System.UInt32)`

ID: `M:TFlex.Model.Document.GetObjectByID(System.UInt32)`

Получение объекта по идентификатору

Parameters:
- `id`: Идентификатор объекта

Returns: Найденный объект или null если объект не найден

### `GetObjectById(TFlex.Model.ObjectId)`

ID: `M:TFlex.Model.Document.GetObjectById(TFlex.Model.ObjectId)`

Получение объекта по идентификатору

Parameters:
- `id`: Идентификатор объекта

Returns: Найденный объект или null если объект не найден

### `GetObjectByName(System.String)`

ID: `M:TFlex.Model.Document.GetObjectByName(System.String)`

Получение объекта по имени

Parameters:
- `name`: Имя объекта

Returns: Найденный объект или null если объект не найден

### `GetObjects`

ID: `M:TFlex.Model.Document.GetObjects`

Контейнер всех объектов документа

### `GetPages`

ID: `M:TFlex.Model.Document.GetPages`

Получить контейнер страниц документа

### `GetRealProperty(System.String)`

ID: `M:TFlex.Model.Document.GetRealProperty(System.String)`

Получить значение свойства элемента

### `GetShortPathName(System.String)`

ID: `M:TFlex.Model.Document.GetShortPathName(System.String)`

Получение короткого пути относительно файла документа

Parameters:
- `fileName`: Имя файла

Returns: Короткий путь к файлу

### `GetTextProperty(System.String)`

ID: `M:TFlex.Model.Document.GetTextProperty(System.String)`

Получить значение свойства элемента

### `ImportIcon(System.String)`

ID: `M:TFlex.Model.Document.ImportIcon(System.String)`

Импорт иконки

Parameters:
- `pathName`: Имя выходного файла

### `ImportPreview(TFlex.Model.Document)`

ID: `M:TFlex.Model.Document.ImportPreview(TFlex.Model.Document)`

Импорт предварительного просмотра документа

Parameters:
- `sourceDocument`: Исходный документ

### `InsertFragment(System.String)`

ID: `M:TFlex.Model.Document.InsertFragment(System.String)`

Вставить фрагмент

### `InsertFragment(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Document.InsertFragment(TFlex.Model.FileLink)`

Вставить фрагмент

### `IsChanging`

ID: `M:TFlex.Model.Document.IsChanging`

Проверка того, что открыт блок изменения документа

Returns: True если блок изменения документа открыт, в противном случае false

### `MacroExists(System.String)`

ID: `M:TFlex.Model.Document.MacroExists(System.String)`

Проверка наличия макроса с указанным именем

Parameters:
- `macro`: Имя макроса

Returns: true если макрос существует

### `MacroExists(System.String,System.Boolean)`

ID: `M:TFlex.Model.Document.MacroExists(System.String,System.Boolean)`

Проверка наличия макроса с указанным именем

Parameters:
- `macro`: Имя макроса
- `macroWithParameters`: Проверять макросы с аргументами

Returns: true если макрос существует

### `MergeTwoTailUndoBlocks`

ID: `M:TFlex.Model.Document.MergeTwoTailUndoBlocks`

Объединить два верхних Undo-блока

### `Open2DView`

ID: `M:TFlex.Model.Document.Open2DView`

Создать новое 2D окно документа

Returns: Объект вида документа

### `Open3DView`

ID: `M:TFlex.Model.Document.Open3DView`

Создать новое 3D окно документа

Returns: Объект вида документа

### `OpenWorkplaneView(TFlex.Model.Page)`

ID: `M:TFlex.Model.Document.OpenWorkplaneView(TFlex.Model.Page)`

Создать новое 2D окно документа с активной рабочей плоскостью

Parameters:
- `page`: Страница документа

Returns: Объект вида документа

### `Print(System.IntPtr,System.Boolean)`

ID: `M:TFlex.Model.Document.Print(System.IntPtr,System.Boolean)`

Печать документа

Parameters:
- `window`: Родительское окно
- `selectAllPages`: Выбрать все страницы, иначе - только активную

### `Print(System.IntPtr,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Document.Print(System.IntPtr,System.Boolean,System.Boolean)`

Печать документа

Parameters:
- `window`: Родительское окно
- `selectAllPages`: Выбрать все страницы, иначе - только активную
- `fitAndCenter`: Центрировать и вписать в страницу

Examples:
- `public static void DocPrint(IntPtr window) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа bool selectAllPages = true; //true-выбрать все страницы, false - только активную bool fitAndCenter = true;//Центрировать и вписать в страницу //метод вызывает диалоговое окно. document.Print(window, selectAllPages, fitAndCenter); //document.PrintNoDialog(); //печать без диалгового окна }`
- `public static void DocPrint(IntPtr window) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа bool selectAllPages = true; //true-выбрать все страницы, false - только активную bool fitAndCenter = true;//Центрировать и вписать в страницу //метод вызывает диалоговое окно. document.Print(window, selectAllPages, fitAndCenter); //document.PrintNoDialog(); //печать без диалгового окна }`

### `Print(TFlex.Model.PrintOptions)`

ID: `M:TFlex.Model.Document.Print(TFlex.Model.PrintOptions)`

Печать документа

Parameters:
- `options`: Параметры печати

### `PrintNoDialog`

ID: `M:TFlex.Model.Document.PrintNoDialog`

Печать документа

### `PrintPage(System.IntPtr,TFlex.Model.Page)`

ID: `M:TFlex.Model.Document.PrintPage(System.IntPtr,TFlex.Model.Page)`

Печать документа

Parameters:
- `window`: Родительское окно
- `page`: Страница для печати

### `PrintPages(System.IntPtr,TFlex.Model.ObjectArray)`

ID: `M:TFlex.Model.Document.PrintPages(System.IntPtr,TFlex.Model.ObjectArray)`

Печать страниц документа

Parameters:
- `window`: Родительское окно
- `pages`: Страницы для печати

### `RedoChanges`

ID: `M:TFlex.Model.Document.RedoChanges`

Повторить изменения, сохранённые в последнем отменённом Undo-блоке

### `RedoChanges(System.UInt32)`

ID: `M:TFlex.Model.Document.RedoChanges(System.UInt32)`

Отменить изменения, сохранённые в `n` верхних Undo-блоках

### `Redraw`

ID: `M:TFlex.Model.Document.Redraw`

Перерисовка всех видов документа

### `Redraw(System.Boolean)`

ID: `M:TFlex.Model.Document.Redraw(System.Boolean)`

Перерисовка всех видов документа

Parameters:
- `updateNow`: Перерисовать синхронно

### `Regenerate(TFlex.Model.RegenerateOptions)`

ID: `M:TFlex.Model.Document.Regenerate(TFlex.Model.RegenerateOptions)`

Пересчёт модели с заданными опциями

Parameters:
- `options`: Опции регенерации модели

### `Regenerate3D`

ID: `M:TFlex.Model.Document.Regenerate3D`

Пересчёт 3D модели без открытия блока изменения документа `M:TFlex.Model.Document.BeginChanges(System.String)`

Returns: true в случае успешного пересчёта, в противном случае false

### `RenameChanges(System.String)`

ID: `M:TFlex.Model.Document.RenameChanges(System.String)`

Задать новое имя блока изменения документа

Parameters:
- `name`: Задаёт новое имя блока изменения документа

### `RunMacro(System.String)`

ID: `M:TFlex.Model.Document.RunMacro(System.String)`

Выполнить макрос с заданным именем

Parameters:
- `macro`: Имя макроса

Returns: true макрос был выполнен успешно

### `RunMacro(System.String,System.Object[])`

ID: `M:TFlex.Model.Document.RunMacro(System.String,System.Object[])`

Выполнить макрос с заданным именем и передать в него параметры

Parameters:
- `macro`: Имя макроса
- `parameters`: Аргументы для вызова метода

Returns: Возвращает результат выполнения макроса

### `Save`

ID: `M:TFlex.Model.Document.Save`

Сохранить документ

Returns: true если операция сохранения была успешной

### `Save(TFlex.Model.SaveOptions)`

ID: `M:TFlex.Model.Document.Save(TFlex.Model.SaveOptions)`

Сохранить документ

Parameters:
- `options`: Опции сохранения документа

Returns: true если операция сохранения была успешной

### `SaveAs(System.String)`

ID: `M:TFlex.Model.Document.SaveAs(System.String)`

Сохранить документ в другой файл

Parameters:
- `fileName`: Имя файла

Returns: true если операция сохранения была успешной

### `SaveCopy(System.String)`

ID: `M:TFlex.Model.Document.SaveCopy(System.String)`

Сохранить текущее состояние документа в другой файл

Parameters:
- `fileName`: Имя файла

Returns: true если операция сохранения была успешной

### `SaveInNomenclature(System.Boolean)`

ID: `M:TFlex.Model.Document.SaveInNomenclature(System.Boolean)`

Сохранить документ в справочник электронной структуры изделия T-FLEX DOCs

Parameters:
- `recursive`: Сохранять сборку со всеми входящими фрагментами

### `SaveInNomenclature(System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Document.SaveInNomenclature(System.Boolean,System.Boolean)`

Сохранить документ в справочник электронной структуры изделия T-FLEX DOCs

Parameters:
- `recursive`: Сохранять сборку со всеми входящими фрагментами
- `autoCheckIn`: Автоматическое применение изменений

### `SaveInNomenclature(TFlex.Model.SaveInNomenclatureOptions)`

ID: `M:TFlex.Model.Document.SaveInNomenclature(TFlex.Model.SaveInNomenclatureOptions)`

Сохранить документ в справочник электронной структуры изделия T-FLEX DOCs

Parameters:
- `options`: Опции сохранения документа

### `SaveModified`

ID: `M:TFlex.Model.Document.SaveModified`

Показать диалог сохранения изменений в документе

Returns: false - для отмены, в противном случае - true

### `SaveModified(TFlex.Model.SaveOptions)`

ID: `M:TFlex.Model.Document.SaveModified(TFlex.Model.SaveOptions)`

Показать диалог сохранения изменений в документе

Parameters:
- `options`: Опции сохранения документа

Returns: false - для отмены, в противном случае - true

### `SetExplodeStatus(System.Boolean)`

ID: `M:TFlex.Model.Document.SetExplodeStatus(System.Boolean)`

Перевод 3D модели в режим сборки-разборки без открытия блока изменения документа `M:TFlex.Model.Document.BeginChanges(System.String)`

### `ShowLastErrorDialog`

ID: `M:TFlex.Model.Document.ShowLastErrorDialog`

Показать диалоговое окно с информацией о последней ошибке, возникшей в документе

### `ShowVariablesDialog`

ID: `M:TFlex.Model.Document.ShowVariablesDialog`

Показать диалог "Переменные модели"

### `UndoChanges`

ID: `M:TFlex.Model.Document.UndoChanges`

Отменить изменения, сохранённые в верхнем Undo-блоке

### `UndoChanges(System.UInt32)`

ID: `M:TFlex.Model.Document.UndoChanges(System.UInt32)`

Отменить изменения, сохранённые в `n` верхних Undo-блоках

## Propertys

### `ActivePage`

ID: `P:TFlex.Model.Document.ActivePage`

Активная страница документа или 0 если нет такой страницы

### `ActiveView`

ID: `P:TFlex.Model.Document.ActiveView`

Объект класса View, представляющий активный (текущий) вид документа

Returns: Mожет вернуть 0 в том случае если у документа нет активного вида или вообще нет видов.

Remarks: У документа есть виды только в том случае, если он открыт для редактирования и не является документом фрагмента или временным документом.

### `BOMData`

ID: `P:TFlex.Model.Document.BOMData`

Контейнер данных для спецификации

### `Bodies`

ID: `P:TFlex.Model.Document.Bodies`

Контейнер всех тел

### `Changed`

ID: `P:TFlex.Model.Document.Changed`

Признак изменения документа

### `CloseAfterCurrentMacroCompletion`

ID: `P:TFlex.Model.Document.CloseAfterCurrentMacroCompletion`

Закрыть документ после завершения текущего макроса

### `DecorationManager`

ID: `P:TFlex.Model.Document.DecorationManager`

Для внутреннего использования

### `Diagnostics`

ID: `P:TFlex.Model.Document.Diagnostics`

Контейнер диагностических сообщений документа или 0, если контейнера нет

### `DraggerManager`

ID: `P:TFlex.Model.Document.DraggerManager`

Для внутреннего использования

### `ExplodeMode`

ID: `P:TFlex.Model.Document.ExplodeMode`

Режим разборки 3D модели

Remarks: Открытие блока изменения документа является необязательным `M:TFlex.Model.Document.BeginChanges(System.String)`

### `ExportToBMF`

ID: `P:TFlex.Model.Document.ExportToBMF`

Объект, экспортирующий документ в формат BMF

### `ExportToBitmap`

ID: `P:TFlex.Model.Document.ExportToBitmap`

Объект, экспортирующий документ в растровые форматы

### `ExportToDWG`

ID: `P:TFlex.Model.Document.ExportToDWG`

Объект, экспортирующий документ в формат DWG

### `ExportToDXF`

ID: `P:TFlex.Model.Document.ExportToDXF`

Объект, экспортирующий документ в формат DXF

### `ExportToDXF3D`

ID: `P:TFlex.Model.Document.ExportToDXF3D`

Объект, экспортирующий документ в формат DXF 3D

### `ExportToIGES`

ID: `P:TFlex.Model.Document.ExportToIGES`

Объект, экспортирующий документ в формат IGES

### `ExportToInventor`

ID: `P:TFlex.Model.Document.ExportToInventor`

Объект, экспортирующий документ в формат Open Inventor

### `ExportToMetafile`

ID: `P:TFlex.Model.Document.ExportToMetafile`

Объект, экспортирующий документ формата Windows Enhanced Metafile (EMF)

### `ExportToMetafileWMF`

ID: `P:TFlex.Model.Document.ExportToMetafileWMF`

Объект, экспортирующий документ формата Windows Metafile (WMF)

### `ExportToParasolid`

ID: `P:TFlex.Model.Document.ExportToParasolid`

Объект, экспортирующий документ в форматы Parasolid

### `ExportToRhino`

ID: `P:TFlex.Model.Document.ExportToRhino`

Объект, экспортирующий документ в формат Rhino

### `ExportToSTEP`

ID: `P:TFlex.Model.Document.ExportToSTEP`

Объект, экспортирующий документ в формат STEP

### `ExportToSTL`

ID: `P:TFlex.Model.Document.ExportToSTL`

Объект, экспортирующий документ в формат STL

### `ExportToVRML`

ID: `P:TFlex.Model.Document.ExportToVRML`

Объект, экспортирующий документ в формат VRML

### `ExportVariables`

ID: `P:TFlex.Model.Document.ExportVariables`

Объект, экспортирующий переменные документа

### `FileLinks`

ID: `P:TFlex.Model.Document.FileLinks`

Ссылки на файлы

### `FileName`

ID: `P:TFlex.Model.Document.FileName`

Полный путь файла документа, включая имя файла

### `FilePath`

ID: `P:TFlex.Model.Document.FilePath`

Путь файла документа, не включая имя файла

### `HasPdmNomenclatureReference`

ID: `P:TFlex.Model.Document.HasPdmNomenclatureReference`

Документ ассоциирован с объектом номенклатуры

### `ImportFromACAD`

ID: `P:TFlex.Model.Document.ImportFromACAD`

Объект, импортирующий данные из формата AutoCAD

### `ImportFromParasolid`

ID: `P:TFlex.Model.Document.ImportFromParasolid`

Объект, импортирующий данные из формата Parasolid

### `ImportFromSTEP`

ID: `P:TFlex.Model.Document.ImportFromSTEP`

Объект, импортирующий данные из формата STEP

### `ImportVariables`

ID: `P:TFlex.Model.Document.ImportVariables`

Объект, импортирующий переменные документа

### `InsertMethod`

ID: `P:TFlex.Model.Document.InsertMethod`

Способ вставки фрагмента

### `InsertMethodString`

ID: `P:TFlex.Model.Document.InsertMethodString`

Способ вставки фрагмента (строка)

### `IsAnnotation`

ID: `P:TFlex.Model.Document.IsAnnotation`

Проверка того, что документ является аннотацией

Returns: `true` , если документ является аннотацией, иначе `false`

### `IsDisposed`

ID: `P:TFlex.Model.Document.IsDisposed`

Возвращает true, если вызывался Dispose()

### `IsFragment`

ID: `P:TFlex.Model.Document.IsFragment`

Режим открытия документа в качестве фрагмента

Returns: True если документ вставлен как фрагмент, иначе False

### `IsReadOnly`

ID: `P:TFlex.Model.Document.IsReadOnly`

Проверка доступности файла документа для записи `M:TFlex.Model.Document.BeginChanges(System.String)` method

Returns: True если файл документа недоступен для записи, иначе false

### `IsUIVisible`

ID: `P:TFlex.Model.Document.IsUIVisible`

Проверка отображения документа в пользовательском интерфейсе

Returns: `true` , если документ отображается либо будет отображён в пользовательском интерфейса, иначе `false`

### `LastSavedVersion`

ID: `P:TFlex.Model.Document.LastSavedVersion`

Версия системы, в которой документ был сохранён последний раз

### `MacroNames`

ID: `P:TFlex.Model.Document.MacroNames`

Список полных имен макросов

### `ModelConfigurations`

ID: `P:TFlex.Model.Document.ModelConfigurations`

Контейнер конфигураций модели

### `ModelObjectGroups`

ID: `P:TFlex.Model.Document.ModelObjectGroups`

Группы элементов

### `PageTypesVisibleInTabs`

ID: `P:TFlex.Model.Document.PageTypesVisibleInTabs`

Получить типы страниц, видимых на вкладках

### `PdmLinkedObject`

ID: `P:TFlex.Model.Document.PdmLinkedObject`

Объект PDM-системы в контексте которого открыт документ

### `PdmNomenclatureObject`

ID: `P:TFlex.Model.Document.PdmNomenclatureObject`

Объект номенклатуры PDM-системы в контексте которого открыт документ

### `Properties`

ID: `P:TFlex.Model.Document.Properties`

Свойства документа

### `Scene`

ID: `P:TFlex.Model.Document.Scene`

Для внутреннего использования

### `Selection`

ID: `P:TFlex.Model.Document.Selection`

Селектор документа

Remarks: Объект класса `T:TFlex.Model.SelectionContainer` . может быть 0 в случае если документ не имеет селектора. Не иметь селектора может, например, документ, используемый в качестве фрагмента.

### `StructureElements`

ID: `P:TFlex.Model.Document.StructureElements`

Вспомогательный объект для работы со структурными элементами

### `Title`

ID: `P:TFlex.Model.Document.Title`

Имя документа

### `Views`

ID: `P:TFlex.Model.Document.Views`

Вид данного документа

### `Visible`

ID: `P:TFlex.Model.Document.Visible`

Проверка является ли документ видимым

Returns: True если документ является видимым
