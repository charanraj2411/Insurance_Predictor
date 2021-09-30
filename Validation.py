from result_calculate import calc_output

text_cols_map = {
    'Sex' : {'Female':0,'Male':1},
    'Smoke' : {'Yes':1,'No':0},
    'Region' : {'southwest':3,'southeast':2,'northwest':1,'northeast':0}
}

text_cols = ['Sex','Smoke','Region']


def form_response(data_req):
    for col,val in data_req.items():
        if col in text_cols:
            data_req[col]=text_cols_map[col][val]
    return calc_output(data_req)

     


