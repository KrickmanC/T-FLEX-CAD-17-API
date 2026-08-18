# CD2DTextLayout

Assembly: `TFlexAPI`

## Summary

IDWriteTextLayout wrapper.

## Constructors

### `CD2DTextLayout(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextFormat*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

ID: `M:CD2DTextLayout.#ctor(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextFormat*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

Constructs a CD2DTextLayout object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `strText`: A CString object that contains the string to create a new CD2DTextLayout object from.
- `textFormat`: A CString object that contains the format to apply to the string.
- `sizeMax`: The size of the layout box.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DTextLayout(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextFormat*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

ID: `M:CD2DTextLayout.#ctor(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DTextFormat*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,CD2DSizeF!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Int32)`

Constructs a CD2DTextLayout object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `strText`: A CString object that contains the string to create a new CD2DTextLayout object from.
- `textFormat`: A CString object that contains the format to apply to the string.
- `sizeMax`: The size of the layout box.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Create(CRenderTarget*)`

ID: `M:CD2DTextLayout.Create(CRenderTarget*)`

Creates a CD2DTextLayout.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DTextLayout.Destroy`

Destroys a CD2DTextLayout object.

### `Dispose`

ID: `M:CD2DTextLayout.Dispose`

The destructor. Called when a D2D text layout object is being destroyed.

### `Get`

ID: `M:CD2DTextLayout.Get`

Returns IDWriteTextLayout interface

Returns: Pointer to an IDWriteTextLayout interface or NULL if object is not initialized yet.

### `GetFontFamilyName(System.UInt32,DWRITE_TEXT_RANGE*)`

ID: `M:CD2DTextLayout.GetFontFamilyName(System.UInt32,DWRITE_TEXT_RANGE*)`

Copies the font family name of the text at the specified position.

Parameters:
- `currentPosition`: The position of the text to examine.
- `textRange`: The range of text that has the same formatting as the text at the position specified by currentPosition. This means the run has the exact formatting as the position specified, including but not limited to the font family name.

Returns: CString object that contains the current font family name.

### `GetLocaleName(System.UInt32,DWRITE_TEXT_RANGE*)`

ID: `M:CD2DTextLayout.GetLocaleName(System.UInt32,DWRITE_TEXT_RANGE*)`

Gets the locale name of the text at the specified position.

Parameters:
- `currentPosition`: The position of the text to inspect.
- `textRange`: The range of text that has the same formatting as the text at the position specified by currentPosition. This means the run has the exact formatting as the position specified, including but not limited to the locale name.

Returns: CString object that contains the current locale name.

### `IsValid`

ID: `M:CD2DTextLayout.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `ReCreate(CRenderTarget*)`

ID: `M:CD2DTextLayout.ReCreate(CRenderTarget*)`

Re-creates a CD2DTextLayout.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `SetFontFamilyName(System.Char!System.Runtime.CompilerServices.IsConst*,DWRITE_TEXT_RANGE)`

ID: `M:CD2DTextLayout.SetFontFamilyName(System.Char!System.Runtime.CompilerServices.IsConst*,DWRITE_TEXT_RANGE)`

Sets null-terminated font family name for text within a specified text range

Parameters:
- `pwzFontFamilyName`: The font family name that applies to the entire text string within the range specified by textRange
- `textRange`: Text range to which this change applies

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE

### `SetLocaleName(System.Char!System.Runtime.CompilerServices.IsConst*,DWRITE_TEXT_RANGE)`

ID: `M:CD2DTextLayout.SetLocaleName(System.Char!System.Runtime.CompilerServices.IsConst*,DWRITE_TEXT_RANGE)`

Sets the locale name for text within a specified text range

Parameters:
- `pwzLocaleName`: A null-terminated locale name string
- `textRange`: Text range to which this change applies

Returns: If the method succeeds, it returns TRUE. Otherwise, it returns FALSE

### `op_Implicit~IDWriteTextLayout*`

ID: `M:CD2DTextLayout.op_Implicit~IDWriteTextLayout*`

Returns IDWriteTextLayout interface

Returns: Pointer to an IDWriteTextLayout interface or NULL if object is not initialized yet.

## Fields

### `m_pTextLayout`

ID: `F:CD2DTextLayout.m_pTextLayout`

A pointer to an IDWriteTextLayout.
