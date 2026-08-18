# CBaseKeyFrame

Assembly: `TFlexCommandAPI`

## Summary

Implements basic functionality of keyframe.

## Remarks

Encapsulates UI_ANIMATION_KEYFRAME variable. Serves as a base class for any keyframe implementation. A keyframe represents a moment in time within a storyboard and can be used to specify the start and end times of transitions. There are two types of keyframes - keyframes added to storyboard at the specified offset (in time), or keyframes added after specified transition. Because durations of some transitions can't be known before animation starts, the actual values of some keyframes are determined at runtime only. Because keyframes may depend on transitions, which in their turn depend on keyframes, it's important to prevent infinite recursions when building keyframe chains.

## Constructors

### `CBaseKeyFrame`

ID: `M:CBaseKeyFrame.#ctor`

Constructs a keyframe object.

## Methods

### `CBaseKeyFrame`

ID: `M:CBaseKeyFrame.#ctor`

Constructs a keyframe object.

### `AddToStoryboard(IUIAnimationStoryboard*,System.Int32)`

ID: `M:CBaseKeyFrame.AddToStoryboard(IUIAnimationStoryboard*,System.Int32)`

Adds a keyframe to storyboard.

Parameters:
- `pStoryboard`: A pointer to a storyboard.
- `bDeepAdd`: If this parameter is TRUE and the keyframe being added depends on some other keyframe or transition, this method tries to add this keyframe or transition to storyboard first.

Returns: TRUE if keyframe was added to storyboard successfully; otherwise FALSE.

Remarks: This method is called to add a keyframe to storyboard.

### `GetAnimationKeyframe`

ID: `M:CBaseKeyFrame.GetAnimationKeyframe`

Returns the underlying keyframe value.

Returns: A current keyframe. The default value is UI_ANIMATION_KEYFRAME_STORYBOARD_START.

Remarks: This is an accessor to the underlying keyframe value.

### `IsAdded`

ID: `M:CBaseKeyFrame.IsAdded`

Tells whether a keyframe has been added to storyboard.

Returns: TRUE if a keyframe is added to a storyboard; otehrwise FALSE.

Remarks: In the base class IsAdded always returns TRUE, but it's overridden in derived classes.

### `IsKeyframeAtOffset`

ID: `M:CBaseKeyFrame.IsKeyframeAtOffset`

Specifies whether the keyframe should be added to storyboard at offset, or after transition.

Returns: TRUE if the keyframe should be added to storyboard at some specified offset. FALSE if the keyframe should be added to storyboard after some transition.

Remarks: Specifies whether the keyframe should be added to storyboard at offset. The offset or transition must be specified in a derived class.

## Fields

### `m_bAdded`

ID: `F:CBaseKeyFrame.m_bAdded`

Specifies whether this keyframe has been added to a storyboard.

### `m_bIsKeyframeAtOffset`

ID: `F:CBaseKeyFrame.m_bIsKeyframeAtOffset`

Specifies whether this keyframe should be added to storyboard at an offset from another existing keyframe, or at the end of some transition.

### `m_keyframe`

ID: `F:CBaseKeyFrame.m_keyframe`

Represents a Windows Animation API keyframe. When a keyframe is not initialized it is set to the predefined value UI_ANIMATION_KEYFRAME_STORYBOARD_START.
