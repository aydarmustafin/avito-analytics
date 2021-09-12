#!/usr/bin/env python
# coding: utf-8

# In[35]:


from IPython.display import Image


def step2_no_umbrella():
    print(
        '\nА на улице 🌃 есть дождик? 💦'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        print('\n\nя же заболею ты че')
        display(Image(
            url='https://bit.ly/3lkXUKD',
            width=400))
    else:
        print('\n\nооо тогда пойду нажруся')
        display(Image(
            url='https://bit.ly/3nsEC90',
            width=400))


def step2_umbrella():
    print(
        '\nА на улице 🌃 есть дождик? 💦'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        print('\n\nок пойду нажруся')
        display(Image(
            url='https://bit.ly/3tBSvTj',
            width=400))
    else:
        print('\n\nтогда зачем мне зонтик лее ты чее ээ')
        display(Image(
            url='https://bit.ly/2YRu60Q',
            width=400))


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()


# In[ ]:





# In[ ]:




