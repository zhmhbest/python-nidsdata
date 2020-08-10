# [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

## 入侵检测

入侵检测软件可保护计算机网络免受未经授权的用户（包括内部人员）的攻击。检测器的目的是建立一个能够区分**不良连接**（即入侵或攻击）和**良好正常连接**的预测模型（分类器）。

每个连接都是一系列TCP数据包的传输，并明确定义了开始时间和结束时间，在这之间，数据按照某种协议在源IP地址和目标IP地址之间流动。每个连接都被标记为正常行为（normal）或攻击行为（attack），并指明攻击类型。每个连接大约包含100个字节。

攻击分为四个主要类别

- DOS: 拒绝服务，例如 <u>syn flood</u>
- R2L: 来自远程计算机的未经授权的访问，例如 <u>guessing password</u>
- U2R: 未经授权访问本地root，例如 <u>buffer overflow</u>
- Probing: 监视和其他探测，例如 <u>port scanning</u>

特别需要注意的是，测试数据与训练数据并不具有相同的概率分布，并且测试数据还包括不在训练数据中的特定攻击类型。这使任务更加现实。**事实上，大多数新颖的攻击都是已知攻击的变种，并且对已知攻击的“Signature”足以捕获新颖的变种**。训练数据集总共包含[24种攻击类型](training_attack_types.txt)，测试数据还有额外14种类型。

## 衍生功能

Stolfo等，定义了高级功能，可帮助区分正常连接和攻击。

### 基于时间和流量特征的连接记录

- **相同主机**：功能仅检查过去两秒钟内具有与当前连接相同的目标主机的连接，并计算与协议行为，服务等有关的统计信息。
- **相同服务**：功能仅检查过去两秒钟内与当前连接具有相同服务的连接。

**相同主机**和**相同服务**功能一起称为**基于时间和流量特征的连接记录**。

### 基于主机的流量特性

一些Probing使用比两秒大得多的时间间隔（例如，每分钟一次）扫描主机（或端口）。因此，连接记录也按目标主机进行排序，并且使用到同一主机的100个连接的窗口而不是时间窗口来构造功能。、

### 其它

与大多数DOS和Probing不同，R2L和U2R攻击的记录中似乎没有频繁出现的顺序模式。这是因为DOS和Probing在很短的时间内涉及到某些主机的许多连接，但是R2L和U2R攻击被嵌入到数据包的数据部分中，并且通常仅涉及单个连接。

## 数据说明

| feature | description | type |
| -: | :- | :-: |
| duration      | 连接的长度（秒数） | 连续 |
| protocol_type | 协议的类型，例如：tcp，udp | 离散 |
| service       | 目的地上的网络服务，例如：http，telnet | 离散 |
| src_bytes     | 从源到目标的数据字节数 | 连续 |
| dst_bytes     | 从目标到源的数据字节数 | 连续 |
| flag          | 连接的正常或错误状态 | 离散 |
| land          | 1 (连接from/to同一个host/port) else 0 | 离散 |
| wrong_fragment| 错误片段的数量 | 连续 |
| urgent        | 紧急包数 | 连续 |

| feature | description | type |
| -: | :- | :-: |
| hot               | 热指标数量 | 连续 |
| num_failed_logins | 登录失败次数  | 连续 |
| logged_in         | 1 (成功登录) else 0 | 离散 |
| num_compromised   | 妥协情况的数量 | 连续 |
| root_shell        | 1 (root shell) else 0 | 离散 |
| su_attempted      | 1 (尝试`su root`指令) else 0 | 离散 |
| num_root          | 访问`/`的次数 | 连续 |
| num_file_creations| 操作创建文件的次数 | 连续 |
| num_shells        | shell prompts数量 | 连续 |
| num_access_files  | 操作访问控制文件的次数  | 连续 |
| num_outbound_cmds | ftp会话中的出站命令数  | 连续 |
| is_hot_login      | 1 (登录名属于hot list) else 0 | 离散 |
| is_guest_login    | 1 (登录名属于宾客) else 0 | 离散 |

| feature | description | type |
| -: | :- | :-: |
| count         | 过去两秒内与当前连接到同一主机的连接数  | 连续 |
|| 注意：以下功能引用这些相同主机的连接 ||
| serror_rate   | 出现``SYN''错误的连接百分比 | 连续 |
| rerror_rate   | 出现``REJ''错误的连接百分比 | 连续 |
| same_srv_rate | 相同服务的连接百分比 | 连续 |
| diff_srv_rate | 与不同服务的连接百分比 | 连续 |
| &nbsp; |||
| srv_count     | 过去两秒内与当前连接相同服务的连接数  | 连续 |
|| 注意：以下功能引用这些相同服务的连接。 ||
| srv_serror_rate       | 出现``SYN''错误的连接百分比 | 连续 |
| srv_rerror_rate       | 出现``REJ''错误的连接百分比 | 连续 |
| srv_diff_host_rate    | 与不同主机的连接百分比 | 连续 |
