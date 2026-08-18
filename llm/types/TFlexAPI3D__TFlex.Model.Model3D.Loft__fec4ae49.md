# TFlex.Model.Model3D.Loft

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D`

## Summary

Операция "по сечениям"

## Constructors

### `Loft(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Loft.#ctor(TFlex.Model.Document)`

Конструктор для создания Лофтинга

Parameters:
- `document`: Документ, в котором создаётся новый объект

## Methods

### `Loft(TFlex.Model.Document)`

ID: `M:TFlex.Model.Model3D.Loft.#ctor(TFlex.Model.Document)`

Конструктор для создания Лофтинга

Parameters:
- `document`: Документ, в котором создаётся новый объект

### `AddGuide(TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.AddGuide(TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить направляющую

### `AddGuideContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.AddGuideContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить контур к направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)
- `contour`: Добавляемый контур

Remarks: Все контуры направляющей в списке одного типа: все листовые или все проволочные

### `AddGuideFaceCondition(System.Int32,TFlex.Model.Model3D.Loft.FaceCondition)`

ID: `M:TFlex.Model.Model3D.Loft.AddGuideFaceCondition(System.Int32,TFlex.Model.Model3D.Loft.FaceCondition)`

Добавить условие касания с гранью

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)
- `condition`: Граничное условие

Remarks: Грани должны стыковаться c направляющей. Условия в виде граней не могут быть заданы, если для данной направляющей задан другой тип граничного условия.

### `AddGuideVectorCondition(System.Int32,TFlex.Model.Model3D.Loft.VectorCondition)`

ID: `M:TFlex.Model.Model3D.Loft.AddGuideVectorCondition(System.Int32,TFlex.Model.Model3D.Loft.VectorCondition)`

Добавить векторное условие на направляющей

Parameters:
- `guideIndex`: Индекс направляющей
- `condition`: Векторное граничное условие

Remarks: Векторные граничные условия не могут быть заданы, если для данной направляющей задан другой тип граничного условия

### `AddProfile(TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.AddProfile(TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить профиль

Parameters:
- `contour`: Контур с объекта модели

### `AddProfileContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.AddProfileContour(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Добавить контур к профилю

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)
- `contour`: Добавляемый контур

Remarks: Все контуры профиля в списке одного типа: все листовые или все проволочные

### `AddProfileFaceCondition(System.Int32,TFlex.Model.Model3D.Loft.FaceCondition)`

ID: `M:TFlex.Model.Model3D.Loft.AddProfileFaceCondition(System.Int32,TFlex.Model.Model3D.Loft.FaceCondition)`

Добавить условие касания с гранью

Parameters:
- `profileIndex`: Индекс профиля (начинается нуля)
- `condition`: Граничное условие

Remarks: Грани должны стыковаться к профилю. Условия в виде граней не могут быть заданы, если для данного профиля задан другой тип граничного условия.

### `AddProfileVectorCondition(System.Int32,TFlex.Model.Model3D.Loft.VectorCondition)`

ID: `M:TFlex.Model.Model3D.Loft.AddProfileVectorCondition(System.Int32,TFlex.Model.Model3D.Loft.VectorCondition)`

Добавить векторное условие на профиле

Parameters:
- `profileIndex`: Индекс профиля
- `condition`: Векторное граничное условие

Remarks: Векторные граничные условия не могут быть заданы, если для данного профиля задан другой тип граничного условия

### `CanSetAutomaticCouplingPoint`

ID: `M:TFlex.Model.Model3D.Loft.CanSetAutomaticCouplingPoint`

Узнать можно ли установить автоматические точки соответствия

Remarks: Автоматические точки соответствия могут быть установлены при выполнении следующих условий: 1. Все контуры плоские. 2. Все контуры замкнуты. 3. Все или все кроме одного контуры профилей являются G1-непрерывными.

### `CanSetPeriodic`

ID: `M:TFlex.Model.Model3D.Loft.CanSetPeriodic`

Узнать можно ли установить параметр периодичности

### `CanSetProfileFacesG2Condition(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.CanSetProfileFacesG2Condition(System.Int32)`

Узнать можно ли установить параметр взятия 2-й производной с граней

Parameters:
- `profileIndex`: Индекс профиля

### `ConvertAutomaticCouplingPoints`

ID: `M:TFlex.Model.Model3D.Loft.ConvertAutomaticCouplingPoints`

Конвертировать автоматические точки соответствия в типы PointVertex и PointEdge

Remarks: После конвертации автоматических точек соответствия параметр установки автоматических точек соответствия сбрасывается

### `GetCouplingPoint(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetCouplingPoint(System.Int32,System.Int32)`

Задать точку соответствия

Parameters:
- `couplingIndex`: Индекс последовательности точек соответствия
- `profileIndex`: Индекс точки в последовательности точек соответствия.

Returns: Точка лежащая на соответствующем профиле

### `GetCouplingPointVectorCondition(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetCouplingPointVectorCondition(System.Int32,System.Int32)`

Получить векторное условие на направляющей

Parameters:
- `couplingIndex`: Индекс направляющей (начинается с нуля)
- `profileIndex`: Номер профиля (начинается с нуля)

Returns: Векторное условие

### `GetGuideContour(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideContour(System.Int32,System.Int32)`

Возвращает контур направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)
- `contourIndex`: Номер контура направляющей (начинается с 0)

### `GetGuideContourCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideContourCount(System.Int32)`

Возвращает число контуров направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)

Returns: Число контуров в профиле

### `GetGuideFaceCondition(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideFaceCondition(System.Int32,System.Int32)`

Получить условие касания с гранью

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)
- `guideFaceConditionIndex`: Индекс грани задающей каксательное условие

Returns: Граничное условие

### `GetGuideFaceConditionCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideFaceConditionCount(System.Int32)`

Получить число условий касаний с гранью

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)

Returns: Вектора заданный в точке

### `GetGuideReverse(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideReverse(System.Int32)`

Возвращает реверс направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)

Returns: Параметр реверса данной направляющей

### `GetGuideVectorCondition(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideVectorCondition(System.Int32,System.Int32)`

Получить векторное условие на направляющей

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)
- `guideVectorConditionIndex`: Номер векторного граничного условия

### `GetGuideVectorConditionCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideVectorConditionCount(System.Int32)`

Получить число векторных условий

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)

Returns: Число векторных условий

### `GetGuideVectorScaleFlag(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetGuideVectorScaleFlag(System.Int32)`

Возвращает параметр интерпретации коэффициента касательного вектора

Parameters:
- `guideIndex`: Номер направляющей параметр которой возвращается

Remarks: Если параметр не установлен (по умолчанию), то коэффициент интерпретируется как длина вектора, если параметр установлен то коэффициент интерпретируется как масштабный коэффициент

### `GetProfileContour(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileContour(System.Int32,System.Int32)`

Возвращает контур профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)
- `contourIndex`: Номер контура профиля (начинается с 0)

Returns: Контур профиля

### `GetProfileContourCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileContourCount(System.Int32)`

Возвращает число контуров профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)

Returns: Число контуров в профиле

### `GetProfileFaceCondition(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileFaceCondition(System.Int32,System.Int32)`

Получить условие касания с гранью

Parameters:
- `profileIndex`: Индекс профиля
- `profileFaceConditionIndex`: Индекс профиля

Returns: Граничное условие

### `GetProfileFaceConditionCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileFaceConditionCount(System.Int32)`

Получить число условий касаний с гранью

Parameters:
- `profileIndex`: Индекс профиля

Returns: Вектора заданный в точке

### `GetProfileFacesG2Condition(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileFacesG2Condition(System.Int32)`

Получить условие взятия 2-й производной с граней

Parameters:
- `profileIndex`: Индекс профиля

### `GetProfileReverse(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileReverse(System.Int32)`

Возвращает реверс профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)

Returns: Параметр реверса

### `GetProfileVectorCondition(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileVectorCondition(System.Int32,System.Int32)`

Получить векторное условие на профиле

Parameters:
- `profileIndex`: Индекс профиля (начинается нуля)
- `profileVectorConditionIndex`: Номер векторного граничного условия (начинается нуля)

Returns: Векторное условие на профиле

### `GetProfileVectorConditionCount(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileVectorConditionCount(System.Int32)`

Получить число векторных условий

Parameters:
- `profileIndex`: Индекс профиля

Returns: Число векторных условий заданных для профиля

### `GetProfileVectorScaleFlag(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.GetProfileVectorScaleFlag(System.Int32)`

Возвращает параметр интерпретации коэффициента касательного вектора

Parameters:
- `profileIndex`: Номер профиля для которого задаётся параметр

Remarks: Если параметр не установлен (по умолчанию), то коэффициент интерпретируется как длина вектора, если параметр установлен то коэффициент интерпретируется как масштабный коэффициент

### `InsertCoupling(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.InsertCoupling(System.Int32)`

Вставить последовательность точек соответсвия

Parameters:
- `couplingIndex`: Индекс последовательности точек соответствия

Remarks: Последовательность точек соответствия проходит через все невырожденные профили. Всегда существует последовательность точек соответствия с нулевым индексом, включающая стартовые точки по умолчанию со всех невырожденных профилей.

### `InsertGuide(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.InsertGuide(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Вставить направляющую в список направляющих

Parameters:
- `guideIndex`: Номер добавляемой направляющей (начинается с 0)

Remarks: После добавления направляющей её нужно наполнить контурами с помощью функции AddGuideContour

### `InsertProfile(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

ID: `M:TFlex.Model.Model3D.Loft.InsertProfile(System.Int32,TFlex.Model.Model3D.Geometry.ModelContour)`

Вставить профиль в список профилей

Parameters:
- `profileIndex`: Номер добавляемого профиля (начинается с 0)

Remarks: После добавления профиля его нужно наполнить контурами с помощью функции AddProfileContour. Операция Лофтинга должна иметь как минимум один невырожденный профиль заданный с помощью контуров

### `IsAutomaticCouplingPointsSet`

ID: `M:TFlex.Model.Model3D.Loft.IsAutomaticCouplingPointsSet`

Получить параметр автоматических точек соответствия

### `RemoveAllCouplingPointVectors(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllCouplingPointVectors(System.Int32)`

Удаляет все векторные условия в точках соответствия

### `RemoveAllGuideContours(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllGuideContours(System.Int32)`

Удалить все контуры направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)

Remarks: После вызова данной функции направляющая становится пустой

### `RemoveAllGuideFaceConditions(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllGuideFaceConditions(System.Int32)`

Удаляет все условия касания с гранью

Parameters:
- `guideIndex`: Индекс направляющей (начинается с нуля)

### `RemoveAllGuideVectorConditions(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllGuideVectorConditions(System.Int32)`

Удаляет все векторные условия

Parameters:
- `guideIndex`: Индекс направляющей

### `RemoveAllProfileContours(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllProfileContours(System.Int32)`

Удалить все контуры профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)

Remarks: После вызова данной функции профиль становится пустым

### `RemoveAllProfileFaceConditions(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllProfileFaceConditions(System.Int32)`

Удаляет все условия касания с гранью

Parameters:
- `profileIndex`: Индекс профиля

### `RemoveAllProfileVectorConditions(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveAllProfileVectorConditions(System.Int32)`

Удаляет все векторные условия

Parameters:
- `profileIndex`: Индекс профиля (начинается нуля)

### `RemoveCoupling(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveCoupling(System.Int32)`

Удалить последовательность точек соответсвия

Parameters:
- `couplingIndex`: Индекс последовательности точек соответствия

Remarks: Для 0-го соответствия (couplingIndex=0) эта операция интерпретируется как удаление стартовых точек соответствия (они заменяются на стартовые точки по умолчанию), само соответствие не удаляется

### `RemoveGuide(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveGuide(System.Int32)`

Удалить направляющую из списка направляющих

Parameters:
- `guideIndex`: Номер удаляемой направляющей (начинается с 0)

### `RemoveGuideContour(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveGuideContour(System.Int32,System.Int32)`

Удалить контур направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)
- `contourIndex`: Номер удаляемого контура (начинается с 0)

### `RemoveProfile(System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveProfile(System.Int32)`

Удалить профиль из списка профилей

Parameters:
- `profileIndex`: Номер удаляемого профиля (начинается с 0)

### `RemoveProfileContour(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.RemoveProfileContour(System.Int32,System.Int32)`

Удалить контур профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)
- `contourIndex`: Номер удаляемого контура (начинается с 0)

### `ResetCouplingPoint(System.Int32,System.Int32)`

ID: `M:TFlex.Model.Model3D.Loft.ResetCouplingPoint(System.Int32,System.Int32)`

Задать точку соответствия

Parameters:
- `couplingIndex`: Индекс последовательности точек соответствия
- `profileIndex`: Индекс точки в последовательности точек соответствия.

### `SetAutomaticCouplingPoint`

ID: `M:TFlex.Model.Model3D.Loft.SetAutomaticCouplingPoint`

Установить автоматические точки соответствия

Remarks: Автоматические точки соответствия позволяют автоматизировать задание точек для простых профилей, для сложных профилей данную опцию использовать не рекомендуется. Опция по умолчанию отключена. Автоматические точки соответствия вычисляются каждый при изменении профилей и зависят от установленных флагов реверса профилей.

### `SetCouplingPoint(System.Int32,System.Int32,TFlex.Model.Model3D.Loft.PointOnContour)`

ID: `M:TFlex.Model.Model3D.Loft.SetCouplingPoint(System.Int32,System.Int32,TFlex.Model.Model3D.Loft.PointOnContour)`

Задать точку соответствия

Parameters:
- `couplingIndex`: Индекс последовательности точек соответствия
- `profileIndex`: Индекс точки в последовательности точек соответствия
- `point`: Точка лежащая на соответствующем профиле

### `SetCouplingPointVector(System.Int32,System.Int32,TFlex.Model.Model3D.Loft.VectorDirection)`

ID: `M:TFlex.Model.Model3D.Loft.SetCouplingPointVector(System.Int32,System.Int32,TFlex.Model.Model3D.Loft.VectorDirection)`

Задать векторное условие в точке соответствия

Parameters:
- `couplingIndex`: Индекс соответствия (начинается с нуля)
- `profileIndex`: Номер профиля (начинается с нуля)
- `condition`: Векторное граничное условие

Remarks: Векторные граничные условия не могут быть заданы, если для указанного профиля задан другой тип граничного условия

### `SetGuideReverse(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Loft.SetGuideReverse(System.Int32,System.Boolean)`

Установить реверс направляющей

Parameters:
- `guideIndex`: Номер направляющей (начинается с 0)
- `reverse`: Параметр реверса для данной направляющей

### `SetGuideVectorScaleFlag(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Loft.SetGuideVectorScaleFlag(System.Int32,System.Boolean)`

Устанавливает параметр использования коэффициента касательного вектора как масштабного

Parameters:
- `guideIndex`: Номер направляющей реверс которого возвращается
- `scale`: true - интерпретировать значение как масштабный коэффициент, false - интерпретировать значение как длину

Remarks: По умолчанию параметр отключен

### `SetProfileFacesG2Condition(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Loft.SetProfileFacesG2Condition(System.Int32,System.Boolean)`

Установить условие взятия 2-й производной с граней

Parameters:
- `profileIndex`: Индекс профиля
- `g2`: 

### `SetProfileReverse(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Loft.SetProfileReverse(System.Int32,System.Boolean)`

Установить реверс профиля

Parameters:
- `profileIndex`: Номер профиля (начинается с 0)
- `reverse`: Параметр реверса

### `SetProfileVectorScaleFlag(System.Int32,System.Boolean)`

ID: `M:TFlex.Model.Model3D.Loft.SetProfileVectorScaleFlag(System.Int32,System.Boolean)`

Устанавливает параметр использования коэффициента касательного вектора как масштабного

Parameters:
- `profileIndex`: Номер профиля реверс которого возвращается
- `scaleFlag`: true - интерпретирвать значение как масштабный коэффициент false - интерпретировать значение как длину

Remarks: По умолчанию параметр отключен

## Propertys

### `FirstDegenerateProfile`

ID: `P:TFlex.Model.Model3D.Loft.FirstDegenerateProfile`

Первый вырожденный профиль

Remarks: Вырожденный профиль представляет из себя точку

### `FirstDegenerateProfileCondition`

ID: `P:TFlex.Model.Model3D.Loft.FirstDegenerateProfileCondition`

Граничное условие для первого вырожденного профиля, значение может быть равно 0

### `FirstEndProfileCondition`

ID: `P:TFlex.Model.Model3D.Loft.FirstEndProfileCondition`

Cпециальное граничное условие для первого профиля, condition может быть равно 0

Remarks: Граниное условие для профиля может быть установлено, если: Не задан первый вырожденный профиль. Для профиля не задано векторное условие или условие касания с гранью. Лофт не является периодическим.

### `GroupType`

ID: `P:TFlex.Model.Model3D.Loft.GroupType`

Получить тип объекта

### `GuideAutoReverse`

ID: `P:TFlex.Model.Model3D.Loft.GuideAutoReverse`

Автореверс для направляющих

Remarks: По умолчанию автореверс включен. Автореверс имеет смысл только для замкнутых направляющих

### `GuideCount`

ID: `P:TFlex.Model.Model3D.Loft.GuideCount`

Получить число направляющих

### `KeepInitialSplitting`

ID: `P:TFlex.Model.Model3D.Loft.KeepInitialSplitting`

Сохранять исходное разбиение

### `LastDegenerateProfile`

ID: `P:TFlex.Model.Model3D.Loft.LastDegenerateProfile`

Последний вырожденный профиль

Remarks: Вырожденный профиль представляет из себя точку

### `LastDegenerateProfileCondition`

ID: `P:TFlex.Model.Model3D.Loft.LastDegenerateProfileCondition`

Граничное условие для последнего вырожденного профиля, значение может быть равно 0

### `LastEndProfileCondition`

ID: `P:TFlex.Model.Model3D.Loft.LastEndProfileCondition`

Специальное граничное условие для последнего профиля, condition может быть равно 0

Remarks: Граниное условие для профиля может быть установлено, если: Не задан первый вырожденный профиль. Для профиля не задано векторное условие или условие касания с гранью. Лофт не является периодическим.

### `Linear`

ID: `P:TFlex.Model.Model3D.Loft.Linear`

Линейчатая поверхность

### `Path`

ID: `P:TFlex.Model.Model3D.Loft.Path`

Путь

Remarks: Путь не может бть установлен, если задана направляющая

### `Periodic`

ID: `P:TFlex.Model.Model3D.Loft.Periodic`

Периодическое построение лофтинга

Remarks: Данная опция не может быть использована, если задан вырожденный профиль, или если задано граничное условие специфичное для первого или последнего профиля

### `ProfileAutoReverse`

ID: `P:TFlex.Model.Model3D.Loft.ProfileAutoReverse`

Автореверс для профилей

Remarks: По умолчанию автореверс включен. Автореверс имеет смысл только для замкнутых профилей.

### `ProfileCount`

ID: `P:TFlex.Model.Model3D.Loft.ProfileCount`

Получить число профилей

### `ThinWall`

ID: `P:TFlex.Model.Model3D.Loft.ThinWall`

Тонкостенное построение

Remarks: Если в качестве первого и/или последнего профиля выбрано листовое тело, то данная опция позволяет построить Лофтинг без граней соответствующих первому и последнему профилю, используя только их контуры. Данная опция не может быть использована, если задано периодическое построение

### `Tolerance`

ID: `P:TFlex.Model.Model3D.Loft.Tolerance`

Точность

Remarks: Для успешного посроения Лофтинга необходимо чтобы расстояние между профилями и направляющими было меньше значения точности, и чтобы расстояния между вершинами контуров было меньше 10 значений точности. Точность должна быть положительным числом, по умолчанию точность равна 1E-5. В том случае если операция не складывается, можно попробовать увеличить или уменьшить значение точности в 10 раз.
