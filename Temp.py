Empty = '''

 <div class="can-record-tab">
  <li class="float-left"><a id="food_tab" class="food-tab current" href="#" onclick="choose_to_food('2019-07-02')"></a></li>
</div>

<div class="can-record" id="can_record">
  <div id="food_record_wrap" class="food-record-wrap upper">
  <div class="food-progress" style="height:74px"></div>
    <div id="food_record" class="food-record">
      <div id="h1" class="record-panel current">
      <h2 class="record-title meal1" onclick="choose_one_time(1,'2019-07-02')">
        <span class="float-left" style="padding-right:10px;">菜单&nbsp;</span>
      <span class="float-left size12 lighter">(SUM大卡)</span>
      <span class="toggle float-right"></span>
        </h2>
        <div class="record-body">
        <table cellpadding="0" cellspacing="0">
          <tbody>

    SOLO


        </tbody></table>
      </div>
    </div> 
  </div>
  </div>  
</div>

<div class="can-result">
    <div class="sum float-left size14">
    <p class="divide5">饮食摄入<span class="stress">:</span> <span class="red1 stress">SUM</span> 大卡</p>

    </div>
    <div class="oper float-right">
      <p class="margin10">
        <a href="/assessment/can_save/8476544" class="red-button2" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'kuQRJWVfQu0JXMtS1k/tarmoL3B2XaqmHywMfjGbqpA='); f.appendChild(s);f.submit();return false;">保存到日记</a>
    </p>
    <p class="center">
      <a href="#"  onclick="clearn()">清空</a><a id="message" style="display: none;">all_dict</a>
    </p>
    </div>
</div>

<script type="text/javascript">
$(document).ready(function(){
      $("#h1").addClass("current");
});
</script> 
'''
Solo = '''
            <tr>
  <td class="name"><div class="limit" title="NAME">NAME</div></td>
  <td class="unit">
    <a class="unit-box" id="amount_37237130" onclick="reduce(ID)" href="#">
    <span class="limit">
      Single
        Company
    </span>
  </a>
  </td>
  <td class="cal"><div class="limit right" title="KLL大卡">KLL大卡</div></td>
  <td class="delete"><a href="#" onclick="reduce_all(ID)"></a></td>
</tr>

'''
Maping = {
    0: {"NAME": "椒盐小土豆", "KLL": 60, "Image": "","Company":"份","Single":1},
    1: {"NAME": "椒盐小土豆", "KLL": 60, "Image": "","Company":"份","Single":1},
    2: {"NAME": "千叶豆腐", "KLL": 50, "Image": "","Company":"份","Single":1},
    3: {"NAME": "千叶豆腐4", "KLL": 66, "Image": "","Company":"份","Single":1},
    4: {"NAME": "千叶豆腐5", "KLL": 66, "Image": "","Company":"份","Single":1},
    5: {"NAME": "千叶豆腐6", "KLL": 66, "Image": "","Company":"份","Single":1},
    6: {"NAME": "千叶豆腐7", "KLL": 66, "Image": "","Company":"份","Single":1},
    7: {"NAME": "千叶豆腐8", "KLL": 66, "Image": "","Company":"份","Single":1},
    8: {"NAME": "千叶豆腐9", "KLL": 66, "Image": "","Company":"份","Single":1},
    9: {"NAME": "千叶豆腐10", "KLL": 66, "Image": "","Company":"份","Single":1},
    10: {"NAME": "千叶豆腐11", "KLL": 66, "Image": "","Company":"份","Single":1},
    11: {"NAME": "千叶豆腐12", "KLL": 66, "Image": "","Company":"份","Single":1},
}
import copy
# {0:1,2:2}
def getXML(all_dict):
    temp = copy.deepcopy(Empty)
    kll = 0
    all_solo = ""
    for id in all_dict:
        solo = copy.deepcopy(Solo)
        solo = solo.replace("NAME",Maping[id]["NAME"])
        solo = solo.replace("KLL", str(Maping[id]["KLL"]*all_dict[id]))
        solo = solo.replace("Company", Maping[id]["Company"])
        solo = solo.replace("Single",str( Maping[id]["Single"]*all_dict[id]))
        solo = solo.replace("ID",str(id))
        kll += Maping[id]["KLL"]*all_dict[id]
        all_solo += solo
    temp = temp.replace("SUM",str(kll))
    temp = temp.replace("SOLO", all_solo)
    temp = temp.replace("all_dict",str(all_dict))
    return temp