#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2023/6/13 11:17
@Author   : ji hao ran
@File     : sascader.py
@Project  : StreamlitAntdComponentsDemo
@Software : PyCharm
"""
from ..utils import *


def sidebar():
    label = st.selectbox('label', [None, 'label'])
    index = st.selectbox('index', [None, 0, [1, 3, 6, 7]])
    format_func = st.selectbox('format_func', FORMAT, 1)
    placeholder = st.text_input('placeholder', 'Please choose')
    multiple = st.checkbox('multiple')
    disabled = st.checkbox('disabled')
    search = st.checkbox('search')
    clear = st.checkbox('clear')
    strict = st.checkbox('strict')
    return_index = st.checkbox('return_index')
    return update_kw(locals())


def main(kw):
    return_index = kw.get('return_index')
    item = sac.cascader(items=[
        sac.CasItem('home', icon='house'),
        sac.CasItem('app', icon='app', children=[
            sac.CasItem('store', icon='bag-check'),
            sac.CasItem('brand', icon='award', children=[
                sac.CasItem('github', icon='github'),
                sac.CasItem('google', icon='google'),
                sac.CasItem('apple', icon='apple', children=[
                    sac.CasItem('admin', icon='person-circle'),
                    sac.CasItem('guest', icon='person'),
                    sac.CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        sac.CasItem('disabled', icon='send', disabled=True),
    ], **kw)
    st.write(f'The selected cascader item {"index" if return_index else "label"} : {item}')
    show_code(f'''
    sac.cascader(items=[
        sac.CasItem('home', icon='house'),
        sac.CasItem('app', icon='app', children=[
            sac.CasItem('store', icon='bag-check'),
            sac.CasItem('brand', icon='award', children=[
                sac.CasItem('github', icon='github'),
                sac.CasItem('google', icon='google'),
                sac.CasItem('apple', icon='apple', children=[
                    sac.CasItem('admin', icon='person-circle'),
                    sac.CasItem('guest', icon='person'),
                    sac.CasItem('twitter' * 5, icon='twitter'),
                ]),
            ]),
        ]),
        sac.CasItem('disabled', icon='send', disabled=True),
    ], {code_kw(kw)})
    ''', True)


def api():
    st.help(sac.cascader)
    st.help(sac.CasItem)


CASCADER_DEMO = {
    'cascader': {
        'sidebar': sidebar,
        'main': main,
        'api': api
    }
}