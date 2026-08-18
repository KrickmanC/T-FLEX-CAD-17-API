# CCustomInterpolator

Assembly: `TFlexAPI3D`

## Summary

Implements a basic interpolator.

## Remarks

Derive a class from CCustomInterpolator and override all necessary methods in order to implement a custom interpolation algorithm. A pointer to this class should be passed as a parameter to CCustomTransition.

## Constructors

### `CCustomInterpolator`

ID: `M:CCustomInterpolator.#ctor`

Constructs a custom interpolator object and sets all values to default 0.

Remarks: Use CCustomInterpolator::Init to initialize duration and final value later in the code.

### `CCustomInterpolator(System.Double,System.Double)`

ID: `M:CCustomInterpolator.#ctor(System.Double,System.Double)`

Constructs a custom interpolator object and initializes duration and velocity to specified values.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: 

## Methods

### `CCustomInterpolator`

ID: `M:CCustomInterpolator.#ctor`

Constructs a custom interpolator object and sets all values to default 0.

Remarks: Use CCustomInterpolator::Init to initialize duration and final value later in the code.

### `CCustomInterpolator(System.Double,System.Double)`

ID: `M:CCustomInterpolator.#ctor(System.Double,System.Double)`

Constructs a custom interpolator object and initializes duration and velocity to specified values.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: 

### `GetDependencies(__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*)`

ID: `M:CCustomInterpolator.GetDependencies(__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*,__MIDL___MIDL_itf_UIAnimation_0000_0010_0001*)`

Gets the interpolator's dependencies.

Parameters:
- `initialValueDependencies`: Output. Aspects of the interpolator that depend on the initial value passed to SetInitialValueAndVelocity.
- `initialVelocityDependencies`: Output. Aspects of the interpolator that depend on the initial velocity passed to SetInitialValueAndVelocity.
- `durationDependencies`: Output. Aspects of the interpolator that depend on the duration passed to SetDuration.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `GetDuration(System.Double*)`

ID: `M:CCustomInterpolator.GetDuration(System.Double*)`

Gets the interpolator's duration.

Parameters:
- `duration`: Output. The duration of the transition, in seconds.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `GetFinalValue(System.Double*)`

ID: `M:CCustomInterpolator.GetFinalValue(System.Double*)`

Gets the final value to which the interpolator leads.

Parameters:
- `value`: Output. The final value of a variable at the end of the transition.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `Init(System.Double,System.Double)`

ID: `M:CCustomInterpolator.Init(System.Double,System.Double)`

Initializes duration and final value.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: The final value of a variable at the end of the transition.

### `InterpolateValue(System.Double,System.Double*)`

ID: `M:CCustomInterpolator.InterpolateValue(System.Double,System.Double*)`

Interpolates the value at a given offset.

Parameters:
- `offset`: The offset from the start of the transition. The offset is always greater than or equal to zero and less than the duration of the transition. This method is not called if the duration of the transition is zero.
- `value`: Output. The interpolated value.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `InterpolateVelocity(System.Double,System.Double*)`

ID: `M:CCustomInterpolator.InterpolateVelocity(System.Double,System.Double*)`

Interpolates the velocity at a given offset

Parameters:
- `offset`: The offset from the start of the transition. The offset is always greater than or equal to zero and less than or equal to the duration of the transition. This method is not called if the duration of the transition is zero.
- `velocity`: Output. The velocity of the variable at the offset.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `SetDuration(System.Double)`

ID: `M:CCustomInterpolator.SetDuration(System.Double)`

Sets the interpolator's duration.

Parameters:
- `duration`: The duration of the transition.

Returns: Basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

### `SetInitialValueAndVelocity(System.Double,System.Double)`

ID: `M:CCustomInterpolator.SetInitialValueAndVelocity(System.Double,System.Double)`

Sets the interpolator's initial value and velocity.

Parameters:
- `initialValue`: The value of the variable at the start of the transition.
- `initialVelocity`: The velocity of the variable at the start of the transition.

Returns: The basic implementation always returns TRUE. Return FALSE from overridden implementation if you wish to fail the event.

## Fields

### `m_currentValue`

ID: `F:CCustomInterpolator.m_currentValue`

The interpolated value.

### `m_currentVelocity`

ID: `F:CCustomInterpolator.m_currentVelocity`

The interpolated velocity.

### `m_duration`

ID: `F:CCustomInterpolator.m_duration`

The duration of the transition.

### `m_finalValue`

ID: `F:CCustomInterpolator.m_finalValue`

The final value of a variable at the end of the transition.

### `m_initialValue`

ID: `F:CCustomInterpolator.m_initialValue`

The value of the variable at the start of the transition.

### `m_initialVelocity`

ID: `F:CCustomInterpolator.m_initialVelocity`

The velocity of the variable at the start of the transition.
