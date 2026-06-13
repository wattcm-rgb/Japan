# Japan Holiday Dashboard Context

## Project
- Single-page Leaflet itinerary dashboard for a Japan family holiday.
- File: `japan-holiday-dashboard.html`

## User goals
- Apply Sakura theme and animated sakura flower background.
- Use route-specific colors and visible map styling.
- Add accommodation website links and correct OMO Kansai coordinates.
- Make popups persist on click until the user clicks away.
- Remove the popup photo preview and redundant popup CSS.
- Set default map zoom so Japan is visible without showing too much outside.
- Replace itinerary overview section with a subtitle under the header.

## Implemented features
- Sakura-themed layout and background.
- Static Sakura watermark via CSS gradients.
- Animated sakura flower-shaped petals using `div.sakra-petal`.
- Leaflet map with airport, accommodation, event, and idea markers.
- Route polylines with distinct colors and hover popups.
- Filterable Instagram idea list with live search and map focus.
- Persistent click-open popups plus map click-to-close behavior.
- Default map zoom set to `6` for Japan-only visibility.
- Cleaned redundant CSS rules and unused selectors.

## Validation
- HTML parsed successfully with no parser errors.
- Redundant selectors like `summary-card`, `top-bar`, `popup-photo`, and `branch-highlight` were removed.
