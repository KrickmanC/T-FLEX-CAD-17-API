# TFlex.Model.Model3D.MaterialParameters

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Параметры материала

## Methods

### `GetProperty(TFlex.Model.Model3D.MaterialParameters.PhysicalProperty)`

ID: `M:TFlex.Model.Model3D.MaterialParameters.GetProperty(TFlex.Model.Model3D.MaterialParameters.PhysicalProperty)`

Чтение физических параметров материала

### `SetProperty(TFlex.Model.Model3D.MaterialParameters.PhysicalProperty,TFlex.Model.Parameter)`

ID: `M:TFlex.Model.Model3D.MaterialParameters.SetProperty(TFlex.Model.Model3D.MaterialParameters.PhysicalProperty,TFlex.Model.Parameter)`

Установка физических параметров материала

Parameters:
- `prop`: Свойство материала
- `parameter`: Физический параметер

Remarks: Единицы измерения параметра в завимости от типа свойства: Плотность (Density) TFlex.Model.Units.StandardUnits.Density.KilogramPerCubicMillimeter Модуль упругости (E_x, E_y, E_z) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter Коэффициент Пуассона (Nu_yz, Nu_xz,Nu_xy) безразмерный Модуль сдвига (G_xy, G_yz, G_xz) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter Коэффициент линейного расширения (Alpha_) TFlex.Model.Units.StandardUnits.ThermalExpansionCoefficient._1PerDegree Теплопроводность (K_x, K_y, K_z) TFlex.Model.Units.StandardUnits.ThermalConductivity.WattPerMillimeterDegree Предел прочности на разрыв (Sigma_ T) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter Предел прочности на сжатие (Sigma_ C) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter Предел текучести (Sigma_ Yield) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter Удельная теплоемкость (specific_heat) TFlex.Model.Units.StandardUnits.SpecificHeatCapacity.JoulePerKilogramKelvin Предел прочности на сдвиг (Tau_ ) TFlex.Model.Units.StandardUnits.BreakingStrength.NewtonPerSquareMillimeter

## Propertys

### `AmbientColor2`

ID: `P:TFlex.Model.Model3D.MaterialParameters.AmbientColor2`

Окружающий цвет

### `BlendColor2`

ID: `P:TFlex.Model.Model3D.MaterialParameters.BlendColor2`

Цвет, используемый в смешанной модели

### `CoordFunction`

ID: `P:TFlex.Model.Model3D.MaterialParameters.CoordFunction`

Режим отображения текстуры

### `Density`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Density`

Плотность материала

### `DiffuseColor2`

ID: `P:TFlex.Model.Model3D.MaterialParameters.DiffuseColor2`

Рассеивающий цвет

### `DirectionS`

ID: `P:TFlex.Model.Model3D.MaterialParameters.DirectionS`

Направление оси S координат текстуры

Remarks: Используется только в режиме отображения "проекция на плоскость"

### `DirectionT`

ID: `P:TFlex.Model.Model3D.MaterialParameters.DirectionT`

Направление оси T координат текстуры

Remarks: Используется только в режиме отображения "проекция на плоскость"

### `Elasticity`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Elasticity`

Модуль упругости

### `EmissiveColor2`

ID: `P:TFlex.Model.Model3D.MaterialParameters.EmissiveColor2`

Излучающий цвет

### `Expansion`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Expansion`

Коэффициент линейного расширения

### `ExportInfo`

ID: `P:TFlex.Model.Model3D.MaterialParameters.ExportInfo`

Дополнительные параметры фотореалистичного изображения

### `Folder`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Folder`

Папка

### `MappingModel`

ID: `P:TFlex.Model.Model3D.MaterialParameters.MappingModel`

Модель совмещения цвета текстуры и грани

### `Name`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Name`

Имя материала

### `Pattern`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Pattern`

Имя шаблона штриховки на сечениях

### `PatternScale`

ID: `P:TFlex.Model.Model3D.MaterialParameters.PatternScale`

Масштаб штриховки на сечениях

### `Puasson`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Puasson`

Коэффициент Пуассона

### `Shininess`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Shininess`

Уровень блеска

### `SpecularColor2`

ID: `P:TFlex.Model.Model3D.MaterialParameters.SpecularColor2`

Отражающий цвет

### `Stress`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Stress`

Допустимое напряжение

### `TemperatureCondition`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TemperatureCondition`

Температуропроводность

### `TextureCenterS`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureCenterS`

Координата S центра текстуры

### `TextureCenterT`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureCenterT`

Координата Т центра вращения текстуры

### `TextureFileName`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureFileName`

Имя файла текстуры

Remarks: Пустое имя означает отсутствие текстуры. Поддерживаются форматы файлов: GIF, JPEG, BMP, PNG. Для возможности экспорта в формат VRML рекомендуется использовать JPEG или PNG

### `TextureRotate`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureRotate`

Угол поворота текстуры

Remarks: Измеряется в градусах

### `TextureScaleS`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureScaleS`

Масштаб текстуры по оси S

### `TextureScaleT`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureScaleT`

Масштаб текстуры по оси T

### `TextureTranslateS`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureTranslateS`

Перенос текстуры по оси S

### `TextureTranslateT`

ID: `P:TFlex.Model.Model3D.MaterialParameters.TextureTranslateT`

Перенос текстуры по оси T

### `ThermalCondition`

ID: `P:TFlex.Model.Model3D.MaterialParameters.ThermalCondition`

Теплопроводность

### `Transparency`

ID: `P:TFlex.Model.Model3D.MaterialParameters.Transparency`

Прозрачность

### `WrapS`

ID: `P:TFlex.Model.Model3D.MaterialParameters.WrapS`

Тип наложения текстуры по оси S

### `WrapT`

ID: `P:TFlex.Model.Model3D.MaterialParameters.WrapT`

Тип наложения текстуры по оси T
