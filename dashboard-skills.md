# Dashboard Skills File

## Purpose
Capture the key prompt requirements and implementation lessons from the Japan Holiday Dashboard build.

## Learned requirements
- Use Sakura-inspired styling for both background and interface.
- Keep the map centered on Japan and avoid showing too much outside the country.
- Ensure marker popups stay open when clicked and close only when clicking away.
- Remove stale UI sections when the content changes.
- Support itinerary and idea filtering with clear route-focused color distinction.
- Use visible gradient and watermark effects without overwhelming the UI.
- Clean up HTML/CSS to remove unused rules after iterative design changes.

## Dashboard build considerations
- Prefer inline CSS and JavaScript in a single-file prototype when publishing a simple demo.
- Use `L.layerGroup()` for category toggles and maintain map state separately from UI state.
- Keep the map `maxBounds` focused on Japan to prevent panning to unrelated regions.
- Animate theme elements unobtrusively using CSS keyframes.
- Avoid adding interactive behavior that conflicts with popup persistence.
- Validate final static HTML with a parser and remove any selectors for markup no longer present.

## Best practices
- Store subtitle content under the header if summary cards are removed for a cleaner landing experience.
- Use descriptive variable names for route colors and map layers.
- Avoid duplicate CSS rules by searching for selector usage before finalizing.
- Guarantee external links open safely with `target="_blank" rel="noreferrer"`.
