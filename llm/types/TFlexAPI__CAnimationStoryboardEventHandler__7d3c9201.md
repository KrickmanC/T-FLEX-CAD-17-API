# CAnimationStoryboardEventHandler

Assembly: `TFlexAPI`

## Summary

Implements a callback, which is called by Animation API when storyboard's status is changed or storyboard is updated.

## Remarks

This event handler is created and passed to IUIAnimationStoryboard::SetStoryboardEventHandler method, when you call CAnimationController::EnableStoryboardEventHandler.

## Constructors

### `CAnimationStoryboardEventHandler`

ID: `M:CAnimationStoryboardEventHandler.#ctor`

Constructs a CAnimationStoryboardEventHandler object.

## Methods

### `CAnimationStoryboardEventHandler`

ID: `M:CAnimationStoryboardEventHandler.#ctor`

Constructs a CAnimationStoryboardEventHandler object.

### `CreateInstance(CAnimationController*,IUIAnimationStoryboardEventHandler**)`

ID: `M:CAnimationStoryboardEventHandler.CreateInstance(CAnimationController*,IUIAnimationStoryboardEventHandler**)`

Creates an instance of CAnimationStoryboardEventHandler callback.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
- `ppHandler`: Output. If the method succeeds it contains a pointer to COM object that will handle storyboard events.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `OnStoryboardStatusChanged(IUIAnimationStoryboard*,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001)`

ID: `M:CAnimationStoryboardEventHandler.OnStoryboardStatusChanged(IUIAnimationStoryboard*,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001,__MIDL___MIDL_itf_UIAnimation_0000_0002_0001)`

Handles OnStoryboardStatusChanged events, which occur when a storyboard's status changes

Parameters:
- `storyboard`: A pointer to storyboard whose status has changed.
- `newStatus`: Specifies new storyboard status.
- `previousStatus`: Specifies previous storyboard status.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `OnStoryboardUpdated(IUIAnimationStoryboard*)`

ID: `M:CAnimationStoryboardEventHandler.OnStoryboardUpdated(IUIAnimationStoryboard*)`

Handles OnStoryboardUpdated events, which occur when a storyboard is updated

Parameters:
- `storyboard`: A pointer to storyboard, which was updated.

Returns: S_OK if the method succeeds; otherwise E_FAIL.

### `SetAnimationController(CAnimationController*)`

ID: `M:CAnimationStoryboardEventHandler.SetAnimationController(CAnimationController*)`

Stores a pointer to animation controller to route events.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
