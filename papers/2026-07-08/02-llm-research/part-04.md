# 🧠 大模型相关研究 | 2026年07月08日

> 本类共 **248** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-248](./part-05.md)

---

### 151. [Beyond Random Sampling: Distribution-Aware Alignment for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2607.04249)

**<font color=#1a73e8>作者：</font>** Weihao Yan, Yeqiang Qian, Yi Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise medical image segmentation is crucial for clinical diagnosis and treatment planning, yet relies heavily on expensive expert annotations. Semi-supervised medical image segmentation (SSMIS) offers a cost-effective solution but typically operates under the assumption of independent and identically distributed (i.i.d.) data, defaulting to random sampling. While statistically valid at scale, this strategy suffers from severe representation bias in low-data regimes, failing to capture the heterogeneous medical data manifold. To address this, we propose a highly data-efficient framework driven by distribution alignment. First, we introduce an offline Distribution-Aware Sample Selection strategy. By leveraging Vision Foundation Models (VFMs) and our designed Density-K-Center algorithm, we explicitly identify representative structural anchors, establishing a more representative labeled domain. Second, to bridge the remaining distribution gap, we propose the Memory-guided Copy-Paste (MCP) module. Tailored for the inherent class imbalance in medical scans, MCP leverages a semantic memory mechanism to retrieve historically consistent priors for cross-domain alignment, encouraging semantic consistency. Coupled with an easy-to-hard progressive schedule, this framework effectively mitigates early-stage pseudo-label noise. Extensive experiments on six diverse 2D and 3D datasets demonstrate strong segmentation performance, particularly in extremely low-labeled scenarios (\eg, 1/16 ratio).

---


### 152. [Risk-Constrained Freshness-Aware Semantic Caching for Open-Web Retrieval-Augmented LLMs](https://arxiv.org/abs/2607.04281)

**<font color=#1a73e8>作者：</font>** Muhammad Mansoor, Tahir Ahmad, Yeo-Chan Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic caching reduces the latency and cost of retrieval-augmented generation (RAG) by serving cached answers to semantically similar queries, but most existing methods do not model the time-varying freshness of open-web evidence. We present FreshCache, a three-tier semantic cache that treats cache reuse as a risk-constrained temporal inference problem: before approving a cache hit, FreshCache estimates the probability that the cached result is stale using a fitted exponential decay model enhanced by a learned MLP, and approves reuse only when that probability falls below a per-tier error budget across answers (epsilon = 0.10), URL lists (epsilon = 0.20), and page content (epsilon = 0.35). This allows the system to degrade gracefully as entries age rather than forcing a binary choice between a stale hit and a full pipeline execution. We introduce FreshCache-Bench, a benchmark of 8,072 base queries across five freshness classes with ground truth staleness labels drawn from real web snapshots at 1, 12, 24 hours, and 7 days after a baseline crawl, expanded to 31,201 queries via paraphrase generation. At the 24-hour evaluation window, FreshCache_MLP achieves 97% search API savings at 0.1% hash-based stale error, and an LLM-judge evaluation on 396 confirmed change pairs shows that only 34.3% of detected content changes actually affect answer correctness, placing true answer-affecting stale error at approximately 0.034%. The rule-based FreshCache achieves 98% search savings at 3.3% stale error under a temporal holdout calibration, outperforming SemanticTTL (14.9% stale, 72% saved), vCache (7.2% stale, 47% saved), and SCALM (5.2% stale, 96% saved). Ablations show the temporal risk gate accounts for an 11.6 point reduction in stale error over similarity-only reuse, and the learned MLP reduces stale error a further 3.2 points over the rule-based model.

---


### 153. [Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection](https://arxiv.org/abs/2607.04292)

**<font color=#1a73e8>作者：</font>** Henry Kabuye, Biju Issac, Jeyamohan Neera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ransomware has evolved into a complex, adaptive, and fast-moving adversary category in which static signatures and monolithic classifiers fail to generalise under concept drift, evasion, and behavioural polymorphism. In this paper, we present Agentic SABRE (Semantic-Behavioural Arbitration for Ransomware Evaluation), an uncertainty-aware, neuro-symbolic, multi-agent framework for adaptive ransomware detection. SABRE fuses semantic, representation-based evidence with behavioural, time-window forensic telemetry and employs Monte Carlo Dropout inference to quantify epistemic uncertainty for each agent. We introduce a decision-layer orchestrator that performs risk- and uncertainty-aware triage using two interpretable thresholds: a risk score and an uncertainty budget. High-confidence, high-risk samples are automatically contained, while uncertain or borderline cases are escalated to human analysts, establishing a flexible computational contract between autonomous response and analyst oversight. To support auditability and trust, SABRE integrates post-hoc explainability mechanisms, including gradient saliency, permutation importance, and counterfactual analysis, enabling both local and global interpretation of agent decisions. Extensive evaluation on RDset and RanSMAP demonstrates that Agentic SABRE preserves perfect discrimination on saturated semantic datasets, with AUC equal to 1.0, while improving robustness under weak behavioural signals. It achieves up to a 4.9 percent relative reduction in false escalations at equal recall while maintaining calibrated predictive uncertainty. Counterfactual analysis further shows that semantic and behavioural decisions can be reversed with bounded perturbation cost, indicating stable and interpretable decision boundaries.

---


### 154. [CausalGame: Benchmarking Causal Thinking of LLM Agents in Games](https://arxiv.org/abs/2607.04293)

**<font color=#1a73e8>作者：</font>** Zhenhao Chen, Yongqiang Chen, Chenxi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building AI Scientist agents with Large Language Models (LLMs) has recently attracted growing attention. Since scientific discovery fundamentally relies on uncovering causal relationships from observations, the capability of causal thinking, i.e., distinguishing causation from correlation and recognizing hidden biases, is essential to LLM agents. Although a number of benchmarks exist for AI Scientists, none explicitly incorporate challenges from selection bias, measurement error, and hidden confounders that widely exist in real-world scientific discovery. To this end, we present CausalGame, a benchmark that evaluates the causal thinking capabilities of LLM agents through interactive games. CausalGame asks LLM agents to actively design experimental protocols, collect observation data, and derive a final solution with an explanation report. To emulate realistic scientific discovery challenges, we design 14 scenarios that incorporate selection bias, measurement error, and hidden confounders. Across 30 LLM agents, none demonstrates reliable causal thinking: the best model reaches only 68.0% survival against analytical optima of 78-85%, and merely 5-7% of sessions receive credits on the causal-reasoning rubrics. CausalGame provides a scalable and controlled testbed for evaluating the causal thinking of AI Scientist agents.

---


### 155. [HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/abs/2607.04302)

**<font color=#1a73e8>作者：</font>** Hui Dong, Yanzhao Li, Jie Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present HiFA4, a post-training operator-level design that executes both QK^T and PV in FlashAttention as 4-bit HIF4 Cube GEMMs for LLM inference on Ascend NPUs, while maintaining the online softmax state in FP16. To our knowledge, HiFA4 is the first Ascend-HIF4-targeted design of this kind evaluated on standard NLP benchmarks.
HiFA4 combines two mechanisms. Smooth-QK applies a calibration-static per-channel equivalent rescaling to Q and K after RoPE, transferring quantization difficulty from K to Q without per-tile online reduction at inference. P-Reordering accumulates the softmax normalizer from the same quantized attention weights P_hat used in the PV GEMM, rather than from a higher-precision reconstruction. We show that this inconsistent formulation introduces a coherent output-scaling error, and validate the effect on a Qwen3-8B Layer-0 MMLU trace, where all 3.6M measured attention tiles exhibit net probability-mass loss with median epsilon_bar = -0.064. P-Reordering also allows the normalizer to be fused into the PV Cube GEMM.
Across five LLMs, HiFA4 reduces quantization-induced decision drift. On Qwen3-8B, it recovers 37.5% of the accuracy gap introduced by direct HIF4 quantization, narrows the sample-weighted accuracy loss from 1.12 pp to 0.70 pp, reduces BF16-inconsistent MMLU predictions from 16.3% to 8.2%, and cuts MMLU accuracy regressions by 57% (1071 to 465). On Gemma2-9B, mild smoothing keeps HiFA4 within 0.7 pp of BF16 while reducing MMLU regressions by 27%. On LLaMA3.1-8B, Mistral-7B, and Phi-4B, where Smooth-QK is disabled, P-Reordering with the adopted Q-Mean auxiliary still reduces full-set MMLU regressions by 41-52%. A preliminary instruction-scheduling analysis projects a 35.4% critical-path latency reduction relative to BF16 by fusing the softmax normalizer into the PV Cube GEMM; on-hardware validation is left to future work.

---


### 156. [SAD-LoRA: Spectral Alignment for Low-Rank Knowledge Distillation](https://arxiv.org/abs/2607.04306)

**<font color=#1a73e8>作者：</font>** Omer Tariq, Syed Muhammad Raza, Jeongbae Son  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distilling a fine-tuned teacher into a LoRA-adapted student is a standard recipe for parameter-efficient compression, but output-level KD does not explicitly control which rank-$r$ weight subspace the adapter occupies. We propose \textbf{SAD-LoRA} (\textbf{S}pectral \textbf{A}lignment \textbf{D}istillation), which selects this subspace from the data-weighted student-space reference update $\DWT\Sigx^{1/2}$ and maintains it during training via a differentiable principal-angle loss on $\colspan(B)$. We show that the data-weighted distillation error decomposes exactly into subspace misalignment, within-subspace coefficient mismatch, and irreducible rank residual; standard KD can affect the first term only indirectly through output gradients. On controlled synthetic problems with a flat teacher spectrum, SAD-LoRA reduces the subspace-misalignment term from $51\%$ to nearly zero and lifts final subspace alignment from $0.49$ to $1.00$. On RoBERTa-large to RoBERTa-base distillation across six GLUE tasks, SAD-LoRA improves rank efficiency: at $r{=}4$, it matches or beats the strongest included spectral baseline on five of six tasks, and at $r{=}8$ it gives the best result on SST-2 and CoLA. Ablations identify subspace alignment as the load-bearing component, while coefficient matching is auxiliary.

---


### 157. [Aura: Consistent Multi-Subject Video Generation via VLM-Grounded Semantic Alignment](https://arxiv.org/abs/2607.04311)

**<font color=#1a73e8>作者：</font>** Zixiang Zhou, Zhentao Yu, Yifeng Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven and multi-element video generation are central to controllable video synthesis, but existing methods still struggle to preserve identity consistency and model complex relationships among multiple subjects. In this paper, we propose Aura, a unified framework for high-fidelity and identity-consistent video generation. To better capture scene dynamics and subject interactions, we introduce AI director-level captions that provide dense and structured descriptions of video content. We further leverage a vision-language model (VLM) with learnable queries to extract multimodal semantic features from textual and visual references, covering both global semantics and fine-grained visual cues. To bridge the representational gap between the VLM and the Diffusion Transformer (DiT), we design a two-stage alignment strategy that progressively maps VLM features into the DiT feature space. For visual conditioning, we adopt token concatenation to inject reference information directly into the generation process. To distinguish heterogeneous subject types and reduce common copy-paste artifacts, we develop a subject-aware RoPE-Shift mechanism. To further differentiate reference images of different categories, we introduce subject-aware learnable tokens. In addition, we introduce Memory Tokens to balance the training signal across examples with different numbers of reference subjects. During inference, Progressive-APG (Adaptive Prompt Guidance) further alleviates oversaturation and improves semantic alignment with user prompts. Finally, we build a high-quality video-subject image dataset through a dedicated data construction pipeline. Extensive experiments show that our method achieves state-of-the-art performance on both single-subject generation and more challenging multi-element scenarios.

---


### 158. [HAS-Bench: Evaluating LLM-Based Human-Agent Systems under Configurable Human Participation](https://arxiv.org/abs/2607.04329)

**<font color=#1a73e8>作者：</font>** Yaozu Wu, Wei-Chieh Huang, Jizhou Guo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate in settings where humans are active collaborators rather than passive task providers. We introduce HAS-Framework, a graph-based framework that represents humans and LLM-powered agents as first-class participants with explicit roles, permissions, communication paths, and action authority. Building on this framework, HAS-Bench evaluates Human-Agent Systems under configurable human participation across agency levels, interaction channels, and persona policies. The benchmark measures both task outcomes and process-level collaboration behavior, including clarification quality, feedback utilization, control calibration, safety, initiative, and interaction cost. Experiments across six domains show that human participation can substantially improve task completion and failure recovery, but the gains depend on when, how, and by whom human input is exercised.

---


### 159. [On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models](https://arxiv.org/abs/2607.04332)

**<font color=#1a73e8>作者：</font>** Chee Heng Tan, Zhuoyi Lin, Mehul Motani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we consider the setting where large language models (LLMs) are trained using reinforcement learning (RL) to simultaneously improve reasoning accuracy and verbalize its confidence. Our reward scheme uses two functions for rewarding confidence verbalized by the LLM: one when the LLM is correct and a different one when the LLM is incorrect. With a poorly designed reward scheme, the LLM may be incentivized to answer incorrectly so that it can be confident that its answer is indeed incorrect, a phenomenon that we call confidence reward hacking. We propose the concept of non-hackable confidence reward schemes and define a spectrum of such reward schemes for RL confidence calibration training in LLMs. We demonstrate that selective confidence reward hacking can occur in practical datasets with reward schemes that are not designed to be non-hackable. We also demonstrate that the reward scheme with the best calibration to accuracy tradeoff depends on the dataset and the application, and propose using the reward scheme as a hyperparameter to optimize the tradeoffs in accordance to what is important for the application. The code of our experiments is available in this https URL.

---


### 160. [IRIS: An Intelligent Vision-Language System for Ocular Surface Diseases via Topic Tree and Scene-Driven VQA Generation](https://arxiv.org/abs/2607.04344)

**<font color=#1a73e8>作者：</font>** Hao Wei, Wenjin Qi, Dasen Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Vision-Language Models (VLMs) demonstrate remarkable generic capabilities, their clinical reasoning in specialized domains like ocular surface diseases (OSDs) is severely hindered by a paucity of high-fidelity, multimodal instruction-tuning data. To dismantle this data bottleneck, we introduce IRIS, an Intelligent Recognition and Interaction System tailored for fine-grained OSD understanding via external eye photography. First, we curate IRIS-120K, the largest and most comprehensive OSD visual question-answering (VQA) dataset to date. Crucially, to overcome the semantic shallowness of conventional image-caption pairs, we propose a synergistic data generation paradigm to explicitly inject clinical priors. Our data engine operates via a dual-branch framework: 1) a Topic Finding Tree (TFT) that hierarchically anchors visual features to precise anatomical and pathological concepts, enforcing rigorous medical deduction logic; and 2) a Scene-driven strategy that synthesizes role-adaptive clinical dialogues to ensure pragmatic generalization. By explicitly aligning a compact 4B-parameter VLM on this structurally enriched corpus, IRIS achieves state-of-the-art performance, comprehensively outperforming both generalist and specialized medical VLMs with up to 34B parameters. Our findings underscore that structured knowledge injection profoundly prevails over sheer parameter scaling, unlocking the potential for resource-efficient, expert-level AI deployment on mobile edge devices for scalable OSD screening. Code, datasets, and model weights will be publicly released by this repo.

---


### 161. [WPG-MoE: Weak-Prior-Guided Dense Mixture-of-Experts for User-Level Social Media Depression Detection](https://arxiv.org/abs/2607.04350)

**<font color=#1a73e8>作者：</font>** Xian Li, Yuanhe Tian, Yang Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online social media posts provide scalable signals for early depression screening, and recent studies mainly improve pre-classification evidence through risk-post selection, symptom grounding, and clinically informed feature construction. However, these screening-stage designs often leave final decisions to a single detector, overlooking how users heterogeneously express depressive risk after screening. A monolithic classifier must average across heterogeneous users, which may dilute localized evidence and cause misclassification, especially for non-self-disclosing users. To address this issue, we propose WPG-MoE, a weak-prior-guided dense mixture-of-experts framework built on a shared large language model (LLM) backbone. WPG-MoE derives user-level weak semantic priors to softly route users to experts matched to different evidence layouts. We formulate this process as learning using privileged information (LUPI): rich LLM-extracted structured evidence guides training-time routing, while inference retains only Patient Health Questionnaire-9 (PHQ-9) template screening and the deployable backbone. Experiments on Chinese and English datasets show that WPG-MoE outperforms strong baselines with interpretable routing behavior.

---


### 162. [RL Forgets! Towards Continual Policy Optimization](https://arxiv.org/abs/2607.04364)

**<font color=#1a73e8>作者：</font>** Mao-Lin Luo, Zhe-Xu Wang, Zi-Hao Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual post-training is becoming a central paradigm for adapting vision-language models to evolving tasks. Recent work has increasingly favored reinforcement learning over supervised fine-tuning, driven by the belief that reinforcement learning is inherently less prone to forgetting. However, the belief remains insufficiently validated, as existing evidence is largely drawn from outdated or homogeneous benchmarks. To revisit this assumption, we introduce MRCL, a Multimodal Reasoning Continual Learning benchmark built from diverse and recently released multimodal datasets. Experiments on MRCL show that reinforcement learning can still suffer from severe catastrophic forgetting during continual post-training. To address this challenge, we propose Continual Policy Optimization (CPO), a replay-free framework grounded in the prior-task behavioral KL objective. CPO uses a theoretically justified parameter-movement regularization to limit policy drift on previous tasks. Extensive experiments across multiple model scales demonstrate that CPO consistently reduces forgetting while preserving, and in some cases improving, pretrained model capabilities. On Qwen3-VL-8B, CPO reduces forgetting by 13.7\% and improves pretrained capability by 7.0\%. The implementation code is available at this https URL.

---


### 163. [Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs](https://arxiv.org/abs/2607.04371)

**<font color=#1a73e8>作者：</font>** Akhiad Bercovich, Talor Abramovich, Daniel Afrimi 等 70 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Nemotron-Labs-3-Puzzle-75B-A9B, a compressed variant of Nemotron-3-Super optimized for interactive deployment. We designed the model to maximize server throughput under high user throughput constraints. In interactive serving workloads on a single 8xB200 node, Puzzle-75B-A9B achieves approximately 2x higher server throughput than Nemotron-3-Super at matched user throughput constraints. In ultra-long-context deployment on a single H100 GPU, the compressed model increases 1M-token concurrency from 1 request to 8 requests. Puzzle-75B-A9B is constructed using a multi-stage pipeline that combines the Iterative Puzzle compression framework with knowledge distillation, reinforcement learning, quantization, and a Multi-Token Prediction head. The compression process jointly optimizes heterogeneous MoE pruning, active parameter budget, and Mamba pruning to improve inference efficiency while preserving model quality. We evaluate Puzzle-75B-A9B on a broad suite of reasoning, coding, multilingual, long-context, and agentic benchmarks. Despite substantial compression, the model retains strong downstream accuracy relative to the parent model across a wide range of tasks. These results demonstrate that large hybrid MoE models can be substantially optimized for deployment efficiency while maintaining strong downstream capability.

---


### 164. [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](https://arxiv.org/abs/2607.04389)

**<font color=#1a73e8>作者：</font>** Yuhong Luo, David M. Pennock, Xintong Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> It is increasingly common to aggregate predictions from multiple LLMs, each with domain expertise or access to private tools and data, to improve collective prediction performance. In decentralized settings, aggregation weights need to be determined without access to models' private information and should remain robust to strategic reporting. We propose a family of advantage-aligned wagering mechanisms for LLM aggregation (WALLA), in which each model reports a prediction and a learned wager, and predictions are aggregated using wagers as weights. WALLA introduces a leave-one-out baseline into the net payout function, yielding three desirable properties: (1) dominant-strategy incentive compatibility of prediction under arbitrary belief structure, (2) advantage--wager alignment, where the optimal wager is proportional to the model's expected score advantage, and (3) prediction-agnostic wager optimization, enabling decentralized learning of wager policies without requiring optimal predictions. We further instantiate two mechanism variants that trade off normality and no-arbitrage while maintaining a bounded worst-case deficit for the mechanism. Experiments on question-answering and forecasting benchmarks across heterogeneous models and private-information settings show that WALLA matches centralized aggregation methods in predictive performance, while simultaneously achieving decentralized learning, advantage-aligned aggregation weights, uncertainty awareness, and incentive-compatible prediction.

---


### 165. [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](https://arxiv.org/abs/2607.04391)

**<font color=#1a73e8>作者：</font>** Serge Lacasse, Jérémie Hatier, Alex Baker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory remains a structural weakness of AI agents. The dominant approach, retrieval-augmented generation (RAG), relies on embedding-based similarity search, which is opaque by construction, difficult to audit, and bounded by the theoretical limits of vector representations. We present the Memory-Orchestrated Semantic System (MOSS), an agentic memory architecture in which the agent drives retrieval over a structured relational database. MOSS is model-agnostic, storage-agnostic, and API-agnostic: it runs on any relational engine, connects to any LLM provider (or to deterministic non-LLM processes), and deploys on any infrastructure, local or cloud. Its retrieval execution is symbolic and reproducible (once a query is formulated, no LLM participates in the retrieval loop) and every step of the system, from indexing to answer formulation, is logged and inspectable, making MOSS auditable by construction. Rather than imposing an external ontology, MOSS derives its conceptual vocabulary from the corpus itself. We report on a longitudinal deployment unique in the agentic-memory literature: a year of continuous production over an individual scholar's working corpus--a conversational corpus reaching back to October 2024 (some 44 million tokens, retroactively indexed) comprising 110,183 segments, alongside 163,494 catalogued documents, 569 inductively derived concepts, 322,662 concept annotations, and eleven metadata graphs totaling approximately five million relations--across four successive infrastructure generations. While the present case is that of a single researcher, the architecture is in no way specific to one person: it serves a team, an institution, or any entity that accumulates knowledge over time. We argue that auditable, sovereign, structurally unbounded memory is a precondition for AI agents intended to accompany a person or an organization over years rather than sessions.

---


### 166. [MechMath Agent Team: LLM Driven Agents for Mathematical Research](https://arxiv.org/abs/2607.04394)

**<font color=#1a73e8>作者：</font>** Yichuan Cao, Ruichen Qiu, Junqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI reasoning has become a central focus in contemporary artificial intelligence, largely driven by the success of large language models. However, mathematical research, which is characterized by non-linear derivation paths, rigorous logical requirements, and protracted exploration cycles, poses severe challenges for existing reasoning systems. To overcome these limitations, we present the MechMath Agent Team (MMAT), which is a large language model driven agent designed to serve as a co-pilot throughout the full cycle of mathematical research. We design a tripartite Harness Architecture that decouples system responsibilities into Control, Execution, and Augmentation planes, thereby reconciling rigorous logical control with the agility demanded by open-ended research. Building upon this framework, we instantiate three specialized agents: a Knowledge Base Manager, a Natural Language Prover, and a Formal Language Prover, all operating in a closed loop to produce formally certified mathematical proofs. We evaluate MMAT on open problems in Number Theory, Algebraic Complexity Theory, Differential Algebra, Operator Algebra, and Inequalities. Across a two-month deployment, 11 problems have been solved, demonstrating its capacity to act as a co-pilot throughout the entire research cycle. The contributions are threefold: a general decoupled Harness Architecture for multi-agent mathematical reasoning, its concrete instantiation in the MMAT system, and empirical validation on a diverse suite of open problems.

---


### 167. [NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation](https://arxiv.org/abs/2607.04395)

**<font color=#1a73e8>作者：</font>** Junjie Tang, Jun Huan, Hao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent agentic approaches to LLM-based kernel generation have achieved impressive results on CUDA. For emerging AI accelerators such as AWS Trainium and Inferentia, automated kernel generation and optimization remain largely unaddressed. Writing kernels for these chips via the Neuron Kernel Interface (NKI) is particularly challenging: developers must navigate a multi-engine architecture, tile-based programming, and explicit data movement across multi-level memory hierarchy. Moreover, no publicly-available training data, benchmarks, or tool-augmented agents exist for this domain. We introduce NKI-Agent, the first system combining domain-specific supervised fine-tuning (SFT) with a compile-verify-fix agent loop for NKI kernel generation. We adapt the existing CUDA-Agent framework to Neuron hardware, curate 6,000 NKI kernel generation tasks for training, and construct NKIBench, a 250-task benchmark across three difficulty levels. Evaluated on real Trn1 hardware, NKI-Agent with Claude Opus 4.8 and a rank-aware system prompt achieves a 77.3% pass rate on the 150-task NKIBench. We show that tool use is critical: Opus 4.8 scores 6% in single-shot mode without agent tools. On a 60-task subset, we show that an SFT-trained Qwen3-Coder-30B-A3B achieves 25.0% pass rate at 1/100th the cost, outperforming Claude Sonnet 4 (15.0%). We also report that Group Relative Policy Optimization (GRPO) with binary compilation reward fails to improve over SFT, providing guidance on reward design for RL-based kernel generation.

---


### 168. [The Good, the Bad, and the Brittle: Benchmarking Robustness and Generalisation of Histopathology Foundation Models](https://arxiv.org/abs/2607.04401)

**<font color=#1a73e8>作者：</font>** Dhyey Yajnik, Amina Asif, Fayyaz Minhas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How robust and generalisable are pathology foundation models and have their scaling limites been reached? We benchmarked twelve pathology foundation models (PFMs) and ResNet baselines using our Robustness Evaluation and Enhancement Toolbox (REET) across eleven clinically realistic perturbations and a dissimilarity-driven Non-Redundant K-fold validation (NR-Kfold) protocol. We introduce a Perturbation Performance Index (PPI) to summarise accuracy trends under controlled perturbation sweeps and analyse robustness scaling with parameter count. We show that PFMs consistently outperform CNNs in both robustness and domain generalisation, yet model scaling shows diminishing returns: mid-sized models such (UNI2/Virchow-2 etc.) achieve comparable or greater resilience than larger systems. NR-Kfold analysis further reveals systematic accuracy loss and increased variability when training-test similarity is broken, underscoring the need for explicit distribution-shift evaluation. These findings suggest that the next generation of pathology foundation models must prioritise data quality, multimodality information and domain alignment over parameter count to achieve genuine clinical reliability.

---


### 169. [Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling](https://arxiv.org/abs/2607.04409)

**<font color=#1a73e8>作者：</font>** Fan Feng, Yujia Zheng, Minghao Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning and planning in imagination using world models provides an effective paradigm for training agents for decision-making. However, existing approaches often rely on high-dimensional latent spaces or generic visual embeddings that retain many factors irrelevant to control, limiting efficiency and generalization across tasks. To this end, we study how agents can learn world models with representations that are task-specific, minimal, and sufficient for decision-making. We achieve this via a closed-loop synergy between the agent and the world model, in which structured world-model learning distills task-sufficient representations from informative interaction data. On the agent side, agents actively probe the environment to collect informative trajectories that expose task-relevant latent factors, guided by an adaptive curriculum. On the world-model side, we learn structured representations over observations to distill compact, task-sufficient latent states from the collected interaction data. This synergy enables the empirical recovery of task-sufficient latent representations that capture all control-relevant factors. Leveraging these representations, the resulting policies achieve improved sample efficiency and generalization, including generalization across skills, object-skill compositions, and previously unseen tasks on standard continuous-control and robotic-manipulation benchmarks.

---


### 170. [AI Wizards at EXIST 2026: Hierarchical Soft-Label Learning for Multimodal Sexism Identification in Memes](https://arxiv.org/abs/2607.04410)

**<font color=#1a73e8>作者：</font>** Matteo Fasulo, Antonio Gravina, Luca Tedeschini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the AI Wizards submission to EXIST 2026 for multimodal sexism identification in memes. The task is composed of three, increasingly harder subtasks. We model them hierarchically as conditional soft-label prediction over empirical annotator distributions. Our system maps fixed Gemini Embedding 2 vision-language representations through a lightweight Gated MLP trained with KL divergence and homoscedastic uncertainty weighting. Our submissions ranked first on Task 2.3 and fourth on Tasks 2.1 and 2.2 on the official Soft-Soft leaderboards. The code is available at this https URL

---


### 171. [LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL](https://arxiv.org/abs/2607.04412)

**<font color=#1a73e8>作者：</font>** Yujin Kim, Namgyu Ho, Sangmin Hwang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for non-verifiable instruction following increasingly relies on LLM judges with prompt-specific rubrics as reward signals. While recent methods adapt these rubrics to the evolving policy during training, the training prompts themselves remain static, drawn from fixed corpora. This static approach often results in a critical misalignment between prompt difficulty and policy capability, leaving the judge unable to recover a discriminative reward signal when prompts fail to elicit quality variance among rollouts. To address this misalignment, we introduce LLM-as-a-Tutor, a framework that extends the LLM's role from judge to tutor: a single model serves as an examiner that pairwise-compares policy rollouts to detect non-challenging prompts, and as a generator that appends atomic constraints to them. This append-only design monotonically raises difficulty in step with the policy's capability, producing a self-calibrating training signal without external difficulty schedules. On three complex instruction-following benchmarks, our method consistently outperforms both policy-unaware baselines and prior policy-adaptive methods that adapt rubrics or rewrite prompts, suggesting prompt adaptation as a missing axis of policy-awareness in non-verifiable RL.

---


### 172. [Agent Step Value: State-Transition Measurement with State-Grounded LLM Evaluators](https://arxiv.org/abs/2607.04419)

**<font color=#1a73e8>作者：</font>** Andrew Zhang, Chengzhan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agent evaluations collapse a multi-step trace into a final answer, a success flag, or a trajectory-level score. These aggregates obscure the diagnostic question developers need most: which action changed the state in a useful direction? We introduce Agent Step Value (ASV), a state-transition measurement framework that scores each observed action by the change it induces in a state-grounded evaluator's distribution over fixed candidate outcomes. ASV renders redacted before/after state projections, uses a stateless LLM evaluator to assign candidate log scores, and reports both gold-free belief diagnostics and offline oracle validation metrics. A label-free rationale pass separates evaluator deliberation from one-token option scoring, preserving candidate likelihoods while exposing leakage and floor-score events. On 100 reviewed open-QA evidence-seeking tasks with live PubMed retrieval, a partially live DeepSeek actor, and DeepSeek log-probability scoring, ASV evaluates 1,100 steps and 2,200 states. Under the fixed-layout rationale-conditioned protocol, mean gold-margin gain is -2.335 (trajectory-bootstrap 95\% CI [-3.395, -1.272]), entropy movement is 0.000, and mean Bayesian surprise is 2.693. ASV therefore localizes constructive and destructive belief pivots that final-answer scores and entropy-only step metrics miss. We release the standalone ASV Eval toolkit.

---


### 173. [Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention](https://arxiv.org/abs/2607.04422)

**<font color=#1a73e8>作者：</font>** Siyu Ding, Mingchuan Ma, Jiabo Tong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent NVFP4 pretraining methods mainly target transformer linear layers, leaving optimizer states, optimizer arithmetic and attention underexplored in 4-bit pipelines. This critical gap blocks stable full-stack 4-bit pretraining, as the three core modules exhibit unique numerical failure patterns: linear layers hit hard quantization noise limits with dimension-propagated error amplification; AdamW second moments are heavy-tailed non-negative values fragile to low-precision denominators; attention carries error-prone computation paths demanding strict forward-backward quantization consistency. We propose Full-Stack FP4, the first complete NVFP4 pretraining framework resolving all three stability bottlenecks via module-wise precision strategies. For linear projections, LoRA-SVD lightweight decomposition suppresses quantization noise and breaks the direct-quantization error ceiling, shrinking the linear-only loss gap from 1.40% to 0.61%. For optimizers, we design AdamW second-moment transformation for robust NVFP4 storage and fully support native NVFP4 Newton-Schulz iterations for the Root (Muon) optimizer. For attention, a mixed-precision scheme quantizes Q/K/V and backward dS while guarding vulnerable paths in BF16, paired with unified tensor reuse to sustain forward-backward alignment. We further analyze fast error accumulation in naive low-bit matrix multiplication and the extreme sensitivity of PV / dOV^T attention branches. All modules are plug-and-play with cumulative stability and efficiency improvements. Our 3B/64B-token pretraining validates near-BF16 performance with merely 1.47% loss gap, verifying feasible stable end-to-end NVFP4 LLM pretraining.

---


### 174. [Transferability Between Understanding and Generation in Unified Multimodal Models](https://arxiv.org/abs/2607.04423)

**<font color=#1a73e8>作者：</font>** Jiwon Kang, Heeji Yoon, Jaewoo Jung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) integrate image understanding and generation within a single architecture, yet how the two tasks interact remains understudied. We investigate $\boldsymbol{\mathsf{transferability}}$ in UMMs: whether training a capability on one task improves the same capability on the other without explicit supervision. Through controlled experiments, we empirically find that transferability depends on architecture-models with fully shared transformer backbone and a unified visual encoder exhibit consistent cross-task transfer, while loosely coupled designs show little or none. Leveraging this transferability, we propose a practical training strategy. The most straightforward way to improve a target generative capability (e.g., counting) is to fine-tune generation directly, but this can degrade visual quality due to distribution shift. Instead, we train the corresponding understanding task and let it transfer into generation, which improves capability-specific generative performance while minimizing distribution shift. We validate this across three capabilities-counting, spatial relation, and text recognition/generation-showing that cross-task transferability can be systematically exploited in UMMs.

---


### 175. [dOPSD: On-Policy Self-Distillation for Diffusion Language Models](https://arxiv.org/abs/2607.04428)

**<font color=#1a73e8>作者：</font>** Phuong Tuan Dat, Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate text by iteratively denoising a masked sequence, offering a parallel alternative to autoregressive models, but eliciting strong reasoning through post-training remains difficult: supervised fine-tuning is off-policy and suffers from exposure bias, while reinforcement learning gives only sparse, sequence-level rewards and is hard to apply without tractable sequence likelihoods. On-policy self-distillation (OPSD) offers a promising alternative, using one model as both student and teacher to provide dense, token-level, on-policy supervision, but its effectiveness hinges on giving the teacher privileged information (PI) - typically an instance-specific ground-truth reference unavailable at inference - so the student ends up distilling a weak PI-free consensus policy that yields little improvement on dLLM reasoning. We introduce dOPSD, which instead derives the teacher's privilege directly from the student's own denoising trajectory, evaluating masked positions using later, more-decoded steps of that same trajectory rather than an external label, so the teacher's advantage emerges from the model's own decoding process; on Dream and LLaDA, dOPSD improves both in-domain math reasoning and out-of-domain code generation, outperforming supervised and on-policy baselines.

---


### 176. [evalci: A Python Library for Statistically Rigorous Comparison of Language Model Evaluations](https://arxiv.org/abs/2607.04429)

**<font color=#1a73e8>作者：</font>** Shreyas K Chandrahas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The dominant practice in language model evaluation is to report a single accuracy number per model and declare the higher one better, without testing whether the gap could plausibly be sampling noise. On benchmarks of a few thousand items, and under temperature sampling where a model can differ from itself run to run by more than the reported gap between models, this practice routinely overstates confidence in headline claims. The statistical machinery to fix this -- confidence intervals, paired significance tests, power analysis, clustered standard errors, multiple-comparison correction -- is well established, but no standard, pip-installable tool packages it in the shape an evaluation actually takes: a per-item results table. We present evalci, a pure-Python library (numpy/scipy/pandas only) that turns a per-item results table into a publication-ready claim -- e.g., "Model A beats Model B, $\Delta=3.1$ pts, 95% CI [1.2, 5.0], paired permutation $p=0.002$, $n=1{,}319$" -- in one function call, with adapters for lm-evaluation-harness and HELM output. Every routine is validated against an independent reference (statsmodels, or brute-force exact enumeration) rather than only against itself. As a case study, we re-analyze a public comparison of nine language models' MMLU accuracy and find that 3 of the 8 adjacent leaderboard-rank gaps are not statistically significant after correcting for the 36 pairwise comparisons the ranking implies. evalci is available at this https URL (source: this https URL, DOI: this https URL)

---


### 177. [Uncertainty-Aware Abstention in Large Language Models with Provable Alignment Guarantees](https://arxiv.org/abs/2607.04430)

**<font color=#1a73e8>作者：</font>** Sijin Dong, Hiroyuki Shinnou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in question answering (QA) systems, yet they may generate hallucinated or misaligned responses without reliable confidence estimates. Uncertainty quantification (UQ) offers a natural basis for selective answering, where a system answers only when its prediction is deemed reliable and abstains otherwise. However, existing uncertainty scores for LLMs are often heuristic: a threshold chosen on such scores does not, by itself, provide statistical guarantees on the error rate among accepted answers. We propose CIC, a confidence-interval-based calibration framework that converts arbitrary uncertainty scores into risk-controlled selective answering rules. Given a held-out calibration set, CIC evaluates each generated response using an application-specific alignment criterion and associates it with an uncertainty score and a binary error label. For each candidate uncertainty threshold, CIC estimates the acceptance-conditioned error rate and constructs a high-probability upper confidence bound using either Hoeffding-style or Clopper-Pearson confidence intervals. It then selects the largest threshold whose upper bound is below a user-specified risk level $\alpha$, thereby maximizing the answering rate subject to a finite-sample reliability constraint. Under exchangeability, CIC guarantees with probability at least $1-\delta$ that the selected threshold, if non-null, controls the error rate among accepted answers at level $\alpha$. We evaluate CIC on both closed-ended and open-ended QA benchmarks across seven LLMs and multiple uncertainty estimators. Experimental results show that CIC consistently achieves valid risk control while retaining strong answering efficiency, providing a practical and statistically grounded mechanism for deploying LLMs in reliability-sensitive QA workflows.

---


### 178. [Operator-on-F complements value-equivalence: a planning-time diagnostic for latent world models](https://arxiv.org/abs/2607.04464)

**<font color=#1a73e8>作者：</font>** Donna Vakalis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World-model evaluation for model-based reinforcement learning typically asks whether the learned model predicts reward and value well, which can leave planning-relevant errors in the model's latent rollouts unmeasured. We introduce a complementary diagnostic, operator-on-F, that compares a model's k-step latent pushforward to the environment's on an observable subset F, using the model's own predictor. On a TD-MPC2 size sweep over cheetah-run, reward-prediction error stays within [0.028, 0.091] for every model size - only about 3x variation - so an unnormalized reward-fit check has narrow resolution to distinguish them; the (unnormalized) Bellman residual and reward error themselves have weak relationships with return (Spearman -0.10 and -0.30). Operator error spans 0.28 to 2.62 over the same sizes. At 317M the operator error is 2.62 - an order of magnitude above the 0.28-0.36 cluster - and the planning return collapses to 0.9, while reward-prediction error (0.091) is the highest of the five but stays within the same small [0.028, 0.091] range as the rest of the sweep. The rank correlation between operator error and return loss is -0.90 (anchor-bootstrap 95% CI [-0.90, -0.70] at n=5 sizes; leave-one-out removal of any single size leaves it at -0.80 or stronger). The operator also returns informative, architecture-discriminating estimates in a cross-architecture comparison between TD-MPC2 and a pure-SSL latent world model. The operator diagnostic complements value-equivalence rather than replacing it.

---


### 179. [Don't Commit Alone: Joint Token Commitment in Diffusion Large Language Models](https://arxiv.org/abs/2607.04469)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) commit multiple tokens per denoising step by decoding each selected position independently from the shared context; when those positions are dependent, the resulting factorization error is captured by conditional total correlation, which confidence-based selection cannot observe from marginals alone. We propose CoCommit, a marker-gated coordination pass that briefly defers commitment: after the usual bundle selection, a learned marker announces the commit set and the backbone's last-$n$ layers are re-applied so marked positions coordinate -- approximating joint-mode decoding -- before greedy argmax writes tokens. The method reuses existing weights with one extra partial forward pass and no auxiliary model. On LLaDA2.1-mini with LoRA adapters and matched greedy inference, joint commitment improves accuracy on all six benchmarks we evaluate, with the largest gains on reasoning and exact-answer tasks.

---


### 180. [Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2607.04470)

**<font color=#1a73e8>作者：</font>** Faid Keddouri, Sohaib Houhou, Aissa Boulmerka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) offer a natural interface for translating human objectives into reward signals for cooperative multi-agent reinforcement learning (MARL), yet the training-time dynamics of this integration remain poorly understood. We show that dynamically updating LLM-generated reward weights during off-policy MARL violates the stationarity assumption of Potential-Based Reward Shaping (PBRS) and contaminates the experience replay buffer, whose stored transitions carry reward labels computed under stale shaping weights. We characterise the result as a regime-dependent failure whose severity depends on how competent the unshaped baseline already is. To control it we propose two stabilisation strategies: a Phase-Based Freeze Schedule that enforces strict stationarity within training phases, and Exponential Moving Average (EMA) smoothing that bounds per-episode weight drift. We evaluate across three cooperative environments and five random seeds with QMIX, complemented by an exploratory VDN extension, yielding a three-regime taxonomy. In the augmentative regime (Simple Spread), where the baseline is functional (74.4 %), EMA significantly improves success to 86.7 % ($+12.3$ pp, $p<0.01$) while naive dynamic updates collapse it to 15.2 %. In the essential regime (Level-Based Foraging), where the baseline is broken (0.1 %), any shaping unlocks the task (95.9 % under EMA). In the supplementary regime (SMAC 3m), where the baseline is near-saturated (98.8 %), stabilised shaping preserves performance (99.9 %) while unstabilised shaping adds variance without gain. These findings establish reward-signal stationarity as a necessary design constraint and indicate that regime placement is a practical predictor of whether dynamic LLM shaping helps or harms.

---


### 181. [EVAS: Efficient Multimodal Temporal Forgery Localization via Audio-Visual Synergy and Steered Boundary Calibration](https://arxiv.org/abs/2607.04472)

**<font color=#1a73e8>作者：</font>** Shen Shen, Quan Zhang, Dan Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of artificial intelligence-generated content necessitates reliable multimodal forensics. Beyond video-level binary classification, precisely localizing sparsely distributed forged segments in long-form videos remains a critical challenge. This task is particularly difficult when manipulations are subtly embedded and cross-modal signals are weak and temporally diffuse. To address these challenges, we propose EVAS, an end-to-end multimodal framework for temporal forgery localization. At its core, a Multi-Stage Audio-Visual Synergy mechanism facilitates progressive cross-modal interaction to learn deep multimodal forensic representations and capture high-order semantic traces of sparse manipulations. Furthermore, we introduce a Boundary-Aware Refinement strategy to achieve steered boundary calibration. By incorporating invalid-frame masking, this strategy suppresses ambiguous regions and sharpens transition predictions. We adopt a decoupled training paradigm with auxiliary heads to disentangle representation learning from inference objectives, enhancing model generalization and stability. Additionally, a lightweight HourglassFFN is incorporated to reduce computational overhead. Extensive experiments demonstrate that EVAS achieves state-of-the-art average localization accuracy and average recall across three benchmark datasets, validating its effectiveness for fine-grained temporal forgery localization.

---


### 182. [TrustCLIP: Learning Private Visual Features via Adversarial Reconstruction](https://arxiv.org/abs/2607.04484)

**<font color=#1a73e8>作者：</font>** Nikos Athanasiou, Ilya A. Petrov, Angela Yao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision and vision-language models rely on high-level visual representations that are increasingly used across recognition, retrieval, and multimodal reasoning pipelines. However, recent advances in generative modeling have shown that such features can often be inverted, enabling realistic reconstructions of the underlying image and raising significant privacy risks. We revisit this problem through the lens of reconstruction and propose TrustCLIP, a reconstruction-driven framework that treats a feature-conditioned generator as an explicit privacy adversary. TrustCLIP learns a projection between encoder features and downstream modules that is explicitly optimized to degrade the reconstructions produced by generative attackers while retaining the necessary signals for downstream tasks. Unlike prior defenses that rely on discriminative privacy metrics, TrustCLIP directly optimizes against a generative reconstruction attacker, targeting a threat not captured by standard evaluation protocols. We demonstrate its effectiveness in both conventional classification and multimodal large language model pipelines. Across these settings, TrustCLIP consistently reduces the fidelity of generative inversions while maintaining downstream task performance. Project page: this https URL

---


### 183. [Geographic Diversity Beats Data Volume for Cross-Domain Generalization in Zero-Label JEPA Driving World Models](https://arxiv.org/abs/2607.04500)

**<font color=#1a73e8>作者：</font>** Santosh Jaiswal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised latent world models can assign a surprise score to driving scenarios without any human labels. A natural follow-up question is whether such a model, trained on driving data from one geographic region, can generalize its notion of complexity to unseen cities and sensor configurations. We study this question through a controlled transfer experiment: we train JEPA-based world models on nuPlan data (Pittsburgh, Boston, Singapore) and evaluate zero-shot on held-out Argoverse 2 validation scenarios from Miami and Austin. We find that models trained on geographically diverse data generalize significantly better than models trained on equal amounts of single-geography data. In a matched-scale ablation at 63,000 scenarios per condition (n=3 seeds each), combined training reduces mean surprise score by 16.5% relative to nuPlan-only training (0.228 +/- 0.015 vs 0.273 +/- 0.008). Notably, training on 200,000 AV2-only scenarios (3x more data from one geography) still produces higher surprise (0.264) than the combined 63K model, suggesting that geographic diversity is a stronger predictor of cross-domain generalization than raw data volume.

---


### 184. [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discovery](https://arxiv.org/abs/2607.04508)

**<font color=#1a73e8>作者：</font>** Kyunghoon Hur, Chihun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI-for-Science can automate ideation, planning, and analysis, but final validation still depends on real experiments. A self-driving lab (SDL) can execute those experiments, yet the loop still has bottlenecks: the agent may spend too many rounds on low-value experiments, or each round may require a high-cost experiment. We target these two physical bottlenecks with one agent. First, a prior-aware agentic DOE loop uses domain knowledge and past results to propose feasible and informative next experiments, reducing trials-to-target. Second, a cost-aware surrogate agent predicts high-cost, high-resolution measurements from low-cost, low-resolution measurements. It chooses between a high- and a low-cost measurement based on the predicted uncertainty. We examine these directions in the biology and materials domains, respectively. Together, under a single agent, these components aim to accelerate the SDL loop by reducing both the number of loops and the cost per experiment.

---


### 185. [Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5](https://arxiv.org/abs/2607.04510)

**<font color=#1a73e8>作者：</font>** Lyndon Drake, Zandi Eberstadt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM) -- the broad misbehaviour a language model acquires after fine-tuning on narrow harmful data -- is mediated in Qwen2.5 models by a latent persona direction, and that direction is causal in open weights. Transplanting it into a model that shares only pretraining with its source induces broad EM (2.83 +/- 0.26% misaligned against a random-direction floor of ~1.1%), and ablating a model's own direction roughly halves an overt inducer's broadcast (21% to 10%). The transplant doubles as a measurement method, causally assaying directions that a source model represents but cannot itself express. Whether a fine-tune recruits this persona depends on method and capacity, and since low-rank PEFT is the cheaper regime at scale, the recruiting method is also the economical one. On Qwen2.5-32B, low-rank LoRA on insecure code recruits it (3.4% misaligned) while full SFT on identical data does not (0.3%) and moves against the persona axis (drift-persona cosine +0.17 at rank 1 to -0.10), the far-inducer, high-capacity exception consistent with a representational-distance x capacity account. The persona's causal role is itself conditional. Steering a bad-medical SFT run away from the direction during training raises the broadcast from 24% to 51% while a matched random control lowers it, so removing the direction is no blanket recipe. Because recruitment is a loss-reducing shortcut that capacity renders redundant, it can be screened for and prevented in the tested instances. Persona loss-relevance at the SFT solution orders four inducers' broadcasts rank-perfectly within Qwen2.5, inoculation removes recruitment selectively (4.75% to 0.0%, code coherence 65% to 87%), and fine-tuning orthogonal to the single behaviour-derived axis reduces it persona-specifically. Results are a controlled case study of one model family, single-seed in places.

---


### 186. [Language Models Represent and Transform Concepts with Shared Geometry](https://arxiv.org/abs/2607.04525)

**<font color=#1a73e8>作者：</font>** Zhimin Hu, Lanhao Niu, Sashank Varma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How concepts are represented in neural networks is a fundamental question in machine learning. The dominant view treats concept representations as stationary geometric objects. Yet concepts appear in context, and context transforms them. Drawing from neural population geometry, we formalize concept representations as point-cloud manifolds and contextual transformations as vector fields, and instantiate this framework in large language models. Across six model families of varying scales, we find that context moves each concept differently. The variance in these displacements is semantically organized, correlating with lexical concreteness and density. Importantly, both the concepts being transformed and this variance structure are shared across models: displacement structure transported from one model predicts held-out displacements in others significantly above chance. Together, these findings show that models share a common geometry not only in how concepts are represented, but more importantly in how context transforms them, a structure with richer organization than prior work has recognized.

---


### 187. [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528)

**<font color=#1a73e8>作者：</font>** Haiwen Yi, Xinyuan Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Software-agent benchmarks usually report whether an agent solves a task, but the agent reaches that outcome through a harness that controls what it sees, which actions it can take, which failures are repaired, which states are verified, and which evidence is logged. We show that this harness can change the agent's multi-step beliefs even when the task, environment, and base LLM are fixed. We introduce a belief-rollout diagnostic that elicits structured K-step trajectories over progress, risk, recoverability, constraints, failure mode, uncertainty, future success, repair cost, and next action under alternative harnesses. We define a cross-harness belief divergence and decompose it into an arrival term for immediate interface shifts and a growth term for horizon-dependent belief changes. On controlled coding tasks and public-benchmark stress tests, blocked actions, compressed repairs, selective verification, and cost-aware evidence pruning often preserve terminal success while changing the beliefs that drive later decisions. We further introduce BIWM, a no-training protocol that canonicalizes observations, logs censored branches, expands repair traces, records verification masks, executes risky branches in shadow, and aligns belief trajectories across harness views. The results suggest that harness design is an experimental variable in agent evaluation, not an implementation detail. Our code is available at this https URL.

---


### 188. [Mechanism-level routing failure in LLMs over Lean-verified algebraic structures](https://arxiv.org/abs/2607.04534)

**<font color=#1a73e8>作者：</font>** Manuel Israel Cázares, Wenlin Zhang, Haobo Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an empirical study of structural routing failure in large language models (LLMs) over a formally verified algebraic corpus. The task requires selecting the correct proof-mechanism label from a fixed closed template set for compact mathematical objects drawn from the FiberRing formalization in Lean 4, where each item is anchored to a Lean-verified artifact and assigned a label from the corresponding certificate family.
Our central finding is a mechanism-level routing ceiling: under blind conditions, gpt-oss-120b achieves 80.3% template accuracy on 22 FiberRing items (n=66; temperature=0, seed=0), while Llama 3.3 70B reaches 68.2%. Exposing a mechanism-bearing Lean verdict/witness cue (Condition A2) raises accuracy to 90.9% and 81.8% -- gaps of +10.6 and +13.6 pp termed cue-induced routing uplift.
The dominant failure is a CRT-to-ring-equivalence misroute: gpt-oss-120b misroutes 7 of 12 CRT items (58.3%) blind, zero under A2. A cross-model dissociation in Llama is notable: verdict accuracy is identical in both conditions (95.5%), while template accuracy improves 13.6 pp -- confirming that truth inference and proof-mechanism classification are separable capacities.
A cross-corpus extension (Set B; 6 POM/CollisionKernel items, 72 evaluations) provides a small cross-module check: CRT-granularity compression reappears with different labels, and an inverse cross-model dissociation emerges. These findings extend the router hypothesis (Cazares 2026) to formal algebraic structures. The full pipeline, manifest, and results are at this https URL.

---


### 189. [EEG-SpikeAgent: Agentic Closed-Loop Program Synthesis for Automated EEG Spike Detection](https://arxiv.org/abs/2607.04558)

**<font color=#1a73e8>作者：</font>** Sonali Santhosh, Kelly Shuhong Yu, Eugene Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated detection of interictal epileptiform discharges in scalp electroencephalography (EEG) is clinically important, but recent high-performing deep-learning models often trade interpretability for accuracy. We introduce EEG-SpikeAgent, a closed-loop program-synthesis framework that uses a large language model (LLM) agentic system to generate signal-processing features for spike detection in scalp EEG. The system iteratively proposes one deterministic EEG feature module at a time, executes the resulting code on EEG to generate tabular features, evaluates performance via a tabular classifier, summarizes run-level metrics, and feeds structured diagnostics back to the model for refinement. Across iterations, EEG-SpikeAgent proposes and refines candidate signal features and decision rules informed by model performance. We evaluated EEG-SpikeAgent on VEPISET, a public 29-channel dataset of 4-second epochs containing 2,516 discharge-containing and 22,933 non-discharge epochs. Across five-fold cross-validation with a gradient-boosted tree classifier, agent-generated features achieved an area under the receiver operating characteristic curve of 0.935, balanced accuracy of 0.699, F1 score of 0.557, sensitivity of 0.401, and specificity of 0.996 at the default operating point. At an operating point with sensitivity 0.80, mean precision was 0.470 and mean specificity was 0.900. Artifact-aware feature generation improved balanced accuracy and F1 score over spike-only feature search. These results indicate that LLM-based program synthesis can automate EEG feature engineering in auditable and inspectable code-driven manner for clinical and methodological review.

---


### 190. [QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding](https://arxiv.org/abs/2607.04559)

**<font color=#1a73e8>作者：</font>** Wei Ao, Lan Wang, Vishnu Naresh Boddeti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of vision-language models (VLMs) in video understanding declines with increasing video duration, as video moments unrelated to the query confuse their language components. Multimodal retrieval has emerged as a critical component of video understanding, addressing this challenge by localizing key visual evidence. However, existing multimodal retrieval methods suffer from biased relevance estimation, limited diversity, and temporal collapse. In this paper, we propose QSVideo, a unified framework that systematically addresses relevance, diversity, and temporal modeling in video retrieval. We first introduce a query-conditioned semantic ranker, QSRanker, which reformulates arbitrary questions into retrieval-friendly queries and estimates structured relevance along object, action, and location dimensions. Building upon this, we design QSRetrieval to jointly optimize relevance and diversity for more informative frame selection. Moreover, we propose temporal alignment strategies tailored for both long and streaming videos to improve evidence recall. Extensive experiments on long and streaming video benchmarks demonstrate that QSVideo greatly enhances video VLM performance under strict frame limit constraints. The code is available at this https URL.

---


### 191. [Heaviside Continuity of Rolling Coefficients for Eliminating Epistemic Entropy in Large Language Models](https://arxiv.org/abs/2607.04562)

**<font color=#1a73e8>作者：</font>** MY Pitsane, Hope Mogale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) generate fluent outputs that can be wrong. Unlike humans, who often exhibit cues when providing false information, LLMs produce errors that are difficult to detect because autoregressive decoding provides no mechanism for verifying intermediate reasoning before state progression. We introduce Heaviside Continuity of Rolling Coefficients (HCRC), a verification-first execution framework that reformulates inference as predicate-gated state transitions governed by a Heaviside Gate. HCRC combines model confidence with independent verification signals from a parallel worker architecture, allowing execution to advance only when predefined correctness predicates are satisfied. This prevents invalid intermediate states from propagating, reducing epistemic entropy without modifying the underlying model. We evaluate HCRC on software-engineering and reasoning tasks across thirteen proposers from four providers. On capable proposers, the gate reduces the false-completion rate (FCR) from 4--7% to 0% while remaining latency-competitive and, in some settings, faster than the unwrapped model. On weaker proposers, it converts false completions into honest halts instead of corrupting downstream state. Beyond benchmarking, HCRC has operated for months as the production control plane of an agentic coding environment, authorizing file mutations, verification-driven progress reporting, and memory compaction. These results establish HCRC as a general framework for verification-driven LLM execution, showing that reliable reasoning can be achieved through principled execution control rather than model scale alone.

---


### 192. [Detecting Answer-Driven Reasoning in LLM-Based Educational Tutors via Truncated Chain-of-Thought Auditing](https://arxiv.org/abs/2607.04572)

**<font color=#1a73e8>作者：</font>** Bonan Shen, Dingyan Shang, Youting Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) tutors often produce fluent step-by-step explanations, but a correct and pedagogically formatted response does not guarantee that the answer was derived from the student-facing problem. In realistic tutoring systems, the model may also have access to teacher notes, answer keys, rubrics, or retrieved solution artifacts. We study whether such private answer information can make tutor explanations answer-driven: the final answer is behaviorally available before the written explanation has justified it. Using Truncated Reasoning AUC Evaluation (TRACE), which probes how early a chain-of-thought prefix can pass a verifier, we evaluate 1000 GSM8K test problems under three paired tutoring contexts: question-only, correct answer-key, and wrong answer-key. At fixed fractions of each generated explanation, we force the model to answer immediately and verify the response against the gold numeric answer. With Qwen2.5-3B-Instruct, answer-key access raises median TRACE AUC from 0.375 to 0.900 and makes the gold answer available at the first 10% prefix in 997 of 1000 cases. The effect remains strong on the 746 examples where both question-only and answer-key explanations end with the correct answer. These results support truncated CoT auditing as a lightweight process-level diagnostic for answer-driven reasoning in math tutoring explanations.

---


### 193. [A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training](https://arxiv.org/abs/2607.04574)

**<font color=#1a73e8>作者：</font>** Junze Ye, Jiayi Cheng, Miao Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For LLM agents, supervised fine-tuning is not only about teacher labels' quality, but also about which interaction contexts those labels condition on. Pure behavioral cloning uses full teacher demonstrations, creating a mismatch between teacher-induced contexts seen in training and student-induced contexts encountered at test time. Recent work addresses this mismatch by querying a teacher at contexts reached by the student, often with increasingly elaborate filtering of the teacher's continuations. We instead frame on-policy data construction as a budget-allocation problem: under matched supervision resources, should teacher output be spent on more start-to-finish demos, longer continuations, outcome filtering, or broader coverage of learner-induced contexts? We formalize this design space through the rollout policy, switch-time distribution, continuation horizon, filtering rules, and two complementary costs: teacher inference generated before filtering and teacher supervision retained for SFT. Across HotpotQA, ALFWorld, and Terminal-Bench-Dev, bounded unfiltered teacher continuations at learner-induced contexts improve over pure behavioral cloning at matched budgets. On HotpotQA and ALFWorld, where we run the full comparison, few-step continuations match or exceed success-filtered and critical-context-filtered alternatives. Our findings suggest that a few teacher steps, placed at learner-induced contexts, can be a more cost-efficient supervision allocation than longer or more heavily curated teacher completions.

---


### 194. [Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation](https://arxiv.org/abs/2607.04576)

**<font color=#1a73e8>作者：</font>** Theodore O. Cochran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly answer questions against knowledge bases they help maintain. A common intuition holds that progressive disclosure, a compact catalog plus a one-line summary per page so the agent loads only what it needs, should make this cheaper than consulting a large monolithic index. We test that on a real 709-page markdown wiki maintained by an LLM. We retrofit it for progressive disclosure and run a preregistered ablation in which four versions of the corpus differ only in how the agent reaches the content: page bodies are byte-identical across arms, frozen as immutable git tags, so any measured difference is due to access structure alone. We cross the arms with three access conditions (a protocol-constrained agent, a free self-routing agent, and a catalog-preload regime) and grade answers blind against verified gold references with a cross-family judge.
A pilot upended the premise: a capable tool-using agent never loads the index, inferring a page's path from the question and reading it directly, so the specific saving the retrofit targets does not materialize. We therefore made answer quality primary and cost secondary. Quality is non-inferior (the retrieval arm matches the index baseline within the preregistered margin) while cost falls in every regime, from about a third for a self-routing agent to well over half under catalog-preload, all confidence intervals excluding zero. The saving comes not from avoiding the index load but from more targeted access: the retrieval arm cites fewer pages and takes fewer tool turns. The study doubles as a case study in evaluation validity, applying threat-to-validity discipline to the tooling that produced it.

---


### 195. [TORINO: Token Reduction via Interpretable Concept Overlap in Vision-Language Models](https://arxiv.org/abs/2607.04593)

**<font color=#1a73e8>作者：</font>** Riccardo Renzulli, Gabriele Spadaro, Shruthi Gowda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated impressive capabilities across different tasks, but their computational cost is dominated by the large number of visual tokens fed to the language model. Existing token reduction methods rely on attention-based scores or pairwise similarity, without an explicit semantic representation of each token. We introduce TORINO (TOken Reduction via Interpretable coNcept Overlap), a plug-and-play framework for adaptive visual token reduction in VLMs that requires no fine-tuning of the underlying model. TORINO leverages Sparse Autoencoders (SAEs) to project visual tokens into an interpretable latent space where token relationships can be analyzed through shared concept activations. Specifically, we define concept overlap as the degree of agreement between active SAE latents and use it to group tokens that share semantic content. Reduction within each group is then performed by either pruning or merging, providing a unified framework that preserves semantically important visual information while removing redundancy. Unlike fixed-budget approaches, TORINO dynamically adapts the reduction rate to input complexity, allowing different images to retain different numbers of tokens. Experiments across multiple vision-language benchmarks show that TORINO achieves favorable efficiency-accuracy trade-offs, reducing the number of visual tokens with minimal performance loss.

---


### 196. [Enhancing Large Multimodal Models in Key Information Extraction via Scene-Aware Document Synthesis](https://arxiv.org/abs/2607.04636)

**<font color=#1a73e8>作者：</font>** Zhipeng Xu, Zulong Chen, Qing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Key Information Extraction (KIE) converts visually rich documents into structured data, but practical deployment remains challenging: strong performance often relies on costly on-server Large Multimodal Models (LMMs), while compact locally deployable models lack sufficient KIE supervision. We present SAYRE, a scene-aware document synthesis framework for generating scalable KIE training data without hand-crafted template design. Given a few exemplar documents, SAYRE captures category-specific content patterns and layout conventions to synthesize document-schema-annotation triples. It further introduces error-driven generation, which expands real-world failure cases into hard training examples while preserving their structural patterns. Experiments on constrained- and open-category KIE show that SAYRE consistently improves Qwen3-VL backbones and achieves the strongest overall performance among on-device LMMs. Data scaling experiments show an overall upward trend as more synthesized data is introduced, especially for smaller models and open-category extraction. Error analysis further shows that synthesized training reduces field-level errors by improving schema-aware extraction over dense tables, business identifiers, and contract clauses. These results establish scene-aware synthesis as an effective data-centric approach for improving practical multimodal KIE.

---


### 197. [Wrong Before Right: Late Rescue and Interface Failure in Aligned Language Models](https://arxiv.org/abs/2607.04640)

**<font color=#1a73e8>作者：</font>** Jiaqi Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how correctness is assembled inside aligned language models, not only whether the final answer is right. Using layer-wise difference-in-differences (DiD) trajectories over polarity-controlled minimal pairs, we identify the wrong-dip: in mid layers (25-90% depth), internal preference transiently commits to the incorrect answer and is rescued only by late-layer correction. We verify this causally with patchscope-style activation transplantation across 17 models, three families, and 64x scale (0.5B-32B). Four findings follow. (1) Alignment amplification of the causal wrong-dip is recipe-specific and emergent: it emerges at 3B in Qwen2.5, remains high, and peaks at 32B (paired t up to 9.7), reverses in Llama-3-8B (t=-2.31), and sits between for Mistral-7B. (2) The dip predicts real compression failures: high-dip items are 3-7x more likely to flip under late-layer low-rank compression, block dropping, or structured pruning, while quantization flips are dip-blind, a double dissociation confirmed by late-layer ablation. (3) The dip is trainable: a LoRA fine-tune with a mid-layer wrong-margin penalty matches output-only SFT accuracy while cutting the causal dip by 67-70% and improving compression robustness; output-only SFT worsens the causal dip by up to 2.8x at perfect surface accuracy. (4) With controlled readouts, the phenomenon survives natural-language I/O: dip stratification of structural-damage failures is significant on naturalistic vignettes, and free-form fragility separates into a dip-auditable late-rescue layer and a dip-blind interface layer. Together, output-level correctness can hide a late-rescue process that governs compression risk, post-training quality, and evaluation distortion.

---


### 198. [Retroactive Chain-of-Thought (RetroCoT): Forensic Reconstruction Prompts as a Safety Diagnostic Across Model Generations](https://arxiv.org/abs/2607.04645)

**<font color=#1a73e8>作者：</font>** Samira Hajizadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models is typically evaluated against direct, imperative harmful requests. We show that this alignment is highly conditioned on pragmatic register: models that refuse a direct request frequently comply when the same underlying objective is expressed through a different communicative stance. This suggests that current alignment policies are not invariant to semantic equivalence, but remain sensitive to how a request is pragmatically framed. We introduce Retroactive Chain-of-Thought (RetroCoT), a single-turn attack that reframes harmful requests as forensic reconstruction tasks. Rather than requesting harmful instructions directly, RetroCoT presupposes that the harmful outcome has already occurred and asks the model, acting as a forensic analyst, to reconstruct in reverse the causal chain that produced it. On AdvBench (n=50), RetroCoT achieves attach success rate of 58% on gpt-4o and 52% on gpt-4o-mini, compared with direct-request baselines of 0% and 4%, respectively. We further identify a pronounced generation gap: GPT-5-family models refuse RetroCoT entirely, explicitly identifying the reconstruction premise in their refusal rationales, consistent with explicit coverage of this reconstruction register. However, this robustness does not generalize across pragmatic forms. A single adversarial feedback turn presenting an existing forensic reconstruction response alongside evaluator critique raises ASR from 0% to 48% on GPT-5.4-mini and from 58% to 94% on GPT-4o; a control condition omitting the fabricated low score achieves 85% on GPT-5.4-mini, indicating that the operative element is pragmatic continuation within the established forensic frame rather than score manipulation. These results suggest that frontier-model alignment remains conditioned on pragmatic framing rather than semantic intent, and that new pragmatic registers can continue to expose a...

---


### 199. [DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2607.04665)

**<font color=#1a73e8>作者：</font>** Gwang-Ho Na, Ho-Joong Kim, Seong-Whan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image from a multimodal query consisting of a reference image and an edit text describing the desired modification. Recent ZS-CIR studies have relied on projection-based methods that map a reference image into pseudo-word tokens in the text embedding space. However, such methods require additional projection and re-encoding steps, increasing training complexity, reducing efficiency, and introducing a discrepancy between training and inference. In this paper, we propose DiCE-CIR, a direct composition learning method that predicts composed query representations by directly composing a reference image and an edit text. To enable scalable training without manually annotated triplets, we automatically construct compositional training samples from large-scale image-caption pairs using a large language model. Based on these samples, we train a lightweight composition module with objectives that promote alignment with the target, edit-consistent semantic transformation, and retrieval discriminability. We conduct extensive experiments on ZS-CIR benchmarks and show that DiCE-CIR achieves state-of-the-art performance on CIRCO and competitive performance on CIRR while maintaining high computational efficiency.

---


### 200. [Does It Fail to See or Fail to Know? Attributing Errors in Vision-Language Models](https://arxiv.org/abs/2607.04683)

**<font color=#1a73e8>作者：</font>** Khang Nhat Hoang Vo, Artem Vazhentsev, Artem Shelmanov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) perform well on visual question answering with high-quality images but struggle when questions require knowledge beyond what is clearly and directly visible. In such settings, uncertainty quantification should not only indicate whether the model is likely to fail but also diagnose why it is uncertain, across dimensions such as perception, entity recognition, and knowledge retrieval. While prior work has focused on individual failure modes in isolation or treated incorrect answers as monolithic failures, we propose a unified framework for disentangling these failure modes and investigate whether pre-generation signals can predict these failure sources. Across a range of datasets and model families, we find a consistent pattern in VLM errors: some failures arise from visual or recognition bottlenecks, while others persist after the relevant entity is identified. Our main finding is that these failure sources can be predicted before decoding: recognition-related failures are best captured by visual-token representations, while failures that remain after recognition are better captured by prompt-conditioned hidden states. This pre-generation signal enables efficient failure-source prediction before the model produces an answer, allowing uncertain cases to be routed to targeted interventions such as image repair, entity recognition support, or external retrieval.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
