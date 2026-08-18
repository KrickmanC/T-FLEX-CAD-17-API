# TFlex.Drawing.Graphics

Assembly: `TFlexAPI`
Namespace: `TFlex.Drawing`

## Summary

Класс предназначен для вывода графического изображения на экран или другое графическое устройство с использованием вещественных координат в системе координат документа.

## Constructors

### `Graphics(System.IntPtr,System.Drawing.Rectangle,TFlex.Drawing.Rectangle)`

ID: `M:TFlex.Drawing.Graphics.#ctor(System.IntPtr,System.Drawing.Rectangle,TFlex.Drawing.Rectangle)`

Конструктор

Parameters:
- `hWnd`: Дескриптор окна
- `rect`: Прямоугольник в системе координат устройства, в который производится вывод изображения
- `window`: Прямоугольник в мировой системе координат, соответствующий прямоугольнику в системе координат устройства

### `Graphics(TFlex.Drawing.Graphics,TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Drawing.Graphics.#ctor(TFlex.Drawing.Graphics,TFlex.Drawing.AffineMap)`

Конструктор. Новый объект основанный на baseGraphics с применением к нему преобразования transformation.

Parameters:
- `baseGraphics`: Базовый объект
- `transformation`: Преобразование

## Methods

### `Graphics(System.IntPtr,System.Drawing.Rectangle,TFlex.Drawing.Rectangle)`

ID: `M:TFlex.Drawing.Graphics.#ctor(System.IntPtr,System.Drawing.Rectangle,TFlex.Drawing.Rectangle)`

Конструктор

Parameters:
- `hWnd`: Дескриптор окна
- `rect`: Прямоугольник в системе координат устройства, в который производится вывод изображения
- `window`: Прямоугольник в мировой системе координат, соответствующий прямоугольнику в системе координат устройства

### `Graphics(TFlex.Drawing.Graphics,TFlex.Drawing.AffineMap)`

ID: `M:TFlex.Drawing.Graphics.#ctor(TFlex.Drawing.Graphics,TFlex.Drawing.AffineMap)`

Конструктор. Новый объект основанный на baseGraphics с применением к нему преобразования transformation.

Parameters:
- `baseGraphics`: Базовый объект
- `transformation`: Преобразование

### `AddDashLine(System.Double)`

ID: `M:TFlex.Drawing.Graphics.AddDashLine(System.Double)`

Добавление в массив штрихов штрихового типа линии сплошного штриха

Parameters:
- `length`: Длина добавляемого штриха

Remarks: Суммарное число штрихов и пробелов между ними не должно превышать 20

### `AddDashSpace(System.Double)`

ID: `M:TFlex.Drawing.Graphics.AddDashSpace(System.Double)`

Добавление в массив штрихов штрихового типа линии пробела (интервала между штрихами)

Parameters:
- `length`: Длина добавляемого пробела

Remarks: Суммарное число штрихов и пробелов между ними не должно превышать 20

### `Arc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.Arc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point)`

Прорисовка дуги с центром в заданной точке, проходящей через две точки, против часовой стрелки

Parameters:
- `center`: Центральная точка дуги
- `point1`: Точка начала дуги
- `point2`: Точка конца дуги

### `Arc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point,System.Boolean)`

ID: `M:TFlex.Drawing.Graphics.Arc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point,System.Boolean)`

Прорисовка дуги с центром в заданной точке, проходящей через две точки

Parameters:
- `center`: Центральная точка дуги
- `point1`: Точка начала дуги
- `point2`: Точка конца дуги
- `direction`: Направление дуги. При значении true против часовой стрелки; false - по часовой стрелке

### `Arc3Points(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.Arc3Points(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point)`

Прорисовка дуги, проходящей через три точки

Parameters:
- `point1`: Точка начала дуги
- `point2`: Точка на дуге
- `point3`: Точка конца дуги

### `ArrowArc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point,System.Int32,System.Double,System.Int32,System.Double)`

ID: `M:TFlex.Drawing.Graphics.ArrowArc(TFlex.Drawing.Point,TFlex.Drawing.Point,TFlex.Drawing.Point,System.Int32,System.Double,System.Int32,System.Double)`

Прорисовка дуги со стрелками с центром в заданной точке, проходящей через две точки, против часовой стрелки

Parameters:
- `center`: Центральная точка дуги
- `point1`: Точка начала дуги
- `point2`: Точка конца дуги
- `startType`: Тип стрелки в начальной точке
- `startSize`: Размер стрелки в начальной точке
- `endType`: Тип стрелки в конечной точке
- `endSize`: Размер стрелки в конечной точке

### `ArrowLine(TFlex.Drawing.Point,TFlex.Drawing.Point,System.Int32,System.Double,System.Int32,System.Double)`

ID: `M:TFlex.Drawing.Graphics.ArrowLine(TFlex.Drawing.Point,TFlex.Drawing.Point,System.Int32,System.Double,System.Int32,System.Double)`

Прорисовка отрезка со стрелками

Parameters:
- `start`: Начальная точка отрезка
- `end`: Конечная точка отрезка
- `startType`: Тип стрелки в начальной точке
- `startSize`: Размер стрелки в начальной точке
- `endType`: Тип стрелки в конечной точке
- `endSize`: Размер стрелки в конечной точке

### `ArrowPolyline(TFlex.Drawing.Polyline,System.Int32,System.Double,System.Int32,System.Double)`

ID: `M:TFlex.Drawing.Graphics.ArrowPolyline(TFlex.Drawing.Polyline,System.Int32,System.Double,System.Int32,System.Double)`

Прорисовка полилинии со стрелками

Parameters:
- `polyline`: Полилиния
- `startType`: Тип стрелки в начальной точке
- `startSize`: Размер стрелки в начальной точке
- `endType`: Тип стрелки в конечной точке
- `endSize`: Размер стрелки в конечной точке

Remarks: Полилиния выводится с учётом установленной растровой операции, цвета вывода, толщины линий, типа линий

### `BeginDraw`

ID: `M:TFlex.Drawing.Graphics.BeginDraw`

Начало вывода изображения

Remarks: Данный метод необходимо вызвать перед началом вывода изображения с использованием функций данного класса. Завершение вывода должно заканчиваться вызовом метода `M:TFlex.Drawing.Graphics.EndDraw` . Вызовы этой пары функций могут быть вложенными, однако обязательным является соблюдение парности. Каждому вызову `M:TFlex.Drawing.Graphics.BeginDraw` должен соответствовать вызов `M:TFlex.Drawing.Graphics.EndDraw` .

### `Circle(TFlex.Drawing.Point,System.Double)`

ID: `M:TFlex.Drawing.Graphics.Circle(TFlex.Drawing.Point,System.Double)`

Прорисовка окружности

Parameters:
- `center`: Центр окружности
- `radius`: Радиус окружности

### `Circle(TFlex.Drawing.Point,TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.Circle(TFlex.Drawing.Point,TFlex.Drawing.Point)`

Прорисовка окружности

Parameters:
- `center`: Центр окружности
- `point`: Точка на окружности

### `ClearBackground`

ID: `M:TFlex.Drawing.Graphics.ClearBackground`

Очистка фона

Remarks: Очистка производится цветом фона, установленного при помощи метода `M:TFlex.Drawing.Graphics.SetBkColor(System.Int32)` или свойства `P:TFlex.Drawing.Graphics.BkColor` . По умолчанию установлен белый цвет фона

### `ClearDashes`

ID: `M:TFlex.Drawing.Graphics.ClearDashes`

Сброс массива штрихов штрихового типа линии

Remarks: Последующее добавление штрихов и пробелов осуществляется при помощи методов `M:TFlex.Drawing.Graphics.AddDashLine(System.Double)` и `M:TFlex.Drawing.Graphics.AddDashSpace(System.Double)`

### `Dispose`

ID: `M:TFlex.Drawing.Graphics.Dispose`

Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `DrawBitmap(System.IntPtr,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Nullable`1{System.Drawing.Color},System.Boolean)`

ID: `M:TFlex.Drawing.Graphics.DrawBitmap(System.IntPtr,System.Double,System.Double,System.Double,System.Double,System.Double,System.Double,System.Nullable`1{System.Drawing.Color},System.Boolean)`

Рисовать растровое изображение

Parameters:
- `bitmapHandle`: Дескриптор растрового изображения
- `x`: X
- `y`: Y
- `width`: Ширина
- `height`: Высота
- `sin`: Синус
- `cos`: Косинус
- `transparentColor`: Цвет прозрачности
- `useAlphaChannel`: Использовать альфа-канал

### `DrawMarker(TFlex.Drawing.MarkerType,TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.DrawMarker(TFlex.Drawing.MarkerType,TFlex.Drawing.Point)`

Вывод маркера

Parameters:
- `type`: Тип маркера
- `point`: Координаты маркера

### `DrawText(TFlex.Drawing.Point,System.String)`

ID: `M:TFlex.Drawing.Graphics.DrawText(TFlex.Drawing.Point,System.String)`

Вывод текста в указанной точке

Parameters:
- `point`: Координаты текста
- `text`: Содержание текста

### `EndDraw`

ID: `M:TFlex.Drawing.Graphics.EndDraw`

Завершение вывода изображения

Remarks: Данную функцию необходимо вызвать после завершения вывода изображения с использованием функций данного класса. До начала необходимо вызвать метод `M:TFlex.Drawing.Graphics.BeginDraw`

### `Fill(TFlex.Drawing.Polyline)`

ID: `M:TFlex.Drawing.Graphics.Fill(TFlex.Drawing.Polyline)`

Заливка области, ограниченной полилинией

Parameters:
- `polyline`: Полилиния

Remarks: Заливка производится учётом установленной растровой операции и цвета вывода

### `FillRectangle(TFlex.Drawing.Rectangle)`

ID: `M:TFlex.Drawing.Graphics.FillRectangle(TFlex.Drawing.Rectangle)`

Заливка прямоугольника

Parameters:
- `rect`: Прямоугольник

### `Finalize`

ID: `M:TFlex.Drawing.Graphics.Finalize`

Финализатор. Выполняет определяемые приложением задачи, связанные с удалением, высвобождением или сбросом неуправляемых ресурсов

### `GetDeviceContext`

ID: `M:TFlex.Drawing.Graphics.GetDeviceContext`

Получение дескриптора графического устройства (HDC)

Returns: Дескриптор графического устройства

Remarks: Для того чтобы воспользоваться дескриптором графического устройства, который используется для вывода данным классом, его можно получить при помощи данного метода. Ненулевое значение может быть получено только когда процесс вывода инициализирован при помощи `M:TFlex.Drawing.Graphics.BeginDraw` или вызван метод `P:TFlex.Drawing.Graphics.DeviceContext` с ненулевым значением дескриптора графического устройства.

Examples:
- `using System; using System.Drawing; using System.Windows.Forms; using System.IO; using TFlex; using TFlex.Model; using TFlex.Model.Model2D; using TFlex.Model.Model3D; using TFlex.Command; using TFlex.Drawing; namespace NewMacroNamespace { public class NewMacroClass { public static void NewMacro() { TFlex.Command.CommandState commandState = new TFlex.Command.CommandState(); DeviceContextCommand deviceContextCommand = new DeviceContextCommand(commandState); deviceContextCommand.InsertGroove(commandState); } public class DeviceContextCommand : CustomCommand { public DeviceContextCommand(TFlex.Command.CommandState cmd) : base(cmd) { } TFlex.Model.Document _document; public override void OnInitialize(InitializeEventArgs e) { _document = TFlex.Application.ActiveDocument; _document.BeginChanges(""); base.OnInitialize(e); UpdateAutomenu(); } public override void OnExit(ExitEventArgs e) { _document.EndChanges(); } public void InsertGroove(TFlex.Command.CommandState cmd) { try { CustomCommand d = new DeviceContextCommand(cmd); d.Run(null); } catch (Exception e) { MessageBox.Show(e.StackTrace); } } public InputState State { get; set; } public enum InputState { None,//ничего не выбрано Draw,//начать рисование Exit//закончить рисование }; //событие перемещения курсора public override void OnShowCursor(TFlex.Command.MouseEventArgs e) { base.OnShowCursor(e); if (State == InputState.Draw) { IntPtr hdc = e.Graphics.GetDeviceContext(); //создание класса Graphics System.Drawing.Graphics newGraphics = System.Drawing.Graphics.FromHdc(hdc); //рисование прямоугольника с рамкой newGraphics.DrawRectangle(new Pen(System.Drawing.Color.BlueViolet, 3), (int)(e.X), (int)(e.Y), 100, 50); //картинка Image img = Image.FromFile(Path.Combine(TFlex.Application.ActiveDocument.FilePath, "mail.png")); //рисование прямоугольника с заливкой картинкой newGraphics.FillRectangle(new TextureBrush(img), new System.Drawing.Rectangle(new System.Drawing.Point((int)(e.X), (int)(e.Y)), new System.Drawing.Size(100, 50))); //освобождение ресурсов img.Dispose(); e.Graphics.ReleaseDeviceContext(hdc); newGraphics.Dispose(); } } public override void OnKeyPressed(TFlex.Command.KeyEventArgs e) { _document = e.Document; switch (e.Code) { case KeyCode.keyEND: { State = InputState.Draw; _document.ApplyChanges(); UpdateAutomenu(); } break; case KeyCode.keyESCAPE: { State = InputState.Exit; GoToNextState(null); OnExit(null); } break; } } //формирование кнопок автоменю protected void UpdateAutomenu() { TFlex.Command.Button[] buttonsAutoMenu = new TFlex.Command.Button[2]; buttonsAutoMenu[0] = new DefaultButton(DefaultButton.Kind.OK, KeyCode.keyEND, State == InputState.Draw ? TFlex.Command.Button.Style.Checked : TFlex.Command.Button.Style.Default); buttonsAutoMenu[1] = new DefaultButton(State == InputState.Exit ? DefaultButton.Kind.Exit : DefaultButton.Kind.Cancel); Automenu = new Automenu(buttonsAutoMenu); } }; } }`
- `using System; using System.Drawing; using System.Windows.Forms; using System.IO; using TFlex; using TFlex.Model; using TFlex.Model.Model2D; using TFlex.Model.Model3D; using TFlex.Command; using TFlex.Drawing; namespace NewMacroNamespace { public class NewMacroClass { public static void NewMacro() { TFlex.Command.CommandState commandState = new TFlex.Command.CommandState(); DeviceContextCommand deviceContextCommand = new DeviceContextCommand(commandState); deviceContextCommand.InsertGroove(commandState); } public class DeviceContextCommand : CustomCommand { public DeviceContextCommand(TFlex.Command.CommandState cmd) : base(cmd) { } TFlex.Model.Document _document; public override void OnInitialize(InitializeEventArgs e) { _document = TFlex.Application.ActiveDocument; _document.BeginChanges(""); base.OnInitialize(e); UpdateAutomenu(); } public override void OnExit(ExitEventArgs e) { _document.EndChanges(); } public void InsertGroove(TFlex.Command.CommandState cmd) { try { CustomCommand d = new DeviceContextCommand(cmd); d.Run(null); } catch (Exception e) { MessageBox.Show(e.StackTrace); } } public InputState State { get; set; } public enum InputState { None,//ничего не выбрано Draw,//начать рисование Exit//закончить рисование }; //событие перемещения курсора public override void OnShowCursor(TFlex.Command.MouseEventArgs e) { base.OnShowCursor(e); if (State == InputState.Draw) { IntPtr hdc = e.Graphics.GetDeviceContext(); //создание класса Graphics System.Drawing.Graphics newGraphics = System.Drawing.Graphics.FromHdc(hdc); //рисование прямоугольника с рамкой newGraphics.DrawRectangle(new Pen(System.Drawing.Color.BlueViolet, 3), (int)(e.X), (int)(e.Y), 100, 50); //картинка Image img = Image.FromFile(Path.Combine(TFlex.Application.ActiveDocument.FilePath, "mail.png")); //рисование прямоугольника с заливкой картинкой newGraphics.FillRectangle(new TextureBrush(img), new System.Drawing.Rectangle(new System.Drawing.Point((int)(e.X), (int)(e.Y)), new System.Drawing.Size(100, 50))); //освобождение ресурсов img.Dispose(); e.Graphics.ReleaseDeviceContext(hdc); newGraphics.Dispose(); } } public override void OnKeyPressed(TFlex.Command.KeyEventArgs e) { _document = e.Document; switch (e.Code) { case KeyCode.keyEND: { State = InputState.Draw; _document.ApplyChanges(); UpdateAutomenu(); } break; case KeyCode.keyESCAPE: { State = InputState.Exit; GoToNextState(null); OnExit(null); } break; } } //формирование кнопок автоменю protected void UpdateAutomenu() { TFlex.Command.Button[] buttonsAutoMenu = new TFlex.Command.Button[2]; buttonsAutoMenu[0] = new DefaultButton(DefaultButton.Kind.OK, KeyCode.keyEND, State == InputState.Draw ? TFlex.Command.Button.Style.Checked : TFlex.Command.Button.Style.Default); buttonsAutoMenu[1] = new DefaultButton(State == InputState.Exit ? DefaultButton.Kind.Exit : DefaultButton.Kind.Cancel); Automenu = new Automenu(buttonsAutoMenu); } }; } }`

### `GetLCSPoint(TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.GetLCSPoint(TFlex.Drawing.Point)`

Получение координат точки, координаты которой заданы в мировой системе координат (системе координат модели), в системе координат графического устройства

Parameters:
- `point`: Точка в мировой системе координат (системе координат модели)

Returns: Точка в системе координат графического устройства, соответствующая исходной

### `GetLinePatternNames`

ID: `M:TFlex.Drawing.Graphics.GetLinePatternNames`

Получение списка названий стилей линий

### `GetLinePatternPreview(System.String,System.Drawing.Rectangleref ,System.Drawing.Color)`

ID: `M:TFlex.Drawing.Graphics.GetLinePatternPreview(System.String,System.Drawing.Rectangle@,System.Drawing.Color)`

Получение изображения для предпросмотра стиля линии

Parameters:
- `pattern`: Название стиля линии
- `rect`: Область рисования
- `backColor`: Цвет фона

### `GetLinePatterns`

ID: `M:TFlex.Drawing.Graphics.GetLinePatterns`

Получение списка названий стилей линий

### `GetTextHeight(System.String)`

ID: `M:TFlex.Drawing.Graphics.GetTextHeight(System.String)`

Получение высоты текста с текущими установками шрифта

Parameters:
- `text`: Текст

Returns: Высота текста

### `GetTextLength(System.String)`

ID: `M:TFlex.Drawing.Graphics.GetTextLength(System.String)`

Получение длины текста с текущими установками шрифта

Parameters:
- `text`: Текст

Returns: Длина текста вдоль его направления

### `GetWCSPoint(System.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.GetWCSPoint(System.Drawing.Point)`

Получение координат точки, координаты которой заданы в системе графического устройства, в мировой системе координат (системе координат модели)

Parameters:
- `point`: Точка в системе координат графического устройства

Returns: Точка в мировой системе координат (системе координат модели), соответствующая исходной

### `Line(TFlex.Drawing.Point,TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.Line(TFlex.Drawing.Point,TFlex.Drawing.Point)`

Прорисовка отрезка между двумя точками

Parameters:
- `start`: Начальная точка отрезка
- `end`: Конечная точка отрезка

### `LineTo(TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.LineTo(TFlex.Drawing.Point)`

Прорисовка отрезка от указателя к данной точке

Parameters:
- `point`: Точка, в которую необходимо провести отрезок и переместить указатель

Remarks: Отрезок выводится от указателя, который был установлен методом `M:TFlex.Drawing.Graphics.MoveTo(TFlex.Drawing.Point)` или предыдущим вызовом метода `M:TFlex.Drawing.Graphics.LineTo(TFlex.Drawing.Point)`

### `MoveTo(TFlex.Drawing.Point)`

ID: `M:TFlex.Drawing.Graphics.MoveTo(TFlex.Drawing.Point)`

Перемещение указателя в точку

Parameters:
- `point`: Точка, в которую необходимо переместить указатель

Remarks: Последующий вызов метода `M:TFlex.Drawing.Graphics.LineTo(TFlex.Drawing.Point)` выведет отрезок, начинающийся в данной точке

### `Polyline(TFlex.Drawing.Polyline)`

ID: `M:TFlex.Drawing.Graphics.Polyline(TFlex.Drawing.Polyline)`

Прорисовка полилинии

Parameters:
- `polyline`: Полилиния

Remarks: Полилиния выводится с учётом установленной растровой операции, цвета вывода, толщины линий, типа линий

### `Rectangle(TFlex.Drawing.Rectangle)`

ID: `M:TFlex.Drawing.Graphics.Rectangle(TFlex.Drawing.Rectangle)`

Прорисовка границ прямоугольника

Parameters:
- `rect`: Прямоугольник

### `ReleaseDeviceContext(System.IntPtr)`

ID: `M:TFlex.Drawing.Graphics.ReleaseDeviceContext(System.IntPtr)`

Освобождение дескриптора графического устройства (HDC)

Parameters:
- `Handle`: Дескриптор графического устройства

Examples:
- `using System; using System.Drawing; using System.Windows.Forms; using System.IO; using TFlex; using TFlex.Model; using TFlex.Model.Model2D; using TFlex.Model.Model3D; using TFlex.Command; using TFlex.Drawing; namespace NewMacroNamespace { public class NewMacroClass { public static void NewMacro() { TFlex.Command.CommandState commandState = new TFlex.Command.CommandState(); DeviceContextCommand deviceContextCommand = new DeviceContextCommand(commandState); deviceContextCommand.InsertGroove(commandState); } public class DeviceContextCommand : CustomCommand { public DeviceContextCommand(TFlex.Command.CommandState cmd) : base(cmd) { } TFlex.Model.Document _document; public override void OnInitialize(InitializeEventArgs e) { _document = TFlex.Application.ActiveDocument; _document.BeginChanges(""); base.OnInitialize(e); UpdateAutomenu(); } public override void OnExit(ExitEventArgs e) { _document.EndChanges(); } public void InsertGroove(TFlex.Command.CommandState cmd) { try { CustomCommand d = new DeviceContextCommand(cmd); d.Run(null); } catch (Exception e) { MessageBox.Show(e.StackTrace); } } public InputState State { get; set; } public enum InputState { None,//ничего не выбрано Draw,//начать рисование Exit//закончить рисование }; //событие перемещения курсора public override void OnShowCursor(TFlex.Command.MouseEventArgs e) { base.OnShowCursor(e); if (State == InputState.Draw) { IntPtr hdc = e.Graphics.GetDeviceContext(); //создание класса Graphics System.Drawing.Graphics newGraphics = System.Drawing.Graphics.FromHdc(hdc); //рисование прямоугольника с рамкой newGraphics.DrawRectangle(new Pen(System.Drawing.Color.BlueViolet, 3), (int)(e.X), (int)(e.Y), 100, 50); //картинка Image img = Image.FromFile(Path.Combine(TFlex.Application.ActiveDocument.FilePath, "mail.png")); //рисование прямоугольника с заливкой картинкой newGraphics.FillRectangle(new TextureBrush(img), new System.Drawing.Rectangle(new System.Drawing.Point((int)(e.X), (int)(e.Y)), new System.Drawing.Size(100, 50))); //освобождение ресурсов img.Dispose(); e.Graphics.ReleaseDeviceContext(hdc); newGraphics.Dispose(); } } public override void OnKeyPressed(TFlex.Command.KeyEventArgs e) { _document = e.Document; switch (e.Code) { case KeyCode.keyEND: { State = InputState.Draw; _document.ApplyChanges(); UpdateAutomenu(); } break; case KeyCode.keyESCAPE: { State = InputState.Exit; GoToNextState(null); OnExit(null); } break; } } //формирование кнопок автоменю protected void UpdateAutomenu() { TFlex.Command.Button[] buttonsAutoMenu = new TFlex.Command.Button[2]; buttonsAutoMenu[0] = new DefaultButton(DefaultButton.Kind.OK, KeyCode.keyEND, State == InputState.Draw ? TFlex.Command.Button.Style.Checked : TFlex.Command.Button.Style.Default); buttonsAutoMenu[1] = new DefaultButton(State == InputState.Exit ? DefaultButton.Kind.Exit : DefaultButton.Kind.Cancel); Automenu = new Automenu(buttonsAutoMenu); } }; } }`
- `using System; using System.Drawing; using System.Windows.Forms; using System.IO; using TFlex; using TFlex.Model; using TFlex.Model.Model2D; using TFlex.Model.Model3D; using TFlex.Command; using TFlex.Drawing; namespace NewMacroNamespace { public class NewMacroClass { public static void NewMacro() { TFlex.Command.CommandState commandState = new TFlex.Command.CommandState(); DeviceContextCommand deviceContextCommand = new DeviceContextCommand(commandState); deviceContextCommand.InsertGroove(commandState); } public class DeviceContextCommand : CustomCommand { public DeviceContextCommand(TFlex.Command.CommandState cmd) : base(cmd) { } TFlex.Model.Document _document; public override void OnInitialize(InitializeEventArgs e) { _document = TFlex.Application.ActiveDocument; _document.BeginChanges(""); base.OnInitialize(e); UpdateAutomenu(); } public override void OnExit(ExitEventArgs e) { _document.EndChanges(); } public void InsertGroove(TFlex.Command.CommandState cmd) { try { CustomCommand d = new DeviceContextCommand(cmd); d.Run(null); } catch (Exception e) { MessageBox.Show(e.StackTrace); } } public InputState State { get; set; } public enum InputState { None,//ничего не выбрано Draw,//начать рисование Exit//закончить рисование }; //событие перемещения курсора public override void OnShowCursor(TFlex.Command.MouseEventArgs e) { base.OnShowCursor(e); if (State == InputState.Draw) { IntPtr hdc = e.Graphics.GetDeviceContext(); //создание класса Graphics System.Drawing.Graphics newGraphics = System.Drawing.Graphics.FromHdc(hdc); //рисование прямоугольника с рамкой newGraphics.DrawRectangle(new Pen(System.Drawing.Color.BlueViolet, 3), (int)(e.X), (int)(e.Y), 100, 50); //картинка Image img = Image.FromFile(Path.Combine(TFlex.Application.ActiveDocument.FilePath, "mail.png")); //рисование прямоугольника с заливкой картинкой newGraphics.FillRectangle(new TextureBrush(img), new System.Drawing.Rectangle(new System.Drawing.Point((int)(e.X), (int)(e.Y)), new System.Drawing.Size(100, 50))); //освобождение ресурсов img.Dispose(); e.Graphics.ReleaseDeviceContext(hdc); newGraphics.Dispose(); } } public override void OnKeyPressed(TFlex.Command.KeyEventArgs e) { _document = e.Document; switch (e.Code) { case KeyCode.keyEND: { State = InputState.Draw; _document.ApplyChanges(); UpdateAutomenu(); } break; case KeyCode.keyESCAPE: { State = InputState.Exit; GoToNextState(null); OnExit(null); } break; } } //формирование кнопок автоменю protected void UpdateAutomenu() { TFlex.Command.Button[] buttonsAutoMenu = new TFlex.Command.Button[2]; buttonsAutoMenu[0] = new DefaultButton(DefaultButton.Kind.OK, KeyCode.keyEND, State == InputState.Draw ? TFlex.Command.Button.Style.Checked : TFlex.Command.Button.Style.Default); buttonsAutoMenu[1] = new DefaultButton(State == InputState.Exit ? DefaultButton.Kind.Exit : DefaultButton.Kind.Cancel); Automenu = new Automenu(buttonsAutoMenu); } }; } }`

### `SetBkColor(System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetBkColor(System.Int32)`

Установка цвета фона

Parameters:
- `color`: Цвет

Returns: Цвет фона, который был установлен до вызова данного метода

Remarks: Предопределённые значения перечислены в перечислении `T:TFlex.Drawing.Color`

### `SetColor(System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetColor(System.Int32)`

Установка цвета, которым должен производиться вывод

Parameters:
- `color`: Цвет

Returns: Цвет, который был установлен до вызова данного метода

Remarks: Предопределённые значения перечислены в перечислителе `T:TFlex.Drawing.Color`

### `SetColorLock(System.Boolean)`

ID: `M:TFlex.Drawing.Graphics.SetColorLock(System.Boolean)`

Установка режима запрета смены цвета (одноцветный режим)

Parameters:
- `lock`: true, если необходимо установить режим запрета смены цвета; false, если необходимо отменить этот режим

Returns: Режим запрета смены цвета, установленный до вызова данного метода

### `SetDashedType(System.Boolean)`

ID: `M:TFlex.Drawing.Graphics.SetDashedType(System.Boolean)`

Установка прорисовки шрихового типа линии

Parameters:
- `dashed`: true, если необходимо рисовать штриховую линию; false для сплошного типа линии

Returns: true, если до вызова была установлена прорисовка штриховой линии; false для сплошного типа линии

### `SetEraseMode(System.Boolean)`

ID: `M:TFlex.Drawing.Graphics.SetEraseMode(System.Boolean)`

Установка режима очистки фона

Parameters:
- `value`: Состояние режима очистки фона

Returns: Предыдущее значение

### `SetFontName(System.String,TFlex.Drawing.FontStyle)`

ID: `M:TFlex.Drawing.Graphics.SetFontName(System.String,TFlex.Drawing.FontStyle)`

Выбор шрифта для прорисовки текста

Parameters:
- `fontname`: Имя шрифта
- `style`: Стиль шрифта. Учитывается только для шрифтов TrueType

Remarks: Тип шрифта зависит от расширения имени шрифта. Если присутствует расширение".shx", то будет выбран шрифт формата SHX. Метод `M:TFlex.Drawing.Graphics.SetFontName(System.String,TFlex.Drawing.FontStyle)` является альтернативой данному методу.

### `SetFontRotation(System.Double,System.Double)`

ID: `M:TFlex.Drawing.Graphics.SetFontRotation(System.Double,System.Double)`

Установка угла поворота текста с помощью вектора вертикали

Parameters:
- `dx`: Координата x вектора вертикали шрифта
- `dy`: Координата y вектора вертикали шрифта

Remarks: Для вывода обычного горизонтального текста вектор вертикали шрифта должен быть направлен вверх, например иметь координаты (1,0). Альтернативным способом задания угла поворота текста является свойство `P:TFlex.Drawing.Graphics.FontAngle`

### `SetLineWidth(System.Double)`

ID: `M:TFlex.Drawing.Graphics.SetLineWidth(System.Double)`

Установка толщины линии для функций вывода линий, полилиний, текстов и других линейных объектов

Parameters:
- `width`: Значение толщины линий

Returns: Толщина линий, которая была установлена до вызова данного метода

### `SetRGBBkColor(System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetRGBBkColor(System.Int32)`

Установка цвета фона в виде компонент красного, зелёного и синего

Parameters:
- `color`: Цвет

Returns: Цвет фона, который был установлен до вызова данного метода

### `SetRGBBkColor(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetRGBBkColor(System.Int32,System.Int32,System.Int32)`

Установка цвета фона в виде компонент красного, зелёного и синего

Parameters:
- `r`: Красная составляющия (от 0 до 255)
- `g`: Зелёная составляющия (от 0 до 255)
- `b`: Синяя составляющия (от 0 до 255)

Returns: Цвет фона, который был установлен до вызова данного метода

### `SetRGBColor(System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetRGBColor(System.Int32)`

Установка цвета, которым должен производиться вывод, в виде компонент красного, зелёного и синего

Parameters:
- `color`: Цвет

Returns: Цвет, который был установлен до вызова данного метода

### `SetRGBColor(System.Int32,System.Int32,System.Int32)`

ID: `M:TFlex.Drawing.Graphics.SetRGBColor(System.Int32,System.Int32,System.Int32)`

Установка цвета, которым должен производиться вывод, в виде компонент красного, зелёного и синего

Parameters:
- `r`: Красная составляющая (от 0 до 255)
- `g`: Зелёная составляющая (от 0 до 255)
- `b`: Синяя составляющая (от 0 до 255)

Returns: Цвет, который был установлен до вызова данного метода

### `SetRop(TFlex.Drawing.RasterOperation)`

ID: `M:TFlex.Drawing.Graphics.SetRop(TFlex.Drawing.RasterOperation)`

Установка типа растровой операции, которую необходимо использовать для вывода

Parameters:
- `rop`: Тип растровой операции

Returns: Тип растровой операции, который был установлен до вызова данного метода

## Propertys

### `BkColor`

ID: `P:TFlex.Drawing.Graphics.BkColor`

Цвет фона

Remarks: Предопределённые значения перечислены в перечислителе `T:TFlex.Drawing.Color`

### `Color`

ID: `P:TFlex.Drawing.Graphics.Color`

Цвет, которым производится вывод

Remarks: Предопределённые значения перечислены в перечислителе `T:TFlex.Drawing.Color`

Examples:
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`
- `public static void SetColor(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа ob.Color = 40;//установка цвета document.EndChanges();//Закрытие блока изменений документа }`

### `ColorLock`

ID: `P:TFlex.Drawing.Graphics.ColorLock`

Режим запрета смены цвета (одноцветный режим)

### `DashedType`

ID: `P:TFlex.Drawing.Graphics.DashedType`

Установка прорисовки шрихового типа линии

Remarks: true, если необходимо рисовать штриховую линию; false для сплошного типа линии

### `DeviceContext`

ID: `P:TFlex.Drawing.Graphics.DeviceContext`

Установка дескриптора графического устройства (HDC)

Remarks: В некоторых случаях необходимо выводить изображение непосредственно на графическое устройство с использованием его дескриптора. Для этого используется данный метод. Для этого можно сконструировать объект данного класса со значением hWnd равным 0. Затем необходимо воспользоваться данным методом для установки дескриптора графического устройства. После завершения вывода обязательно обнуление дескриптора графического устройства. Для этого в качестве значения параметра hdc должно быть передано значение 0.

### `FontAngle`

ID: `P:TFlex.Drawing.Graphics.FontAngle`

Установка угла поворота текста

Remarks: Угол поворота измеряется от горизонтали. Положительное значение угла соответствует повороту против часовой стрелки. По умолчанию значение этого параметра равно 0. Альтернативным способом задания угла поворота текста является метод `M:TFlex.Drawing.Graphics.SetFontRotation(System.Double,System.Double)`

### `FontClearBackground`

ID: `P:TFlex.Drawing.Graphics.FontClearBackground`

Установка параметра "очистка фона"

Remarks: По умолчанию значение этого параметра равно false

### `FontExtension`

ID: `P:TFlex.Drawing.Graphics.FontExtension`

Установка коэффициента расширения шрифта

Remarks: Коэффициент расширения шрифта учитывается только при выводе шрифта формата SHX. По умолчанию коэффициент расширения шрифта равен 1.

### `FontHorizontalAlignment`

ID: `P:TFlex.Drawing.Graphics.FontHorizontalAlignment`

Установка выравнивания текста по горизонтали

Remarks: По умолчанию значение этого параметра равно Left

### `FontInterval`

ID: `P:TFlex.Drawing.Graphics.FontInterval`

Установка коэффициента междустрочного интервала

Remarks: Абсолютное значение междустрочного интервала вычисляется перемножением высоты шрифта и данного коэффициента. По умолчанию коэффициент дополнительного интервала между симолами шрифта равен 0.5

### `FontName`

ID: `P:TFlex.Drawing.Graphics.FontName`

Выбор шрифта для прорисовки текста

Remarks: Тип шрифта зависит от расширения имени шрифта. Если присутствует расширение ".shx", то будет выбран шрифт формата SHX. Если выбирается шрифт типа TrueType (без расширения), то по умолчанию устанавливается стиль Normal из перечислителя `T:TFlex.Drawing.FontStyle` . Метод `M:TFlex.Drawing.Graphics.SetFontName(System.String,TFlex.Drawing.FontStyle)` является альтернативой данному методу

### `FontSize`

ID: `P:TFlex.Drawing.Graphics.FontSize`

Установка размера шрифта

### `FontSpacing`

ID: `P:TFlex.Drawing.Graphics.FontSpacing`

Установка дополнительного интервала между символами

Remarks: Абсолютное значение дополнительного интервала между символами вычисляется перемножением высоты шрифта и данного коэффициента. По умолчанию коэффициент дополнительного интервала между символами шрифта равен 0

### `FontTilt`

ID: `P:TFlex.Drawing.Graphics.FontTilt`

Установка угла наклона шрифта

Remarks: Угол наклона учитывается только при выводе шрифта формата SHX. Угол измеряется в градусах. По умолчанию угол наклона шрифта равен 90.

### `FontVerticalAlignment`

ID: `P:TFlex.Drawing.Graphics.FontVerticalAlignment`

Установка выравнивания текста по вертикали

Remarks: По умолчанию значение этого параметра равно Lower

### `IsDisplayDevice`

ID: `P:TFlex.Drawing.Graphics.IsDisplayDevice`

Текущий вывод производится на экран

### `IsExportDevice`

ID: `P:TFlex.Drawing.Graphics.IsExportDevice`

Текущий вывод производится в файл другого формата

### `IsMarkDevice`

ID: `P:TFlex.Drawing.Graphics.IsMarkDevice`

Текущий вывод производится для пометки объекта

### `IsPrinterDevice`

ID: `P:TFlex.Drawing.Graphics.IsPrinterDevice`

Текущий вывод производится на принтер

### `LCSRectangle`

ID: `P:TFlex.Drawing.Graphics.LCSRectangle`

Прямоугольник вывода в системе координат графического устройства

### `LineWidth`

ID: `P:TFlex.Drawing.Graphics.LineWidth`

Толщина линии для функций вывода линий, полилиний, текстов и других линейных объектов

### `MarkColor`

ID: `P:TFlex.Drawing.Graphics.MarkColor`

Цвет, используемый для пометки элементов

### `RGBBkColor`

ID: `P:TFlex.Drawing.Graphics.RGBBkColor`

Цвет фона в виде компонент красного, зелёного и синего

### `RGBColor`

ID: `P:TFlex.Drawing.Graphics.RGBColor`

Цвет, которым производится вывод, в виде компонент красного, зелёного и синего

### `Rop`

ID: `P:TFlex.Drawing.Graphics.Rop`

Тип растровой операции, установленной для вывода

### `Scale`

ID: `P:TFlex.Drawing.Graphics.Scale`

Масштаб преобразования в систему координат графического устройства

### `WCSRectangle`

ID: `P:TFlex.Drawing.Graphics.WCSRectangle`

Прямоугольник вывода в мировой системе координат
