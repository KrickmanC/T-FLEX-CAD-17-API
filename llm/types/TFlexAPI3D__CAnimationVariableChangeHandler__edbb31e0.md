# CAnimationVariableChangeHandler

Assembly: `TFlexAPI3D`

## Summary

Implements a call back, which is called by Animation API when the value of an animation variable changes.

## Remarks

This event handler is created and passed to IUIAnimationVariable::SetVariableChangeHandler method, when you call CAnimationVariable::EnableValueChangedEvent or CAnimationBaseObject::EnableValueChangedEvent (which enables this event for all animation variables encapsulated in an animation object).

## Constructors

### `CAnimationVariableChangeHandler`

ID: `M:CAnimationVariableChangeHandler.#ctor`

Constructs a CAnimationVariableChangeHandler object.

## Methods

### `CAnimationVariableChangeHandler`

ID: `M:CAnimationVariableChangeHandler.#ctor`

Constructs a CAnimationVariableChangeHandler object.

### `CreateInstance(CAnimationController*,IUIAnimationVariableChangeHandler**)`

ID: `M:CAnimationVariableChangeHandler.CreateInstance(CAnimationController*,IUIAnimationVariableChangeHandler**)`

Creates an instance of CAnimationVariableChangeHandler object.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
- `ppHandler`: Output. If the method succeeds it contains a pointer to COM object that will handle variable change events.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `OnValueChanged(IUIAnimationStoryboard*,IUIAnimationVariable*,System.Double,System.Double)`

ID: `M:CAnimationVariableChangeHandler.OnValueChanged(IUIAnimationStoryboard*,IUIAnimationVariable*,System.Double,System.Double)`

Called when a value of an animation variable has changed.

Parameters:
- `storyboard`: The storyboard that is animating the variable.
- `variable`: The animation variable that was updated.
- `newValue`: The new value.
- `previousValue`: The previous value.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `SetAnimationController(CAnimationController*)`

ID: `M:CAnimationVariableChangeHandler.SetAnimationController(CAnimationController*)`

Stores a pointer to animation controller to route events.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
