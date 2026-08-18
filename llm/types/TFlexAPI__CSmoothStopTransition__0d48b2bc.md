# CSmoothStopTransition

Assembly: `TFlexAPI`

## Summary

Encapsulates a smooth-stop transition.

## Remarks

A smooth-stop transition slows down as it approaches a given final value, and reaches it with a velocity of zero. The duration of the transition is determined by the initial velocity, the difference between the initial and final values, and the specified maximum duration. If there is no solution consisting of a single parabolic arc, this method creates a cubic transition. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CSmoothStopTransition(System.Double,System.Double)`

ID: `M:CSmoothStopTransition.#ctor(System.Double,System.Double)`

Constructs a smooth-stop transition and initializes its maximum duration and final value.

Parameters:
- `maximumDuration`: The maximum duration of the transition.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

## Methods

### `CSmoothStopTransition(System.Double,System.Double)`

ID: `M:CSmoothStopTransition.#ctor(System.Double,System.Double)`

Constructs a smooth-stop transition and initializes its maximum duration and final value.

Parameters:
- `maximumDuration`: The maximum duration of the transition.
- `dblFinalValue`: The value of the animation variable at the end of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CSmoothStopTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CSmoothStopTransition.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_maximumDuration`

ID: `F:CSmoothStopTransition.m_maximumDuration`

The maximum duration of the transition.
