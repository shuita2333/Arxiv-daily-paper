# 📦 其他研究 | 2026年07月10日

> 本类共 **207** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-207**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-207**

---

### 201. [Neural Operator-enabled Topology-informed Evolutionary Strategy for PDE-Constrained Optimization](https://arxiv.org/abs/2607.07682)

**<font color=#1a73e8>作者：</font>** Xiangming Huang, Guannan Zhang, Lu Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inverse design of physical systems governed by partial differential equations is computationally demanding due to the high dimensionality and non-convexity of design spaces. Generative models for inverse design often lack robustness and transferability, whereas evolutionary strategies are robust but struggle in high-dimensional spaces. This paper introduces a Neural Operator-enabled Topology-informed Evolutionary Strategy (NOTES) that integrates dimensionality reduction, representation learning, and evolutionary optimization for efficient and transferable inverse design. NOTES couples a DeepONet-based neural operator with the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) to perform global optimization in a compact latent space that encodes topology-aware priors while discovering high-performance designs for unseen operating conditions. Applied to nanophotonic beam-deflector inverse design governed by Maxwell's equations, NOTES reduces the design dimensionality from 256 to 25 and consistently achieves over 95 percent efficiency, outperforming CMA-ES, topology optimization, and other baselines. Applied to structural optimization, NOTES discovers designs that achieve compliance down to 246. By decoupling topology learning of a DeepONet from the governing physics in a PDE solver, NOTES provides a flexible and transferable framework for the inverse design of physical systems.

---


### 202. [ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening](https://arxiv.org/abs/2607.07683)

**<font color=#1a73e8>作者：</font>** Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as they require high computational resources or strong high-speed internet connectivity. This causes several cases where conditions like acute coronary occlusion (ACS) is overlooked and reperfusion therapy delayed. Although prior work has tackled digitization and diagnosis separately, and utilized advanced AI models for them, there still remains a lack of a compute-light, on-device framework that reconstructs paper ECGs at high fidelity, while accurately supporting multiple clinically relevant endpoints. We address this need with an end-to-end lightweight on-device digitization-to-diagnosis pipeline that converts a smartphone photo or scan of a paper ECG into a calibrated 12-lead signal and screens for Myocardial Infarction (MI) pathologies, with SHapley Additive exPlanations (SHAP) to support interpretability. Trained and evaluated on 21,799 ECGs from the PTB-XL dataset and further validated on hospital-acquired ECG-Matrix dataset, the complete system runs in <30 s per ECG on CPU-only resources, achieving 95.51% accuracy (F1 = 0.9519) for MI detection on PTB-XL and 88.89% accuracy (F1 = 0.8862) for OMI detection on ECG-Matrix. This work showcases that legacy paper records can be reliably democratized in any part of the world, providing a scalable decision support when digital ECG export, connectivity, or high-end compute are unavailable

---


### 203. [Agent Delivery Engineering Predictive Reliability Framework](https://arxiv.org/abs/2607.07689)

**<font color=#1a73e8>作者：</font>** Dexing Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM multi-agent systems face reliability risks invisible to infrastructure monitoring. We propose the ADE Predictive Reliability Framework (ADE-PRF), enabling proactive health trajectory prediction from passive degradation detection. ADE-PRF aggregates 20 heterogeneous signals across five layers into a Trust Margin (TM) metric (39.2-point dynamic range). Triple-method parallel prediction enables 8-hour forecasts: the Exponential method achieves MAE=1.228, Direction Accuracy=76.8%, with 99.65% within +/-10-point tolerance. Production validation spans 380,227 predictions and 280,579 validations across six agent profiles over 15 continuous days, plus seven sandbox-controlled experiments. Key findings include detection of "false prosperity" -- degradation concealed by normal surface metrics -- and immediate TM coupling with ground-truth states upon ADE plugin integration, with 16/20 factors relying on ADE-collected data. Exponential consistently outperforms Kalman. ADE-PRF provides among the earliest reliability quantification with forward-looking warnings for production LLM agents.

---


### 204. [Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning](https://arxiv.org/abs/2607.07690)

**<font color=#1a73e8>作者：</font>** Vladislav Beliaev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is rewarded for out-solving the other. To win, a model must out-reason a rival that has seen its work, so reasoning is judged implicitly during training, with no process labels and no reward model. Because both models are optimized, each faces a progressively stronger rival, which single-model RL cannot provide. The two need only be comparably strong and behaviorally different. At inference the pair deploys as it trains, a two-stage cascade in which one model drafts and the other answers after reading the draft. On the hard split of DeepMath with Qwen3, this doubles GRPO's pass@1, roughly eight times the gain of an untrained Mixture-of-Agents pass over the same base. The ordering replicates on competitive-programming code and across model families (Qwen3.5, Gemma 4). For now the models talk in text; the next step is to let them reason together in latent space.

---


### 205. [Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety](https://arxiv.org/abs/2607.07695)

**<font color=#1a73e8>作者：</font>** Yujiao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces. Three findings emerge. (1) Deployment rules causally alter collective safety: changing only the consequence rule moves mean fatality by 22 to 58 percentage points within every population. (2) There is no safe default, but the targeting hazard is universal: the safest rule, the least-safe rule, and even the direction of the incidence effect vary across populations, yet regressive identity-targeting is never decisively safest in any context for any population, eliminates the least-resourced agent in 30-87% of games everywhere, and is selection-unsafe relative to the cooperative reference for all seven populations. (3) Identity salience is the mechanism: a one-shot anonymization ablation on the most exploitation-prone population (gpt-5.1) shows that merely naming the loss bearer in the rule text drives targeted elimination from 22% to 81% at identical payoffs; under repeated play, anonymization only delays the targeting, as agents re-infer the hidden rule from observed eliminations. We package the methodology as a safety-case workflow that certifies a provisional rule region $\Phi(c,P)$ per deployment context and population, with explicit residual risks and monitoring obligations.

---


### 206. [From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization](https://arxiv.org/abs/2607.07702)

**<font color=#1a73e8>作者：</font>** Ying Chang, Jiahang Xu, Xuan Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, while naive context reduction methods such as truncation or sliding windows can discard causally important evidence and produce misleading optimization signals. To resolve this dilemma, we introduce STRACE (Structural TRajectory Analysis and Causal Extraction), a framework that constructs high signal-noise optimization contexts for more precise and effective optimization. At the batch level, STRACE mines failure patterns to filter redundant traces and retain representative failures; within each selected trace, it performs causal localization over a textual dependency graph to remove non-causal steps and identify the true root-cause module for optimization. Empirical results demonstrate that STRACE significantly outperforms standard context-filtering baselines. Notably, on a challenging formal verification task (VeruSAGE-Bench), it successfully optimizes human-expert designed agents, delivering $1.4\times$ success-rate improvement (42.5% to 58.5%). The code is available at this https URL .

---


### 207. [The Key to Going Linear: Analysis-Driven Transformer Linearization](https://arxiv.org/abs/2607.07706)

**<font color=#1a73e8>作者：</font>** Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of approximation errors and introduce structural interventions, specifically sink tokens, short convolutions, and fixed-budget cache routing, which reduces the remaining gap. We scale this linearization approach across LLaMA and Qwen models up to 32B parameters, outperforming prior post hoc baselines on MMLU and matching the long-context retrieval of complex adaptive-caching frameworks.

---


> [!TIP]
> 当前位于：**201-207**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-207**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
