# 🧠 大模型相关研究 | 2026年10月27日

> 本类共 **204** 篇论文：已确认 **185** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

---

### 201. [Natural Language Autoencoders Identify Without Explaining](https://arxiv.org/abs/2610.32691)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kristina Šekrst, Barbara Geld  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Autoencoders (NLAs) express a model's internal activations in the form of readable text. The verbalizer turns an activation into an English explanation; the reconstructor then converts that explanation back into an activation, and the explanation is considered successful if the round trip brings back the original activation. We claim that this criterion evaluates whether the information is sufficient and does not address descriptive faithfulness. A sentence can contain sufficient information to make it possible to identify an activation even if it wrongly explains what the activation does: in the case of reconstruction, the primary aim is to accurately identify the activations and not to describe them. This issue has the same structure as the chain-of-thought faithfulness problem, in which verbal output that has been trained to go with a process is taken as a report on that process, and it parallels the dissociation between an individual's introspective report and the actual governing process as documented in human psychology. Although proposed as interpretability tools for the purpose of alignment, NLAs reintroduce, through unverified explanations, the epistemic problem that they were intended to resolve.

---


### 202. [Direction-Aware Token Credit Assignment with Reward-Model Gradients](https://arxiv.org/abs/2610.32772)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yikuan Hu, Jifeng Zhu, Minle Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GRPO shares a response-level advantage across tokens, leaving unresolved how strongly each token should contribute to learning. Updates induced by the shared advantage reinforce or suppress the sampled token at each position, but these updates do not always point toward increasing reward at the token level. This motivates a work-based view of credit: just as work depends on the component of force along a displacement, token credit should reflect the local reward change along the policy update direction. We introduce Direction-Aware Token Credit Assignment (DATC), which maps frozen reward-model gradients into policy logit space and allocates weights by evaluating the alignment between the reward direction and GRPO's signed sampled-action update direction, while preserving the sign and mean of the response-level advantage. DATC outperforms GRPO in all four settings across two model families.

---


### 203. [Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond](https://arxiv.org/abs/2610.32802)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zheng Jiang, Yiming Chen, Houde Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation aligns teacher feedback with a student's current behavior, yet acquiring useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. We introduce Frontier-OPD, which addresses this problem through the student's learning frontier: decision situations that remain challenging but admit useful autonomous continuation after brief teacher guidance. To operationalize this frontier, Frontier-OPD organizes on-policy experience into a shared-state trajectory graph, where trajectory-balanced aggregation of teacher-student disagreement identifies distinct intervention candidates while preserving the histories needed for replay. Short teacher bridges are then assessed by comparing agreement over the bridge and the ensuing student continuation with an equally long segment of the original trajectory, providing a behavioral proxy for guidance that the current student can build on. Accepted teacher responses augment ordinary distillation data, and fresh rollouts renew the frontier estimate as the policy changes. Experiments on ALFWorld, WebShop, and ScienceWorld report higher mean autonomous performance than the compared distillation baselines across the evaluated student scales and teacher configurations, with ablations indicating complementary effects of candidate selection and guidance filtering. In one ALFWorld timing setting, the additional collection cost is offset by a shorter time to a target success rate.

---


### 204. [A Foundation Model for Policy In-Context Longitudinal Causal Effect Estimation](https://arxiv.org/abs/2610.32863)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenxin Chen, Kyra Gan, Mingyu Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Longitudinal causal effect estimation is complicated by time-varying confounding and treatment-confounder feedback loops. Existing methods generally require data-specific nuisance-model fitting, and many are tailored to prespecified treatment sequences or prediction horizons, leading to time-consuming computation at deployment. We introduce *Policy In-Context Longitudinal causal Effect estimation with Prior-data Fitted Networks* (**PICLE-PFN**), the first foundation model for longitudinal causal effect estimation that supports *dynamic* treatment policies. PICLE-PFN represents target policies through in-context history-decision demonstrations, providing a unified interface for a broad class of treatment policies. Pretrained over synthetic data sampled from longitudinal structural causal models, PICLE-PFN amortizes causal effect estimation across datasets, policies, and horizons. Given a new observational dataset and target policy, it directly predicts conditional average potential outcomes (CAPOs) in one forward pass without task-specific training or hyperparameter tuning. Across synthetic and semi-synthetic longitudinal benchmarks, PICLE-PFN achieves competitive RMSE and substantially improved uncertainty calibration with a fraction of deployment runtime, compared to state-of-the-art conventional estimators trained and tuned separately for each dataset.

---


> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
