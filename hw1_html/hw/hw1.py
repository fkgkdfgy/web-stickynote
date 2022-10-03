from flask import Flask, render_template, request
from element import Project,ProjectCols

id_manager={}

app = Flask(__name__)

info_template = ""
with open("./templates/info.html",mode="r") as f:
    info_template=f.read()

def sign_valid(req):
    if "id" in req.form and "password" in req.form:
        return True
    else:
        return False

def build_new_projects(form_dict):
    result_pc = ProjectCols()
    size = len(form_dict.getlist('index'))
    print('size:{}'.format(size))
    for i in range(size):
        tmp_project=Project(form_dict.getlist('pro_name')[i],\
                            form_dict.getlist('index')[i],\
                            form_dict.getlist('progress')[i],\
                            form_dict.getlist('status')[i],\
                            form_dict.getlist('history')[i])
        result_pc.projects.append(tmp_project)
    return result_pc

def projectcol_to_html(id,pc):
    result = info_template.replace("### ID_BLOCK",id)
    result = result.replace("### BODY_BLOCK",pc.to_html())  
    return result

@app.route("/single_web")
def sign_in_or_up():
    return render_template("sign_in.html")

@app.route("/info", methods=['POST'])
def info():
    print(request.form)
    if sign_valid(request):
        id = request.form['id']
        if "sign_in" in request.form:
            if id not in id_manager:
                return "没有这个用户"
            else:
                return projectcol_to_html(id,id_manager[id])
        elif "sign_up" in request.form:
            id_manager[id]=ProjectCols() 
            return projectcol_to_html(id,id_manager[id])
    elif 'upload' in request.form:
        id = request.form['id']
        id_manager[id]=build_new_projects(request.form)
        return projectcol_to_html(id,id_manager[id])
    elif 'download' in request.form:
        id = request.form['id']
        return projectcol_to_html(id,id_manager[id])
    elif 'add_new_line' in request.form:
        id = request.form['id']
        pc=id_manager[id]
        pc.add_project(Project())
        return projectcol_to_html(id,id_manager[id])
    else:
        return "没有这个用户"

if __name__ == '__main__':
    app.run(host='192.168.107.140',port=8080)
    