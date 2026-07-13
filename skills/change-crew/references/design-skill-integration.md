# Design Skill Integration

Use this reference when a task touches web UI, mobile UI, visual styling, responsive layout, component composition, Figma, motion, or design-system consistency.

Change Crew is the delivery orchestrator. Do not copy a specialist design skill into the workflow. Route to the right design skill or apply its principles, then keep the resulting constraints in Change Crew artifacts.

## Reference Skills

These public or installed skills are useful benchmarks for design-heavy work:

| Skill | Use For | Reusable Lesson |
| --- | --- | --- |
| `design-taste-frontend` / taste-skill | landing pages, portfolios, redesigns, high-polish web UI | avoid templated "AI slop"; infer a strong visual direction from the brief; audit existing brand and content before designing |
| Anthropic `frontend-design` | general front-end visual quality | treat layout, typography, states, and polish as first-class implementation requirements |
| `ui-ux-pro-max-skill` | UI/UX audit, accessibility, heuristics, product flows | make usability, hierarchy, spacing, contrast, and interaction feedback explicit review criteria |
| `platform-design-skills` | native platform conventions | choose iOS, Android, web, or desktop patterns instead of generic cross-platform UI |
| `mobile-app-ui-design` | mobile app screens and flows | prioritize safe areas, touch targets, navigation, keyboard behavior, and device-size checks |
| SwiftUI agent/design skills | SwiftUI/iOS app work | use native components, previews, dynamic type, accessibility, and platform idioms |
| Figma skills | Figma-to-code, code-to-Figma, design systems | sync tokens, variants, component mappings, and visual intent instead of treating Figma as a static screenshot |
| frontend design toolkits | component libraries, visual QA, screenshot loops | verify rendered pixels, not just code structure |

## Routing

Select one route during `SURFACE_DISCOVERY` and record it in `surface-map.md`.

| Situation | Route |
| --- | --- |
| Marketing page, landing page, portfolio, brand site, homepage redesign | Use or mirror `design-taste-frontend`; require a distinct visual direction, real imagery or relevant assets, responsive hero/sections, and screenshot verification. |
| Product app, dashboard, admin, CRM, SaaS workflow | Prefer the existing project design system. Use UI/UX audit principles for density, state coverage, accessibility, and workflow efficiency. Avoid marketing-style composition unless the product already uses it. |
| Existing UI component change | Preserve local component APIs, tokens, spacing, icons, and interaction patterns. Improve polish only within the touched scope unless the task requests a redesign. |
| Mobile iOS | Use SwiftUI/iOS or platform design guidance. Check safe areas, dynamic type, native navigation, permissions, and device previews or simulator smoke tests. |
| Mobile Android | Use Material/platform guidance. Check back behavior, permissions, keyboard, density, status/navigation bars, and emulator or screenshot checks. |
| Flutter, React Native, Expo, cross-platform mobile | Combine mobile design guidance with platform escape hatches for safe areas, keyboard, permissions, and platform-specific navigation. |
| Figma link, design tokens, component library, design-to-code | Use Figma skills when available. Record token, variant, motion, and component mapping obligations in `contract.md`. |
| No user-facing UI | Do not load design skills. Use backend/data/infra/docs playbooks instead. |

## Contract Additions For UI Work

Add these sections to `contract.md` when relevant:

- Visual direction: product/admin, editorial, brand, native mobile, or existing-system-only.
- Design source of truth: existing code, Figma, screenshots, brand assets, or inferred brief.
- Component system: allowed UI library, icon library, token source, spacing scale, typography source.
- Required states: loading, empty, error, disabled, permission denied, optimistic, offline, long text, narrow viewport.
- Responsiveness: named desktop/tablet/mobile breakpoints or device targets.
- Accessibility: keyboard path, focus order, labels, contrast, reduced motion, screen-reader expectations.
- Visual verification: screenshots or browser/device smoke tests to capture.

## Review Checklist

For web and mobile UI changes, review must ask:

- Does the result fit the product surface instead of looking like a generic template?
- Does it use the existing design system before inventing new primitives?
- Are visual hierarchy, spacing, typography, and alignment intentional?
- Are all user-visible states represented and tested or manually verified?
- Does text wrap without overlap at common viewport or device sizes?
- Are controls semantic, reachable by keyboard or assistive tech, and large enough for touch where applicable?
- Are icons, imagery, colors, and motion consistent with platform and project conventions?

## Verification Checklist

When layout or visual behavior matters, verification should include at least one rendered check:

- browser screenshot for web UI;
- mobile simulator/emulator screenshot or device preview for mobile UI;
- visual diff or component-story screenshot when the repo supports it;
- manual viewport checks for small, medium, and wide sizes when automation is unavailable.

Record missing visual verification as a gap in `verification-report.md`; it does not automatically block done unless the task is primarily visual, high-risk, or user-facing.
