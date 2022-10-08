function create_project(_content,_items=[])
{
    var content={'content':_content , 'items': _items, 'status': 0};   
    return content;
}

function get_attr(target,head)
{
    if(head in target)
    {
        return target[head];
    }
    return undefined;
}

function set_attr(target,head,value)
{
    if(head in target)
    {
        target[head]=value;
        return true;
    }
    return false;
}

function add_child(target,child)
{
    target['items'].append(child);
}

function get_child(target,index)
{
    if(index < get_attr(target,'items').length)
    {
        return get_attr(target,'items')[index];
    }
    else
    {
        return undefined;
    }
    
}

function create_project_with_tree(content,level,child_num)
{
    var node = create_project(content);
    if (level ==0)
    {
        return node;
    }
    for(var i=0;i<child_num;i++)
    {
        add_child(node,create_project_with_tree(content+'_'+String(i),level-1,child_num));
    }
    return node;
}

function create_project_with_tail(content,level)
{
    return create_project_with_tree(content,level,1);
}

function update_to_body_info()
{
    
}

function update_to_plane(project)
{
    // 更新 project_bar info
    var bar_node = document.querySelector('#project_bar .info');
    bar_node.innerHTML='';
    for(var i =0;i<get_attr(project,'items').length;i++)
    {
        var node = document.createElement('div');
        var project = get_attr(project)
        node.innerHTML = get_child(project,i);
        bar_node.appendChild(node);
    }
}

function download(){
    var manager = create_project('manager');
    manager.add_child(create_project_with_tail('hw_first',3));
    manager.add_child(create_project_with_tree('hw_second',3));
    update_to_plane(manager);
}
