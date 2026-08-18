# CAccelerateDecelerateTransition

Assembly: `TFlexCommandAPI`

## Summary

Implements an accelerate-decelerate transition.

## Remarks

During an accelerate-decelerate transition, the animation variable speeds up and then slows down over the duration of the transition, ending at a specified value. You can control how quickly the variable accelerates and decelerates independently, by specifying different acceleration and deceleration ratios. When the initial velocity is zero, the acceleration ratio is the fraction of the duration that the variable will spend accelerating; likewise with the deceleration ratio. If the initial velocity is non-zero, it is the fraction of the time between the velocity reaching zero and the end of transition. The acceleration ratio and the deceleration ratio should sum to a maximum of 1.0. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CAccelerateDecelerateTransition(System.Double,System.Double,System.Double,System.Double)`

ID: `M:CAccelerateDecelerateTransition.#ctor(System.Double,System.Double,System.Double,System.Double)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: The value of the animation variable at the end of the transition.
- `accelerationRatio`: The ratio of the time spent accelerating to the duration.
- `decelerationRatio`: The ratio of the time spent decelerating to the duration.

## Methods

### `CAccelerateDecelerateTransition(System.Double,System.Double,System.Double,System.Double)`

ID: `M:CAccelerateDecelerateTransition.#ctor(System.Double,System.Double,System.Double,System.Double)`

Constructs a transition object.

Parameters:
- `duration`: The duration of the transition.
- `finalValue`: The value of the animation variable at the end of the transition.
- `accelerationRatio`: The ratio of the time spent accelerating to the duration.
- `decelerationRatio`: The ratio of the time spent decelerating to the duration.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CAccelerateDecelerateTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_accelerationRatio`

ID: `F:CAccelerateDecelerateTransition.m_accelerationRatio`

The ratio of the time spent accelerating to the duration.

### `m_decelerationRatio`

ID: `F:CAccelerateDecelerateTransition.m_decelerationRatio`

The ratio of the time spent decelerating to the duration.

### `m_duration`

ID: `F:CAccelerateDecelerateTransition.m_duration`

The duration of the transition.

### `m_finalValue`

ID: `F:CAccelerateDecelerateTransition.m_finalValue`

The value of the animation variable at the end of the transition.
