# TFlex.Model.Model3D.Visual.DecorationContainer

Assembly: `TFlexAPI3D`
Namespace: `TFlex.Model.Model3D.Visual`

## Summary

Контейнер декораций

## Remarks

Позволяет группировать несколько декораций Не допускается модифицировать контейнер декораций, который был получен от системы, а не создан явным образом.

## Constructors

### `DecorationContainer(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.#ctor(System.String)`

Parameters:
- `name`: Имя должно быть уникальным

## Methods

### `DecorationContainer(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.#ctor(System.String)`

Parameters:
- `name`: Имя должно быть уникальным

### `AddDecoration(TFlex.Model.Model3D.Visual.Decoration)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.AddDecoration(TFlex.Model.Model3D.Visual.Decoration)`

Добавление декорации

### `GetDecoration(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.GetDecoration(System.String)`

Поиск декорации

### `GetEnumerator`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.GetEnumerator`

Реализация интерфейса IEnumerable

### `IsEmpty`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.IsEmpty`

Проверка пустоты

### `RemoveAllDecorations`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.RemoveAllDecorations`

Удаление всех декораций

### `RemoveDecoration(System.String)`

ID: `M:TFlex.Model.Model3D.Visual.DecorationContainer.RemoveDecoration(System.String)`

Удаление декорации
