# Recipe App

## Overview
A web application for managing and sharing recipes, built using Flask.

## Features
- User registration and login
- Create, edit, and delete recipes
- View recipes with pagination
- Search recipes by title or ingredients

## Endpoints
- `/register`: User registration
- `/login`: User login
- `/logout`: User logout
- `/recipe/new`: Create a new recipe
- `/recipe/<int:id>`: View and edit a recipe
- `/recipe/<int:id>/delete`: Delete a recipe

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd recipe_app
