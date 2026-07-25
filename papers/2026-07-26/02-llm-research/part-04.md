# 🧠 大模型相关研究 | 2026年07月26日

> 本类共 **153** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-153**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-153**

---

### 151. [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557)

**<font color=#1a73e8>作者：</font>** Xiao Yu, Baolin Peng, Ruize Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. By decoupling training and inference, OpenForgeRL allows researchers to easily train, study, and improve agents directly in the real harnesses and environments they are deployed with. We validate our framework across diverse, complex harnesses and environments, spanning tool/claw-based agents and multimodal GUI browser- and computer-use agents. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Both outperform open baselines of similar size on nearly all benchmarks, and in the GUI setting match or surpass models several times larger. Beyond benchmarks, we analyze how harness choice (e.g., ZeroClaw, OpenClaw, Codex) and RL shape agent behavior. We find that some harnesses are substantially harder to learn than others, and that RL improves agentic reliability, such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak.

---


### 152. [Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning](https://arxiv.org/abs/2607.21558)

**<font color=#1a73e8>作者：</font>** Baihui Wang, Bernard Koch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building socially calibrated large language models, which can learn from others without simply yielding to them, requires more than reducing sycophancy as a one-dimensional failure mode. Models must distinguish when to incorporate others' perspectives from when to maintain a well-grounded moral judgment. We study the broader resistance-compliance process governing this distinction. Across three studies, we show that models' judgment revision is structured along three dimensions that parallel classic phenomena in human social psychology: the distance between an incoming view and the model's initial position, the source attribution of that view, and the coalition structure supporting it. Models are generally more receptive to nearby positions, more influenced by views presented as their own prior judgments, and differently responsive to group pressure. These findings recast sycophancy as one expression of a broader judgment-updating process shaped by social influence. Our framework provides a principled basis for distinguishing constructive belief revision from sycophantic compliance, thereby supporting better alignment in morally consequential interactions.

---


### 153. [MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education](https://arxiv.org/abs/2607.21570)

**<font color=#1a73e8>作者：</font>** Qian Wu, Xinrong Zhou, Zizhan Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) show promise for medical education, but most existing systems focus on localized interactions such as question answering or single-turn feedback, rather than organizing an entire clinical case into a decision-centered learning trajectory. We introduce \textit{MedGame}, a framework that transforms static clinical cases into structured, executable storytelling games. MedGame uses a dual-engine design: a Medical Narrative Designer synthesizes case-grounded clinical storylines with states and decision nodes, while a Story Director converts them into dependency-aware multimodal orchestration plans rendered by our released interactive platform. We construct MedGame Bench, a 5,000-case benchmark and evaluation protocol for Medical Narrative Generation and Story Direction. Experiments show that task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models. A pilot student study further shows that learners perceive MedGame as more engaging and useful than text-only alternatives.

---


> [!TIP]
> 当前位于：**151-153**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-153**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
