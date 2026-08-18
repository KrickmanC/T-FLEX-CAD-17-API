# CAnimationManagerEventHandler

Assembly: `TFlexAPI`

## Summary

Implements a callback, which is called by Animation API when a status of animation manager changed.

## Remarks

This event handler is created and passed to IUIAnimationManager::SetManagerEventHandler method, when you call CAnimationController::EnableAnimationManagerEvent.

## Constructors

### `CAnimationManagerEventHandler`

ID: `M:CAnimationManagerEventHandler.#ctor`

Constructs a CAnimationManagerEventHandler object.

## Methods

### `CAnimationManagerEventHandler`

ID: `M:CAnimationManagerEventHandler.#ctor`

Constructs a CAnimationManagerEventHandler object.

### `CreateInstance(CAnimationController*,IUIAnimationManagerEventHandler**)`

ID: `M:CAnimationManagerEventHandler.CreateInstance(CAnimationController*,IUIAnimationManagerEventHandler**)`

Creates an instance of CAnimationManagerEventHandler object.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
- `ppManagerEventHandler`: Output. If the method succeeds it contains a pointer to COM object that will handle status updates to an animation manager.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `OnManagerStatusChanged(__MIDL___MIDL_itf_UIAnimation_0000_0000_0002,__MIDL___MIDL_itf_UIAnimation_0000_0000_0002)`

ID: `M:CAnimationManagerEventHandler.OnManagerStatusChanged(__MIDL___MIDL_itf_UIAnimation_0000_0000_0002,__MIDL___MIDL_itf_UIAnimation_0000_0000_0002)`

Called when a status of animation manager has changed.

Parameters:
- `newStatus`: New status.
- `previousStatus`: Previous status.

Returns: Current implementation always returns S_OK;

### `SetAnimationController(CAnimationController*)`

ID: `M:CAnimationManagerEventHandler.SetAnimationController(CAnimationController*)`

Stores a pointer to animation controller to route events.

Parameters:
- `pAnimationController`: A pointer to animation controller, which will receive events.
