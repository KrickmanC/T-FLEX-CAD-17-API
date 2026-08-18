# TFlex.Application

Assembly: `TFlexAPI`
Namespace: `TFlex`

## Summary

Объект данного класса обеспечивает доступ к объектам T-FLEX CAD

## Remarks

К таким объектам относятся документы, команды, главное окно приложения и прочее.

## Methods

### `#cctor`

ID: `M:TFlex.Application.#cctor`

Конструктор

### `AddDocumentsSearchFolder(System.String)`

ID: `M:TFlex.Application.AddDocumentsSearchFolder(System.String)`

Назначить папку для поиска указанного типа файлов, если при работе с системой она не была задана явно

Parameters:
- `folder`: Папка для поиска

### `AddMacrosIndirectAssembly(System.String)`

ID: `M:TFlex.Application.AddMacrosIndirectAssembly(System.String)`

Добавить ссылку на сборку в макрос

Parameters:
- `assemblyPath`: Путь к файлу сборки

### `AddResourceFile(System.String)`

ID: `M:TFlex.Application.AddResourceFile(System.String)`

Загружает строковые ресурсы из указанного файла в формате Microsoft ResX для использования в неуправляемом коде

### `AddResourceFile(System.String,System.String)`

ID: `M:TFlex.Application.AddResourceFile(System.String,System.String)`

Загружает строковые ресурсы из указанного файла в формате Microsoft ResX для использования в неуправляемом коде

Parameters:
- `directory`: Путь к директории, содержащей файл ресурсов, или 'null', если файл расположен в директории T-FLEX CAD

Remarks: Данные загружаются из файла "<directory>\<baseName>.<language>.resx", где "<language>" -- двухбуквенное обозначение языка T-FLEX CAD (например, "en" для английской версии, "de" для немецкой и т.п.). Если файл с таким именем отсутствует, то часть имени файла с обозначением языка отбрасывается и попытка загрузки повторяется для файла "<directory>\<baseName>.resx".

### `CallPluginRestService(System.String,TFlex.Rest.Request)`

ID: `M:TFlex.Application.CallPluginRestService(System.String,TFlex.Rest.Request)`

Вызвать RESTful сервис плагина. Формат входных/выходных данных зависит от конкретного плагина.

### `CreateAnnotation(System.String,TFlex.Annotation)`

ID: `M:TFlex.Application.CreateAnnotation(System.String,TFlex.Annotation)`

Создать новую аннотацию для указанного файла документа

Parameters:
- `documentFileName`: Путь к файлу аннотируемого документа
- `annotation`: Параметры создаваемой аннотации с указанием пути к файлу

Returns: `true` в случае успешного создания аннотации, иначе `false`

### `DoEvents`

ID: `M:TFlex.Application.DoEvents`

Обрабатывает все сообщения Windows, которые в данный момент находятся в очереди сообщений.

Remarks: Метод позволяет приложению обрабатывать другие события, которые могут возникнуть при выполнии кода

### `EnableDOCs`

ID: `M:TFlex.Application.EnableDOCs`

Разрешить интеграцию с T-FLEX DOCs

### `EnableNotRespondingDialog(System.Boolean)`

ID: `M:TFlex.Application.EnableNotRespondingDialog(System.Boolean)`

Для внутреннего использования

### `ExitSession`

ID: `M:TFlex.Application.ExitSession`

Завершить работу c API

Remarks: Вызывается при необходимости завершения работы с API в активном приложении. При завершении работы приложения вызывается автоматически. Вызывается в паре с методом `M:TFlex.Application.InitSession(TFlex.ApplicationSessionSetup)`

### `FindLibraryName(System.String)`

ID: `M:TFlex.Application.FindLibraryName(System.String)`

Поиск библиотечного пути

### `FindPathName(System.String)`

ID: `M:TFlex.Application.FindPathName(System.String)`

Полный путь к файлу

### `FindPathName(System.String,System.String)`

ID: `M:TFlex.Application.FindPathName(System.String,System.String)`

Полный путь к файлу

### `ForceCulture`

ID: `M:TFlex.Application.ForceCulture`

Принудительно выставить локализацию текущему потому. Использовать в using-e.

### `GetCustomLicenseStatus(System.UInt32)`

ID: `M:TFlex.Application.GetCustomLicenseStatus(System.UInt32)`

Получить статус лицензии пользователя

Parameters:
- `license`: Номер лицензии

### `GetDocumentExternalFileLinks(System.String,System.Boolean,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.GetDocumentExternalFileLinks(System.String,System.Boolean,System.Boolean,System.Boolean)`

Возвращает все имеющиеся в модели ссылки на внешние файлы

Parameters:
- `fileName`: Имя файла документа
- `includeModelFilesOnly`: 
- `includeLibraryLinks`: 
- `recursive`: 

### `GetDocumentIcon(System.String)`

ID: `M:TFlex.Application.GetDocumentIcon(System.String)`

Возвращает иконку документа, если она есть

Parameters:
- `fileName`: Имя файла документа

### `GetDocumentIcon(System.String,System.Int32)`

ID: `M:TFlex.Application.GetDocumentIcon(System.String,System.Int32)`

Возвращает иконку документа с указанным размером, если она есть

Parameters:
- `fileName`: Имя файла документа
- `iconSize`: Размер иконки

### `GetShortPathName(System.String,System.String)`

ID: `M:TFlex.Application.GetShortPathName(System.String,System.String)`

Получение короткого пути относительно папки

### `GetSystemFilePath(System.String,System.Boolean)`

ID: `M:TFlex.Application.GetSystemFilePath(System.String,System.Boolean)`

Полный путь к системному файлу

Parameters:
- `strFileName`: Document
- `bReadOnly`: 

### `GetSystemProfileFilePath(System.String,System.String,System.Boolean)`

ID: `M:TFlex.Application.GetSystemProfileFilePath(System.String,System.String,System.Boolean)`

Полный путь к системному файлу

Parameters:
- `fileName`: Document
- `profileItemName`: Имя элемента окружения
- `bReadOnly`: Только на чтение. Файл не будет копироваться во временную папку, если его там еще нет.

Remarks: Для внутреннего использования

### `HideEmbeddedHelp`

ID: `M:TFlex.Application.HideEmbeddedHelp`

Убрать раздел справочного руководства

### `IdleSession`

ID: `M:TFlex.Application.IdleSession`

Для внутреннего использования

### `InitSession(TFlex.ApplicationSessionSetup)`

ID: `M:TFlex.Application.InitSession(TFlex.ApplicationSessionSetup)`

Инициализация API

Parameters:
- `setup`: Параметры инициализации сессии

Returns: true в случае успешного завершения

Remarks: Данный метод необходимо вызвать при инициализации API в случае использования его в отдельном приложении (EXE). При необходимости завершения работы с API до закрытия приложения нужно вызывать метод `M:TFlex.Application.ExitSession`

### `InitializeCustomLicense(System.UInt32)`

ID: `M:TFlex.Application.InitializeCustomLicense(System.UInt32)`

Активировать лицензию пользователя

Parameters:
- `license`: Номер лицензии

### `LockUpdateUI(TFlex.Model.Document)`

ID: `M:TFlex.Application.LockUpdateUI(TFlex.Model.Document)`

Создать блокировщик обновления интерфейса

Remarks: Для использования в using-инструкциях. При вызове Dispose обновляется интерфейс.

### `NewAnnotation(System.String,TFlex.Annotation)`

ID: `M:TFlex.Application.NewAnnotation(System.String,TFlex.Annotation)`

Создать новую аннотацию для указанного файла документа

Parameters:
- `documentFileName`: Путь к файлу аннотируемого документа
- `annotation`: Параметры создаваемой аннотации с указанием пути к файлу

Returns: Созданный документ аннотации или `null` в случае ошибки

### `NewDocument`

ID: `M:TFlex.Application.NewDocument`

Создать новый документ

Returns: Созданный документ или null в случае ошибки

### `NewDocument(System.Boolean)`

ID: `M:TFlex.Application.NewDocument(System.Boolean)`

Создать новый документ

Parameters:
- `b3D`: В случае, если параметр равен true, новый документ создаётся на основе 3D прототипа

Returns: Созданный документ или null в случае ошибки

### `NewDocument(System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.NewDocument(System.Boolean,System.Boolean)`

Создать новый документ

Parameters:
- `b3D`: В случае, если параметр равен true, новый документ создаётся на основе 3D прототипа
- `visible`: Указывает, должен ли новый документ быть видимым

Returns: Созданный документ или null в случае ошибки

### `NewDocument(System.String)`

ID: `M:TFlex.Application.NewDocument(System.String)`

Создать новый документ на основе указанного файла прототипа

Parameters:
- `prototype`: Путь к файлу прототипа

Returns: Созданный документ или null в случае ошибки

### `NewDocument(System.String,System.Boolean)`

ID: `M:TFlex.Application.NewDocument(System.String,System.Boolean)`

Создать новый документ на основе указанного файла прототипа

Parameters:
- `prototype`: Путь к файлу прототипа
- `visible`: Указывает, должен ли новый документ быть видимым

Returns: Созданный документ или null в случае ошибки

### `OpenAsDocument(System.String)`

ID: `M:TFlex.Application.OpenAsDocument(System.String)`

Открыть документ или импортировать файл

Parameters:
- `fileName`: Имя файла

Returns: Открытый документ или null в случае ошибки

### `OpenAsDocument(System.String,System.Boolean)`

ID: `M:TFlex.Application.OpenAsDocument(System.String,System.Boolean)`

Открыть документ или импортировать файл

Parameters:
- `fileName`: Имя файла
- `visible`: Указывает, должен ли открытый документ быть видимым

Returns: Открытый документ или null в случае ошибки

### `OpenAsDocument(System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenAsDocument(System.String,System.Boolean,System.Boolean)`

Открыть документ или импортировать файл

Parameters:
- `fileName`: Имя файла
- `visible`: Указывает, должен ли открытый документ быть видимым
- `readOnly`: Открыть документ только для чтения

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(System.String)`

ID: `M:TFlex.Application.OpenDocument(System.String)`

Открыть документ

Parameters:
- `fileName`: Имя файла документа

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(System.String,System.Boolean)`

ID: `M:TFlex.Application.OpenDocument(System.String,System.Boolean)`

Открыть документ

Parameters:
- `fileName`: Имя файла документа
- `visible`: Указывает, должен ли открытый документ быть видимым

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenDocument(System.String,System.Boolean,System.Boolean)`

Открыть документ

Parameters:
- `fileName`: Имя файла документа
- `visible`: Указывает, должен ли открытый документ быть видимым
- `readOnly`: Открыть документ только для чтения

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(System.String,TFlex.OpenDocumentOptions)`

ID: `M:TFlex.Application.OpenDocument(System.String,TFlex.OpenDocumentOptions)`

Открыть документ

Parameters:
- `fileName`: Имя файла
- `options`: Параметры открытия файла

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(TFlex.Model.FileLink)`

ID: `M:TFlex.Application.OpenDocument(TFlex.Model.FileLink)`

Открыть документ

Parameters:
- `link`: Ссылка на файл документа

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(TFlex.Model.FileLink,System.Boolean)`

ID: `M:TFlex.Application.OpenDocument(TFlex.Model.FileLink,System.Boolean)`

Открыть документ

Parameters:
- `link`: Ссылка на файл документа
- `visible`: Указывает, должен ли открытый документ быть видимым

Returns: Открытый документ или null в случае ошибки

### `OpenDocument(TFlex.Model.FileLink,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenDocument(TFlex.Model.FileLink,System.Boolean,System.Boolean)`

Открыть документ

Parameters:
- `link`: Ссылка на файл документа
- `visible`: Указывает, должен ли открытый документ быть видимым
- `readOnly`: Открыть документ только для чтения

Returns: Открытый документ или null в случае ошибки

### `OpenDocumentFromDOCs(System.Int32,System.Boolean)`

ID: `M:TFlex.Application.OpenDocumentFromDOCs(System.Int32,System.Boolean)`

T-FLEX DOCs 11 больше не поддерживается

### `OpenDocumentFromDOCs(System.Int32,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenDocumentFromDOCs(System.Int32,System.Boolean,System.Boolean)`

T-FLEX DOCs 11 больше не поддерживается

### `OpenFileDialog(System.String,System.String)`

ID: `M:TFlex.Application.OpenFileDialog(System.String,System.String)`

Диалог выбора файла из папки или библиотеки

Parameters:
- `type`: 
- `title`: 

### `OpenFragmentDocument(System.String)`

ID: `M:TFlex.Application.OpenFragmentDocument(System.String)`

Открыть документ фрагмента для чтения

Parameters:
- `fileName`: Имя файла документа

Returns: Открытый документ или null в случае ошибки

### `OpenFragmentDocument(System.String,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenFragmentDocument(System.String,System.Boolean,System.Boolean)`

Открыть документ фрагмента для чтения

Parameters:
- `fileName`: Имя файла документа
- `with3D`: 
- `recalculate`: 

Returns: Открытый документ или null в случае ошибки

### `OpenFragmentDocument(TFlex.Model.FileLink)`

ID: `M:TFlex.Application.OpenFragmentDocument(TFlex.Model.FileLink)`

Открыть документ фрагмента для чтения

Parameters:
- `link`: Ссылка на файл документа

Returns: Открытый документ или null в случае ошибки

### `OpenFragmentDocument(TFlex.Model.FileLink,System.Boolean,System.Boolean)`

ID: `M:TFlex.Application.OpenFragmentDocument(TFlex.Model.FileLink,System.Boolean,System.Boolean)`

Открыть документ фрагмента для чтения

Parameters:
- `link`: Ссылка на файл документа
- `with3D`: 
- `recalculate`: 

Returns: Открытый документ или null в случае ошибки

### `PickPoint(TFlex.Model.Document,TFlex.PickPointParameters)`

ID: `M:TFlex.Application.PickPoint(TFlex.Model.Document,TFlex.PickPointParameters)`

Получить точку в одном из видов документа

Parameters:
- `document`: Документ
- `parameters`: Параметры ввода точки

Returns: Результат ввода точки

### `PickPoint(TFlex.PickPointParameters)`

ID: `M:TFlex.Application.PickPoint(TFlex.PickPointParameters)`

Получить точку в одном из видов активного документа

Parameters:
- `parameters`: Параметры ввода точки

Returns: Результат ввода точки

Examples:
- `using System; using System.Windows.Forms; using TFlex; using TFlex.Model; using TFlex.Model.Model2D; using TFlex.Model.Model3D; namespace NewMacroNamespace { public class NewMacroClass { public static void PickPoint() { PickPointParameters par = new PickPointParameters(); //выбор только размеров SelectionFilter filter = new SelectionFilter(); filter.Enable(ObjectType.Dimension); par.Filter = filter; par.Prompt = "Выбрать размер"; par.MouseMove += new TFlex.PickPointMouseMove(PickPointMouseMove);//событие перемещения мыши PickPointResult res = TFlex.Application.PickPoint(par);//получить точку в одном из видов активного документа string mess = "Объект не выбран"; if (res.SelectedObject != null) { mess = string.Empty; string val = string.Empty; ObjectProperty[] arr = res.SelectedObject.GetProperties();//массив свойств выбранного объекта for (int i = 0; i < arr.Length; i++) { switch (arr[i].Type) { case (ObjectPropertyType.IntProperty): val = res.SelectedObject.GetIntProperty(arr[i].Name).Value.ToString(); break; case (ObjectPropertyType.RealProperty): val = res.SelectedObject.GetRealProperty(arr[i].Name).Value.ToString(); break; case (ObjectPropertyType.TextProperty): val = res.SelectedObject.GetTextProperty(arr[i].Name); break; } mess += arr[i].Name + ": " + val + "\r\n"; } } MessageBox.Show(mess); } static public void PickPointMouseMove(Object sender, PickPointEventArgs e) { } } }`

### `RunSystemCommand(System.String,TFlex.Model.ModelObject[],TFlex.SystemCommandFinishedCallback)`

ID: `M:TFlex.Application.RunSystemCommand(System.String,TFlex.Model.ModelObject[],TFlex.SystemCommandFinishedCallback)`

Выполнить команду с ожиданием её завершения

Remarks: Название команды в T-FLEX Open API отображается во всплывающей подсказке к кнопке команды в интерфейсе T-FLEX CAD. Для включения её отображения во всплывающей подсказке к кнопке команды необходимо в T-FLEX CAD включить опцию "Включить в подсказки имена команд в Open API".

### `ShowEmbeddedHelpTopic(System.String)`

ID: `M:TFlex.Application.ShowEmbeddedHelpTopic(System.String)`

Показать раздел справочного руководства

Parameters:
- `url`: Адрес страницы справочного руководства

### `ShowHelp`

ID: `M:TFlex.Application.ShowHelp`

Показать справочное руководство

### `TerminateAllCommands`

ID: `M:TFlex.Application.TerminateAllCommands`

Завершить все активные комманды

### `WaitForSystemCommandFinished(System.String,TFlex.SystemCommandFinishedCallback)`

ID: `M:TFlex.Application.WaitForSystemCommandFinished(System.String,TFlex.SystemCommandFinishedCallback)`

Ожидание завершения команды

## Propertys

### `ActiveDocument`

ID: `P:TFlex.Application.ActiveDocument`

Текущий (активный) документ системы

### `ActiveMainWindow`

ID: `P:TFlex.Application.ActiveMainWindow`

Активное главное окно системы

### `ActiveViewDocument`

ID: `P:TFlex.Application.ActiveViewDocument`

Текущий (активный) документ активного вида

### `BOMSectionsDatabase`

ID: `P:TFlex.Application.BOMSectionsDatabase`

Путь к файлу базы данных, в котором храниться структура разделов спецификации

### `Culture`

ID: `P:TFlex.Application.Culture`

Параметры локализации приложения

### `DisableSubstituteFontDialog`

ID: `P:TFlex.Application.DisableSubstituteFontDialog`

Блокировать диалог замены ненайденного шрифта

Remarks: Когда блокировка больше не требуется, необходимо вернуть предыдущее состояние

### `Documents`

ID: `P:TFlex.Application.Documents`

Перечислитель открытых в T-FLEX CAD документов

### `EvaluationVersion`

ID: `P:TFlex.Application.EvaluationVersion`

Свойство, возвращающее true, если версия T-FLEX CAD ознакомительная

### `FileLinksAutoRefresh`

ID: `P:TFlex.Application.FileLinksAutoRefresh`

Режим обновления файловых ссылок

Remarks: Работает только в режиме пользовательского приложения. См. метод `M:TFlex.Application.InitSession(TFlex.ApplicationSessionSetup)`

### `InterfaceLanguage`

ID: `P:TFlex.Application.InterfaceLanguage`

Язык интерфейса T-FLEX CAD

### `IsDOCsEnabled`

ID: `P:TFlex.Application.IsDOCsEnabled`

Включена ли интеграция с T-FLEX DOCs

### `IsMacrosEnabled`

ID: `P:TFlex.Application.IsMacrosEnabled`

Разрешить выполнение макросов

### `IsSessionInitialized`

ID: `P:TFlex.Application.IsSessionInitialized`

Состояние инициализации API

### `LibraryConfigurations`

ID: `P:TFlex.Application.LibraryConfigurations`

Открытые конфигурации библиотек

### `MeasuringSystem`

ID: `P:TFlex.Application.MeasuringSystem`

Система измерения T-FLEX CAD

### `Options`

ID: `P:TFlex.Application.Options`

Установки приложения

### `Product`

ID: `P:TFlex.Application.Product`

Конфигурация T-FLEX CAD

### `RegistryName`

ID: `P:TFlex.Application.RegistryName`

Путь в реестре для настроек пользователя

### `Settings`

ID: `P:TFlex.Application.Settings`

Установки приложения

### `Strings`

ID: `P:TFlex.Application.Strings`

Доступ к строкам локализации приложения

### `StudentVersion`

ID: `P:TFlex.Application.StudentVersion`

Свойство, возвращающее true, если версия T-FLEX CAD учебная

### `SystemPath`

ID: `P:TFlex.Application.SystemPath`

Полный системный путь

### `Units`

ID: `P:TFlex.Application.Units`

Единицы измерения приложения

### `Version`

ID: `P:TFlex.Application.Version`

Версия T-FLEX CAD

### `Window`

ID: `P:TFlex.Application.Window`

Главное окно системы
