# CDiscreteTransition

Assembly: `TFlexAPI3D`

## Summary

Encapsulates a discrete transition.

## Remarks

During a discrete transition, the animation variable remains at the initial value for a specified delay time, then switches instantaneously to a specified final value and remains at that value for a given hold time. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CDiscreteTransition(System.Double,System.Double,System.Double)`

ID: `M:CDiscreteTransition.#ctor(System.Double,System.Double,System.Double)`

Constructs a discrete transition object and initializes its parameters.

Parameters:
- `delay`: The amount of time by which to delay the instantaneous switch to the final value.
- `dblFinalValue`: The value of the animation variable at the end of the transition.
- `hold`: The amount of time by which to hold the variable at its final value.

## Methods

### `CDiscreteTransition(System.Double,System.Double,System.Double)`

ID: `M:CDiscreteTransition.#ctor(System.Double,System.Double,System.Double)`

Constructs a discrete transition object and initializes its parameters.

Parameters:
- `delay`: The amount of time by which to delay the instantaneous switch to the final value.
- `dblFinalValue`: The value of the animation variable at the end of the transition.
- `hold`: The amount of time by which to hold the variable at its final value.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CDiscreteTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CDiscreteTransition.m_dblFinalValue`

The value of the animation variable at the end of the transition.

### `m_delay`

ID: `F:CDiscreteTransition.m_delay`

The amount of time by which to delay the instantaneous switch to the final value.

### `m_hold`

ID: `F:CDiscreteTransition.m_hold`

The amount of time by which to hold the variable at its final value.
