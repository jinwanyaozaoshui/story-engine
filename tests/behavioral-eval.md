# Behavioral Evaluation / 模型行为评估

`test-prompts.json` 是模型/Agent 行为评估集，不是确定性单元测试。

## 为什么分开

`tests/run_tests.py` 可以确定性验证仓库结构、规则 ID、JSON 字段、引用路径和公开信息扫描，但无法证明一个语言模型会按照预期执行剧情诊断。

## 建议评估流程

1. 选择要评估的模型或 Agent 运行环境。
2. 加载 `SKILL.md` 与所需 reference 文件。
3. 逐条运行 `test-prompts.json` 中的 `prompt`。
4. 记录模型名称/版本、运行日期、系统提示或 Skill 装载方式、原始输出。
5. 对照 `expected_trigger`、`expected_rules`、`expected_behavior`、`forbidden_behavior` 和 `pass_criteria` 进行人工或可复现 harness 评分。
6. 只有在能够提供运行方式或原始记录时，才发布“通过率”结论。

## 不应混淆

- **Repository validation passed**：说明公开仓库结构和测试定义一致。
- **Behavioral evaluation passed**：说明某个具体模型/Agent 在某个具体运行环境下满足了行为标准。

二者不是同一件事。
