# 🧠 大模型相关研究 | 2026年10月23日

> 本类共 **204** 篇论文：已确认 **192** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

---

### 201. [CineEvolve: An Agentic Self-Evolution Framework for Cinematic Multi-Shot Video Generation](https://arxiv.org/abs/2610.29590)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jingzhe Zhang, Peixuan Zhang, Genying Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematic multi-shot video generation requires both narrative planning and iterative refinement. Existing methods either lack narrative reasoning or rely on feed-forward workflows without policy updates. In this paper, we propose CineEvolve, an agentic self-evolution framework for cinematic multi-shot video generation that unifies a Director and a Critic within a single vision-language policy. Emulating real-world filmmaking that couples iterative direction with critical feedback, we train CineEvolve via alternating reinforcement learning, where the Director surfaces flaws to sharpen the Critic, and the updated Critic guides the Director's targeted revisions. To stabilize co-evolution, we introduce Evolutionary GRPO (E-GRPO), leveraging historical anchoring and revision safeguarding to mitigate advantage inflation. Additionally, we contribute CineTraj, a 40K cinematic trajectory dataset spanning creation, critique, and revision. Extensive experiments demonstrate that CineEvolve outperforms existing approaches. Our code will be available at this https URL.

---


### 202. [Leveraging Time-Series Foundation Models for Financial Crime Detection](https://arxiv.org/abs/2610.29667)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Danae Natalie Savvidi, H. Çağrı Bilgi, Kubilay Atasu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial crime detection requires identifying illicit activity within large transaction networks, where suspicious behaviour is rare and unfolds over time. Existing graph-based methods capture relationships among accounts but typically underuse the temporal behaviour encoded in account transaction histories. We introduce Temporal-Context Edge Enrichment (TCEE), a framework that addresses this gap by summarising each account's transaction history with a frozen time-series foundation model (TSFM), and enriching each transaction's representation with the relevant temporal context from these summaries. These enriched representations can be scored directly for edge classification, or fed into a graph neural network (GNN) as edge features to capture broader structural information. Across six AMLWorld datasets, TCEE improves PR-AUC over the strongest evaluated baseline on five by a relative 10.8% on average, while training 6.0x faster end-to-end. Feeding TCEE's representations into a GNN raises PR-AUC a further 4.8% on the four smaller datasets. On an Ethereum phishing dataset, we show that TSFM-generated account representations fed into a GNN are also effective for node classification, improving PR-AUC by 14.5% over the strongest baseline. As TSFMs continue to advance, our results suggest they can strengthen financial crime detection by capturing temporal signals that complement graph-based approaches.

---


### 203. [Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhiqian Xia, Jielong Tang, Ling-An Zeng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term agent memory is shifting from predefined workflows toward learnable policies for memory construction and retrieval. Existing learning-based methods either optimize construction alone or combine retrieval-side online reinforcement learning (RL) with offline construction supervision, limiting co-adaptation between the two stages. In this paper, we explore end-to-end online RL for a unified memory manager (Uni-Mem) that learns both capabilities under a shared policy. However, joint optimization with existing RL algorithms such as GRPO faces confounded group comparisons and sparse feedback over long memory-management trajectories. To this end, we propose Stage-Decoupled GRPO, which alternates construction and retrieval optimization while controlling variation from the other stage within each rollout group, yielding stage-specific learning signals. We further introduce Event-Wise Credit Assignment (ECA), which localizes feedback to responsible events and propagates event-level advantages to their constituent operations. Experiments on LoCoMo and LongMemEval show that Uni-Mem outperforms the strongest RL-based memory, demonstrating the effectiveness of jointly learning memory construction and retrieval via Stage-Decoupled GRPO and ECA.

---


### 204. [Plausible but Unimplantable: A Trustworthiness Audit of Shape Completion Foundation Models for Cranial Defect Reconstruction](https://arxiv.org/abs/2610.30035)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Marek Wodzinski, Kamil Kwarciak, Daria Hemmerling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A patient who has lost part of the skull vault needs an implant that fits the defect exactly, and such implants are still drawn by hand in CAD by specialists, which makes each case slow and expensive. The task can be considered as a shape completion problem, so pretrained completion models, and now the first shape completion foundation models, look like a way to remove that manual step. We audited three publicly released pretrained shape completion models, two of them foundation models, applied zero-shot to 239 cranial defects, some carved from public skull datasets and some real post-craniectomy cases. Each output was compared with simply returning the patient's own remaining bone, and tested for whether the predicted material could be placed without intersecting the bone that is still there. On the 210 carved defects none of the three improved on doing nothing, and on the 29 real cases only one did so beyond chance. Yet not one output, from any model in any configuration, was implantable: none managed both to stay clear of the bone the patient still has and to place more material than doing nothing, where a task-specific volumetric model, trained for this task and selected on these cases, was implantable on all but one. The output that most convincingly resembles a skull is no more placeable than the rest, and at these point densities implant thickness cannot be read off the emitted points at all, which is a property of the output representation rather than of any one model. On this evidence the shape completion foundation models we could obtain cannot be trusted and, used as released, are not usable in clinical practice. Substantial research towards trustworthy foundation models for shape completion is still needed.

---


> [!TIP]
> 当前位于：**201-204**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-204**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
