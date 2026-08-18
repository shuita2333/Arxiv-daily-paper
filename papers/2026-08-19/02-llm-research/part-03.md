# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 101. [TAHB: A Comprehensive Benchmark for Text-Attributed Hypergraph Learning](https://arxiv.org/abs/2608.15055)

**<font color=#1a73e8>作者：</font>** David Yoon Suk Kang, JungHyun Kim, Juhyun Jeon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hypergraphs effectively model higher-order groupwise relationships beyond pairwise interactions, while pretrained language models (PLMs) and large language models (LLMs) provide rich semantic understanding from textual attributes. However, research on combining language models with hypergraph learning remains limited due to the lack of public text-attributed hypergraph benchmarks. To address this limitation, we present TAHB (Text-Attributed Hypergraph Benchmark), the first public benchmark integrating hypergraph structures and raw textual attributes. TAHB contains 10 real-world datasets from four domains - e-commerce, academia, movies, and politics networks - enabling systematic evaluation of text-aware hypergraph representation learning. Experimental results show that TAHB preserves key structural properties of real-world hypergraphs and consistently reproduces performance tendencies observed in existing benchmarks. Furthermore, experiments under both LLM-as-Enhancer and LLM-as-Predictor settings demonstrate that LLM-enhanced textual semantics improve hypergraph learning performance, while structural and textual information jointly provide the best setting for LLM-based prediction. Our benchmark provides a foundation for future research at the intersection of hypergraph learning and language models.

---


### 102. [GraphLoom: Reliability-Calibrated Graph Evidence Routing for Multimodal KG-RAG](https://arxiv.org/abs/2608.15056)

**<font color=#1a73e8>作者：</font>** Zafar Ali, Asad Khan, Aalia Malik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval-augmented generation (RAG) systems often rely on long unstructured contexts or aggressively expanded evidence graphs, which can introduce noisy evidence, weaken multi-hop reasoning, and increase unsupported generation. We present GraphLoom, a reliability-calibrated multimodal knowledge-graph RAG framework for compact and faithful evidence routing. Given a question and its associated multimodal input, GraphLoom constructs an instance-level multimodal knowledge graph from grounded scene descriptions, extracted relational triples, and external commonsense knowledge. Instead of injecting all retrieved evidence into the generator, GraphLoom performs reliability-aware subgraph retrieval with bounded expansion and selectively routes high-utility evidence through hierarchical graph memory slots and joint graph-sequence attention in a frozen language model. To improve robustness in complex reasoning settings, GraphLoom further combines interleaved retrieval with budgeted corrective retrieval, enabling adaptive multi-hop evidence refinement under noisy retrieval conditions. We evaluate GraphLoom on ScienceQA, MultiModalQA, and OK-VQA, including large distractor evidence pools that approximate noisy external knowledge retrieval. Experimental results show consistent gains in answer quality and evidence faithfulness over strong multimodal RAG, graph-retrieval, and open-source vision-language baselines, with improved retrieval quality on MultiModalQA and stable performance under noisy evidence pools. Additional analyses using MiniCheck-based verification, human evaluation, and latency profiling show that reliability-calibrated graph evidence routing provides an effective alternative to long-context multimodal evidence injection.

---


### 103. [MEDR: Query-Independent Frame Selection via Multi-Signal Event Modeling and Dynamic Rescoring](https://arxiv.org/abs/2608.15058)

**<font color=#1a73e8>作者：</font>** Xinlei Pu, Weijie Shi, Wen Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frame selection is a fundamental component of multimodal large language models, enabling long videos to be processed under limited visual-token and computational budgets. Uniform sampling preserves temporal coverage but may miss informative content that appears only briefly. To alleviate this limitation, query-dependent methods can retrieve question-relevant frames. However, because the selected frames depend on the current question, the same visual input cannot be directly shared across different questions, and frame selection must be repeated in multi-turn video dialogue. This motivates us to seek a query-independent frame selection method that preserves the reusability of a fixed visual input while improving the coverage of informative events beyond uniform sampling. We propose Multi-Signal Event Modeling and Dynamic Rescoring (MEDR), a training-free and query-independent frame selection method. Multi-Signal Event Modeling organizes complementary visual, motion, and text signals into signal-specific temporal events. Dynamic Rescoring then iteratively reevaluates each candidate relative to the current selected set, updating its score according to frame-level signal strength, additional event coverage, and temporal proximity. The resulting fixed frame set is constructed without observing the query and can be reused across different questions. On the standard benchmark evaluations, MEDR improves model accuracy by 0.63%-0.89% on Video-MME. On the long-video subset of LongVideoBench, it improves accuracy by up to 1.23% with Qwen3-VL-8B. MEDR further improves overall accuracy by 0.53%, while reusing exactly the same frame set for every question about a video.

---


### 104. [Do Visual Grounding Decoders Need Feed-Forward Networks? A Controlled Study over Frozen Vision-Language Features](https://arxiv.org/abs/2608.15061)

**<font color=#1a73e8>作者：</font>** Tarun Tomar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Do feed-forward networks (FFNs) in visual grounding decoders add essential computation once a pretrained vision-language model has already encoded image and language context? We compare a four-block attention-only decoder (A4), a matched four-block attention-plus-FFN decoder (S4), and an eight-block attention-only parameter control (A8) over frozen VLM features. A4 matches or slightly exceeds S4 on RefCOCOg and Ref-Adv-s. FineCops-Ref reveals a small A4 deficit of 0.52 percentage points at IoU@0.5 (95% CI [0.12, 0.95] in favor of S4), but A8 recovers it and finishes 0.26 points above S4. Official FineCops levels do not show a monotonic increase in the gap. A4 reduces trainable decoder parameters by 44.4% and cached-decoder latency by 10.1%, although end-to-end latency remains backbone-dominated. These results concern the trainable grounding decoder, not a complete attention-only VLM.

---


### 105. [RecurrentGPT: Expressive Depth through Recurrent Modulation in Transformers](https://arxiv.org/abs/2608.15062)

**<font color=#1a73e8>作者：</font>** Amr Hegazy, Amr Alanwar, Mostafa Elhoushi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling transformer language models creates an inherent tension between expressivity and memory efficiency. While unique weights across layers preserve functional specialization---from input-grounding to abstract refinement---they incur a substantial memory footprint. Conversely, standard depth-sharing enforces uniform transformations that collapse representational diversity and degrade modeling quality. We introduce RecurrentGPT, a recurrent depth transformer where fixed-depth prelude and coda blocks bracket a single shared core iterated R times. Inspired by gated recurrent neural networks, we employ a lightweight projection and an elementwise update gate---conditioned on the hidden state, the fixed prelude output, and noise resampled at every step---to modulate the recurrent update. This allows the model to specialize the input to the same few layers across recurrences, rather than requiring many unique layers to achieve functional diversity. Under an isoFLOPS constraint, a 3-layer RecurrentGPT matches the accuracy of a 12-layer GPT-2 Small baseline with similar training and inference FLOPs, and leads MoR and heavy-tail depth sampling in all nine scale-by-budget cells; at medium and large scale it approaches dense quality at the standard token budget and overtakes it at medium scale once that budget is doubled. Under an isoPARAMS constraint, deeper recurrence achieves a 2.76 validation loss versus 2.84 for a non-recurrent counterpart at matched parameter and data budget. Our results demonstrate that adaptive depth reuse is a principled strategy for trading parameters for quality: at large scale, 63% fewer parameters and 59% less peak decoding memory for a 10% increase in compiled generation latency.

---


### 106. [Funnel of Thoughts: Efficient Test-Time Scaling via Early Voting and Rollout Pruning](https://arxiv.org/abs/2608.15065)

**<font color=#1a73e8>作者：</font>** Chanhee Park, Sungbin Han, Jeongho Yoon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models produce diverse, sometimes inconsistent answers across repeated queries on the same problem, so multi-sample inference is a prerequisite for reliable deployment. Majority voting at k rollouts is the standard solution and the de facto accuracy target for this regime, but it is prohibitively expensive at the scale LRMs require. We introduce Funnel of Thoughts (FoT), an inference-time method that preserves the full 32-trajectory voted accuracy while halving its attention FLOPs, a 28.8% reduction in full-model inference cost. Across 115K reasoning trajectories from six LRMs, we find that unproductive trajectories often reveal themselves through repeated hesitation markers such as "Wait", "Actually", and "perhaps." These trajectories are less likely to reach the correct answer and consume disproportionate attention FLOPs, degenerating into no-answer loops in the worst case. Built on this training-free lexical signal, FoT identifies the vocabulary that captures these pathological patterns and prunes affected trajectories before completion, reducing online generation attention FLOPs by 56.1% and wall time by 37.6% without any additional model inference; the same signal transfers without retuning across held-out architectures and out-of-domain tasks.

---


### 107. [Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071)

**<font color=#1a73e8>作者：</font>** Tianxin Wei, Zhan Shi, Minhua Lin 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from experience is critical for developing capable, self-improving large language model (LLM) agents. Existing methods typically extract knowledge from accumulated trajectories via reflection, memory, rules, or skills. However, agents in realistic environments continuously encounter novel tasks, often offering only a one-shot opportunity to improve. These executions yield rich but highly noisy contexts, entangling broadly useful lessons with task-specific artifacts. Critically, prior works rarely validate their effectiveness on complex real-world tasks or isolate the underlying drivers of improvement. To address these gaps, we formulate online harness learning, where a frozen agent improves by continually updating a structured harness across sequential tasks. This formulation enables a systematic study of key self-improvement factors through our proposed Evo-Harness. At its core, context-to-harness skill compilation distills noisy, single-shot executions into reusable skill harnesses for cross-domain and topic-level adaptation. To demonstrate the efficacy of one-shot skill compilation, we evaluate across five realistic benchmarks (TerminalBench2, SWE-bench, CL-Bench, -bench, WebArena-Infinity). Our extensive analysis demonstrates the effectiveness of Evo-Harness and provides a principled understanding of how LLM agents can effectively learn on the fly. Our code is available at this https URL.

---


### 108. [SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models](https://arxiv.org/abs/2608.15075)

**<font color=#1a73e8>作者：</font>** Kexin Ma, Jing Xiao, Bowen Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RS-LVLMs have advanced multimodal understanding of Earth observation imagery, yet their performance is fundamentally constrained by high-resolution processing, as visual token counts grow quadratically with linear input resolution while important visual evidence is inherently sparse and increasingly diluted across the expanded sequence. Existing token pruning methods largely rely on scale-agnostic resolution policies and isolated importance cues, limiting task-aligned granularity adaptation and holistic evidence preservation. To address this, we present Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning (SA-GEM), a plug-and-play framework that unifies task-adaptive token granularity allocation with holistic geospatial token importance modulation. Specifically, a lightweight router selects the resolution based on query-dependent token granularity, while a token importance modulator jointly models task relevance, spatial structure, and local redundancy to preserve holistic geospatial evidence. We show that higher resolution is not universally beneficial and, once sufficient granularity is reached, token quality matters more than token quantity. Experiments across various benchmarks demonstrate that SA-GEM achieves consistent gains in both accuracy and efficiency over existing pruning methods. On XLRS-Bench, it surpasses GeoLLaVA-8K by 2.3% in accuracy with a 2.4 times total inference speedup.

---


### 109. [A Pilot Study of Autocompleting Tokenizers](https://arxiv.org/abs/2608.15080)

**<font color=#1a73e8>作者：</font>** Samuel Wexler, Mark Hopkins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern input methods routinely rely on autocomplete to omit information that can be recovered from local context. Inspired by these autocomplete-assisted writing systems, we investigate whether Transformer inputs can be compressed in a similar manner. Byte-level tokenization offers a simple and language-independent alternative to subword tokenization, but its longer input sequences typically result in increased computational cost and reduced model quality. We propose a compression scheme that employs a lightweight autoregressive byte language model to identify and remove bytes that are easily predictable from their surrounding context before Transformer processing. The resulting compressed representation is then provided as input to a standard encoder--decoder Transformer. Experiments on machine translation show that a substantial fraction of source-language bytes can be omitted without degrading translation quality. On English--French, our best method preserves translation performance while reducing source sequence length by nearly one-third. Additional experiments on Finnish--English, Russian--English, and Chinese--English demonstrate that the approach generalizes across diverse writing systems and morphological typologies, yielding comparable or improved translation quality at compression ratios between 0.47 and 0.67. These findings suggest that many input bytes are predictable enough to be represented implicitly rather than explicitly, providing a simple mechanism for reducing the sequence-length overhead associated with byte-level models.

---


### 110. [Beyond Thresholds: A Quality-Aware Decision Intelligence Framework for Cold Chain IoT Systems](https://arxiv.org/abs/2608.15082)

**<font color=#1a73e8>作者：</font>** Aashna Sofat, Balwinder Sodhi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cold chain logistics has advanced technologically, yet most deployed systems remain reactive monitors, not decision-making agents: thresholds trigger alerts, but nothing relates violations to cumulative product degradation or converts degradation signals into logistics decisions. We address this gap with a Quality-Aware Decision Intelligence (QADI) framework combining three capabilities: a structured quality state representation, $S_q = [L, Q, U, R]$ -- remaining shelf life, degradation rate, estimation uncertainty, and operational risk, all derived and computable from the framework equations; a hybrid quality modeling layer combining physics-based microbial kinetics with a data-driven correction term; and a reasoning layer built on Microsoft Phi-4~\cite{Phi4} with retrieval-augmented generation over a structured domain knowledge base.
We benchmark against five baselines -- threshold monitoring, physics-only, physics-plus-noise, optimisation-based decisions, and a rule-based expert system -- across eight cold chain scenarios, using pasteurised milk as the primary case, with ground truth shelf-life drawn from published dairy studies~\cite{Singh1994, Smigic2015} independent of our model. Comparisons use Wilcoxon signed-rank tests with Holm correction. Across milk and broccoli scenarios, the framework attains mean absolute shelf-life error of 7.2 hours (versus 30.9 hours, physics-only; $p<0.001$), spoilage rate of 14.5% (versus 16.6%, physics-only and rule-based; p=0.08), and oracle-optimal decisions in 99.5% of scenarios. Removing the LLM reasoning component drops optimality to 45.5% ($p<0.001$). Expert-rated explanation quality reaches 83% ($\kappa = 0.71$). Ablations show hybrid modeling and LLM reasoning contribute distinct gains, while RAG retrieval mainly drives explanation quality. Code: this https URL.

---


### 111. [Why Vision Fails as a Universal Bridge: Rectifying Modality Asynchrony in Multilingual MLLMs](https://arxiv.org/abs/2608.15085)

**<font color=#1a73e8>作者：</font>** Yihang Du, Juhao Liang, Zhengzhao Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) exhibit substantial performance degradation in non-English visual reasoning, despite the strong multilingual competence of their text-only backbones. While mechanistic evidence from text-only models suggests that non-English inputs are routed through an English-centric latent space, the multimodal implications of this phenomenon remain unexplored. Through rigorous mechanistic analysis, we identify the \textbf{Ghost Anchor} phenomenon: a temporal modality asynchrony where linguistic translation to the English semantic manifold completes in early layers, while visual semanticization remains immature. Consequently, visual signals are physically present yet functionally invisible during the early alignment window. To rectify this, we propose \textbf{ANCHOR}, a training framework employing Proactive Visual Anchoring (PVA) to accelerate early visual semantic emergence, ensuring visual representations proactively guide linguistic translation. Mechanistic interventions confirm that ANCHOR successfully restores the causal influence of visual signals during early translation. Furthermore, extensive experiments on XMMMU, MaXM, and CVQA demonstrate that ANCHOR consistently outperforms standard baselines, achieving robust visual reasoning across both fine-tuned and zero-shot languages.

---


### 112. [StateM: Reaching 95.3% Raw Accuracy, or a \$15 Frontier Run, on Terminal-Bench 2.1 via Harness Scaling](https://arxiv.org/abs/2608.15089)

**<font color=#1a73e8>作者：</font>** Ziheng Qin, Yaxin Lu, Zhangyang Atlas Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents can fail even when their underlying models can solve the constituent steps. They may lose track of mutable state, fail to reactivate lessons from earlier executions, skip known procedures, or stop prematurely. We bet on harness scaling to improve the execution system around an agent without changing its model weights. We introduce StateM, an agent-native runtime that organizes execution around durable states, phase-local context, checked transitions, recoverable runbooks, and versioned procedural practices that agents and users can inspect together.
On Terminal-Bench 2.1, StateM raises GPT-5.5 xhigh to 92.1\%, versus 83.1\% reference and GPT-5.6 Sol Ultra at 91.9\%. The runbook transfers unchanged to GPT-5.6. With GPT-5.6 Sol xhigh, StateM reaches 95.3\% raw accuracy across 445 trials and succeeds on all 89 tasks at least once. The frozen profile raises GPT-5.6 Luna from 76.7 to 85.4\%, above the 84.9\% Sol xhigh reference.
Using the same runtime, runbook structure, and golden rules, less than \$38 of adaptation raises DeepSeek-V4 Flash from 82.7 to 88.1\% under standard timeouts and to 89.1\% on an 88-task common core. Extending only the remaining latency-sensitive task matches the reported 88.8\% GPT-5.6 Sol max result. Final-score API usage is about \$15 versus \$574.68 for the GPT reference; total DeepSeek expenditure is \$52.22.
On BusinessBench, family-specific runbooks built on development sets yield held-out gains of 0.55 macro and 1.34 micro points; two mechanism-matched families improve by 10.04 points. Concrete rules generalize when tasks share execution structure, while the control methodology applies broadly. StateM turns selected postmortem findings into persistent, executable preconditions and practices, making learned controls explicit and enforceable through stateful controls. Code at this http URL.

---


### 113. [WeSCE: A Benchmark for Measuring Security Drift in LLM-Driven Code Editing](https://arxiv.org/abs/2608.15092)

**<font color=#1a73e8>作者：</font>** Zhiyu Zhang, Tingyue Wen, Senke Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce WeSCE, a benchmark for quantifying security drift in code editing under weak-security constraints, where tasks specify only functional objectives without explicit security requirements. WeSCE consists of 400 executable programs derived from real-world code, covering feature addition, feature removal, bug fixing, and refactoring. To quantify security drift, we propose a continuous risk representation that aggregates heterogeneous vulnerability signals through a unified formulation, and define drift measures capturing changes in overall risk, worst-case severity, and vulnerability distribution under code transformations, providing a multi-scale view of security spanning average-case behavior to worst-case emphasis.

---


### 114. [A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models](https://arxiv.org/abs/2608.15102)

**<font color=#1a73e8>作者：</font>** Amrit Gopinath, Raghul, Durairaj Thenmozhi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition. Inspired by the Declarative-Procedural framework, we analyze lexical, grammatical, and syntactic processing in a decoder-only English-German MoE Transformer trained under sequential language exposure. We construct a probe-based validation set and extract token-level routing distributions to quantify category-dependent specialisation using mutual information, routing entropy, and Jensen-Shannon distance. The curriculum-trained model exhibits a peak mutual information of 0.1148 at layer 5, indicating category-dependent differences in routing distributions across linguistic categories. Surprisingly, a no-curriculum baseline trained on mixed English-German data shows stronger aggregate specialisation, reaching a peak mutual information of 0.2599 at the same layer. These results suggest that interpretable linguistic organization emerges within MoE routing patterns even without sequential language exposure. A replication at a second training seed shows that the no-curriculum condition's specialisation concentrates on a single language whose identity is seed-dependent, whereas the curriculum consistently yields a stable, language-balanced routing profile; rather than uniformly increasing specialisation, staged bilingual exposure reduces single-language dominance. The official Github repository: this https URL

---


### 115. [Beyond Direct Access: Resource Hijacking in LLM Agents](https://arxiv.org/abs/2608.15108)

**<font color=#1a73e8>作者：</font>** Puyu Zeng, Qibing Ren  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly connected to high-value resources such as computing infrastructure, credentials, usage budgets, identities, private knowledge, communication channels, and organizational workflows. Existing agent security research mainly studies attacks on instructions, data, and tool behaviors, while high-value resources accessible to agents have received much less attention as direct attack targets. We are the first to identify and systematically study agent resource hijacking, a security blind spot in which attackers induce agents to invoke, consume, transfer, or control high-value resources for their own goals without directly obtaining those resources or their credentials. To study this threat, we introduce ResourceHijackBench together with an automated pipeline for generating resource hijacking cases. We organize high-value agent resources into six categories and construct 300 attack scenarios with 900 attack prompts. Each case runs in an isolated local environment that records actual resource use, allowing attacks to be evaluated from agent behavior rather than text responses alone. Without additional defenses, OpenClaw reaches an average attack success rate of 84.06%. The attack remains effective across different model backends, with average success rates ranging from 69.98% to 89.58%. Existing defenses reduce part of the risk, but the strongest evaluated defense still leaves an average attack success rate of 55.11%. These results show that high-value resources accessible to agents form an important and previously overlooked attack surface, and that current agent defenses are not sufficient to protect them from resource hijacking.

---


### 116. [Constraint-Aware Synthetic Tabular Data Generation via Inter-Column Constraint Discovery with LLM Agents](https://arxiv.org/abs/2608.15109)

**<font color=#1a73e8>作者：</font>** Jianxing Zhao, Mao Guan, Dongyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating structurally valid synthetic tabular data remains difficult: outputs with high statistical fidelity and downstream utility can still violate semantically meaningful domain constraints. We study the discovery and enforcement of three complementary inter-column constraint families---equations, linear inequalities, and logical dependencies. Our unified tool-grounded workflow represents all three as machine-executable hypotheses and applies a common interface for full-table validation, deterministic diagnosis, and counterexample-guided revision. A generator-agnostic postprocessor coordinates family-specific repairs on outputs from unchanged tabular generators. Across curated behavioral audits and end-to-end evaluations, the complete workflow improves held-out violation detection over one-shot direct prompting, while postprocessing yields zero measured violations for every retained, applicable constraint, improves downstream utility on most datasets, and largely preserves univariate marginals.

---


### 117. [Perspective-Invariant Attack with Enhanced Transferability of Adversarial Examples](https://arxiv.org/abs/2608.15115)

**<font color=#1a73e8>作者：</font>** Kaisheng Liang, Yiming Cao, Bin Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial examples generated on a surrogate deep neural network (DNN) can often successfully fool other black-box DNN models. This cross-model transferability poses serious security threats to DNNs in practical applications. Input transformation techniques are widely used to enhance adversarial transferability by increasing the diversity of input images. However, existing methods primarily rely on local operations with limited degrees of freedom (DOF), such as block-wise shuffling and resizing, overlooking global perspective transformations that naturally arise from viewpoint changes. In this work, we propose a Perspective-Invariant Attack (PIA), which introduces a multi-DOF vertex sampling strategy that systematically covers the perspective transformation hierarchy from 2-DOF translation to 8-DOF projective mapping. By generating geometrically diverse input variations, PIA effectively reduces overfitting of adversarial perturbations to the surrogate model, thereby improving adversarial transferability. We further propose PIA-Mix, a generic extension that maintains a complementary transformation pool and efficiently combines our perspective transformation with auxiliary methods for improved transferability. Extensive experiments involving various DNN architectures, advanced defense mechanisms, and multimodal large language models (LLMs) demonstrate that PIA and PIA-Mix outperform state-of-the-art transfer-based attacks.

---


### 118. [Anatomy of a Quantized Agent: VRAM Stability and Forecasting in Code-Synthesis Agentic Workloads](https://arxiv.org/abs/2608.15117)

**<font color=#1a73e8>作者：</font>** Anubhab Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analytical models of peak VRAM consumption for LLM inference decompose memory into weight-storage, KV-cache, and activation terms parameterized by step count, tool invocations, and context expansion. We evaluate this decomposition empirically within a strictly scoped measurement study: a LangGraph-based CUDA-kernel-synthesis agent (AgentK), a 4-bit quantization family (Q4 K M), a single NVIDIA H100 GPU, and four LLM backbones across 1,920 trajectories. Focusing on peak-memory forecasting behavior, we report two primary observations. First, closed-form analytical models achieve competitive accuracy when provided with two empirical constants: loaded-weight VRAM and a fixed activation-memory overhead. Supplied with live GPU readings and ground-truth trajectory parameters, the closed-form model matches or outperforms the best learned baseline on three of the four backbones (test MAPE 2.2-4.4% vs. 3.4-6.5%, p = 0.76). The exception is the smallest backbone (Phi-4-mini), where minimal VRAM variance (CV 0.3%) causes dynamic modeling to underperform simple regression. Second, compile success strictly bifurcates by backbone capacity (from 5.7% for Phi-4-mini to 62.0% for Qwen2.5-Coder-14B), demonstrating that functional code synthesis remains constrained by intrinsic LLM capabilities rather than available memory. Furthermore, because overall peak-memory variance is remarkably low across all backbones (CV 0.3-9.4%), learned prompt-feature regression offers statistically insignificant improvements over a constant-mean baseline. Consequently, we find no justification for deploying complex predictive VRAM models in highly quantized, weight-dominated regimes. We release the evaluated corpus and anonymized framework to support replication.

---


### 119. [Left-Branching Transformers Excel at Right-Branching Languages: Data Shapes Word Order Preferences in Language Models](https://arxiv.org/abs/2608.15129)

**<font color=#1a73e8>作者：</font>** Varvara Arzt, Allan Hanbury, Terra Blevins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We systematically compare word order preferences in decoder-only language models across 192 artificial languages and typologically diverse natural languages. On artificial languages, models exhibit a left-branching preference that aligns with neither natural language universals nor human word order learning biases. On natural languages, monolingual models show no clear base word order bias at small scales, but as data grows, a preference for right-branching subject-verb-object (SVO) languages emerges while SOV falls behind despite being the most frequent order cross-linguistically. This SVO advantage extends to multilingual models and correlates with language resource level and data quality rather than word order. Thus, the same architecture exhibits opposite preferences on artificial and natural languages, establishing that word order biases observed in practice are data-driven. Since highly-resourced languages are overwhelmingly SVO, these biases risk gradually reducing word order diversity, particularly in languages that productively use multiple word orders, with the widespread adoption of LLMs.

---


### 120. [ReForge: Keeping ABR Algorithms Never Finished with Verified Large Language Model Edits](https://arxiv.org/abs/2608.15138)

**<font color=#1a73e8>作者：</font>** Zhiqiang He, Zhi Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing an ABR algorithm for one network scenario takes an engineer months, and large language models now do this work in hours, matching or beating hand-built designs. But either way, the design fits only the world visible at its birth, and fails on the world that arrives after. We ask whether an ABR algorithm can keep pace with the world, redesigned in minutes as each scenario arrives, with every change proven harmless to every scenario already served. In this work, we propose ReForge, a continual heuristic learning framework that adapts to continuously changing scenarios. ReForge runs that routine with a large language model (LLM) in the loop. Each round the LLM reads where the current design falls short and proposes one small edit, and a replay over every network served so far decides. Specifically, what it edits is a single page of fuzzy rules that routes every decision to one of a frozen pool of pre-trained policies. The LLM writes the first page from measurements alone, then keeps improving it on its own. Each round it reads where the current rules fall short and proposes one small edit, and a replay over every network served so far decides whether the edit lands. We evaluate ReForge on nine real-world network families arriving one at a time as 3G, 4G, then 5G. A few edits per arrival lift mean QoE from 1.23 to 1.74, past the best single policy at 1.66 and to 94\% of an oracle, and even repair families the loop never saw, one rising from 0.30 to 0.80. All code, data, and experiment records will be open-sourced upon cleanup.

---


### 121. [ACTS-SQL: Agentic and Critic-Oriented Tree-Structured SQL Correctness with Large Language Models](https://arxiv.org/abs/2608.15145)

**<font color=#1a73e8>作者：</font>** Xinmei Huang, Jie Song, Peng Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been increasingly adopted in Text-to-SQL systems, yet SQL errors remain a major obstacle in real-world Text-to-SQL inference pipelines. Existing SQL correction approaches either rely on large-scale, high-quality training data with substantial overhead, or adopt single-path agentic workflows that are brittle to early mistakes and prone to error propagation.
To develop a practical SQL correctness system for industrial scenarios, we present a training-free framework that formulates SQL correction as a plan-guided, tree-structured debugging process. By maintaining multiple correction strategies and enabling backtracking, the framework mitigates error accumulation during iterative refinement. We further integrate execution-based verification and clause-level diagnostic tools to support strategy pruning and precise error localization.
We evaluate the system on the BIRD-Critic benchmark and observe consistent accuracy gains over strong LLM backbones and representative agent-based baselines, achieving a 9.42% improvement over the previous state-of-the-art method. The framework is also deployed in the Torch Log Service (TLS) of Volcano Engine to support an online Text-to-TLS API. In production, it improves execution accuracy from 36.77% to 53.61% on real user queries with a representative strong LLM backbone (GPT-5). These results demonstrate the effectiveness and stability of our approach in real-world deployments.

---


### 122. [Constitutive Priors for Machine Intelligence: A Legitimacy Theory of the Artificial Physical World](https://arxiv.org/abs/2608.15147)

**<font color=#1a73e8>作者：</font>** Jiang Jiang, Yifu Sun, Qi Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine intelligence has conquered the symbolic world but stalled at the physical one. The stall is structural: physical AI faces a cold-start deadlock -- no intelligence without data, no data without deployed intelligence. Our thesis: the deadlock is real but unevenly distributed, and the exception has a name: the artificial physical world. Buildings, industrial facilities, and infrastructure are intentionally constituted and documented: designed artifacts ship with readable archives that precede and constitute their instances; here, norms are promulgated before instances, not averaged from them. Four contributions. (i) From a four-world ontology we derive a legitimacy criterion for constitutive prior frameworks: prior extraction is legitimate if and only if the object domain is intentionally constituted and has left a readable archive; the criterion is testable through direction of fit -- deviation from a constitutive norm is a violation in the world, not a revision of the model. (ii) We establish a layering lower bound: any such framework has at least four layers -- syntax, concept, knowledge, instance -- because four construction goals pair into mutually incompatible carriers. (iii) We register deployment claims across five industrial domains and a 32-class failure-mode vocabulary. (iv) We stake the framework on five falsifiable predictions, the central one checkable on the public engineering record: if it fails, the framework fails. Semi-formal arguments back these claims (Appendix A): a Gold-type boundary on rule coverage in archiveless worlds, a decidability result for failure reduction over closed concept layers, and a boundary theorem for certificate-anchored calculi. Large language models find an honored place here -- as readers of the archive, not as the archive. First of three companion works; the companions take up the questions deliberately left open.

---


### 123. [From "What-If" to "What-Is": Counterfactual Thinking-Inspired Semantic Alignment for Visual Brain Decoding](https://arxiv.org/abs/2608.15163)

**<font color=#1a73e8>作者：</font>** Kaitao Yan, Chi Liu, Congcong Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual brain decoding reconstructs visual content perceived by a person from neural measurements such as fMRI, providing a computational approach to studying how visual information is represented in the brain. Recent multimodal representations and diffusion priors have improved reconstruction realism. However, visually plausible reconstructions may contain incorrect objects, attributes, or relations because a strong generative prior can complete content not sufficiently specified by the decoded representation. Conventional reconstruction metrics mainly assess the final image and may therefore obscure such semantic errors. We propose ConceptAlign, a counterfactual semantic alignment framework for visual brain decoding. ConceptAlign pools decoded visual tokens and projects them into a frozen text-embedding space, aligning the representation with the ground-truth caption while separating it from scene-preserving near-miss alternatives. Generated offline by an LLM, these alternatives modify one critical object, attribute, or relation while retaining the scene. A margin-based objective learns fine-grained semantic boundaries between the observed stimulus and plausible but incorrect interpretations without requiring LLM calls during inference. We introduce a systematic three-level semantic evaluation framework covering foundational discriminability, counterfactual description discrimination, and representational geometry. Experiments on the Natural Scenes Dataset show that ConceptAlign improves reconstruction measures, counterfactual semantic discrimination, and representational alignment over the MindEye2 backbone. Matched negative-source ablations, independent LLM and human-written alternatives, and human evaluation support the effectiveness and robustness of the supervision, with favorable patterns in fine-grained conflicts, limited-data decoding, and cross-subject structure.

---


### 124. [SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion](https://arxiv.org/abs/2608.15165)

**<font color=#1a73e8>作者：</font>** Yu He, Weikai Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can continually improve without parameter updates by converting historical experience into reusable procedural knowledge. However, existing methods often consolidate experience based on semantic similarity or LLM judgments, which may merge superficially related but behaviorally incompatible strategies and thereby degrade performance. To address the issue, we propose SkillCommit, an online skill evolution framework that continuously transforms experience into a hierarchical library of reusable skills. Each new experience is initially preserved as an instance-specific patch, retaining the behavior validated in its local context. As related skills accumulate, SkillCommit abstracts those sharing a common behavioral mechanism into higher-level skills. Specifically, for each incoming skill, embedding-based retrieval first identifies candidate related skills. Cross-instance replay and an LLM-based mechanism check determine whether these skills transfer across cases and share a common underlying mechanism. Candidates that pass both checks are abstracted into a higher-level skill and committed only if it preserves the validated behavior of all constituent skills. Experiments on RuleArena, OpenExempt and KOR-Bench demonstrate that SkillCommit consistently improves agent performance across diverse domains. Moreover, the learned skills transfer across model scales and families, enabling cross-model experience transfer.

---


### 125. [Insurance as AI Risk Infrastructure: A Generative-Agent Simulation of AI Adoption](https://arxiv.org/abs/2608.15181)

**<font color=#1a73e8>作者：</font>** Yixuan Yuan, Dedai Wei, Chudong Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of artificial intelligence (AI) tools has demonstrated immense potential to enhance societal well-being and operational efficiency. However, the inherent unreliability and uncertain operational consequences of modern AI systems, typified by large language models (LLMs), have created a significant barrier to enterprise adoption. Many enterprises remain hesitant to integrate these tools deeply into their workflows due to concerns about unpredictable losses and liability exposure. While existing technical safeguards primarily seek to reduce the likelihood or severity of AI-enabled workflow failures, they do not by themselves provide ex post financial protection when residual pecuniary tail losses materialize. In this paper, we introduce a socio-economic framework that complements these safeguards by transferring and absorbing the residual financial consequences of AI adoption through insurance. To evaluate this framework, we develop an LLM-driven agent-based social simulation (LABSS) system. We assess the behavioral validity of the simulation using established economic and sociological theories. Our analysis demonstrates that the proposed insurance framework reduces firm-level financial exposure, thereby accelerating the aggregate adoption of AI tools and improving firm solvency and aggregate capital.

---


### 126. [DCA-MoE: Spatially Adaptive Cross-Layer Fusion and Density-Routed Experts for Crowd Counting](https://arxiv.org/abs/2608.15213)

**<font color=#1a73e8>作者：</font>** Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crowd counting must recover reliable local density under severe variations in perspective, head scale, occlusion, and background clutter. Although modern counting objectives provide strong spatial supervision, many multi-level decoders still use spatially invariant feature fusion and apply one receptive-field pattern to every location. We propose DCA-MoE, a framework that makes both decisions content dependent while retaining a frozen DINOv3 encoder. Spatially Adaptive Layer Fusion (SALF) predicts position-wise weights over four aligned backbone features, and Density-Routed Multi-Receptive-Field Experts (DR-MoE) assigns each location a soft mixture of local, mid-range, and large-context residual experts. An EBC-style head reconstructs block density, while DMCount supervision and an auxiliary routing-balance term train the decoder without updating the backbone. On the NWPU-Crowd validation split, the strongest paired configuration, based on DINOv3 ViT-L/16, obtains 31.7 MAE and 72.2 RMSE; the matched ViT-B/16 full model obtains a paired 32.2/75.9. Cross-dataset results remain mixed, and several component baselines currently report independently selected minima from a single seed. The evidence therefore supports the feasibility of spatially adaptive fusion and routing, while broader paired and multi-seed evaluation remains necessary for causal attribution.

---


### 127. [TRACE-BN: Transferring Bangla-English Tutoring Behavior to a Sub-1B Offline Language Model](https://arxiv.org/abs/2608.15223)

**<font color=#1a73e8>作者：</font>** Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Mohammad Tushar Abdullah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bangla-English tutoring requires more than producing a correct translation: learners also need explanations of grammar differences, awareness of their likely errors, and targeted practice. We present TRACE-BN, a curriculum-guided dataset of structured tutoring traces for Bangla-speaking learners of English at the CEFR A1-A2 level. Each trace combines word-level glosses, literal and natural translations, Bangla grammar explanations, a plausible learner error, and a targeted practice question with its answer. The traces are generated by Gemini 3.5 Flash Lite as the teacher model from NCTB Classes 9-10 English curriculum units, then filtered for structural validity, script integrity, and semantic duplication. We transfer the resulting structured tutoring behavior to Qwen3-0.6B using LoRA with 4-bit quantization for resource-constrained offline deployment. On held-out inputs, schema validity increases from 85.4% to 95.8%, while, against teacher-model references, chrF++ improves from 15.28 to 34.77 and BLEU from 4.52 to 21.03. Field-level evaluation by two independent judges shows improvements across translation, grammar explanation, learner-error diagnosis, and practice alignment, while a human audit supports the quality of the supervision data. The results show that curriculum-guided structured supervision can transfer multi-component tutoring behavior to a sub-1B model under these resource constraints. The dataset, model checkpoints, and code are publicly available at this https URL

---


### 128. [Structuring Semantic Embeddings for Principle Evaluation: A Prototype-Guided Contrastive Learning Approach](https://arxiv.org/abs/2608.15224)

**<font color=#1a73e8>作者：</font>** Che Shen, Junwei Su, Lingpeng Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable post-hoc evaluation asks whether already generated text satisfies a target criterion after generation. In this paper we study a focused frozen-embedding setting using principle-evaluation proxy tasks: toxicity detection, fine-grained emotion categorization, and ordinal review rating. General-purpose text embeddings are widely deployed for such tasks, but broad semantic similarity can place semantically similar yet task-distinct examples in overlapping regions of the representation space. We introduce Prototype-Guided Contrastive Learning (PGCL), a prototype-guided geometric regularization module built on top of frozen text embeddings. The module combines a semantic stream, a prototype-anchor attention stream, supervised contrastive learning, offset-based prototype-margin regularization, and stream regularization to produce a compact task-adapted representation without updating the base encoder. Controlled experiments show that PGCL improves over raw frozen embeddings on all three datasets and gives the clearest direct-baseline margin on AmazonReviews, while remaining competitive with strong direct frozen metric-learning baselines on GoEmotions and ToxicComment. We also add supervised residual-adapter, encoder-LoRA, full fine-tuning, objective ablation, sensitivity, and fully logged few-shot LLM protocol diagnostics to define the boundary of the claim. The theoretical analysis is revised as a sufficient-condition account for prototype-margin behavior under explicit assumptions in the prototype-mapping space, rather than as an unconditional training or final-embedding separation guarantee.

---


### 129. [UC-VLM: Consistency-Driven Learning for AI-Generated Image Detection with Vision-Language Large Models](https://arxiv.org/abs/2608.15238)

**<font color=#1a73e8>作者：</font>** Lei Tan, Shuwei Li, Mohan Kankanhalli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Large Models (VLLMs) are promising for AI-generated image (AIGI) detection because they can produce both a prediction and a natural-language output. However, most existing VLLM-based detectors primarily fine-tune the language side while giving limited attention to low-level visual forensic cues. They also often depend on manually crafted prompts or human-annotated rationales, which limits this http URL present UC-VLM, a unified multi-stage framework for AIGI detection that relies solely on binary supervision. UC-VLM first identifies effective instruction variants automatically. It then reuses the same binary label within a multi-stage training framework: (i) a visual discrimination objective that strengthens sensitivity to non-semantic forensic cues, and (ii) a label-conditioned generation objective that uses the binary label to supervise textual outputs. This design turns weak binary supervision into a shared supervision signal for both the visual pathway and the language output. Our key novelty is a unified multi-stage binary-supervised framework that consistently reuses the same authenticity labels for visual adaptation and label-conditioned text generation, while leveraging automatically optimized instructions to reduce prompt sensitivity without requiring human-written rationales or hand-crafted this http URL show that UC-VLM achieves 96.1% average accuracy on GenImage, exceeding the strongest prior result by 4.6%, and obtains 69.6% / 77.9% accuracy on Chameleon under ProGAN / SDV1.4 training, surpassing the best baseline by 11.2% / 15.3%, respectively.

---


### 130. [Learning reshapes power-law anisotropy in internal representations](https://arxiv.org/abs/2608.15239)

**<font color=#1a73e8>作者：</font>** Asahi Nakamuta, Jun-nosuke Teramae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power-law anisotropy in internal representations has been observed across a wide range of biological and artificial neural systems, from state-of-the-art language models to the mouse cerebral cortex. This anisotropy is a key geometric property of high-dimensional information processing and underlies a variety of theoretical analyses. However, the mechanism by which it emerges from input structure and task-driven learning has remained unclear. Here, we characterize this formation process by exactly solving the learning dynamics of a wide two-layer linear neural network in a teacher--student setting with power-law input and teacher structures. We show that, in the feature-learning regime, the local power-law exponent of the internal-representation spectrum evolves nonmonotonically over the course of training and exhibits up to four distinct asymptotic regimes across modes and training times. By contrast, in the lazy regime, the exponent remains essentially unchanged. We further demonstrate numerically that similar exponent dynamics arise in more realistic nonlinear networks. Together, these results suggest a general mechanism by which the dynamic interaction between input statistics and task structure gives rise to power-law internal representations.

---


### 131. [MDwAIstScheduler: Bringing On-Device Voice Documentation into Clinical Practice](https://arxiv.org/abs/2608.15252)

**<font color=#1a73e8>作者：</font>** Diego Mardian, Frank Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinical documentation forces physicians to split attention between the patient and their keyboard, and much of it spills into uncom- pensated after-hours work. We present MDwAIstScheduler, a low- cost, belt-worn pipeline that lets a physician speak naturally dur- ing the encounter and have the resulting medications, allergies, labs/orders/referrals, follow-up scheduling, vitals, and problems land in the EHR as review-ready drafts. Building on our earlier prototype, which relied on cloud speech recognition and a cloud language model, the current pipeline runs both transcription and intent extraction entirely on-device. Using a medical-domain auto- matic speech recognition (ASR) model and a 1.7B-parameter lan- guage model we fine-tuned for clinical action extraction, no patient audio or text leaves the device, and the structured drafts are written directly into the Elation EHR for the physician to confirm. The result is a documentation tool that removes keyboard work from the visit without removing the clinician from the record, allowing them to focus on what matters most, patient care, while reducing burden at the same time.

---


### 132. [Demographic Injection in Medical Language Models under Diversity, Equity, and Inclusion Prompts](https://arxiv.org/abs/2608.15254)

**<font color=#1a73e8>作者：</font>** Diego Mardian, Frank Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical-AI guidance increasingly recommends prompting language models to reason with attention to diversity, equity, and inclusion (DEI). We measure a side effect that misrepresents patients: a one-sentence DEI prompt appended to a medical question leads models to add patient demographic attributes (race, socioeconomic status, sex) the question never stated, in effect rewriting who the patient is. We call this demographic injection. Across 47 models, four medical benchmarks, and 376,000 responses scored by a validated model-judge pipeline, a single DEI prompt raises the injection rate from 0.7% to 33.1% (47x) in all 47 of 47 models, attributable to the equity content rather than to added length (18x above a length-matched control; p=1.4x10^-14). Most added content is a general population statement that leaves the answer unchanged, but a smaller subset attaches an attribute to the specific patient or changes the selected option (0.25-2.4% of responses, 99.8% toward the incorrect option), where the invented demographic changes the answer the model recommends. Phrasing scales the effect from 14% to 56%. DEI prompts are just one example of a more general mechanism. Any instruction that nudges how a model reasons can make it add unrequested details, including details about the patient. Flagged outputs are treated as model errors under study, not clinical guidance.

---


### 133. [Towards Standardized Evaluation in Automated Domain Modeling: Introducing a Benchmark](https://arxiv.org/abs/2608.15255)

**<font color=#1a73e8>作者：</font>** Vasiliy Seibert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain modeling plays an essential role in domain-driven design, capturing essential entities and their relationships within a specific domain. Despite advancements in automated domain modeling, the absence of standardized benchmarks has hindered the comparative assessment of existing approaches. This paper introduces a benchmark designed to address this gap. The benchmark combines the 45-record Golden UML Modelset (Verbruggen et al., 2025) on Zenodo, as distributed by the Text2UML project of Calamo, Mecella, and Snoeck (Calamo et al., 2025), with the 8-record reference archive of Chen et al. (Chen et al., 2023a,b), enabling the evaluation of automated domain modeling approaches across different levels of complexity and scale. Given a natural language description, the task is to generate a corresponding domain model. For each description, a reference domain model is provided as ground truth. A metric is used to compare the generated domain model with the corresponding ground-truth model. To demonstrate the utility of the benchmark, we evaluate multiple automated domain modeling approaches, including heuristic rule-based methods and LLM-driven strategies. In accordance with the FAIR4RS recommendations (Chue Hong et al., 2022), the benchmark is provided as a research artifact to encourage reuse and support future research on automated domain modeling.

---


### 134. [VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?](https://arxiv.org/abs/2608.15265)

**<font color=#1a73e8>作者：</font>** Yansong Ning, Jingwen Ye, Zhongkai Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing an interactive 3D open world from a user query is important. However, existing methods are primarily evaluated on idealized, simple queries, making it difficult to systematically analyze and compare how multimodal agents understand user intent, use 3D tools, and reason over textual and visual 3D world information. To this end, we propose VibeWorlding, a unified framework for benchmarking and training vibe worlding agents: a multimodal agent that can autonomously infer user intent, plan scene layout, invoke 3D tools, and reflect on the multimodal feedback in a multi-turn agent-environment interaction process. To achieve this, we first build VWE-BENCH, a benchmark of 2,616 high-quality 3D assets, 323 human-annotated seed 3D worlds, and 6,828 reverse-synthesized multimodal user queries, split into verified queries with ground-truth and unverified queries with carefully designed rubrics. Moreover, we develop VibeWorlding-Gym, a joint multimodal RL post-training framework that integrates (1) a sandbox environment unifying asset retrieval, editing, and image rendering as MCP tools, and (2) a rubric-based verifier that combines physical feasibility and intent fulfillment verification, supporting both fair model evaluation and scalable multimodal RL reward service. Our experiments show that current frontier MLLMs are far from solving the vibe worlding agent task, with even GPT-5.5 and Qwen3.8-Max reaching below 60% success rate, and trace the bottleneck to precise 3D world editing. We further find that RL training can ease this weakness and enable open-source MLLMs to even surpass closed-source frontiers: our VibeWorlder-8B is comparable to frontier MLLMs, while our flagship VibeWorlder-30B-A3B attains the best overall Pass@1 among all evaluated models.

---


### 135. [Time as Structure: Temporal Dependency Graphs for Verifiable Deadline Computation over Legal Documents](https://arxiv.org/abs/2608.15270)

**<font color=#1a73e8>作者：</font>** Maryia Zhyrko, Lifeng Han, Suzan Verberne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Miss a filing deadline by one day and the claim is barred, however strong the case. Computing that deadline is rarely simple: the period runs from a triggering event, is counted by a statutory convention, and may be suspended by a mandatory conciliation window. We ask whether a language model should answer such questions directly, or read the document and leave the arithmetic to code. We extract dated facts and their dependencies into a temporal dependency graph and compute deadlines from it with a calendar-correct engine. On UK Employment Appeal Tribunal judgments the engine reproduces six of seven timeliness rulings, and matches the judges' own dates to the day. The strongest of four language models, asked the same cases, gets the arithmetic right and the answer wrong: in six of twenty-one responses its stated verdict contradicts its own thinking, and every contradiction runs the same way, calling a late claim timely. To test the systems at scale we move the dismissal date across the statutory boundary, generating 427 cases whose answers are computed rather than annotated. On the cases both systems answer, the pipeline is right 90.2% of the time against 61.2% for direct answering. The limit is extraction: on contracts the errors are almost never in the arithmetic, but in choosing which event the period starts from.

---


### 136. [No Task Fails Every Time: Why One-Shot Audits Are Structurally Blind to Agent Damage](https://arxiv.org/abs/2608.15286)

**<font color=#1a73e8>作者：</font>** Shiven Khurdi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce AgentRelBench, an environment-agnostic reliability instrument that computes ground-truth, severity-priced damage from database state diffs across repeated runs, with no LLM in the measurement path, demonstrated on EnterpriseOps-Gym. Across 2,128 evaluation runs spanning nine models in six families (four development, three pre-registered held-out, plus a frontier pass on two frontier-tier models that the pre-registration designates exploratory), we find: (1) damage on irreversible actions is universal across the families we measured and stochastic within them on pinned, single-provider stacks. (2) No task damaged on every run: zero always-fail cells across 42 confirmatory held-out damage events. A single clean run misses a damage-producing (model, task) pair 0.80 of the time on the development pool (13 pairs); the held-out pool is descriptively consistent (0.575 over 5 pairs, pair-weighted) but sits below our pre-registered power floor and is reported as underpowered, not as confirmation. (3) Damage-producing task count falls with model capability, from 7 of 20 tasks for an 8B model to 1 of 20 for the most capable; capability is confounded with family and training, so this is an observed gradient, not a causal claim. The residual damage does not change in character: in the exploratory frontier pass, the most capable model's one damaging task damages at $\hat{p} = 0.16$ per run, inside the same demonstrably-stochastic band, and a single audit misses it 84% of the time. (4) One model family committed the gated irreversible change while declaring it had refused: transcript- and judge-based grading scores those runs as safe refusals, only state diffs as damage. All confirmatory findings were pre-registered with per-claim demote criteria; one demoted our own initially favored finding, which we report.

---


### 137. [MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation](https://arxiv.org/abs/2608.15299)

**<font color=#1a73e8>作者：</font>** Lie Li, Wen Li, Junxiao Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsely-activated Mixture-of-Experts (MoE) Transformers universally fix the same number of routed experts across all layers, a convention that ignores the well-documented heterogeneity in layer-wise redundancy. We demonstrate that this uniformity is systematically suboptimal and propose MAPLE, a plug-and-play framework that reallocates the routed-expert budget heterogeneously across layers of any pretrained MoE LLM, without modifying weights or requiring retraining. Our core contribution is a closed-form sensitivity-guided allocation: we probe each layer's response to variation in expert count, quantify sensitivity using three measures, and derive an analytically optimal budget assignment that directs capacity towards sensitive layers and absorbs reductions in redundant layers. This closed-form solution is further refined by a sensitivity-constrained genetic search that uses layer-wise sensitivity as a prior to guide exploration, yielding faster convergence and superior allocation quality. On four MoE models spanning different scales and architectures, MAPLE outperforms uniform and pruning-based baselines under a 75% routed-expert budget. Notably, on DeepSeek-MoE-16B, MAPLE uses only 75% of the experts yet surpasses the original 100% expert-uniform baseline on ARC-E, ARC-C, and BoolQ, improving accuracy from 65.09 to 71.40, 48.49 to 51.50, and 80.03 to 82.38, respectively. These accuracy gains translate into measured deployment efficiency: implementing MAPLE in SGLang reduces single-GPU end-to-end serving latency by 32.2% and improves throughput by 47.4%. These results show that well-designed heterogeneous allocation can be more effective than simply activating more experts, establishing it as a principled and practical axis for improving MoE efficiency.

---


### 138. [Divergent-Convergent Reasoning: Scaling Test-Time Compute through Structured Solution Synthesis](https://arxiv.org/abs/2608.15303)

**<font color=#1a73e8>作者：</font>** Bo Wen, Yuhao Chen, Erhan Bilal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time compute can substantially improve Large Language Model (LLM) reasoning performance, yet how and when additional compute helps remains poorly understood. We study Divergent-Convergent Reasoning (DCR), a simple two-phase primitive consisting of an exploration phase that generates multiple candidate solutions followed by a convergent reconciliation phase. We present three core results. First, we show that even a single reconciliation step can reliably amplify correct minority reports: across datasets, DCR often recovers the correct answer when correct exploration outputs are in the minority, a regime where majority voting fails. Second, we introduce recursive DCR, an autoregressive reconciliation system that iteratively analyzes disagreements and allocates additional test-time compute. Recursive DCR achieves higher accuracy than fixed-compute baselines-reaching 93.3% on AIME 2024 and 92.0% on AIME 2025-while using roughly 27% less compute on average, demonstrating that attentive resource allocation is superior to uniform scaling. Third, we analyze disagreement among exploration outputs via a simple, training-free dispersion metric. Dispersion reveals a structured relationship between disagreement and test-time gains: in regimes where DCR is effective, higher disagreement among exploration outputs is associated with larger accuracy improvements from reconciliation. Together, these results show that disagreement, often viewed as noise, can be systematically exploited to improve test-time reasoning and reveal emerging scaling laws for agentic LLM systems.

---


### 139. [Understanding Cognition-Induced Risks in Agentic AI Systems](https://arxiv.org/abs/2608.15304)

**<font color=#1a73e8>作者：</font>** Guanchu Wang, Qinuo Li, Mengnan Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier agentic systems powered by large language models (LLMs) exhibit human-like patterns of cognition. As these systems become deeply integrated across different domains, their cognitive engagement raises critical concerns for human society that remain insufficiently studied. To address this gap, we systematically analyze risks induced by expanding cognitive capabilities, following a three-level framework defined by their cognitive scope, from physical cognition to social cognition, and finally to self-referential cognition. We study their potential risks to human agency, autonomy, and control capability, corresponding to each cognitive level. We finally propose strategies to mitigate these risks and enhance the controllability of agentic AI systems, ensuring their long-term safe development.

---


### 140. [MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning](https://arxiv.org/abs/2608.15311)

**<font color=#1a73e8>作者：</font>** Ankita Sharma, Bahar Farahani, Sanaz Rahimi Moosavi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated instruction fine-tuning enables Large Language Models (LLMs) to adapt to decentralized, privacy-sensitive data without requiring data sharing. Recent Mixture-of-Experts (MoE) LLMs are particularly attractive for federated learning because their sparse activation reduces computation and communication while scaling model capacity. However, existing federated MoE methods primarily focus on parameter aggregation and personalization, overlooking the routing behavior of MoE models as a source of information for client collaboration. Under heterogeneous instruction distributions, indiscriminate aggregation can lead to negative transfer, highlighting the need to identify which clients should collaborate during federated optimization. We propose ClientMorpher, a routing-aware, personalized federated instruction fine-tuning framework that leverages routing signatures from pretrained MoE models to organize client collaboration prior to aggregation. We investigate two complementary clustering strategies: ClientMorpher-C, which directly clusters clients using expert activation profiles, and ClientMorpher-E, which first clusters experts based on their cross-client usage signatures and then derives client collaboration groups. We evaluate ClientMorpher for federated instruction fine-tuning on the Databricks Dolly-15K dataset, using pathological and Dirichlet-based heterogeneous client distributions across multiple instruction-following tasks. Experimental results show that routing-aware collaboration consistently improves personalized performance compared to conventional federated averaging and local training, while maintaining the same communication cost. Furthermore, our study shows that client-centric and expert-centric clustering provides an effective and scalable approach for personalized federated instruction fine-tuning of sparse MoE LLMs.

---


### 141. [When Do Concepts Become Functionally Sufficient During Language-Model Training?](https://arxiv.org/abs/2608.15323)

**<font color=#1a73e8>作者：</font>** Raphael Bernas, Paul G. Chevalier, Fanny Jourdan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding a model and its learning mechanisms in depth requires identifying when its internal structures become useful, rather than simply looking at the final state. We study this through concept dynamics: at each layer and checkpoint, we decompose activations, select sparse soft masks, and inject masked reconstructions into the model. Concept analysis is therefore tested functionally: a mask is useful only insofar as it preserves a target under intervention. We compare sufficiency for activation reconstruction, linear decodability, true downstream preservation, and checkpoint transfer under learned alignment. The framework treats decomposition assumptions as hypotheses rather than interpretability guarantees, monitoring functional sufficiency across checkpoints and source-to-final reconstructability under learned alignment. At the shared fixed-penalty operating point across seven models, downstream masks retain substantially less soft mass than reconstruction masks; predictive-distribution shifts remain small.

---


### 142. [When AI Rewrites, Classifiers Relax: Uncertainty-Aware Sentiment Analysis on Sarcastic and AI-Paraphrased Social Text](https://arxiv.org/abs/2608.15338)

**<font color=#1a73e8>作者：</font>** Shresth Shroff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment classifiers are increasingly applied to social media content that is either sarcastic or AI-generated --- two distributional regimes where standard evaluations offer little guidance. We present a three-part empirical study of sentiment classifier behaviour under these conditions. First, we find that confidence scores on sarcastic text are significantly lower than on non-sarcastic text (Mann--Whitney $p = 2 \times 10^{-6}$), confirming that classifiers sense their own uncertainty on ironic content even without explicit uncertainty modelling. Second, and counterintuitively, we show that sentiment classifiers achieve higher accuracy on AI-paraphrased reviews than on the original human-authored text (RoBERTa: $+5.8$ pp for Qwen3.5-4B paraphrases, $+3.7$ pp for Gemma4-E4B), revealing a cross-domain stylistic alignment effect: AI paraphrases remove distributional noise that confounds Twitter-trained classifiers, producing cleaner, more prototypical sentiment text. Third, we demonstrate that a lightweight abstention wrapper --- flagging the $14\%$ of inputs with confidence below $0.6$ --- improves accuracy from 82.2\% to 88.9\% ($+6.7$ pp) on the retained set. We further compare Semantic Entropy and MC-Dropout-style disagreement as uncertainty signals and find near-identical AUROC ($0.650$ vs.\ $0.646$) on sarcastic text, suggesting that for short social media inputs, both methods are interchangeable. Our results motivate a shift from confident single-label prediction to uncertainty-aware abstention in high-stakes sentiment applications such as mental health flagging and content moderation.

---


### 143. [Decomposing Whole Slide Image Report Generation with Graph-Constrained Multiple Instance Learning Workflows](https://arxiv.org/abs/2608.15353)

**<font color=#1a73e8>作者：</font>** Antony Gitau, Martyna Borak, Bjørn-Jostein Singstad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide image (WSI) report generation requires recognizing spatially distributed pathological features and organizing them into a coherent diagnostic narrative. Although direct vision-to-text models can yield fluent reports, they obscure the contributions and failure modes of visual recognition, structured reasoning, and language generation. We propose a decomposed framework in which frozen Virchow2 tile embeddings are aggregated by multiple-instance learning (MIL) classification heads that answer organ-specific diagnostic questions. An organ-conditioned graph constrains the assembly of these answers into a structured reasoning chain, which a language model realizes as a pathology report. On the REG2026 held-out set of 2,028 slides, the proposed workflow achieved a chain-Jaccard score of 0.702. Performance fell to 0.420 without graph-based chain construction, 0.398 when the organ-specific graphs were replaced by a single organ-agnostic graph, and 0.371 when the language model constructed the chain freely from MIL predictions. Using the same report generator, graph-structured chains improved the report score from 0.330 to 0.495. On 350 external TCGA WSIs spanning the seven REG organs without fine-tuning, the expected organ graph was selected in 64.0% of cases and ranked among the top three in 86.6%. Providing the correct organ graph increased agreement with coarse TCGA primary-diagnosis labels from 61.8% to 92.6%, identifying organ routing as a main bottleneck under domain shift. Overall, organ-conditioned, graph-constrained chain assembly improves structured reasoning and report generation while enabling stage-specific error localization.

---


### 144. [Incoherent by Design? On the Moral Self-Consistency of LLMs](https://arxiv.org/abs/2608.15354)

**<font color=#1a73e8>作者：</font>** Pegah Nokhiz, Aravinda Kanchana Ruwanpathirana, Helen Nissenbaum  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used in morally sensitive contexts, yet it is unclear whether they apply ethical principles consistently across situations. A model that can state a moral principle may still violate it when the same scenario is rephrased or reframed. This inconsistency is a problem for any system whose outputs are used to inform moral decisions. If generative systems exhibit internal inconsistency, then the epistemic integrity of AI-mediated systems becomes uncertain. To study this concern, we investigate the stability of moral reasoning in LLMs within a controlled prompting framework across three major philosophical schools of thought: deontology, utilitarianism, and virtue ethics. We construct sets of morally equivalent scenarios in which the underlying situation is held constant while the framing varies to reflect different ethical stances and stylistic perturbations. We then evaluate responses from multiple models, including GPT, Mistral, and Llama. To assess consistency, we convert model outputs into structured logical statements and identify contradictions across responses generated within the same school of thought. Our results reveal substantial inconsistency with contradiction rates reaching up to 78% across scenarios. These findings point to a broader phenomenon of epistemic instability in generative AI wherein models fail to reliably maintain coherence with respect to their own prior outputs. This kind of instability carries real consequences. As generative systems influence how people form beliefs, judge actions, and absorb values, their inconsistencies can shape human reasoning and decision-making as well. Moreover, if a system cannot consistently represent its own normative commitments, then value alignment becomes a moving target rather than a well-defined objective. Thus, we argue that demonstrating internal incoherence is a necessary precursor to AI alignment.

---


### 145. [SAPE: Sandwich Adapters for Parameter Efficiency in Large Language Model Fine-Tuning](https://arxiv.org/abs/2608.15360)

**<font color=#1a73e8>作者：</font>** Mohammad Aref Jafari-Raddani, Morteza Mohajjel Kafshdooz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Parameter-Efficient Fine-Tuning (PEFT) has substantially reduced the hardware cost of adapting Large Language Models (LLMs) by decreasing the number of trainable parameters, recent studies have sought to further improve PEFT through parameter sharing. However, these approaches either employ uniform parameter sharing across layers, which can delay convergence, or rely on dynamic masking strategies, which add computational overhead. The potential of sharing patterns inspired by the inherent hierarchical structure of Transformer architectures remains unexplored in PEFT. To address this gap, we introduce SAPE (Sandwich Adapters for Parameter Efficiency), a PEFT framework based on a sandwich-style hard weight-sharing topology. SAPE routes intermediate Transformer layers through balanced shared group adapters while strictly isolating the input embedding and final projection boundary transformations to prevent gradient interference. This design significantly reduces memory consumption while eliminating the computational overhead associated with dynamic parameter-sharing methods. Extensive evaluations across encoder-only and causal decoder architectures demonstrate that SAPE achieves state-of-the-art performance in low-parameter regimes. On natural language understanding, SAPE outperforms proPETL on RoBERTa-large while utilizing only 10% of the baseline's parameter budget. On natural language generation and world knowledge reasoning with LLaMA-3.2 (3B) under a strict ~0.6M parameter constraint, SAPE outperforms AdaLoRA, yielding absolute improvements of +4.85% on GSM8K and +3.11% on CommonsenseQA. Furthermore, through comprehensive topological ablations, we formalize an inherent capacity trade-off: while hard parameter sharing strongly regularizes semantic generalization, it slightly smooths the sharp layer-wise transformations required for rigid multi-step arithmetic reasoning.

---


### 146. [FedPA-LoRA: Product-Aligned Framework for Mitigating Aggregation and Initialization Errors in Heterogeneous Federated LoRA](https://arxiv.org/abs/2608.15381)

**<font color=#1a73e8>作者：</font>** Juseok Jeon, Ramy E. Ali, Doyun Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) enables efficient federated fine-tuning of large language models, but its factorized parameterization creates a tension between accurate aggregation of local updates and continuity of locally optimized factors. Factor-wise aggregation incurs aggregation mismatch but better preserves factor continuity, whereas product-space reconstruction reduces this mismatch at the cost of greater factor-level initialization mismatch from newly reconstructed factors. We propose FedPA-LoRA, a product-aligned federated LoRA framework that jointly addresses these limitations and provably converges under both homogeneous and heterogeneous client ranks. Each client preserves its local factors across communication rounds and aligns its product toward a rank-specific global reference, maintaining local optimization continuity while promoting global consistency under data heterogeneity. The server aggregates heterogeneous-rank updates in the common product space and efficiently reconstructs a rank-constrained global adapter without forming the dense aggregate. This design supports client-specific computation and communication budgets. Experiments on natural language understanding and generation tasks show that FedPA-LoRA consistently outperforms representative baselines across varying levels of data heterogeneity and homogeneous- and heterogeneous-rank settings, with up to a $6.82$ percentage-point improvement in average GLUE accuracy under heterogeneous client ranks.

---


### 147. [Grounding Healthcare LLMs in a Causal Knowledge Graph: Framework, Metrics, and a Cardiovascular Pilot](https://arxiv.org/abs/2608.15382)

**<font color=#1a73e8>作者：</font>** Ummara Mumtaz, Aimen Noor, Awais Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly proposed for healthcare decision support, but their evaluations still reward single-answer accuracy rather than reasoning about interventions, mechanisms, harms, evidence, and uncertainty. We propose a reproducible, graph-centered evaluation framework for intervention-oriented LLM behavior in healthcare and stress-test it in a cardiovascular pilot. The framework has four components: (i) a domain causal knowledge graph in which assertions are first-class, provenance-preserving nodes with stable identifiers; (ii) a scenario-conditioned subgraph extraction step that, given any clinical scenario, retrieves the relevant reified-assertion subgraph; (iii) four controlled grounding conditions that vary how the retrieved subgraph is composed into the model's context (ungrounded C1, knowledge-graph C2, causal-graph C3, integrated C4); and (iv) an automated scoring pipeline, anchored on assertion identifiers, that computes intervention accuracy, and other evaluation measures on a single pass. To test the framework, we built a category-balanced scenario generator across eight reasoning failure modes and instantiated it on a cardiovascular graph. The metric panel discriminates conditions along interpretable, non-redundant axes: C4 obtains the strongest causal edge F1 (0.838), adverse-effect F1 (0.833), evidence accuracy (0.738), and unsupported claim rate (0.114), while C1 obtains the highest raw intervention accuracy (0.948) with no measurable causal or evidential grounding.

---


### 148. [Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference](https://arxiv.org/abs/2608.15383)

**<font color=#1a73e8>作者：</font>** Amjad Saab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) language models reduce arithmetic by activating only a small subset of experts per token, yet deployment still requires storing and moving the full expert bank. We present ExactMoE, an inference design that applies symmetric group-128 four-bit weight quantization only to routed experts, stores those experts in kernel-native MARLIN form in pinned host memory, and executes all selected experts through a configurable GPU-resident slot cache and fused grouped MoE kernels. The router, attention, embeddings, normalization layers, and language-model head remain in BF16. "Exact" refers to complete expert availability and an unchanged top-k routing procedure: no expert is pruned, substituted, or forced to execute on the CPU. It does not imply numerical identity with the BF16 model. On OLMoE-1B-7B-0924-Instruct, evaluated on a single NVIDIA L4, a 16-slot configuration reduces peak reserved GPU memory from 14.168 to 1.836 GiB (87.04%) while retaining 81.85% of BF16 decode throughput. A fully resident 64-slot configuration reaches 31.923 tokens/s versus 21.662 tokens/s for BF16 while reserving 4.061 GiB. Across 12,450 zero-shot multiple-choice questions, ExactMoE obtains 70.3534% normalized accuracy versus 70.8996% for BF16, retaining 99.23% of the baseline accuracy. In a matched 16-token ablation, fused grouped execution is 1.97x as fast as a sequential W4 reference. These results identify a practical memory-transfer-throughput frontier for complete-expert MoE inference.

---


### 149. [Agentic-SQL Revisited: Autonomy-Based Taxonomy and Empirical Benchmark Analysis for LLM Text-to-SQL](https://arxiv.org/abs/2608.15389)

**<font color=#1a73e8>作者：</font>** Changruo Zhao, Zujun Peng, Yu Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based Text-to-SQL progress is reported across heterogeneous benchmarks, backbones, and inference protocols, making cross-system comparison fragile. We reframe the field as a leaderboard aggregation: we collect the metrics authors themselves report and organize them along an inference-autonomy axis spanning constrained, in-context, iterative, agentic, and reasoning-internalized generation, with traceable provenance for every cell. To anchor the aggregation empirically, we run a focused case study on Spider, comparing 8B open-source backbones with and without chain-of-thought (CoT) supervision against few-shot DeepSeek~V3 and GLM-4 baselines. Four patterns emerge: Spider gains transfer unevenly to BIRD and Spider~2.0; autonomy buys robustness at non-trivial cost; reasoning internalization sits between answer-only decoding and externally orchestrated agents; and CoT gains concentrate on Hard and Extra-Hard queries. We release a Python harness mirroring the autonomy axis so that future methods can be added directly to the leaderboard.

---


### 150. [TwinGridShield: Consequence-Aware Runtime Authorization for LLM Grid-Agent Actions](https://arxiv.org/abs/2608.15391)

**<font color=#1a73e8>作者：</font>** Md Fazley Rafy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-assisted energy-management tools can translate natural-language context into structured grid commands, but syntactic validity does not imply physical admissibility. This paper presents TwinGridShield, a model-independent runtime authorization layer that evaluates each proposed action in a deterministic network twin before release. The prototype checks connectivity, branch-flow, generator, and load-shedding invariants and records each decision in a hash-chained log. A controlled IEEE 14-bus study evaluates single-step switching, redispatch, and load-shedding actions using DC power flow and experimentally assigned branch ratings. In the matched-model experiment, a stochastic proposal source configured to select an unsafe action with probability p=0.84 produced 421 unsafe proposals in 500 attacked-condition trials, a realized rate of 84.2%. This value characterizes the configured surrogate and is not an empirical measurement of LLM prompt-injection susceptibility. TwinGridShield produced 0 unsafe releases in those 500 trials. Because action labeling and authorization used the same DC model, system state, branch ratings, and encoded constraints, this result verifies conformance of the implementation to its encoded authorization predicate rather than safety under model error. The principal robustness evaluation therefore introduces model mismatch. Unsafe acceptance reached 5.63% under bounded +20% and -20% per-bus load-measurement error and 30.09% when actual branch ratings were 20% below modeled ratings.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
