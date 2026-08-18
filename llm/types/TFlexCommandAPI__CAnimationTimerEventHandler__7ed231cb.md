# CAnimationTimerEventHandler

Assembly: `TFlexCommandAPI`

## Summary

Implements a call back, which is called by Animation API when timing events occur.

## Remarks

This event handler is created and passed to IUIAnimationTimer::SetTimerEventHandler when you call CAnimationController::EnableAnimationTimerEventHandler.

## Methods

### `CreateInstance(CAnimationController*,IUIAnimationTimerEventHandler**)`

ID: `M:CAnimationTimerEventHandler.CreateInstance(CAnimationController*,IUIAnimationTimerEventHandler**)`

Creates an instance of CAnimationTimerEventHandler callback.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
- `ppTimerEventHandler`: Output. If the method succeeds it contains a pointer to COM object that will handle animation timer events.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `OnPostUpdate`

ID: `M:CAnimationTimerEventHandler.OnPostUpdate`

Handles events that occur after an animation update is finished.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `OnPreUpdate`

ID: `M:CAnimationTimerEventHandler.OnPreUpdate`

Handles events that occur before an animation update begins.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `OnRenderingTooSlow(System.UInt32)`

ID: `M:CAnimationTimerEventHandler.OnRenderingTooSlow(System.UInt32)`

Handles events that occur when the rendering frame rate for an animation falls below the minimum desirable frame rate.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `SetAnimationController(CAnimationController*)`

ID: `M:CAnimationTimerEventHandler.SetAnimationController(CAnimationController*)`

Stores a pointer to animation controller to route events.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
