# CInstantaneousTransition

Assembly: `TFlexAPI3D`

## Summary

Encapsulates an instantaneous transition.

## Remarks

During an instantaneous transition, the value of the animation variable changes instantly from its current value to a specified final value. The duration of this transition is always zero. Because all transitions are cleared automatically, it's recommended to allocated them using operator new. The encapsulated IUIAnimationTransition COM object is created by CAnimationController::AnimateGroup, until then it's NULL. Changing member variables after creation of this COM object has no effect.

## Constructors

### `CInstantaneousTransition(System.Double)`

ID: `M:CInstantaneousTransition.#ctor(System.Double)`

Constructs a transition object and initializes its final value.

Parameters:
- `dblFinalValue`: The value of the animation variable at the end of the transition.

## Methods

### `CInstantaneousTransition(System.Double)`

ID: `M:CInstantaneousTransition.#ctor(System.Double)`

Constructs a transition object and initializes its final value.

Parameters:
- `dblFinalValue`: The value of the animation variable at the end of the transition.

### `Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

ID: `M:CInstantaneousTransition.Create(IUIAnimationTransitionLibrary*,IUIAnimationTransitionFactory*)`

Calls the transition library to create encapsulated transition COM object.

Parameters:
- `pLibrary`: A pointer to transition library, which is responsible for creation of standard transitions.
- `pFactory`: A pointer to transition factory, which is responsible for creation of custom transitions.

Returns: TRUE if transition is created successfully; otherwise FALSE.

## Fields

### `m_dblFinalValue`

ID: `F:CInstantaneousTransition.m_dblFinalValue`

The value of the animation variable at the end of the transition.
