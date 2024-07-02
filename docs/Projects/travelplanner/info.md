 
# TravelPlanner

需要的数据： 
1. 

## 考虑改进 

observation消耗的token太多了，后面性能会下降

而且，给了很多没有用的字段，纯粹消耗性能

## notebook write的改进

没有格式化内容，直接放进去？
看一下事实，如果是的话能改进

## 2-stage和sole-planning

终于明白了为什么取名叫2-stage了，论文没好好看呀。

travel planner原本就是两个stage，
一个stage是收集所需信息，
另一个是根据信息和query规划行程。

那么这个收集信息的步骤可以加速。

## 凌晨疑问
Q
```python
react_planner_agent_prompt = PromptTemplate(
                        input_variables=["text","query", "scratchpad"],
                        template = REACT_PLANNER_INSTRUCTION,
                        )

reflect_prompt = PromptTemplate(
                        input_variables=["text", "query", "scratchpad"],
                        template = REFLECT_INSTRUCTION,
                        )

react_reflect_planner_agent_prompt = PromptTemplate(
                        input_variables=["text", "query", "reflections", "scratchpad"],
                        template = REACT_REFLECT_PLANNER_INSTRUCTION,
                        )
```
这三个prompttemplate的构造和概念明天看一下，看不懂。


**发现funciton calling GET请求可以用rag来取代**

Q**X agent的X指的是任何场景吗？
去学agent架构（wll's paper, langchain agent docs， github X agent）**









<br><br><br><br><br><br>
end