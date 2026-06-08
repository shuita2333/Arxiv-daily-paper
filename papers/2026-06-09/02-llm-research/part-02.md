# 🧠 大模型相关研究 | 2026年06月09日

> 本类共 **114** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-114](./part-03.md)

---

### 51. [Diagnosing Visual Ignorance in Vision-Language Models](https://arxiv.org/abs/2606.06890)

**<font color=#1a73e8>作者：</font>** Runyu Zhou, Qi Zhang, Qixun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) frequently rely on language priors, producing confident answers that are weakly grounded in visual evidence. While this behavior is widely observed, its internal mechanisms and its impact on benchmark evaluation remain insufficiently understood. In this work, we study language-prior reliance from both mechanistic and behavioral perspectives. Internally, we combine counterfactual layer replacement with supervised layer-wise MLP probing to trace how ground-truth visual semantics and language-prior semantics compete across the language decoder. Our analysis reveals a multi-stage bottleneck: intermediate layers often fail to effectively retrieve visual information, while later layers can further suppress surviving visual signals in favor of text-space biases. Externally, we introduce a progressive visual decay metric based on multi-step Gaussian blurring, which identifies instances whose answers remain invariant even as visual content is increasingly destroyed. Across twelve visual question-answering benchmarks and three representative VLMs, we find that a substantial fraction of examples remain answerable under severe or total visual obfuscation, indicating that current benchmarks can inadvertently reward visual ignorance. These findings demonstrate that language-prior reliance is a systematic routing failure affecting both model internals and benchmark validity. Finally, we outline critical pathways for future research, highlighting the necessity of designing training distributions and evaluation protocols built on structurally isolated or counterfactual data to enforce genuine cross-modal grounding.

---


### 52. [Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors](https://arxiv.org/abs/2606.06891)

**<font color=#1a73e8>作者：</font>** Hanxun Yu, Xuan Qu, Lei Ke 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite advances in 3D scene understanding, existing 3D Large Multimodal Models operate in offline settings, requiring complete scene observations or predefined video clips. In this paper, we present an online 3D vision-language model that enables real-time spatial understanding from streaming video. Our approach adopts an autoregressive streaming control modeling based on the LLM's next-token prediction objective to learn when to respond, and employs a lightweight Visual-Spatial Feature Integration (VSFI) module to incrementally inject temporally aligned geometry priors into the visual stream. To alleviate long-context decoding overhead, we propose a plug-and-play Geometry-Adaptive Voxel Compression (GAVC) module for efficient visual token compression. To address the scarcity of streaming 3D-language data, we further develop a scalable data generation pipeline that curates over 1M online spatio-temporal 3D QA pairs and establishes a comprehensive benchmark spanning 29 tasks. Extensive experiments show that our approach significantly outperforms both proprietary and open-source models across online and offline 3D spatial understanding, reasoning, and grounding tasks. The project page is available at this https URL

---


### 53. [GRASP: Geometry-aware Residual Alignment for Scalable Pretraining Data Attribution](https://arxiv.org/abs/2606.06892)

**<font color=#1a73e8>作者：</font>** Yue Min, Ruining Chen, Yujun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalable data attribution methods typically assign isolated utility scores to individual training examples. This prevalent additive assumption fundamentally fails to capture critical subset dynamics, including data redundancy and complementary coverage. In this work, we reframe attribution as subset-level counterfactual utility prediction and introduce GRASP, an interaction-aware surrogate. Grounded in a theoretical smoothness lower bound, GRASP explicitly models subset interactions through a quadratic geometric penalty. To achieve pretraining-scale efficiency without relying on hidden oracle tuning, we couple low-dimensional feature sketches with a strictly finite lower-confidence bound selection protocol. Extensive subset-retraining evaluations demonstrate that GRASP decisively outperforms existing scalable baselines. It more than doubles the task-level rank correlation for counterfactual subset fidelity while reducing upfront artifact construction costs by nearly an order of magnitude. Downstream diagnostics further show that this scoring mechanism transfers to language model curation and cross-domain vision selection, establishing a robust foundation for optimizing massive pretraining corpora.

---


### 54. [TALAN: Task-Aligned Latent Adaptation Networks for Targeted Post-Training of Large Language Models](https://arxiv.org/abs/2606.06902)

**<font color=#1a73e8>作者：</font>** Chengkai Zhang, Ziteng Liu, Junpu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Targeted post-training aims to improve reasoning, math, and code without degrading strengths. Low-rank adapters are efficient but task-global; activation interventions are input-aware but often require separate probes, vectors, or inference-time steering. We introduce TALAN (Task-Aligned Latent Adaptation Networks), a sequence-conditioned latent side path inserted into a transformer's residual stream and co-trained with a low-rank adapter in one SFT loop. TALAN compresses the active sequence into latent memory, remixes it into token-level perturbations, and writes them back through a controlled residual update. It is configured along six axes: insertion location, memory size, mixer, writeback rule, trainability scope, and gradient scale.
Across four Qwen3-family backbones and four STEM/code benchmarks, TALAN improves matched LoRA and DoRA baselines. With LoRA, it yields a +1.41 point cross-model mean gain, positive on all four backbones and non-negative on all 16 model-benchmark cells. With DoRA, it yields a +1.85 point mean gain, positive on all backbones and on 13 of 16 cells. Paired seed checks support positive average effects but show nontrivial variance, so we treat them as sensitivity checks. Cost is small: <1% trainable parameters relative to the backbone and 1.01-1.02x inference overhead versus matched LoRA. A Llama-3.2-1B transfer probe is also positive under LoRA and rsLoRA across seven paired seeds, supporting a transfer beyond Qwen.
Internal-state analyses suggest TALAN is a small complementary activation intervention. The matched adapter update is 80-1,700x larger than the TALAN perturbation, yet their directions have near-zero cosine; per-layer measurements show this small orthogonal perturbation propagates and amplifies through depth. TALAN offers a practical platform for studying steerable activation-level adaptation within standard adapter-based post-training.

---


### 55. [ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning](https://arxiv.org/abs/2606.06915)

**<font color=#1a73e8>作者：</font>** Vladislav Smirnov, Chieu Nguyen, Sergey Senichev 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time compute (TTC) scaling has emerged as a powerful paradigm for improving large language model (LLM) reasoning by allocating additional compute during inference, e.g., via multi-sample generation and verifier-based reranking. Existing TTC scaling strategies and reasoning scorers remain fragmented, evaluated under inconsistent protocols, and are rarely analyzed through the lens of quality-cost trade-offs. We introduce ThinkBooster, a unified framework for seamless test-time compute scaling of LLM reasoning, which consists of (i) a modular Python library implementing state-of-the-art TTC scaling strategy and scorer families, (ii) a benchmark that jointly evaluates performance and computational efficiency, and (iii) a deployable OpenAI-compatible proxy service that enables drop-in integration of adaptive reasoning into real-world applications. We further provide a demo visual debugger for inspecting the reasoning trajectories, intermediate selection decisions, and alternative reasoning paths. Empirical results on mathematical and coding tasks reveal the performance-compute trade-offs of TTC scaling strategies and scoring methods and demonstrate that ThinkBooster provides practical gains in real-world tasks. The code is available online under an MIT license.

---


### 56. [The Fine-Tuning Trap: Evaluating Negative Transfer and the Role of PEFT in Sub-1B Mathematical Reasoning](https://arxiv.org/abs/2606.06920)

**<font color=#1a73e8>作者：</font>** Rahul Nair, Chun Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying Small Language Models (SLMs) on edge devices requires efficient fine-tuning strategies that adapt models to new tasks without degrading their general capabilities. In this study, we benchmark five sub-1B models (135M-1B) on mathematical reasoning tasks and uncover a critical vulnerability: Full Fine-Tuning (Full FT) actively harms performance in models under 300M parameters, often dropping accuracy below zero-shot baselines. This "negative transfer" makes Parameter-Efficient Fine-Tuning (PEFT) not just an efficiency preference, but a stability requirement. We find that while Low-Rank Adaptation (LoRA) and Weight-Decomposed LoRA (DoRA) perform comparably, their strengths vary by task; DoRA excels in complex reasoning (GSM8K), while LoRA dominates pattern matching (OrcaMath). In particular, Full FT is outperformed by LoRA on aligned models (Qwen2.5-0.5B) and even by simple 5-shot In-Context Learning on the smallest architectures (SmolLM2-135M). Based on these findings, we recommend defaulting to PEFT for all aligned sub-1B models and caution against Full FT for any architecture smaller than 500M parameters to prevent catastrophic forgetting. Reproduction of this work can be found at this https URL.

---


### 57. [From Sampled Outcomes to Capability Distributions: Rethinking Supervision for LLM Routing](https://arxiv.org/abs/2606.06924)

**<font color=#1a73e8>作者：</font>** Guannan Lai, Haoran Hu, Long Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing LLM routing methods typically treat a model's single response to a query as its capability label for training routers. However, because LLM generation is inherently stochastic, such single-shot supervision provides only a noisy observation of a query-model pair's behavior rather than a reliable capability estimate. We show that this assumption introduces systematic noise into routing supervision, making learned routing policies less reliable. To address this issue, we propose DARS (Distribution-Aware Routing Supervision), a framework that constructs routing supervision from a distributional view of model behavior. Instead of relying on a single generated response, DARS considers uncertainty from both the input side and the output side, capturing how semantically equivalent query formulations and stochastic generations affect model performance. Based on these distribution-aware observations, DARS builds more reliable supervision signals for routing. Experiments across diverse tasks show that single-shot labels can be misleading for model selection, while distribution-aware supervision provides more stable labels and improves learned routing behavior. Our results suggest that reliable LLM routing should move beyond single-response observations and be grounded in query-level model capability distributions.

---


### 58. [SVHighlights: Towards Extremely Long Sport Video Highlight Detection](https://arxiv.org/abs/2606.06926)

**<font color=#1a73e8>作者：</font>** Donggyu Lee, Youngbin Ki, Jeonghun Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While highlight detection for long-form videos is of great practical importance, most existing methods remain limited to short-form content, largely due to the absence of a suitable benchmark. To bridge this gap, we introduce SVHighlights, to the best of our knowledge, the first benchmark for highlight detection in extremely long sports videos, each exceeding one hour in duration, across multiple sports categories. SVHighlights is constructed from pairs of full-length sports videos and their corresponding official highlight videos using a dataset generation pipeline, enabling scalable label generation without conventional per-clip saliency annotation. The benchmark comprises 320 videos with an average duration of 2.00 hours and a total of 640.18 hours, substantially exceeding previous datasets. Existing methods also face fundamental challenges on long videos: models trained on short clips fail to generalize to hour-long content, and their clip-level scoring lacks the broader context needed to identify highlights. To address this and provide a strong baseline, we present TF-SELECTOR, a training-free segment-based approach that divides each video into context-aware segments by merging adjacent shots sharing the same semantic content, and predicts segment-level saliency scores using a large language model with multimodal inputs including visual captions, transcripts, and audio volume. Experiments demonstrate that TF-SELECTOR achieves superior performance across most metrics compared to Video Temporal Grounding (VTG)-tuned baselines, with improvements of +3.12 in HIT@1, +4.06 in HIT@K, and +2.95 in IoU. These results establish SVHighlights as a challenging testbed for long-form highlight detection and demonstrate that a simple segment-based strategy can effectively scale to hour-long videos.

---


### 59. [Personality Anchoring for Social Simulation: Linking Personality, Social Behavior, and Interaction Success with LLM Agents](https://arxiv.org/abs/2606.06936)

**<font color=#1a73e8>作者：</font>** Vahid Sadiri Javadi, Aksa Aksa, Fryderyk Róg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social interactions are shaped by the interplay of dispositional traits and situational context, yet systematically investigating how personality configurations between individuals jointly influence social behavior across diverse social contexts remains methodologically challenging. We address this gap by introducing a simulation pipeline adapted from the CHARISMA framework, which employs well-known movie characters and public figures as psychologically grounded agents for multi-LLM social simulation using a method we term personality anchoring. We present a large-scale empirical study examining how dyadic Agreeableness composition influences social interaction outcomes across 1,010 simulated conversations. Our results reveal a monotonic relationship between dyadic Agreeableness composition and shared goal achievement, with Homogeneous-Agreeable pairs achieving success 10 times the rate of Homogeneous-Disagreeable pairs (62% vs. 6%). Behavioral mediation analysis reveals that Agreeableness shapes goal achievement partially through cooperative strategy selection, though it continues to predict outcomes within the same dominant strategy, indicating pathways beyond observable conversational behavior. Robustness analyses confirm high consistency of results across repeated simulations (ICC = 0.89) and stable personality expression across diverse scenarios, validating personality anchoring as a viable operationalization strategy.

---


### 60. [Quantum-Inspired Trace-Augmented Evidence Selection for Reasoning over Structured Hypothesis Spaces](https://arxiv.org/abs/2606.06941)

**<font color=#1a73e8>作者：</font>** Laura Wynter, Nirvik Sahoo, Paul Griffin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now solve a wide range of expert-level exams at or above human level, yet remain brittle on specialised, evidence-intensive domains such as law. On these tasks, errors arise not only from gaps in world knowledge but also from subtle distinctions between pieces of evidence and inconsistent use of supporting evidence. The most common aggregator over sampled chain-of-thought (CoT) traces, majority vote, returns the most popular answer regardless of whether its evidence is actually strongest. We propose to treat the selection of CoT reasoning fragments into a set of evidence as an explicit combinatorial optimisation problem, allowing well-supported but minority hypotheses to override noisy majorities, and to evaluate the approach on legal-reasoning benchmarks that are particularly sensitive to evidence quality. We introduce EP-HUBO (Evidence Pool Higher-Order Binary Optimisation), which generates multiple CoT traces with a small local model, parses fragments into per-hypothesis evidence pools, solves a higher-order unconstrained binary optimisation per pool with quality-derived weights (relevance, specificity, distinctiveness), and delegates a single adjudication call per question to a frontier model. We evaluate EP-HUBO on two evidence-intensive legal benchmarks using both simulated annealing on classical hardware and the Dirac-3 photonic entropy-quantum machine from Quantum Computing Inc. HUBO-style optimisation gives a principled way to aggregate reasoning fragments while preserving minority-but-correct hypotheses, and is most valuable in low-contamination domains where frontier models have not already absorbed the benchmark material.

---


### 61. [SS-TPT: Stability and Suitability-Guided Test-Time Prompt Tuning for Adversarially Robust Vision-Language Models](https://arxiv.org/abs/2606.06943)

**<font color=#1a73e8>作者：</font>** Sunoh Kim, Daeho Um  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) such as CLIP achieve strong zero-shot recognition but remain highly fragile under adversarial perturbations. Recent test-time adaptation defenses improve robustness by leveraging many augmented views, but this leads to impractical slowdown and a clear robustness-throughput trade-off. To address this challenge, we present Stability and Suitability-guided Test-time Prompt Tuning (SS-TPT), evaluating the quality of each augmented view via two complementary scores: (1) stability, measuring prediction invariance to weak augmentations, and (2) suitability, measuring feature-space density among views. These stability and suitability (SS) scores guide both adaptation and inference through an SS-guided consistency loss and an SS-weighted prediction, amplifying trustworthy views while suppressing corrupted ones. Extensive experiments demonstrate that SS-TPT significantly outperforms prior state-of-the-art methods, achieving superior robustness-throughput trade-offs across diverse datasets and varying numbers of views, thereby demonstrating both strong practicality and generality. Our code is available at this https URL.

---


### 62. [Auditing Training Data in Domain-adapted LLMs: LoRA-MINT](https://arxiv.org/abs/2606.06946)

**<font color=#1a73e8>作者：</font>** Gonzalo Mancera, Daniel DeAlcala, Aythami Morales 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present LoRA-MINT, a new methodology for Membership Inference Test (MINT) applied to recent Large Language Models (LLMs) fine-tuned for specific Natural Language Processing (NLP) tasks through Low-Rank Adaptation (LoRA). The primary goal is to assess whether individual samples were part of the training data of these adapted models, providing a useful auditing tool for the management of intellectual property and sensitive data. Our analysis explores the relationship between model perplexity and membership status, providing a systematic framework for estimating data exposure in fine-tuned LLMs. We conducted experiments on four models and three benchmark datasets, obtaining precision values in determining if given data were used for training ranging from 0.77 to 0.92, which outperform state-of-the-art baselines and demonstrate the robustness and generality of the proposed method. In general, our findings underscore the potential of LoRA-MINT as an effective and scalable framework for auditing LLMs, improving transparency, and fostering the ethical and responsible deployment of AI and NLP technologies. For the sake of concreteness and current relevance, our discussion and experiments are centered on LoRAadjusted LLMs, but note that most of the presented methodology is easily applicable for auditing training data given any other technique for adapting LLMs or, more generally, any other domain-adapted AI models.

---


### 63. [OpenHalDet: A Unified Benchmark for Hallucination Detection across Diverse Generation Scenarios](https://arxiv.org/abs/2606.06959)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Zhen Fang, Yongxin Deng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is essential for the reliable deployment of large language models (LLMs). However, existing evaluations face two core challenges: inconsistent inference configuration and evaluation, and limited coverage of downstream domains and tasks. Consequently, reported detector performance is often difficult to compare, reproduce, and generalize beyond specific experimental settings. We introduce OpenHalDet, a unified benchmark for hallucination detection across diverse generation scenarios. OpenHalDet standardizes the evaluation pipeline, from prompt construction and response generation to truthfulness annotation, detector scoring, and metric computation. It supports heterogeneous detector families under different access settings, including black-box methods that use only generated outputs, gray-box methods that rely on probability-based signals, and white-box methods that exploit internal model signals. By bringing diverse tasks, models, and detectors into a shared framework, OpenHalDet enables controlled comparison and provides a systematic view of how different detection paradigms behave in LLM applications. We release OpenHalDet as an open and extensible codebase to facilitate reproducible evaluation and future development of hallucination detection methods. The code and datasets are available at this https URL.

---


### 64. [From Vision to Text: A Compact Multimodal Approach for Robust, Cross-Domain Presentation Attack Detection on ID Cards](https://arxiv.org/abs/2606.06966)

**<font color=#1a73e8>作者：</font>** Qingwen Zeng, Juan E. Tapia, Sneha Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain shifts challenge Presentation Attack Detection (PAD) on ID Cards, given the restricted data available due to privacy concerns. This work proposes a compact multimodal model, based on new generative and discriminative blocks, which combines visual and textual data for PAD on genuine and synthetic ID images. While multimodal models exhibit strong generalisation after supervised fine-tuning, they fail in zero-shot settings. Our findings underscore that model capacity and real-world data are essential for reliable PAD, while existing synthetic datasets may not reflect real-world challenges. We argue for a re-evaluation of synthetic data as a benchmark and emphasise the need for more realistic, diverse datasets to advance PAD research.

---


### 65. [Accounting for Context: Shaping Moral Credences for Value Alignment](https://arxiv.org/abs/2606.06972)

**<font color=#1a73e8>作者：</font>** Jazon Szabo, Sanjay Modgil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring that agent behaviours are aligned with human moral values inevitably raises the problem of how to account for the plurality of moral perspectives that societies -- and even individuals -- typically adopt. Work on moral uncertainty proposes mechanisms to fairly and democratically aggregate evaluations of actions across different moral theories. However, this paper argues that one needs to account for contextual factors when aggregating moral evaluations. For example, consequentialist perspectives assume an ability to accurately determine how an agent's actions change the world; an assumption that often does not hold in real world settings. We, therefore, formalise agent decision making under moral uncertainty, while also accounting for these kinds of contextual factors. We thereby show that a seemingly commonsensical property -- the weak Pareto principle -- is violated. We argue that this apparent problem is, in fact, a variation of Simpson's paradox, and hence reveals the limitations of aggregation mechanisms that ignore the impact of contextual factors.

---


### 66. [Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning](https://arxiv.org/abs/2606.06976)

**<font color=#1a73e8>作者：</font>** Yijin Zhou, Linqian Zeng, Xiaoya Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents often make suboptimal tool-use decisions, including unsupported tool invocation and hallucinated direct responses, which may accumulate errors throughout multi-step interactions. Existing approaches mainly improve these behaviors through inference-time correction or coarse-grained reward signals based on decision outcomes and structured checklists, leaving the uncertainty characteristics of agent decisions underexplored. We observe that decision-oriented reinforcement learning tends to weaken the uncertainty separation between correct and incorrect actions, resulting in overconfident mistakes and weaker exploration signals. Therefore, we propose TRUST, which incorporates uncertainty quantification into reward design as a repulsive force for maintaining uncertainty separation, and labels lightweight key-turn annotations for unified post-training of multi-turn trajectories. Experimental results across diverse tool-use benchmarks show that TRUST consistently enhances both decision quality and agent performance while maintaining more reliable uncertainty estimates during optimization.

---


### 67. [Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition](https://arxiv.org/abs/2606.06985)

**<font color=#1a73e8>作者：</font>** Tung X. Nguyen, Hieu Minh Truong, Giang-Son Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-switching (CS), the alternation between multiple languages within a single utterance, remains challenging for Automatic Speech Recognition (ASR). To address this issue, we propose a Point-of-Interest (POI)-aware contrastive training framework that improves recognition at CS-critical regions. We first identify CS spans by adopting POI detection method from literature, then construct acoustically plausible near-miss hypotheses by perturbing POIs in ASR N-best outputs and expanding candidates with a large language model. Hard but plausible negatives are retained through filtering with acoustic, phonemic, and textual constraints. Finally, we fine-tune Whisper-small with LoRA using a POI-weighted cross-entropy anchor objective together with a multi-negative contrastive ranking loss. Experiments on CS-FLEURS (cmn-eng) and ViMedCSS (vie-eng) show consistent reductions of over 2% in both general and CS-aware error rates compared to standard LoRA fine-tuning.

---


### 68. [Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization](https://arxiv.org/abs/2606.07000)

**<font color=#1a73e8>作者：</font>** Shizhe Xiang, Ke An, Wenlong Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent post-training methods, particularly Reinforcement Learning with Verifiable Rewards (RLVR), have significantly enhanced the reasoning ability of Large Vision-Language Models (LVLMs). However, the sparse nature of verifiable rewards provides little token-level supervision for failed rollouts, often leading to inefficient exploration in complex multimodal reasoning tasks. Although policy distillation can offer dense guidance, external teacher based methods introduce substantial computational overhead, while answer conditioned tuning methods may expose answer-level information and induce shortcut-like generation behavior. To address these limitations, we propose PTD-PO, a Privileged Tutoring Distillation Policy Optimization framework for RLVR that provides dense guidance without exposing the answer to the student policy. Specifically, PTD-PO constructs structured privileged hints from spatial attention guidance and intermediate textual reasoning steps, and uses them through in-context learning to produce step-wise token-distribution supervision. The student is still optimized under the original answer-free context, and its failed rollouts are aligned with the hint-augmented reference model at the token-distribution level. To further stabilize distillation under the distribution shift between guided and unguided contexts, we introduce a Top-K Jensen-Shannon divergence objective that focuses alignment on informative token probabilities while reducing memory overhead. Experiments on LVLMs ranging from 2B to 8B parameters show that PTD-PO consistently outperforms RLVR and distillation baselines, mitigates entropy collapse, and improves complex multimodal reasoning performance.

---


### 69. [RASFT: Rollout-Adaptive Supervised Fine-Tuning for Reasoning](https://arxiv.org/abs/2606.07006)

**<font color=#1a73e8>作者：</font>** Yongliang Miao, Fengyuan Liu, Wei Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is a prevailing method for adapting large language models to reasoning tasks by imitating offline expert demonstrations, often treating a single expert trajectory as the target behavior. However, reasoning is not simple path imitation: rigidly following one demonstrated solution may overfit to surface forms and suppress the model's own reasoning distribution. We propose Rollout-Adaptive Supervised Fine-Tuning (RASFT), a policy-aware SFT framework that calibrates expert supervision according to problem-level solvability estimated from verified on-policy rollouts. For each problem, RASFT strengthens expert guidance when the current policy struggles, while relaxing rigid imitation and incorporating correct self-generated trajectories when the model already exhibits reliable reasoning behavior. To preserve useful reasoning priors, RASFT further introduces a clipped inverse ratio between the frozen reference model and the current policy to constrain excessive policy drift. Experiments across multiple models on six mathematical reasoning benchmarks and two code reasoning benchmarks show that RASFT achieves better overall performance than SFT, SFT variants, and representative RL methods. The code is available at this https URL.

---


### 70. [The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective](https://arxiv.org/abs/2606.07017)

**<font color=#1a73e8>作者：</font>** Xiaoou Liu, Tiejin Chen, Weibo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation model agents are increasingly deployed for real-world decision-making, but suffer from the sim-to-real gap. While robotics and classical control have mature frameworks to address this gap, the foundation model community is treating agent robustness as an entirely novel phenomenon. Our paper proposes formalizing the foundation model agent evaluation and training gap as a classical sim-to-real problem structured entirely around the four elements of a Markov Decision Process, including Observation, Action, Transition, and Reward. In this paper, we set a comprehensive research agenda that translates classical discrepancies into the foundation model domain and advocates for adopting established solutions like domain randomization. We provide concrete examples, such as a multilingual tool calling to demonstrate how severe observation space gaps lead to operationally invalid actions despite correct semantic intent. Ultimately, this agenda aims to drive a paradigm shift, yielding a unified vocabulary and standardized stress test benchmarks to foster a new generation of highly trustworthy agents for reliable real-world applications.

---


### 71. [MADE: Beyond Scoring via a Multilingual Agentic Diagnosing Engine for Fine-Grained Evaluation Insights](https://arxiv.org/abs/2606.07020)

**<font color=#1a73e8>作者：</font>** Yilun Liu, Miao Zhang, Shimin Tao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual and multicultural benchmarks now cover dozens of languages and model families, but the resulting score landscapes remain metric-rich and insight-poor, necessitating fine-grained multilingual post-evaluation diagnosis. However, single LLMs and open-ended agents are easily swamped by the long, noisy diagnostic input, and no reusable taxonomy exists for it. To address this, we propose MADE, a Multilingual Agentic Diagnosing Engine that decomposes post-evaluation analysis into planning, aggregate analysis, instance-level case inspection, multilingual and cultural reflection, and grounded report synthesis. MADE is paired with an expert-led 54-query and 15-language diagnostic set, evaluated on top of a large-scale multilingual evaluation substrate (33 model families, 11 benchmarks, 26 languages, 34 cultures, 8.66M evaluation records). Experiments show that MADE outperforms the strongest shared baseline by 47% in diagnosis report quality and is preferred by human multilingual experts in 87.9% of pairwise comparisons. Applied with multilingual experts, MADE further surfaces four actionable findings on deployment, iteration, and cross-cultural pitfalls, turning benchmark score tables into model-selection and remediation guidance.

---


### 72. [GuideCAD: A Lightweight Multimodal Framework for 3D CAD Model Generation via Prefix Embedding](https://arxiv.org/abs/2606.07024)

**<font color=#1a73e8>作者：</font>** Minseong Kim, Jinyeong Park, Sungho Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal approaches used for 3D CAD generation require substantial computational resources, necessitating efficient training. To address this, we propose GuideCAD, which leverages semantically rich visual-textual representations having only a small number of trainable parameters to generate 3D CAD models. Specifically, GuideCAD uses a mapping network that converts image embeddings into prefix embeddings, enabling a pretrained large language model to integrate visual and textual information. As a result, a transformer-based decoder predicts the construction sequence using the visual-textual embeddings in order to generate the 3D CAD model. For experimental evaluation, we construct a new dataset, referred to as GuideCAD, which consists of text-image pairs. Each pair includes a text prompt that represents a 3D CAD construction sequence and its corresponding 3D CAD image. Our experimental results show that GuideCAD generates comparably high-quality 3D CAD models while using approximately four times fewer parameters and achieving twice the training efficiency compared to fine-tuning approaches. We have released the source code and dataset for our method at: this https URL

---


### 73. [TRACE: Trajectory Reasoning through Adaptive Cross-Step Evidence Aggregation for LLM Agents](https://arxiv.org/abs/2606.07054)

**<font color=#1a73e8>作者：</font>** Vijitha Mittapalli, Shreyaa Jayant Dani, Satya Srujana Pilli 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents can pursue hidden malicious objectives through sequences of individually benign actions, making sabotage difficult to detect using standard trajectory-level monitoring. Existing approaches either evaluate complete trajectories in a single pass or partition them into independently scored windows, limiting their ability to connect evidence across temporally distant actions. We propose TRACE, a monitoring framework for long-horizon LLM agent trajectories. TRACE operates through a TIJ (Triage-Inspect-Judge) loop that identifies high-signal regions, performs targeted inspection while maintaining accumulated evidence across reasoning steps, and synthesizes a trajectory-level verdict. We evaluate TRACE on ten task domains from SHADE-Arena against state-of-the-art baselines. TRACE achieves an aggregate F1 of 0.713 and recall of 0.844, with the largest gains on tasks requiring long-range evidence linking.

---


### 74. [Modeling semantic association in self-paced reading with language model embeddings](https://arxiv.org/abs/2606.07066)

**<font color=#1a73e8>作者：</font>** Sara Møller Østergaard, Kenneth Enevoldsen, Afra Alishahi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic association between a word and its context has been identified as an important component of reading comprehension, even when word predictability is accounted for. Recent research has highlighted the potential of language model ( LM) embeddings to quantify semantic association. Yet, embedding-based semantic association have been operationalized in a myriad of ways. In this study, we use embeddings from LMs to estimate semantic association on a corpus of joint electroencephalography (EEG) and self-paced reading of natural, Dutch texts. Semantic association is calculated in ten different implementations that vary the embedding model and context lengths. The effects of semantic association across the different implementations on the N400 and self-paced reading times are examined using Bayesian hierarchical models and Bayes factor. The results show that the choice of embedding model can alter the estimated effect of semantic association on both the N400 and self-paced reading times. Furthermore, the results demonstrate a promising potential of sentence embeddings for capturing semantic association, as only implementations relying on sentence embeddings indicate reliable results of semantic association beyond word predictability on both neural and behavioral measures. Together, these findings highlight the importance of methodological choices in quantifying semantic association.

---


### 75. [mmPISA-bench: Do LLMs Reason Equally Well Across 43 Languages?](https://arxiv.org/abs/2606.07069)

**<font color=#1a73e8>作者：</font>** Yerzhan Sapenov, Jaromir Savelka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce mmPISA-bench, a compact high-quality multilingual reasoning benchmark derived from the OECD Programme for International Student Assessment (PISA). The benchmark consists of 25 multiple-choice questions that require reasoning in order to be answered correctly. Each question is provided in official human translations to 43 languages and complemented with machine-translated counterparts (i.e., 2,150 data points in total). We evaluate two mainstream proprietary LLMs across languages, reasoning effort levels, and translation types in terms of their ability to answer the questions correctly. Our results show that modern LLMs can reason effectively across all evaluated languages, achieve accuracy comparable to human test-takers, with some performance variations across covered languages. We further find that machine-translated questions do not degrade accuracy relative to official human translations which suggests that high-quality machine translation (synthetic data) might often be adequate for large-scale multilingual reasoning evaluations where official translations are not available. Finally, we analyze token usage and related inference cost and find that LLMs usage in some languages is simultaneously more expensive and less accurate.

---


### 76. [On the Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.07082)

**<font color=#1a73e8>作者：</font>** Zhennan Shen, Yanshu Li, Qingyu Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is increasingly used to improve large language model reasoning, but its training dynamics remain poorly understood. We characterize the trajectory of OPD updates in parameter space and compare it with supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). A suite of parameter-space diagnostics consistently places OPD in a relaxed off-principal regime: compared with SFT, its updates affect fewer weights and avoid principal directions more strongly, while compared with RLVR, they remain less tightly constrained. Beyond this static localization, OPD exhibits subspace locking: its cumulative updates rapidly enter a narrow low-dimensional channel. Constraining training to the update subspace formed early in training preserves OPD performance but substantially degrades SFT, indicating that the locked subspace is functionally sufficient for OPD. Control experiments further show that sparsifying the update tokens and shifting rollout generation off-policy preserve the rank dynamics, whereas mixing the OPD objective with RLVR changes them. Overall, these results suggest that OPD is not merely an intermediate point between SFT and RLVR, but induces its own update geometry in parameter space.

---


### 77. [SigmaScale: LLM Compression with SVD-based Low-Rank Decomposition and Learned Scaling Matrices](https://arxiv.org/abs/2606.07098)

**<font color=#1a73e8>作者：</font>** Ernests Lavrinovics, Marco Letizia, Roy Janco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SigmaScale, a method for learning auxiliary scaling matrices $S$ to aid truncated Singular Value Decomposition (SVD) based Large Language Model (LLM) compression. Instead of deriving scaling matrices analytically, SigmaScale optimizes two sets of vectors that define diagonal row and column scaling transformations under an activation-aware compression loss. We show that learned scaling lowers the effective intrinsic rank of weight matrices, as reflected by reductions in effective-rank entropy, and that this reduction is strongly correlated with compression loss. Experiments on Llama 3.1 8B Instruct and Qwen3-8B show that SigmaScale is competitive with closely related state-of-the-art SVD-based compression methods across perplexity and zero-shot benchmarks. By using learned activation-aware transformations, SigmaScale explores a more flexible route to low-rank LLM compression by adapting to the structure of individual model weights. The advantage observed in specific tasks makes our approach a valid option for applications requiring a reduced LLM-inference computing cost.

---


### 78. [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100)

**<font color=#1a73e8>作者：</font>** Mengya Liu, Baoxiong Jia, Jiangyong Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes, while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world robotic manipulation benchmarks.

---


### 79. [GP-Adapter: Gaussian Process CLIP-Adapter for Few-Shot Out-of-Distribution Detection](https://arxiv.org/abs/2606.07102)

**<font color=#1a73e8>作者：</font>** Taisei Saito, Koretaka Ogata, Takafumi Hiroi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose GP-Adapter, a training-free framework that augments CLIP (Contrastive Language-Image Pre-training) with Gaussian Process (GP) uncertainty modeling for few-shot classification and out-of-distribution (OOD) detection. While CLIP achieves strong zero-shot recognition, it yields deterministic similarity scores and offers limited uncertainty information, which is critical under distribution shift and data scarcity. GP-Adapter constructs modality-specific, class-wise one-class GPs on top of frozen CLIP embeddings using an RBF kernel for image features and a linear kernel for text prompts and fuses their predictive statistics to produce a variance-aware confidence score for OOD detection. The method requires no fine-tuning of the CLIP backbone and relies only on a small $K$-shot cache and lightweight hyperparameter selection, with memory cost scaling as $O(CK^2)$ for $C$ classes and $K$ shots. Experiments on ImageNet and multiple OOD benchmarks show that GP-Adapter provides competitive few-shot performance and consistently improves OOD detection when combined with prompt-learning baselines, highlighting the complementarity between GP-based uncertainty modeling and prompt learning. Overall, our results suggest that integrating probabilistic inference with large pre-trained vision-language models can improve reliability in low-data and distribution-shifted settings. Code is available at this https URL

---


### 80. [OffQ: Taming Structured Outliers in LLM Quantization by Offsetting](https://arxiv.org/abs/2606.07116)

**<font color=#1a73e8>作者：</font>** Haoqi Wang, Lorenz K. Mueller, Jiawei Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization has been widely adopted to accelerate the inference of large language models (LLMs) by significantly reducing computational cost and memory usage. However, activation outliers pose a major challenge to effective quantization, often leading to notable performance degradation. In this paper, we introduce OffQ, a method designed to mitigate activation outliers in low-bit quantization through a novel offsetting mechanism. Specifically, OffQ first identifies a low-dimensional outlier subspace in the activations using a proposed top-1 PCA, and then concentrates high-magnitude activations into 1 channel via rotation. OffQ then absorbs this concentrated outlier channel by converting its magnitude into a shared offset, thereby reducing the standard deviation of the activations. This offsetting strategy enables effective W4A4KV4 quantization of LLMs using deployment-friendly uniform-grid and uniform-precision quantization. Extensive experiments across diverse LLM architectures and benchmarks demonstrate that OffQ outperforms state-of-the-art baselines, consistently improving model accuracy while preserving low-bit efficiency.

---


### 81. [Native3D: End-to-End 3D Scene Generation via Unified Mesh-Texture Modeling and Semantic Alignment](https://arxiv.org/abs/2606.07117)

**<font color=#1a73e8>作者：</font>** Yibo Liu, Ziwei Zhang, Haozhou Pang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents Native3D, the first end-to-end 3D scene generation framework that completely bypasses 2D intermediate representations. Traditional approaches typically require adapting 3D representations to the 2D domain to leverage pre-trained diffusion models, which inevitably introduces domain adaptation issues including geometric structural distortion and texture detail degradation. To address these limitations, we design a unified mesh-texture joint representation that simultaneously models both geometric structures and texture features through a Transformer-based scene encoder, effectively maintaining spatial relationships and visual consistency among objects within scenes. We further propose the 3D Representation Alignment Loss (3D REPA Loss), which employs an improved contrastive learning mechanism to align multi-level semantic representations in the latent space, significantly enhancing geometric and textural fidelity. Experimental results demonstrate that Native3D outperforms existing methods in both generation quality and editing flexibility, providing a novel solution for 3D scene editing.

---


### 82. [$α$-PFN: Fast Entropy Search via In-Context Learning](https://arxiv.org/abs/2606.07134)

**<font color=#1a73e8>作者：</font>** Herilalaina Rakotoarison, Steven Adriaensen, Tom Viering 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information-theoretic acquisition functions such as Entropy Search (ES) offer a principled exploration-exploitation framework for Bayesian optimization (BO). However, their practical implementation relies on complicated and slow approximations, i.e., a Monte Carlo estimation of the information gain. This complexity can introduce numerical errors and requires specialized, hand-crafted implementations. We propose a two-stage amortization strategy that learns to approximate entropy search-based acquisition functions using Prior-data Fitted Networks (PFNs) in a single forward pass. A first PFN is trained to be conditioned on information about the optima; second, the $\alpha$-PFN is trained to predict the expected information gain by training on information gains measured with the first PFN. The $\alpha$-PFN offers a flexible learned approximation, which replaces the complex heuristic approximations with a single forward pass per candidate, enabling rapid and extensible acquisition evaluation. Empirically, our approach is competitive with state-of-the-art entropy search implementations on synthetic and real-world benchmarks, while accelerating the different entropy search variants across all our experiments, with speed ups over 50x. Source code: this https URL.

---


### 83. [TraRA: Trajectory-level Recognition Aggregation for Video Text Spotting in Urban Surveillance](https://arxiv.org/abs/2606.07161)

**<font color=#1a73e8>作者：</font>** Duc Tri Tran, Trung Thanh Nguyen, Vijay John 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Text Spotting (VTS) is essential for urban surveillance and intelligent transportation systems, enabling automated reading of street signs, vehicle markings, and scene text in video streams. However, reliable recognition remains challenging due to dynamic video factors common in surveillance scenarios, including motion blur, occlusion, and scale variation, which degrade frame-level recognition. Existing VTS methods typically perform recognition independently on each frame, leading to inconsistent and inaccurate results across sequences. To address these limitations, we propose TraRA (Trajectory-level Recognition Aggregation for VTS), a plug-and-play method that performs trajectory-level text recognition by leveraging temporal and multimodal consistency. TraRA integrates two key modules: (1) the Temporal Clustering and (2) the Vision-Language Aggregation. The former refines noisy trajectories by grouping temporally and visually coherent text instances, while the latter employs a Low-Rank Adaptation-enhanced Vision-Language model to fuse visual cues with linguistic context across frames. By aggregating information over entire text trajectories, TraRA achieves robust text recognition even under challenging surveillance conditions. Extensive experiments on four public benchmarks, including road and urban scene datasets (RoadText, BOVText, ArTVideo, and ICDAR15), demonstrate that TraRA consistently improves tracking and recognition performance over state-of-the-art VTS methods. The source code is available at this https URL.

---


### 84. [When Recovery Matters: The Blind Spot of Surrogate Privacy in MLLM Editing](https://arxiv.org/abs/2606.07171)

**<font color=#1a73e8>作者：</font>** Siyuan Xu, Yibing Liu, Peilin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) enable flexible instruction-driven image editing, but privacy risks arise when user images expose diverse and user-specific private content. Canonical privacy protection strategies typically substitute sensitive regions with surrogate content before cloud editing. Yet, the resulting output is often an edited surrogate rather than the desired edited source image, neglecting the local recovery in both design and evaluation scope. To this end, we introduce SPPE (Surrogate-based Privacy-Preserving Editing), the first recovery-oriented benchmark covering 36 fine-grained privacy categories and 65 editing instructions. It defines two complementary tasks: 1) editability assessment, which estimates before cloud interaction whether a surrogate can induce an edit consistent with the original image; and 2) surrogate-to-source edit recovery, which evaluates whether the edited surrogate can be transferred back to the private source with the edit effect preserved. We address each task with a dedicated method: ERMA predicts surrogate editability through instruction-aware multimodal relation modeling, while \method performs cycle-consistent recovery by using the surrogate editing pair as visual edit evidence and the source image as a source-preserving anchor. Experiments on SPPE and InstructPix2Pix show consistent improvements on both tasks. For editability assessment, ERMA improves over the best-performing baselines by 13.9% in SRCC and 12.3% in PLCC. For surrogate-to-source edit recovery, C2E-S2SER outperforms SOER across all 8 source integrity and edit consistency metrics on SPPE.

---


### 85. [Textual Supervision Enhances Geospatial Representations in Vision-Language Models](https://arxiv.org/abs/2606.07172)

**<font color=#1a73e8>作者：</font>** Marcelo Sartori Locatelli, Fernando Tonucci, Jea Kwon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial understanding is a critical yet underexplored dimension in the development of machine learning systems for tasks such as image geolocation and spatial reasoning. In this work, we analyze the geospatial representations acquired by three model families: vision-only architectures (e.g., ViT), vision-language models (e.g., CLIP), and large-scale multimodal foundation models (e.g., LLaVA, Qwen, and Gemma). By evaluating across image clusters, including people, landmarks, and everyday objects, grouped based on the degree of localizability, we reveal systematic gaps in spatial accuracy and show that textual supervision enhances the learning of geospatial representations. Our findings suggest the role of language as an effective complementary modality for encoding spatial context and multimodal learning as a key direction for advancing geospatial AI.

---


### 86. [Seeing Without Exposing: Adaptive Privacy Control for Open-World, Context-Hungry MLLMs](https://arxiv.org/abs/2606.07175)

**<font color=#1a73e8>作者：</font>** Siyuan Xu, Yibing Liu, Peilin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have raised new privacy challenges. On the data side, user-provided inputs often include unpredictable sensitive information; while on the downstream task side, model reasoning depends on rich visual context that may itself be privacy-sensitive. Existing privacy protection methods, however, rely on predefined sensitive categories and fixed obfuscation strategies, struggling to tackle such challenges in MLLMs. To address this dilemma, we propose Anchored Privacy Drifting (APD), a training-free method that drifts privacy-sensitive elements toward semantically equivalent alternatives while anchoring contextual cues to the source image. To systematically evaluate this dual objective of privacy protection and contextual preservation, we introduce AdaptShield, a comprehensive benchmark covering 22 privacy categories, which combines conventional privacy metrics with MLLM-based assessments of contextual utility. Extensive experiments show that our method achieves balanced improvements in both privacy sanitization and content retention, with average gains of 10.4% on textual categories and 8.5% under MLLM-based evaluation across four MLLM series, i.e., Qwen2.5, Qwen3, InternVL3, and InternVL3.5.

---


### 87. [From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning](https://arxiv.org/abs/2606.07190)

**<font color=#1a73e8>作者：</font>** Yuhang Zhou, Yixin Cao, Guangnan Ye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning prefixes shape the future trajectory of LLM problem solving, yet existing process reward models usually evaluate them through local step correctness. We argue that correctness is a useful but indirect proxy for the effect we ultimately care about: whether a prefix increases the probability of successful completion. We define this effect as prefix gain, the solve-rate improvement induced by conditioning lightweight student model group on a prefix, and use it to train a Prefix Utility Model (PUM) with a simple pairwise ranking objective. PUM learns outcome-grounded prefix utility and can score both complete trajectories and partial reasoning prefixes. Across Best-of-$N$ selection, beam search, and reinforcement learning on mathematical reasoning, PUM provides a strong prefix-level supervision signal, especially when candidate pools are large, search budgets increase, or rule-based rewards are sparse. We release all data, models, and code at this https URL.

---


### 88. [Moodie: An Early-Stage Design Exploration for Supporting Fear of Missing Out with LLM-based Chatbots](https://arxiv.org/abs/2606.07231)

**<font color=#1a73e8>作者：</font>** Hsin-Yu Tsai, Jingxian Liao, Fu-Yin Cherng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The excessive use of social media has led to the challenge known as Fear of Missing Out (FoMO). Existing studies fail to provide accessible, interactive tools that focus on the emotional and cognitive aspects of FoMO. This work presents Moodie, a chatbot designed using Large Language Models to support emotion regulation and reduce FoMO. We conducted a formative study to understand the needs of individuals with FoMO and developed Moodie. Then, we conducted a preliminary evaluative study (N=21) to observe how participants interact with Moodie and a baseline chatbot (GPT-4o) over one week. The results show that while both Moodie and a baseline chatbot reduced FoMO to a similar extent, Moodie resulted in greater engagement and social connection. This finding raises interesting questions about the advantages of purpose-built chatbots compared to general-purpose models for mental health support. Future research will include chat log analysis, prototype refinements, and longitudinal evaluations.

---


### 89. [When Large Language Models Fail in Healthcare: Evaluating Sensitivity to Prompt Variations](https://arxiv.org/abs/2606.07237)

**<font color=#1a73e8>作者：</font>** Mahdi Alkaeed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in healthcare for tasks such as clinical question answering, diagnosis support, and report summarization. Despite their promise, these models remain highly sensitive to subtle prompt perturbations, both lexical and syntactic, posing serious risks in safety-critical clinical applications. In this study, we conduct a systematic sensitivity analysis to evaluate the robustness of both general-purpose (e.g., GPT-3.5, Llama3) and medical-specific LLMs (e.g., ClinicalBERT, BioLlama3, BioBERT) using the MedMCQA benchmark. We categorize perturbations into natural and adversarial types and examine their effect on model consistency, accuracy, and reliability in clinical reasoning tasks. Our findings reveal that medical LLMs are not intrinsically safe. Even minor variations in phrasing can alter clinical advice, and targeted adversarial prompts can provoke harmful outputs. In high-stakes settings like healthcare, such unpredictability is unacceptable-models that change diagnoses due to reworded inputs or hallucinate medications when slightly rephrased cannot be reliably trusted by clinicians. While models tend to show resilience to simple lexical substitutions or paraphrasing, they often break down under syntactic reordering or misleading contextual cues. This fragility is evident across both general-purpose and domain-specific LLMs. Notably, adversarial manipulations can lead to clinically dangerous outputs, such as recommending incorrect dosages or omitting critical findings.

---


### 90. [Phun-Bench: Evaluating LLMs on Phonological Understanding in Chinese](https://arxiv.org/abs/2606.07300)

**<font color=#1a73e8>作者：</font>** Xing Yue, Yongliang Shen, Weiming Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language is a vehicle for thought, intricately tied to sounds, symbols, and meaning. However, most large language model (LLM) research focuses on meaning (semantics) and symbols (spelling) while largely overlooking sounds. Existing benchmarks on LLMs' phonological abilities are either solvable through rote memorization or intertwined with other abilities, making them inadequate to measure LLMs' genuine ability in phonological understanding. Here, we present Phun-Bench, a purpose-built Chinese benchmark with diverse tasks and settings across three dimensions (Homophony, Rhyme, and Phonetic Similarity), designed to systematically evaluate LLMs' phonological understanding. Our results show that while LLMs excel at recalling correct pronunciations, they generally struggle to leverage phonological knowledge in the flexible and intuitive way that human speakers do. Moreover, through detailed analyses, we propose a hypothesis regarding the underlying mechanism of LLMs' phonological understanding and "perception", highlighting an underexplored frontier for future research.

---


### 91. [Bootstrap Theory of Representational Emergence: Explanatory Insufficiency as a Driver of Representation Learning and World Models](https://arxiv.org/abs/2606.07303)

**<font color=#1a73e8>作者：</font>** Jacques Raynal, Pierre Slangen, Elsa Raynal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning is central to modern machine learning, enabling transitions from handcrafted features to learned embeddings, latent spaces, foundation models, world models, and digital twins. Yet most research examines how representations are optimized after a representational framework has been selected, while less attention is given to when a new level of representation becomes necessary. We introduce the Bootstrap Theory of Representational Emergence (TBER), a framework describing how new representations arise when existing ones become explanatorily insufficient. In this view, representational innovation is not only driven by more data, larger models, or greater computational power, but also by persistent explanatory gaps: situations in which a representation can still describe observations but can no longer make their organization or transformations intelligible. TBER identifies explanatory insufficiency as a positive signal for representational transition. A representation becomes insufficient not because it is necessarily false, but because its explanatory domain has been exceeded. The bootstrap dynamic follows a recursive sequence: observations reveal anomalies; anomalies expose insufficiencies; insufficiencies motivate new representations; and these new representations generate further observations and possible new this http URL formalize this process through five stages: stabilized observation, anomaly detection, recognition of explanatory insufficiency, representational emergence, and provisional stabilization. We discuss applications to representation learning, latent spaces, foundation models, world models, digital twins, adaptive biological systems, and scientific discovery. TBER suggests that future AI systems may benefit from mechanisms for detecting the explanatory limits of their own internal representations.

---


### 92. [Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration](https://arxiv.org/abs/2606.07316)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Lei Zhang, Iadh Ounis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Byzantine collaboration among large-language-model agents requires a finality-control primitive: given delivered stochastic, structured natural-language proposals, the protocol must decide whether the round supports a commit, what kind of commit, or a typed safe abort. Naive aggregation hides this choice behind a single verdict; classical Byzantine fault tolerance hides it behind byte-identity that LLM proposals do not satisfy. We introduce Hierarchical Certified Semantic Commitment (H-CSC), a BFT-inspired protocol that converts embedding-derived finality signals over verdict-conditioned proposal groups into one of three typed outcomes: a semantic_commit (a 2f+1 within-verdict semantic core backs the verdict, emitting a parameter-bound digest over the quantised aggregate), a verdict_commit (strong verdict margin but dispersed semantic rationale, emitting a verdict-level certificate without claiming a semantic aggregate), or an explicit abort with a typed reason. The contribution is typed finality, not raw commit accuracy. On a controlled semantic-poisoning diagnostic (BCS_v1, 120 episodes), H-CSC commits with low angular deviation on BFT-feasible buckets (0.31 to 2.04 degrees) and aborts 100% of beyond-BFT rounds (n<3f+1) as intended. On a real LLM-agent claim-verification benchmark (MVR-50, 50 tasks) under paired static and rushing Byzantine attacks, H-CSC commits 0.90/0.92 with honest-reference-invalid rates of 0.02/0.00, statistically matching a strong certificate-emitting verdict-only baseline. Unlike that baseline, H-CSC also emits an embedding-backed semantic_commit digest on 74%/72% of rounds, supplying typed provenance. A strict-semantic ablation commits only 0.54/0.48, showing the verdict-level fallback is necessary for coverage (+0.36/+0.44) at the same <=0.04 safety floor; a 100-task cross-model check across four LLMs preserves invalid_hmaj within 0.00 to 0.03.

---


### 93. [LLM-Guided Evolution for Medical Decision Pipelines](https://arxiv.org/abs/2606.07342)

**<font color=#1a73e8>作者：</font>** Ivan Sviridov, Artem Oskin, Ivan Panin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to clinical workflows often requires costly fine-tuning or manual prompt and pipeline engineering. We study LLM-guided MAP-Elites evolution as an inference-time alternative for discovering medical decision strategies and provide an implementation repository at this https URL. We formulate urgency triage, interactive consultation, and medical image classification as evolutionary searches over executable artifacts optimized by task-specific fitness functions.
Across all three settings, evolution improves over manually designed baselines under practical constraints. In triage, evolved programs increase Semigran accuracy from $77.3\%$ to $87.1\%$ and emergency recall from $0.60$ to $0.97$, while improving safety-weighted held-out MIMIC-ESI performance. In interactive consultation, evolved policies improve the accuracy--cost frontier across Llama-3, Qwen-3.5, and Gemma-4 and transfer to held-out iCRAFTMD. In PneumoniaMNIST, prompt-only evolution improves frozen MedGemma VLMs while preserving strict JSON outputs. Qualitative analysis shows that the gains come from interpretable program-level mechanisms, calibrated triage boundaries, targeted evidence acquisition, selective commitment, and finding-oriented visual decision rules, rather than superficial prompt rewording alone.

---


### 94. [TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention](https://arxiv.org/abs/2606.07345)

**<font color=#1a73e8>作者：</font>** Si-Yang Liu, Han-Jia Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models, exemplified by TabPFN, perform prediction via in-context learning, inferring test labels directly from labeled training examples. They have demonstrated competitive performance, particularly on small-to-medium datasets. However, recent tabular foundation models often improve accuracy with increasingly complex architectures, incurring higher inference cost and limiting practical deployment. In this work, we revisit the original TabPFN design and show that a lightweight row-wise attention-only backbone can remain highly competitive with two simple enhancements: a gated attention stabilization mechanism and a small set of learnable register tokens that provide global context and improve pretraining quality. The resulting model, TabSwift, supports both classification and regression, and is competitive with stronger tabular foundation models (e.g., TabPFN v2 and TabICL) while being more efficient at inference. For latency-sensitive serving, we further introduce an adaptive layer-wise early-exit mechanism that dynamically adjusts inference depth per sample. Overall, TabSwift enables efficient and anytime tabular in-context learning for practical deployments.

---


### 95. [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://arxiv.org/abs/2606.07362)

**<font color=#1a73e8>作者：</font>** Huzaifa Shaaban Kabakibo, Animesh Trivedi, Lin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As scalable inference services become popular, the cold start latency of an inference engine becomes important. Today, vLLM has evolved into the de facto inference engine of choice for many inference workloads. Although popular, due to its complexity and rapid evolution, there has not been a systematic study of its startup latency. With major architectural innovations such as the V1 API and the introduction of this http URL, this paper presents the first detailed performance characterization of vLLM startup latency. We break down the startup process into six foundational steps and demonstrate that it is predominantly CPU bound. Each step exhibits consistent and interpretable scaling trends with respect to model-level and system-level parameters, enabling fine-grained attribution of latency sources. Building on these insights, we develop a lightweight analytical model that accurately predicts vLLM startup latency for a given hardware configuration, providing actionable guidance for resource planning in large-scale inference environments. All benchmarking datasets, analysis tools, and prediction scripts are open sourced at this https URL.

---


### 96. [A robust PPG foundation model using multimodal physiological supervision](https://arxiv.org/abs/2606.07365)

**<font color=#1a73e8>作者：</font>** Eloy Geenjaar, Vince Calhoun, Scott Daly 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG), a non-invasive measure of changes in blood volume, is widely used in both wearable devices and clinical settings. Recent PPG foundation models either use open-source ICU datasets with pretraining paradigms that require curated data and thus complicate generalization to field-like data, or use closed-source field-like PPG data. In contrast, we propose a PPG foundation model that does not require high-quality or field-like pretraining data, and instead leverages accompanying electrocardiogram and respiratory signals in ICU datasets to select contrastive samples during pretraining. Our approach allows the model to retain and learn from noisy PPG segments, improving robustness at inference. Our model, pretrained on 3x fewer subjects than existing state-of-the-art approaches, achieves performance improvements on 14 out of 15 diverse downstream tasks, including field-like daily activity and heart rate prediction. Our results demonstrate that multimodal supervision can integrate complementary physiological information to improve the robustness of PPG foundation models and enhance their generalization to consumer-grade data.

---


### 97. [Self-evolving LLM agents with in-distribution Optimization](https://arxiv.org/abs/2606.07367)

**<font color=#1a73e8>作者：</font>** Yudi Zhang, Meng Fang, Zhenfang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently emerged as powerful controllers for interactive agents in complex environments, yet training them to perform reliable long-horizon decision making remains a fundamental challenge. A key difficulty lies in credit assignment: agents often receive delayed rewards only at the end of episodes. In this paper, we propose Q-Evolve, a self-evolving framework for LLM agents that unifies automatic process-reward labeling and policy learning within a principled in-distribution reinforcement learning paradigm. In each evolving iteration, our method learns an in-distribution critic from a hybrid off-policy dataset that combines expert demonstrations with agent-generated trajectories, stabilizing Bellman backups in sparse-reward settings via a weighted Implicit Q-Learning objective. The learned value function is then used to derive step-wise process rewards through advantage estimation, enabling dense and reliable supervision without environment backtracking or human annotation. Leveraging these signals, we perform behavior-proximal policy optimization that evolves the agent over the data used for process reward labeling, allowing iterative self-improvement without exacerbating distribution shift. We evaluate our method on AlfWorld, WebShop, and ScienceWorld, showing Q-Evolve outperforms strong baselines in sample efficiency, robustness, and overall task performance. Our results demonstrate that stable agent self-evolution is achievable through the co-evolution of process-level supervision and policy, both grounded within a shared in-distribution learning loop.

---


### 98. [Online Pandora's Box for Contextual LLM Cascading](https://arxiv.org/abs/2606.07392)

**<font color=#1a73e8>作者：</font>** Alexandre Belloni, Yan Chen, Yehua Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motivated by Large Language Model (LLM) cascading, we propose an online contextual Pandora's Box model for adaptively querying and selecting LLM APIs. In each period, a decision-maker observes a request context and faces a two-phase decision problem. In the query phase, the decision-maker sequentially queries APIs, where each query reveals a generated output and the decision-maker incurs an (output-dependent) cost. In the selection phase, the decision-maker selects one of the generated outputs to deploy and observes only the downstream reward of the deployed output. This output-mediated feedback structure differs from classical online contextual Pandora's Box models, in which opening a box directly reveals its reward.
Rather than estimating the full conditional output and cost distributions of each API, we directly model the reservation index and develop a learning approach for the query phase. Specifically, we impose a parametric structure on the contextual reservation index functions induced by the classical Weitzman's policy. Our policy combines generalized method of moments (GMM) type estimation of these reservation indices with UCB-style confidence bounds for both these indices and the shared output-level reward evaluator. Under regularity conditions, we prove that the resulting policy achieves dimension-dependent $\widetilde O(\sqrt T)$ cumulative regret over a horizon of $T$ periods.

---


### 99. [M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions](https://arxiv.org/abs/2606.07402)

**<font color=#1a73e8>作者：</font>** Zhengjun Huang, Wenxuan Liu, Zhoujin Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents are increasingly deployed over accumulating multimodal information, yet existing benchmarks assume a human-human form with sparse visuals and straightforward content, evaluating neither reasoning over authentic multimodal file interaction nor the interpretation of concealed user information. We therefore introduce M$^3$Exam, a query-centric multimodal conversational memory benchmark built on realistic user-agent interaction, with multi-dimensional evaluation spanning cross-modal grounding and implicit information inference. Benchmarking MLLMs and memory systems reveals persistent gaps in cross-modal grounding, cross session reasoning, and the efficiency cost of accumulating multimodal context. We further propose M$^3$Proctor, a multimodal memory method that detects query modality bias and consumes raw visual sources only on demand, improving accuracy by 13% while cutting index-construction time and retrieved tokens by over 70%.

---


### 100. [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404)

**<font color=#1a73e8>作者：</font>** Rohan Shravan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper reports on training a hundred-billion-parameter sparse mixture of experts on a single eight-GPU node, end to end. LightningLM 0.1V is a recurrence-backbone language model family grown in four stages from a small dense seed, through a 5B and a 9B mixture of experts, to a 120B model with 460 routed experts under top-12 routing. Each larger model is grown from the trained weights of the smaller one; active parameters rise monotonically from 1.78B at the dense seed to 5.93B at 120B (about 5% of the 118.67B stored). The full lineage runs on single nodes, the larger stages at 8K context, reaching a released training loss of 1.78 at 120B scale.
This is a systems and experience report. It is organized around three disciplines. Reversibility: a reversible recurrence stack reconstructs activations in the backward pass instead of storing them, holding activation memory flat as the model grows. State-preserving growth: each expansion (dense to MoE, shallow to deep, few experts to many) is given as a reproducible principle paired with the failure that results from getting it wrong; several failures are silent. Single-node economics: the 120B trains through TQP, a strategy of quantized base expert weights and trained low-rank adapters that carries optimizer state on 2.26B adapter parameters rather than 100B+ resident in routed experts, cutting expert-path optimizer state by a factor of ~45.
What is new is the integration of known primitives, not any primitive in isolation: one grown lineage running end to end on a single node, documented at practitioner level, with per-domain held-out loss as evidence that targeted capabilities (multilingual Indic competence, code) were learned by construction. Model family, tokenizer, and training code are released.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-114](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
