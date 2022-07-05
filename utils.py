"""
Kniznica Utils
"""
        
def dict_to_model(model, data):
	"""
	Prevedie a ulozi data z json formatu do objektu
	_id sa ignoruje

	:param model:	model, ktory chceme nacitat
	:param data:	data vo formate json
	:return:		vrati Model s ulozenymi datami z data
	"""
	if data and len(data) > 0: 
		for c in model.__table__.columns:
			if c.name not in ['_id']:
				val = data.get(c.name)
				setattr(model, c.name, val)
	
	return model

