# Discovery, matching, and verification

Use this workflow for a new theme or a visual correction. A format-only edit does not require a new full storefront audit. For an audit-only request, inspect and propose; do not alter the active theme or upload assets.

## Establish what is being tested

Record the product URL, variant, theme name, verified version/store id, actual viewport, and the override stylesheet currently loaded. Shopify asset paths such as `/t/74/` are installed-theme identifiers, not theme store ids.

Keep editable CSS and CSS served by the preview distinct. Record a bundled/minified artifact separately when the project uses one. Inspect stylesheet links, inline GPO styles, and relevant winning declarations. An absent or outdated override is an integration finding; it is not proof that the new CSS is visually wrong. Do not invent a CDN URL to test a guessed version.

Wait for the GPO controls and relevant fonts/styles to appear before measuring. Confirm the actual `innerWidth` and `innerHeight` after changing a viewport. Do not label a measurement “mobile” merely because a resize request succeeded.

## Build the native-to-GPO map automatically

Find native candidates inside the main product area first. Use their roles, labels, form association, markup, and theme CSS to choose the equivalent. Exclude cart drawers, sticky duplicates, hidden originals, newsletter inputs, and country/currency selectors from the default product-control mapping.

For each mapping, record:

- Native selector and the element that paints the border/background/icon.
- GPO selector and its painted wrapper, inner field, prefix/suffix, or quantity parts.
- Typography, per-side borders, radius, padding, measured outer height, box sizing, and relevant pseudo-elements.
- Token source: a CSS variable with its scope, an inspected stylesheet declaration, or a measured fallback.
- States available and verification status: observed match, inferred mapping, not rendered, or unresolved.

Inspect parents and `::before` / `::after`; a transparent or opacity-zero native select can be an interaction layer over a painted wrapper. Its own computed border/font is not necessarily the appearance to reproduce. Measure the visible label/value as well as the wrapper.

Do not require the user to choose selectors or measure pixels when the preview or assets provide the evidence. If one control is absent, inspect the same theme's assets or another relevant product linked from the store. Ask only when the specific missing source prevents accurate completion.

## Choose reusable tokens by control role

| GPO component | Preferred native evidence |
| --- | --- |
| Label, selected value, help | Product option label, value text, supporting text |
| Select, custom dropdown, font dropdown | Native variant select and painted wrapper |
| Text, textarea, dimension, phone, color input | Native text field; decorated-field wrapper where applicable |
| Button swatch | Native variant pill; use button geometry only as a documented fallback |
| Color/image swatch | Native swatch and its selected ring |
| Single quantity | Native quantity input |
| Option quantity with plus/minus | Native quantity stepper, including its outer border and button parts |
| Upload action and remove | Native primary and secondary actions, respectively |
| Tabs / disclosure | Native tabs / accordion heading and active state |
| Checkbox, radio, switch, range | Corresponding native control; otherwise a documented theme-token adaptation |

Use a shared `--gpo-theme-field-height` only for controls whose native roles have equivalent geometry. Split `--gpo-theme-select-height`, `--gpo-theme-input-height`, `--gpo-theme-quantity-height`, and `--gpo-theme-option-quantity-height` when justified. Define tokens on `.gpo-app` and consume them with `var()`. A 38px child inside a 40px bordered wrapper is not a 2px mismatch. Do not add borders twice or use the full control height as the line-height of multiline content.

Prefer theme CSS variables that resolve in the GPO control's ancestor scope. Inspect the source declaration to retain relative units and responsive formulas; do not replace `rem`, `calc()`, or a configurable variable with one observed pixel value. Use compiled constants when the theme actually provides no suitable variable. Keep body, navigation, label, and action typography distinct when the theme does.

The Sunrise/Grid references define format and component patterns, not universal color, radius, or height defaults. Consult [observed theme cases](theme-cases.md) only for a relevant theme or failure pattern.

## Generate and integrate the override

Emit the plain CSS/comment format from `SKILL.md`, with scoped custom properties and flat selectors. Keep fixes in their component sections. Preserve GPO's conditional visibility, values, choice state, font previews, and quantity behavior.

Set geometry on the element that owns it; let the inner input fill the remaining box. Scope overrides to GPO. Avoid a blanket font/line-height reset that suppresses font-picker previews or catches quantity buttons unintentionally. Use `!important` only for demonstrated competing declarations; record the reason briefly when it is not obvious.

Validate CSS syntax with an available parser. Test the exact deliverable CSS using the project's supported local/preview integration. Follow the browser tool's supported APIs; read-only evaluation must not be used to inject CSS or mutate the page. Writing/uploading to an external store follows the user's authorization and available integration. If preview integration is unavailable, deliver the CSS with visual application explicitly unverified.

## Verify and repair autonomously

Use a representative desktop and narrow mobile viewport; 1440×1000 and 390×844 are useful defaults, not design constraints. Inspect another width when a breakpoint or failure warrants it. Compare with the corresponding native control at the same viewport and state.

Exercise changed controls: default, selected, focus via pointer and keyboard, expanded dropdown, and disabled/error states when present. Use hover when the available browser API supports it. Check image dropdown, font picker, prefix/suffix, phone country menu, textarea, quantity, and horizontal/vertical tabs when they are changed or rendered. File-upload/remove verification needs an authorized disposable fixture; otherwise mark that state untested.

Verify observable outcomes:

- The intended CSS override is loaded and its declarations win.
- Dropdown opening/closing effects match the native control, an option can be selected, and its value is retained after blur.
- Selection/focus stays visible without unintended size changes.
- Prefix/suffix and quantity controls align when labels wrap.
- Textarea remains multiline; dropdown/country lists are not clipped by an ancestor.
- GPO controls stay inside their container on narrow screens; page-level overflow must be attributed before blaming GPO.
- Native product controls keep their appearance, and GPO logic retains its prior behavior.

A height difference over 1 CSS pixel is a useful review flag for an intended identical box, not a universal failure threshold. Expected layout changes from conditional fields are not “jumps.” Whole-page screenshot differences caused by product media or animation are not evidence of a control mismatch.

Repair demonstrated mismatches within the authorized scope, then repeat the affected checks. Stop when the relevant checks pass, or report the specific missing integration/source that prevents completion. Do not mark absent controls or states as passed.

Save concise screenshots and a mapping/verification record alongside the result. Report CSS syntax validation and storefront application separately. Do not claim fully automatic matching across new themes until the workflow has passed an unseen theme with relevant controls and settings.

### Dropdown effects

Inspect the native dropdown in its closed, opening, open, and closing states. Record how the list is shown or hidden (`display`, `visibility`, `opacity`, `max-height`, or transforms), the relevant transition/animation properties, duration, delay and easing, and whether the caret rotates or stays still. A settled screenshot alone cannot establish that the opening/closing effect matches. Use live interactions and inspected source/computed styles; identify any behavior that could not be observed.

- Compare the button, list container, option hover/selected background, and caret separately. Their effects can differ; resetting the list transition should not remove a native option-hover transition.
- Check GPO's inherited rules and specialized image/color/font dropdown selectors. Remove or replace an inherited effect only when native evidence supports it. If the theme opens immediately, explicitly reset a competing GPO list transition and reproduce its closed/open visibility states; do not apply `transition: none` to every theme by default.
- Exercise opening, closing with the trigger and outside click, and selecting a value. Compare any theme-supported keyboard behavior when the controls expose it. Confirm the caret and selected marker in both states, retained values after blur, and image/font previews when present.
- Verify affected dropdown effects on desktop and mobile with the actual saved/served override. Keep lists within the viewport and preserve their stacking, scrolling and maximum height. When hover input is unavailable, report source/computed-style coverage separately from a visually exercised hover state.

## Learning review after each match

Review the match's mapping and verification record before finishing. Useful candidates include an overlooked painted wrapper, a theme variable with a narrower scope, a distinct quantity role, a repeated cascade problem, or an inspection step that would have avoided manual correction. Check whether the skill already addresses the finding; reuse an existing rule instead of proposing a duplicate.

For each actionable proposal, report briefly in the user's language:

- **Observation and evidence:** what happened, the relevant theme/version and control, and the measured state or stylesheet declaration. Distinguish verified behavior from a hypothesis when preview application was unavailable.
- **Proposed addition:** name the skill file or section and give the concrete instruction, mapping, or check to add. Put theme-specific mappings in `references/theme-cases.md`; use `SKILL.md` or this workflow for a supported reusable decision rule.
- **Benefit and verification:** explain which repeated investigation or manual fix it would avoid. State the checks already performed and any further check needed before broadening the rule to other themes or settings.

Keep these proposals proportionate to the findings. Complete the current theme's required fixes and verification before using the report to propose future skill improvements. If there is no useful new addition, do not invent one. Keep the mapping/evidence with the match result so a later requested skill update can use it without repeating the audit.
