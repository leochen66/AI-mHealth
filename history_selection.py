from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class Selection(FlaskForm):
	date = SelectField('選擇日期:',choices=[
		('7/26','7/26'),
		('7/27','7/27'),
		('7/28','7/28'),
		('7/29','7/29'),
		('7/30','7/30'),
		('7/31','7/31'),
		('ALL','ALL'),
		])
	begin_time = SelectField('起始時間:',choices=[
		(0,'00:00'),
		(1,'01:00'),
		(2,'02:00'),
		(3,'03:00'),
		(4,'04:00'),
		(5,'05:00'),
		(6,'06:00'),
		(7,'07:00'),
		(8,'08:00'),
		(9,'09:00'),
		(10,'10:00'),
		(11,'11:00'),
		(12,'12:00'),
		(13,'13:00'),
		(14,'14:00'),
		(15,'15:00'),
		(16,'16:00'),
		(17,'17:00'),
		(18,'18:00'),
		(19,'19:00'),
		(20,'20:00'),
		(21,'21:00'),
		(22,'22:00'),
		(23,'23:00'),
		(24,'24:00'),
		])
	duration = SelectField('經過時間:',choices=[
		(1,'1小時'),
		(3,'3小時'),
		(6,'6小時'),
		(12,'12小時'),
		(24,'整天')
		])
