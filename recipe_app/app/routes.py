# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Recipe, db
from .forms import RecipeForm

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.paginate(page=page, per_page=5)
    return render_template('index.html', recipes=recipes)

@bp.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, description=form.description.data, 
                        ingredients=form.ingredients.data, instructions=form.instructions.data, 
                        created_by=current_user.id)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('recipe_form.html', form=form)

@bp.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        abort(403)
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        db.session.commit()
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.description.data = recipe.description
        form.ingredients.data = recipe.ingredients
        form.instructions.data = recipe.instructions
    return render_template('recipe_form.html', form=form)

@bp.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('main.index'))
