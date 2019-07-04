import Temp
Maping = Temp.Maping
'''
1蔬菜 2肉类 3海鲜 4菇类 5饮品 6酱料 7套餐
'''
Maping = {
    1:{
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
        11: {"NAME": "千叶豆腐12", "KLL": 66, "Image": "","Company":"份","Single":1},},
    2:{
        0: {"NAME": "肉", "KLL": 60, "Image": "","Company":"份","Single":1},
        1: {"NAME": "肉1", "KLL": 60, "Image": "","Company":"份","Single":1},
        2: {"NAME": "肉2", "KLL": 50, "Image": "","Company":"份","Single":1},
        3: {"NAME": "肉3", "KLL": 66, "Image": "","Company":"份","Single":1},
        4: {"NAME": "肉4", "KLL": 66, "Image": "","Company":"份","Single":1},
        5: {"NAME": "肉5", "KLL": 66, "Image": "","Company":"份","Single":1},
        6: {"NAME": "6", "KLL": 66, "Image": "","Company":"份","Single":1},
        7: {"NAME": "7", "KLL": 66, "Image": "","Company":"份","Single":1},
        8: {"NAME": "8", "KLL": 66, "Image": "","Company":"份","Single":1},
        9: {"NAME": "9", "KLL": 66, "Image": "","Company":"份","Single":1},
        10: {"NAME": "0", "KLL": 66, "Image": "","Company":"份","Single":1},
        11: {"NAME": "11", "KLL": 66, "Image": "","Company":"份","Single":1},},
    }

Solo = '''
<div class="item-list-wrap">
	  	<div class="item-list" id="item_469_6">
	      <div class="illus">
		      <a href="/shiwu/pingguo_junzhi" target="_blank"><img src="Image"></a>
	      </div>
        <div class="intr size13">
          <dl>
            <dt class="stress">
            <span class="item-name float-left"><a href="/shiwu/pingguo_junzhi" target="_blank">NAME</a></span>
            </dt>
            <dd class="gray2">
            <span class="float-left limit" title="KLL大卡(每SingleCompany)" style="width:120px">KLL大卡(每SingleCompany)</span>
            </dd>
          </dl>
        </div>
        <div class="oper">
          <a class="add" href="#" onclick="dddd(ID)"></a>
        </div>
      </div>
    </div>
'''


Empty = '''
<ul class="can-tab center size13">
    <li class="meal1"><a href="javascript:void(0);" onclick="change_title(1,1)" class="CHANGE1">蔬菜</a></li>
    <li class="meal6"><a href="javascript:void(0);" onclick="change_title(2,1)" class="CHANGE2">肉类</a></li>
    <li class="meal2"><a href="javascript:void(0);" onclick="change_title(3,1)" class="CHANGE3">海鲜</a></li>
    <li class="meal7"><a href="javascript:void(0);" onclick="change_title(4,1)" class="CHANGE4">菇类</a></li>
    <li class="meal3"><a href="javascript:void(0);" onclick="change_title(5,1)" class="CHANGE5">饮品</a></li>
    <li class="meal8"><a href="javascript:void(0);" onclick="change_title(6,1)" class="CHANGE6">酱料</a></li>
    
  <li class="sport"><a href="javascript:void(0);" onclick="change_title(7,1)" class="CHANGE7">套餐</a></li>
</ul>

<div class="can-menu-wrap">
  <div class="green-bar">
	<span id="can_menu_tab" class="float-left can-menu-tab">
	  	</span>
	
  </div>
  
  <div id="can_md_food">
      <div class="can-menu">
	  SOLO
  </div>
   </div>

  <div class="page center">
   

   PAGE
   
   </div>
    
  </div>
<script type='text/javascript'>
  $(function(){
      itemHoverFix("can_md_food");
      intrHoverFix("can_md_food");
	  addHoverFix("can_md_food");
  });
</script>

<script>
  function upload_food_unit(food_id, et){
    tarObj = $('.pop-oper:visible:first').parents('.item-list');
    tarObj.css({
        position:"static",
        "z-index":0
    });
    $(tarObj).find('.pop-oper:visible:first').hide();

    var tarObj = $("#item_"+ food_id + "_" + et);
    tarObj.css({
      position:"relative",
      "z-index":2
    });
    $("#upload_food_unit"+food_id+"_"+et).show();
    return false;
  }
  function close_upload_food_unit(food_id, et){
    var tarObj = $("#item_"+food_id+"_"+et);
    tarObj.css({
        position:"static",
        "z-index":0
    });
    $("#upload_food_unit"+food_id+"_"+et).hide();
  }
</script>

  </div>
</div>
'''
# temp = Empty.replace("SOLO",Solo+Solo+Solo+Solo+Solo)
# def getTemp(change,page):
#     return temp
Page_Current = '<em class="current"><b>PAGENUM</b></em> '
Page = '<a href="#" onclick="change_title(CHANGE,PAGENUM)">PAGENUM</a> '
import copy
def getTemp(change,page):
    temp = copy.deepcopy(Empty)
    all_solo = ""
    change_data = Maping[change]
    key_list = list(change_data.keys())
    page_sum = int(len(key_list)/10)
    if len(key_list)%10>0:
        page_sum += 1
    page_message = '<a class="previous_page disabled" onclick="change_title(%s,%s)" href="#">« 上一页</a>'%(str(change),str(page-1 if page>1 else page))
    for value in range(1,page_sum+1):
        if value == page:
            page_message += Page_Current.replace("PAGENUM",str(value))
        else:
            page_message += Page.replace("PAGENUM",str(value)).replace("CHANGE",str(change))
    page_message += '<a class="previous_page disabled" onclick="change_title(%s,%s)" href="#">下一页 &raquo;</a>'%(str(change),str(page+1 if page<=page_sum else page))
    max_len = len(key_list)
    start_len = (page-1)*10
    end_len = 0
    if max_len > start_len+10:
        end_len = start_len + 10
    else:
        end_len = max_len
    for index in range(start_len,end_len):
        solo = copy.deepcopy(Solo)
        solo = solo.replace("NAME", change_data[key_list[index]]["NAME"])
        solo = solo.replace("KLL", str(change_data[key_list[index]]["KLL"]))
        solo = solo.replace("Company", change_data[key_list[index]]["Company"])
        solo = solo.replace("Single", str(change_data[key_list[index]]["Single"]))
        solo = solo.replace("ID", str(key_list[index]))
        all_solo += solo
    temp = temp.replace("SOLO", all_solo).replace("CHANGE"+str(change),"current").replace("PAGE",page_message)
    return temp
