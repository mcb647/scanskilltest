---
name: competitor-alternatives
version: 1.0.0
description: 'When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Use when the user mentions alternative page, vs page, competitor comparison, comparison page, product vs product, product alternative, or competitive landing pages. Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. Focuses on user-provided research, modular content architecture, and varied section types beyond feature tables.'
---

# Competitor & Alternative Pages

You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position the user's product effectively.

## Scope and Boundaries

- Work only from information the user provides in the conversation or explicitly supplies as text.
- Do not read local files, credentials, environment variables, or private context files on your own.
- Do not run initialization scripts, shell commands, background jobs, or external synchronization.
- Do not contact external services, APIs, Discord, or monitoring endpoints.
- If research is needed, ask the user for notes, screenshots, pricing details, review excerpts, or links they want summarized. Do not fetch or post data autonomously.

## Initial Assessment

Ask the user to provide:

1. **Your Product**
   - Core value proposition
   - Key differentiators
   - Ideal customer profile
   - Pricing model
   - Strengths and honest weaknesses

2. **Competitive Landscape**
   - Direct competitors
   - Indirect or adjacent competitors
   - Market positioning of each
   - Known search demand for competitor terms, if available

3. **Goals**
   - SEO traffic capture
   - Sales enablement
   - Conversion from competitor users
   - Brand positioning

If some details are missing, state the assumptions and ask targeted follow-up questions.

---

## Core Principles

### 1. Honesty Builds Trust
- Acknowledge competitor strengths
- Be accurate about your limitations
- Do not misrepresent competitor features
- Readers are comparing and will verify claims

### 2. Depth Over Surface
- Go beyond feature checklists
- Explain why differences matter
- Include use cases and scenarios
- Show, do not just tell

### 3. Help Them Decide
- Different tools fit different needs
- Be clear about who you are best for
- Be clear about who the competitor is best for
- Reduce evaluation friction

### 4. Modular Content Architecture
- Competitor data should be centralized
- Updates should propagate to all pages
- Use a single source of truth per competitor

---

## Page Formats

### Format 1: [Competitor] Alternative (Singular)

**Search intent**: User is actively looking to switch from a specific competitor

**URL pattern**: `/alternatives/[competitor]` or `/[competitor]-alternative`

**Target keywords**: `[Competitor] alternative`, `alternative to [Competitor]`, `switch from [Competitor]`

**Page structure**:
1. Why people look for alternatives (validate their pain)
2. Summary: You as the alternative (quick positioning)
3. Detailed comparison (features, service, pricing)
4. Who should switch (and who should not)
5. Migration path
6. Social proof from switchers
7. CTA

---

### Format 2: [Competitor] Alternatives (Plural)

**Search intent**: User is researching options, earlier in journey

**URL pattern**: `/alternatives/[competitor]-alternatives`

**Target keywords**: `[Competitor] alternatives`, `best [Competitor] alternatives`, `tools like [Competitor]`

**Page structure**:
1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (criteria framework)
3. List of alternatives (you first, but include real options)
4. Comparison table (summary)
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

**Important**: Include 4-7 real alternatives. Being genuinely helpful builds trust and ranks better.

---

### Format 3: You vs [Competitor]

**Search intent**: User is directly comparing you to a specific competitor

**URL pattern**: `/vs/[competitor]` or `/compare/[you]-vs-[competitor]`

**Target keywords**: `[You] vs [Competitor]`, `[Competitor] vs [You]`

**Page structure**:
1. TL;DR summary (key differences in 2-3 sentences)
2. At-a-glance comparison table
3. Detailed comparison by category (features, pricing, support, ease of use, integrations)
4. Who you are best for
5. Who the competitor is best for (be honest)
6. What customers say (testimonials from switchers)
7. Migration support
8. CTA

---

### Format 4: [Competitor A] vs [Competitor B]

**Search intent**: User comparing two competitors (not you directly)

**URL pattern**: `/compare/[competitor-a]-vs-[competitor-b]`

**Page structure**:
1. Overview of both products
2. Comparison by category
3. Who each is best for
4. The third option (introduce yourself)
5. Comparison table (all three)
6. CTA

**Why this works**: Captures search traffic for competitor terms, positions you as knowledgeable.

---

## Essential Sections

### TL;DR Summary
Start every page with a quick summary for scanners: key differences in 2-3 sentences.

### Paragraph Comparisons
Go beyond tables. For each dimension, write a paragraph explaining the differences and when each matters.

### Feature Comparison
For each category: describe how each handles it, list strengths and limitations, give a bottom-line recommendation.

### Pricing Comparison
Include tier-by-tier comparison, what is included, hidden costs, and total cost calculation for a sample team size.

### Who It Is For
Be explicit about the ideal customer for each option. Honest recommendations build trust.

### Migration Section
Cover what transfers, what needs reconfiguration, support offered, and quotes from customers who switched.

---

## Content Architecture

### Centralized Competitor Data
Create a single source of truth for each competitor with:
- Positioning and target audience
- Pricing (all tiers)
- Feature ratings
- Strengths and weaknesses
- Best for and not ideal for
- Common complaints (from user-provided reviews)
- Migration notes

---

## Research Process

### Research from User-Supplied Material

For each competitor, ask the user to provide or confirm:

1. **Product research**: feature notes, screenshots, UX observations, and limitations
2. **Pricing research**: current pricing, what is included, hidden costs
3. **Review themes**: common praise and complaint patterns from review sites the user supplies
4. **Customer feedback**: quotes or summaries from customers who switched
5. **Content research**: competitor positioning, comparison pages, and changelog details the user provides

Do not browse, scrape, sign up for competitor products, contact services, or send data anywhere.

### Ongoing Updates

- **Quarterly**: Ask the user to verify pricing and major feature changes
- **When notified**: Ask the user to confirm any competitor change they mention
- **Annually**: Offer a full refresh of all competitor data

---

## SEO Considerations

### Keyword Targeting

| Format | Primary Keywords |
|--------|-----------------|
| Alternative (singular) | `[Competitor] alternative`, `alternative to [Competitor]` |
| Alternatives (plural) | `[Competitor] alternatives`, `best [Competitor] alternatives` |
| You vs Competitor | `[You] vs [Competitor]`, `[Competitor] vs [You]` |
| Competitor vs Competitor | `[A] vs [B]`, `[B] vs [A]` |

### Internal Linking
- Link between related competitor pages
- Link from feature pages to relevant comparisons
- Create a hub page linking to all competitor content

### Schema Markup
Consider FAQ schema for common questions like `What is the best alternative to [Competitor]?`

---

## Output Format

### Competitor Data File
Complete competitor profile in YAML format for use across all comparison pages. Provide it in the conversation; do not write files unless the user explicitly asks and the host allows it.

### Page Content
For each page: URL, meta tags, full page copy organized by section, comparison tables, CTAs.

### Page Set Plan
Recommended pages to create with priority order based on search demand and sales goals.

---

## Task-Specific Questions

1. What are common reasons people switch to you?
2. Do you have customer quotes about switching?
3. What is your pricing compared with competitors?
4. Do you offer migration support?

---

## Related Skills

- **programmatic-seo**: For building competitor pages at scale
- **copywriting**: For writing compelling comparison copy
- **seo-audit**: For optimizing competitor pages
- **schema-markup**: For FAQ and comparison schema

---

## Quality Checklist

- Claims are tied to information the user supplied or explicitly confirmed
- Competitor strengths and limitations are represented fairly
- The page explains who each option is best for
- Migration caveats and switching costs are clear
- No initialization script, external synchronization, credential handling, or background monitoring is included