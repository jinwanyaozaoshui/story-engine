# Generic Integration Contract / 通用集成接口

Story Engine 可以独立使用，也可以被上层 Agent、编辑器或工作流调用。本接口只描述通用数据，不绑定任何私人项目或特定总控系统。

## 建议输入

- `request_mode`: 快速诊断、灵感补全、阶段方案共创、连续阶段复核、跨卷承接检查、风险专项检查。
- `confirmed_content`: 用户明确确认的内容。
- `immutable_items`: 用户要求不可修改的内容。
- `current_stage_goal`: 当前可结算阶段目标（若已知）。
- `context`: 与本次结构判断相关的阶段、关系、资源、规则和长期线索。

## 建议输出

- `rules`: 本次使用的规则 ID。
- `conclusion`: 成立、基本成立但有缺口、只能预警或无法验证。
- `stage_plan`: 启动、目标、不行动代价、限制、选择、行动反馈、收益与代价。
- `permanent_residue`: 八类状态残留。
- `next_stage_pull`: 下一阶段如何由本阶段结果启动。
- `risks`: 循环重启、公式化、多发动机失衡等风险诊断。
- `unverifiable_items`: 输入不足项。
- `suggestions`: 带 `[建议]` / `[假设]` / `[推导]` 标记的候选修补。

## 约束

- 上层系统不得把风险规则改写为硬性作品质量判定。
- 不得把长期线索直接替代当前阶段目标。
- 不得把未知设定写成 `confirmed_content`。
- 结构化输出可以按 `schemas/story-engine-output.schema.json` 进行校验。
