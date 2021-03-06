#from . import meal_crawl
import datetime

###### form

def get_form(place, data):
    today = str(datetime.date.today().month) + '월' + str(datetime.date.today().day) + '일'
    #print("data: ", data[12], data[25])
    menu_text_2 = '제2학생회관('+today+')\n' \
        '>학생식단(백반) ' + data[13].split()[0] + '원\n' \
        + make_menu(data[12]) + \
        '\n>교직원식당 ' + data[19].split()[0] + '원\n' \
        + make_menu(data[18]) + \
        '\n>학생식당(일품)\n' \
        + make_menu_ilpum(data[25]) + '\n'
    menu_text_3 = '제3학생회관('+today+')\n' \
        '교직원식당 ' + data[19].split()[0] + '원\n' \
        + make_menu(data[18]) + '\n'

    if place == '취업지원회관':
        return menu_text_2
    elif place == '제3학생회관':
        return menu_text_3
    else:
        return 'meal error'

def make_menu(data):
    str='\t'
    for key in data.split():
        if key =='(pork' or key=='(beef' or key=='(pork,' or key=='beef' or key=='null':
            continue
        elif key =='included)':
            continue
        str += key +'\n\t'

    return str

def make_menu_ilpum(data):
    i=0;
    iscontinue=False
    str='\t'
    for key in data.split():
        if key=='(pork' or key=='(beef' or key=='(pork,' or key=='beef' or key=='null':
            continue
        elif key == 'included)':
            iscontinue=True
            continue
        elif iscontinue == True:
            iscontinue=False
            continue

        if i%2==1:
            str += key+'원\n\t'
        else :
            str += key+'\t'
        i += 1

    return str