from flask import Flask, jsonify,make_response,request
app = Flask(__name__)
import Temp
path = '/api/v1.0'
temp = '''
 <div class="can-record-tab">
  <li class="float-left"><a id="food_tab" class="food-tab current" href="#" onclick="choose_to_food('2019-07-02')"></a></li>
</div>

<div class="can-record" id="can_record">
  <div id="food_record_wrap" class="food-record-wrap upper">
  <div class="food-progress" style="height:74px"></div>
    <div id="food_record" class="food-record">
      <div id="h1" class="record-panel current">
      <h2 class="record-title meal1" onclick="choose_one_time(1,'2019-07-02')">
        <span class="float-left" style="padding-right:10px;">早餐&nbsp;</span>
      <span class="float-left size12 lighter">(764大卡)</span>
      <span class="toggle float-right"></span>
        </h2>
        <div class="record-body">
        <table cellpadding="0" cellspacing="0">
          <tbody>

            <tr>
  <td class="name"><div class="limit" title="豆浆">豆浆</div></td>
  <td class="unit">
    <a class="unit-box" id="amount_37237130" onclick="edit_item_unit(37237130,1,'2019-07-02');" href="javascript:void(0);">
    <span class="limit">
      200
        毫升
    </span>
  </a>
  </td>
  <td class="cal"><div class="limit right" title="62.0大卡">62大卡</div></td>
  <td class="delete"><a href="#" onclick="$.ajax({async:true, data:'authenticity_token=' + encodeURIComponent('kuQRJWVfQu0JXMtS1k/tarmoL3B2XaqmHywMfjGbqpA='), success:function(request){$('#md_record').html(request);}, type:'post', url:'/can/remove_eating/37237130?date=2019-07-02&amp;et=1'}); return false;"></a></td>
</tr>


        </tbody></table>
      </div>
    </div> 
  </div>
  </div>  
</div>

<div class="can-result">
    <div class="sum float-left size14">
    <p class="divide5">饮食摄入<span class="stress">:</span> <span class="red1 stress">764</span> 大卡</p>
    
    </div>
    <div class="oper float-right">
      <p class="margin10">
        <a href="/assessment/can_save/8476544" class="red-button2" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'kuQRJWVfQu0JXMtS1k/tarmoL3B2XaqmHywMfjGbqpA='); f.appendChild(s);f.submit();return false;">保存到日记</a>
    </p>
    <p class="center">
      <a href="#" onclick="if (confirm('您确定清空饮食运动记录吗？')) { $.ajax({async:true, data:'authenticity_token=' + encodeURIComponent('kuQRJWVfQu0JXMtS1k/tarmoL3B2XaqmHywMfjGbqpA='), success:function(request){$('#md_record').html(request);}, type:'post', url:'/can/clear_record?date=2019-07-02&amp;et=1'}); }; return false;">清空</a>
    </p>
    </div>
</div>

<script type="text/javascript">
$(document).ready(function(){
      $("#h1").addClass("current");
});
</script> 
'''
tasks = [    #这是我们的数据
    {
        'id': 1,
        'data': 'data_1',
    },
    {
        'id': 2,
        'data': 'data_2',
    }
]
import Title
@app.route("/can/change_title/<int:id>",methods=["POST"])
def changeTitle(id):
    pagenum = request.args.get("pagenum")
    return Title.getTemp(id,int(pagenum));
@app.route("/can/add_eating/<int:commodity_id>",methods=["POST"])
def test1(commodity_id):
    # if commodity_id == 9999:
    #     print("clearn")
    #     return Temp.getXML({})
    print("*"*22)
    user_list = eval(request.args.get("date"))
    print(user_list,commodity_id)
    if commodity_id in user_list.keys():
        user_list[commodity_id] += 1
    else:
        user_list[commodity_id] = 1
    # print(commodity_id)
    return Temp.getXML(user_list)
    # return temp
@app.route("/can/clearn",methods=["POST"])
def clearn():
    return Temp.getXML({})


@app.route("/can/reduce/<int:id>",methods=["POST"])
def reduce(id):
    user_list = eval(request.args.get("date"))
    if id in user_list.keys():
        if user_list[id] == 1:
            user_list.pop(id)
        else:
            user_list[id] -= 1
    return Temp.getXML(user_list)
@app.route("/can/reduce_all/<int:id>",methods=["POST"])
def reduce_all(id):
    user_list = eval(request.args.get("date"))
    if id in user_list.keys():
        user_list.pop(id)
    return Temp.getXML(user_list)

@app.route("/",methods=["get"])
def index():
    return app.send_static_file("2.html")

@app.route(path + '/tasks', methods=['GET'])  #获取全部列表
def getTasks():
    return jsonify({"tasks":tasks})

@app.route(path + '/tasks/<int:task_id>', methods=['GET']) #获取相应ID的列表
def getTaskById(task_id):
    for solo in tasks:
        if solo["id"] == task_id:
            return jsonify({"tasks":solo})
    return not_found({'error': 'Not found'})

@app.route(path + '/tasks', methods=['POST']) #创建新数据
def createTask():

    if not request.json or not 'data' in request.json: #入参判断
        return error_request("Resquest Data Error")
    task = {
        'id': tasks[-1]['id'] + 1,  #ID自增
        'data': request.json['data'],
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route(path + '/tasks/<int:task_id>', methods=['PUT'])  #更新数据
def updataTask(task_id):
    if not request.json or not 'data' in request.json : #入参判断
        return error_request("Resquest Data Error")
    for solo in tasks:
        if solo["id"] == task_id:  #id遍历查询
            solo["data"] = request.json["data"] #更新数据
            return jsonify({"tasks":tasks})
    return not_found("id %s not found"%(str(task_id))) #未找到相关id 返回 404

@app.route(path + '/tasks/<int:task_id>', methods=['DELETE'])  #删除数据
def deleteTask(task_id):
    for solo in tasks:
        if solo["id"] == task_id:
            tasks.remove(solo)
            return jsonify({"tasks":tasks})
    return not_found("id %s not found"%(str(task_id)))

@app.errorhandler(404)   #重写404
def not_found(error):
    return make_response(jsonify(error), 404)
@app.errorhandler(400)  #重写400
def error_request(error):
    return make_response(jsonify(error), 400)

if __name__ == '__main__':
    app.run()