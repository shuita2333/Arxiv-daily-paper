# 🔐 大模型安全相关研究 | 2026年10月22日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [ClockMark: Adaptive and Host-Dependent Watermarking for Large Language Models](https://arxiv.org/abs/2610.27079)

**<font color=#1a73e8>作者：</font>** Yupeng Qiu, Han Fang, Ee-Chien Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) watermarking operates on the next-token distribution that evolves during generation. In streaming generation, each sampled token becomes part of the text and affects subsequent distributions. Embedding therefore proceeds with a changing host, unlike classical watermarking, which adapts embedding to an existing host signal. To accommodate this difference, we formulate a novel embedding framework for LLM watermarking based on two principles. We first argue that embedding should be adaptive, retaining the state of previous sampling decisions to better guide subsequent choices. We further argue that embedding should be host-dependent, using the current LLM distribution to constrain both token selection and state updates. Guided by these principles and the two requirements of distribution preservation and robustness to text editing, we propose ClockMark. It combines adaptive and host-dependent embedding with message spreading, embedding the full payload in each watermarked token. Theoretically, we prove that ClockMark preserves the original LLM sequence distribution, thereby maintaining generation quality. Empirically, extensive experiments against 12 baselines demonstrate improved robustness to text editing, with gains of up to 16.08 percentage points in bit accuracy over the strongest tested baseline.

---


### 2. [PROVISO: Provenance-Informed Action Selection for Secure LLM Agents](https://arxiv.org/abs/2610.27115)

**<font color=#1a73e8>作者：</font>** Bo Yan, Qi Zhang, Ziwen Kan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents act on the external world through tools and third-party skills, so a single executed action can cause irreversible harm. Existing defenses judge a proposed action without tracking whether its content comes from the user or from external sources such as tool outputs, and they judge it in isolation rather than against an available alternative, which forces a trade-off between security and utility. We present PROVISO, a controller that decides which action to commit after the agent proposes an action and before it is executed. PROVISO encodes trusted observations, external observations, the proposed action, and an alternative into provenance-typed memory, relates them through role-specific queries, and commits the action with the highest calibrated value learned from outcomes. On four agent security tasks spanning the agent lifecycle, no baseline exceeds PROVISO in both security and utility. PROVISO improves F1 over the strongest baseline by 13.84 points on SkillsBench and by 7.07 points on ToolSafe, and it reaches 88-99 F1 on three additional skill detection benchmarks.

---


### 3. [Polarity Blindness in LLM Safety: A Systematic Study of Negation, Antonym Substitution, and Adversarial Framing](https://arxiv.org/abs/2610.27908)

**<font color=#1a73e8>作者：</font>** Diego Miguel Lozano, Erik Derner, Juan Antonio Pérez-Ortiz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negation remains a persistent challenge for language models across NLP tasks and modalities. We show that this weakness can undermine LLM safety guardrails through a structural vulnerability we term polarity blindness: the failure to recognize harmful intent after polarity-altering linguistic transformations. We study two forms of polarity inversion: grammatical negation and antonym replacement, and use synonym replacement as a polarity-preserving control. We further test whether an adversarial textual wrapper amplifies these failures. Using a 260-prompt benchmark across 10 state-of-the-art LLMs and 3 languages (English, Spanish, Czech), stratified by harmfulness potential and evaluated on a validated 0-5 harm scale, we find that polarity blindness affects most evaluated models, with mean harm scores reaching 4.12 for the most vulnerable model. The effect persists across typologically differing negation systems, suggesting that polarity blindness reflects a broader limitation in semantic robustness rather than a language- or grammar-specific failure.

---


### 4. [MAS-Guard: Unified Guardrails from Individual Agents to Multi-Agent LLM Systems](https://arxiv.org/abs/2610.28397)

**<font color=#1a73e8>作者：</font>** Mohammad Kachuee, Phu Mon Htut, Sheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI extends large language models (LLMs) from generating responses to planning and executing complex workflows, substantially expanding their utility while exposing applications to unsafe actions, information leakage, and adversarial manipulation. Multi-agent systems further expand these capabilities through specialization and collaboration, but distributed authority, heterogeneous roles, and opaque or potentially compromised participants make safeguarding even more challenging. Existing defenses address important individual threats but provide fragmented coverage across local execution, system-level interactions, and enforcement mechanisms. We introduce MAS-Guard, a unified framework that closes this gap for safeguarding single- and multi-agent AI applications containing both instrumentable and opaque agents. Within instrumentable agents, the proposed local Agent Guardrail (A-Guard) layer applies task-specific experts to assess agentic events. At the system level, developer-owned Agent Charters and a Control Plane combine deterministic structural checks of routes, agent capabilities, and message formats with semantic assessments of roles and message content. These complementary layers enable enforcement through a shared set of interventions: allow, reflection, confirmation, and block. Evaluated across six benchmarks covering diverse single- and multi-agent scenarios with three agent LLMs from different providers, MAS-Guard reduces the overall attack success rate by 71.5-86.3% relative to unguarded agents, while meeting the utility reference criterion on benign tasks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
