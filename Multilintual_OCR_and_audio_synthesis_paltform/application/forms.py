from wtforms import TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length


# import utils
import utils


languages_choice = []
for key, value in utils.languages.items():
    languages_choice.append((key, value))
    


class filed_data(FlaskForm):
    data_field = TextAreaField('Data', 
                            validators=[DataRequired(), 
                            Length(min=1, max=1000)]
    )
    language = SelectField("Language to translate to", choices=languages_choice)
    submit = SubmitField('Translate') 