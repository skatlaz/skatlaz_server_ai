Claro. Abaixo está uma versão mais profissional, moderna e orientada ao GitHub para o **README.md principal do Skatlaz Server AI 2.0**, focada em arquitetura, MCPs, RAG, agentes, Ollama e automação empresarial.

# 🚀 Skatlaz Server AI 2.0

> Enterprise AI Platform for Agents, MCPs, RAG, Automation, Multimedia Processing and Local LLM Infrastructure.

![Version](https://img.shields.io/badge/version-2.0-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Django](https://img.shields.io/badge/django-5.x-darkgreen)
![License](https://img.shields.io/badge/license-Open%20Source-brightgreen)

---

# 🌎 Overview

Skatlaz Server AI 2.0 is a modular Artificial Intelligence platform designed to orchestrate Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), intelligent agents, automation workflows, multimedia pipelines, and domain-specific MCP Servers.

The platform can operate entirely on-premises using local models through Ollama or connect to cloud providers such as Gemini and OpenAI-compatible APIs.

Designed for organizations, developers, educators, researchers, and content creators, Skatlaz Server AI provides a unified environment for AI-powered workflows.

---

# 🧠 Core Features

## AI Chat Platform

* Multi-session conversations
* Persistent context
* Agent orchestration
* Multi-provider routing
* Chat history management

---

## MCP Server Architecture

MCP stands for:

**Modular Cognitive Processor**

Each MCP extends the platform with specialized knowledge and capabilities.

Examples:

* Programming
* Finance
* Education
* Multimedia
* Sports
* Research
* Automation
* Entertainment

---

## RAG Engine

Built-in Retrieval-Augmented Generation system.

Features:

* Document indexing
* Vector search
* Knowledge collections
* Semantic retrieval
* Chunk management
* Source tracking

Supported sources:

* PDF
* DOCX
* TXT
* HTML
* RSS
* XML
* JSON
* Websites
* APIs

---

## Fine-Tuning Framework

Prepare datasets and training jobs for:

* LoRA
* QLoRA
* Transformers
* Ollama-compatible exports

Supported outputs:

* Safetensors
* GGUF
* Model Packages

---

## Agent Framework

Create intelligent agents with:

* Custom prompts
* RAG collections
* MCP integrations
* Multi-step workflows
* Context memory

---

# 🏗️ Architecture

```text
User
  │
  ▼
Skatlaz Server AI
  │
  ▼
Prompt Router
  │
  ▼
Agent Layer
  │
  ▼
MCP Router
  │
  ├── Entertainment MCP
  ├── GexProg MCP
  ├── Office Worker MCP
  ├── Music Producer MCP
  ├── OpenStudio MCP
  ├── Studies MCP
  ├── Finance MCP
  ├── SurfTask MCP
  └── WorldSports MCP
  │
  ▼
RAG Engine
  │
  ▼
LLM Providers
  │
  ▼
Response
```

---

# 📦 Included Components

## AI Core

Main orchestration layer.

Features:

* Providers
* Agents
* Prompt Templates
* Chat Sessions
* Chat Messages
* Analytics
* RAG Collections

---

## Web Diver

Integrated web crawler.

Capabilities:

* Website extraction
* Metadata collection
* Content summarization
* HTML processing
* RSS feeds

---

## MCP Manager

Install and manage MCP packages.

Supports:

* Dynamic loading
* Version control
* Agent integration
* Custom workflows

---

## Analytics

Track usage by:

* Date
* Country
* Region
* Browser
* Operating System
* Language
* Origin

---

# 🔌 Supported LLM Providers

## Local Models

* Ollama
* DeepSeek
* DeepSeek-Coder
* Mistral
* Llama
* Qwen
* Gemma

---

## Cloud Providers

* Gemini
* OpenAI Compatible APIs
* OpenRouter Compatible APIs

---

# 🎬 Multimedia Processing

Through OpenStudio MCP and Music Producer MCP.

## Video

* Editing
* Filters
* Effects
* Subtitle generation
* Audio extraction

Supported formats:

* MP4
* MKV
* WEBM

---

## Audio

* Stem separation
* AI mastering
* Voice processing
* Speech-to-Text
* Text-to-Speech
* Backing vocals

Supported formats:

* WAV
* MP3
* FLAC
* OGG

---

## Images

* AI generation
* OCR
* Thumbnail generation
* Posters
* Book covers
* Marketing assets

Supported formats:

* PNG
* JPG
* WEBP

---

# 📚 MCP Ecosystem

Official MCP modules:

| MCP                  | Purpose                            |
| -------------------- | ---------------------------------- |
| Entertainment MCP    | Movies, TV Shows, Music            |
| GexProg MCP          | Programming & Software Engineering |
| InfoToday MCP        | Research & Public Information      |
| Music Producer MCP   | Audio Production                   |
| Office AI Worker MCP | Documents & Productivity           |
| Money MCP            | Finance & Statistics               |
| OpenStudio MCP       | Multimedia Processing              |
| Studies MCP          | Education & Learning               |
| SurfTask MCP         | Web Scraping & Automation          |
| WorldSports MCP      | Sports Analytics                   |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/skatlaz/skatlaz_server_ai.git

cd skatlaz_server_ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create administrator:

```bash
python manage.py createsuperuser
```

Start server:

```bash
python manage.py runserver
```

Access:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 📡 Main Endpoints

| Endpoint              | Description      |
| --------------------- | ---------------- |
| /ask/                 | Ask AI           |
| /search/              | Search Knowledge |
| /train/               | Dataset Training |
| /feeds/               | RSS Processing   |
| /admin/               | Administration   |
| /ai/chat/             | Chat API         |
| /ai/models/list/      | Available Models |
| /ai/rag/search/       | Vector Search    |
| /ai/rag/index-source/ | Index Documents  |
| /ai/crawler/start/    | Start Web Diver  |
| /ai/finetune/prepare/ | Prepare Training |
| /ai/ollama/export/    | Export Models    |

---

# 🛡️ Enterprise Features

* Local AI Infrastructure
* Multi-Agent Architecture
* RAG Collections
* Fine-Tuning Management
* MCP Ecosystem
* Analytics Dashboard
* Role-Based Access
* API Integrations
* Multimedia Pipelines
* Automation Workflows

---

# 🚀 Roadmap

## Version 2.x

* Advanced MCP ecosystem
* Improved RAG engine
* Enhanced analytics
* Multimedia improvements
* Workflow automation

## Version 3.0

Planned features:

* DeepSeek-Code native integration
* Autonomous AI Agents
* Visual Workflow Builder
* Android Support
* iOS Support
* Distributed Agent Network
* AI Software Engineering Assistant
* Katlaz++ Integration

---

# 📜 License

Developed by Skatlaz.

This software is Open Source and Freeware.

You are free to study, modify, distribute and use the software according to the license included with the project.

---

# 🌐 Skatlaz

Website:

[https://skatlaz.com](https://skatlaz.com)

Contact:

[https://skatlaz.com/en/contact/](https://skatlaz.com/en/contact/)

Technology • Artificial Intelligence • Automation • Research

© Skatlaz Digi-AI Office

# 🧠 Prompt Engineering Guide

The Skatlaz Server AI 2.0 platform was designed to operate through natural language instructions.

Users can interact with the system using prompts, commands, tasks, workflows and AI agents.

Prompt Structure is a guide for configure MCPs Server on Skatlaz Server AI 2.0 like a prompt examples.

---

# Prompt Structure

A prompt can be as simple as:

```text
Create a website for a bakery.
```

Or highly structured:

```text
Task: Create a Django application

Requirements:
- Authentication
- PostgreSQL
- Bootstrap UI
- REST API

Output:
- Project structure
- Source code
- Documentation
```

---

# General Commands

## Ask

```text
Ask:
Explain what Retrieval Augmented Generation is.
```

## Search

```text
Search:
Latest news about Artificial Intelligence.
```

## Summarize

```text
Summarize:
This PDF document.
```

## Translate

```text
Translate:
Portuguese to English.
```

## Analyze

```text
Analyze:
Attached financial spreadsheet.
```

---

# Software Development Commands

Powered by GexProg MCP.

---

## Create Project

```text
Create a Python project for inventory management.
```

```text
Create a Django CRM system.
```

```text
Create a FastAPI REST API.
```

---

## Generate Code

```text
Generate Python code for image processing.
```

```text
Generate a React dashboard.
```

```text
Generate a Flutter mobile application.
```

---

## Debug Code

```text
Debug this source code.
```

```text
Find memory leaks in this application.
```

```text
Optimize this SQL query.
```

---

## Refactor Code

```text
Refactor this application using Clean Architecture.
```

```text
Convert procedural code to object-oriented code.
```

---

# Research Commands

Powered by InfoToday MCP.

---

## Academic Research

```text
Research:
Quantum Computing.
```

```text
Research:
Large Language Models.
```

---

## Create Report

```text
Create a report about renewable energy.
```

---

## Extract Citations

```text
Extract references from this document.
```

---

# RAG Commands

---

## Index Documents

```text
Index this PDF into the knowledge base.
```

```text
Create a RAG collection named "Engineering".
```

---

## Search Knowledge Base

```text
Search the Engineering collection.
```

```text
Find information about transformers.
```

---

## Generate Answer Using RAG

```text
Answer using the Engineering collection.
```

---

# Office AI Worker Commands

---

## Generate Documents

```text
Create a business proposal.
```

```text
Create a technical report.
```

```text
Create a project presentation.
```

---

## Spreadsheet Analysis

```text
Analyze this spreadsheet.
```

```text
Generate charts from this data.
```

---

## OCR

```text
Extract text from this image.
```

```text
Convert scanned PDF into searchable text.
```

---

# Music Producer Commands

---

## Audio Analysis

```text
Analyze this audio file.
```

---

## Stem Separation

```text
Separate vocals, drums, bass and instruments.
```

---

## Mastering

```text
Master this song for streaming platforms.
```

---

## AI Music Generation

```text
Create a blues guitar backing track.
```

```text
Generate progressive rock keyboard arrangements.
```

---

# OpenStudio Commands

---

## Image Generation

```text
Create a book cover.
```

```text
Generate a movie poster.
```

```text
Generate a website banner.
```

---

## Video Processing

```text
Generate subtitles for this video.
```

```text
Extract audio from this video.
```

---

## Voice Generation

```text
Create narration for this ebook.
```

---

# Education Commands

Powered by Studies MCP.

---

## Quiz Creation

```text
Create a quiz about Physics.
```

---

## Study Plan

```text
Create a 30-day study plan for Machine Learning.
```

---

## Educational Content

```text
Explain Neural Networks.
```

```text
Create a presentation about Data Science.
```

---

# Web Automation Commands

Powered by SurfTask MCP.

---

## Website Analysis

```text
Analyze this website.
```

---

## Web Scraping

```text
Extract all article titles from this website.
```

---

## Monitoring

```text
Monitor this website every day.
```

---

# Agent Commands

---

## Create Agent

```text
Create an Engineering Agent.
```

```text
Create a Financial Analyst Agent.
```

---

## Assign Knowledge Base

```text
Attach Engineering collection to agent.
```

---

## Execute Task

```text
Ask Engineering Agent:
Create a Django application with PostgreSQL.
```

---

# MCP Task Commands

Generic MCP execution syntax:

```text
Task Type: code
Language: Python
Target OS: Windows

Prompt:
Create a desktop application.
```

```text
Task Type: debug
Language: C#
Target OS: Linux

Prompt:
Find errors in this source code.
```

```text
Task Type: documentation
Language: HTML

Prompt:
Generate technical documentation.
```

---

# Best Practices

* Use clear objectives.
* Specify expected outputs.
* Include file formats.
* Include target platforms.
* Attach reference documents when possible.
* Use RAG collections for domain-specific knowledge.
* Use specialized MCPs whenever available.
* Break large projects into smaller tasks.

---

# Example Complete Prompt

```text
Task Type: code

Language: Python

Target OS: Windows

Framework:
Django

Database:
PostgreSQL

Requirements:
- Authentication
- Dashboard
- REST API
- Reporting

Output:
- Source code
- Documentation
- Installation guide

Generate complete project.
```
