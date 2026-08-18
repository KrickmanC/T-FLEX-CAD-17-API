# CAnimationVariableIntegerChangeHandler

Assembly: `TFlexCommandAPI`

## Summary

Implements a call back, which is called by Animation API when the value of an animation variable changes.

## Remarks

This event handler is created and passed to IUIAnimationVariable::SetVariableIntegerChangeHandler method, when you call CAnimationVariable::EnableIntegerValueChangedEvent or CAnimationBaseObject::EnableIntegerValueChangedEvent (which enables this event for all animation variables encapsulated in an animation object).

## Constructors

### `CAnimationVariableIntegerChangeHandler`

ID: `M:CAnimationVariableIntegerChangeHandler.#ctor`

Constructs a CAnimationVariableIntegerChangeHandler object.

## Methods

### `CAnimationVariableIntegerChangeHandler`

ID: `M:CAnimationVariableIntegerChangeHandler.#ctor`

Constructs a CAnimationVariableIntegerChangeHandler object.

### `CreateInstance(CAnimationController*,IUIAnimationVariableIntegerChangeHandler**)`

ID: `M:CAnimationVariableIntegerChangeHandler.CreateInstance(CAnimationController*,IUIAnimationVariableIntegerChangeHandler**)`

Creates an instance of CAnimationVariableIntegerChangeHandler callback.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
- `ppHandler`: Output. If the method succeeds it contains a pointer to COM object that will handle variable integer change events.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `OnIntegerValueChanged(IUIAnimationStoryboard*,IUIAnimationVariable*,System.Int32,System.Int32)`

ID: `M:CAnimationVariableIntegerChangeHandler.OnIntegerValueChanged(IUIAnimationStoryboard*,IUIAnimationVariable*,System.Int32,System.Int32)`

Called when a value of an animation variable has changed.

Parameters:
- `storyboard`: The storyboard that is animating the variable.
- `variable`: The animation variable that was updated.
- `newValue`: The new rounded value.
- `previousValue`: The previous rounded value.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `SetAnimationController(CAnimationController*)`

ID: `M:CAnimationVariableIntegerChangeHandler.SetAnimationController(CAnimationController*)`

Stores a pointer to animation controller to route events.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
