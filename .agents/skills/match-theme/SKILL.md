---
name: match-theme
description: "Match Globo Product Options (GPO) controls to a Shopify theme and deliver plain CSS with the user's standard comments. Use when the user says 'match theme', asks to style GPO like a theme, or asks to reformat an existing theme override to match the Sunrise 57 and Grid 718 examples."
---

# Match Theme

Create or update the theme-specific GPO `.css` file using these plain CSS examples:

- [Sunrise 13.01.02, theme store id 57](references/57-sunrise.css)
- [Grid 7.2.0, theme store id 718](references/718-grid.css)

Read the headers and section comments of both examples before writing. Read their relevant control sections when implementing those controls. These files define the user's preferred format and level of control coverage; their colors, dimensions, native selectors, and fonts belong to their respective themes.

## Theme matching

For a new match, use the discovery and verification workflow in [automation](references/automation.md). Inspect the supplied preview and local assets before asking for missing material. Identify the native equivalents: product option labels, variant select, variant pills or swatches, text inputs, quantity selector, buttons, tabs, and accordions. Match each GPO control to the corresponding theme control. Keep each target theme's own appearance.

Measure the painted outer box of each native control, including wrappers and pseudo-elements, rather than assuming the underlying input owns its geometry. Use separate tokens for select, text input, button option, single quantity, and option stepper when native controls differ. A shared field-height is appropriate only after verifying equivalent geometry. Preserve multiline textarea behavior. If the preview has no native counterpart, inspect the same theme assets or a relevant product page; record a supported fallback rather than presenting it as a measured match.

Use existing theme CSS variables for customizable values. Use verified compiled constants when the theme exposes no variable. For an existing override, preserve its known mappings until stronger source evidence supports a change. Continue with mappings supported by the available evidence. Ask only for specific missing material that prevents accurate completion.

Comments must describe supported mappings. Name the actual native selector when it has been inspected. Otherwise name the known control or CSS-variable source; do not invent a selector or claim measurements have been verified on a storefront.

## Required CSS format

Deliver browser-ready CSS that requires no preprocessor. Use scoped CSS custom properties for reusable tokens and flat selectors such as `.gpo-app .gpo-input`. Keep declarations inside their rule blocks; write media queries as ordinary top-level CSS rules.

Use four-space indentation for new files. Keep grouped selectors readable, usually one selector per line, with one blank line between rules. Use explicit selectors instead of nested rules.

Start with this header, using the actual known name, version, and theme store id:

```css
/* Match theme style: ThemeName 1.2.3 (theme store id 123) */
.gpo-app {
    /* Select height = the variant dropdown (.native-select, min-height 40px) */
    --gpo-theme-select-height: 40px;
    --gpo-theme-text: var(--theme-text);
    --gpo-theme-input-bg: var(--theme-input-bg);

    color: var(--gpo-theme-text);
}

/* Dropdown: same outer box as .native-select */
.gpo-app .gpo-dropdown {
    min-height: var(--gpo-theme-select-height);
    background-color: var(--gpo-theme-input-bg);
}
```

Omit unknown identity fields rather than inventing them. Place short source comments next to significant tokens, such as field height, chevron, or focus outline. Prefix generated custom properties with `--gpo-theme-`, define them on `.gpo-app`, and define only tokens the file uses. Keep theme CSS variables as token values or reference them directly. Use native CSS functions such as `var()`, `calc()`, and `color-mix()` where the target supports them.

Place the transparent app background and necessary font inheritance resets before the token/typography rule, as in the examples. Preserve a theme's necessary container rule in this area. Set the app typography on `.gpo-app`; follow it with flat control rules.

Use short English `/* ... */` comments. Section comments state the component and, where helpful, the native mapping or visual behavior. Examples:

```css
/* Group */
/* Label: like legend.form__label */
/* Swatches: same box as the variant dropdown (.select-wrapper) */
/* Selected: the 1px accent outline of .select-wrapper:focus-within */
/* Arrow: the theme chevron, 0.75rem from the edge */
/* List: same field look */
/* Input: like the theme .input / .textarea (height from its native field) */
/* File upload */
/* Action: like the theme .button */
/* Switch */
/* Range */
/* Tabs */
```

Use this section order for controls present in the file:

1. Group
2. Label, selected values, help text, counter, tooltip, and totals when present
3. Button swatches
4. Color / image swatches
5. Quantity, including option quantities and the single quantity input
6. Choicelist: checkbox and radio
7. Dropdown / Select, then Arrow and List
8. Input: text, textarea, dimension, prefixes and suffixes, phone, and color picker
9. File upload, then Action and Remove where distinct
10. Switch
11. Range
12. Tabs, then Horizontal and Vertical

Do not use numbered section comments, uppercase category banners, long separator lines, change-log comments, or a final 'complete the remaining states' patch block. Put each rule and fix in its relevant section. Use brief local comments only for a native mapping or a meaningful compatibility detail, such as suppressing the base dropdown icon or overriding the base image-dropdown item height.

## Editing and verification

Consolidate duplicate and superseded rules carefully. Preserve selection, hover, focus, expanded dropdown, file upload, phone picker, decorated input, and quantity behaviors. Use specificity sufficient to override the GPO base styles without depending on load order.

Match dropdown effects as well as the static appearance. Compare native opening/closing, option hover/selection, and caret behavior; do not assume GPO's inherited transitions match the theme. Follow the [dropdown effects checks](references/automation.md#dropdown-effects), including image and font dropdowns when present.

For a format-only edit, preserve the effective styling. Moving a previously unscoped rule under `.gpo-app` changes specificity; check overlapping rules and shorthand/longhand declarations before claiming equivalent behavior.

Parse each changed `.css` with an available CSS parser and check the selectors and declarations. Deliver plain CSS without preprocessor variables, functions, interpolation, or nesting. If converting an existing source, preserve effective selectors, specificity, rule order, and values; update actual references to the new CSS file within the requested scope. CSS syntax validation alone does not establish visual equivalence.

If a preview is available, first establish which override is actually loaded. Keep the editable CSS and served preview CSS distinct; record a bundled/minified artifact separately when the project uses one. Verify changed controls and states using the workflow in [automation](references/automation.md), and resolve demonstrated mismatches within the authorized scope. Report changed files, the observed verification coverage, and any material limitation briefly in the user's language. For audit-only requests, deliver findings and proposals without changing the active theme or publishing assets.

## Learn from each match

After every match, including one with limited preview verification, review the actual corrections, failed mappings, repeated investigation, and any manual work the user still had to do. Look for a concrete addition that would make the next match more accurate or reduce repeated work. Check the existing instructions and references before proposing an addition.

When there is a useful new finding, briefly propose the skill improvement in the completion report, following [the learning review](references/automation.md#learning-review-after-each-match). Include the observed evidence, the exact instruction or reference to change, and how the addition would help future matches. Keep theme/version-specific exceptions in the theme cases; generalize only when the evidence supports it. Do not manufacture suggestions when the existing skill already covers the finding. Proposing an improvement does not itself mean changing the skill; apply skill updates when the user requests them.
