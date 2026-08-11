---
name: story-engine
description: Use for fiction plot-engine diagnosis and co-creation: stage goals, constraints, costly choices, feedback, persistent state changes, adjacent/cross-volume continuity, dual engines, resource/anti-goal/rule-pressure engines, restart/formula/imbalance risks, engine transition, and terminal closure. Not for prose polishing, full character arcs, encyclopedic worldbuilding, or style imitation.
---

# Story Engine / 剧情发动机

Story Engine 是一个面向长篇小说与连续剧情的结构诊断/共创 Skill。它不把“设定、金手指、任务名”本身当作剧情发动机，而是检查：**什么迫使故事现在启动，主角当前要完成什么，在什么限制下作出有代价选择，行动产生什么反馈，结果留下什么永久状态变化，以及这些变化怎样牵引下一阶段。**

## 核心方法

一个有效阶段通常需要：

1. 启动条件；
2. 当前可结算目标；
3. 不行动代价；
4. 限制；
5. 至少两个有真实取舍的行动选项；
6. 行动与反馈；
7. 收益与代价；
8. 永久状态残留；
9. 下一阶段牵引（终局除外）。

Story Engine 同时支持诊断和共创。诊断时查结构缺口并执行删除/反事实测试；共创时保留用户已确定内容，只在缺口处提出带来源标记的候选方案。

风险规则只提示输入材料中的结构风险，不用于判定整部作品的质量。

## 规则集

正向规则：

- `SE-RC-001` 通用剧情发动机循环
- `SE-RC-002` 资源稀缺发动机
- `SE-RC-003` 反目标发动机
- `SE-RC-004` 现实目标与隐藏任务双引擎
- `SE-RC-005` 规则压力发动机

风险规则：

- `SE-F-001` 循环重启风险
- `SE-F-002` 发动机公式化风险
- `SE-F-003` 多发动机失衡风险

## 触发场景

适合：

- “这个阶段能不能持续推进？”
- “是不是缺目标、代价、阻碍或反馈？”
- “上一卷到下一卷是不是断了？”
- “现实线和隐藏线有没有互相供能？”
- “连续三段是不是太重复？”
- “资源、规则、身份、关系哪条线没有实际功能？”
- “终局还需不需要继续开新目标？”

不适合把本 Skill 作为主工具处理：纯正文润色、完整人物弧光、百科式世界观搭建、章节级文风模仿、纯资料查询。

## 执行流程

1. **识别请求模式**：快速诊断、灵感补全、阶段方案共创、连续阶段复核、跨卷承接检查或风险专项检查。
2. **保护来源边界**：区分 `[已确定]`、`[不可修改]`、`[建议]`、`[推导]`、`[假设]`、`[无法验证]`。新增人物、组织、能力、规则、事件或结局必须标记来源。
3. **判断输入是否足够**：不足时先诊断已有材料，不为了形式完整而连续追问大量问题。
4. **先用 `SE-RC-001` 检查基础循环**：启动、目标、不行动代价、限制、选择、行动、反馈、收益与代价、永久残留、下一阶段牵引。
5. **按结构选择专项正向规则**：资源稀缺用 `SE-RC-002`；反目标用 `SE-RC-003`；现实/隐藏并行用 `SE-RC-004`；规则压力用 `SE-RC-005`。
6. **按材料范围选择风险规则**：相邻阶段/跨卷/换地图职业能力时用 `SE-F-001`；至少三轮循环比较时用 `SE-F-002`；多发动机并行时用 `SE-F-003`。
7. **执行删除与反事实测试**：按任务需要删除上一阶段、现实端、隐藏端、某发动机、任务发布者或长期线索，并测试部分成功、旧办法失效、资源反噬、能力变化承接、发动机转型和终局收束。
8. **裁剪输出**：只输出本次任务需要的字段，并在结束前复查所有新增剧情内容是否有来源标记。

## 硬边界

- `SE-F-001`、`SE-F-002`、`SE-F-003` 都不是硬性失败判定。
- 固定题材循环不自动等于公式化。
- 换地图、职业、任务或能力不自动等于循环重启。
- 阶段性主次变化不自动等于失衡。
- 发动机转型不等于失败。
- 终局收束不要求继续制造下一轮目标。
- 规则复杂化不自动等于多发动机失衡。

八类状态残留：身份、权限、资源、责任、关系、认知、公开标签、媒介或场景状态。每阶段不要求全部具备。

## 按需读取

- `references/rule-cards.md`：八张规则卡与边界。
- `references/input-schema.md`：输入字段、模式路由和状态残留。
- `references/output-templates.md`：诊断和共创输出模板。
- `references/diagnostic-tests.md`：删除测试和反事实测试。
- `references/evidence-boundaries.md`：公开验证口径、风险规则边界。
- `references/integration-contract.md`：通用结构化集成接口。
- `schemas/story-engine-output.schema.json`：可选的结构化输出 JSON Schema。
- `tests/test-prompts.json`：模型行为评估输入、预期规则和禁止行为。
- `tests/run_tests.py`：确定性仓库验证。

## 版本

Public release: `0.1.0`.
