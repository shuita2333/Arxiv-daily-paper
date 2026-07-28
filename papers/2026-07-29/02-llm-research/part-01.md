# 🧠 大模型相关研究 | 2026年07月29日

> 本类共 **240** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 1. [Semalith v1.4: A Calibrated 184M Safety Classifier Achieving State-of-the-Art Prompt-Injection Detection at 44x Fewer Parameters than Llama-Guard-3-8B](https://arxiv.org/abs/2607.22545)

**<font color=#1a73e8>作者：</font>** Tejasvi C. Addagada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language models in financial-services and agentic settings requires safety classifiers that simultaneously handle prompt injection, regulatory compliance, and general harm, a combination no existing open guardrail addresses in a single inference pass.
Semalith v1.4 is a 184M-parameter DeBERTa-v3-base classifier performing simultaneous three-axis safety classification including prompt injection, general harm, and financial-services regulatory compliance, in a single forward pass. Its 22-class head (BENIGN, nine prompt-injection sub-types, general-harm, eleven BFSI labels) is trained with a 4-class auxiliary super-category head under jointly weighted loss, on a 76,204-row corpus mined from 49 public sources with SHA-1 deduplication against every held-out evaluation set, with 21 of 22 benchmarks at zero contamination (max 0.22%).
Against Llama-Guard-3-8B on 22 held-out benchmarks, Semalith v1.4 wins every prompt-injection evaluation (7/7) and 11 of 18 benchmarks overall at 44x fewer parameters, with FPR = 0.000 on 208 benign agentic prompts vs 0.063 for Llama-Guard-3-8B. On general-harm benchmarks (WildGuardMix, HEx-PHI, HarmBench), Llama-Guard-3 leads; this complementary split is documented in Section 4. Six measured weak spots are disclosed in Section 6.
Deployment guidance: v1.3 is recommended for conversational moderation deployments (ToxicChat F1 0.624); v1.4 is recommended when BFSI label coverage or zero-FPR on benign agentic prompts is the priority.

---


### 2. [SeT-Diff: Towards Semantic Foundation Models for HPC Telemetry and Time-Series](https://arxiv.org/abs/2607.22548)

**<font color=#1a73e8>作者：</font>** Giovanni B. Esposito, Francesco Antici, Daniele Cesarini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data centers and their compute nodes require accurate and flexible digital twins capable of modeling the complex interplay of workloads, environmental parameters, and physical metrics. Current machine learning approaches for HPC and its telemetry typically rely on a static subset of anonymous, fixed-position sensor variables tailored to single tasks. Consequently, these models become obsolete when target tasks change or sensor metrics vary. We propose SeT-Diff, the first foundational model for compute node telemetry and time-series. Unlike rigid architectures, our diffusion-based approach conditions the generative process on each sensor's semantic description, decoupling the system dynamics from the structure of the dataset. Experiments on a real-world supercomputer dataset demonstrate a Mean Absolute Error (MAE) of 0.0470 on reconstruction tasks. SeT-Diff exhibits zero-shot permutation stability, maintaining accuracy with negligible degradation even when sensors are shuffled. A single pre-trained model effectively performs data imputation, forecasting, and virtual sensing - achieving a 0.033 MAE in thermal inference - making SeT-Diff an effective data-driven digital twin for HPC systems.

---


### 3. [MioFFAn: an Annotation Software for Formula Formalization with LLM Automation Capabilities](https://arxiv.org/abs/2607.22552)

**<font color=#1a73e8>作者：</font>** Nicolas Sibuet, Horacio Saggion, Riccardo Rossi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The automatic translation of mathematical expressions in scientific literature into executable symbolic code (a process we refer to as Formula Formalization) is hindered by a severe scarcity of high-quality, ground-truth datasets specialized for technical scientific domains. In this paper, we present MioFFAn, an open-source, document-centric, and customizable framework designed to facilitate rapid annotation for this task. Building upon the MioGatto architecture, we extend existing features to overcome structural limitations and pivot its scope by introducing specific functionalities for Formula Formalization, such as selection of equations of interest and aided symbolic code specification. By allowing users to configure custom taxonomies and properties for identified symbols, and compatible symbolic operators, we ensure the framework is adaptable to diverse specialized scientific fields. Furthermore, MioFFAn is designed to incorporate partial automation via Large Language Models. By defining a modular set of automated sub-tasks with strict output formats, we enable researchers to iteratively refine automation capabilities and evaluate competing strategies using standard NLP metrics. We specify the current automation methodology and perform a preliminary evaluation that demonstrates to efficacy of this human-in-the-loop approach.

---


### 4. [Evaluating the Impact of Reviewer Guideline Design on LLM-Based Automated Peer Review](https://arxiv.org/abs/2607.22553)

**<font color=#1a73e8>作者：</font>** Haowen Li, Yoichi Ishibashi, Masafumi Oyamada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer review is an essential process in scientific research, yet the growing workload has made its automation increasingly necessary. In this study, we analyze how different types of reviewer guidelines, such as official conference guidelines and reviewer-imitating ones generated from high-quality human reviews using LLMs, affect automated peer review. Our experiments show that official conference guidelines produce review results most consistent with human judgments, suggesting that evaluation criteria refined through conference practice serve as effective guidance for automated reviewing as well. In contrast, reviewer-imitating guidelines were generally less effective than official conference guidelines. Furthermore, enforcing strict rubric-style scoring consistently degraded performance, highlighting the importance of allowing subjective and holistic scoring.

---


### 5. [Same Question, Different Answers: Evaluating LLM Reliability Beyond Accuracy](https://arxiv.org/abs/2607.22554)

**<font color=#1a73e8>作者：</font>** Kazem Faghih, Yize Cheng, Shoumik Saha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often achieve strong accuracy on benchmarks, yet it remains unclear how reliably they apply this knowledge when the same question is phrased in different but equivalent ways. In this work, we study how model answers change under meaning-preserving paraphrases across factual question answering and mathematical reasoning tasks. Across four benchmarks and 13 models, we find that model outputs frequently depend on the exact wording of the prompt. While overall accuracy typically changes only modestly across paraphrases, instance-level behavior is far less stable: for many questions, models alternate between correct and incorrect answers depending on phrasing, with mismatch rates reaching more than 23%. Conditioning on questions that are answered correctly in their original form reveals even larger failures measured by answer flip rates, showing that single-prompt correctness is often a poor indicator of reliability. At the same time, we find that models often produce a correct answer for at least one paraphrase of a question, suggesting that the underlying knowledge is present but inconsistently retrieved. Building on this observation, we show that a simple self-paraphrasing strategy can partially recover this latent knowledge and improve performance at inference time. Together, these findings suggest that standard accuracy metrics can mask substantial instability, and that evaluating consistency across equivalent inputs provides a clearer picture of LLM reliability.

---


### 6. [DeepLens Diagnosis Agent: Agentic Workflow Design Lets a Small Reasoning Model Compete with Frontier LLMs](https://arxiv.org/abs/2607.22555)

**<font color=#1a73e8>作者：</font>** Mahmood Bayeshi, Veysel Kocaman, Muhammed Ali Naqvi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical diagnosis is a multi-stage process: extract facts, consult knowledge, generate a differential analysis, and select the best diagnosis with explanations. Frontier LLMs are strong generalists, but single-shot prompting often yields brittle diagnostic reasoning. We present the DeepLens Diagnosis Agent, a five-stage harnessing pipeline (combining model capabilities with disciplined process constraints) centered on a small medical reasoning model (JSL Medical Small 7B v2) and retrieval-augmented generation (RAG). The pipeline enforces structured clinical extraction, disciplined retrieval, constrained candidate generation, explicit evidence triangulation, and an auditable final decision. On the 915-case DiagnosisArena benchmark, the agent achieved 60.14% top-1 diagnostic accuracy, the highest among small and medium-sized models. The same model without the agent workflow achieved 23.99%, a +36-point gain from workflow design alone, despite 88.2% on standard medical benchmarks, showing that diagnostic reasoning under uncertainty requires more than knowledge recall. The agent costs USD 0.0072 per case (24K tokens on A100) with 24-second latency, 35-45% cheaper than Claude Sonnet 4.5 (USD 0.0110) and Gemini 3.1 Pro (USD 0.0128) while outperforming them by +9.70pp and +9.17pp. Harnessing can also correct frontier model failures; workflow constraints can outweigh parameter count or API cost.
Beyond aggregate accuracy, the pipeline produces structured intermediate artifacts that make each stage inspectable and support error localization. These properties support high-stakes settings where traceability, reproducibility, and auditable evidence matter alongside benchmark performance.

---


### 7. [MIITA: Memory-Induced Inference-Time Adaptation for Continual Learning with Small Language Models](https://arxiv.org/abs/2607.22556)

**<font color=#1a73e8>作者：</font>** Dong Li, Yanchi Liu, Xujiang Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) is essential for small language models (SLMs) to adapt to evolving real-world needs in resource-constrained deployments. However, directly updating their limited parameter space causes catastrophic forgetting. While memory-based methods naturally address this by decoupling knowledge retention from parameters, existing approaches designed for large language models (LLMs) rely on abundant storage and strong in-context reasoning that SLMs lack. To address these challenges, we propose MIITA, a Memory-Induced Inference-Time Adaptation framework for supervised CL under constrained storage. MIITA stores supervised experiences as compact correction-direction prototypes with semantic anchors, and retrieves them at inference time using semantic and uncertainty-based cues. The retrieved directions are applied through gated temporary hidden-state adaptation, enabling non-destructive reuse of past supervision without backbone updates, prompt extensions, or test-time backpropagation. A local theoretical analysis links this design to first-order loss reduction, uncertainty-guided retrieval, and directional coverage for retaining old-stage knowledge. Extensive experiments across diverse supervised CL settings show that MIITA consistently improves final performance and mitigates forgetting under fixed memory budgets.

---


### 8. [SF-AMS: Strategic Forgetting for Structured Memory in LLM Agent](https://arxiv.org/abs/2607.22562)

**<font color=#1a73e8>作者：</font>** Ning Yang, Siqi Li, Miaoxin Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Managing long-context dependencies remains a primary bottleneck in LLM agents, as redundant and irrelevant information can degrade multi-step reasoning. Strategic Forgetting for Agent Memory Systems (SF-AMS) is proposed as a framework for maintaining compact high-utility memory by modeling the long-term importance of memory units. SF-AMS replaces static retrieval and heuristic decay with a utility-driven survival mechanism that updates memory importance from usage redundancy and temporal signals, inducing a hierarchical memory structure that prioritizes stable entity-consistent information while filtering noise. On top of this, Composite Importance Scoring integrates semantic and entity level signals to improve retrieval robustness. Experiments on LoCoMo and LongMemEval-s show consistent gains over strong state of the art baselines including LightMem MemO and A-Mem. The largest improvement appears in multi-hop reasoning under Qwen2.5-7B where SF-AMS achieves plus 9.65 F1 over the strongest baseline followed by temporal reasoning under GPT-4o-mini plus 6.91 F1 and open-domain tasks plus 6.53 F1 demonstrating strong cross backbone generalization. These results show that modeling memory importance as a dynamic utility signal is critical for reliable long-context reasoning.

---


### 9. [MedLoCoMo: A Long-Context Multi-Session Medical Dialogue Benchmark for Large Language Models](https://arxiv.org/abs/2607.22566)

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Ziqing Wang, Kaize Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MedLoCoMo is a Medical Long-Context Memory benchmark for patient-specific clinical reasoning over multi-admission medical dialogue. Existing medical QA benchmarks largely test short context knowledge or single document grounding, leaving open whether LLMs can use, connect, and abstain over longitudinal patient histories. We build MedLoCoMo from deidentified MIMIC-IV and MIMIC-IV-Note records by constructing admission-level clinical packets, synthesizing grounded doctor-patient conversations, and generating evidence linked QA items over single-admission, cross-admission, and adversarial unanswerable settings. The benchmark contains 100 patient timelines averaging 1,669.8 turns, 29.7 sessions, and 74,512.2 tokens per conversation. Across the evaluated baselines, cross-admission reasoning is consistently harder than localized evidence use, even when models have long context windows or use external memory or retrieval methods. The code and MedLoCoMo benchmark release is available at this https URL for use and reproducibility.

---


### 10. [Keyword Matters: Unveiling the Energy Sensitivity of On-Device LLM Prompting](https://arxiv.org/abs/2607.22568)

**<font color=#1a73e8>作者：</font>** Ruiyi Tao, Xiaolong Tu, Haoxin Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed on mobile and embedded devices to improve privacy and reduce network latency. Yet on-device inference faces a fundamental constraint: high energy consumption on battery-powered, resource-limited hardware. While model compression and runtime acceleration have been widely studied, the effect of \emph{prompt design} on energy efficiency remains underexplored. This paper presents an empirical study of the relationship between prompt wording and energy consumption for on-device LLMs. Using real power measurements collected on a smartphone, we quantify how linguistic features, particularly imperative keywords and instruction structure, affect decoding length and total energy. Our results show consistent energy differences across verbs and tasks, indicating that prompt engineering is a lightweight lever for improving energy efficiency.

---


### 11. [Reference Feature Atlases for Mechanistic Auditing of Language Models](https://arxiv.org/abs/2607.22570)

**<font color=#1a73e8>作者：</font>** Rui Wu, Tong Che  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Auditing a new language model usually means relearning and reinterpreting its internal features from scratch. We propose a reference feature atlas: a sparse feature library trained once on a reference panel and reused for new targets, which attach by fitting only a linear decoder. This yields two complementary views. The atlas channel reads the target on already interpreted panel features, providing a stable coordinate system across models. The residual channel learns features only from what the atlas fails to reconstruct, making "outside the reference panel" an explicit audit signal.
We train leave-one-out atlases over five 7-9B instruction-tuned models and audit held-out Mistral and Qwen targets. On three controlled LoRA hidden objectives injected into both targets, the residual channel makes the planted mechanism perfectly controllable at runtime while matched controls stay unaffected and recovers the planted objective as the top-ranked latent across both targets; on Mistral, where the per-target SAE and pairwise crosscoder baselines are retrained for a head-to-head benchmark, both baselines fail to do so. On Qwen-2.5, the same channel additionally reveals a panel-relative political-framing cluster; steering it shifts the audited framing metrics while out-of-domain controls remain unchanged.

---


### 12. [SCAIR: Schema-Conditioned Agentic Iterative Reasoning for Enterprise Knowledge Graphs](https://arxiv.org/abs/2607.22571)

**<font color=#1a73e8>作者：</font>** Prateek Chaturvedi, Yuqicheng Zhu, Hongkuan Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph-based Retrieval-Augmented Generation (KG-RAG) enables natural language interaction with structured enterprise knowledge, yet existing agentic approaches that perform well on public benchmarks often fail to generalize to real-world enterprise Knowledge Graphs (KGs), which are dense, schema-driven, and operationally constrained. To address these limitations, we propose SCAIR (Schema-Conditioned Agentic Iterative Reasoning), a training-free framework that integrates structured planning with controlled iterative reasoning by injecting schema-conditioned structural priors and enforcing schema-aware traversal during multi-hop reasoning. Experiments on an enterprise-oriented benchmark constructed from a real-world Configuration Management DataBase (CMDB) demonstrate that SCAIR substantially improves performance over existing KG-RAG methods. Crucially, our study highlights that reliable enterprise graph reasoning cannot rely on generic agentic designs; instead, it must explicitly incorporate the target domain's structural and operational constraints into the reasoning process. We demonstrate that by aligning agent design with business logic, substantial performance gains can be achieved without the need for costly model retraining.

---


### 13. [Schema-Aware Localisation (SAL): Live Schema Grounding and Hallucination Validation for Oracle NL2SQL](https://arxiv.org/abs/2607.22572)

**<font color=#1a73e8>作者：</font>** Sanjay Mishra, Divya Chukkapalli, Ganesh R. Naik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can generate fluent SQL from natural language, but on real enterprise Oracle databases they frequently fail at execution time: columns and aliases are hallucinated and dialect-specific syntax is missed, leading to ORA-00904 invalid-identifier errors. In this setting, failures are primarily due to missing schema grounding: the model cannot know which tables and columns actually exist. This paper introduces Schema-Aware Localisation (SAL), a lightweight middleware layer for Oracle NL2SQL that requires no model retraining. SAL queries Oracle's USER_TAB_COLUMNS catalog to build a live schema map, selects a relevant table subset for each question (falling back to the full schema for multi-table queries), and injects this ground-truth context into the LLM prompt. Generated SQL is then checked by the Hallucination Index (Hidx), which validates every this http URL reference against the live catalog, automatically rewrites predictable prefix errors, and otherwise triggers a structured retry with itemised corrections. We evaluate SAL on 500 TPC-H natural language questions executed against a live Oracle Autonomous Database 23c instance using GPT-4o-mini. Without any schema grounding, execution-grounded truth (EGT; executes and matches the reference result set) is 2.2% (12/500). A hand-written static schema hint brings EGT to 62.0%. SAL, with no manual schema curation, achieves 62.6% EGT (96% simple, 95% medium, 40.7% complex) while reducing execution failures from 97.6% to 2.6%.

---


### 14. [Too much evidence, too little time: From text to actionable recommendations through multi-objective evidence reasoning](https://arxiv.org/abs/2607.22574)

**<font color=#1a73e8>作者：</font>** Adela Bara, Simona-Vasilica Oprea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence-based clinical decision making requires specialists to identify, evaluate and synthesize relevant scientific literature. However, PubMed searches for complex clinical cases often return hundreds of publications that cannot be reviewed manually under time constraints. This study proposes SCEPTER (Single-Case Evidence-driven PubMed-To-rEcommendation Reasoner), a framework for transforming clinical case descriptions into evidence-based recommendations. SCEPTER combines PubMed retrieval, PubMedBERT semantic ranking, large language model (LLM)-based claim extraction, evidence-level weighting, contradiction detection, consensus analysis and multi-objective Pareto claim selection. The framework generates structured evidence syntheses and grounded actionable recommendations. A Paper Q&A module further enables interactive exploration of selected publications. The proposed framework introduces multi-objective reasoning model that integrates literature support, contradiction analysis and interactive literature interrogation into a unified clinical decision-support pipeline. Evaluation on 150 case studies demonstrated that the framework reduced an average search space of 576 papers to 53 retained papers, 7 Pareto-optimal claims and 3 final recommendations, corresponding to an overall compression ratio of 192:1. Despite this reduction, the retained evidence maintained high diversity (entropy=0.901). The ablation study showed that Pareto-based selection increased evidence diversity and recommendation utility compared with conventional ranking approaches.

---


### 15. [Temporal Context Reinstatement Drives Episodic-Like Order Memory in Long-Context Language Models](https://arxiv.org/abs/2607.22575)

**<font color=#1a73e8>作者：</font>** Mathis Pink, Vy Ai Vo, Qinyuan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human episodic memory supports the retrieval of experiences that unfold over extended timescales, yet the computational mechanisms underlying this ability remain debated due to the limited mechanistic accessibility in long-term memory experiments in humans. Long-context LLMs may offer promising ways to reveal plausible computational mechanisms that drive this type of retrieval. Here, we investigate whether and how LLMs capture the core behavioral signatures of episodic memory via a temporal order memory task. Using a new dataset of human behavior based on memory of a full-length novel, we show that models exhibit the same characteristic distance effect observed in humans on this task. We next apply long-context mechanistic interpretability analyses to uncover how models solve this task, and find that model performance relies on a one-dimensional temporal code that is reinstated during retrieval by a single time-reinstatement attention head. These findings support temporal context reinstatement as an important mechanism for episodic-like temporal-order memory in LLMs, offering new insights into how temporal aspects of long-term episodic memory may be instantiated in both artificial and biological systems.

---


### 16. [cMoLLM at Scale: Horizontal Scaling Laws for Mixture-of-LLMs](https://arxiv.org/abs/2607.22577)

**<font color=#1a73e8>作者：</font>** Xin Yang, Yemin Wang, Mingda Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling large language models (LLMs) has driven their success, yet dense Transformers couple capacity and computation: every parameter is activated for every token, making training and inference costs grow linearly with model size-a critical bottleneck as models approach trillion-parameter regimes. We aim to scale capacity through MoE-style mixture throughout the LLM pipeline rather than only the FFN. Prior pipeline-level approaches include ParaScale, which introduces virtual tokens and parallel streams but incurs substantial overhead and suffers from homogenized routing and gradient collapse, and AltUp, which uses an auxiliary prediction branch but offers limited adaptivity and slow convergence. We establish that MoE-style mixture layers can be reformulated as variable-kernel dynamic convolutions, where each expert corresponds to a $1{\times}1$ convolutional kernel and routing implements input-conditioned kernel aggregation. Building on this equivalence, we introduce cMoLLM: a convolutionally gated mixture-of-LLMs that routes over end-to-end streams through fully differentiable dynamic convolution. In GPT-2-style models trained on FineWeb, cMoLLM improves language modeling perplexity and downstream GLUE and SQuAD accuracy under matched compute, with better stream utilization, more stable optimization, and favorable scaling compared to ParaScale- and AltUp-style baselines.

---


### 17. [HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization](https://arxiv.org/abs/2607.22578)

**<font color=#1a73e8>作者：</font>** Size Li, Zhiqing Tang, Hongrui Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of Large Language Models (LLMs) has shifted serving systems from processing isolated requests to orchestrating high-concurrency, multi-tenant agentic workflows. However, existing solutions typically prioritize intra-workflow optimization, largely neglecting the significant potential for inter-workflow optimization. In this paper, we propose HeraSys, an LLM serving system designed to optimize the end-to-end performance of concurrent workflows. Through fine-grained orchestration, HeraSys eliminates cross-workflow computational redundancy via structural node merging and reuse. Furthermore, HeraSys introduces a load-aware joint scheduling policy that dynamically manages execution order by evaluating both inter- and intra-query priorities. By integrating a resource skewing mechanism with adaptive batching and pipeline decomposition, HeraSys effectively mitigates tail latency while maintaining low average latency, thereby substantially improving system throughput. Extensive experiments demonstrate that HeraSys reduces P99 latency by up to 2.17$\times$ and increases serving throughput by up to 1.85$\times$ under strict latency guarantees.

---


### 18. [Multi-Objective Structured Pruning of LLMs for Latency and Model Size Optimization](https://arxiv.org/abs/2607.22583)

**<font color=#1a73e8>作者：</font>** Muhammad Junaid Ali, Smail Niar, El-Ghazali Talbi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved widespread adoption because of their strong reasoning and query-response capabilities. However, deploying them in embedded and edge computing environments remains challenging because of strict latency, memory, and energy constraints. Their large parameter counts and computational demands hinder efficient execution on resource-constrained platforms. Although model pruning has emerged as a viable solution for reducing scale while preserving performance, jointly optimizing layers, attention heads, and Multi-Layer Perceptron (MLP) dimensions remains highly complex. Exhaustively exploring this combined design space is computationally expensive and often leads to local optima or unstable configurations. To address these limitations, we propose a hardware-aware, multi-objective structured pruning framework. The proposed two-stage method explicitly targets latency and model size for efficient deployment on edge devices. In the coarse-grained stage, multi-objective depth pruning removes entire attention and MLP blocks to reduce computational load and memory usage. In the subsequent fine-grained stage, Parallel Bayesian Optimization (PBO) searches for the optimal layer-wise pruning ratios for pruning under latency constraints, while importance-based strategies rank the specific components to be pruned within each layer's allocated budget. Experimental results show that our approach reduces model complexity with minimal impact on commonsense reasoning tasks and zero-shot performance. Our method achieves a favorable trade-off among accuracy, latency, and model size, making it suitable for edge deployment. Across multiple LLMs at 37.5% and 50% pruning ratios, the proposed approach achieves better performance on commonsense reasoning tasks than existing methods while significantly reducing inference cost.

---


### 19. [MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models](https://arxiv.org/abs/2607.22586)

**<font color=#1a73e8>作者：</font>** Jinsong Shu, Chenyang Wu, Zhongle Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Key-Value (KV) caching is essential for efficient inference in multimodal large language models (MLLMs), yet its memory footprint grows linearly with context length and becomes a major bottleneck due to the large number of visual tokens. Recent prefill-stage KV selection methods estimate KV importance from prefilling statistics, implicitly assuming that prefilling-time queries are representative of those encountered during decoding. We show that this assumption breaks down in multimodal inference, where decoding-time queries exhibit substantially larger variance than prefilling-stage representations, leading to unstable KV importance estimation under tight cache budgets. As a result, small ranking errors can disproportionately discard semantically critical visual tokens and degrade grounding and reasoning performance. We propose MM-ShiftKV, a training-free, decode-aware and strictly prefill-only KV selection method. MM-ShiftKV approximates decoding-time query behavior during prefilling by constructing variance-expanded query proxies and estimates prompt KV importance based on their aggregated attention mass. Experiments on multimodal benchmarks demonstrate that MM-ShiftKV consistently outperforms existing methods under strict KV-cache budgets. Our code is available at this https URL.

---


### 20. [TriSP: Tri-Signal Structured Pruning for Large Language Models](https://arxiv.org/abs/2607.22587)

**<font color=#1a73e8>作者：</font>** Manel Kara laoua, Soumia Bouyahiaoui, Aicha Boutorh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across diverse tasks but their deployment is constrained by the memory and compute cost of their parameters. Structured pruning addresses this by removing entire structures such as attention heads and Multi-Layer Perceptron (MLP) neurons to produce smaller dense models that run efficiently on standard hardware. However, existing methods rely on either gradient-based importance estimation, which is memory-prohibitive, or activation-based statistical proxies, which do not directly measure the effect of removal on the loss. Furthermore, the interaction between the importance criterion and the post-pruning recovery strategy has not been systematically studied. We propose TriSP (Tri-Signal Structured Pruning), an importance metric that combines weight magnitude scaled by activation norm with first-order gradient sensitivity via a geometric mean, producing a channel-level score that captures both structural and loss-sensitivity signals. Combined with adaptive per-layer budget allocation and low-rank adaptation (LoRA) recovery, TriSP achieves the lowest perplexity and highest zero-shot accuracy across all tested configurations, reaching 6.80 WikiText-2 perplexity at 20% pruning on LLaMA-7B. Inference throughput improves by 82% at 50% pruning, while still maintaining competitive performance.

---


### 21. [ParBench: A Benchmark for Reliable Evaluation of LLM Parallel Code Translation](https://arxiv.org/abs/2607.22588)

**<font color=#1a73e8>作者：</font>** Samyak Jhaveri, Erel Kaplan, Tom Yotam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern compute-intensive software must migrate across a changing ecosystem of accelerators, programming APIs, compiler stacks, and portability layers, including CUDA, OpenMP, OpenCL, and OpenMP target offload. Large language models and autonomous coding agents are increasingly proposed for such migration, but the field lacks reliable ways to measure whether they preserve the low-level parallel semantics that make translations behaviorally valid, including thread indexing, synchronization, memory management, host-device coordination, and API-specific execution structure.
We present ParBench, a kernel-centric benchmark framework for evaluating LLM-based parallel API translation under executable, reproducible conditions. ParBench fixes the surrounding build, run, and verification infrastructure through declarative benchmark specifications and asks models to translate only the computational kernels. It draws on multiple open-source HPC suites and covers representative cross-API translation directions among CUDA, OpenMP, OpenCL, and OpenMP target offload. To test whether success reflects robust translation rather than surface-form memorization, ParBench includes AST-driven, intended behavior-preserving, baseline-validated source augmentation. Evaluations on state-of-the-art open and proprietary LLMs show persistent barriers to reliable parallel code translation, including direction asymmetry, multi-file coordination, incomplete API adaptation, and uneven robustness to source-level perturbations. Code is available at this https URL.

---


### 22. [Lexical discovery in unknown environments orchestrated by Large Language Models](https://arxiv.org/abs/2607.22591)

**<font color=#1a73e8>作者：</font>** Rafael Sendra-Arranz, Iñaki Dellibarda Varela, Eduardo Rocon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Populations of autonomous agents deployed in unknown environments (e.g. planetary or deep-sea exploration) must develop shared vocabularies to refer to entities that have no name in any human language. We propose the Neuro-Symbolic Lexical Discovery (NSLD) framework, in which a population of LLM-based agents plays a referential game over out-of-distribution visual referents, autonomously self-organising a shared alien lexicon. Each agent combines a frozen CLIP vision encoder with a private FAISS vector index and a text-only LLM. Crucially, discovered alien words are anchored to natural language via semantic proximity in the embedding space, enlarging the human vocabulary with new perceptually grounded words. Consensus is reached in simulations with populations of up to twenty agents and ten visual referents. Convergence dynamics are characterised through three analytical models achieving R^2 > 0.95, representing a first step towards pre-deployment planning in autonomous exploration missions.

---


### 23. [Structure Over Scale: Schema-Constrained Causal Graphs for RAG](https://arxiv.org/abs/2607.22592)

**<font color=#1a73e8>作者：</font>** Marc Saouda, Rajprakash Bale, Eren Aldis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (GraphRAG) grounds answers in structured knowledge, but current systems extract entities and relationships exhaustively, producing graphs whose size and construction cost scale with corpus length rather than with the reasoning a query requires. We introduce HCG-RAG (Hierarchical Causal Graph RAG), which replaces open-ended extraction with schema-constrained causal graphs: an automated pipeline distills a corpus into a fixed, typed vocabulary of causal variables and materializes a compact two-tier graph over it. Our schema-constrained graphs match entity-relation baselines on answer quality at a fraction of the cost: 3-20x fewer nodes, 8x-135x fewer build-time LLM calls than the most LLM-intensive baseline (MS-GraphRAG), and graphs compact enough for a domain expert to audit, correct, and extend. On medical and clinical benchmarks, including a neurologist-validated epilepsy dataset, HCG-RAG matches or exceeds the best entity-relation systems. An ablation isolates the causal graph as a structured retrieval filter, contributing +6 percentage points (pp) over embedding-only retrieval. Across all domains with discoverable hierarchical causal structure, only methods imposing higher-level organization outperform flat entity-relation retrieval, indicating that what is placed in the graph matters more than how many nodes it contains.

---


### 24. [An Agentic Orchestration of Atomistic Simulations](https://arxiv.org/abs/2607.22596)

**<font color=#1a73e8>作者：</font>** Rahul Somasundaram, Adela Habib, Khanh Dang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Atomistic simulations are central to materials design, but their execution involves complex, multi-step workflows that require significant human expertise. Here, we present an agent-based system embedded within the URSA (Universal Research and Scientific Agent) framework that automates the design, execution, and validation of atomistic simulations, demonstrated using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) tool. Our system autonomously selects interatomic potentials, constructs and runs simulations, and performs iterative error recovery within a closed-loop workflow. We evaluate the scientific reliability of the agent by benchmarking its outputs against LAVA, a high-throughput toolkit for LAMMPS and the Vienna Ab initio Simulation Package (VASP) calculations. Our framework reduces manual intervention and trial-and-error, thereby improving the rigor, reproducibility, and scalability of atomistic modeling.

---


### 25. [HyCE-RAG: Hypergraph Chain-of-Evidence Retrieval-Augmented Generation for Explainable Multi-hop Question Answering](https://arxiv.org/abs/2607.22597)

**<font color=#1a73e8>作者：</font>** Hong-Yu An, Yun-Jian Zhang, Chen-Wei Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering requires systems to retrieve evidence from multiple documents and connect scattered facts into a coherent reasoning process. Standard retrieval-augmented generation (RAG) mainly relies on semantic similarity between a query and text chunks, and therefore often fails to model structural relations among entities, facts, and evidence units. Graph-based RAG improves this by introducing graph-structured knowledge, but pairwise edges are still limited in representing higher-order associations involving multiple entities and contexts. We propose HyCE-RAG, a Hypergraph Chain-of-Evidence Retrieval-Augmented Generation framework for explainable multi-hop question answering. HyCE-RAG organizes entities, relations, and contextual evidence into hyperedges, builds a query-aware evidence hypergraph, and performs confidence propagation over entity--hyperedge incidence structures. It then uses confidence-guided evidence assembly to select, connect, and rank evidence paths before answer generation. The scoring process jointly considers semantic relevance, entity connectivity, evidence coverage, relation reliability, extraction confidence, and propagated confidence. By providing the language model with structured evidence chains rather than flat retrieved passages, HyCE-RAG supports more faithful and interpretable reasoning. Experiments on HotpotQA, 2WikiMultihopQA, MuSiQue, and two GraphRAG-Bench subsets show that HyCE-RAG consistently outperforms standard RAG and graph-based RAG baselines in answer accuracy, context relevance, and faithfulness. These results suggest that hypergraph-based evidence organization is a promising direction for post-retrieval reasoning in complex question answering.

---


### 26. [Chart Deception in Vision-Language Models: From Vulnerability to Mitigation](https://arxiv.org/abs/2607.22600)

**<font color=#1a73e8>作者：</font>** Ridwan Mahbub, Mohammed Saidul Islam, Md Tahmid Rahman Laskar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Information visualizations are widely used to communicate patterns, trends, and outliers, yet deceptive design choices-such as truncated or inverted axes, distorted aspect ratios, inappropriate encodings, and misleading color mappings-can systematically alter interpretation while preserving the underlying data. As Vision-Language Models (VLMs) are increasingly used for chart understanding and analytical reasoning, assessing their robustness to such deceptive visualizations has become critical for trustworthy data analysis. We introduce VisDeception, the first controlled paired benchmark for evaluating the robustness of VLMs to misleading chart designs. The benchmark contains 1,600 paired faithful and misleading charts spanning eight major categories of deceptive visualization tactics, where each misleading chart is paired with a faithful counterpart generated from the same underlying data. To isolate deception-induced reasoning errors from baseline chart-understanding errors, we introduce the Deception Score, a paired evaluation metric that quantifies how misleading visualizations shift model responses away from the faithful interpretation of the data. Across 32,000 responses from 10 state-of-the-art VLMs, we find that even advanced models remain highly vulnerable to deceptive visual manipulations. To improve robustness, we further propose an inference-time multi-agent mitigation framework that grounds reasoning in structured chart metadata extracted from the visualization before answer generation, enabling models to reduce the influence of deceptive visual cues without requiring explicit user instructions. Together, our findings reveal important reliability gaps in current chart-understanding systems and establish benchmark-driven evaluation, deception-aware metrics, and structured reasoning as promising directions for developing more trustworthy VLMs for visual analytics.

---


### 27. [DeepLook: Deeper Thinking with Lookahead](https://arxiv.org/abs/2607.22602)

**<font color=#1a73e8>作者：</font>** Tingxin Yang, Zefeng Wang, Mengyue Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling has emerged as a powerful paradigm for improving large language model reasoning, often delivering larger gains on difficult reasoning tasks than parameter scaling alone. However, existing approaches remain inefficient in how compute is allocated within a reasoning trace. Motivated by the observation that reasoning failures often exhibit an early onset of uncertainty before a wrong answer become explicit, we introduce DeepLook, a training-free monitor-and-intervene decoding framework that concentrates lookahead compute at uncertainty bottlenecks. DeepLook aggregates token-level confidence into segment-level signals, triggers when confidence drops relative to recent history, and explores candidate continuations with fixed-horizon lookahead. Branches are ranked by Average Lookahead Confidence (ALC), the average segment-level confidence over rollout continuations, then pruned and aggregated through voting. On four competition-style mathematics benchmarks across DeepSeek-R1-8B, Qwen3-32B, GPT-OSS-20B, and GPT-OSS-120B, DeepLook shifts the accuracy--token-cost Pareto frontier: it improves accuracy over DeepConf-low in 11 of 16 settings while reducing dataset-level token generation by 87.3% on average, including gains of +3.1 on AIME25 with Qwen3-32B and +8.8 on BRUMO25 with GPT-OSS-20B. These results show that selective, future-aware intervention yields substantially stronger accuracy--cost trade-offs than uniformly scaling complete reasoning trajectories. Code is available here.

---


### 28. [Group Preference Collapse in Personalized Multimodal Large Language Models](https://arxiv.org/abs/2607.22603)

**<font color=#1a73e8>作者：</font>** Fan Lyu, Wenqi Zhang, Joost van de Weijer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized multimodal large language models (MLLMs) aim to generate user-specific responses, but existing methods mainly rely on profile-level information and overlook diverse user preferences. We identify group preference collapse, where multi-user personalized MLLMs become insensitive to individual preferences and drift toward dominant population-level choices due to suppressed preference signals and unreliable preference use during generation. We propose PrefMoE, a preference-centric framework that separates stable profile information from preference-related representations. PrefMoE decomposes preferences into shared prototypes and personalized residuals, preserves individualized residuals with imbalance-aware learning, counterfactual pseudo-user augmentation, and residual decorrelation, and routes profile and preference factors through separate LoRA adaptation paths. Experiments across multiple MLLM backbones show that PrefMoE improves preference-sensitive personalization while substantially reducing preference collapse. Project page: this https URL.

---


### 29. [Evaluating LLMs as Interpretable Controllers for Dynamical Systems](https://arxiv.org/abs/2607.22609)

**<font color=#1a73e8>作者：</font>** Aleksander Østensen, Alberto Mino Calero, Anastasios M. Lekkas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for decision-making and reasoning tasks, yet their potential as controllers for physical systems remains largely unexplored. This work investigates whether LLMs can function as interpretable controllers for a dynamic thermal environment, examining their ability to follow setpoints, interpret natural-language commands, reason about actuator effects, and incorporate prior model-based knowledge. Five LLMs of varying scales are evaluated under multiple scenarios, including settings with penalties on heater or fan usage and cases where the models have access to a physics-based prediction tool. The results show that control performance depends on model complexity: while low- and mid-scale models frequently misinterpret actuator dynamics or generate inconsistent reasoning, high-complexity models such as Qwen-3~14B and GPT-4o achieve accurate temperature tracking, stable actuator usage, and coherent explanations aligned with physical principles. Incorporating a physics-based model significantly improves control smoothness and energy efficiency by enabling anticipatory decision-making. A detailed reasoning taxonomy further reveals a clear progression from causal misinterpretation in smaller models to cohesive and temporally aware reasoning in larger ones. The findings demonstrate that LLMs can act as interpretable controllers when sufficiently capable and appropriately grounded in domain knowledge, highlighting promising opportunities for hybrid model-based and language-driven control strategies that can provide plausible explanations.

---


### 30. [Tokengeist: Multi-Turn Attribution Tracing in Agentic Conversations](https://arxiv.org/abs/2607.22610)

**<font color=#1a73e8>作者：</font>** Jessica Tang, Shraddha Barke, Sharad Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model produces a response in a multi-turn conversation, which tokens from prior turns shaped that answer, and how did those dependencies propagate across prior turns? Existing context attribution methods process the full context in a single pass, recovering surface-level dependencies but missing the layered, non-linear structure of real-world dialogues and multi-step reasoning tasks. We introduce multi-turn context attribution (MTCA): given a target span in a model response, the task of tracing attribution backward across turns to identify not only which prior turns were directly relevant, but also how those turns themselves depended on earlier context. We propose Tokengeist, an attribution-method-agnostic and scalable framework that recovers full dependency paths by casting attribution as a recursive traversal of a directed acyclic graph (DAG) over conversation turns. We will release MTCABench, a benchmark of 3,845 target spans across 665 multi-turn conversations, annotated with gold provenance graphs reaching depths of up to 14, across four dependency types. Across four open-weight models, flat attribution methods fail to recover multi-hop dependencies, achieving under 20% source recall, while Tokengeist reaches 90%. Our results reveal systematic failure modes of single-pass attribution -- which we term provenance collapse -- and motivate attribution methods that reason recursively across turns.

---


### 31. [Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure](https://arxiv.org/abs/2607.22611)

**<font color=#1a73e8>作者：</font>** Arun Malik, Deepal Jayasinghe, Bradley Klemick 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of autonomous AI agents in production infrastructure introduces fundamental security challenges that traditional role-based access control (RBAC) models cannot address. Unlike deterministic automation, AI agents exhibit stochastic behavior, making conventional trust models insufficient for governing their access to critical systems. This paper presents a decentralized, multi-layered access control architecture designed specifically for agentic AI systems operating in critical cloud infrastructure. Our framework introduces four key innovations: (1) a compound identity model that binds agent actions to delegated human authority, (2) a hierarchical permission system spanning five granularity levels from global platform access to per-parameter constraints, (3) a decentralized policy ownership model where tool teams independently govern their authorization boundaries, and (4) progressive trust escalation with safety interlocks that prevent autonomous agents from executing high-risk operations. We ground our design in the OWASP Top 10 for LLM Applications (2025) threat taxonomy and demonstrate how each architectural decision mitigates specific attack vectors. Deployed in production at a major cloud provider managing network infrastructure across hundreds of datacenters, the system enforces granular access control for 20+ specialized AI agents and 60+ deterministic playbooks processing thousands of operations daily while maintaining zero unauthorized write operations over eight months of production deployment. We present empirical data on access pattern distributions, denial rates, and the effectiveness of layered authorization in preventing privilege escalation by non-deterministic actors.

---


### 32. [DynaResize: Runtime GPU Reallocation for Disaggregated LLM Post-Training](https://arxiv.org/abs/2607.22614)

**<font color=#1a73e8>作者：</font>** Hanlin Du, Zhiyuan Yan, Haiquan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RL-based LLM post-training increasingly disaggregates Rollout and Training across separate GPU resources, but static GPU partitioning suffers from severe pipeline bubbles under long-tail rollout latency. We present DynaResize, a runtime GPU reallocation system that dynamically switches GPUs between Rollout and Training to balance stage execution times without changing RL semantics. DynaResize decomposes resizing into fine-grained operations and removes non-startup-critical work from the critical path through communicator reuse, bounded state staging, and hysteresis-based resizing. Experimental results show that DynaResize can improve end-to-end throughput by 66.5% and reduce total execution time by 33% over the optimal static configuration, while hiding 27% of role-switching overhead.

---


### 33. [Opti-Q: A Constraint-Based Optimization Framework for Multi-LLM Question Planning](https://arxiv.org/abs/2607.22621)

**<font color=#1a73e8>作者：</font>** Aamir Hamid, Bharg Barot, Satvik Racharla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) enable strong question answering (QA), budgeted deployment is complicated by nondeterminism and heterogeneous resource profiles (cost, latency, and energy). We present OPTI-Q, a database-inspired, cost-based optimizer that implements a plan-before-execute paradigm for multi-LLM orchestration. OPTI-Q models LLM invocations as physical operators in an execution DAG and, for each question, searches for plans that optimize answer quality (QoA) while trading off financial cost, latency, and energy under user-specified resource constraints. Plans can include sequential operators that pass intermediate answers as context and parallel/blend operators that run models concurrently and merge their outputs. To search this space without executing each candidate plan, OPTI-Q uses PERFDB, a statistics catalog populated and refreshed from benchmarks and execution traces, to estimate the QoA and resource costs of both individual operators and composed subplans. Using these estimates, OPTI-Q performs Pareto-frontier search and selects a final plan based on user preferences. On MMLU-Pro and SimpleQA under user-specified budgets, OPTI-Q improves average QoA by ~58% and ~41% over baselines at comparable cost, demonstrating that database-style planning yields better quality-resource trade-offs for multi-LLM QA.

---


### 34. [Learning When to Reason for Text-to-SQL via SFT and DPO](https://arxiv.org/abs/2607.22622)

**<font color=#1a73e8>作者：</font>** Soohyuk Jang, Jiheum Yeom, Nohil Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent Text-to-SQL methods rely heavily on reasoning-centric paradigms such as Chain-of-Thought (CoT), achieving substantial gains on complex benchmarks at the cost of high inference-time overhead. However, a large fraction of real-world queries are simple lookups or aggregations that can be resolved without multi-step deduction, making forced reasoning wasteful. Thus, we propose AutoThinkSQL, a framework that integrates an auto-thinking mechanism into both Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) on Text-to-SQL. Our approach enables the model to dynamically bypass reasoning for simple queries while invoking deep CoT for complex queries. On Qwen3-Coder-30B-A3B, our method achieves consistent gains compared to the best counterpart baseline on both Spider and BIRD benchmarks while simultaneously reducing average output tokens by 24.6% and 18.3%, and average latency by 17.1% and 11.5% compared to CoT-only generation. Further analysis indicates that the model learns to align its reasoning decisions with query difficulty.

---


### 35. [TokenMem: Faithful Knowledge Injection for Frozen LLMs](https://arxiv.org/abs/2607.22625)

**<font color=#1a73e8>作者：</font>** Chengzhang Yu, Chenyang Zheng, Zening Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enhances large language models (LLMs) with external knowledge, but suffers from knowledge conflicts: when retrieved information contradicts parametric memory, the shared self-attention pathway produces unpredictable outputs. We present TokenMem, a lightweight memory system that injects knowledge into frozen LLMs through a dedicated cross-attention channel, bypassing competition with parametric memory in the residual stream. TokenMem trains only a thin gating adapter ($\sim$3-7M parameters) via a two-phase curriculum: first learning general knowledge utilization, then strengthening faithful compliance under counterfactual knowledge. In controlled experiments on five models spanning three families (Qwen3-4B/8B/14B, LLaMA-3.1-8B, OLMo-3-7B), TokenMem achieves 69-70% Knowledge Compliance (KC) on counterfactual benchmarks, compared to 20-52% for vanilla RAG, a gap of up to 49 percentage points. Ablation studies show that the two-phase curriculum is critical: removing Phase 2 collapses KC to near-zero. Mechanistic analysis reveals that the gate adapter learns a conflict-aware, layer-specific injection strategy without explicit supervision.

---


### 36. [Masked Distillation: Internalizing the Chain-of-Thought in Language Models](https://arxiv.org/abs/2607.22629)

**<font color=#1a73e8>作者：</font>** Durgesh Kalwar, Vardhan Palod, Subbarao Kambhampati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) produce long, explicit chains of intermediate steps before generating a final answer at inference time. These intermediate traces dominate latency, memory usage, and serving cost, even though the final answer correctness is not causally related to the trace correctness and the trace length is not a reliable indicator of the problem complexity. This raises a natural question: can the computation expressed in these intermediate tokens be internalized into the parameters of a language model, enabling it to produce answers directly (or with much shorter intermediate traces)? We introduce \textit{masked distillation}, a knowledge-distillation framework in which a student LLM is trained to predict only the solution tokens conditioned on the question, while a reasoning teacher provides feedback on the student's responses after conditioning on the question and its own CoT trace. We instantiate this framework in two settings: (i) a \textit{self-distillation} setting, in which the same model serves as the teacher in thinking mode and as the student in non-thinking mode, and (ii) a \textit{dual-model} setting, in which a larger reasoning teacher supervises a separate smaller non-thinking student over the solution tokens. By treating intermediate tokens as a scaffold which reasoning models use to fit over the solution tokens, We additionally vary the length of intermediate-token scaffolding the student is supervised on, interpolating between full internalization (the student emits only the solution) and no internalization (the student emits the full trace before the answer). We evaluate the framework through controlled experiments on two reasoning domains: GSM8K (grade-school arithmetic) and Countdown (a number-puzzle search task).

---


### 37. [VlogReward: Learning Multi-Dimensional Evaluation for Vlog Editing](https://arxiv.org/abs/2607.22632)

**<font color=#1a73e8>作者：</font>** Yexiang Liu, Wen Zhong, Sijie Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid rise of vlogs as a personalized storytelling medium has created a demand for automated systems to evaluate and refine vlog editing plans. However, vlog assessment is highly subjective and remains challenging due to a lack of standardized criteria, dataset and benchmark, and effective reward models. To address these challenges, we define a comprehensive vlog evaluation framework guided by professional vlog creators and product managers, establishing a taxonomy of six key dimensions, i.e., Creativity, Consistency, Concept Design, Cinematography, Narration, and Pacing. Subsequently, we curate a large-scale dataset of 100k vlog edits and a dedicated benchmark, VRMBench, to evaluate the vlog rewarding capabilities of Multimodal Large Language Models (MLLMs). Finally, we present VlogReward, a robust vlog reward model that can provide both fine-grained multi-dimensional scores and actionable feedback for iterative refinement. Technically, we enhance the Group Relative Policy Optimization (GRPO) framework by introducing an adjustable inter-group comparison reward, which mitigates the "direction blindness" issue of standard GRPO and enables the model to better distinguish varied-quality edits. VlogReward achieves state-of-the-art results that significantly outperform existing MLLMs, including GPT-5 and Gemini-3-Pro. We hope that our study can help vlog creators and foster automated vlog evaluation and refinement systems.

---


### 38. [PRESTO: Prefix-Aligned Tree Drafting for Diffusion Speculative Decoding](https://arxiv.org/abs/2607.22634)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Zhifan Ye, Qi Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have emerged as a promising alternative to autoregressive (AR) LLMs, generating tokens in parallel. This makes them effective draft models for speculative decoding (SD), producing an entire block of draft tokens in a single forward pass. Yet existing diffusion-based drafting methods rely on linear drafting, even though dLLMs emit multiple candidate tokens across positions, inducing a large combinatorial space of decoding paths. Consequently, they limit acceptance length and decoding efficiency. To exploit this multi-candidate structure, we apply tree-based drafting to diffusion drafters, enabling exploration of diverse candidate paths. However, we find that naive tree drafting is suboptimal: diffusion marginals are prefix-blind, mismatching the prefix-based AR verification and yielding unreliable path ranking. We propose PRESTO, a principled framework that extends tree-based drafting to diffusion drafters while resolving the fundamental mismatch between diffusion draft confidence and prefix-based AR verification through PREfix-aligned Scoring and priority-based Tree search for diffusion speculative decOding. The key principles behind PRESTO are that (1) candidate ranking should align with the prefix-based nature of AR verification, and (2) tree construction should prioritize candidate paths with high verification potential to maximize acceptance length. Extensive experiments show that PRESTO achieves up to an average of $1.5\times$ end-to-end throughput speedup on the state-of-the-art dedicated diffusion drafter SD and an average of $1.12\times$ on self-speculative diffusion LLMs across diverse benchmarks.

---


### 39. [TRACE: Business Rule-Grounded Reasoning Curriculum for Knowledge-Preserving Parametric Tool Retrieval in Enterprise LLMs](https://arxiv.org/abs/2607.22639)

**<font color=#1a73e8>作者：</font>** Sai Shruthi Sistla, Ashutosh Hathidara, Christopher Toukmaji 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parametric retrieval enables LLMs to retrieve tools implicitly by assigning each API a unique virtual token and training the model to generate it via constrained beam search. Toolsense shows that this regime has two critical drawbacks: it destroys parametric tool knowledge during training, and its beam-search decoding is too slow for real-time deployment. We introduce TRACE (Tool Retrieval via Augmented Chain-of-thought and Enterprise rules), a two-stage curriculum that resolves this dissociation. Stage 1 reuses the multi-format memorization SFT from ToolSense to seed tool knowledge with LoRA. Stage 2 is our core contribution: the model is trained to emit a thinking trace before producing a JSON list of tool tokens, using two data sources -- RRB pairs from ToolSense and queries synthesized to target business rules curated by domain experts -- both augmented with reasoning traces. This training objective preserves Stage 1 MCQ and QA probing accuracy while enabling single-beam greedy decoding at production latency. Evaluated on a combined enterprise catalog of 8,300+ tools across two enterprise product lines, TRACE training for Stage 2 not only preserves but improves tool understanding: MCQ accuracy gains +3.2 pp and QA probing gains +9 pp over Stage 1. On retrieval, TRACE achieves ~86% recall on Domain A and ~60% on Domain B -- compared to embedding baseline performance of ~27% & ~52% -- both with single-beam greedy decoding, making it directly deployable at production latency.

---


### 40. [CRAFT: Learn the Schema, Execute the Plan](https://arxiv.org/abs/2607.22642)

**<font color=#1a73e8>作者：</font>** Aakash Kolekar, Sahika Genc, Shahriar Shariat 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise coding agents translate natural-language analytical requests into executable code over proprietary APIs, schemas, and metric definitions. Yet the prevailing deployment pattern injecting exhaustive schema and tool documentation into each prompt increases inference overhead, complicates schema evolution, and undermines reliability in multi-turn analysis. We investigate whether stable schema knowledge and tool-use behavior can instead be acquired through post-training while preserving the consistency required for production-facing analytics. We present CRAFT, a two-stage post-training recipe for schema-grounded coding agents. First, schema-stripped PLAN supervised fine-tuning learns domain-structured plans and executable behaviors from validated trajectories without exhaustive prompt-time schema injection. Second, execution-shaped reinforcement learning aligns the policy for tool selection, code quality, plan-code consistency, and recovery from failed executions. Training trajectories are curated through a Tri-Gate filter combining execution validation, data-integrity checks, and LLM-judge reasoning audit. We evaluate CRAFT for planned rollout in advertising analytics, covering campaign performance analysis, metric drill-downs, entity-level performance analysis, and multi-turn analytical refinement. The enterprise evaluation environment incorporates beta APIs as the agent-facing tool surface and spans 25 schema-linked core entities and 30 agentic workflows. Relative to a schema-stuffed baseline, CRAFT improves composite Agent Score by +9.6 pp, consistency by +4.1 pp, and multi-turn coherence by +4.2 pp, while reducing input-token burden by approximately 9x and schema-discovery loops by up to 5x. We further report deployment tradeoffs, reward-shaping limitations, and training-infrastructure extensions required for multi-turn tool-use reinforcement learning in enterprise settings.

---


### 41. [Reason Before You Retrieve: Agentic Planning for Multi-modal RAG](https://arxiv.org/abs/2607.22643)

**<font color=#1a73e8>作者：</font>** Tianyu Yang, Shir Simon, Zhenzhen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval-augmented generation (mRAG) aims to answer image-text queries with external knowledge, but most existing systems still retrieve directly from raw multimodal input over a flat evidence space. This design often struggles with two key challenges: the retrieval target is under-specified because the question intent must be grounded to the correct visual referent, and the search space is weakly structured, forcing semantically distinct evidence to compete in a single global ranking step. We propose MM-R2, a multimodal agentic retrieval framework that reasons before retrieval by explicitly modeling both what to retrieve and where to search. MM-R2 first constructs an intent-grounded retrieval state from the image-question pair, capturing the information need, grounded referent, and retrieval constraints. It then performs retrieval over a structured KnowledgeMap, where the agent selects relevant retrieval units before issuing grounded queries within them. To enable this capability, we build MM-R2-Traj, a large-scale trajectory dataset of multi-step retrieval processes, and adopt a two-stage post-training strategy with supervised fine-tuning and GRPO. Experiments on Infoseek and Encyclopedic VQA datasets show that MM-R2 substantially outperforms strong baselines on answer accuracy while also yielding more interpretable and verifiable retrieval trajectories.

---


### 42. [Extracting Algorithms in Pre-trained LLMs: A Case on Hidden Markov Models](https://arxiv.org/abs/2607.22646)

**<font color=#1a73e8>作者：</font>** Yijia Dai, Zhaolin Gao, Yahya Sattar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) display a striking ability to predict next observations from Hidden Markov Models (HMMs) via in-context learning (ICL), but the algorithm underlying this capability remains undetermined: prior work has proposed several candidates without consensus, and none has been grounded in the model's internal activations. We close this gap with a three-stage pipeline. First, we empirically compare LLM behavior against a suite of candidate algorithms and narrow the space to three classes -- though no single class explains LLM behavior across all HMM settings and sequence lengths. Second, we derive theoretical connections between the three classes and show how each can be implemented in-context by a Transformer, validating the construction in a small trained Transformer. Third, returning to pre-trained LLMs, we introduce the Principal Activations Probe (PAP), a layer-wise probing and intervention method that isolates algorithmic signals in model activations. PAP reveals low-dimensional linear representations that causally drive model predictions and track empirical ICL performance. PAP further reveals how these representations shift with properties of the underlying HMM regime; distinct computational stages are localized to different layers. Together, our results connect the in-context behavior of pre-trained LLMs to the underlying internal mechanisms and advance our understanding of how LLMs perform ICL on HMMs.

---


### 43. [STAIF: A Stage-wise Optimization for Complex Instruction Following](https://arxiv.org/abs/2607.22649)

**<font color=#1a73e8>作者：</font>** Jian Hong, Chen Cheng, Quan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Following complex instructions with multiple explicit constraints remains a fundamental challenge for large language models (LLMs). Existing alignment methods, such as DPO, optimize holistic reward signals that often underemphasize strict satisfaction of individual constraints, particularly under out-of-distribution or multi-constraint settings. In this paper, we propose STAIF, a stage-wise optimization framework that decouples the alignment of subjective (soft) constraints from the optimization of objectively verifiable (hard) constraints. Stage 1 applies preference optimization with multiple negative samples to sharpen sensitivity to soft constraints, while Stage 2 applies Reinforcement Learning with Verifiable Rewards (RLVR) to enforce strict compliance with hard constraints. To support this method, we construct STAINSTRUCT, a high-quality bilingual (English, Chinese) dataset of approximately 31,000 complex multi-constraint instructions. Extensive analyses validate the design of STAIF and show state-of-the-art performance on representative benchmarks against strong baselines, as well as genuine generalization.

---


### 44. [ARdena: Scenario-driven control of real-time LLM agents](https://arxiv.org/abs/2607.22651)

**<font color=#1a73e8>作者：</font>** Luka Borozan, Domagoj Matijević  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled increasingly capable conversational agents, but reliably controlling their behavior in real-time interactive environments remains a significant challenge. Existing approaches often rely on model fine-tuning or alignment procedures that are difficult to adapt to changing interaction requirements. This paper introduces layered scenario-driven LLM control, a framework that enables runtime behavior control through structured prompting. By combining persistent context with scenario-specific constraints, the approach allows agent behavior to be modified during interaction without changing the underlying model. The framework is implemented in ARDena, a real-time multimodal embodied agent that integrates speech interaction, visual perception, tool use, and avatar-based response generation. The proposed approach is evaluated with respect to control effectiveness, response latency, and operational stability. The results demonstrate that scenario definitions alone can produce substantially different interaction behaviors while maintaining stable real-time operation, highlighting the effectiveness of scenario-driven prompting for controlling LLM agents.

---


### 45. [KG2Code: Bridging Knowledge Graphs and Large Language Models via Executable Code for Question Answering](https://arxiv.org/abs/2607.22652)

**<font color=#1a73e8>作者：</font>** Yike Wu, Nan Hu, Guilin Qi 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent research has explored the integration of knowledge graphs (KGs) with large language models (LLMs) to enhance their performance on downstream knowledge-intensive tasks, particularly knowledge graph question answering (KGQA). Existing approaches primarily combine LLMs with KGs through retrieval-augmented generation (RAG)-based, agent-based, and SPARQL-based methods. Although these methods have achieved notable success, they still suffer from several limitations, including structural information loss, unfaithful reasoning, and limited flexibility and generalization. To address these challenges, this paper proposes KG2Code, a novel approach that transforms knowledge graphs into a code-based representation, preserving structural semantics while naturally aligning with the code-aware pretraining of modern LLMs. Based on KG2Code, KG2Code-QA is further introduced as a KGQA framework that formulates KGQA as a code generation task. This formulation enables the generation of verifiable reasoning traces and executable code, thereby substantially mitigating the impact of hallucinations. In addition, an automated pipeline is developed to construct a large-scale, high-quality code corpus for effectively training open-source LLMs on KG2Code-QA. After training, LLMs are able to perform KGQA in zero-shot scenarios. Extensive experiments demonstrate that the proposed approach significantly outperforms existing KG-enhanced LLM methods for KGQA, while exhibiting strong generalization to unseen KGs. The code and data are available at Github.

---


### 46. [Do Language Models Converge to Themselves? Recursive Self-Refinement as Textual Relaxation](https://arxiv.org/abs/2607.22653)

**<font color=#1a73e8>作者：</font>** Xuening Wu, Qianya Xu, Yanlan Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in recursive refinement workflows, where an initial draft is repeatedly revised by the same model. Despite their growing use, the long-term dynamics of such workflows remain poorly understood. Does repeated refinement continue to improve outputs indefinitely, or does it converge toward a stable textual form?
We study recursive self-refinement as a dynamical process in which repeated LLM revision drives text toward a model-preferred soft fixed-point region. Using GPT-5.5, we generate 10-step refinement trajectories for 50 ICML 2025 abstracts under both default-temperature and deterministic decoding, and additionally evaluate 15 ICML 2020 abstracts. We analyze normalized edit distance, exact and approximate fixed points, word-count stability, exponential relaxation, and external LLM-as-a-judge evaluation.
Across all settings, refinement trajectories rapidly saturate. Most edits occur within the first few iterations, after which trajectories enter a soft fixed-point region with only minor surface-level changes. Deterministic decoding reaches exact fixed points earlier and exhibits smaller residual fluctuations than default-temperature decoding, while both achieve universal approximate convergence. The average edit magnitude follows a consistent exponential relaxation pattern, suggesting convergence toward a model-preferred textual equilibrium rather than open-ended optimization. External evaluation indicates that converged abstracts improve clarity, conciseness, and scientific style while preserving technical meaning.
These findings support a dynamical-systems view of LLM self-refinement and motivate practical stopping criteria based on edit-magnitude saturation.

---


### 47. [EventOD: Event-Aware OD Flow Generation via LLM-Guided Semantic Modulation](https://arxiv.org/abs/2607.22655)

**<font color=#1a73e8>作者：</font>** Jie Zhao, Jie Feng, Can Rong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Estimating origin-destination (OD) flows under disruptive events is important for disaster response and urban resilience. Existing deep OD models trained on routine mobility often degrade when extreme events abruptly alter regional functions and population activities, while retraining a new generator for each event is impractical under limited event-time supervision. We propose EventOD, an event-adaptive OD generation framework that steers a pretrained OD generator using structured event semantics. EventOD first uses a large language model to infer region-level functional and demographic control vectors from coarse event observations. It then learns two lightweight adaptation modules, AlphaNet and BetaNet, to calibrate the magnitude of these semantic shifts, and further introduces a retrieval-augmented fallback pathway for scenarios with sparse supervision. The resulting event-conditioned features are injected into a pretrained graph diffusion OD model through input-level modulation, enabling event-aware adaptation without updating generator parameters. Experiments on hurricane- and pandemic-induced mobility across U.S. counties show that EventOD consistently improves both reconstruction accuracy and distributional fidelity over strong baselines. Source code is available at this https URL.

---


### 48. [Between Suppression and Collapse: Evaluating Narrative Unlearning with LENS](https://arxiv.org/abs/2607.22657)

**<font color=#1a73e8>作者：</font>** Viktoriia Makovska, George Fletcher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reproduce disinformation-aligned narrative frames as plausible explanations, raising the question of whether existing machine-unlearning algorithms can suppress this behavior. We introduce Level-based Evaluation of Narrative Suppression (LENS), a contextualization based evaluation protocol for testing target narrative reproduction across direct, attributed, contrastive, and abstract resistance levels. We evaluate two source-grounded narratives: one framing Russia's war against Ukraine as forced by NATO expansion, and one framing the United States as exploiting or abandoning Taiwan. The experiments cover four near-12B multilingual instruction models: Lapa LLM, Gemma-12B, Qwen-14B, and TAIDE-Gemma.
We introduce the Suppression-Collapse Efficiency (SCE) score as a checkpoint selection summary that rewards target-narrative suppression while penalizing degraded outputs. Our results shows that selected checkpoints can reduce narrative reproduction and suppression may transfer beyond direct forget prompts. We also report entity recovery as a separate side effect: abstract A/B/C prompts can cause models to recover the real-world actors associated with the target frame after unlearning. These findings demonstrate that LENS is a successful diagnostic protocol for both reporting and guiding the further study of the deeper structure of narrative unlearning.

---


### 49. [StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech](https://arxiv.org/abs/2607.22658)

**<font color=#1a73e8>作者：</font>** Yuzhe Wang, Thomas Thebaud, Jennifer Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech dialogue models increasingly depend on prosody and interactional nuance to convey social intent, yet benchmarks for these cues remain limited. We introduce StanceBench, a benchmark for measuring interpersonal stance in conversational speech and evaluating audio-capable LLMs as automated judges. Using the Seamless Interaction corpus, StanceBench (1) specifies 9 stance dimensions via role-prompt poles, (2) standardizes single-speaker and interaction-based evaluations, and (3) reports LLM-as-a-judge robustness, bias, and stance inference. Across evaluated stances, empathy and politeness are the easiest. Warmth and assertiveness are moderately separable with positivity skew/asymmetry. Honesty is the hardest and shows high prompt order bias, consistent with needing cross-turn evidence. Attentiveness is separable but aligns weakly with humans. Interaction stances are more context-sensitive, with threshold gaps and high variance, especially conflict regulation.

---


### 50. [TRE: Training-Free Hallucination Detection for Diffusion Language Models](https://arxiv.org/abs/2607.22661)

**<font color=#1a73e8>作者：</font>** Pengcheng Weng, Yanyu Qian, Yue Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (D-LLMs) have recently gained increasing attention, yet their reliability is significantly hindered by the hallucination problem. Existing hallucination detection approaches for D-LLMs mainly follow a training-based paradigm, relying on data-driven training to optimize the detector. Such reliance not only limits their generalizability across domains models but also incurs additional training cost and deployment overhead. To address these limitations, we propose TRE, a training-free hallucination detection metric for D-LLMs. TRE is a parameter-free and single-run metric that estimates hallucination risk directly from the entropy signals of a single generation, without requiring any detector training or repeated sampling. TRE extracts entropy signals within the D-LLM decoding process along both the spatial and temporal dimensions. From a token-level spatial perspective, we focus on revealing tokens as the most informative carriers of uncertainty, capturing where uncertainty is actively committed. From a diffusion step-level temporal perspective, we empirically identify the dominance of late-step entropy and hence aggregate these signals with a simple linear weighting scheme to obtain TRE. Extensive experiments on multiple D-LLMs and QA datasets demonstrate that TRE achieves competitive performance, while enjoying strong generalizability, efficiency, and robustness.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
