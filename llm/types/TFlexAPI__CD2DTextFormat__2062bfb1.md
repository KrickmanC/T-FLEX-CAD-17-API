# CD2DTextFormat

Assembly: `TFlexAPI`

## Summary

IDWriteTextFormat wrapper.

## Constructors

### `CD2DTextFormat(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,DWRITE_FONT_WEIGHT,DWRITE_FONT_STYLE,DWRITE_FONT_STRETCH,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,IDWriteFontCollection*,System.Int32)`

ID: `M:CD2DTextFormat.#ctor(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,DWRITE_FONT_WEIGHT,DWRITE_FONT_STYLE,DWRITE_FONT_STRETCH,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,IDWriteFontCollection*,System.Int32)`

Constructs a CD2DTextFormat object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `strFontFamilyName`: A CString object that contains the name of the font family.
- `fontSize`: The logical size of the font in DIP ("device-independent pixel") units. A DIPequals 1/96 inch.
- `fontWeight`: A value that indicates the font weight for the text object.
- `fontStyle`: A value that indicates the font style for the text object.
- `fontStretch`: A value that indicates the font stretch for the text object.
- `strFontLocale`: A CString object that contains the locale name.
- `pFontCollection`: A pointer to a font collection object. When this is NULL, indicates the system font collection.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

## Methods

### `CD2DTextFormat(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,DWRITE_FONT_WEIGHT,DWRITE_FONT_STYLE,DWRITE_FONT_STRETCH,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,IDWriteFontCollection*,System.Int32)`

ID: `M:CD2DTextFormat.#ctor(CRenderTarget*,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,System.Single,DWRITE_FONT_WEIGHT,DWRITE_FONT_STYLE,DWRITE_FONT_STRETCH,ATL.CStringT<System.Char,StrTraitMFC_DLL<System.Char,ATL.ChTraitsCRT{System.Char}>>!System.Runtime.CompilerServices.IsConst*!System.Runtime.CompilerServices.IsImplicitlyDereferenced,IDWriteFontCollection*,System.Int32)`

Constructs a CD2DTextFormat object.

Parameters:
- `pParentTarget`: A pointer to the render target.
- `strFontFamilyName`: A CString object that contains the name of the font family.
- `fontSize`: The logical size of the font in DIP ("device-independent pixel") units. A DIPequals 1/96 inch.
- `fontWeight`: A value that indicates the font weight for the text object.
- `fontStyle`: A value that indicates the font style for the text object.
- `fontStretch`: A value that indicates the font stretch for the text object.
- `strFontLocale`: A CString object that contains the locale name.
- `pFontCollection`: A pointer to a font collection object. When this is NULL, indicates the system font collection.
- `bAutoDestroy`: Indicates that the object will be destroyed by owner (pParentTarget).

### `Create(CRenderTarget*)`

ID: `M:CD2DTextFormat.Create(CRenderTarget*)`

Creates a CD2DTextFormat.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `Destroy`

ID: `M:CD2DTextFormat.Destroy`

Destroys a CD2DTextFormat object.

### `Dispose`

ID: `M:CD2DTextFormat.Dispose`

The destructor. Called when a D2D text format object is being destroyed.

### `Get`

ID: `M:CD2DTextFormat.Get`

Returns IDWriteTextFormat interface

Returns: Pointer to an IDWriteTextFormat interface or NULL if object is not initialized yet.

### `GetFontFamilyName`

ID: `M:CD2DTextFormat.GetFontFamilyName`

Gets a copy of the font family name.

Returns: CString object that contains the current font family name.

### `GetLocaleName`

ID: `M:CD2DTextFormat.GetLocaleName`

Gets a copy of the locale name.

Returns: CString object that contains the current locale name.

### `IsValid`

ID: `M:CD2DTextFormat.IsValid`

Checks resource validity

Returns: TRUE if resource is valid; otherwise FALSE.

### `ReCreate(CRenderTarget*)`

ID: `M:CD2DTextFormat.ReCreate(CRenderTarget*)`

Re-creates a CD2DTextFormat.

Parameters:
- `pRenderTarget`: A pointer to the render target.

Returns: If the method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

### `op_Implicit~IDWriteTextFormat*`

ID: `M:CD2DTextFormat.op_Implicit~IDWriteTextFormat*`

Returns IDWriteTextFormat interface

Returns: Pointer to an IDWriteTextFormat interface or NULL if object is not initialized yet.

## Fields

### `m_pTextFormat`

ID: `F:CD2DTextFormat.m_pTextFormat`

A pointer to an IDWriteTextFormat.
