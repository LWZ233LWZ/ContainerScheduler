# ContainerScheduler
A container scheduler.


目标：高效的集群资源利用率，快速的调度决策，健壮的鲁棒性

高效的集群资源利用率：每种资源根据以往的资源使用情况调整超卖比

快速的调度决策：快速决定被调度任务去往哪个计算节点

健壮的鲁棒性：调度程序本身的可用性

调度系统流程包括如下几个过程：
1)所有计算节点给调度器上报可用资源情况（cpu，mem，disk）
2)应用申请资源
3)调度器根据调度算法，选择合适的节点
4)应用运行到调度的节点上

实现语言：Python
本来是准备采用Golang，但是Golang目前使用不熟练

