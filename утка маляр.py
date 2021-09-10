#!/usr/bin/env python
# coding: utf-8

# In[35]:


from IPython.display import Image


def step2_no_umbrella():
    print('\n\n\nя же заболею ты че')
    display(Image(url='https://cs11.pikabu.ru/post_img/2018/12/17/8/1545050494117988750.jpg', width=500))


def step2_umbrella():
    print('\n\n\nкаеф не заболею')
    display(Image(url='https://www.meme-arsenal.com/memes/60e72b470dad02bbdbadeaa48faf2642.jpg', width=500))


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




