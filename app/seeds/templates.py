from app.models import db, Template, environment, SCHEMA
from sqlalchemy.sql import text

def seed_templates():
    templates = [
        {'template_id': 1, 'name': 'Getting Started Template'},
        {'template_id': 2, 'name': 'List Template'},
        {'template_id': 3, 'name': 'Reading List Template'},
        {'template_id': 4, 'name': 'To-Do Template'},
        {'template_id': 5, 'name': 'Code Block Template'},
        {'template_id': 6, 'name': 'Tables Template'},
    ]

    for template in templates:
        db.session.add(Template(
            template_id = template['template_id'],
            name = template['name'],
        ))

    db.session.commit()

def undo_templates():
    if environment == "production": 
        db.session.execute(f"TRUNCATE table {SCHEMA}.Templates RESTART IDENTITY CASCADE;")
    else: 
        db.session.execute(text("DELETE FROM Templates"))
    
    db.session.commit()