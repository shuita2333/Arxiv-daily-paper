# 🧠 大模型相关研究 | 2026年06月13日

> 本类共 **128** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-128](./part-03.md)

---

### 1. [ToolSense: A Diagnostic Framework for Auditing Parametric Tool Knowledge in LLMs](https://arxiv.org/abs/2606.12451)

**<font color=#1a73e8>作者：</font>** Ashutosh Hathidara, Sai Shruthi Sistla, Sebastian Schreiber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models deployed as agents over large tool catalogs face a critical tool-retrieval bottleneck. As embedding-based retrieval approaches rely on compact encoders that may under-capture specialized tool semantics, parametric tool retrieval addresses this by encoding each tool as a virtual token appended to the LLM vocabulary, fine-tuned in two stages (memorization then retrieval SFT) to use the LLM as a retriever, achieving strong performance on standard ToolBench retrieval benchmarks. Yet these benchmarks use verbose, fully-specified queries, and their evaluation applies constrained decoding that restricts outputs to valid token paths, neither reveals whether the model actually understands its tools. We introduce \textbf{ToolSense}, an open-source LLM-powered diagnostic framework that takes any tool catalog as input and automatically generates three benchmarks: a Realistic Retrieval Benchmark (RRB) with queries at three ambiguity tiers, an MCQ probing benchmark, and a QA probing benchmark. Applying ToolSense to ToolBench (~47k tools) and evaluating five parametric model training configurations reveals a knowledge-retrieval dissociation: on RRB queries, several configurations collapse by ~50-64 percentage points compared to fully-specified ToolBench benchmarks, falling below the embedding-model baseline. Additionally, despite strong retrieval performance, some models score near-random on factual probes, suggesting a knowledge-retrieval dissociation. We open-source the ToolSense framework and the ToolBench diagnostic benchmarks at this https URL.

---


### 2. [SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems](https://arxiv.org/abs/2606.12474)

**<font color=#1a73e8>作者：</font>** Ruxue Shi, Yili Wang, Mengnan Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) solve complex tasks through inter-agent collaboration, but their communication-driven nature also allows security risks to spread across agents and trigger system-wide failures. Existing MAS defenses mainly follow a reactive paradigm after execution by detecting and isolating harmful agents, which may cause irreversible damage and degrade collaborative utility. To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard). SAIGuard performs communication-state simulation over the MAS interaction graph, estimates the impact of incoming messages on local agent states and the global MAS state, and detects risky messages via reconstruction deviations from benign communication patterns. Instead of isolating agents, SAIGuard sanitizes or regenerates suspicious messages before it propagation into system. Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.

---


### 3. [ReCal: Reward Calibration for RL-based LLM Routing](https://arxiv.org/abs/2606.12479)

**<font color=#1a73e8>作者：</font>** Qihang Yu, Hanwen Tong, Zhengqi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing has emerged as an effective paradigm for leveraging the complementary strengths of multiple LLMs through dynamic model and reasoning-strategy selection. Recent reinforcement learning (RL)-based routing methods further improve routing quality by optimizing routing policies from interaction feedback. However, they still struggle to provide informative and comparable learning signals under heterogeneous tasks with varying difficulty. In practice, multiple objectives (e.g., correctness, format behavior) are aggregated into a single scalar reward, leading to ambiguous credit assignment and conflicting optimization signals. Moreover, reward signals exhibit significant variability across instances, where some instances produce higher or more variable rewards, introducing optimization bias that favors trivial samples over informative ones. To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing. We first introduce a hierarchical reward decomposition mechanism with component-wise advantage estimation. We further propose a distribution-aware optimization strategy that calibrates optimization variability through variance-aware reweighting and per-dataset normalization. Experiments on seven datasets demonstrate that ReCal consistently improves routing performance, and training stability over baselines. Code is available at this https URL.

---


### 4. [Representing Time Series as Structured Programs for LLM Reasoning](https://arxiv.org/abs/2606.12481)

**<font color=#1a73e8>作者：</font>** Jaeho Kim, Changhun Oh, Seokhyun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong reasoning and instruction-following capabilities, making them potentially powerful tools for time-series analysis. However, time series lie outside their native textual modality, raising a fundamental question: how should time series be represented so that LLMs can reason about them effectively? Existing work typically serializes raw numerical sequences or fine-tunes pre-trained LLMs on time-series data. These approaches place the burden of extracting temporal structure directly on the LLM, creating a modality mismatch that often degrades performance on long sequences and introduces substantial computational overhead. In this work, we introduce Time-Series-to-Structured-Program representation (T2SP), a deterministic, training-free method that represents a time series as a structured symbolic program. T2SP decomposes time series into trends, periods, and salient events, expressing them in a program-friendly format aligned with the textual and code-like modalities on which LLMs are natively trained. By shifting temporal-structure extraction from the model to the representation itself, T2SP enables off-the-shelf LLMs to leverage their existing reasoning capabilities for time-series understanding. We evaluate T2SP on three reasoning tasks -- editing, captioning, and question answering -- where it consistently improves performance, reduces reasoning time, and lowers failure rates compared with raw-string representations. Our results demonstrate that T2SP provides an effective interface between time series and LLMs.

---


### 5. [DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics](https://arxiv.org/abs/2606.12487)

**<font color=#1a73e8>作者：</font>** Zimo Zhao, Maolin Wang, Bowen Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is essential for efficient large language model inference, but reliably quantizing activations remains challenging when weights, activations, and KV caches are all quantized to 4-bit precision. A key difficulty lies in massive activations, whose extreme values dominate the activation range and amplify quantization errors. State-of-the-art methods mainly mitigate massive activations through transformation-based smoothing, such as orthogonal rotations and affine scaling, but overlook the cross-layer dynamics of the residual stream. In this paper, we show that massive activations emerge and disappear in a phase-wise pattern across network depth, triggering large residual changes. These changes cause newly injected layer-wise updates to dominate the 4-bit quantization scale and weaken historical residual information. To characterize this behavior, we introduce Jump Ratio and Historical Feature SNR. This suggests that static transformation-based smoothing cannot fully resolve dynamic quantization instability caused by cross-layer residual changes. Based on this analysis, we propose DynamicPTQ, a Dynamic Post-Training Quantization policy for phase-aware mixed-precision activation quantization. DynamicPTQ identifies quantization-sensitive layers from residual-stream dynamics and assigns 8-bit activation precision only to these layers, while keeping weights, KV caches, and other activations in 4-bit precision. It can be directly integrated with strong PTQ baselines such as QuaRot, SpinQuant, and FlatQuant. Experiments on LLaMA-2 and LLaMA-3 show that DynamicPTQ consistently improves perplexity and zero-shot QA performance under W4A4KV4 quantization, while achieving 1.05 to 1.07 times throughput improvement with modest memory overhead. These results demonstrate a practical path toward robust low-bit LLM inference.

---


### 6. [Rubric-Guided Self-Distillation: Post-Training Without Rubric Verifiers](https://arxiv.org/abs/2606.12507)

**<font color=#1a73e8>作者：</font>** MohammadHossein Rezaei, Anas Mahmoud, Zihao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubrics have emerged as an alternative to RLVR in open-ended domains where a single ground-truth final answer is not available. Existing rubric-based training methods rely on an LLM verifier that scores each rollout against rubrics. This introduces substantial training-time overhead, exposes optimization to verifier-specific biases, and reduces rubric feedback to a sparse end-of-trajectory signal. We propose Rubric-Guided Self-Distillation (RGSD), a verifier-free training method in which the base policy, conditioned on the rubric, serves as the teacher for the unconditioned student. RGSD distills the rubric-conditioned teacher distribution into the student token-by-token, replacing sparse trajectory-level rewards with dense per-token learning signals and removing the LLM judge from the training loop entirely. Across Qwen-2.5 (3B, 7B) and Qwen3-Thinking (4B, 8B) models on medical and science domains, RGSD achieves rubric satisfaction comparable to judge-based GRPO while using one on-policy rollout per prompt and no training-time verifier calls. Ablations show that raw rubrics provide a stronger teacher enrichment signal than self-generated reference responses, while a stronger GRPO judge can outperform RGSD in some settings, positioning RGSD as a complementary verifier-free alternative when verifier cost or reliability is the bottleneck.

---


### 7. [Analyzing and Improving Fine-grained Preference Optimization in Medical LVLMs](https://arxiv.org/abs/2606.12590)

**<font color=#1a73e8>作者：</font>** Shayan Mohammadizadehsamakosh, Pritam Sarkar, Leonid Sigal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved strong performance across medical imaging tasks, yet they remain prone to factual inconsistencies, poor visual grounding, and misalignment with clinically meaningful feedback. Existing post-training alignment approaches, including Direct Preference Optimization (DPO) and its variants, face three critical limitations in the medical domain: (1) sequence-level reward signals treat clinically critical tokens identically to generic filler text; (2) reliance on static supervised fine-tuning references as preferred responses introduces an off-policy distribution shift, steering optimization toward stylistic artifacts over clinical correctness; and (3) alignment objectives lack explicit visual grounding constraints, leaving models insensitive to subtle yet diagnostically decisive pathological features. Our method leverages a bidirectional token-wise KL regularizer alongside a visual-contrastive grounding objective that pairs clean and lesion-corrupted images to penalize responses generated without adequate visual evidence. Together, these components form a fine-grained, on-policy alignment framework that constructs preference pairs by minimally editing model-generated outputs, correcting only clinically erroneous spans while preserving the original linguistic style. Extensive experiments across medical imaging tasks and clinical text generation benchmarks validate the effectiveness of our approach.

---


### 8. [Emerging Flexible Designs for Geospatial Multimodal Foundation Models](https://arxiv.org/abs/2606.12595)

**<font color=#1a73e8>作者：</font>** Philipe Dias, Waqwoya Abebe, Abhishek Potnis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are rapidly transforming Earth observation by enabling scalable pretraining across diverse unlabeled geospatial modalities. However, their architectural diversity ranging from encoder-only to encoder-decoder and masked autoencoding paradigms makes it challenging to assess performance trade offs in a consistent manner. In this work, we present an apples-to-apples comparison of leading FM architectures designed for geospatial multimodal reasoning, with a particular focus on flexibility across varied spectral band configurations. We standardize pretraining using identical self supervised learning objectives and training datasets, and evaluate all models under consistent parameterization on the GEOBench benchmark across classification and segmentation tasks. Our results offer new insights into the design trade-offs between model flexibility, modality alignment, and downstream task performance. By highlighting architectural strengths and limitations under controlled conditions, this study provides practical guidance for building next generation geospatial foundation models capable of robust multimodal reasoning.

---


### 9. [Constrained Semantic Decompression in LLMs through Persian Proverb-Conditioned Story Generation](https://arxiv.org/abs/2606.12599)

**<font color=#1a73e8>作者：</font>** Zahra Habibzadeh, Paria Khoshtab, Amir Mesbah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transforming a dense, abstract proverb into an engaging and morally faithful narrative requires deep cultural understanding and robust semantic grounding. We frame this problem as a \emph{constrained semantic decompression} task and study proverb-conditioned story generation as a testbed for abstraction-to-realization in large language models (LLMs). Focusing on Persian, we introduce the Proverb Aligned Narrative Dataset (PAND), pairing proverbs with human-written stories and explicit meanings. By a hybrid evaluation framework that combines human-calibrated LLM-as-a-Judge with structural metrics, we analyze model behavior across multiple prompting regimes. Our findings reveal a persistent \emph{decompression gap}: current LLMs often achieve strong surface-level fluency while failing to faithfully instantiate the underlying moral and causal structure encoded in proverbs. We further show that explicit reasoning and iterative refinement can partially mitigate these failures, suggesting that many decompression errors arise from difficulties in translating abstract meaning into narrative form rather than a complete lack of relevant knowledge. Our proposed task naturally extends to other forms of compressed cultural knowledge.

---


### 10. [Shopping Reasoning Bench: An Expert-Authored Benchmark for Multi-Turn Conversational Shopping Assistants](https://arxiv.org/abs/2606.12608)

**<font color=#1a73e8>作者：</font>** Shuxian Fan, Seonwoo Min, Youna Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational shopping assistants now serve hundreds of millions of customers, yet no existing benchmark jointly evaluates the open-ended multi-turn reasoning, domain expertise, and criterion-level quality that real shopping conversations demand. Shopping reasoning is unique among language model applications. Unlike factual question answering or verifiable code generation, it requires balancing subjective preferences, budget constraints, and cross-product trade-offs across multi-turn dialogue, capabilities absent from previous e-commerce and general-purpose benchmarks. We introduce the Shopping Reasoning Bench, an expert-authored benchmark of 525 missions (232 single-turn, 293 multi-turn) with 10863 importance-weighted binary rubrics authored by retail domain experts. These criteria are organized under a taxonomy of five reasoning categories and fifteen subcategories covering diverse demands such as preference refinement, trade-off analysis, and compatibility assessment. An evaluation of nine models across three families (GPT, Claude, Gemini) shows that pass rates reach only 57--77% overall. On multi-turn missions, all models score 13--29 points lower on optional above-and-beyond criteria than on required ones, and performance degrades 4--18 points as conversations progress. These gaps show that current models handle basic shopping assistance but fall short of expert-level advice, making Shopping Reasoning Bench a challenging testbed for future shopping assistant development.

---


### 11. [Viral Proteins Reveal Geometry of Protein Language Models](https://arxiv.org/abs/2606.12609)

**<font color=#1a73e8>作者：</font>** Arthur Bigot, Harmon Bhasin, Core Francisco Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein language models are trained on highly imbalanced datasets, raising the question of how they represent underrepresented biological sequences. Using viral proteins as a case study across ESM model families, we identify a dominant nativeness axis in embedding space, aligned with masked reconstruction perplexity, that orders sequences from well-modeled cellular proteins through viral proteins to shuffled and random sequences. Scaling contracts this axis unevenly across viral families. Despite this, protein language model embeddings retain viral-specific signal: viral proteins remain linearly separable beyond zero-shot perplexity and shallow sequence features. Together, these results suggest that pLM representations are structured by a general notion of nativeness while preserving information specific to distinct biological groups.

---


### 12. [The Mathematics of AI Winters: The mathematical Taxonomy of Paradigm Fragility in AI Winter](https://arxiv.org/abs/2606.12610)

**<font color=#1a73e8>作者：</font>** Miquel Noguer i Alonso, David Pacheco Aznar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two major periods of reduced funding and confidence in artificial intelligence research, commonly called the first and second AI winters, are usually explained through engineering failure, commercial disappointment, and inflated expectations. This article develops a complementary thesis: that the dominant paradigms of those periods also met genuine formal barriers, including limitations of representation, optimisation, computational complexity, statistical learnability, and high-dimensional approximation. The contribution is synthetic rather than archival. We do not claim that particular theorems mechanically caused the winters; rather, we show that several central disappointments of early AI were aligned with mathematically precise bottlenecks. We analyse these bottlenecks through the perceptron impossibility results of Minsky and Papert, the complexity-theoretic hardness of exact neural-network training established by Blum and Rivest, minimax rates for nonparametric estimation in high dimension due to Stone, vanishing-gradient analyses by Hochreiter and by Bengio and collaborators, and classical statistical learning theory in the tradition of Vapnik and Chervonenkis, Valiant, and Blumer and collaborators. We then relate these barriers to the later breakthroughs that mitigated, rather than eliminated, them.

---


### 13. [ECA: Efficient Continual Alignment for Open-Ended Image-to-Text Generation](https://arxiv.org/abs/2606.12633)

**<font color=#1a73e8>作者：</font>** Jiangtao Kong, Peijun Zhao, Chun-Fu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental Learning (IL) for Open-ended Image-to-Text Generation (OpenITG) enables models to continuously generate accurate, contextually relevant text for new images while preserving previously acquired knowledge. Unlike prior studies, this paper addresses a more practical scenario in which the predominant category of visual data shifts over time as environments evolve. In this context, we introduce a new notion of continual alignment, which incrementally adapts the alignment module within pre-trained VLMs to preserve high-quality cross-modal representations. Based on this idea, we propose Efficient Continual Alignment (ECA), a novel exemplar-free IL approach for OpenITG. The key challenge is enabling the model to acquire new, task-specific features while minimizing interference with the established alignment without accessing raw data from previous tasks. To address this, ECA employs three core mechanisms: a Mixture of Query (MoQ) module that adapts task-specific query tokens, a Fisher Dynamic Expansion (FeDEx) that dynamically expands model structure based on a Fisher Information Matrix (FIM)-based metric, and an embedding dictionary with Dictionary Replay (DR) to retain past knowledge. To evaluate ECA's performance, we construct four new IL OpenITG benchmarks that better reflect real-world scenarios. Experimental results demonstrate that ECA significantly mitigates catastrophic forgetting and improves IL performance compared to baseline methods. Code and benchmarks are available at this https URL.

---


### 14. [MentalMARBERT: Domain-Adaptive Pre-training and Two-Stage Fine-Tuning for Arabic Mental Health Disorders Detection](https://arxiv.org/abs/2606.12649)

**<font color=#1a73e8>作者：</font>** Fatimah Almalki, Areej Alhothali, Lulwah Alharigy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting mental health disorders from Arabic social media text remains challenging due to dialectal variation, informal language, limited high-quality annotated resources, and severe class imbalance. While English mental health natural language processing (NLP) has progressed substantially, Arabic multi-class disorder classification remains insufficiently studied. This study proposes a two-phase framework for Arabic mental health text classification. In phase 1, three Arabic pre-trained language models, AraBERT, CAMeLBERT, and MARBERT, undergo Domain-Adaptive and Task-Adaptive Pretraining (DAPT and TAPT) using a large-scale corpus of unlabeled Arabic mental health tweets. The adapted models are evaluated under a unified protocol to identify the most effective backbone model. In phase 2, the selected model is assessed across four configurations combining single-stage and hierarchical two-stage classification architectures with full fine-tuning and Low-Rank Adaptation (LoRA). To support this study, we constructed a novel annotated Arabic mental health dataset comprising 50,670 tweets across six categories, with strong inter annotator agreement (Krippendorff's Alpha = 0.733, average pairwise agreement = 0.797). Experimental results show that the domain-adapted MARBERT (MentalMARBERT) achieves statistically significant improvements over baseline models in both accuracy and macro-F1. The hierarchical two-stage architecture combined with full fine-tuning achieves the best overall performance, reaching a macro-F1 of 0.861 and an accuracy of 0.877. These findings demonstrate the effectiveness of domain-specific adaptive pretraining and hierarchical classification for Arabic mental health disorder detection.

---


### 15. [TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation](https://arxiv.org/abs/2606.12657)

**<font color=#1a73e8>作者：</font>** Siyu Li, Toan Tran, Lingyi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility data is important for transportation, urban planning, and epidemic control, but large-scale trajectory collection is often costly and privacy-constrained, motivating realistic synthetic trajectory generation. Existing LLM-based generators typically rely on either prompt engineering, which preserves zero-shot reasoning but lacks fine-grained spatiotemporal grounding, or trajectory-level fine-tuning, which improves statistical precision but incurs substantial computational cost and may weaken general reasoning. We propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for human mobility trajectory generation without model fine-tuning. TrajGenAgent uses a two-stage orchestrator-worker design: an LLM first synthesizes an individual- and weekday-conditioned activity chain from historical evidence via in-context learning, and a deterministic workflow then grounds each activity into a complete visit using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation, and LLM-based duration estimation. To evaluate realism beyond aggregate spatiotemporal statistics, we introduce an anomaly-detection-based evaluation framework using two complementary detectors to assess behavioral and semantic plausibility. Experiments on benchmark and large-scale simulation datasets show that TrajGenAgent improves spatiotemporal fidelity, semantic coherence, and individual-specific behavioral realism over representative neural and LLM-based baselines, while avoiding parameter updates.

---


### 16. [Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents](https://arxiv.org/abs/2606.12674)

**<font color=#1a73e8>作者：</font>** Kushal Raj Bhandari, Ling Yue, Ching-Yun Ko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compact language models (LMs) reduce cost, latency, and deployment risk for tool agents. Yet MCP-style tool use requires more than isolated function calling: an agent must discover tools from live catalogs, satisfy schemas, preserve dependencies across intermediate outputs, and ground final responses in executed evidence. Small planners often generate plausible workflow graphs that fail under tool resolution, parameter validation, dependency tracking, or execution. We argue that this failure mode is poorly handled by small-corpus distillation. A few hundred teacher traces can teach workflow format, but rarely cover the recovery behavior needed to repair failed plans over changing tool catalogs. We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows. It evolves typed workflow graphs through structured edits, execution feedback, adaptive intensity, meta-guided redesign, and diversity pruning. On held-out MCP-Bench tasks spanning live MCP servers and 250 tools, Evoflux raises execution feasibility from roughly 3% to 17-24% across small planners. In contrast, SFT and SFT+DPO on the same search-mined data match, underperform, or collapse below zero-shot performance; ReAct reaches higher peaks, but with higher variance and token cost. These results show that execution-grounded search is more reliable under scarce teacher-trace budgets.

---


### 17. [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688)

**<font color=#1a73e8>作者：</font>** Atindra Jha, Naomi Sagan, Keisuke Kamahori 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about model structure, making them ill-suited to accommodate this new architectural diversity. Here we present M*, a universal serving system for efficient serving of composite AI models. M* represents models as dataflow graphs, processing requests spanning diverse modalities and tasks as traversals over these graphs. The core insight is a modular abstraction that supports arbitrary composition of model components, flexible placement onto a physical cluster, and model-agnostic optimizations within a distributed runtime. We call this abstraction the Walk Graph and show how it can concisely capture composite models from a broad range of families. We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speech workloads on Qwen3-Omni. M* also outperforms the V-JEPA 2-AC rollout baseline for robotic planning by up to 12.5x. Thus, our work paves the road towards more efficient serving of complex models with minimal developer effort.

---


### 18. [Observable Patterns Are Not Explanations: A Causal-Geometric Analysis of Latent Reasoning Models](https://arxiv.org/abs/2606.12689)

**<font color=#1a73e8>作者：</font>** Darpan Aswal, Thomas Palmeira Ferraz, Yongxin Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent reasoning models (LRMs) replace explicit chain-of-thought with continuous thoughts. Recent work treats observable latent-state patterns, such as BFS-like frontiers and decodable arithmetic computation, as evidence for internal reasoning mechanisms. Evaluating two LRMs (Coconut and CODI) against controls lacking the proposed recurrence or curriculum, we find these patterns also appear in the controls and do not always causally affect behavior. Causal interventions reveal that latent-thought utilization is not binary but graded, scaling with a thought's causal effect on model behavior. Geometric analyses reveal this effect concentrates in low-rank directions whose step-to-step geometry grows more structured as their behavioral influence increases. Latent thoughts should therefore be treated as hidden computation, not hidden explanation: decodability, attention, or static structure alone cannot establish mechanism. LRM interpretability thus requires matched controls and causal tests.

---


### 19. [LLM-Powered Personalized Glycemic Assessment in Type 2 Diabetes with Wearable Sensor Data](https://arxiv.org/abs/2606.12699)

**<font color=#1a73e8>作者：</font>** Yifan Gao, Yanmin Gong, Yun Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Type 2 Diabetes (T2D) poses an increasing global health threat, demanding effective glycemic assessment to support personalized and improved diabetes care. Wearable sensors such as continuous glucose monitors (CGM) and fitness trackers offer many valuable insights for glycemic assessment. However, effectively analyzing these data requires integration with essential individual-level context. Existing methods are often based on traditional machine learning (ML) and rely primarily on historical blood glucose measurements and overlook personalized information, which limits their performance across diverse diabetes populations. Recent advances in large language models (LLMs) have demonstrated their ability to integrate diverse data modalities while modeling sequential dependencies, motivating the exploration of their potential for personalized glycemic assessment.
In this paper, we propose GlyLLM, an LLM-powered framework for modeling CGM-based glycemic dynamics through the integration of wearable sensor data and structured metadata. GlyLLM can leverage the extensive prior knowledge of pre-trained LLMs and achieve sensor-text semantic abstraction at decision time. Experiments on two related tasks on the AI-READI dataset demonstrate that our model outperforms traditional ML methods by an average of 13.66\% in Root Mean Squared Error (RMSE) for glucose forecasting and 13.08\% in Area Under the Receiver Operating Characteristic (AUROC) for diabetes categorization. Additionally, our ablation study shows that diabetes surveys and biometric tests are more critical than other health information for glycemic assessment. Our work presents a promising step toward harnessing the power of LLMs to advance personalized glycemic assessment in T2D care.

---


### 20. [Deployment-Centered Evaluation: Predicting Query-Level Rejection Risk in a Clinical LLM System](https://arxiv.org/abs/2606.12702)

**<font color=#1a73e8>作者：</font>** Alyssa Unell, Miguel Fuentes, Brenna Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into clinical systems, making it essential to evaluate the real-world utility of these systems. However, static benchmarks tend to measure correctness rather than user acceptance, aggregate performance across queries, and require densely annotated datasets -- leading to major blind spots for evaluating clinical systems. In this work, we perform a deployment-centered evaluation of an LLM system embedded within electronic health records at an academic medical center, where user feedback is sparse but closely reflects the deployment conditions. Specifically, we train a pre-response classifier that estimates the risk that a future interaction will result in the user rejecting the LLM response, based on query content and deployment-specific context available before generation. We conduct a prospective analysis of our model over 4.5 months of user feedback, finding that our prediction model achieves an AUROC of 0.719. Further, we estimate the benefit of such predictions in two downstream use cases (guardrail triggering and abstention). Our key conceptual insight is that making use of deployment-specific context (i.e., the provider type, department name, language model used for response), as opposed to only query content, improves the ability to predict whether the user will reject the system output. Altogether, our empirical case study demonstrates the feasibility of predicting user rejection using deployment-specific context, opening the door to targeted guardrails.

---


### 21. [Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review](https://arxiv.org/abs/2606.12716)

**<font color=#1a73e8>作者：</font>** Xinyu Zhao, Rana Muhammad Shahroz Khan, Zhen Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) and Multimodal LLMs (MLLMs) into scientific peer-review workflows introduces novel and significant risks for adversarial manipulation, especially given the multimodal nature of scientific papers where figures, not just text, convey core evidence. This creates a significant gap: current robustness studies on AI peer-review are overwhelmingly text-only. Moreover, the problem is distinct from standard jailbreaking, as a peer-review attack seeks to induce a domain-specific, targeted failure (e.g., "inflate this score") rather than a general safety policy violation, for which no practical defenses exist. To address this, we introduce PaperGuard, the first comprehensive benchmark designed to systematically evaluate and defend AI-generated peer-review against these domain-specific, cross-modal attacks. Our framework is built on three pillars: (1) a new multimodal peer-review dataset spanning multiple scientific domains; (2) a unified suite of attacks, including black-box prompt injections and white-box perturbations, specifically designed to target both text (GCG) and figures (PGD); and (3) a practical defense, motivated by the long-context challenge of academic papers, that uses chunk-based embedding search to efficiently localize and mitigate harmful instructions. Our extensive experiments, conducted across state-of-the-art models, confirm that AI reviewers are pervasively vulnerable. PaperGuard establishes the foundational benchmark, protocols, and actionable defense necessary to pioneer trustworthy, attack-resilient AI-assisted scholarly reviewing.

---


### 22. [Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict Behavior](https://arxiv.org/abs/2606.12730)

**<font color=#1a73e8>作者：</font>** Rafal Kocielnik, Pengrui Han, Peiyang Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Anticipating LLM behavioral tendencies from low-cost psychometric probes is critical for safe deployment, but only if self-reports (SR) reliably predict behavior. Recent work documented substantial SR-behavior dissociation in LLMs, but relied on broad personality traits (Big 5) that predict specific behaviors weakly, even in humans. Furthermore, the isolation of conversational sessions combined with weak context matching left open whether LLMs truly lack coherence or whether the conditions needed to detect such coherence were not met. We contrast Big 5 with the Theory of Planned Behavior (TPB), which measures intention targeted to a specific behavior and predicts human behavior substantially better than broad traits. We run experiments across four behavioral tasks and 11 frontier LLMs, while also varying session context and identity induction. We find that SR-behavior coherence exists but is selective. 1) Within a shared conversation, the Theory of Planned Behavior reaches human-level coherence; Big 5 does not. 2) Across separate conversations, coherence survives only for behaviors anchored outside the immediate prompt, such as implicit bias shaped by training, and collapses when behavior is strongly primed by context, as with sycophancy. 3) Persona prompting makes self-reports more consistent across conversations, but does not bring behavior into alignment. These findings suggest that coarse personality frameworks, such as Big 5 may not be the best tools for testing deployment behavior. More task- and behavior-specific instruments are needed, and even these must be evaluated across tasks and contexts.

---


### 23. [Normative Robustness as a Frontier for Non-Verifiable Reasoning in LLMs](https://arxiv.org/abs/2606.12731)

**<font color=#1a73e8>作者：</font>** Elizaveta Tennant, Benjamin Henke, Anita Keshmirian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLMs increasingly serve in advisory and deliberative roles, users rely on them for non-verifiable reasoning in domains lacking objective ground truths. However, traditional evaluations of LLM reasoning focus almost exclusively on fact-based domains, such as mathematics and science, leaving uncertainty over whether and to what degree models can handle ambiguous, subjective, or value-laden problems over time. To address this concern, we propose moral reasoning as a paradigmatic subdomain of non-verifiable reasoning. We define moral robustness as a model's capacity to exhibit sound moral reasoning across time and contexts, and we introduce a scalable, adversarial, multi-turn evaluation framework to empirically measure this capability. We simulate 48,000 user-agent moral deliberations across four frontier LLMs, varying premise relevance, premise order, conversation duration, and the user's stated moral view. We find that models successfully ignore morally-irrelevant distractors, but shift their reasoning by up to 6.5%, on average, towards the user's stated preferred moral view, and varying their reasoning depending on factors such as order (altering moral judgments by order in 13-22% of the cases) and duration (altering moral judgments between single-turn and multi-turn in 10-24% of the cases). Our analysis indicates that models tailor not just their final verdicts but their underlying justifications to align with a user's moral viewpoint - a failure mode we characterize as moral deliberative sycophancy.

---


### 24. [GRIP: Feedback-Guided Prompt Retrieval for Large Multimodal Models](https://arxiv.org/abs/2606.12744)

**<font color=#1a73e8>作者：</font>** Garvita Allabadi, Matteo Sodano, Roberto Estevão 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-Context Learning (ICL) has become a powerful mechanism for adapting Large Language Models (LLMs) to new tasks without fine-tuning. Extending this concept to Large Multimodal Models (LMMs), Multimodal In-Context Learning (M-ICL) relies on retrieving relevant examples, such as images, captions, or question-answer pairs, to guide predictions across tasks like classification, captioning, and visual question answering (VQA). Most existing approaches select in-context examples based on feature-space similarity, assuming that semantically similar samples provide the most useful context. However, our systematic analysis reveals that this assumption does not always hold: visually similar examples are not necessarily those that most effectively enhance in-context learning performance.
To address this, we propose the Guided Retrieval of In-context Prompts (GRIP), a learnable vision-only retrieval framework that leverages feedback from LMMs to identify examples that truly improve model predictions. GRIP learns to distinguish beneficial from detrimental in-context examples through contrastive training, refining retrieval beyond pure similarity. Across three multimodal tasks, namely classification, captioning, and VQA, GRIP improves consistently over similarity-based retrieval on Qwen2.5-VL-7B, with its strongest gains in classification on Idefics2-8B. Moreover, we demonstrate that retrievers trained with feedback from one open LMM can be transferred to other models without retraining, including closed-source GPT-4o and Gemini, enabling scalable and cost-efficient deployment of M-ICL. Code will be published upon acceptance.

---


### 25. [Prefill Awareness in Large Language Models](https://arxiv.org/abs/2606.12747)

**<font color=#1a73e8>作者：</font>** Andy Wang, Parv Mahajan, David Demitri Africa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-relevant studies of language models, including alignment and jailbreaking evaluations and AI control protocols, often rely on prefilling model outputs. If AI models can recognize and act on the fact their prior assistant messages have been inserted or edited, the effectiveness and validity of these methods could be compromised. We investigate whether frontier language models can distinguish between tampered and untampered assistant-side context, a capability we call prefill awareness. To do so, we construct a binary preference benchmark across three prefill mechanisms, filtering for cases where models show consistent stances. We find that frontier models show substantial prefill awareness: Claude Opus 4.5 detects prefills opposing its preferences in 9-35% of cases with a 0% false positive rate when prompted; additionally, models often revert towards baseline behavior without explicitly reporting that the prefill was foreign. Controlled ablations later also show that detection and resistance rely on different cues, where stylistic mismatch mainly affects whether models flag a prefill as foreign, while preference mismatch mainly affects whether they revert toward their baseline answer. We also examine more realistic agentic settings such as misalignment-continuation evaluations and SWE-bench trajectories, where frontier models sometimes disavow prefilled assistant turns in ways that depend strongly on dataset, task success, and hidden formatting artifacts. Our results indicate that prefill awareness is already a substantial confound for some prefill-based methods. We recommend that model developers track this capability in frontier systems.

---


### 26. [LLMs Can Better Capture Human Judgments--With the Right Prompts](https://arxiv.org/abs/2606.12754)

**<font color=#1a73e8>作者：</font>** Danica Dillion, Chen Cecilia Liu, Baihui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Are large language models (LLMs) bad at capturing human judgment? Two commonly stated limitations are that LLMs fail to capture full distributions of responses, and that their judgments are unstable across wording variations. We demonstrate simple prompting strategies that mitigate these limitations. Across two datasets--a U.S.-representative set of 144 moral scenarios and 38 moral beliefs from the International Social Survey Programme's Family and Changing Gender Roles module covering 32 countries--we show how simple elicitation techniques help improve AI-human alignment. First, prompting models to report standard deviations and response proportions recovers the full range of human responses better than common strategies. Second, ensuring scenarios are clear to human participants--as reflected in human confusion ratings--boosts model alignment, and LLMs can track human confusion ratings. At the same time, we find that LLMs' estimates of their own error are poorly calibrated, though they can predict human variability relatively well. These results suggest that asking better questions to LLMs can yield better answers.

---


### 27. [Adaptive Weighted Averaging](https://arxiv.org/abs/2606.12763)

**<font color=#1a73e8>作者：</font>** Aditya Bhaskara, Ashok Cutkosky, Ravi Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of selecting the largest among $n$ unknown values $x_1,\dots,x_n$ given only a single unbiased estimate $y_i$ for each $x_i$. We design strategies that are simultaneously admissible (not uniformly dominated by any other strategy) and also never worse than a given baseline such as uniform random selection. We provide an application to stochastic optimization, where we obtain online-to-batch conversion bounds with a desirable "no-compromise" guarantee: they are never worse than standard random iterate selection, and yet can be significantly better in benign settings.

---


### 28. [Detecting Functional Memorization in Code Language Models](https://arxiv.org/abs/2606.12764)

**<font color=#1a73e8>作者：</font>** Matthieu Meeus, Anil Ramakrishna, Matthew Grange 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate code at scale. Meanwhile, prior work has investigated whether training data may be recoverable from model outputs, by auditing the textual overlap between training examples and model generations. Code, however, can be functionally equivalent while textually dissimilar. In this work, we study functional memorization: extraction of functional logic beyond what verbatim metrics detect. We construct a counterfactual setup for Olmo-3-32B, comparing a midtrained model (exposed to target code) against a pretrained reference (not exposed). We prompt both models with Python function signatures and measure both textual and functional similarity (i.e., LLM-as-a-judge, execution-based). Our results show clear evidence of functional memorization, highlighting the need for auditing metrics that go beyond textual overlap.

---


### 29. [Constructing Evaluation Datasets for Procedural Reasoning: Balancing Naturalness, Grounding, and Multi-Hop Coverage](https://arxiv.org/abs/2606.12767)

**<font color=#1a73e8>作者：</font>** Sarah Elshabrawy, Rahul K. Dass, Ashok K. Goel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating procedural reasoning in AI-supported learning systems requires question-answer datasets that are both learner-like and grounded in the instructional knowledge the system is expected to use. We study how TMK-based question generation strategies affect dataset quality for procedural and multi-hop reasoning.
We compare three strategies: strict generation from Task-Method-Knowledge (TMK) models, transcript-first generation with post-hoc TMK filtering, and TMK-aware generation that combines transcripts with structured guidance. To evaluate generated items, we introduce a grounding validation framework based on closed-set evidence units extracted from TMK models. The framework measures whether answers are supported by the underlying representation, whether questions are self-contained, and whether they target multi-hop procedural reasoning.
Across 23 instructional topics and 690 generated question-answer pairs, strict TMK generation achieves the strongest overall quality, with 96.5% grounded questions and 92.6% usable questions. Transcript-first generation produces more learner-like questions but more context-dependent or weakly grounded items, while TMK-aware generation yields high raw multi-hop coverage but lower grounding. These results show that procedural richness and natural phrasing do not guarantee representational grounding, motivating explicit representation-aware validation for evaluation datasets in AI-supported learning.

---


### 30. [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.12780)

**<font color=#1a73e8>作者：</font>** Yijun Ma, Zehong Wang, Yiyang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. Existing LLM-agent methods often rely on memory or planning modules, yet they rarely close the loop between them to continually refine an internal understanding of environment dynamics. We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge. Rather than representing experience as isolated rules or low-level action constraints, ProPlay abstracts successful trajectories into procedures and organizes them in a procedure graph that captures causal transitions among task stages. Each transition is associated with a reliability record embedding to estimate its task-specific contribution from past outcomes. Before each episode, ProPlay simulates future procedural trajectories over known graph structures as structured soft guidance; after execution, it refines the graph using environment feedback. Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines. Our code has been released in this https URL.

---


### 31. [A Tutorial on World Models and Physical AI](https://arxiv.org/abs/2606.12783)

**<font color=#1a73e8>作者：</font>** Il-Seok Oh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World modeling is emerging as a central principle for building intelligent systems capable of prediction, reasoning, and decision making. A central distinction can be drawn between explicit world models, which learn structured dynamics for rollout-based reasoning and planning, and implicit world models, which encode predictive structure within scalable learned representations. These complementary paradigms provide a foundation for physical AI in domains such as robotics and autonomous driving, enabling intelligence beyond reactive control under real-world constraints. Recent foundation models further suggest a pathway toward unified systems integrating perception, prediction, and action. Despite rapid progress, major challenges remain in hierarchical reasoning, long-horizon planning, and autonomous goal formation, which are critical for advancing toward artificial general intelligence. This tutorial presents a coherent framework in which diverse world modeling approaches are unified through shared predictive structure and differentiated by how such structure is represented and exploited.

---


### 32. [How Fine-Grained Should a RAG Benchmark Be? A Hierarchical Framework for Synthetic Question Generation](https://arxiv.org/abs/2606.12789)

**<font color=#1a73e8>作者：</font>** Chase M. Fensore, Kaustubh Dhole, Jason Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating retrieval-augmented generation (RAG) systems requires benchmarks that capture diverse question characteristics, yet practitioners lack empirical guidance on which dimensions to vary and at what granularity. We present HieraRAG, a hierarchical framework for studying granularity in RAG benchmark construction, defining optimal granularity as the level that maximizes discriminative power (the standard deviation of generation quality across categories) within a given RAG configuration. As a case study, we generate 5,872 synthetic question-answer (QA) pairs from FineWeb-10BT across 3 dimensions (Question Complexity, Answer Type, Linguistic Variation) at 3 granularity levels (2, 4, and 8 categories). With a BM25+Falcon-3-10B pipeline, optimal granularity varies by dimension: complexity benefits from fine-grained distinctions (discriminative power: 0.053) while answer type and linguistic variation peak at medium granularity. We introduce a Coherence Ratio metric to quantify whether fine-grained splits cleanly subdivide parent categories, revealing structural differences across dimensions (Question Complexity: 0.40 vs. Answer Type: 1.44). Human evaluation of 110 stratified QA pairs confirms synthetic quality. While these specific findings reflect a single configuration, HieraRAG provides a portable procedure and validation metric for practitioners to determine evaluation granularity within their own RAG settings.

---


### 33. [The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements](https://arxiv.org/abs/2606.12797)

**<font color=#1a73e8>作者：</font>** Md Jafrin Hossain, Mohammad Arif Hossain, Weiqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services, healthcare triage, and financial advising. We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees. Applying six containment principles derived from a compositional model of agentic architectures, we audit three dominant frameworks (LangChain, AutoGPT, and OpenAI Agents SDK) and find no native compliance in any of them. Memory integrity, a defense against one of the most prevalent vulnerability classes, is not observed in any of the three evaluated frameworks. We validate these findings empirically: in a simulated government benefits agent built on LangChain, a single memory-poisoning write induces persistent targeted corruption across all tested seeds and backends, increasing the wrongful denial rate for targeted applicants to 88.9%. Under a complex five-factor policy, the same attack preserves aggregate accuracy while increasing targeted wrongful denials by 3.5x, rendering the corruption difficult to detect through standard monitoring. We then introduce two lightweight containment mechanisms: a memory integrity validator and a policy gate, which eliminate both attack vectors with sub-millisecond overhead (<0.2ms per call). We conclude that the current agentic framework ecosystem may not yet meet secure-by-default expectations for public-facing deployments and outline priority architectural interventions to enable trustworthy deployment in high-stakes, socially impactful applications.

---


### 34. [MLUBench: A Benchmark for Lifelong Unlearning Evaluation in MLLMs](https://arxiv.org/abs/2606.12809)

**<font color=#1a73e8>作者：</font>** He Li, Haoang Chi, Qizhou Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are trained on massive multimodal data, making data unlearning increasingly important as data owners may request the removal of specific content. In practice, these requests often arrive sequentially over time, giving rise to the challenging problem of MLLM Lifelong Unlearning. However, most existing benchmarks are limited in scale and scope, failing to capture the complexities of MLLM lifelong unlearning. To fill this gap, we introduce the MLUBench, a large-scale and comprehensive benchmark featuring 127 entities across 9 classes under lifelong unlearning requests. We perform extensive experiments using MLUBench and reveal that existing unlearning methods suffer from severe, cumulative degradation. More critically, we further identify the unique challenge of this problem: unlike in unimodal models, MLLM lifelong unlearning is constrained by the need to preserve multimodal alignment. Continually unlearning from one modality could degrade the entire model. To alleviate this challenge, we propose LUMoE, an effective method. Experiments demonstrate that LUMoE significantly mitigates the degradation problem faced by baselines. The source code and the MLUBench dataset are open-sourced in this https URL.

---


### 35. [Localizing Anchoring Pathways in Language Models](https://arxiv.org/abs/2606.12818)

**<font color=#1a73e8>作者：</font>** Hillary N. Owusu, Sarah Wiegreffe, Naomi H. Feldman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Irrelevant numbers in a prompt can shift language model judgments, producing anchoring effects in numerical reasoning. We study where this anchor-sensitive signal is carried inside language models using a controlled multiple-choice setup with shared answer options. We define a logit-difference metric comparing the correct answer option with the answer option corresponding to the anchor, and validate that it tracks behavioral anchoring. Using attribution-based circuit localization on 7B--8B Qwen and Llama base and instruction-tuned models, we find that edge-level methods recover this signal more faithfully than node-level methods. Low- and high-anchor circuits transfer strongly within a model, suggesting shared pathway structure across anchor direction. However, sparse transfer across base and instruction-tuned variants is less reliable, indicating that post-training changes which pathways matter most. Overall, our results provide a mechanistic account of how anchoring-related decision signals are carried inside language models.

---


### 36. [GeoNatureAgent Benchmark: Benchmarking LLM Agents for Environmental Geospatial Analysis Across Frontier and Open-Weight Foundation Models](https://arxiv.org/abs/2606.12821)

**<font color=#1a73e8>作者：</font>** Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environmental scientists spend disproportionate effort on data wrangling rather than analysis, and AI agents that automate geospatial workflows remain unvalidated: no benchmark evaluates agents operating through structured tool calling against real APIs. We introduce the GeoNatureAgent Benchmark, the first benchmark for environmental analysis agents that operate via structured tool calls to a production-style geospatial API. It comprises 93 tasks across 18 categories, covering municipality analysis, multi-turn conversation, spatial reasoning, cross-indicator synthesis, error handling and recovery, ranking, comparison, multilingual understanding, habitat analysis, and task rejection. Tasks are evaluated against an open, self-hostable API serving three environmental indicators across Spain and Portugal via sixteen tools. We evaluate seven LLMs (Claude Sonnet 4, DeepSeek V3.2, GLM-5, Gemini 2.5 Pro, Qwen3-235B, GPT-OSS-120B, Llama 4 Scout) under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. We find: (1) Claude Sonnet 4 leads at 60.8% +/- 0.8%, followed by DeepSeek V3.2 at 56.3% +/- 3.1%, with no other model above 51%; (2) the cost-accuracy Pareto frontier is occupied mostly by open-weight models, with DeepSeek V3.2 offering 93% of Claude's capability at 11x lower cost ($0.011/case); (3) comparison tasks remain universally unsolved (0% on close-value comparisons), exposing systematic reasoning limits; and (4) structured tool calling against a real API is more discriminative than general-purpose GIS benchmarks, with accuracies 25-35 points lower. We further show extensibility by integrating BigEarthNet V2 land cover for Portugal alongside Spanish CO2 and erosion indicators. The benchmark, harness, and self-hostable API are publicly available.

---


### 37. [Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics](https://arxiv.org/abs/2606.12828)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do research topics in artificial intelligence grow gradually, or do they advance through abrupt, detectable jumps? Analyzing 80,814 accepted main-track papers from five premier AI conferences (ACL, CVPR, ICLR, ICML, NeurIPS) spanning 2017 to 2025, we show major AI topics advance through topical phase transitions: remaining marginal for years, then surging across venues within one to three years. Large language models became the dominant cross-venue topic by 2025, diffusion models rose with comparable abruptness, and language-model methods crossed into computer vision via vision-language models, whereas reinforcement learning compounded smoothly, distinguishing genuine phase transitions from ordinary growth. This structure is our primary contribution: a large-scale, cross-venue characterization of how AI research reorganizes. We then ask whether a transition leaves a detectable footprint before it peaks. We define an early-warning signature, four publication-dynamics criteria frozen on 2017-2021 data, and evaluate it out of sample on 2023-2025 transitions, obtaining a precision of 27% and recall of 63% against a 13.5% base rate. Applied to 2025 data, the signature flags reasoning and test-time compute, agentic AI, multimodal LLMs, retrieval-augmented generation, and world models as topics to monitor over 2026-2028. The source code is also publicly available on GitHub at this https URL.

---


### 38. [Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning](https://arxiv.org/abs/2606.12830)

**<font color=#1a73e8>作者：</font>** Changye Li, Meng Lu, Yi Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent vision-language models (VLMs) demonstrate strong multimodal understanding, they remain limited in spatial reasoning tasks that require active evidence acquisition and multi-step visual interaction. This limitation suggests that relying solely on implicit visual representations from vision encoders is insufficient for recovering fine-grained spatial evidence. We introduce PERception-Interaction-reason Agent (PERIA), a tool-augmented visual agent for spatial reasoning tasks across map reasoning, visual probing, and vision reconstruction. PERIA uses two lightweight tool families: vision perception tools for exposing textual, symbolic, and spatial evidence, and vision interaction tools for manipulating visual context, tracing paths, and verifying spatial relations. To train PERIA, we develop a unified recipe that combines supervised tool-use trajectory synthesis, composite rewards, and Observation-Relaxed Group-in-Group Policy Optimization (OR-GIGPO) for effective multi-tool behavior. Experiments on 13 benchmarks from 8 datasets show that PERIA-8B improves over the Qwen3-8B backbone by 10.0% on in-distribution benchmarks and 4.4% on out-of-distribution benchmarks, while outperforming previous state-of-the-art baselines of similar size by 7.0%-14.8%. It also achieves performance comparable to much larger models such as Qwen3-VL-235B-A22B-Thinking and GPT-5, demonstrating the effectiveness of PERIA in enhancing spatial reasoning capabilities.

---


### 39. [The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale](https://arxiv.org/abs/2606.12835)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid emergence of autonomous AI agents is transforming artificial intelligence from isolated model inference into distributed systems of reasoning, communication, and action. This paper develops the vision of the Internet of Agentic AI (IoAI): an open ecosystem in which heterogeneous agents discover one another, negotiate responsibilities, exchange context, invoke tools, and execute workflows across cloud, edge, device, organizational, and cyber-physical environments. We synthesize foundations from single-agent agentic AI, multi-agent systems, distributed computing, communication networks, game theory, and security engineering to characterize the architectures and mechanisms required for scalable agent ecosystems. The paper examines agent deployment models, workflow lifecycles, communication protocols, interoperability layers, resource-management challenges, and trust architectures, with case studies in adaptive manufacturing and distributed operational coordination. The resulting framework highlights the central research challenges of controlled emergence, semantic interoperability, secure identity, incentive-compatible coordination, resource-aware orchestration, and governance for large-scale networks of autonomous agents.

---


### 40. [TimeROME-DLM: Temporal Causal Tracing and Low-Rank Inference-Time Knowledge Editing for Masked Diffusion Language Models](https://arxiv.org/abs/2606.12841)

**<font color=#1a73e8>作者：</font>** Zhengtao Yao, Liuyang Song, Hongbo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) such as LLaDA now rival autoregressive (AR) LLMs, but every existing knowledge-editing and unlearning method (ROME, MEMIT, etc.) targets AR transformers and either makes assumptions that fail under iterative denoising, or requires gradient updates whose backward-pass activations cost tens of GB of extra VRAM and which collapse MDLMs at standard learning rates. We introduce TimeROME-DLM, the first training-free, gradient-free, inference-time knowledge-editing framework for MDLMs. It couples two components: a Temporal Indirect Effect (TIE) causal-tracing protocol that identifies, for each fact, the coordinate whose intervention most strongly drives the object prediction at later denoising steps; and a closed-form, low-rank residual edit memory that aggregates subject keys and target deltas across all forget facts and applies a single ridge-regularised update at that coordinate at every diffusion forward, with sparsification to limit utility spillover. Backbone weights stay frozen; only three hyperparameters (alpha, lambda, q) are tuned on a small validation split. On TOFU forget01 with TOFU-finetuned LLaDA-8B-Base, TimeROME-DLM cuts forget-set log-probability by roughly 83 nats. The same configuration transfers to LLaDA-8B-Instruct, Dream-7B, MMaDA-8B, DiffuLLaMA-7B, and LLaDA-MoE-1.4B. It keeps retain-set log-probability nearly flat (within ~1 nat at the utility-safe operating point) across 50 sequentially inserted facts, delivers a four- to fourteen-fold wall-clock speedup with zero additional VRAM over the strongest converged training-time baseline, and scales sub-linearly to 400 facts. TimeROME-DLM closes the locate-then-edit gap between AR LLMs and MDLMs at a fraction of the computational cost.

---


### 41. [Small LLMs for Biomedical Claim Verification: Cost-Effective Fine-Tuning, Structural Dataset Shortcuts, and Cross-Domain Generalization](https://arxiv.org/abs/2606.12854)

**<font color=#1a73e8>作者：</font>** Gaurav Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models such as GPT-4o and GPT-5 achieve strong zero-shot performance on biomedical claim verification, but cost and opacity limit scalable use. We fine-tune three small LLMs: Phi-3-mini (3.8B), Qwen2.5-3B, and Mistral-7B, via QLoRA on SciFact and HealthVer, providing the first study of QLoRA models against GPT-4o and fine-tuned BioLinkBERT encoders. Mistral-7B QLoRA surpasses both GPT-4o and GPT-5 (up to 12% F1 gain) at a fractional cost using just 1,008 training examples. We conduct extensive in-domain and cross-domain evaluation: models trained on SciFact tested on HealthVer and vice versa, at matched sizes to isolate dataset structure from data quantity. We identify a previously unreported structural artifact in SciFact that inflates in-domain scores, and show through bidirectional out-of-domain evaluation that training on structurally sound data enables robust cross-domain transfer. We plan to release all code and adapter checkpoints.

---


### 42. [Multimodal Graph Negative Learning](https://arxiv.org/abs/2606.12863)

**<font color=#1a73e8>作者：</font>** Zhengyu Wu, Xu Wang, Hongchao Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal attributed graphs (MAGs) integrate graph topology with heterogeneous modality attributes, such as text and images, thereby enabling richer modeling of complex relational systems. However, such expressiveness also makes learning on MAGs depend on multiple semantic sources, including structural topology, textual and visual attributes, each of which can be regarded as a branch for node representation. Node-level branch semantic imbalance arises when these branches differ across nodes in semantic informativeness and reliability: a branch that provides discriminative semantics for one node may mislead another due to bias in modality quality or structural context. Existing methods often mitigate such heterogeneity through cross-branch agreement or alignment, implicitly treating the dominant prediction as reliable supervision. When the dominant branch is biased, forced imitation may propagate its bias to other branches and suppress original semantics that are useful for classification. We propose GraphMNL, a graph-aware multimodal negative learning framework that addresses this issue by using Negative Learning as cross-branch guidance. Instead of forcing inferior branches to imitate a teacher prediction, the model teaches them which classes a node is unlikely to belong to. GraphMNL builds a branch library, identifies dominant and inferior branches via graph-aware reliability arbitration, gates unstable transfer, and applies target-preserving negative learning over non-target classes. This design decouples target supervision from branch guidance so that supervised losses learn the correct class, while Negative Learning suppresses unlikely alternatives when branch agreement is unreliable. Through the comprehensive experimental evaluation, GraphMNL achieves the best performance on Grocery datasets with 72.47% accuracy and 76.60 F1 score on Reddit M datasets.

---


### 43. [SMGFM: Spectral Multimodal Graph Pretraining for Multimodal-Attributed Graphs](https://arxiv.org/abs/2606.12867)

**<font color=#1a73e8>作者：</font>** Zhengyu Wu, Xu Wang, Hongchao Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal-attributed graphs (MAGs) couple graph topology with node semantics from text, images, and other modalities. Traditional graph learning contextualizes node semantics by coupling topology with node features. However, this coupling design becomes troublesome in MAGs, where structure-induced and modality-intrinsic semantics may contribute differently to downstream tasks. Structure-induced semantics promote relational consistency through smooth topological variation, whereas modality-intrinsic semantics often encode local, fine-grained distinctions that should not be uniformly smoothed or aligned. Therefore, the key challenge is to identify semantic roles before cross-modal fusion. To this end, we leverage graph-frequency variation as a prior, where low-frequency components capture topology-consistent semantics and high-frequency components preserve modality-specific semantics. Based on this intuition, we propose SMGFM, a spectral multimodal graph pretraining framework that decomposes each modality-specific node signal into graph-frequency bands and assigns band-level semantic roles before cross-modal interaction. Concretely, SMGFM constructs frequency-resolved modality tokens with scalable Chebyshev filters, estimates their coupling reliability through topology-conditioned routing, and performs band-modality interaction before fusion. Its frequency-routed objectives align smooth consensus routes while preserving modality-specific routes, mitigating spatial-domain entanglement and uniform cross-modal alignment. Extensive experiments conducted on the MAG datasets demonstrate that SMGFM achieves state-of-the-art performance across graph-level and modality-level tasks.

---


### 44. [DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks](https://arxiv.org/abs/2606.12871)

**<font color=#1a73e8>作者：</font>** Jingxuan Han, Wei Liu, Mingyang Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search Agents (SAs) typically leverage large language models (LLMs) to support complex information-seeking tasks by autonomously exploring web sources and synthesizing information into comprehensive responses. For SAs evaluation, prior benchmarks mainly focus on specialized tasks that are unlikely to arise in real-world user scenarios. Moreover, their reliance on coarse task-level rubrics often limits evaluation interpretability. To bridge this gap, we introduce DailyReport, an open-ended benchmark to evaluate SA capabilities on daily search tasks. It contains 150 open-ended tasks with 3,546 associated rubrics, capturing widely discussed and timely information demands of real-world users. Each task is decomposed into subtasks and evaluated with cascade rubrics across disentangled dimensions. Through cascade performance attribution and user-centric aggregation, we derive highly interpretable scores for each dimension, along with a user preference score. Our results on 17 agentic systems show that current systems still fall short of users' expectations. To facilitate future research, our dataset and code are made publicly available at this https URL.

---


### 45. [Multi-Bitwidth Quantization for LLMs Using Additive Codebooks](https://arxiv.org/abs/2606.12876)

**<font color=#1a73e8>作者：</font>** Liza Babaoglu, Shuangyi Chen, Ashish Khisti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed across heterogeneous hardware with varying resource constraints, the ability to adaptively manage the trade-off between performance and efficiency without retraining is critical. We propose Drop-by-Drop, a novel multi-bitwidth post-training quantization framework that enables inference-time precision control over LLM weights from a single trained model. Our method is theoretically grounded in information theory and successive refinement. We establish that LLM weights, which commonly follow a Gaussian distribution, can be optimally reconstructed with increasing fidelity as additional bits are incorporated, under a weighted mean squared error distortion motivated by LLM loss functions. To realize this in practice, Drop-by-Drop incorporates Matryoshka-style supervision into the loss function, exploiting the structure of additive codebooks. Drop-by-Drop produces a single model where ordered subsets of codebooks yield accurate partial reconstructions at each precision level. This approach significantly reduces storage and memory overhead by allowing a single checkpoint to serve multiple bitwidths, while maintaining competitive perplexity and accuracy across major architectures, such as Qwen, LLaMA, Gemma, and Mistral.

---


### 46. [Direct Preference Optimization for Chatbot Fine-Tuning: An Empirical Study](https://arxiv.org/abs/2606.12881)

**<font color=#1a73e8>作者：</font>** Yvonne Qiu, Dezhi Yu, ShuoJia Fu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an approach to fine-tuning large language models using Direct Preference Optimization (DPO), a reinforcement learning technique. Our experimental results demonstrate that DPO simplifies the training pipeline, improves computational efficiency, and achieves competitive performance. The evaluation using BLEU, ROUGE, and cosine similarity metrics indicates effective learning and convergence, though further investigation is needed to address observed training instability.

---


### 47. [HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness](https://arxiv.org/abs/2606.12882)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Wang, Haixin Wang, Alexander Taylor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as agents for long-horizon tasks, yet their performance is shaped not only by model capability and environment design, but also by the harness that mediates agent--environment interaction. Existing harnesses are largely manually engineered, making them difficult to scale as trajectories grow longer and interactions become more complex. In this work, we ask whether harness can be generated by a learnable plug-in module that can be trained in an end-to-end fashion. We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection. HarnessBridge learns two bidirectional projections: observation projection, which distills raw trajectories into compact, decision-relevant states, and action projection, which converts proposed actions into executable transitions or trajectory-grounded rejections. We train HarnessBridge on a harness supervision dataset via unified instruction tuning. On Terminal-Bench~2.0 and SWE-bench Verified, HarnessBridge matches or surpasses strong specialized harnesses while substantially reducing token usage and trajectory length, and generalizes from smaller generators to larger commercial models.

---


### 48. [SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings](https://arxiv.org/abs/2606.12897)

**<font color=#1a73e8>作者：</font>** Julia Ive, Felix Jozsa, Evridiki Georgaki 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to access organisational documentation, including standard operating procedures (SOPs), HR policies and institutional guidelines. However, retrieval-augmented generation (RAG) systems that rely on free-form rewriting can introduce hallucinations and unstable trade-offs between completeness and conciseness, particularly in safety- and compliance-critical settings. Objectives: To evaluate extraction as a hallucination-resistant alternative to rewriting-based RAG and compare strategies that balance precision, recall and safety across document types and model scales. Methods: We compare multiple prompting strategies, including line-number-based source selection, extraction of relevant guideline sentences with explicit safety annotations, and a multi-stage pipeline that refines draft answers using supporting evidence from source guidelines. Experiments are conducted on documents of varying length and structure, including local NHS acute care and oncology guidelines and UK-wide NICE guidelines, using both frontier-scale and locally deployable models. Performance is assessed using automatic metrics and human expert evaluation of relevance and completeness. Results: Line-number selection achieves the strongest results, outperforming direct copying and safety-focused strategies across both large and small models while maintaining high term recall (up to 95%) and close alignment with source text. Safety-oriented approaches improve precision but introduce systematic omissions, while multi-stage filtering further amplifies this trade-off. Performance varies with document structure: line-based extraction excels in protocol-like content, whereas alternative strategies perform better on more verbose documents (up to 97% term recall).

---


### 49. [Magnifying What Matters: Attention-Guided Adaptive Rendering for Visual Text Comprehension](https://arxiv.org/abs/2606.12898)

**<font color=#1a73e8>作者：</font>** Shenglai Zeng, Qirui Wang, Kai Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Text Comprehension (VTC) renders text into images for a vision-language model (VLM) to read, sidestepping LLM context-window limits and powering applications from long-page OCR to multi-page memory QA. Yet existing VTC pipelines treat rendering and layout as a fixed, content-agnostic preprocessing step and offer little mechanistic understanding of how VLMs internally process visualized text. Through a focused empirical study on VTC QA tasks, we reveal that VLMs exhibit a localization-without-utilization regime: evidence-localizing attention emerges sharply in the middle-to-late layers and is largely decoupled from answer correctness, yet simply enlarging the localized spans on the rendered page recovers a large fraction of the failures. Building on these observations, we propose AGAR (Attention-Guided Adaptive Rendering), a training-free, model-agnostic method that leverages a VLM's own middle-to-late layer attention to identify the top-K important visual patches, maps them back to word spans, and re-renders the page with those spans enlarged before re-inferring the answer. Extensive experiments across nine VTC benchmarks (short-form, long-context, and multi-page memory QA) and four VLM backbones show that AGAR (i)consistently improves off-the-shelf VLMs as a plug-and-play enhancement, (ii)composes with VLM post-training to yield further gains, and (iii)remains robust under both visual- and text-side input degradation.

---


### 50. [Zero-source LLM Hallucination Detection with Human-like Criteria Probing](https://arxiv.org/abs/2606.12900)

**<font color=#1a73e8>作者：</font>** Jiahao Yang, Shuhai Zhang, Hailong Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often hallucinate by generating factually incorrect or unfaithful content, posing significant risks to their safe use. Detecting such hallucinations is particularly challenging under the zero-source constraint, where no model internals or external references are available, and detection must rely solely on the textual query-answer pair. In this paper, we propose Human-like Criteria Probing for Hallucination Detection (HCPD), a paradigm that emulates the multi-faceted reasoning of human evaluators. Its core is a Human-like Criteria Probing (HCP) mechanism, in which a LLM agent adaptively decomposes its judgment into a weighted set of interpretable criteria and aggregates criterion-specific scores into a final truthfulness measure. To achieve this adaptive capability, we introduce a reward-based alignment scheme using only weak supervision from semantic consistency. At inference, we employ a multi-sampling aggregation strategy to ensure robust decisions while preserving full interpretability. We further provide theoretical analysis supporting the reliability of our approach. Extensive experiments show that HCPD consistently outperforms state-of-the-art baselines, offering an effective and explainable solution for zero-source hallucination detection. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-128](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
