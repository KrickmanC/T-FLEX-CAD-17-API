# CKeyFrame

Assembly: `TFlexAPI`

## Summary

Represents an animation keyframe.

## Remarks

This class implements an animation keyframe. A keyframe represents a moment in time within a storyboard and can be used to specify the start and end times of transitions. A keyframe may be based on other keyframe and have an offset (in seconds) from it, or may be based on a transition and represent a moment in time when this transition ends.

## Constructors

### `CKeyFrame(CBaseKeyFrame*,System.Double)`

ID: `M:CKeyFrame.#ctor(CBaseKeyFrame*,System.Double)`

Constructs a keyframe that depends on other keyframe.

Parameters:
- `pKeyframe`: A pointer to keyframe.
- `offset`: Offset, in seconds, from keyframe specified by pKeyframe.

Remarks: The constructed keyframe will represent a moment in time within a storyboard, which has a specified offset from pKeyframe.

### `CKeyFrame(CBaseTransition*)`

ID: `M:CKeyFrame.#ctor(CBaseTransition*)`

Constructs a keyframe that depends on a transition.

Parameters:
- `pTransition`: A pointer to a transition.

Remarks: The constructed keyframe will represent a moment in time within a storyboard when the specified transition ends.

## Methods

### `CKeyFrame(CBaseKeyFrame*,System.Double)`

ID: `M:CKeyFrame.#ctor(CBaseKeyFrame*,System.Double)`

Constructs a keyframe that depends on other keyframe.

Parameters:
- `pKeyframe`: A pointer to keyframe.
- `offset`: Offset, in seconds, from keyframe specified by pKeyframe.

Remarks: The constructed keyframe will represent a moment in time within a storyboard, which has a specified offset from pKeyframe.

### `CKeyFrame(CBaseTransition*)`

ID: `M:CKeyFrame.#ctor(CBaseTransition*)`

Constructs a keyframe that depends on a transition.

Parameters:
- `pTransition`: A pointer to a transition.

Remarks: The constructed keyframe will represent a moment in time within a storyboard when the specified transition ends.

### `AddToStoryboard(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CKeyFrame.AddToStoryboard(IUIAnimationStoryboard*,System.Int32)`

Adds a keyframe to a storyboard.

Parameters:
- `pStoryboard`: A pointer to a storyboard.
- `bDeepAdd`: Specifies whether to add keyframe or transition recursively.

Returns: TRUE, if keyframe was added successfully.

Remarks: This method adds a keyframe to storyboard. If it depends on other keyframe or transition and bDeepAdd is TRUE, this method tries to add them recursively.

### `AddToStoryboardAfterTransition(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CKeyFrame.AddToStoryboardAfterTransition(IUIAnimationStoryboard*,System.Int32)`

Adds a keyframe to storyboard after transition.

Parameters:
- `pStoryboard`: A pointer to a storyboard.
- `bDeepAdd`: Specifies whether to add a transition recursively.

Returns: TRUE, if keyframe was added successfully.

Remarks: This function is called by the framework to add a keyframe to storyboard after transition.

### `AddToStoryboardAtOffset(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CKeyFrame.AddToStoryboardAtOffset(IUIAnimationStoryboard*,System.Int32)`

Adds a keyframe to storyboard at offset.

Parameters:
- `pStoryboard`: A pointer to a storyboard.
- `bDeepAdd`: Specifies whether to add a keyframe this keyframe depend on recursively.

Returns: TRUE, if keyframe was added successfully.

Remarks: This function is called by the framework to add a keyframe to storyboard at offset.

### `GetExistingKeyframe`

ID: `M:CKeyFrame.GetExistingKeyframe`

Returns a pointer to a keyframe this keyframe depends on.

Returns: A valid pointer to keyframe, or NULL if this keyframe does not depend on other keyframe.

Remarks: This is an accessor to a keyframe this keyframe depends on.

### `GetOffset`

ID: `M:CKeyFrame.GetOffset`

Returns an offset from other keyframe.

Returns: An offset in seconds from other keyframe.

Remarks: This method should be called to determine an offset in seconds from other keyframe.

### `GetTransition`

ID: `M:CKeyFrame.GetTransition`

Returns a pointer to a transition this keyframe depends on.

Returns: A valid pointer to transition, or NULL if this keyframe does not depend on transition.

Remarks: This is an accessor to a transition this keyframe depends on.

## Fields

### `m_offset`

ID: `F:CKeyFrame.m_offset`

Specifies offset of this keyframe from a keyframe stored in m_pExistingKeyFrame.

### `m_pExistingKeyFrame`

ID: `F:CKeyFrame.m_pExistingKeyFrame`

Stores a pointer to an existing keframe. This keyframe is added to storyboard with m_offset to the existing keyframe.

### `m_pTransition`

ID: `F:CKeyFrame.m_pTransition`

Stores a pointer to transtion that begins at this keyframe.
