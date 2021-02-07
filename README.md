# RandomArrangement
 Auto generate a arrangement list that you customized.

## Usage
- main.py：随机抽取2020_1_23_list.json中的人员
  - number_limit：设定一次抽取几个人
  - reset：重置「已经抽取过的」列表
- arrange.py：按照arrangement_event_list.json和2020_1_23_list.json来随机安排人员
  - arrangement_event_list.json：用于表达岗位的安排，支持子项目
  - 2020_1_23_list.json：记录所有人员信息
  - 输出：arrangement.json 是unicode编码的
  - 仍然可以指定number_limit，但是注意和arrangement.json符合
