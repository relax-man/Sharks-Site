from flask import Blueprint, render_template, redirect, request
from werkzeug.utils import secure_filename
import os

from db import db
from models import Shark, Oceanarium, CageDivingPlace


main = Blueprint('main', __name__)

# GET

@main.route('/')
def index():
    return render_template('pages/index.html')

@main.route('/sharks-types')
def sharks_types():
    sharks = Shark\
        .query\
        .order_by(Shark.pk.desc())\
        .all()
    return render_template(
        'pages/sharks-types.html',
        sharks=sharks
    )

@main.route('/nutrition')
def nutrition():
    return render_template('pages/nutrition.html')

@main.route('/habitats')
def habitats():
    return render_template('pages/habitats.html')

@main.route('/statistic')
def statistic():
    return render_template('pages/statistic.html')

@main.route('/facts')
def facts():
    return render_template('pages/facts.html')

@main.route('/oceanariums')
def oceanariums():
    oceanariums = Oceanarium\
        .query\
        .order_by(Oceanarium.pk.desc())\
        .all()
    return render_template(
        'pages/oceanariums.html',
        oceanariums=oceanariums
    )

@main.route('/cage-diving')
def cage_diving():
    cage_diving_places = CageDivingPlace\
        .query\
        .order_by(CageDivingPlace.pk.desc())\
        .all()
    return render_template(
        'pages/cage-diving.html',
        cage_diving_places=cage_diving_places
    )

@main.route('/protection-methods')
def protection_methods():
    return render_template('pages/protection-methods.html')

# DETAIL

@main.route('/sharks-types/<int:pk>')
def shark_type_detail(pk):
    shark = Shark.query.get(pk)
    return render_template('detail/shark.html', shark=shark)

# POST

SHARKS_IMAGES_UPLAOD_FOLDER = 'img\\shark-types\\upload-images'
OCEANARIUMS_IMAGES_UPLAOD_FOLDER = 'img\\oceanariums\\upload-images'

@main.route('/add-shark-type', methods=['POST'])
def add_shark_type():
    name = request.form.get('name')
    description = request.form.get('description')
    img = request.files.get('img')
    img_path = None
    video_id = request.form.get('video_id')

    if not name or not description:
        return redirect('/sharks-types')

    if img and img.filename:
        filename = secure_filename(img.filename)
        img_path = os.path.join(SHARKS_IMAGES_UPLAOD_FOLDER, filename)
        img.save(os.path.join('static', img_path))
        img_path = img_path.replace('\\', '/')

    shark_instance = Shark(
        name=name,
        description=description,
        img_path=img_path,
        video_id=video_id
    )
    db.session.add(shark_instance)
    db.session.commit()

    return redirect('/sharks-types')


@main.route('/add-oceanarium', methods=['POST'])
def add_oceanarium():
    name = request.form.get('name')
    description = request.form.get('description')
    img = request.files.get('img')
    img_path = None
    iframe_src = request.form.get('frame_src')

    if not name or not description or not iframe_src:
        return redirect('/oceanariums')

    if img and img.filename:
        filename = secure_filename(img.filename)
        img_path = os.path.join(OCEANARIUMS_IMAGES_UPLAOD_FOLDER, filename)
        img.save(os.path.join('static', img_path))
        img_path = img_path.replace('\\', '/')

    oceanarium_instance = Oceanarium(
        name=name,
        description=description,
        img_path=img_path,
        iframe_src=iframe_src
    )
    db.session.add(oceanarium_instance)
    db.session.commit()

    return redirect('/oceanariums')

@main.route('/add-cage-diving-place', methods=['POST'])
def add_cage_deiving_place():
    name = request.form.get('name')
    description = request.form.get('description')
    iframe_src = request.form.get('frame_src')

    if not name or not description or not iframe_src:
        return redirect('/cage-diving')

    cage_diving_place_instance = CageDivingPlace(
        name=name,
        description=description,
        iframe_src=iframe_src
    )
    db.session.add(cage_diving_place_instance)
    db.session.commit()

    return redirect('/cage-diving')

# Filters

@main.app_template_filter('add_linebreaks')
def add_linebreaks(s):
    return s.replace('\n', '<br>')
