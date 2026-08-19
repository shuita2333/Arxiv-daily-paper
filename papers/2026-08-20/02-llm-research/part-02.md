# 🧠 大模型相关研究 | 2026年08月20日

> 本类共 **161** 篇论文：已确认 **151** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-161](./part-04.md)

---

### 51. [SignalReasoner: Assessing the Upper Bound of 3B Models for Signal Mathematical Reasoning](https://arxiv.org/abs/2608.17301)

**<font color=#1a73e8>作者：</font>** Guozheng Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training with supervised chain-of-thought fine-tuning and reinforcement learning from verifiable rewards has substantially improved the mathematical reasoning capabilities of large language models (LLMs). However, their application to signal processing problems remains relatively under-explored. This report investigates reinforcement fine-tuning strategies for adapting Qwen2.5-3B-Base to graduate-level signal mathematical problems from WirelessMATHBench-XL, a comprehensive benchmark for mathematical reasoning in this domain. We examine two training paradigms: (i) direct reinforcement learning (RL) on WirelessMATHBench-XL with verifiable rewards; and (ii) supervised fine-tuning (SFT) on a distilled wireless-domain chain-of-thought corpus, followed by the same domain-specific RL stage. Across both paradigms, we benchmark Group Relative Policy Optimization (GRPO), Group Sequence Policy Optimization (GSPO), and Geometric-Mean Policy Optimization (GMPO). We aim to assess whether domain-aware CoT SFT serves as an effective initialization for subsequent RL, and whether GSPO or GMPO offer advantages in stability or accuracy over GRPO for signal reasoning tasks. Our best model achieves an overall accuracy of 39.12\%, representing a more than threefold improvement over the untrained Base model (12.37\%).

---


### 52. [Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models](https://arxiv.org/abs/2608.17306)

**<font color=#1a73e8>作者：</font>** Yang Chen, Zhan Zhuang, Yanbin Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While adversarial prompt tuning can enhance robustness of vision-language models efficiently, we find that existing methods aggravate robust generalization overfitting on seen classes, leading to a rapid degradation in performance against adversarial examples of unseen classes as training progresses. We empirically identify that this degradation stems from the tendency of the model to learn pseudo-robust features (i.e., non-generalizable shortcuts). To mitigate this, we propose ADAPT (Adversarial Disentangled Prompt Tuning), a robust prompt tuning framework following the philosophy of ``Learning What Not to Learn''. Specifically, ADAPT uses a dual-prompt mechanism with a target prompt and a pool of decoy prompts. During training, the decoy prompts are guided to entrap diverse pseudo-robust features, while the target prompt is constrained to be orthogonal to the decoys in the embedding space to learn robust features. By disentangling the robust features from the pseudo-robust features, ADAPT effectively prevents robust generalization overfitting. We further provide an analysis showing that the orthogonal loss bounds the effect of shifts in pseudo-robust features on unseen classes, yielding a testing error guarantee. Empirically, extensive experiments demonstrate that ADAPT substantially improves the robustness of the target prompt on unseen classes. The code is available at this https URL.

---


### 53. [Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements](https://arxiv.org/abs/2608.17310)

**<font color=#1a73e8>作者：</font>** Zhi Zheng, Rongsheng Chen, Yunpeng Ba 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder. This paper argues that evolution strategies (ES) can be a better choice for fine-tuning long-horizon LLM agents. Compared with agentic RL, ES offers three key advantages: 1) Model Scalability: ES enables full-parameter optimization with only minimal, inference-level GPU memory, making it possible to fine-tune large LLMs. 2) Flexibility: its lightweight, black-box feedback interface makes ES fine-tuning easy to compose with prompt-space evolution (e.g., skill optimization & test-time compute); and 3) Long-Horizon Scalability: ES performs trajectory-level parameter attribution without decomposing rewards across horizons, yielding better scalability than Agentic RL as the horizon length grows. Based on this insight, we propose Agentic ESOpt, a full-parameter agentic fine-tuning framework tailored to flexible parameter--context co-evolution. At each step, Agentic ESOpt samples perturbations around the current LLM parameters, evaluates the resulting agents with rewards, and applies an online reward-weighted update. To improve the exploration--adaptation trade-off, Agentic ESOpt further introduces a cosine decay schedule of the perturbation scale $\sigma$. On WebArena-Lite, full-parameter optimization of Qwen-3.5-27B improves the No Skill baseline by 6.69%. In test-time automatic heuristic design, Agentic ESOpt performs online prompt--parameter co-evolution, improving its matched baseline in 28 of 36 settings.

---


### 54. [Procedural Collapse: A Structural Account of Disengagement in LLM-Assisted Writing](https://arxiv.org/abs/2608.17326)

**<font color=#1a73e8>作者：</font>** JaeWon Kim, Katelyn Mei  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When students use large language models for writing, the dominant explanation for disengagement is dispositional: they are over-reliant, and the remedy is to scaffold self-regulation. We argue that a structural explanation is needed, offering an alternative basis for design interventions to support appropriate AI-assisted writing. Current LLM writing interfaces induce procedural collapse: the replacement of an iterative, self-paced writing process with a single output that shifts the writer's task from generation to comprehensive evaluation. Because that evaluation is costly, shallow engagement becomes the default, and the cognitive work writing was supposed to produce goes unperformed. The framework points toward design directions that reduce the burden on writers to self-regulate, including decomposed interaction, goal elicitation as a default first step, and single-level output. They complement metacognitive scaffolding by restructuring the interaction itself.

---


### 55. [MS-MFAD : Multimodal large language models for Face Anti-spoofing Detection](https://arxiv.org/abs/2608.17328)

**<font color=#1a73e8>作者：</font>** Xiaoyong Yu, Rongzhen Li, Shuming Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial biometric recognition systems currently face compound threats intertwining generative AI and high-fidelity physical spoofing. Existing defenses suffer from systemic bottlenecks, including poor generalization, non-auditable reasoning, and reliance on massive, low-quality datasets. To address these challenges, we propose Multimodal Large Language Models (MFAD) for face anti-spoofing detection, an explainable reasoning system for Unified Face Anti-Spoofing Detection (UFAD), accompanied by a semantic-level annotation benchmark. Unlike methods relying on external tools or coarse alignment, MFAD activates the intrinsic reasoning capabilities of Multimodal Large Language Models (MLLMs) via a fine-grained pixel-semantic anchoring mechanism. This eliminates localization hallucinations and ensures auditable reasoning paths. We introduce a cross-attack semantic-level unified annotation paradigm: by annotating only 1,000 precise masks per attack category, we generate reasoning evidence chains strictly corresponding to spoofed regions. Supervised fine-tuning on the Qwen-VL foundation model demonstrates that, using limited high-quality samples, the system achieves a 40-50% relative reduction in in-domain ACER and restricts cross-domain performance degradation to within 11.62%/5.23%, significantly outperforming existing frameworks. Furthermore, under white-box adversarial attacks, detection accuracy drops by only 3.2%, validating the robustness of semantic anchoring compared to models trained on massive short-text data. Domain practitioners rated the evidence reliability of reasoning paths at 4.57/5, with inference latency satisfying real-time deployment requirements. These results confirm that a few-shot, high-quality semantic annotation paradigm is effective for building trustworthy, explainable, and cost-efficient UFAD systems.

---


### 56. [LLMs for Medical Consultation Are Evaluated Too Late: The Preformulation Gap](https://arxiv.org/abs/2608.17330)

**<font color=#1a73e8>作者：</font>** Yining Hua, Cyrus Ayubcha, Hongbin Na 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models for medical consultation are often evaluated after a clinical problem has already been made clear, although real consultations may begin with a vague, minimized, or misframed concern. We evaluated three API models across four physician-authored, multi-turn vignettes under baseline and entry-to-care instruction conditions, yielding 24 fixed-script transcripts; two cases also used adaptive standardized-patient simulation, yielding 12 transcripts. Self-care or home-management advice before any patient answer appeared in 9 of 12 baseline case-model cells and 0 of 12 instruction cells, while structured handoff summaries appeared in 0 of 12 and 10 of 12 cells, respectively. The instruction changed sequencing and documentation, although it did not reliably ensure elicitation of decisive facts. The preformulation gap should therefore be evaluated directly through observable first-contact behavior rather than inferred from diagnostic accuracy or final-answer quality.

---


### 57. [TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration](https://arxiv.org/abs/2608.17336)

**<font color=#1a73e8>作者：</font>** Hanzhi Zhang, Qiao Zhang, Qinglei Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context prefill in large language models (LLMs) incurs substantial computation and memory traffic because dense self-attention computes quadratic query-key scores. Existing methods either use a uniform low-precision path or select token interactions, leaving spatial precision routing over hardware-aligned score tiles outside fused dense attention. We introduce TileMix, a tile-centric precision-routing kernel that makes numerical precision an executable spatial decision over score-tile groups within fused dense attention. TileMix partitions the attention matrix into hardware-aligned score tiles, packs routing decisions into compact bitmasks, and dispatches each tile group through FP16 or INT8 score computation while both paths update a shared online-softmax state. Scalable precision grouping lets each routing bit govern multiple adjacent key tiles, preserving hardware-aligned compute tiles and compact metadata at long contexts. By routing all legal tile groups, TileMix preserves dense token connectivity, requires no training, and supports grouped-query attention, variable-length batches, and INT8 key/value caches. Across LongEval, LV-Eval, and A100 prefill benchmarks on LLaMA, Qwen, and Vicuna, TileMix recovers long-context quality lost under uniform INT8 and improves prefill throughput over FP16, yielding a controllable accuracy-efficiency frontier across model families. The implementation is available at this https URL.

---


### 58. [LLM-Only PDDL Domain Repair with Open-Weight Models](https://arxiv.org/abs/2608.17341)

**<font color=#1a73e8>作者：</font>** Nader Karimi Bavandpour, Pascal Bercher  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI planning is concerned with finding a sequence of actions that achieves a specified goal. It relies on explicit models of the world, commonly represented in the Planning Domain Definition Language (PDDL). An active line of research investigates how errors in such models can be detected and repaired. For example, users may provide positive test plans that are solutions, and negative test plans that fail during execution. Automated repair methods then modify the PDDL model to satisfy these constraints. In this paper, we evaluate the ability of recent open-weight large language models to perform this repair task using an LLM-only approach. Our experiments show that the symbolic baseline achieves an $F_1$ score of $.49$, while the best-performing LLM reaches $.87$ with high reasoning effort, an absolute improvement of $.38$. However, that setting has a mean test pass rate of only $.82$, falling to $.06$ on the Thoughtful domain; even the best setting that includes the test traces reaches only $.92$. Thus, current open-weight models cannot guarantee satisfaction of the test constraints required for reliable automated model repair.

---


### 59. [MoFE: A Novel Mixture-of-Experts Framework with Fourier Neural Operators for Cryptocurrency Forecasting](https://arxiv.org/abs/2608.17342)

**<font color=#1a73e8>作者：</font>** Bowen Liu, Mingming Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting cryptocurrency prices remains a formidable challenge due to inherent non-stationarity, abrupt regime shifts, and multi-scale stochastic dependencies. Conventional deep learning models often struggle to capture complex underlying dynamics, frequently resulting in persistent phase-lagged predictions. To address these limitations, we propose MoFE, a novel deep learning framework that integrates Fourier Neural Operators (FNOs) within a Mixture-of-Experts (MoE) architecture. Rooted in the theoretical framework of stochastic differential equations, MoFE conceptualizes cryptocurrency volatility as a superposition of multi-frequency components, which includes user network based fundamental growth, mining costs and halving mechanism caused seasonal volatility, and market sentiment-induced chaos. Specifically, specialized adaptive FNO (AFNO) and Convolution dual-domain experts learn continuous function-to-function mappings to encapsulate global spectral trends, cyclical adjustments and microstructures, while a dynamic gating based MoE mechanism enables adaptive strategy switching across diverse market regimes. Extensive experiments on Bitcoin datasets spanning January 2020 to December 2025 demonstrate that MoFE achieves state-of-the-art (SOTA) performance in both T+1 and T+5 forecasting horizons. Notably, the model effectively mitigates the phase-lag effect, delivering superior Directional Accuracy (DA) and Information Coefficient (IC). In high-fidelity simulated trading environments, these predictive gains transfer into significant excess returns and robust risk-adjusted performance, characterized by a high Sharpe ratio.

---


### 60. [FlowShield: cryptocurrency anti-money laundering with transaction semantics parsing and fund flow tracking](https://arxiv.org/abs/2608.17355)

**<font color=#1a73e8>作者：</font>** Qishuang Fu, Andreas Deppeler, Joseph K. Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency anti-money laundering (Crypto AML) is increasingly challenged by sophisticated laundering behaviors that rapidly fragment stolen assets through diverse semantics and across multiple blockchains. Existing Crypto AML methods often simplify transaction semantics, rely on topology-centric signals, or output isolated detection labels. In this paper, we present \textsc{FlowShield}, a Crypto AML framework for transaction-level laundering detection and investigator-facing report generation. \textsc{FlowShield} first recovers behavior-level semantics from observable relations, making laundering intents explicit. To trace value provenance and redistribution, \textsc{FlowShield} reconstructs fund-flow subgraphs from three complementary perspectives. It then employs a text--structure fusion mechanism, enabling the interplay between large language model (LLM)-encoded semantics and flow texts with graph convolutional network (GCN)-encoded structure. Beyond mere detection, \textsc{FlowShield} further generates readable suspicious activity reports (SARs), offering investigators concise summaries and explainable red flags. To address the data scarcity in multi-chain detection, we construct and open-source \textit{BybitML}, the first public multi-chain laundering dataset. We evaluate \textsc{FlowShield} on \textit{BybitML} and two public laundering datasets and experimental results demonstrate that \textsc{FlowShield} achieves the best overall performance, with an average F1 score of 98.0\%. Further behavior and SAR analyses demonstrate that \textsc{FlowShield} can reveal diverse laundering strategies and produce readable reports for investigating complex multi-hop fund flows.

---


### 61. [ArguLens: An Open-Source System for Automated Essay Scoring and Label-Aware Feedback Generation](https://arxiv.org/abs/2608.17356)

**<font color=#1a73e8>作者：</font>** Weiran Wang, Hongxiang Shi, Huitao Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most automated essay scoring (AES) systems output a single holistic score without interpretable evidence and rely on closed APIs that introduce data privacy and cost barriers. We present ArguLens, an opensource, locally deployable system that decomposes AES into three decoupled components: a discourse-move classifier (Qwen2.5-7B-Instruct fine-tuned with LoRA on PERSUADE 2.0), a grade-independent LightGBM scorer over 31 linguistic and discourse features, and a label-aware feedback generator served through vLLM with a Qwen2.5-14BInstruct backbone. A Gradio web UI exposes pluggable inference backends and supports single-essay and batch scoring with downloadable per-essay breakdowns. On an essaydisjoint PERSUADE 2.0 test split, the logitprobe classifier achieves 82.6% accuracy and 0.727 macro-F1; under prompt-grouped 5-fold cross-validation the scorer reaches a mean QWK of 0.813 under an oracle discoursefeature protocol, and an ablation shows that adding gold discourse annotations yields an increment of +0.055 QWK over the lexical+syntactic configuration (paired t-test, p = 0.010). This is a component-level diagnostic rather than an end-to-end classifier-to-scorer result. The feedback generator ships with a structured evaluation protocol; its human-rater study is left to future work. The system is released under Apache 2.0 at this https URL.

---


### 62. [PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX](https://arxiv.org/abs/2608.17379)

**<font color=#1a73e8>作者：</font>** Genghan Zhang, Yixin Dong, Chengze Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce PTXBench, a benchmark for evaluating and adapting large language models (LLMs) to use architecture-specific PTX for GPU kernel optimization. PTXBench measures functional correctness, whether selected target instructions execute at runtime, and speedup over frontier libraries across GEMM and attention workloads on H100 and B200 GPUs. Our evaluation shows that architecture-specific PTX capability remains uneven: success rates fall substantially on complex attention backward workloads, and executing the target instructions does not necessarily translate into competitive performance. No evaluated model consistently matches frontier libraries across the suite. We further adapt Qwen3.6-27B using supervised fine-tuning. Repair-conditioned training improves several tasks, but generalization remains uneven; data coverage, balance, and the quality of the reasoning teacher matter in addition to dataset size. PTXBench provides an auditable testbed for measuring and improving LLMs' ability to exploit evolving GPU architectures.

---


### 63. [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](https://arxiv.org/abs/2608.17393)

**<font color=#1a73e8>作者：</font>** Yiming Du, Yuxin Jiang, Tao Yuan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates. To address this, we present LEGO-RL, a framework that bridges native coding-agent harnesses with scalable policy-gradient optimization without modifying their internal control flow. LEGO-RL is built upon three pillars: (1) faithful optimization via in-process LLM proxying that captures raw generation streams for token-level alignment and robust trainer-side log-probability recomputation, even under harness-side compaction or re-serialization; (2) reliable execution via scalable sandbox orchestration featuring image caching and stage-wise defenses to mitigate reward hacking; and (3) observable training through an integrated plugin that automates validation and monitoring, paired with a Live UI for granular trajectory diagnostics. We evaluate LEGO-RL by training the sparse MoE model Qwen3.5-35B-A3B with GSPO across three native coding-agent harnesses. LEGO-RL improves Qwen3.5-35B-A3B across OpenHands SDK (64.0% to 70.4%), Claude Code (62.4% to 68.2%), and OpenCode (57.2% to 66.6%) on SWE-bench Verified, while maintaining a rollout-training probability correlation above 0.99.

---


### 64. [An Investigation of Translationese in the Generations of Multilingual Large Language Models](https://arxiv.org/abs/2608.17399)

**<font color=#1a73e8>作者：</font>** Maria Valentini, Téa Wright, Julisa Granados 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text which has been translated from another language tends to carry with it evidence of translation$\unicode{x2014}$hence, it is often referred to as $\textit{translationese}$. Multilingual large language models (MLLMs) generate text in a variety of languages. However, it is still unclear if MLLMs' generations resemble internal translation (from English or, potentially, other languages) and, thus, result in translationese. Here, we ask the following research questions: (1) Does text generated by MLLMs resemble translationese? (2) How does translationese produced by MLLMs differ from translationese produced through direct translation? We leverage established indicators of translated text to evaluate text generated by state-of-the-art MLLMs in five languages, comparing to both non-translated and human-written baselines in order to isolate translationese from other kinds of interference. Through the use of high-accuracy classification models, analyses of variance on individual linguistic features, and the collection of human annotations in a subset of two languages (German and Spanish), we assess the translationese content of MLLM generations and examine the key features that distinguish MLLM-generated text from typical translation-related interference.

---


### 65. [MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding](https://arxiv.org/abs/2608.17402)

**<font color=#1a73e8>作者：</font>** Bonan Zhang, Shiyu Dong, Quan Hung Tran 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision encoders are a critical component of vision-language models, and scaling their capacity effectively improves performance. However, dense scaling increases compute cost and inference latency. Mixture-of-Experts (MoE) architectures offer a compelling alternative, having enabled efficient scaling in LLMs, yet the MoE design space for CLIP-style vision encoders remains underexplored at State-of-the-Art (SOTA) levels. In this work, we systematically study MoE designs for vision encoder scaling and find that fine-grained MoE topologies yield substantial gains over both dense and standard MoE counterparts. We further propose an auxiliary-loss-free balancing variant for better expert utilization, and design a specialized MoE kernel to mitigate inference latency overhead. To enhance video capabilities while preserving image knowledge, we introduce frame-level distillation paired with a novel freezing mechanism. We pretrain a series of Mixture-of-Experts Vision Encoders (MoE-ViE) across a range of sizes, all consistently outperforming their dense counterparts. Our largest model matches the zero-shot performance of a SOTA encoder 1.7x its size at 76% of its latency. When aligned with an LLM, MoE-ViE surpasses all compared encoders on image and video benchmarks, including those with up to 5x more activated parameters. Code is available at this https URL.

---


### 66. [GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models](https://arxiv.org/abs/2608.17411)

**<font color=#1a73e8>作者：</font>** Peizheng Guo, Jianqi Zhang, Xingyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the group gradients induced by different queries within the same mini-batch are directly averaged to form the policy update. However, these group gradients can point in conflicting directions. Our empirical analysis suggests that group-gradient conflicts tend to be associated with less effective policy updates, motivating the need for a reliable aggregated update direction under such conflicts. Standard GRPO aggregation treats the realized group gradients as deterministic contributions and does not account for differences in their reliability during aggregation. To address this issue, we propose Gradient Uncertainty-Aware Policy Optimization (GUPO), which models each group gradient as a random variable under a Bayesian formulation and estimates its probability distribution. GUPO then derives gradient uncertainty using a Dirichlet-based formulation and uses it to calibrate the contribution of each group gradient during aggregation. Extensive experiments on multiple benchmarks demonstrate the effectiveness of GUPO.

---


### 67. [REChart: Reasoning-Efficient Chart Editing with Large Reasoning Models](https://arxiv.org/abs/2608.17414)

**<font color=#1a73e8>作者：</font>** Yuanbang Liu, Chenxi Ruan, Yihan Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chart editing requires inferring and modifying visualization code from a reference chart image based on an editing instruction, challenging fine-grained visual reasoning, instruction following, and executable code synthesis capabilities of MLLMs. Large reasoning models (LRMs) with extended Chain-of-Thought (CoT) reasoning are suitable for tackling such complex multimodal tasks. However, our preliminary study reveals an ``inverted-U'' relationship between reasoning length and chart-editing performance: Excessive reasoning often leads to ``overthinking,'' where models drift toward hallucinated visual details or get stuck in redundant reasoning loops. To address the gap, we introduce REChart, a two-stage training framework that provides process-level supervision over intermediate reasoning steps, improving both editing fidelity and reasoning efficiency. First, we synthesize 200k high-quality reasoning trajectories for supervised fine-tuning from a large image-instruction-code pool, using a role-specialized agentic Reason-Score-Refine workflow that iteratively refine the chart code toward higher quality. Second, we optimize the model via reinforcement learning with two complementary rewards: a \emph{fidelity} reward evaluating code correctness, visual fidelity, and structural consistency, and an \emph{efficiency} reward that assigns each rollout a random thinking budget, truncates the reasoning process, and credits the final reasoning segment according to its contribution to the output. On the ChartEdit and ChartMIMIC benchmarks, our model achieves state-of-the-art chart-editing performance among open-source models of comparable scale, while mitigating overthinking and reducing average reasoning token usage by 79.0\% under a maximum thinking budget of 16,384 tokens compared with the base model.

---


### 68. [SemComp-Bench: Benchmarking Semantic Task Completion in Video Generation](https://arxiv.org/abs/2608.17426)

**<font color=#1a73e8>作者：</font>** Keyu Tu, Zhuowei Chen, Mengqi Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Semantic Task Completion Video Generation, an outcome-oriented video generation task. Under this formulation, success requires both achievement of the intended outcome and semantic grounding. Semantic grounding characterizes the correspondence between the reference image and the generated outcome in terms of high-level semantics relevant to the task. Evaluation focuses on the generated outcome and requires neither the presentation of a complete sequence of intermediate task steps nor conventional appearance consistency with the reference image. To support systematic evaluation, we construct SemComp-Data, an evaluation dataset covering six domains. Each instance comprises a reference image, a detailed instruction, a brief instruction, and an outcome-centric video clip. A scalable four-stage curation pipeline converts raw videos into standardized SemComp-Data instances. We further introduce SemComp-Bench, an evaluation protocol that uses a vision-language model (VLM) to answer structured binary questions. SemComp-Bench reports the OA Score and the GR Score for Outcome Achievement and Generation Reliability, respectively. Experiments on representative video generation models show that achieving intended outcomes while maintaining task-relevant semantic grounding in reference images remains challenging.

---


### 69. [Counterfactual Anatomy-guided Spatial-Temporal Decoding for Annotation-Free Hallucination Mitigation in Medical VLMs](https://arxiv.org/abs/2608.17427)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Adinath Dukre, Abhijit Das 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (Med-VLMs) have demonstrated strong performance on medical visual question answering, yet they remain prone to hallucination, generating clinically unsupported statements that are insufficiently grounded in image evidence. Mitigation methods applied during decoding offer a practical solution, but they typically lack anatomical awareness or rely heavily on ground truth annotations, which limits their applicability. We propose Counterfactual Anatomy-guided Spatial-Temporal decoding (CAST), a framework that operates entirely during inference and requires no manual annotations for anatomically grounded hallucination mitigation. CAST automatically discovers anatomical regions relevant to the given query through broad medical segmentation. It then selects a compact, causally informative area using counterfactual intervention based on the drop in answer likelihood under occlusion. Guided by this chosen region, CAST performs a unified contrastive decoding process, combining classifier-free guidance to correct spatial attention with stepwise temporal contrast to regulate generation dynamics. Experiments on the SLAKE and MIMIC-CXR datasets across three Med-VLMs demonstrate that CAST consistently outperforms strong baselines and surpasses decoding strategies reliant on ground truth. Our results indicate that compact, automatically selected regions provide highly effective contrastive guidance without expert annotations, offering a practical and generalizable solution for improving spatial grounding and reducing hallucinations. Code is available at this https URL.

---


### 70. [Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations](https://arxiv.org/abs/2608.17433)

**<font color=#1a73e8>作者：</font>** Liangtao Lin, Qingang Zhang, Zhaomeng Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have been widely adopted to operate mission-critical infrastructure (MCI). These agents normally rely on a harness that determines what information they can access, which tools they can use, and what actions they can take. Existing systems often expose the same comprehensive harness to every task, which may not be necessary and cause resource wastes. In this paper, we focus on the identification of optimal harness configurations, and view it as a resource-matching problem between what each task requires and what the harness provides. To measure this match, we classify MCI tasks based on the mathematical representation of the underlying system and rank harness configurations by the amount and type of information they provide. We then construct task-to-harness mappings from two sources: mining research literature and measuring controlled agent execution. Leveraging the measured mapping, we propose a new harness provisioning algorithm: map-guided escalation. It begins with a task-specific harness and expands to full provision only after a failed self-check. We evaluate our method in two representative MCI tasks: in liquid cooling, it improves the agent accuracy from 0.652 under full provision to 0.715 and achieves accuracy comparable to Reflexion with 48% fewer tokens; In power grids, full provision remains accuracy-optimal, while map-based provisioning offers lower-cost alternatives. These findings show that harness provisioning follows a domain-dependent accuracy-cost Pareto frontier rather than a universal optimum.

---


### 71. [Structure-Internalized Rule Language Model for Faithful Knowledge Graph Reasoning](https://arxiv.org/abs/2608.17443)

**<font color=#1a73e8>作者：</font>** Xingrui Zhuo, Jiapu Wang, Manzong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph Reasoning (KGR) aims to discover latent facts by leveraging the structural evidence available in KGs, posing a challenge to the structural semantic understanding capability of KGR models. Recent studies have demonstrated that Large Language Models (LLMs) can achieve remarkable progress on KGR tasks via flexible in-context learning. However, the inherent representation inconsistency between KG structural context and LLM parametric knowledge remains inadequately addressed. This limitation prevents LLMs from effectively perceiving reasoning evidence that aligns with KG constraints, which undermines both the effectiveness and faithfulness of reasoning. We refer to this problem as reasoning evidence perception drift of LLMs over KGs. To address this problem, we propose a Structure-Internalized Rule Language Model (SIRLM), which centers on structural rule generation to couple the parametric learning of structural knowledge with the faithfulness evaluation of reasoning logic, enabling LLMs to anchor tightly to KG-grounded evidence. Specifically, we first design a Structure-Internalized Rule Generator (SIRG), which incorporates an in-context learning block augmented with a structural relation memory to coordinate structural and parametric knowledge. Furthermore, we equip SIRG with a KG tokenizer based on structural invariance learning and a neuro-symbolic reasoner based on rule-constrained message propagation. These components provide SIRG with learnable structural representations and faithful rule-execution feedback, respectively. Our SIRLM can be seamlessly integrated into standard LLM training paradigms, such as SFT and GRPO. Extensive experiments against 17 state-of-the-art KGR methods on 36 datasets demonstrate the significant superiority of SIRLM.

---


### 72. [Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services](https://arxiv.org/abs/2608.17445)

**<font color=#1a73e8>作者：</font>** Bowen Sun, Zhengyue Zhao, Xiaogeng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answers elsewhere, leaving no reliable grouping signal. We ask whether decomposition attacks can still be stopped under this setting. For a fixed attack strategy without retries, we prove that the achievable security and utility tradeoff depends entirely on how benign requests for the same capabilities are grouped. Persistent, recognizable groups permit a useful defense; fresh, indistinguishable groups do not. When attackers can retry and learn from Allow/Block decisions, this useful operating point disappears: the feedback reveals what passes but not whether a block was correct. Experiments on 91 executable tasks and 11,393 capability-matched benign requests support these results. Under a 1% denial cap for these requests and a 0.5% cap for unrelated background traffic, all ten tested policies, including one privileged policy with an exact request-to-operation map, either fail to stop attacks or exceed the budget. On defense-unseen task families, attack success is at least 99% after one attempt and 100% after two. Effective defenses therefore require additional evidence or mechanisms tied to grouping, such as reliable identity linkage, costs for fresh identities, or control over answer use.

---


### 73. [From Entity Mentions to Tone: An LLM-Based Pipeline for Media Bias Analysis](https://arxiv.org/abs/2608.17454)

**<font color=#1a73e8>作者：</font>** Klesti Hoxha, Olti Qirici  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a pipeline for analyzing media bias and framing in online news. The pipeline groups articles into topics and events, adds named-entity and sentiment annotations, and compares news sources through people mentions, source-level tone, and event-level coverage patterns. We apply it to 8,358 Albanian news articles collected from GDELT and compare the resulting annotations with GDELT's automated annotations. The results show moderate agreement for sentiment and entity extraction, as well as additional person-entity pairs that can potentially support the bias analysis. We compare two annotation prompts and find that stricter sentiment-validation rules remove label-score inconsistencies but increase execution time and reduce annotation coverage. Based on these results, the simpler prompt is used for the rest of the analysis. We have provided sample analysis on source-level framing pro les, person-level tone differences across sources, and event-level gatekeeping and coverage indicators. These outputs show how the same news collection can be used to examine what sources cover, how they describe public figures, and where coverage is concentrated. The approach is particularly useful in settings where manually verified datasets or specialized language tools are limited.

---


### 74. [SAGE: Self-Evolving Storyboard Skills via Attribution-Guided Rule Evolution](https://arxiv.org/abs/2608.17468)

**<font color=#1a73e8>作者：</font>** Maolin Ran, Xiaoyang Lu, Jiaqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Storyboards turn screenplays into visual shot plans for automated short drama production. Professional storyboarding relies on tacit directorial expertise and remains an industrial bottleneck. Large language models can automate this step, but methods for supplying directing knowledge face three challenges: (1) Knowledge acquisition: the craft remains implicit in exemplars or must be written manually. (2) Knowledge refinement: authored knowledge is not evaluated against execution outcomes, and opaque generation prevents feedback attribution to the knowledge behind each decision. (3) Knowledge injection: injecting all knowledge exceeds usable context, while manual selection for every narrative group does not scale. We present SAGE (Skill with Attribution-Guided Evolution), a deployed framework that learns, attributes, evolves, and routes directing knowledge from expert demonstrations. SAGE derives rules that are independent of episode content by contrasting each training screenplay with its expert storyboard. During generation, the model records each narrative group's adopted rules. Combining these records with localized feedback enables targeted updates to individual rules. Evolved rules form scenario packages with a routing index, so each group retrieves only a bounded set appropriate to its situation without expert intervention. On 18 test episodes across three genres, SAGE scored 77.8 on a rubric validated by experts, versus 77.1 for professional directors. Deployed for 14 days on Virtual Film Studio, SAGE produced 1,344 narrative group outputs; 87.2 percent were accepted without substantive edits, and the production team recorded over 83 percent less authoring time per episode. We release PROSE, the first public dataset pairing screenplays with storyboards by professional directors across 68 episodes: this https URL.

---


### 75. [When AI Designs AI: Innovation or Imitation?](https://arxiv.org/abs/2608.17471)

**<font color=#1a73e8>作者：</font>** Yikang Yang, Zhengxin Yang, Luzhou Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM agents have made them increasingly capable of designing methods for complex AI tasks. This raises two central questions about agent-designed methods relative to human-designed methods: how well they perform, and how different their algorithmic designs are. To study these questions, this paper introduces an analysis that derives task-specific algorithmic design spaces from human-designed methods, maps both human- and agent-designed methods into these spaces, and quantifies their algorithmic differences at the module level. Widely used LLM agents are evaluated on a suite of representative, open-ended AI tasks spanning multiple modalities, and the methods they design are analyzed in terms of both task performance and algorithmic differences from human-designed methods. Experimental results show that current agents can occasionally match or surpass human state-of-the-art (SOTA) performance (10/72 configurations), but such success does not generalize reliably across tasks or agents. Moreover, 96.8% of agent-designed methods fall within human-derived algorithmic design spaces, largely recombining algorithmic choices found in human-designed methods, while nearly half exactly match an existing human algorithmic design. Taken together, these findings suggest that although current agents can occasionally match or surpass human SOTA performance, their algorithmic designs remain within human-derived algorithmic design spaces, reflecting the reuse and recombination of algorithmic choices.

---


### 76. [KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation](https://arxiv.org/abs/2608.17485)

**<font color=#1a73e8>作者：</font>** Bowen Sun, Yixi Cai, Xiaogeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) API relays authenticate customers separately but often forward requests through shared provider credentials. Providers scope prompt caches to upstream principals and namespaces, so relay customers mapped to one cache identity can observe each other's cache state. Prior work showed cache sharing at selected endpoints but did not identify which credential, pool, adapter, or nested hop controls the finalidentity. We present KeyPooling, a measurement method that traces customer identity through cache lookup and write, verifies runtime transformations, and tests one predicted identity component at a time. Across five open-source gateways connected to OpenAI and Anthropic, none bound customers to upstream credentials by default; under a shared credential, all five exposed cross-customer cache reads for both providers. Principal and namespace splits, pool associations, and adapter and nested-relay contrasts localized the controlling transformations. In an outcome-independent weekly OpenRouter frame, tests covered 80.5% of eligible token volume and found cross-account reads for 12 of 28 labels carrying 33.7% of volume. On one production route, a controlled procedure recovered eight consecutive target positions without target access. Broader tests identify cache granularity, routing, rate limits, attribution, and budget as conditions for token-by-token recovery, not security controls. We derive a defense contract: every customer must enter a provider-enforced domain, or a namespace derived from authenticated identity must survive every final cache lookup and write. Placing this split after reusable public prefixes preserved most modeled reuse at a 1.7-2.5% cost increase.

---


### 77. [When More Foundation Models Means Less: Diagnosing and Addressing Multi-View Fusion Failure](https://arxiv.org/abs/2608.17490)

**<font color=#1a73e8>作者：</font>** Yibo Liu, Bowen Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation-model hubs turn multi-view fusion into a selection problem: from a large heterogeneous encoder pool, which views should be fused, and how many? We show that downstream performance is non-monotonic in the number of fused encoders; later views can be redundant or task-misaligned, causing accuracy to saturate or decline. We formalise this setting as view-set composition and propose KAGES (Kernel-Alignment Greedy Encoder Selector), a label-aware method that orders frozen encoders by their marginal gain in centred kernel-target alignment. KAGES requires no downstream classifier training during selection, evaluates each candidate in $\mathcal{O}(n^2)$ time independent of encoder dimension, and admits a conditional $(1-e^{-\gamma})$ prefix-wise guarantee under monotonicity and a positive submodularity ratio. Across five recognition regimes and low-shot, larger-pool, and full-data protocols, KAGES improves average AULC over full fusion by 3.9, 5.8, and 3.3 points, respectively, and exceeds DPP and facility-location selection in average AULC. Image retrieval exhibits later, task-dependent saturation along the KAGES ordering, while peak-then-decline reproduces in frozen-LLM fusion. These results show that effective large-pool fusion depends on selecting a compact, task-aligned set of views rather than indiscriminately fusing more encoders.

---


### 78. [SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models](https://arxiv.org/abs/2608.17501)

**<font color=#1a73e8>作者：</font>** Sarvesh Gharat, Junpei Komiyama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent efforts toward fully automated AI scientists have demonstrated that language-model agents can generate hypotheses, execute experiments, and draft scientific manuscripts. However, during the early stages of research, when research problems are formulated, these AI scientists often rely heavily on proprietary frontier models. Their proposals are shaped by opaque parametric knowledge and by literature searches conditioned on the proposals themselves. Such knowledge is effectively a black box, and this dependence makes the evidential basis and validity of generated research problems difficult to audit and leaves the process vulnerable to model-specific hallucinations and biases. Furthermore, if proprietary research materials are transmitted to external APIs, the use of these models creates confidentiality, privacy, and data-governance concerns.
We introduce the Structural Gap Hypothesis Agent (SGHA), a fully automated, corpus-first research-problem discovery system that runs entirely on a local LLM. SGHA structures a scientific literature corpus into evidence-linked paper objects and a typed evidence graph, detects unresolved structural patterns across papers, screens candidate gaps before formulation, and produces traceable research-problem families. In particular, it is able to output assumptions, objectives, success criteria, and remaining ambiguities. All LLM-based components of SGHA are executed using a locally served open-weight 9B language model, without requiring proprietary frontier-model APIs. We compare SGHA with the AI Scientist-v2 idea formulation module in five machine-learning domains. Our results suggest that explicit corpus structure and evidence-constrained reasoning can support promising, inspectable research-problem formulation without relying on frontier models during generation or verification.

---


### 79. [SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment](https://arxiv.org/abs/2608.17514)

**<font color=#1a73e8>作者：</font>** Bishwash Khanal, Anlan Zhang, Sasu Tarkoma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can describe images fluently, but they often fail to provide actionable photographic critique because semantic content and aesthetic judgment remain entangled. We propose SE-MoLoRA, a modular parameter-efficient adaptation framework for domain-specific photographic assessment. The method separates general photographic knowledge from specialist residual judgments using an always-active shared LoRA expert and routed adapters for composition, lighting, and technical quality. A lightweight query router selects the relevant specialist, enabling targeted critique without training separate full models. A rank-64 shared adapter captures broad photographic vocabulary, while rank-32 specialists learn domain-specific residuals with an orthogonal regularization penalty that encourages disentangled representations. Training data is obtained by distilling the Reddit Photo Critique Dataset into domain-labeled critique samples. On held-out critique generation, SE-MoLoRA improves BERTScore-F1 from 0.2317 to 0.4215 over monolithic LoRA and is preferred in 84.6\% of pairwise comparisons, while using fewer active parameters than separate specialist models. SVD-based ablation study shows that shared-specialist decomposition and orthogonal regularization reduce expert overlap. These results demonstrate that modular adaptation improves controllability and specificity in multimodal photographic critique.

---


### 80. [Effects of Answer Format Variation on Gender Bias in Large Language Models](https://arxiv.org/abs/2608.17516)

**<font color=#1a73e8>作者：</font>** Ksenia Merzlyakova, Sebastian Padó, Franziska Weeber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gender bias or other social biases in large language models (LLMs) are frequently evaluated with question answering or survey benchmarks where the LLM needs to give a response in a predefined answer format. It is well known in survey science that the answer format has a substantial impact on answers, just as LLMs are sensitive to the prompt wording. However, to our knowledge it has not been studied yet how changes in answer format impact the measurement of gender bias in LLMs and their alignment with human response distributions. We evaluate three instruction-tuned models on the BBQ benchmark and OpinionQA survey data across closed-ended, Likert-scaled and open-ended formats, comparing bias measurement and distributional alignment under otherwise identical conditions. We find that answer format does substantially alter measured outcomes, including reversals in order rankings. These differences arise because each format elicits distinct response behaviours, such as forced-choice selection, scale-based distributions and refusal in free-text generation. Our findings highlight the importance of treating answer format as a substantive component of LLM evaluation and motivate multi-format designs for more robust model assessment.

---


### 81. [Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents](https://arxiv.org/abs/2608.17524)

**<font color=#1a73e8>作者：</font>** Ram Rachum, Yotam Amitai, Bálint Gyevnár 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This preliminary paper outlines a planned evaluation benchmark for Explainable Reinforcement Learning (XRL) methods. Current evaluations rely on functionally-grounded metrics like faithfulness and compactness, and on human-grounded proxies like subjective ratings or prediction accuracy. We suggest evaluating XRL methods by how effectively their generated explanations help to diagnose and fix malfunctioning reinforcement learning (RL) agents. We propose EvalXRL, a benchmark in which a Large Language Model (LLM) coding agent uses different XRL methods to diagnose a held-out malfunction in an RL agent, and then repair it.
Our proposed benchmark iterates across (environment $\times$ malfunction $\times$ XRL method) tuples and uses the reward signal of the RL agents to form a final score for each XRL method. The coding agent may use the method interactively: invoke the XRL method, process its output, form new hypotheses on what is broken, and invoke the method again with parameters adjusted for testing these hypotheses. This closed-loop structure may be described as a simplified version of the scientific method. Some XRL methods provide self-evaluations that follow this pattern; we propose the first head-to-head comparison of multiple XRL methods in closed-loop usage.

---


### 82. [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528)

**<font color=#1a73e8>作者：</font>** Zhiyuan He, Siwei Zhang, Zhiwen Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an approach later adopted by frameworks such as verl Uni-Agent, AReaL 2.0, slime, and Polar. We refer to this paradigm as harnessed agentic RL, where the deploy-time harness directly participates in model post-training. Harnessed agentic RL differs fundamentally from traditional agentic RL: the harness, rather than the training engine, owns the environment interaction loop, while the trainer observes only sequences of LLM request-response pairs. This introduces challenges in retokenization, sample merging, advantage calculation, loss normalization, and backend scheduling, which can substantially affect training stability and effectiveness. We present Agent Lightning v1.0, a lightweight framework for harnessed agentic RL implemented in approximately 3,500 lines of code. It supports arbitrary agent harnesses and serves as a practical testbed for studying these challenges. We evaluate it on instruction-following, search, and coding agents, and provide a complete reproducible pipeline for coding-agent RL. Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, a 14.6-point absolute gain. We release the complete workflow and training scripts to facilitate reproducible research on harnessed agentic RL.

---


### 83. [When to Review: Spaced Repetition for Continual Pre-Training of Language Models](https://arxiv.org/abs/2608.17530)

**<font color=#1a73e8>作者：</font>** Alankar Atreya, Devesh Batra, Yoages Kumar Mantri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual pre-training of large language models must acquire new information without erasing old knowledge. Existing replay methods often choose a global old/new mixture and sample uniformly, ignoring that examples differ in how quickly they are forgotten. We formulate continual pre-training as adaptive review scheduling: the training loop should decide not only how much history to replay, but which examples should return at each step. We introduce Spaced Repetition Training (SRT), a continual learning framework inspired by cognitive science, which schedules sample-rehearsal using the SuperMemo-2 (SM-2) algorithm. SRT maintains per-example review state, maps per-example perplexity to a recall-quality signal, and schedules historical examples for retention and new examples for consolidation while leaving the model, objective, and optimizer unchanged. On temporally separated Wikipedia and code corpora, SRT improves the stability-plasticity trade-off, recovering 5 to 37 percentage points of old-knowledge accuracy lost by naive continual pre-training across model scales while preserving or improving new-knowledge acquisition. At larger scale, SRT preserves broad benchmark performance that naive continual pre-training and uniform replay substantially degrade. Experiments with vision and tabular data further suggest that the scheduling principle extends beyond language when paired with an appropriate recall signal.

---


### 84. [ArborMem: Navigating Interaction States with Memory Forests](https://arxiv.org/abs/2608.17534)

**<font color=#1a73e8>作者：</font>** Zongwei Lv, Yuemeng Xu, Yilun Yao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as persistent conversational assistants, requiring memory that preserves relevant experience and maintains continuity across interactions. Existing methods improve access to conversational history through long-context processing, selective retrieval, and structured memory organization. However, most systems treat memory access as retrieving relevant past information without first determining which prior interaction state the current turn resumes. This limitation becomes particularly important when conversations interleave multiple tasks, people, and plans that may be interrupted and later revisited. We introduce ArborMem, an online memory framework that represents a long-running conversation as a navigable forest of interaction states. Each branch preserves a locally coherent trajectory, while the forest maintains multiple trajectories that may later be resumed. For each new input, ArborMem localizes the relevant state, restores its branch-local context, and augments it with reusable evidence retrieved across branches, preserving interaction continuity without conflating semantically related but structurally distinct trajectories. Existing long-term memory benchmarks cover diverse memory and reasoning capabilities but do not explicitly isolate branch-structured challenges. We therefore introduce BranchMemEval, a controlled diagnostic benchmark for interleaved and resumable interaction trajectories. Experiments on LongMemEval, LoCoMo, BEAM 100K, and BranchMemEval show that ArborMem outperforms the strongest baselines by 3.36 to 10.31 percentage points on the three established benchmarks and by 5.0 points on BranchMemEval. Its advantage grows under constrained read budgets, while complete memory queries remain below half a second.

---


### 85. [GroupForward: Building Referable 3D Scenes via Instance-Grouped Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2608.17535)

**<font color=#1a73e8>作者：</font>** Qijian Tian, Zimeng Wu, Xuhong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simultaneously reconstructing and understanding 3D environments is essential for embodied agents. Toward this goal, feed-forward semantic 3D Gaussian Splatting (3DGS) efficiently constructs semantic scene representations from sparse multi-view observations. However, existing methods lack explicit instance discrimination and mainly support category- or phrase-based semantic queries. To this end, we propose GroupForward, an instance-grouped feed-forward Gaussian splatting model that reconstructs geometry, appearance, instance structure, and semantics from sparse, unposed, and uncalibrated multi-view images. Unlike existing methods that attach high-dimensional semantic features to each Gaussian, GroupForward learns compact instance embeddings that group Gaussians into cross-view consistent 3D instances, reformulating feed-forward semantic 3DGS from per-Gaussian semantic feature rendering to instance-level semantic aggregation and propagation. Building on these instance groups, we further propose a Referential Scene Reasoning Framework (RSRF) for complex 3D referring segmentation. RSRF constructs an instance-grouped 3D scene graph and retrieves candidate instances for a given referring expression. A vision-language model then reasons over structured instance evidence and multi-view observations to identify the referred instance among the candidates. RSRF thereby extends language interaction from simple semantic querying to complex referential scene reasoning. Experiments on semantic reconstruction and referential reasoning demonstrate the effectiveness of our instance-grouped reconstruction and reasoning framework.

---


### 86. [CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method](https://arxiv.org/abs/2608.17536)

**<font color=#1a73e8>作者：</font>** Jin Su, Zhuofeng Zhao, Huanhuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal consultation questions exhibit multi-level complexity. A single retrieval strategy often leads to over-reasoning for simple questions and poor interpretability for complex ones, making it difficult to meet the requirements for both answer quality and efficiency in high-risk scenarios. To address this issue, this paper proposes CoAL-RAG, a complexity-aware legal retrieval-augmented generation method, which constructs a multi-dimensional evaluation mechanism based on ``question essence'' and ``retrieval consistency'' to enable adaptive routing of retrieval strategies. First, the reasoning demand is quantified according to the logical structure of the question. Then, the discrepancy between semantic retrieval and keyword retrieval is utilized to indirectly reflect problem complexity, thereby selecting the most appropriate retrieval strategy and dynamically filtering contextual information. Experimental results demonstrate that the proposed method significantly outperforms baseline models not only on Chinese legal benchmarks (SocialLawQA, LawBench) but also demonstrates strong cross-jurisdictional generalization on English datasets (LexGLUE, CaseHold). Specifically, on Chinese datasets, the BLEU score improves by 42.5\% and ROUGE-L reaches 3.6 times that of knowledge graph-based methods. On English benchmarks, CoAL-RAG maintains highly competitive accuracy, achieving an optimal balance between generation quality, deep logical reasoning, and system efficiency across different legal systems.

---


### 87. [Code as Representation: A Compilable Parsing Paradigm for Academic Documents](https://arxiv.org/abs/2608.17550)

**<font color=#1a73e8>作者：</font>** Rihui Jin, Jun Wang, chengyuan zhu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Academic papers are a primary carrier of scientific knowledge, yet most of this knowledge remains locked in PDFs that are optimized for human reading rather than machine use. For Multimodal Large Language Models (MLLMs), the core challenge is not only perception, but representation: scientific pages interleave text with Structured Academic Elements (SAEs) such as tables, formulas, charts, and pseudocode, whose structure, data, and logic are poorly preserved by common surrogates like Markdown. We therefore propose Compilable Academic Document Parsing (CADP), a paradigm that reconstructs a full page as contextual \LaTeX{} plus executable Python, so that structure-preserving elements and executable chart representations can be reconstructed, recompiled, and directly verified against the source page. To support this setting, we introduce CADP-Bench, an expert-verified benchmark of full academic pages containing tightly coupled text and multiple SAE types, evaluated through a re-injection compilation protocol. We further study current capabilities using SOTA MLLMs and an exploratory multi-agent baseline that incorporates common agentic techniques. Results show that even frontier models still struggle to produce high-fidelity executable reconstructions, highlighting substantial room for improvement in structure-aware scientific document parsing. CADP-Bench is released for future research.

---


### 88. [CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided Video Editing](https://arxiv.org/abs/2608.17566)

**<font color=#1a73e8>作者：</font>** Fuchen Long, Cong Wang, Zitao Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality and diversity of instruction-based video editing datasets are steadily improving, yet existing datasets mainly focus on single editing operations and fall short in supporting compositional instruction-guided video editing. In particular, multiple editing intents must be jointly understood and faithfully executed within the same video. To address this issue, we introduce CoinVE-200K, a large-scale, high-quality dataset for Compositional Instruction-Guided Video Editing. CoinVE-200K contains 1080p video-editing pairs of up to 201 frames, covering diverse compositional scenarios where each sample involves 2 to 5 atomic editing operations. The instructions target humans, objects, and backgrounds, and cover edit types such as addition, removal, modification, and stylization. All samples are built through a carefully designed generation and filtering pipeline to ensure instruction faithfulness, visual quality, temporal consistency, and compositional diversity. We also introduce CoinVE-Bench, a benchmark for compositional-instruction video editing across diverse subjects, operation types, and instruction complexities. Furthermore, we present CoinVE-Edit, a 22B compositional video editing model built upon Wan2.1-T2V-14B and Qwen3-VL-8B-Instruct. CoinVE-Edit disentangles region-aware attention for different editing instructions, enabling precise multi-region editing while preserving irrelevant content and temporal coherence. Experiments on CoinVE-Bench show that CoinVE-Edit achieves strong performance in instruction following, compositional editing accuracy, visual quality, and temporal consistency.

---


### 89. [Domain-Adapted Molecular Language Models for Efficient Search of Make-on-Demand Libraries](https://arxiv.org/abs/2608.17567)

**<font color=#1a73e8>作者：</font>** Henrik Wille, Luis-Finley Schütz, Felix Strieth-Kalthoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained molecular language models are increasingly used as molecular encoders for learning structure-property relationships. However, their practical suitability for molecular discovery within and beyond their pretraining domain remains unclear. Herein, we systematically benchmark four molecular language models across six virtual molecular libraries spanning drug discovery, organic materials, and catalysis. Native molecular language model embeddings show substantial variation in discovery performance across libraries, whereas molecular fingerprints provide a consistently strong and robust baseline. Consistent with a potential domain-representation mismatch, we show that explicit domain adaptation substantially improves representation performance. Fine-tuning molecular language model encoders on structures from the target virtual library consistently improves sample efficiency, with several adapted encoders emerging as the top-performing representations across the benchmark tasks. These results show that molecular representation quality depends strongly on the target domain and that explicit adaptation can improve the practical utility of molecular foundation models. More broadly, our findings establish domain-adapted molecular representations as a promising strategy for sample-efficient adaptive decision making in virtual screening and self-driving laboratories.

---


### 90. [Quantifying Risk Under Evolving Uncertainty: Belief-Dependent Robustness for Safe Sequential Decision Making](https://arxiv.org/abs/2608.17574)

**<font color=#1a73e8>作者：</font>** Deep Kumar Ganguly, Jan Kretinsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How cautious should an agent be while it is still learning its environment? We propose RATTL (Risk-Adversarial Total-Reward Learning), which ties caution to epistemic uncertainty: the agent holds a Bayesian posterior over unknown dynamics and plans against a Wasserstein ambiguity set whose radius is a monotone function of that posterior. The radius contracts with evidence, so behaviour interpolates continuously between worst-case robustness and risk-neutral total-reward maximization. The design follows the duality underlying the Entropic Value-at-Risk, which converts the choice of a risk level into the choice of an ambiguity radius. We show the resulting planning problem is well posed under transience and compactness conditions, and prove a Safety Sandwich: the RATTL value lies between the uninformed robust value and the full- knowledge optimum, with a gap that vanishes as the posterior concentrates. In a canonical binary-hazard instance, the induced criterion reduces to Conditional Value-at-Risk at a level set by the posterior entropy. A worked example shows the agent deferring the efficient action until a sharp identification threshold. RATTL targets runtime safety for agents, including LLM-based systems, acting under uncertainty.

---


### 91. [Auditing Exposure to Harmful Content on TikTok using Multimodal Language Models: A Cross-National, Age-Stratified Study](https://arxiv.org/abs/2608.17583)

**<font color=#1a73e8>作者：</font>** Hamidreza Saffari, Francesco Pierri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online video platforms can expose young users to harmful content, but independent audits remain difficult because video annotation is costly and moderation judgments vary across languages. We audit TikTok in France, Italy, and Sweden with sockpuppet accounts representing four age personas (13, 16, 19, 40), collecting 36,971 videos from passive For-You-page scrolling and active sessions that scroll, search for harm keywords, and scroll again. To scale annotation, we validate four multimodal LLMs against native-speaker labels on a 300-video reference set. Gemini 2.5 Flash with eight sampled frames plus text performs best (aggregate kappa = 0.42), at half the per-call cost of native-video upload, and we apply it to a 10% sample for approximately \$50 in total API spend across both modalities. Keyword search returns 35-56% harmful content, a 1.5-7.5x increase over the scrolling baseline in ten of twelve country-age combinations; the spike is temporary and flattens the age differences observed in France and Sweden. Under passive scrolling, Italy has the highest harm rate at every age, with Italian age-19 reaching 48.6%. Overall, MLLM-based auditing offers a scalable approach for cross-national youth-safety audits, while provider safety filters (1.1% refusal rate) under-count the most explicit harms.

---


### 92. [Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback](https://arxiv.org/abs/2608.17587)

**<font color=#1a73e8>作者：</font>** Kang Peng, Zhiwei Zhang, Yichen Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert-written natural language skills can improve tool-using agents, yet agent-authored skills perform 8-11 points worse than using no skill. This gap suggests that following procedural guidance and improving it from execution evidence are distinct capabilities. Inference time loops can repair skills but do not improve the model that writes the next one. We study how to organize execution experience from intermediate skills into training states for an optimizer. We introduce WER (Write, Execute, and Refine), a multi-phase framework that trains a Skill Optimizer outside a frozen executor. The optimizer proposes skills, a frozen agent executes each repeatedly, and a programmatic verifier scores the outcomes. The scores provide relative credit and select mixed-outcome records. Matched successful and failed trajectories from these records form the next phase's refinement states, so the optimizer learns from the consequences of its earlier outputs. On BFCL v4 multi-turn and tau2-bench, WER improves average Pass@1 over the no-skill baseline by 7.80 and 3.85 points, respectively. Under an identical refinement workflow, it outperforms the same backbone without optimizer training by 9.35 and 10.29 points. The trained 4B optimizer reaches 76.63 percent on BFCL v4, outperforming all evaluated off-the-shelf general-purpose models used as skill optimizers on average.

---


### 93. [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](https://arxiv.org/abs/2608.17588)

**<font color=#1a73e8>作者：</font>** Zhibo Zhang, Zhen Ouyang, Ling Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills package reusable natural language procedures with executable resources, enabling software agents to acquire task specific capabilities without model adaptation. Automatically generating such Skills can improve task performance, yet evaluating a candidate solely from its artifact or final task outcome leaves unresolved which actions the equipped agent will perform and which side effects those actions will produce. We present TRUSS, an evidence guided framework for generating functionally effective and safety reliable Agent Skills. TRUSS first inspects functional claims against source and domain evidence while evaluating the complete artifact under nine predefined safety properties. Candidates admitted by this static gate are loaded by a shadow agent inside a Controllable Execution Environment, where brokered tools expose requested actions to policy enforcement and record their results as provenance preserving execution traces. Functional failures and property violations are linked back to the responsible Skill content and used to guide iterative refinement.
We evaluate TRUSS on 168 SkillInject artifacts, 155 SkillSafetyBench cases, and all 187 tasks in SkillGenBench. TRUSS achieves 100.00\% precision and recall in vulnerability detection. Repair reduces attack success from 38.71\% to 19.35\% with GPT 5.5 and from 46.45\% to 29.68\% with GPT 5.4, with zero attack regression. For Skill generation, TRUSS raises task effectiveness from 17.11\% without Skills to 52.94\%, while increasing the benchmark Security rate from 50.80\% to 100.00\%. These results show that execution evidence can expose behavioral failures missed by artifact inspection and can guide Skill generation toward jointly verified functional and safety outcomes.

---


### 94. [PathoArgus: Advancing Evidence-Grounded Long-Context Visual Reasoning across Gigapixel Whole-Slide and Multi-Slide Case Contexts](https://arxiv.org/abs/2608.17607)

**<font color=#1a73e8>作者：</font>** Bowen Liu, Qixiang Zhang, Xiaomeng Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide pathology reasoning requires models to integrate gigapixel-scale visual evidence across complete case-linked slides, yet current question-answering benchmarks primarily measure final answer accuracy--a metric vulnerable to linguistic priors and benchmark regularities, and insufficient to establish that predictions are grounded in the supplied tissue. We introduce PathoArgus-Bench, a benchmark and evaluation protocol that explicitly tests the full evidence chain: availability, accessibility, use, and responsiveness. PathoArgus-Bench comprises 22,078 four-choice questions from 4,913 patients across 15 TCGA projects, covering six pathology capabilities across three levels of evidence demand, and operates under a fixed reader budget that retains only a small fraction of the gigapixel context. To further isolate evidence-grounded reasoning, we contribute ESG (Evidence State Quartets), a controlled set of 483 quartets where the question text is fixed while the target WSI set is moved, replaced, or removed, requiring consistent predictions across all states. Evaluating 20 general-purpose, medical, and pathology-specific systems reveals a stark gap: while GPT-5.6 achieves 57.09% overall accuracy and 57.04% on ESG, it correctly completes only 19 of 483 quartets (3.93% QExact), exposing that row-level accuracy does not translate into reliable evidence grounding. We also introduce PathoArgus, a fixed-budget reader that allocates context via question relevance and spatial coverage, attaining 50.39% overall accuracy yet only 1.86% QExact--demonstrating that improved context access alone does not ensure consistent evidence-based prediction. Our benchmark and diagnostics establish that acquiring useful whole-slide context is necessary but far from sufficient, and call for a shift from answer-centric to evidence-grounded evaluation in computational pathology.

---


### 95. [Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing](https://arxiv.org/abs/2608.17638)

**<font color=#1a73e8>作者：</font>** Kang Chen, Sihan Zhao, Yixin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What a reasoning model writes is only a partial record of the process that produces it. We introduce a two-level internal readout for mixture-of-experts reasoning. We first distill vocabulary-scale J-space into J64, a 64-axis semantic frame learned from the model's own reasoning states. J64 reveals readable process state that the emitted trace does not show: it separates inference effort from problem-induced strain. It also adds 0.096 to 0.135 held-out AUC over a baseline that reads the same rollout as token occupancy and aggregates it in exactly the same way. We then reconstruct J64 from native expert-routing statistics. The result is R64, a low-overhead proxy: its median per-axis correlation with J64 is 0.69 to 0.86 across three models and two families, and on gpt-oss-20b it preserves 95 to 100% of J64's predictive gain. The readout supports test-time decisions at two temporal resolutions. Over completed candidate sets, J64 and R64 improve single-branch selection, and R64-weighted voting improves plain majority voting in seven of eight settings. During generation, rolling readout windows drive a cumulative stop-and-resample policy whose operating point is fixed on training questions alone. J64 improves accuracy by 1.1 to 5.9 points over a sibling-permuted control, and the routing-only R64 proxy retains 0.9 to 3.2 of those points. Finally, router edits aimed at the mechanism J64 names induce the predicted reasoning behaviors and shift a diagnosed stall from numerical guessing toward exact symbolic execution. Together, J64 makes latent process state readable, while routing makes it deployable and actionable.

---


### 96. [LLM-Derived Preference Judgments Are Not Self-Consistent](https://arxiv.org/abs/2608.17644)

**<font color=#1a73e8>作者：</font>** Matthew T. Ford, Francis Bahk, Jingjing Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents increasingly interpret a person's natural-language preferences by querying an LLM for numerical preference judgments, e.g., by asking how much the person would be willing to pay for an item. A growing body of work estimates a utility function from these judgments and then chooses actions based on their estimated utility. This pipeline assumes the judgments are approximately self-consistent: that a single utility function can reproduce them. But are they? To study this question, we measure the self-consistency of cardinal LLM preference judgments. For example, the difference in stated willingness-to-pay between two items should match the stated payment that makes a person indifferent to exchanging them. We develop statistical tests and interpretable measures of how far observed responses depart from the best-fitting self-consistent utility function. Experiments with flight, apartment, and hotel examples across six LLMs reveal large persistent inconsistencies. This suggests that LLM-derived preference judgments cannot be faithfully summarized by a single utility function.

---


### 97. [GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities](https://arxiv.org/abs/2608.17665)

**<font color=#1a73e8>作者：</font>** Haoran Bu, Zejian Chen, Litian Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a propagation channel. This threat contains three stages. During exposure and memory retention, the attacker exposes a small set of target agents to arguments that reinforce their respective stated stances. The targets' memory systems then process and retain these arguments. During retrieval and reproduction, a shared stance-neutral discussion cues the targets to retrieve and reproduce their respective retained arguments. During iterative propagation, untreated agents influenced by the reproduced arguments restate and spread them. We instantiate this threat in GraphWake with three components: (i) stance-support argumentation knowledge graphs construct knowledge-based arguments; (ii) axiom-oriented triple selection distills them for reliable retention and reproduction; and (iii) stance-neutral memory cueing triggers concurrent retrieval and reproduction, initiating propagation. Experiments across multiple discussions and memory systems show that GraphWake substantially increases group polarization. These findings reveal a community-level polarization risk.

---


### 98. [Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](https://arxiv.org/abs/2608.17684)

**<font color=#1a73e8>作者：</font>** Jialong Li, Jialing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents turn experience into reusable skills, workflows, or memories, but post-evolution accuracy alone does not show whether learned behavior preserves previously correct behavior or security. We audit SkillOpt, Agent Workflow Memory (AWM), and ReasoningBank in simulated e-banking using matched benign acquisition trajectories, sealed evaluation endpoints, execution-grounded checks, and independent state replay. On Qwen 3.7 Flash, SkillOpt raises benign utility from 0.741 to 0.837 while exposure to injected content rises from 0.820 to 0.943. Conditional attack success after exposure falls from 0.605 to 0.562, yet overall attack success rate (ASR) rises from 0.496 to 0.530 and unauthorized financial state changes rise to 0.685. Across three independently evolved lineages, capability, exposure, and unauthorized-state changes increase in all three, whereas ASR increases in only two. ReasoningBank raises utility to 0.859 without increasing aggregate ASR, although unauthorized state changes remain slightly above Static. AWM reveals a separate evaluation hazard: a literal WebArena text-action envelope disrupts tool execution in our native function-calling executor. In a post-hoc sensitivity test, removing only that envelope restores utility from 0.319 to 0.756, while exposure rises from 0.299 to 0.909 and ASR from 0.195 to 0.575. Auditing self-evolving financial agents therefore requires tracking regressions, attack-surface contact, unauthorized financial-state change, and artifact-executor compatibility, not accuracy alone.

---


### 99. [Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals](https://arxiv.org/abs/2608.17687)

**<font color=#1a73e8>作者：</font>** Joao Fonseca, Rodrigo Rodrigues, Paolo Romano  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite their widespread use, Large Language Models (LLMs) remain limited by a fundamental problem: the generation of plausible but false content, known as hallucinations. Most existing detection methods operate at the answer or sentence level, yet per-token detection is essential for localizing hallucinated spans and enabling fine-grained interventions. In this paper, we explore the use of the Mixture-of-Experts (MoE) paradigm to address this gap. In MoE architectures, a single forward pass activates a sparse subset of experts (i.e., distinct feedforward networks per layer) via a routing mechanism, producing internal signals (e.g., router entropy, expert disagreement, and expert usage patterns) that are unavailable in dense architectures and have not been previously exploited for hallucination detection. To this end, we introduce InnerExpert, the first method to leverage these MoE-specific signals for per-token hallucination detection. InnerExpert combines routing-level and standard transformer signals into compact per-token feature vectors, classified by a lightweight detector trained on labels produced by an LLM-as-a-judge pipeline, which enables continuous model updates without manual annotation. Our results show that InnerExpert outperforms existing methods across five datasets and two MoE architectures, achieving up to 0.91 answer-level and 0.76 token-level AUROC, while requiring only a single forward pass.

---


### 100. [Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents](https://arxiv.org/abs/2608.17718)

**<font color=#1a73e8>作者：</font>** An He, Yao Wang, Haibin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents increasingly operate across many steps, tools, and observa- tions. In this setting, the relevant oversight question is not only whether each action is locally valid, but whether the evolving trajectory still corresponds to the task the user authorized. Drift can accumulate quietly: an agent may call the right tool with plausible arguments at every step, while its prefix moves toward a broader role, an adjacent objective, or evidence the user never supplied. Existing monitors mostly check local compliance, deliver final-trace verdicts, or score generic risk; they do not directly estimate this prefix-level relation. We introduce ontological trust, a task-conditioned property of trajectory prefixes, and instantiate it as RGE, an online monitor that decomposes trust along Role, Goal, and Evidence. RGE uses LLMs only to derive structured task and step representations; trust-state updates, projec- tions, and intervention decisions are deterministic, so the output is a replayable and auditable trust trajectory rather than a single end-to-end judge verdict. We construct a cross-domain trajectory corpus from OSWorld, FinanceBench, and EICU-AC, covering benign executions, prefix-paired drift, and pseudo-consistency failures. On this corpus, RGE outperforms adapted rule-, judge-, and shield-style baselines on prefix-paired drift detection. With the two larger estimator models, it exceeds 93% Drift F1 on every benchmark while keeping benign coverage at or above 95.8%. Pseudo-consistency is harder: detection depends on whether task completion is externally visible, a structural limit we characterize empirically.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-161](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
