# CInterpolatorBase

Assembly: `TFlexAPI3D`

## Summary

Implements a callback, which is called by Animation API when it needs to calculate a new value of animation variable.

## Remarks

This handler is created and passed to IUIAnimationTransitionFactory::CreateTransition when a CCustomTransition object is being created as a part of animation initialization process (started by CAnimationController::AnimateGroup). Usually you don't need to use this class directly, it just routs all events to a CCustomInterpolator-derived class, whose pointer is passed to constructor of CCustomTransition.

## Constructors

### `CInterpolatorBase`

ID: `M:CInterpolatorBase.#ctor`

Constructs the CInterpolatorBase object.

## Methods

### `CInterpolatorBase`

ID: `M:CInterpolatorBase.#ctor`

Constructs the CInterpolatorBase object.

### `CreateInstance(CCustomInterpolator*,IUIAnimationInterpolator**)`

ID: `M:CInterpolatorBase.CreateInstance(CCustomInterpolator*,IUIAnimationInterpolator**)`

Creates an instance of CInterpolatorBase and stores a pointer to custom interpolator, which will be handling events.

Parameters:
- `pInterpolator`: A pointer to custom interpolator.
- `ppHandler`: Output. Contains a pointer to instance of CInterpolatorBase when the function returns.

### `GetDependencies(__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*)`

ID: `M:CInterpolatorBase.GetDependencies(__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*)`

Gets the interpolator's dependencies.

Parameters:
- `initialValueDependencies`: Output. Aspects of the interpolator that depend on the initial value passed to SetInitialValueAndVelocity.
- `initialVelocityDependencies`: Output. Aspects of the interpolator that depend on the initial velocity passed to SetInitialValueAndVelocity.
- `durationDependencies`: Output. Aspects of the interpolator that depend on the duration passed to SetDuration.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the GetDependencies method.

### `GetDuration(System.Double*)`

ID: `M:CInterpolatorBase.GetDuration(System.Double*)`

Gets the interpolator's duration.

Parameters:
- `duration`: Output. The duration of the transition, in seconds.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the GetDuration method.

### `GetFinalValue(System.Double*)`

ID: `M:CInterpolatorBase.GetFinalValue(System.Double*)`

Gets the final value to which the interpolator leads.

Parameters:
- `value`: Output. The final value of a variable at the end of the transition.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the GetFinalValue method.

### `InterpolateValue(System.Double,System.Double*)`

ID: `M:CInterpolatorBase.InterpolateValue(System.Double,System.Double*)`

Interpolates the value at a given offset

Parameters:
- `offset`: The offset from the start of the transition. The offset is always greater than or equal to zero and less than the duration of the transition. This method is not called if the duration of the transition is zero.
- `value`: Output. The interpolated value.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the InterpolateValue method.

### `InterpolateVelocity(System.Double,System.Double*)`

ID: `M:CInterpolatorBase.InterpolateVelocity(System.Double,System.Double*)`

Interpolates the velocity at a given offset

Parameters:
- `offset`: The offset from the start of the transition. The offset is always greater than or equal to zero and less than or equal to the duration of the transition. This method is not called if the duration of the transition is zero.
- `velocity`: Output. The velocity of the variable at the offset.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the InterpolateVelocity method.

### `SetCustomInterpolator(CCustomInterpolator*)`

ID: `M:CInterpolatorBase.SetCustomInterpolator(CCustomInterpolator*)`

Stores a pointer to custom interpolator, which will be handling events.

Parameters:
- `pInterpolator`: A pointer to custom interpolator.

### `SetDuration(System.Double)`

ID: `M:CInterpolatorBase.SetDuration(System.Double)`

Sets the interpolator's duration

Parameters:
- `duration`: The duration of the transition.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the SetDuration method.

### `SetInitialValueAndVelocity(System.Double,System.Double)`

ID: `M:CInterpolatorBase.SetInitialValueAndVelocity(System.Double,System.Double)`

Sets the interpolator's initial value and velocity.

Parameters:
- `initialValue`: The value of the variable at the start of the transition.
- `initialVelocity`: The velocity of the variable at the start of the transition.

Returns: If the method succeeds, it returns S_OK. It returns E_FAIL if CCustomInterpolator is not set, or custom implementation returns FALSE from the SetInitialValueAndVelocity method.
