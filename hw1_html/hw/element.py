
def input(s_type,s_string,s_name):
    return '''<td> <input type="{}" value="{}" name="{}"></td>'''.format(s_type,s_string,s_name)

class Project:
    def __init__(self,name=None,index=-1,progress=0,status=None,history=None):
        self.name = name
        self.index = index
        self.progress=progress
        self.status = status
        self.history = history
        
    def to_html(self):
        index_in_html=input("number",self.index,"index")
        name_in_html=input("text",self.name,"pro_name")
        progress_in_html=input("number",self.progress,"progress")
        status_in_html=input("text",self.status,"status")
        history_in_html=input("text",self.history,"history")
        return index_in_html + name_in_html + \
               progress_in_html + status_in_html + \
               history_in_html
        
class ProjectCols:
    def __init__(self):
        self.projects = []
        
    def to_html(self):
        if len(self.projects)==0:
            return ""
        else:
            project_list = []
            for p in self.projects:
                project_list.append("<tr> {} </tr>".format(p.to_html()))
            return " ".join(project_list)
    