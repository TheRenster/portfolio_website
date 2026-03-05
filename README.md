# Personal Portfolio Website | Lauren Knox (TheRenster)

This repository contains the source code and assets for my personal portfolio website — a single-page app that showcases my background, projects, and contact information. Hosted on Google Cloud Run.

## What's in this repo (and why you might care)

- **`portfolio_website.py`** — The main Streamlit app: all pages, layout, and UI logic live here, including a contact form backed by SMTP for email delivery.
- **Project image assets** (`crypto arbitrage image.png`, `dnc_image.png`, `ff_image.png`, etc.) — Visuals used to showcase featured projects on the site.
- **Personal assets** (`Headshot.jpg`, `resume.pdf`, `droplet_portfolio.pdf`) — Supporting files displayed or linked from the portfolio.
- **`clarity_context_logo.png`** — Logo asset for the Clarity Context project.
- **`.github/workflows/`** — A keepalive workflow that pings the hosted app to prevent it from spinning down due to inactivity.
- **`website_pinger/`** — A supplementary script for monitoring the site's uptime and availability.
- **`.devcontainer/`** — Dev container configuration for a consistent local development environment.

## If you're interested in:

- How to build and structure a personal portfolio as a Python web app,
- How to wire up a contact form with SMTP secrets in Streamlit, or
- How to deploy a Streamlit app to Google Cloud Run,

then this repo is a practical, real-world example. If you're looking for a framework-agnostic or JavaScript-based portfolio template, this won't be the right fit.

## High-level structure

- `portfolio_website.py` — Main app entry point
- `*.jpg / *.png` — Image assets for projects and personal branding
- `resume.pdf`, `droplet_portfolio.pdf` — Downloadable documents
- `.github/workflows/` — Automation for keepalive pinging
- `website_pinger/` — Uptime monitoring script
- `.devcontainer/` — Dev environment configuration
