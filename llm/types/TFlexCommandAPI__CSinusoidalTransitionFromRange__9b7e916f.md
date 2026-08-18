# CSinusoidalTransitionFromRange

Assembly: `TFlexCommandAPI`

## Summary

Encapsulates a sinusoidal-range transition, with a given range of oscillation.

## Remarks

The value of the animation variable fluctuates between the specified minimum and maximum values over the entire duration of a sinusoidal-range transition. The slope parameter is used to disambiguate between the two possible sine waves specified by the other parameters. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CSinusoidalTransitionFromRange(System.Double,System.Double,System.Double,System.Double,__MIDL___MIDL_itf_UIAnimation_0000_0009_0001)`

ID: `M:CSinusoidalTransitionFromRange.#ctor(System.Double,System.Double,System.Double,System.Double,__MIDL___MIDL_itf_UIAnimation_0000_0009_0001)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `dblMinimumValue`: The value of the animation variable at a trough of the sinusoidal wave.
- `dblMaximumValue`: The value of the animation variable at a peak of the sinusoidal wave.
- `period`: The period of oscillation of the sinusoidal wave in seconds.
- `slope`: The slope at the start of the transition.

## Methods

### `CSinusoidalTransitionFromRange(System.Double,System.Double,System.Double,System.Double,__MIDL___MIDL_itf_UIAnimation_0000_0009_0001)`

ID: `M:CSinusoidalTransitionFromRange.#ctor(System.Double,System.Double,System.Double,System.Double,__MIDL___MIDL_itf_UIAnimation_0000_0009_0001)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `dblMinimumValue`: The value of the animation variable at a trough of the sinusoidal wave.
- `dblMaximumValue`: The value of the animation variable at a peak of the sinusoidal wave.
- `period`: The period of oscillation of the sinusoidal wave in seconds.
- `slope`: The slope at the start of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CSinusoidalTransitionFromRange.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblMaximumValue`

ID: `F:CSinusoidalTransitionFromRange.m_dblMaximumValue`

The value of the animation variable at a peak of the sinusoidal wave.

### `m_dblMinimumValue`

ID: `F:CSinusoidalTransitionFromRange.m_dblMinimumValue`

The value of the animation variable at a trough of the sinusoidal wave.

### `m_duration`

ID: `F:CSinusoidalTransitionFromRange.m_duration`

The duration of the transition.

### `m_period`

ID: `F:CSinusoidalTransitionFromRange.m_period`

The period of oscillation of the sinusoidal wave in seconds.

### `m_slope`

ID: `F:CSinusoidalTransitionFromRange.m_slope`

The slope at the start of the transition.
