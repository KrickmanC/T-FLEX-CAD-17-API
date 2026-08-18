# TFlex.Model.IModelObjectWithLayer

Assembly: `TFlexAPI`
Namespace: `TFlex.Model`

## Summary

Интерфейс объекта документа T-FLEX CAD, обладающего слоем

## Propertys

### `Layer`

ID: `P:TFlex.Model.IModelObjectWithLayer.Layer`

Слой, на котором размещается объект

Examples:
- `public static void SetLayer(Object ob) { Document document = TFlex.Application.ActiveDocument;//Получение активного документа document.BeginChanges("");//Открытие блока изменений документа Layer l = new Layer(document); l.Monochrome = true;//Параметр слоя "одноцветный" l.Color = 12;//цвет ob.Layer = l;//установка слоя document.EndChanges();//Закрытие блока изменений документа }`
