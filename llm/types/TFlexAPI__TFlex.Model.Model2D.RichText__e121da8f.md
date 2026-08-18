# TFlex.Model.Model2D.RichText

Assembly: `TFlexAPI`
Namespace: `TFlex.Model.Model2D`

## Summary

Базовый класс форматированного текста

## Methods

### `BeginEdit`

ID: `M:TFlex.Model.Model2D.RichText.BeginEdit`

Начало редактирования текста

Remarks: Функция устанавливает текст в режим редактирования для последующей работы с ним

### `ClearAll`

ID: `M:TFlex.Model.Model2D.RichText.ClearAll`

Очистка содержимого всего текста

### `CopyToClipboard`

ID: `M:TFlex.Model.Model2D.RichText.CopyToClipboard`

Копировать выделенный текст в буфер обмена

### `CreateTable(System.UInt32,TFlex.Model.Model2D.Table.CreationSettings)`

ID: `M:TFlex.Model.Model2D.RichText.CreateTable(System.UInt32,TFlex.Model.Model2D.Table.CreationSettings)`

Создание таблицы перед символом, заданным порядковым номером относительно начала текста

Parameters:
- `position`: Порядковый номер символа, перед которым надо вставить таблицу, относительно начала текста
- `settings`: Параметры создания таблицы

Returns: Таблица

### `CreateTable(TFlex.Model.Model2D.Table.CreationSettings)`

ID: `M:TFlex.Model.Model2D.RichText.CreateTable(TFlex.Model.Model2D.Table.CreationSettings)`

Создание таблицы перед символом, на котором находится курсор

Parameters:
- `settings`: Параметры создания таблицы

Returns: Таблица

Remarks: После создания таблицы, курсор перемещается в начало первой ячейки

### `Delete`

ID: `M:TFlex.Model.Model2D.RichText.Delete`

Удаление выделенного фрагмента или символа, на котором находится курсор

### `Delete(System.UInt32)`

ID: `M:TFlex.Model.Model2D.RichText.Delete(System.UInt32)`

Удаление нескольких символов, начиная с того, на котором находится курсор

Parameters:
- `count`: Количество удаляемых символов

Remarks: Параметры выделения фрагмента будут потеряны

### `Deselect`

ID: `M:TFlex.Model.Model2D.RichText.Deselect`

Снятие выделения

Remarks: Курсор будет находиться там, где был конец выделенного фрагмента

### `EditInModalWindow(TFlex.Model.Model2D.RichText.EditData)`

ID: `M:TFlex.Model.Model2D.RichText.EditInModalWindow(TFlex.Model.Model2D.RichText.EditData)`

Редактировать текст в модальном диалоге

### `EndEdit`

ID: `M:TFlex.Model.Model2D.RichText.EndEdit`

Завершение редактирования текста

### `ExportToExcel(TFlex.Model.Model2D.RichTextExcelExportOptions)`

ID: `M:TFlex.Model.Model2D.RichText.ExportToExcel(TFlex.Model.Model2D.RichTextExcelExportOptions)`

Экспортировать текст в Excel

Parameters:
- `options`: Параметры экспорта

### `GetCursorInfo`

ID: `M:TFlex.Model.Model2D.RichText.GetCursorInfo`

Получение параметров положения курсора в тексте

Returns: Параметры положения курсора

### `GetDefaultFontSize`

ID: `M:TFlex.Model.Model2D.RichText.GetDefaultFontSize`

Получение размера символов, используемого по умолчанию

### `GetSelectedRtfText`

ID: `M:TFlex.Model.Model2D.RichText.GetSelectedRtfText`

Получение выделенного текста в формате RTF

Returns: Выделенный текст в формате RTF

### `GetSelectedText`

ID: `M:TFlex.Model.Model2D.RichText.GetSelectedText`

Получение выделенного текста

Returns: Выделенный текст

### `GetSelection(TFlex.Model.Model2D.Position*,TFlex.Model.Model2D.Position*)`

ID: `M:TFlex.Model.Model2D.RichText.GetSelection(TFlex.Model.Model2D.Position*,TFlex.Model.Model2D.Position*)`

Получение границ выделенного фрагмента

Parameters:
- `begining`: Начало выделенного фрагмента
- `end`: Конец выделенного фрагмента

### `GetTableByIndex(System.UInt32)`

ID: `M:TFlex.Model.Model2D.RichText.GetTableByIndex(System.UInt32)`

Получение таблицы по её порядковому номеру

Parameters:
- `index`: Порядковый номер таблицы относительно начала текста

Returns: Таблица

### `GetTablePosition(TFlex.Model.Model2D.Table)`

ID: `M:TFlex.Model.Model2D.RichText.GetTablePosition(TFlex.Model.Model2D.Table)`

Получение порядкового номера символа, перед которым находится таблица, относительно начала текста

Parameters:
- `table`: Таблица

Returns: Порядковый номер символа, перед которым находится таблица, относительно начала текста

### `GetText(TFlex.Model.Model2D.Position,TFlex.Model.Model2D.Position)`

ID: `M:TFlex.Model.Model2D.RichText.GetText(TFlex.Model.Model2D.Position,TFlex.Model.Model2D.Position)`

Получение текста, находящегося в заданном отрезке

Parameters:
- `pos1`: Начало отрезка
- `pos2`: Конец отрезка

Returns: Текст, находящийся в заданном отрезке

### `InsertCommonSymbol(TFlex.Model.Model2D.CommonSymbol)`

ID: `M:TFlex.Model.Model2D.RichText.InsertCommonSymbol(TFlex.Model.Model2D.CommonSymbol)`

Вставка символа

Parameters:
- `symbol`: Символ

### `InsertCopyOfTable(System.UInt32,TFlex.Model.Model2D.Table)`

ID: `M:TFlex.Model.Model2D.RichText.InsertCopyOfTable(System.UInt32,TFlex.Model.Model2D.Table)`

Вставка копии таблицы перед символом, заданным порядковым номером относительно начала текста

Parameters:
- `position`: Порядковый номер символа, перед которым надо вставить таблицу, относительно начала текста
- `table`: Таблица, копию которой надо создать

Returns: Копия таблицы

### `InsertCopyOfTable(TFlex.Model.Model2D.Table)`

ID: `M:TFlex.Model.Model2D.RichText.InsertCopyOfTable(TFlex.Model.Model2D.Table)`

Вставка копии таблицы перед символом, на котором находится курсор

Parameters:
- `table`: Таблица, копию которой надо создать

Returns: Копия таблицы

Remarks: После создания таблицы, курсор перемещается в начало первой ячейки

### `InsertFormLimitsSymbol(TFlex.Model.Model2D.Formlimits)`

ID: `M:TFlex.Model.Model2D.RichText.InsertFormLimitsSymbol(TFlex.Model.Model2D.Formlimits)`

Вставка обозначения базы или допуска формы или расположения

Parameters:
- `obj`: Обозначение базы или допуска формы или расположения

### `InsertFraction(System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RichText.InsertFraction(System.String,System.String)`

Вставка дроби

Parameters:
- `upper`: Строка числителя (может отсутствовать)
- `lower`: Строка знаменателя (может отсутствовать)

Remarks: При создании дроби используется значение масштаба шрифта, указанное в свойстве `P:TFlex.Model.Model2D.RichText.CurrFractionScale`

### `InsertFragment`

ID: `M:TFlex.Model.Model2D.RichText.InsertFragment`

Вставка фрагмента с указанием ссылки

Returns: Добавленный фрагмент

### `InsertFragment(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.RichText.InsertFragment(TFlex.Model.FileLink)`

Вставка фрагмента с указанием ссылки

Parameters:
- `link`: Используемая ссылка

### `InsertFragment(TFlex.Model.FileLink,TFlex.Model.Model2D.RichText.InsertObjectOptions)`

ID: `M:TFlex.Model.Model2D.RichText.InsertFragment(TFlex.Model.FileLink,TFlex.Model.Model2D.RichText.InsertObjectOptions)`

Вставка фрагмента с указанием ссылки

Parameters:
- `link`: Используемая ссылка
- `insertOptions`: Опции вставки

### `InsertFragment(TFlex.Model.Model2D.Fragment)`

ID: `M:TFlex.Model.Model2D.RichText.InsertFragment(TFlex.Model.Model2D.Fragment)`

Вставка фрагмента

Parameters:
- `obj`: Фрагмент

### `InsertHyperlink(TFlex.Model.Model2D.HyperlinkProperties)`

ID: `M:TFlex.Model.Model2D.RichText.InsertHyperlink(TFlex.Model.Model2D.HyperlinkProperties)`

Вставка гиперссылки

Parameters:
- `properties`: Параметры гиперссылки

### `InsertImage`

ID: `M:TFlex.Model.Model2D.RichText.InsertImage`

Вставка изображения с указанием ссылки

Returns: Добавленное изображение

### `InsertImage(TFlex.Model.FileLink)`

ID: `M:TFlex.Model.Model2D.RichText.InsertImage(TFlex.Model.FileLink)`

Вставка изображения с указанием ссылки

Parameters:
- `link`: Используемая ссылка

### `InsertImage(TFlex.Model.FileLink,TFlex.Model.Model2D.RichText.InsertObjectOptions)`

ID: `M:TFlex.Model.Model2D.RichText.InsertImage(TFlex.Model.FileLink,TFlex.Model.Model2D.RichText.InsertObjectOptions)`

Вставка изображения с указанием ссылки

Parameters:
- `link`: Используемая ссылка
- `insertOptions`: Опции вставки

### `InsertIndex(System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RichText.InsertIndex(System.String,System.String)`

Вставка индексов

Parameters:
- `upper`: Строка в верхнем индексе (может отсутствовать)
- `lower`: Строка в нижнем индексе (может отсутствовать)

Remarks: При создании индекса используется значение масштаба шрифта, указанное в свойстве `P:TFlex.Model.Model2D.RichText.CurrIndexScale`

### `InsertParagraph`

ID: `M:TFlex.Model.Model2D.RichText.InsertParagraph`

Вставка абзаца

Remarks: Абзац будет вставлен перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertParagraph(TFlex.Model.Model2D.CharFormat)`

ID: `M:TFlex.Model.Model2D.RichText.InsertParagraph(TFlex.Model.Model2D.CharFormat)`

Вставка абзаца с использованием заданного формата символов

Parameters:
- `format`: Формат разделителя

Remarks: Абзац будет вставлен перед символом, на котором находится курсор Параметры выделения фрагмента будут потеряны

### `InsertParagraphs(System.UInt32)`

ID: `M:TFlex.Model.Model2D.RichText.InsertParagraphs(System.UInt32)`

Вставка нескольких абзацев с использованием для разделителя формата символов по умолчанию для разделителя

Parameters:
- `count`: Количество абзацев

Remarks: Абзацы будет вставлены перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertParagraphs(System.UInt32,TFlex.Model.Model2D.CharFormat)`

ID: `M:TFlex.Model.Model2D.RichText.InsertParagraphs(System.UInt32,TFlex.Model.Model2D.CharFormat)`

Вставка нескольких абзацев с использованием для разделителя заданного формата символов

Parameters:
- `count`: Количество абзацев
- `format`: Формат разделителя

Remarks: Абзацы будет вставлены перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertRoughnessSymbol(TFlex.Model.Model2D.RoughnessSymbol)`

ID: `M:TFlex.Model.Model2D.RichText.InsertRoughnessSymbol(TFlex.Model.Model2D.RoughnessSymbol)`

Вставка обозначения шероховатости

Parameters:
- `obj`: Обозначение шероховатости

### `InsertSymbol(System.UInt32,System.Boolean)`

ID: `M:TFlex.Model.Model2D.RichText.InsertSymbol(System.UInt32,System.Boolean)`

Вставка символа с заданным кодом

Parameters:
- `code`: Код символа
- `fIgnoreFontAngularity`: Игнорировать наклон шрифта

### `InsertText(System.String)`

ID: `M:TFlex.Model.Model2D.RichText.InsertText(System.String)`

Вставка текста с использованием формата символов по умолчанию

Parameters:
- `rtfText`: Текст

Remarks: Текст будет вставлен перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertText(System.String,TFlex.Model.Model2D.CharFormat)`

ID: `M:TFlex.Model.Model2D.RichText.InsertText(System.String,TFlex.Model.Model2D.CharFormat)`

Вставка текста с использованием заданного формата символов

Parameters:
- `text`: Текст
- `format`: Формат символов

Remarks: Текст будет вставлен перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertText(System.String,TFlex.Model.Model2D.CharFormat,TFlex.Model.Model2D.ParaFormat)`

ID: `M:TFlex.Model.Model2D.RichText.InsertText(System.String,TFlex.Model.Model2D.CharFormat,TFlex.Model.Model2D.ParaFormat)`

Вставка текста с использованием заданного формата символов

Parameters:
- `text`: Текст
- `charFormat`: Формат символов
- `paraFormat`: Формат абзаца

Remarks: Текст будет вставлен перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `InsertVariable(TFlex.Model.Variable,TFlex.Model.VariableProperties)`

ID: `M:TFlex.Model.Model2D.RichText.InsertVariable(TFlex.Model.Variable,TFlex.Model.VariableProperties)`

Вставка переменной

Parameters:
- `pObj`: Переменная
- `varProps`: Параметры вставки переменной

### `InsetRtfText(System.String)`

ID: `M:TFlex.Model.Model2D.RichText.InsetRtfText(System.String)`

Вставка текста в формате RTF

Parameters:
- `text`: RTF текст

Remarks: Текст будет вставлен перед символом, на котором находится курсор. Параметры выделения фрагмента будут потеряны

### `MoveCursor(System.Int32)`

ID: `M:TFlex.Model.Model2D.RichText.MoveCursor(System.Int32)`

Перемещение курсора на несколько символов вперёд или назад

Parameters:
- `charactersCount`: Количество символов

Remarks: Если значение параметра charactersCount больше 0, то курсор будет перемещён вперёд на charactersCount символов. Если значение параметра charactersCount меньше 0, то курсор будет перемещён на абсолютное значение charactersCount символов

### `PasteFromClipboard`

ID: `M:TFlex.Model.Model2D.RichText.PasteFromClipboard`

Вставить текст из буфера обмена

### `ReplaceAbsentFontNames(System.String)`

ID: `M:TFlex.Model.Model2D.RichText.ReplaceAbsentFontNames(System.String)`

Заменяем отсутствующие в системе шрифты во всех элементах текста.

Parameters:
- `newName`: Новое имя шрифта

### `ReplaceFontName(System.String,System.String)`

ID: `M:TFlex.Model.Model2D.RichText.ReplaceFontName(System.String,System.String)`

Заменяем выбранный шрифт во всех элементах текста.

Parameters:
- `oldName`: Старое имя шрифта для замены
- `newName`: Новое имя шрифта

### `SelectAll`

ID: `M:TFlex.Model.Model2D.RichText.SelectAll`

Выделение всего текста

### `SetCursor(TFlex.Model.Model2D.PositionProperties)`

ID: `M:TFlex.Model.Model2D.RichText.SetCursor(TFlex.Model.Model2D.PositionProperties)`

Установка положения курсора в тексте

Parameters:
- `position`: Положения курсора в тексте

Remarks: Функция устанавливает курсор в начало (конец) текста

### `SetCursor(TFlex.Model.Model2D.PositionProperties,TFlex.Model.Model2D.Position.TablePosition)`

ID: `M:TFlex.Model.Model2D.RichText.SetCursor(TFlex.Model.Model2D.PositionProperties,TFlex.Model.Model2D.Position.TablePosition)`

Установка положения курсора в ячейке таблицы

Parameters:
- `position`: Положение курсора в ячейке таблицы
- `table`: Положение ячейки

Remarks: Функция устанавливает курсор в начало(конец) ячейки таблицы

### `SetDefaultFont(System.String,System.Double,System.UInt32,System.Boolean)`

ID: `M:TFlex.Model.Model2D.RichText.SetDefaultFont(System.String,System.Double,System.UInt32,System.Boolean)`

Установка шрифта, используемого по умолчанию

Parameters:
- `name`: Имя шрифта
- `size`: Размер символов
- `color`: Цвет символов
- `defaultItalic`: Курсив по умолчанию

### `SetDefaultFont(System.String,System.Double,System.UInt32,System.Boolean,System.Boolean)`

ID: `M:TFlex.Model.Model2D.RichText.SetDefaultFont(System.String,System.Double,System.UInt32,System.Boolean,System.Boolean)`

Установка шрифта, используемого по умолчанию

Parameters:
- `name`: Имя шрифта
- `size`: Размер символов
- `color`: Цвет символов
- `defaultItalic`: Курсив по умолчанию
- `defaultBold`: Полужирный по умолчанию

### `SetSelection(TFlex.Model.Model2D.Position)`

ID: `M:TFlex.Model.Model2D.RichText.SetSelection(TFlex.Model.Model2D.Position)`

Установка выделения фрагмента, находящегося между курсором и заданной позицией

Parameters:
- `position`: Один из краёв выделяемого фрагмента

Remarks: Курсор устанавливается в конец выделяемого фрагмента

### `SetSelection(TFlex.Model.Model2D.Position,TFlex.Model.Model2D.Position)`

ID: `M:TFlex.Model.Model2D.RichText.SetSelection(TFlex.Model.Model2D.Position,TFlex.Model.Model2D.Position)`

Установка выделения фрагмента текста

Parameters:
- `pos1`: Начало выделяемого фрагмента
- `pos2`: Конец выделяемого фрагмента

Remarks: Курсор устанавливается в конец выделяемого фрагмента

### `TrySetTableOnly(System.Boolean)`

ID: `M:TFlex.Model.Model2D.RichText.TrySetTableOnly(System.Boolean)`

Попробовать выставить свойство TableOnly

Parameters:
- `tableOnly`: Таблица

Remarks: Возвращает true в случае успеха

## Propertys

### `AutoUpdate`

ID: `P:TFlex.Model.Model2D.RichText.AutoUpdate`

Автоматический пересчёт текста при открытом блоке изменения текста

### `CharacterFormat`

ID: `P:TFlex.Model.Model2D.RichText.CharacterFormat`

Формат одного символа, на котором находится курсор, или символов, находящихся в выделенном фрагменте, в зависимости от состояния выделения

### `CurrFractionScale`

ID: `P:TFlex.Model.Model2D.RichText.CurrFractionScale`

Текущий масштаб высоты шрифта для дробей, используется при вставке новых дробей

### `CurrIndexScale`

ID: `P:TFlex.Model.Model2D.RichText.CurrIndexScale`

Текущий масштаб высоты шрифта для индексов, используется при вставке новых индексов

### `CursorPosition`

ID: `P:TFlex.Model.Model2D.RichText.CursorPosition`

Положение курсора в тексте

### `DefaultCharacterFormat`

ID: `P:TFlex.Model.Model2D.RichText.DefaultCharacterFormat`

Формат символов, используемый по умолчанию

### `DefaultNumberFormat`

ID: `P:TFlex.Model.Model2D.RichText.DefaultNumberFormat`

Формат символов нумерации, используемый по умолчанию

### `DefaultParagraphFormat`

ID: `P:TFlex.Model.Model2D.RichText.DefaultParagraphFormat`

Формат абзацев, используемый по умолчанию

### `ParagraphFormat`

ID: `P:TFlex.Model.Model2D.RichText.ParagraphFormat`

Формат одного символа, на котором находится курсор, или символов, находящихся в выделенном фрагменте, в зависимости от состояния выделения

### `ProductStructureFile`

ID: `P:TFlex.Model.Model2D.RichText.ProductStructureFile`

Ссылка на документ состава изделия по которому создан текст, если текст является отчетом состава изделия

### `ProductStructureId`

ID: `P:TFlex.Model.Model2D.RichText.ProductStructureId`

ID состава изделия по которому создан текст, если текст является отчетом состава изделия

### `ReportPrototypeFile`

ID: `P:TFlex.Model.Model2D.RichText.ReportPrototypeFile`

Ссылка на документ прототип отчета, если текст является отчетом состава изделия

### `ShowVariableNames`

ID: `P:TFlex.Model.Model2D.RichText.ShowVariableNames`

Показать имена переменных

### `TableOnly`

ID: `P:TFlex.Model.Model2D.RichText.TableOnly`

Запретить ввод текста вне таблицы

### `TextLength`

ID: `P:TFlex.Model.Model2D.RichText.TextLength`

Получение длины всего текста с начала до конца без учёта таблиц

### `TextValue`

ID: `P:TFlex.Model.Model2D.RichText.TextValue`

Получение текста, находящегося в заданном отрезке

Returns: Текст документа
