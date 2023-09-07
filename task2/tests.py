from bs4 import BeautifulSoup

from utils import load
from solution import find_content_elements


def test_load_404():
	r = load('https://google.com/not/found/url')
	assert r is None

def test_find_content_elements_1():
	e = BeautifulSoup('<div class="mw-category-group">' +
		'<h3>Test</h3>' + '<ul>  <li></li>   <li></li>    </ul>'
	'</div>', features="html.parser")
	elements = find_content_elements(e)
	assert elements == {'Test': 2}


def test_find_content_elements_2():
	e = BeautifulSoup('<div class="mw-category-group">'
		'<h3>Test</h3> <ul>   <li></li>    </ul>'
	'</div>'
	'<div class="mw-category-group">' +
		'<h3>Test 2</h3>   <ul>  <li></li>   <li></li>    </ul>'
	'</div>'
	, features="html.parser")
	elements = find_content_elements(e)
	assert elements == {'Test': 1, 'Test 2': 2}
