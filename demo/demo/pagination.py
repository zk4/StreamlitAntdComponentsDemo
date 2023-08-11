#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/8/9 15:22
@Author   : ji hao ran
@File     : pagination.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def sidebar():
    total = st.number_input('total', 0, 200, 100, 50)
    index = st.selectbox('index', [1, 2])
    page_size = st.number_input('page_size', 5, 20, 10, 5)
    align = st.selectbox('align', ["start", "center", "end"], 1)
    circle = st.checkbox('circle')
    disabled = st.checkbox('disabled')
    jump = st.checkbox('jump', True)
    simple = st.checkbox('simple')
    show_total = st.checkbox('show_total', True)
    return locals()


def main(kw):
    r = sac.pagination(**kw)
    st.write(f'The selected pagination number is: {r}')
    show_code(f'''
    sac.pagination({code_kw(kw)})
    ''', True)


def api():
    st.help(sac.pagination)


PAGINATION_DEMO = {
    'pagination': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}