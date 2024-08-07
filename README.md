﻿# Intro to Applied Data Science Project 2

## Description

This is a web application built with a React frontend and FastAPI + Python backend. It allows users to compare two PDF documents using OpenAI's ChatGPT.
It is intended for use by urban planners and other professionals in assessing bid responses to a Request for Proposal (RFP).
PDF files are parsed locally using PyPDF.
Users can freely use my code and deploy their own version, but will need an OpenAI API key to do so.
This version is hosted online at https://pdf-compare-tool.vercel.app/ where you can try it for free. However, it will be limited when used in this way because use of my key incurs real costs.

The frontend is hosted on Vercel and the backend is on render.com, running in the free tier. The server is slow to spin up, spin down, and to process pdf documents- expect a request to take 2+ minutes. If the "Submit" button is greyed out, it is working!

## Installation

### Prerequisites

- Node.js and npm
- Python and pip

### Steps

1. Clone the repository.
2. Navigate to the project directory. 
3. Install the required Python packages using `pip install -r requirements.txt`.
3. Navigate to /my-app, then install the required npm packages using `npm install`.

## Usage

1. Start the FastAPI server. (`python main.py`)
2. Start the React application. (Navigate to /my-app and run `npm start`)
3. Open the application in a web browser.
4. Follow the on-screen instructions to use the application.
