
<img width="1596" height="694" alt="Screenshot From 2026-06-18 00-04-59" src="https://github.com/user-attachments/assets/31a8e1b2-0e8a-41f7-bde9-94053baeb8ee" />


# 🚀 Server Alert Monitor System

A comprehensive server and machine monitoring system with automatic failure detection, real-time alerts via Telegram and Gmail, and AI-powered analysis.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![n8n](https://img.shields.io/badge/n8n-automation-orange)
![License](https://img.shields.io/badge/license-MIT-blue)


## 🎯 Overview

**Server Alert Monitor System** is a proactive monitoring solution that automatically tests server availability, tracks system performance metrics, and triggers instant alerts when problems are detected. The system combines traditional monitoring with AI-powered analysis to provide intelligent recommendations and early warning detection.

### Key Capabilities
- **Server Testing**: 20 concurrent requests with performance analysis
- **System Monitoring**: CPU, RAM, Disk, and Temperature tracking
- **Smart Alerts**: Real-time notifications via Telegram and Gmail
- **AI Analysis**: Intelligent interpretation of system data
- **Historical Data**: Complete incident history stored in MySQL

## ✨ Features

### 🌐 Server Monitoring
- **Performance Testing**: 20 simultaneous requests with response time analysis
- **Availability Tracking**: Automatic detection of server downtimes
- **Success Rate**: Percentage calculation of successful requests
- **RPS Analysis**: Requests per second performance metric
- **Status Classification**: Server state determination (Very Stable / Stable / Unstable / Weak)

### 🖥 System Resource Monitoring
- **CPU Usage**: Real-time processor utilization tracking
- **Memory (RAM)**: Available and used memory monitoring
- **Disk Space**: Storage capacity and usage analysis
- **Temperature**: System thermal monitoring with warning zones

### 📊 Alert & Notification System
- **Telegram**: Instant push notifications with rich formatting
- **Gmail**: Detailed HTML email reports with full analysis
- **Database Storage**: Complete history of all incidents
- **Smart Filtering**: Only sends alerts when issues are detected

### 🤖 AI-Powered Analysis
- **Intelligent Interpretation**: Natural language analysis of system data
- **Anomaly Detection**: Identification of unusual patterns
- **Predictive Insights**: Early warning of potential issues
- **Actionable Recommendations**: Specific steps to resolve problems

## 🏗 Architecture
┌─────────────────────────────────────────────────────────────────────┐
│ Monitoring System Architecture │
├─────────────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────┐ ┌──────────────────────────────┐ │
│ │ Python │ │ n8n Workflow │ │
│ │ Script │──────────▶│ Automation Engine │ │
│ │ (main.py) │ │ │ │
│ │ │ │ ┌────────────────────────┐ │ │
│ │ ┌───────┐ │ │ │ Groq AI Model │ │ │
│ │ │Server │ │ │ │ (LLM Analysis) │ │ │
│ │ │Tests │ │ │ └────────────────────────┘ │ │
│ │ └───────┘ │ │ │ │ │
│ │ │ │ ▼ │ │
│ │ ┌───────┐ │ │ ┌────────────────────────┐ │ │
│ │ │System │ │ │ │ Alert Manager │ │ │
│ │ │Stats │ │ │ ├────────────────────────┤ │ │
│ │ └───────┘ │ │ │ • Telegram Bot │ │ │
│ └─────────────┘ │ │ • Gmail OAuth2 │ │ │
│ │ │ │ • MySQL Database │ │ │
│ │ │ └────────────────────────┘ │ │
│ └────────────────────┼──────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────┐ │
│ │ MySQL DB │ │
│ │ (History) │ │
│ └─────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
