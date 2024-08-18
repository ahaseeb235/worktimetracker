from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SelectField, DateField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange

class UserInputForm(FlaskForm):
    # Name of employee
    name = StringField('Name of Employee', validators=[DataRequired()])

    # Time-in and Time-out fields
    time_in = TimeField('Time In', validators=[DataRequired()])
    time_out = TimeField('Time Out', validators=[DataRequired()])

    # Select month
    month = SelectField('Select Month', 
                        choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')],
                        validators=[DataRequired()])

    # Select date
    date = DateField('Select Date', format='%Y-%m-%d', validators=[DataRequired()])

    # Total hours worked for that day (read-only)
    total_hours_day = DecimalField('Total Hours Worked (Day)', 
                                   validators=[Optional(), NumberRange(min=0.0, max=24.0)], 
                                   places=2, 
                                   render_kw={'readonly': True})

    # Total hours for the month (read-only)
    total_hours_month = DecimalField('Total Hours Worked (Month)', 
                                     validators=[Optional(), NumberRange(min=0.0)], 
                                     places=2, 
                                     render_kw={'readonly': True})

    # Pick list for workday type
    workday_type = SelectField('Workday Type', 
                               choices=[('Worked', 'Worked'), ('Training', 'Training'), 
                                        ('Bank Holiday', 'Bank Holiday'), 
                                        ('Annual Leave', 'Annual Leave'), 
                                        ('Sick Leave', 'Sick Leave'), 
                                        ('Overtime', 'Overtime')],
                               validators=[DataRequired()])
    
    # Submit Field
    submit = SubmitField("Submit") 
     