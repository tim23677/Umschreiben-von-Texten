# Technical and Research Writing

House style for technical and research documents in Chinese and English: experiment
reports, result tables, design documents, papers, commit messages, and summaries of
findings.

**Precedence.** For these documents this guide overrides the PERSONALITY AND SOUL section
of `SKILL.md`. That section asks for opinions, varied rhythm, and informal asides. Those
requirements do not apply to technical documents. The 33 AI-writing patterns in `SKILL.md`
still apply.

Two principles underlie the eight rules:

- Concepts that already have a standard expression do not get a new one.
- If an expression requires the reader to infer what it refers to, state the referent
  directly.

概念已有通用说法的，不另造表述。如果一个说法需要读者推断其指代对象，改为直接说明。

---

## Rule 1 — Use standard terminology / 使用标准术语

| 原表述 | 修改后 |
|---|---|
| 超长度 / 超不超长度 | 截断 / 是否触及长度上限 |
| Ray 的端口会跟自己撞 | 多个任务的 Ray 抢占同一端口 |
| 臂 | 方案 |
| 只看长度那条线 | 长度启发式基线 |
| 刷奖励 | 奖励被优化但评测指标未改善 |
| 存档 | checkpoint |

| Original | Revised |
|---|---|
| the port thing collides with itself | multiple Ray tasks bind the same port |
| arm | configuration |
| the length-only line | length heuristic baseline |
| reward farming | reward increased while the evaluation metric did not improve |
| save file | checkpoint |
| ran out of room | reached the context length limit |

## Rule 2 — Do not invent metaphors as terminology / 不发明比喻作为术语

| 原表述 | 修改后 |
|---|---|
| 血统 | 基座来源 |
| 8 个不同血统 | 8 个不同基座的模型 |
| 那是尺寸差异，不是血统差异 | 原有区间由 Qwen 的 14B、32B、72B 构成，差异来自参数量而非基座 |
| 已经吃掉一半空间 | 已覆盖一半区间 |
| 变成了一个认题目的检索器 | 退化为问题识别，与学习价值无关 |
| 挑出来的题目看上去健康得多 | 选中问题的截断比例更低 |
| 误差范围还盖着基准线 | 置信区间与基线重叠 |

| Original | Revised |
|---|---|
| bloodline / lineage | base model |
| 8 different bloodlines | 8 models with different base models |
| eats half the space | covers half the range |
| becomes a question-recognizer | degenerates into problem identification |
| the selected problems look much healthier | the selected problems have a lower truncation rate |
| the error bars still cover the baseline | the confidence interval overlaps the baseline |

## Rule 3 — Neutral nouns for headers and category names / 表头和分类名使用中性名词

Use 问题 / 现象 / 影响 / 结果 / 设置, or Issue / Observation / Effect / Result / Setup.

| 原表述 | 修改后 |
|---|---|
| 坑 / 代价和教训 | 问题 / 影响 |
| 把握 | 确认程度 |
| 怎么做的 | 实验设置 |
| 重挑一次还剩多少重合 | 重采样后的重合率 |
| 有几种不同取值 | 取值数量 |
| 还在跑的 | 进行中 |
| 一个必须关掉的开关 | 需要关闭的过滤器 |

| Original | Revised |
|---|---|
| Gotchas / Lessons learned the hard way | Issues / Effects |
| How confident we are | Confidence level |
| What we did | Experimental setup |
| Still cooking | In progress |
| A switch you have to turn off | Filter to disable |

**Status labels stay consistent.** Choose one set and use it throughout. If earlier
sections use 已完成 / 已确认 / 未达到基线 / 结论待定, later sections must not switch to
做通了 / 意外发现 / 需要修. In English, if earlier sections use Complete / Confirmed /
Below baseline / Undetermined, later sections must not switch to Got it working / Surprise
finding / Needs a fix.

## Rule 4 — Do not use the "X, not Y" construction / 不使用"是 X，不是 Y"的对比句式

| 原表述 | 修改后 |
|---|---|
| 梯度对齐：是噪声，不是信号 | 梯度对齐：三项检查结果均在噪声范围内 |
| 我们买到了血统上的多样性，但没有买到能力上的多样性 | 新增模型覆盖了更多基座，但正确率均低于原有区间下界 |
| 考法和用法对不上 | 评测口径为成对比较，与实际使用方式不一致 |
| 稳定是靠粗糙换来的 | 取值数量少的指标重合率高 |
| 越稳定的指标越挑不出东西，越挑得出东西的指标越不稳定 | 重合率与取值数量呈反向关系 |

| Original | Revised |
|---|---|
| Gradient alignment: noise, not signal | Gradient alignment: all three checks fall within the noise range |
| It is a labelling problem, not a reasoning problem | The failure occurs in the recorded state rather than in the generated text |
| We gained coverage but not capability | The added models cover more base models; all fall below the lower bound of the existing accuracy range |

## Rule 5 — Entries need not contain a number or a conclusion / 条目可以不含数字或结论

An entry may state only what occurred. It is complete as written.

> 对照组为随机选取的 32 个问题。

> The control group consists of 32 randomly selected problems.

Do not append a comparison or implication that was not measured.

## Rule 6 — Write "原因未查明" when the cause is unknown / 未查明原因时直接写明

Use 原因未查明 / Cause not determined. Once stated, later sections must not supply
unverified explanations for the same observation.

| 原表述 | 修改后 |
|---|---|
| 这可能也解释了前文那个现象 | 该现象与截断的关系尚未验证 |

| Original | Revised |
|---|---|
| This probably also explains the earlier observation | The relationship between that observation and truncation has not been verified |

A later section that establishes the mechanism through measurement may state it. Confirmed
findings are not subject to this rule.

## Rule 7 — No colloquialisms / 不使用口语词

| 原表述 | 修改后 |
|---|---|
| 赢得很干脆 | 差值为 0.030 |
| 测得更准 / 测得更糙 | 估计精度更高 / 更低 |
| 可选的余地很小 | 候选范围小 |
| 基本上等于抓阄 | 接近随机选取 |
| 本来就分不出高下 | 真实差距低于可分辨范围 |
| 白跑 / 白占 | 无效运行 / 空占 |
| 不是白捡的 | 需要 79 GPU·小时 |
| 一个致命问题 | 主要问题 |
| 有事后找补的嫌疑 | 该切分方式在观察结果之后确定 |
| 原因不复杂 | 删除 |
| 既然预测这条路走不通，那就退一步 | 删除，直接进入实验设置 |

| Original | Revised |
|---|---|
| wins handily | difference of 0.030 |
| not much to choose from | small candidate range |
| basically a coin flip | approximately random selection |
| free / comes for free | requires 79 GPU-hours |
| a killer problem | the main problem |
| smells like post-hoc justification | the split was chosen after the results were observed |
| the reason is simple | delete |

Transitional sentences carrying no information are deleted rather than rewritten.

## Rule 8 — No anthropomorphism / 不使用拟人表述

Attribute behaviour to the procedure or the quantity.

| 原表述 | 修改后 |
|---|---|
| 天生需要几百到上千次采样 | 该信号所需的采样量为几百到上千次 |
| 一旦超就制造出参差 | 截断发生时会增大奖励方差 |
| 24 步训练只挪动 0.05 | 24 步训练后正确率变化为 0.05 |
| 超得越彻底反而越稳定 | 截断率越高，奖励方差越低 |
| 回答内容本身的好坏参差 | 答案质量的差异 |

| Original | Revised |
|---|---|
| the signal naturally needs hundreds of samples | the signal requires hundreds to thousands of samples |
| once it goes over it creates spread | truncation increases reward variance |
| 24 steps only moves it 0.05 | accuracy changes by 0.05 after 24 training steps |
| the model wants to exploit the reward | reward increases without a corresponding change in the evaluation metric |

---

## Revision checklist

1. Coined terms replaced with standard terms.
2. Figurative expressions replaced with the quantity or mechanism referred to.
3. Headers and category names are neutral nouns; status labels consistent throughout.
4. No "X, not Y" constructions.
5. Entries stating only what occurred left as they are.
6. Unknown causes written as 原因未查明 / Cause not determined, with no unverified
   explanation elsewhere.
7. No colloquialisms; information-free transitions deleted.
8. No anthropomorphic subjects.
