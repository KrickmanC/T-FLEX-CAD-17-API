# CSinusoidalTransitionFromVelocity

Assembly: `TFlexCommandAPI`

## Summary

Encapsulates a sinusoidal-velocity transition, with an amplitude determined by the animation variable's initial velocity..

## Remarks

The value of the animation variable oscillates around the initial value over the entire duration of a sinusoidal-range transition. The amplitude of the oscillation is determined by the animation variable's velocity when the transition begins. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CSinusoidalTransitionFromVelocity(System.Double,System.Double)`

ID: `M:CSinusoidalTransitionFromVelocity.#ctor(System.Double,System.Double)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `period`: The period of oscillation of the sinusoidal wave in seconds.

## Methods

### `CSinusoidalTransitionFromVelocity(System.Double,System.Double)`

ID: `M:CSinusoidalTransitionFromVelocity.#ctor(System.Double,System.Double)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `period`: The period of oscillation of the sinusoidal wave in seconds.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CSinusoidalTransitionFromVelocity.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_duration`

ID: `F:CSinusoidalTransitionFromVelocity.m_duration`

The duration of the transition.

### `m_period`

ID: `F:CSinusoidalTransitionFromVelocity.m_period`

The period of oscillation of the sinusoidal wave in seconds.
