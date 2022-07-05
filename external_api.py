"""
Modul pre Externe API
"""

import requests


def getExternalApi(key, id):
	"""
	Fukncia pre pracu s externym api
	Pokial je problem na serveri, alebo s datami, tak vrati chybovu hlasku

	:param key:		typ poziadavky, s ktorou checeme pracovat, posts, users..
	:param id:		id poziadavky, ktoru chceme ziskat
	:return:		vrati data vo formate json
	"""
	try:
		url = 'https://jsonplaceholder.typicode.com/{}/{}'.format(key, id)
		response = requests.get(url)
	except:
		#Ak vyhodi except, tak nastal problem s komunikaciou servera
		data = {'error': '', 'error': 'Chyba pri komunikacii s externym API!'}

	# Pokial vsetko vrati response, tak komunikacia s webom prebehla
	if 'response' in dir():
		# ak status_code je 200 tak stranka vratila pozadovane data
		if response.status_code == 200:
			try:
				#pokial su data v poriadku, tak sa prevedu zo stringu na format json
				data = response.json()
			except:
				data = {'error': 'Chyba pri spracovani dat z webu!'}
		# ak status_code je napr 404, tak poziadavka bola sice ok, ale server nema prisusne data
		elif response.status_code == 404:
				data = {'error': 'Chyba, externe API vracia prazne data, zle ID?'}
		else:
			data = {'error': 'Chyba pri nacitani dat z webu!'}

	return data


def getExternalApiPost(id):
	"""
	Funkcia vrati prispevok z externeho API
	Ak sa nenajde, vrati chybovu hlasku

	:param id:	id prispevku 
	:return:	vrati prispevok v json formate
	"""
	data = getExternalApi('posts', id)
	return data


def getExternalApiUser(id_user):
	"""
	Funkcia vrati pouzivatela z externeho API
	Ak sa nenajde, vrati chybovu hlasku

	:param id:	id pouzivatela
	:return:	vrati pouzivatela v json formate
	"""
	data = getExternalApi('users', id_user)
	return data

def getExternalApiPostForDB(limit=3):
	"""
	Funkcia vrati zoznam prispevkov z externeho API
	Je urcena pre naplnenie dat do databazy

	:param limit:	pocet prispevkov pre nacitanie z api
	:return:		vrati zoznam prispevkov v json formate
	"""
	data_all = []
	for _id in range(0, limit):
		data = getExternalApiPost(_id)
		# Ak sa najde error, tak preskoc
		if data and 'error' not in data:
			data_all.append(data)
	return data_all