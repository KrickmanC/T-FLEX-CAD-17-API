# TFlex.Command.PluginCommand

Assembly: `TFlexAPI`
Namespace: `TFlex.Command`

## Summary

Реализация функциональности команды приложения

## Remarks

При получении сообщения через функцию `!:TFlex::Plugin::OnCommand(TFlex.Model.Document, System.UInt32)` приложение конструирует объект данного класса и запускает его на выполнение при помощи функции `Run` . После этого до завершения данной команды или запуска другой команды сообщения Windows транслируются в вызовы функция данного класса.

## Constructors

### `PluginCommand(TFlex.Plugin)`

ID: `M:TFlex.Command.PluginCommand.#ctor(TFlex.Plugin)`

Конструктор команды

Parameters:
- `OwnerPlugin`: Объект приложения в котором произошел вызов команды

## Methods

### `PluginCommand(TFlex.Plugin)`

ID: `M:TFlex.Command.PluginCommand.#ctor(TFlex.Plugin)`

Конструктор команды

Parameters:
- `OwnerPlugin`: Объект приложения в котором произошел вызов команды

### `Dispose`

ID: `M:TFlex.Command.PluginCommand.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `OnContinue(TFlex.Command.ContinueEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnContinue(TFlex.Command.ContinueEventArgs)`

Обработчик завершения выполнения вложенной команды

Parameters:
- `e`: Аргументы события

Remarks: Данную функцию необходимо переопределить для того, чтобы получить управление при завершении вложенной команды и код её завершения

### `OnExit(TFlex.Command.ExitEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnExit(TFlex.Command.ExitEventArgs)`

Обработчик выхода из команды

Parameters:
- `e`: Аргументы события

Remarks: Данную функцию необходимо переопределить для того, чтобы получить управление в момент завершения выполнения команды. Это сообщение приходит последним в процессе выполнения команды

### `OnInitialize(TFlex.Command.InitializeEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnInitialize(TFlex.Command.InitializeEventArgs)`

Обработчик инициализации команды

Parameters:
- `e`: Аргументы события

### `OnKeyPressed(TFlex.Command.KeyEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnKeyPressed(TFlex.Command.KeyEventArgs)`

Обработчик нажатия клавиши на клавиатуре или кнопки автоменю

Parameters:
- `e`: Аргументы события

### `OnMouseMove(TFlex.Command.MouseEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnMouseMove(TFlex.Command.MouseEventArgs)`

Обработчик перемещения курсора мыши

Parameters:
- `e`: Аргументы события

### `OnSelect(TFlex.Command.SelectEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnSelect(TFlex.Command.SelectEventArgs)`

Фильтр выбираемых объектов

Parameters:
- `e`: Аргументы события

Remarks: В обработчике этого события надо отбрасывать неподходящие объекты

### `OnShowCursor(TFlex.Command.MouseEventArgs)`

ID: `M:TFlex.Command.PluginCommand.OnShowCursor(TFlex.Command.MouseEventArgs)`

Динамическая отрисовка курсора

Parameters:
- `e`: Аргументы события

Remarks: Данная функция вызывается в тот момент, когда требуется прорисовка динамического курсора при перемещении мыши

### `PassSelected`

ID: `M:TFlex.Command.PluginCommand.PassSelected`

Передать ранее выбранный с помощью метода `M:TFlex.Command.PluginCommand.SelectByEvent(TFlex.Command.CursorEventArgs,System.Boolean)` объект системе.

Remarks: Вызов данного метода имитирует выбор объекта в режиме ожидания.

### `ResetSelectedObject`

ID: `M:TFlex.Command.PluginCommand.ResetSelectedObject`

Отменить выбор последнего объекта

### `Run(TFlex.Model.View)`

ID: `M:TFlex.Command.PluginCommand.Run(TFlex.Model.View)`

Запустить команду на выполнение

### `Run(TFlex.Model.View,System.Boolean)`

ID: `M:TFlex.Command.PluginCommand.Run(TFlex.Model.View,System.Boolean)`

Запустить команду на выполнение

Parameters:
- `subCommand`: Указание, должна ли текущая команда быть остановлена (false; старое поведение) перед запуском этой или нет (true)

### `SelectByEvent(TFlex.Command.CursorEventArgs,System.Boolean)`

ID: `M:TFlex.Command.PluginCommand.SelectByEvent(TFlex.Command.CursorEventArgs,System.Boolean)`

Функция выбора объекта

Parameters:
- `ev`: Аргументы события, возникающие при манипуляциях с курсором
- `mark`: Подсвечивать выбираемые объекты

Remarks: Этим методом можно пользоваться в обработчике щелчка мыши или нажатия на Enter. Изнутри метода вызывается обработчик Select, выбранный объект помещается в контейнер (см. `T:TFlex.Model.SelectionContainer` ).

### `Terminate`

ID: `M:TFlex.Command.PluginCommand.Terminate`

Завершить выполнение команды

## Propertys

### `Automenu`

ID: `P:TFlex.Command.PluginCommand.Automenu`

Автоменю команды

### `DisplayNameForError`

ID: `P:TFlex.Command.PluginCommand.DisplayNameForError`

Название команды для отображения в сообщениях об ошибке

### `ID`

ID: `P:TFlex.Command.PluginCommand.ID`

Возвращает зарегестрированный идентификатор команды

### `IsTransparentChangesEnabled`

ID: `P:TFlex.Command.PluginCommand.IsTransparentChangesEnabled`

Разрешает блоку отмены действий оставаться открытым между событиями команды

### `Owner`

ID: `P:TFlex.Command.PluginCommand.Owner`

Получить приложение команды

### `PropertiesWindow`

ID: `P:TFlex.Command.PluginCommand.PropertiesWindow`

Окно свойств команды

### `SupportedBehavior`

ID: `P:TFlex.Command.PluginCommand.SupportedBehavior`

Поддерживаемое командой поведение

## Events

### `Continue`

ID: `E:TFlex.Command.PluginCommand.Continue`

Событие завершения выполнения вложенной команды

Remarks: Данное событие необходимо реализовать для того, чтобы получить управление при завершении вложенной команды и код её завершения

### `Exit`

ID: `E:TFlex.Command.PluginCommand.Exit`

Событие завершения выполнения команды

Remarks: Данное событие необходимо реализовать для того, чтобы получить управление в момент завершения выполнения команды. Это сообщение приходит последним в процессе выполнения команды

### `Initialize`

ID: `E:TFlex.Command.PluginCommand.Initialize`

Событие инициализации команды

### `KeyPressed`

ID: `E:TFlex.Command.PluginCommand.KeyPressed`

Событие, возникающее при нажатии клавиши клавиатуры или кнопки автоменю

### `MouseMove`

ID: `E:TFlex.Command.PluginCommand.MouseMove`

Событие, возникающее при перемещении курсора

### `Select`

ID: `E:TFlex.Command.PluginCommand.Select`

Событие, возникающее при выборе объекта

Remarks: В обработчике этого события надо отбрасывать неподходящие объекты

### `ShowCursor`

ID: `E:TFlex.Command.PluginCommand.ShowCursor`

Событие, возникающее при прорисовке динамического курсора при перемещении мыши

Remarks: Данное событие необходимо реализовать в тот момент, когда требуется прорисовка динамического курсора при перемещении мыши
