try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
    
config = {
    'description':'Linkchecker',
    'author':'Kelly Hair',
    'url':'https://github.com/kellyhair/linkchecker/',
    'download_url':'https://github.com/kellyhair/linkchecker/',
    'author_email':'kelly@routerlab.net',
    'version':'0.1',
    'install_requires':['nose'],['pyping']
    'packages': ['linkchecker'],
    'scripts':[],
    'name':'linkchecker'
    }
    

setup(**config)

    
    
    