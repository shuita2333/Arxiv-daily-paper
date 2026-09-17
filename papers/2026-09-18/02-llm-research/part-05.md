# 🧠 大模型相关研究 | 2026年09月18日

> 本类共 **210** 篇论文：已确认 **198** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-210**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-210**

---

### 201. [FoundAna: A GNN-assisted Foundation Model for Graph Anomaly Detection](https://arxiv.org/abs/2609.18107)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Suprim Nakarmi, Chahana Dahal, Yue Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection aims to identify graph structures (e.g., nodes, edges, or subgraphs) that deviate significantly from expected patterns, which supports critical applications in fraud detection, spam identification, network intrusion, etc. Despite the growing methods in the field, existing approaches follow a one-model-per-dataset paradigm, limiting their transferability across diverse real-world scenarios due to task heterogeneity, label scarcity, and domain variability. In this work, we introduce FoundAna, a GNN-assisted Foundation Model for Graph Anomaly Detection - the first foundation model framework designated for generalizable, cross-graph anomaly detection by combining GNNs and transformers. FoundAna integrates an anomaly detection-specific GNN component with a standard transformer encoder augmented by four complementary positional encodings, which enable the model to capture both local and global structural information. Specifically, the positional encoding enriched node representations are passed through attribute and adjacency decoders, and the reconstruction errors serve as the anomaly score. Extensive experiments on nine benchmark datasets spanning financial, social, and citation network domains demonstrate that FoundAna consistently outperforms state-of-the-art baselines. The code implementation and Supplementary materials are here: this https URL.

---


### 202. [MoRE: Mixture of Reused Experts](https://arxiv.org/abs/2609.18176)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Eric S. Qiu, Utku Umur Acikalin, Justin Lovelace 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures decouple model capacity from computational cost, yet incur high memory footprints as parameters grow linearly with the number of experts. Recurrent Transformers achieve parameter efficiency by reusing layer weights, but typically lack the capacity for competitive language modeling. We propose Mixture of Reused Experts (MoRE), a hybrid that shares expert pools across groups of adjacent layers. Each layer retains its own router but selects from a larger shared pool, expanding the diversity of routing combinations without additional parameters. To enable shared experts to distinguish between layers, we introduce lightweight learnable depth embeddings that condition each layer's input before routing. Experiments across three model scales (114M-1.15B parameters) show that MoRE consistently achieves lower perplexity and stronger downstream performance than standard MoEs and state-of-the-art weight-sharing architectures at matched compute and parameter budgets, with only minimal modifications to existing MoE implementations.

---


### 203. [T-SANDHI: Tone Sandhi-aware Adaptive Network with Decoupled Hybrid Injection for Low-resource Taiwanese Hokkien Speech Recognition](https://arxiv.org/abs/2609.18194)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hung-Yang Sung, Chien-Chun Wang, Tien-Hong Lo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Taiwanese Hokkien automatic speech recognition (ASR), prior studies often treat tone sandhi as a major challenge under the assumption that models fail to process implicit phonological variations. However, our experiments on Taiwanese Hokkien reveal that speech foundation models actually handle tone sandhi variations effectively, and the real performance bottleneck stems from a localized confusion between these variations and retained citation tones. To address this, we propose T-SANDHI to explicitly decouple surface acoustics from underlying lexical intent on top of a frozen Whisper backbone. Using a lexicon-guided multi-task learning structure driven by text-derived pseudo labels, our lightweight hybrid injection module integrates independent citation and sandhi phonetic streams via dynamic gating. Extensive evaluation on the TAT-MOE corpus and two blind test sets demonstrates that this explicit disentanglement effectively resolves tonal mapping confusion, outperforming baselines with strict parameter efficiency.

---


### 204. [Multi-Appliance Non-Intrusive Load Monitoring via Label-Preserving Aggregate Recomposition and Prediction Consistency](https://arxiv.org/abs/2609.18315)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiangfeng Liu, Yanfang Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-intrusive load monitoring (NILM) estimates appliance power sequences from aggregate power, but models trained on source households commonly lose accuracy in unseen households. Aggregate power also contains loads from other appliances and measurement error, so predictions may depend on the residual background that co-occurs with source-household targets. Time-aligned submetered measurements and the additive decomposition of aggregate power expose a relation unused by window-wise supervision: an aggregate window can be recomposed by replacing only its residual background while preserving all modeled target-appliance power sequences pointwise. We combine label-preserving aggregate recomposition with prediction consistency. Both windows receive complete power and operating-state supervision. For each appliance, disagreement between the two power predictions is penalized only when both satisfy a fixed reliability criterion and only to the extent that it exceeds a fixed margin. The proposed method is implemented using a multi-appliance architecture with two-stage shared-to-specific mixture-of-experts routing. On REDD, UK-DALE, and REFIT, the proposed method lowers appliance-averaged mean absolute error relative to single-window training from 14.75 to 13.14 W, from 8.88 to 8.51 W, and from 15.83 to 14.55 W. Label-preserving aggregate recomposition and prediction consistency are used only during training, and add no inference-time module or parameter.

---


### 205. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Awomo-WM Team, Enhui Ma, Kaiwen Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling physical dynamics, including how objects move, interact, and change state, is central to video world models for embodied AI. We present StrucPhysVideo, a family of video world models that bridges physics-focused data curation with language- and action-conditioned prediction of scene evolution. Our data pipeline combines motion-aware video segmentation, quality and content filtering, and physical relevance verification with structured annotations of objects, materials, and temporally localized interactions. By disentangling camera motion from object behavior and explicitly describing contact, deformation, and state transitions, the pipeline provides supervision grounded in observable physical events. Building on these data, we introduce StrucPhysVideo-TI2V, a sparse Mixture-of-Experts (MoE) text-image-to-video model trained with a curriculum that progressively emphasizes physical dynamics while retaining general-domain video data. StrucPhysVideo-TI2V achieves state-of-the-art performance on Physics-IQ Verified, scoring 45.5% and outperforming Cosmos3-Super-Image2Video by 2.8 percentage points. Caption ablations across backbones further demonstrate the effectiveness of physics-focused supervision. We further extend StrucPhysVideo-TI2V to StrucPhysVideo-IA2V, an interactive image-action-to-video world model that predicts visual outcomes from robot end-effector commands. Action conditioning, causal autoregressive generation, and few-step distillation enable incremental robot rollouts with only four denoising steps. Together, StrucPhysVideo advances physical dynamics modeling from image- and language-conditioned video prediction toward action-driven interaction.

---


### 206. [SVMemAgent: A Streaming Video Memory Agent for Query-Agnostic Online Frame Selection](https://arxiv.org/abs/2609.18540)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dohwan Ko, Ji Soo Lee, Pierce Chuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most keyframe selection studies focus on offline settings, assuming access to the full video and query in advance. In contrast, real-world streaming scenarios require online frame selection under unknown video duration, without access to either the query or future frames during selection. To address this, we introduce Streaming Video Memory (SVMem), a compact and representative memory of previously observed content, updated continuously as the video stream unfolds. Building on this setting, we propose the Streaming Video Memory Agent (SVMemAgent), which dynamically maintains a memory by deciding at each timestep whether to replace an existing memory frame with the incoming frame or discard it. SVMemAgent is trained using Group Relative Policy Optimization (GRPO) with task-driven rewards derived from diverse question-answer pairs, implicitly exposing the policy to a distribution of queries during training so that SVMem retains generally informative frames at inference, when queries are unavailable. Experiments on both online and offline video benchmarks show that SVMemAgent consistently outperforms online frame selection baselines and achieves competitive performance with offline methods that assume access to the full video and query. Through task-driven rewards, SVMemAgent learns an emergent keyframe selection policy that prefers frames containing textual information, which may benefit downstream VideoQA tasks.

---


### 207. [VibeAvatar: Aligning Phonetic Kinematics and Human Aesthetics for High-Fidelity Talking Avatar Synthesis](https://arxiv.org/abs/2609.18632)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qilin Wang, Mingyu Li, Hao Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal talking avatar synthesis aims to generate realistic talking videos from a reference portrait and speech. Despite rapid progress in diffusion-based methods, existing approaches still struggle to jointly achieve accurate lip articulation, human-preferred motion aesthetics, and efficient inference. We observe that phonetic accuracy and motion aesthetics arise from fundamentally different sources and should be addressed at complementary stages rather than learned implicitly by a single generator. Based on this insight, we propose VibeAvatar, which disentangles these two objectives through a Phonetic Kinematics Adapter (PKA) that converts recognition-oriented speech features into phonetic-kinematic conditions at the conditioning stage, and an Aesthetic Motion Policy (AMP) that optimizes a flow-consistent stochastic sampling policy via Group Relative Policy Optimization (GRPO) at the post-training stage. With a lightweight flow-based motion generator operating in a compact 1D warp-based latent motion space, VibeAvatar achieves state-of-the-art results in articulation, aesthetics, and efficiency on both objective metrics and user studies, while generating a 10-second 512px video in under 10 seconds with only $\sim$3GB VRAM.

---


### 208. [Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows](https://arxiv.org/abs/2609.18820)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level evaluators. The policies organizations actually hold, such as referral thresholds, authority limits, and review requirements, are properties of the whole execution rather than of any one step. This mismatch admits a failure mode we call a Compositional Policy Violation (CPV): every individual step passes its own check while the composed execution violates the governing policy. A predicate over a single step cannot evaluate a property that step does not determine, so no improvement in the accuracy of the step-scoped monitors detects this class. We define CPVs as the failure of step-level compliance to compose, and present a taxonomy of four types: Authority Creep, Threshold Laundering, Cumulative Sum Violation, and Context Collapse. We show that the correct repair for each class is dictated by where the guarded quantity mutates. We then introduce a provenance-aware runtime architecture that evaluates policies over complete execution traces, recomputing guarded quantities from raw provenance rather than the pipeline's derived representation.

---


### 209. [FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning](https://arxiv.org/abs/2609.18964)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhilin He, Gauri Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Reinforcement Learning (FRL) enables collaborative policy learning across distributed agents with heterogeneous environments. While recent methods based on variance reduction, divergence penalization, and momentum optimization improve FRL under heterogeneous settings, they still primarily synchronize policy or value-network parameters and do not explicitly address distributional mismatch among heterogeneous clients. Therefore, we propose \textbf{FedGuide}, a FRL framework that uses diffusion priors as behavior models to provide personalized data supported distributions for heterogeneous local policy learning. Instead of directly averaging local policies, FedGuide aggregates those diffusion priors through Optimal-Transport Mixture-of-Experts (OT-MoE), preserving heterogeneous behavior modes in distribution space. It further develops a Distribution Correction Estimation (DICE) value baseline to provide low-variance, return-aware guidance for local policy improvement. Experiments across heterogeneous environments show that FedGuide outperforms representative FRL methods in client-average returns, final-round performance, and worst-round robustness, while maintaining stable learning under stronger heterogeneity.

---


### 210. [AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination](https://arxiv.org/abs/2609.19140)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matteo Golinelli, Idilio Drago, Matteo Boffa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents for security inspect web pages, source code, logs, configuration files, and command outputs. These environments may contain deceptive artifacts that influence the agent's behavior. We call this adversarial task contamination. Whereas prompt injection relies on attacker-supplied instructions, task contamination also includes non-instructional evidence, such as fake results and decoy endpoints. We present AgentLSD, a controlled framework for studying adversarial task contamination. AgentLSD uses Capture the Flag (CTF) challenges as its experimental environment. We inject trap artifacts, such as fake flags, misleading hints, decoy endpoints, and hidden cues, while preserving the intended CTF solution. The framework supports paired clean and trap-augmented experiments with deterministic trap generation, runtime injection, telemetry, and delivery verification. We evaluate six models on 11 web CTF challenges. In the clean condition, agents capture 41% of the flags, and no model solves every challenge. We then measure the impact of task contamination. Even when the agent still recovers the flag, traps increase the number of turns (+20) and reasoning tokens (+2k). Solve-rate effects are more heterogeneous, as some model-challenge pairs are largely unaffected while others follow decoys or submit wrong flags. These results show that clean CTF performance understates vulnerability to deceptive task evidence. AgentLSD isolates this effect and provides a reproducible benchmark for studying it. We release the framework, configurations, trap specifications, and raw traces.

---


> [!TIP]
> 当前位于：**201-210**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-210**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
