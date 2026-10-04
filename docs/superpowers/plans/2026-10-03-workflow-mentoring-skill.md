# Workflow Mentoring Skill Implementation Plan

> **For agentic workers:** This documentation-only plan is being executed inline at the user's request.

**Goal:** Record the user-reported skill of mentoring and guiding interns in workflow design and implementation for Agentic RAG and Browser Use.

**Architecture:** Add one distinct canonical skill page and link it from both project profiles under user-reported contributions. Keep the existing “Mentoring a trainee” entry unchanged and do not add source-evidence claims or project requirements.

**Tech Stack:** Markdown wiki with YAML frontmatter; Python standard library for link and index validation.

---

### Task 1: Add the canonical skill page

**Files:**
- Create: `wiki/skills/mentoring-and-guiding-interns-in-workflow-design-and-implementation.md`

- [x] **Step 1: Create the page with required metadata and lists**

Use the title **Mentoring and guiding interns in workflow design and implementation**, no source references, and related links to both project profiles. Define it as guiding interns through workflow design and implementation. Include the standard sections:

```markdown
## Projects needing this skill
- None recorded.

## Projects with user-reported use
- Agentic RAG — user-reported.
- Browser Use and Enterprise Web Automation — user-reported.

## Projects showing this skill
- No source-supported personal skill claims recorded.
```

The required frontmatter fields are `id`, `type: skill`, `title`, `aliases`, `related`, and `source_refs`.

### Task 2: Record the user report in both project profiles

**Files:**
- Modify: `wiki/projects/agents-agentic-rag.md`
- Modify: `wiki/projects/agents-browser-use.md`

- [x] **Step 1: Link the skill in each project's related metadata**

Add `../skills/mentoring-and-guiding-interns-in-workflow-design-and-implementation.md` to each project's `related` list.

- [x] **Step 2: Add a user-reported contribution row**

In Agentic RAG, replace the “No personal contributions or outcomes have been user-reported” statement with a user-reported contribution row. In Browser Use, add the same capability under its existing “Contributions and capabilities” table:

```markdown
| [Mentoring and guiding interns in workflow design and implementation](../skills/mentoring-and-guiding-interns-in-workflow-design-and-implementation.md) | user-reported | The user reports mentoring and guiding interns through workflow design and implementation for this project. |
```

Do not add this item to either project's “Know-how needed” or “Skills shown by sources” section.

### Task 3: Update the wiki index and activity log

**Files:**
- Modify: `wiki/index.md`
- Modify: `wiki/log.md`

- [x] **Step 1: Add the skill to the user-reported skills list**

Add a link to the new page under `### User-reported contributions and capabilities` in `wiki/index.md`.

- [x] **Step 2: Record the taxonomy update**

Append a dated `2026-10-03` entry in `wiki/log.md` noting the new canonical skill, both user-reported project associations, and that no source evidence or know-how requirements were asserted.

### Task 4: Validate the wiki update

**Files:**
- Validate: new skill page, both project pages, `wiki/index.md`, and `wiki/log.md`

- [x] **Step 1: Check required sections, attribution, and reciprocal links**

Confirm that all three canonical skill sections exist; both project pages contain the user-reported row and skill link; the skill page lists both projects; and the existing “Mentoring a trainee” page remains unchanged.

- [x] **Step 2: Check index coverage and Markdown links**

Resolve the new relative links and confirm the new skill path is present in `wiki/index.md`. Do not modify `raw/`. The workspace is not a Git repository, so no commit can be created here.
