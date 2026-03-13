# AI Employee Vault

An Obsidian-based AI employee system where an AI agent named **Atlas** works inside a structured vault — reading tasks, planning actions, executing work, and logging everything. Built during **Hackathon 0**.

## What It Does

The AI Employee Vault turns Obsidian into a virtual office for an AI worker. You drop tasks into an **Inbox** folder, and Atlas (the AI employee) picks them up, creates a plan, executes the work, and moves completed tasks to **Done** — all while following rules from a Company Handbook and logging every action.

Think of it as a file-driven task management system where the AI operates like a real employee: it reads instructions, follows procedures, asks for approval on sensitive actions, and keeps a dashboard updated.

## How It Works

```
You drop a file into /Inbox
        |
        v
File Watcher moves it to /Needs_Action (with timestamp + metadata)
        |
        v
Atlas reads the task and checks /Skills for matching workflows
        |
        v
Atlas creates a plan in /Plans
        |
        v
Atlas executes the plan (or moves to /Pending_Approval if sensitive)
        |
        v
Task moves to /Done, Dashboard + Logs updated
```

## Folder Structure

| Folder | Purpose |
|---|---|
| `/Inbox` | Drop new task files here |
| `/Needs_Action` | Tasks waiting to be processed by Atlas |
| `/Pending_Approval` | Tasks that need human approval before proceeding |
| `/Plans` | Execution plans Atlas creates before doing work |
| `/Done` | Completed tasks and their plans |
| `/Logs` | Daily activity logs |
| `/Skills Process Task` | Reusable skill templates (e.g., how to process a task) |
| `/Skills-summarize-file` | Skill for summarizing file contents |

## Key Files

| File | Purpose |
|---|---|
| `CLAUDE.md` | Master instructions for Atlas — workflow, rules, and behavior |
| `Company_Handbook.md` | Company rules, safety policies, and priority levels |
| `Dashboard.md` | Live status board — pending tasks, completed work, alerts |
| `file_watcher.py` | Python script that monitors `/Inbox` and auto-routes new files |
| `File-Watcher.py.md` | Documentation/reference for the file watcher using `watchdog` |

## Features

- **Autonomous Task Processing** — Atlas reads, plans, executes, and completes tasks without hand-holding
- **File Watcher** — Python script auto-detects new files in `/Inbox`, timestamps them, and routes to `/Needs_Action`
- **Approval Workflow** — Sensitive tasks (payments, deletes, sends) get moved to `/Pending_Approval` instead of auto-executing
- **Skill System** — Reusable skill templates in `/Skills` folders teach Atlas how to handle specific task types
- **Daily Logging** — Every action is logged in `/Logs/YYYY-MM-DD.md`
- **Dashboard** — Real-time status board showing pending, in-progress, and completed tasks
- **Priority Levels** — URGENT, HIGH, NORMAL, LOW with defined response times
- **Safety Rules** — Never deletes files (only moves), never sends messages without approval

## Getting Started

### Prerequisites

- [Obsidian](https://obsidian.md/) (free note-taking app)
- Python 3.8+ (for the file watcher)
- An AI assistant that can read/write files (e.g., Claude with Claude Code)

### Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/midhatnayab7-creator/AI-Employee-Vault.git
   ```

2. **Open in Obsidian**
   - Open Obsidian → "Open folder as vault" → select the cloned folder

3. **Edit Company Handbook**
   - Open `Company_Handbook.md` and fill in your name and business name

4. **Start the File Watcher**
   ```bash
   python file_watcher.py
   ```

5. **Drop a task into `/Inbox`**
   - Create any `.md` file with instructions (e.g., "Summarize this report", "Draft an email to John")
   - The file watcher will auto-move it to `/Needs_Action`

6. **Let Atlas work**
   - Point your AI assistant at the vault and let it follow `CLAUDE.md` instructions

## Example Tasks Atlas Can Handle

- Drafting professional emails (with approval before sending)
- Summarizing documents and reports
- Processing and organizing files
- Creating weather/data research reports
- Any task you define with a skill template

## Priority Levels

| Level | Response Time |
|---|---|
| URGENT | Immediately |
| HIGH | Within 4 hours |
| NORMAL | Within 24 hours |
| LOW | Within 1 week |

## Built With

- [Obsidian](https://obsidian.md/) — Vault and note management
- [Claude Code](https://claude.ai/) — AI agent runtime
- Python — File watcher automation

## Author

**Midhat Nayab** — [GitHub](https://github.com/midhatnayab7-creator)

---

*Built at Hackathon 0*
