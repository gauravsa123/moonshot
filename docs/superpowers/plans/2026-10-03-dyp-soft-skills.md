# Dynamic Pricing Soft-Skill Requirements Implementation Plan

> **For agentic workers:** The user requested direct inline execution of this documentation-only plan.

**Goal:** Add five user-confirmed soft-skill requirements to Dynamic Pricing and aggregate them through the existing canonical taxonomy.

**Architecture:** Reuse the existing Value Mate canonical skills rather than create duplicates. Keep the DYP requirements separate from personal contributions and source-evidenced skills; update reciprocal project lists, index, and log.

**Tech Stack:** Markdown wiki with YAML frontmatter; Python standard library for link and coverage validation.

---

### Task 1: Add five requirements to the DYP profile

**Files:**
- Modify: `wiki/projects/pricing-dynamic-pricing-euromaster.md`

- [x] **Step 1: Add canonical skill links and requirements**

Add these existing skill pages to the project's `related` metadata and to the “Know-how needed” table, each with `user-confirmed` status and a rationale stating it was added by the user as a project requirement:

| User wording | Canonical skill page |
|---|---|
| Team collaboration | `cross-functional-team-collaboration.md` |
| Leading the team | `team-leadership-and-direction.md` |
| Stakeholder management | `stakeholder-management.md` |
| Leadership communication | `leadership-communication.md` |
| Support in decision making | `decision-support-and-facilitation.md` |

Update the introductory note to state that the project requirements are user-confirmed, and update the review-state count from 14 to 19. Do not add these items to personal contributions or source-evidenced skills.

### Task 2: Aggregate the requirements on existing skill pages

**Files:**
- Modify: `wiki/skills/cross-functional-team-collaboration.md`
- Modify: `wiki/skills/team-leadership-and-direction.md`
- Modify: `wiki/skills/stakeholder-management.md`
- Modify: `wiki/skills/leadership-communication.md`
- Modify: `wiki/skills/decision-support-and-facilitation.md`

- [x] **Step 1: Add DYP to each “Projects needing this skill” list**

Add `[Dynamic Pricing and Price Optimization for Euromaster](../projects/pricing-dynamic-pricing-euromaster.md) — user-confirmed project requirement.` to each page. Preserve existing Value Mate links and all existing source-evidence metadata.

### Task 3: Update the wiki index and activity log

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [x] **Step 1: Index the five requirements**

Add links to the five canonical skill pages under `### Dynamic Pricing requirements`.

- [x] **Step 2: Record provenance**

Append a dated log entry that records the user's confirmation, the five reused canonical skills, and that these are project requirements—not personal-use claims or DYP source-evidence claims.

### Task 4: Validate the update

**Files:**
- Validate: DYP project profile, five canonical skill pages, `wiki/index.md`, and `wiki/log.md`

- [x] **Step 1: Check status and aggregation**

Confirm all five DYP rows are `user-confirmed`, all five skill pages list both DYP and Value Mate under “Projects needing this skill,” and the DYP review-state count is 19.

- [x] **Step 2: Check index coverage and links**

Resolve the added Markdown links and confirm the five canonical skill paths appear under Dynamic Pricing requirements. Do not edit files under `raw/`. The workspace is not a Git repository, so no commit can be created here.
