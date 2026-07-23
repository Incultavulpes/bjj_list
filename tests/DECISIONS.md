# Technical Decision Log

## Scraping Termination Logic

### Decision
Opted for empty container detection rather than parsing pagination controls to manage extraction loops.

### Context
E-commerce platforms reserve empty pagination parameters for future expansion. Querying out-of-bounds pages returns a standard response with global components but an empty product container.

### Benefits
- **Resilience**: Reduces coupling to CSS classes that change frequently during frontend updates.
- **Simplicity**: Avoids fragile parsing logic for pagination elements before running the pipeline.
- **Adaptability**: Scales automatically to variable catalog sizes per instructor without relying on hardcoded page counts.

### Trade-Off
Incurs one additional request per target to confirm the empty container state.