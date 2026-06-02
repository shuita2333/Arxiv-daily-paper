# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-376](./part-08.md)

---

### 301. [Training Prompt Matters: State-Adaptive Optimization for Robust Fine-Tuning](https://arxiv.org/abs/2606.01967)

**<font color=#1a73e8>作者：</font>** Wenhang Shi, Yiren Chen, Shuqing Bian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While prompt engineering is instrumental in maximizing the capabilities of Large Language Models (LLMs) during inference, the role of prompts during training remains critically underexplored. Prevailing fine-tuning paradigms typically treat training prompts as mere surface forms, assuming that semantically equivalent instructions yield identical learning outcomes. However, we reveal that this equivalence is deceptive: while paraphrased prompts often lead to comparable in-task performance, they induce drastically different cross-task impacts regarding catastrophic forgetting and generalization. Crucially, these impacts are positively correlated across tasks, indicating the existence of superior prompts that consistently yield better performance. Furthermore, we discover that these superior prompts can be robustly identified by task loss prior to learning. Leveraging these insights, we introduce State-Adaptive Prompt Optimization (SAPO), a lightweight yet effective training strategy that shifts task formulation from a static input to a dynamic, state-adaptive variable. Comprehensive experiments on diverse benchmarks confirm its effectiveness, which significantly mitigates forgetting while improving generalization, achieving substantial performance gains over state-of-the-art methods. These results provide insights into how training prompts shape learning dynamics and offer a practical recipe for robust fine-tuning. Our code is available at this https URL.

---


### 302. [Algorithmic algorithm development with LLMs: A Case Study on LLM-Usage for Contraction Order Optimization in Tensor Networks](https://arxiv.org/abs/2606.01975)

**<font color=#1a73e8>作者：</font>** Fabian Hoppe, Melven Röhrig-Zöllner, Philipp Knechtges  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider LLM-based algorithm development through a case study on contractionorder optimisation for tensor networks with OpenEvolve. We pay particular attention to the choice of the LLM as well as design choices such as evaluation metric and test instances. Our results highlight both the promise of verifier-guided evolutionary coding agents for algorithm development/improvement and the continuing importance of evaluation, validation, and interpretation -- and corresponding challenges -- by the human scientist.

---


### 303. [An NLP-Driven Framework for Curriculum-Labor Market Alignment: Schema-Constrained LLM Extraction, ESCO-Anchored Semantic Matching, and Multi-Dimensional Gap Quantification](https://arxiv.org/abs/2606.01982)

**<font color=#1a73e8>作者：</font>** Sherzod Turaev, Mary John, Mamoun Awad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Schema-constrained information extraction from diverse educational and labor-market corpora remains an open challenge in natural language processing because existing pipelines rely primarily on lexical-surface methods that cannot recover implicit competencies, lack grounding in shared taxonomies, and provide no formal measures of extraction reliability or document-level completeness. To address these limitations, this paper proposes a four-stage NLP framework that combines (i) schema-constrained prompting of a two-model frontier-LLM ensemble against a JSON Schema-enforced seven-slot competency formalism, (ii) Sentence-BERT (SBERT) alignment of the extracted records against an eleven-domain ESCO v1.2.1 controlled vocabulary, (iii) a two-tier adjudication protocol that resolves inter-model disagreements, and (iv) a verification mechanism that combines per-slot Cohen's kappa, schema conformance, and document-level completeness audits. The framework is instantiated for a critical application in higher-education quality assurance, namely curriculum-labor market alignment for the ABET-accredited BSc Computer Science program at the United Arab Emirates University. The pipeline extracts 400 competency records from the 85-course 2025-2026 study plan and aligns them, under a five-scope analysis ranging from the computing core to a probability-weighted student trajectory, with 30 job postings (483 requirement clauses) at an SBERT cosine threshold of 0.50. The extractor achieves Cohen's kappa of 0.79 on the skill slot, with 100% schema conformance and 100% document-level completeness. The alignment surfaces interpretable supply-demand gaps of 25.0% in general and transversal skills, 13.8% in algorithms and computational theory, and 12.2% in software engineering and project management, with a near-zero 1.8% gap in artificial intelligence and data science despite 38.6% supply coverage.

---


### 304. [SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning](https://arxiv.org/abs/2606.01991)

**<font color=#1a73e8>作者：</font>** Lichao Wang, Zhaoxing Ren, Tianzhuo Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) agents increasingly leverage the Model Context Protocol (MCP) to operate in complex environments, the expansion of their action spaces offers agents unsafe capabilities and underscores the risk of power-seeking. While broad action space and greater environment influence are essential for task fulfillment, they create a fragile risk surface where minor errors or hallucinations are magnified into catastrophic failures. In response, we propose SafeMCP, a {server-side} defense plugin that constrains tool acquisition via predictive reasoning regarding future safety risks. SafeMCP utilizes an internal world model for look-ahead reasoning to implement a two-tier defense: proactive tool filtering to constrain hazardous power expansion and immediate intervention as a fail-safe. To train SafeMCP, we introduce a three-stage pipeline comprising environmental dynamic grounding, safe policy initialization, and reinforcement learning (RL) with dual verifiable rewards. Experiments on PowerSeeking Bench, ToolEmu, and AgentHarm show that SafeMCP achieves a safe equilibrium, effectively mitigating risks while preserving agent utility.

---


### 305. [MMG2Skill: Can Agents Distill In-the-Wild Guides into Self-Evolving Skills?](https://arxiv.org/abs/2606.01993)

**<font color=#1a73e8>作者：</font>** Xinyu Che, Junqi Xiong, Yunfei Ge 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Abundant procedural knowledge on the Web holds great potential for helping agents solve long-horizon tasks. However, such knowledge is often multimodal, heterogeneous, noisy, and implicitly assumes human executors, making it difficult to use directly as the skills required by agents. To bridge the gap between human-oriented guides and agent-executable skills, we formalize this problem as guide-to-skill learning: converting in-the-wild guides into executable skills and continuously improving them from trajectories observable to the agent. To evaluate the capability of existing agents on this task, we introduce MMG2Skill-Bench, the first benchmark designed for this problem. We further propose MMG2Skill, a closed-loop framework that compiles guides into editable skills, conditions a fixed vision-language model (VLM) agent on these skills during execution, and revises the skills from trajectory-level root-cause feedback without using benchmark scores. Across GUI control, open-ended gameplay, and strategic card play with six VLM backbones, MMG2Skill consistently outperforms vanilla baseline agents in every model-domain setting, achieving macro-average gains of +12.8 to +25.3 percentage points across backbones. Ablation studies show that directly prompting agents with raw guides can degrade performance, while both structured skill construction and trajectory-driven revision are necessary for the observed improvements. On success-inferable tasks, analyzer-based early stopping further prevents late-stage performance regressions and saves 25%-53% of attempts when the success signal is properly calibrated.

---


### 306. [CARTE: A Benchmark for Mapping Language Model Knowledge Across France](https://arxiv.org/abs/2606.01995)

**<font color=#1a73e8>作者：</font>** Sarah Almeida Carneiro, Christos Xypolopoulos, Xiao Fei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce CARTE 1 (Culturally Anchored Regional-Territorial Evaluation), a multiplechoice benchmark for evaluating the ability of large language models (LLMs) to perform fine-grained reasoning over geographically grounded and regionally differentiated knowledge within France. While prior benchmarks focus on national-level cultural understanding, they largely overlook intra-country variation and the need to distinguish between closely related regional contexts. CARTE addresses this gap by introducing 2,431 questions spanning the 13 metropolitan regions of France and covering 14 thematic domains, including culture, language, demographics, economy, environment, and mobility. We further introduce CARTE-LV, a subset targeting Linguistic Variation across French regions, enabling focused evaluation of language-related differences. We evaluate 27 LLMs ranging from 1B to 12B parameters under few-shot settings. Our experiments reveal performance disparities across regions and model scales, suggesting systematic gaps in pretraining coverage and limited robustness to intra-national variation.

---


### 307. [Scaling Agentic Capabilities via Grounded Interaction Synthesis](https://arxiv.org/abs/2606.02001)

**<font color=#1a73e8>作者：</font>** Wenhang Shi, Jinhao Dong, Yiren Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General agentic intelligence hinges on the ability to interact with diverse real-world tools to complete complex tasks, a capability fundamentally tied to the quality of interaction data. To bypass the prohibitive costs of human annotation, prevailing paradigms depend entirely on Large Language Models (LLMs) to scale the synthesis of agentic environments and tasks. However, such unconstrained generation often degenerates into biased random sampling of LLMs' internal priors, failing to capture the diversity and difficulty of real-world domains or construct high-fidelity, long-horizon tasks. In this work, we introduce Grounded Agentic Interaction Synthesis (GAIS), a framework that automates the scalable construction of diverse environments and complex tasks via a two-phase grounding mechanism. Specifically, we construct protocol-anchored environments derived from real-world Model Context Protocol (MCP) servers to ensure functional diversity and difficulty. Subsequently, we employ structure-guided planning to navigate these environments, actively enforcing logical dependencies and adversarial policies to generate complex tasks. Experiments on BFCL, $\tau^2$-Bench, and ACEBench demonstrate that GAIS-synthesized data significantly outperforms state-of-the-art baselines, enabling base models to match or even surpass their official instruction-tuned counterparts. Furthermore, GAIS exhibits superior data efficiency and scalability, achieving exceptional capabilities with significantly less data while maintaining continuous growth where baselines stagnate. Our code and dataset are publicly available at this https URL.

---


### 308. [PlanarBench: Evaluating LLM Spatial Reasoning via Planar Graph Drawing](https://arxiv.org/abs/2606.02010)

**<font color=#1a73e8>作者：</font>** Oleksandr Nikitin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> PlanarBench tests whether LLMs can draw planar graphs as ASCII art given only an edge list -- a spatial reasoning task that resists memorization because edge order, edge orientation, and node labels are all permutable.
We evaluate 91 models on the 199 simplest non-isomorphic connected planar graphs (2 - 7 vertices).
Edge count is the dominant difficulty predictor ($r = -0.85$) -- a finding not reported in prior LLM graph benchmarks, which use only node count as the difficulty axis.

---


### 309. [Extreme Low-Bit Inference in Reasoning Models: Failure Modes and Targeted Recovery](https://arxiv.org/abs/2606.02011)

**<font color=#1a73e8>作者：</font>** Ekaterina Alimaskina, Darya Rudas, Denis Shveykin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) rely on long reasoning traces, making inference expensive. While low-bit quantization reduces per-token decoding cost, we show that aggressive 2-bit inference can fail to deliver end-to-end speedup because instability in the generation process inflates total token count. Instead of merely lowering answer accuracy, 2-bit quantization often produces much longer traces with repetitive loops, budget exhaustion, delayed commitment, and unclosed reasoning segments. We analyze full reasoning traces of Qwen3 reasoning models across mathematical and commonsense benchmarks and show that accuracy degradation is tightly linked to these process-level failures. To address them, we introduce two lightweight controls: FP16 planning, which gives the 2-bit model a short high-precision outline, and loop rescue, which detects repetitive traces and either commits to an earlier answer or falls back to FP16. On MATH-500, loop rescue improves Qwen3-8B accuracy from 17.2% to 74.2%, while planning plus loop rescue improves Qwen3-32B from 65.0% to 87.2%. Overall, our results show that extreme low-bit reasoning becomes practical when its failures are treated as controllable generation pathologies: with lightweight detection and selective FP16 support, 2-bit inference can recover accuracy while preserving real end-to-end speed. Our code is available at: this https URL.

---


### 310. [OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents](https://arxiv.org/abs/2606.02031)

**<font color=#1a73e8>作者：</font>** Rui Yang, Qianhui Wu, Yuxi Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building capable visual web agents requires long-horizon reasoning, precise grounding, and robust interaction with dynamic real-world websites. Despite rapid progress, the strongest systems remain largely proprietary, while open agents still depend heavily on supervised post-training over large collections of curated web trajectories. This dependence creates a major scalability bottleneck: high-quality demonstrations are expensive to collect, and static datasets offer limited coverage of the diverse, ever-changing open web. Although online RL has shown promise for text-based agents, its potential for training visual web agents directly on live websites remains largely underexplored. In this paper, we introduce OpenWebRL, an open framework for training visual web agents with online multi-turn RL on real websites. OpenWebRL covers the full training pipeline, including scalable live-browser infrastructure, supervised initialization, multimodal context management, trajectory-level success judging, and efficient multi-turn policy optimization. Using this framework, we train OpenWebRL-4B, which establishes a new open-source state of the art on challenging live-web benchmarks. With only 0.4K initialization trajectories and 2.2K open-ended RL training tasks, OpenWebRL-4B achieves 67.0% success on Online-Mind2Web and 64.0% on DeepShop, outperforming prior open agents of similar or larger scale and remaining competitive with proprietary systems including OpenAI CUA and Gemini CUA. Beyond strong benchmark performance, we systematically study the key design choices that make online RL effective for visual web agents, and analyze how RL improves agentic reasoning. Overall, our work offers a practical path toward building more capable, reproducible, and cost-efficient open web agents. We will release our training data, models, and code to support future research.

---


### 311. [SentGuard: Sentence-Level Streaming Guardrails for Large Language Models](https://arxiv.org/abs/2606.02041)

**<font color=#1a73e8>作者：</font>** Jiaqi Yu, Xin Wang, Yixu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly stream long, reasoning-intensive responses in real time, making when to moderate as critical as whether to moderate. Existing guardrails fall into two unsatisfactory extremes: response-level methods delay intervention until the full output is generated, whereas token-level methods act on incomplete semantics, often producing unstable decisions and excessive guard invocations. To address this challenge, we propose SentGuard, a sentence-level streaming guardrail that operates in parallel with generation. A lightweight waiting buffer groups streamed tokens into sentence chunks and releases only verified chunks to the user, introducing a small offset that enables SentGuard to assess the current prefix while the target LLM decodes subsequent content. To support this, we construct StreamSafe, a benchmark with structured per-sentence annotations across 8 harm categories, capturing the evolution of safety risks across both reasoning and response segments. We further train SentGuard with a coarse-to-fine objective to detect unsafe intent as soon as it emerges at sentence boundaries. Experiments on 5 safety benchmarks show that SentGuard outperforms existing baselines, detecting 90.5% of unsafe cases within two sentences while maintaining a low streaming false-positive rate of 7.41%.

---


### 312. [Agentic-J: An AI Agent for Biological Microscopy Image Analysis](https://arxiv.org/abs/2606.02080)

**<font color=#1a73e8>作者：</font>** Lukas Johanns, Marilin Moor, Davide Panzeri 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Biological image analysis increasingly demands integration across heterogeneous tools, programming environments, and domain knowledge that few researchers can command simultaneously. We present Agentic-J, a containerised, multi-agent AI assistant, primarily for ImageJ/Fiji that enables biologists to specify analysis tasks in natural language, from nuclei segmentation and cell tracking to multi-condition quantification. The agent generates executable scripts organised into a documented project structure, so every analysis decision is traceable and the workflow can be reproduced or shared. The specialised sub-agents handle plugin management, code generation, debugging, quality assurance, and statistical reporting. In this paper we introduce the system's design, demonstrate real biological microscopy image analysis workflows, and detailed the technical implementation.

---


### 313. [DFlare: Scaling Up Draft Capacity for Block Diffusion Speculative Decoding](https://arxiv.org/abs/2606.02091)

**<font color=#1a73e8>作者：</font>** Jiebin Zhang, Zhenghan Yu, Song Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block diffusion speculative decoding accelerates LLM inference by predicting all tokens within a block simultaneously for the target model to verify in parallel. Predicting an entire block at once requires a sufficiently capable draft model and effective utilization of the target model's internal knowledge. However, the state-of-the-art method DFlash constrains all draft layers to share a single fused representation derived from only a few target layers, limiting per-layer expressiveness and hindering further scaling of draft capacity. In this paper, we present \modelname, which flares out the narrow conditioning bottleneck of DFlash through a lightweight layer-wise fusion mechanism: each draft layer attends to its own learnable combination of a broad set of target layers at negligible overhead, simultaneously injecting richer target knowledge and providing every draft layer with a distinct input. This enhanced per-layer expressiveness enables scaling the draft model to deeper architectures with consistent gains. We further scale training data from 800K to 2.4M samples to fully exploit the enlarged capacity. On six benchmarks spanning mathematical reasoning, code generation, and conversation, \modelname attains average wall-clock speedups of 5.52x on Qwen3-4B, 5.46x on Qwen3-8B, and 3.91x on GPT-OSS-20B, improving over DFlash by roughly 11\%, 8\%, and 5\% respectively. Our code is available at this https URL.

---


### 314. [PortBERT: Navigating the Depths of Portuguese Language Models](https://arxiv.org/abs/2606.02100)

**<font color=#1a73e8>作者：</font>** Raphael Scheible-Schmitt, Henry He, Armando B. Mendes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer models dominate modern NLP, but efficient, language-specific models remain scarce. In Portuguese, most focus on scale or accuracy, often neglecting training and deployment efficiency. In the present work, we introduce PortBERT, a family of RoBERTa-based language models for Portuguese, designed to balance performance and efficiency. Trained from scratch on over 450 GB of deduplicated and filtered mC4 and OSCAR23 from CulturaX using fairseq, PortBERT leverages byte-level BPE tokenization and stable pre-training routines across both GPU and TPU processors. We release two variants, PortBERT base and PortBERT large, and evaluate them on ExtraGLUE, a suite of translated GLUE and SuperGLUE tasks. Both models perform competitively, matching or surpassing existing monolingual and multilingual models. Beyond accuracy, we report training and inference times as well as fine-tuning throughput, providing practical insights into model efficiency. PortBERT thus complements prior work by addressing the underexplored dimension of compute-performance tradeoffs in Portuguese NLP. We release all models on Huggingface and provide fairseq checkpoints to support further research and applications.

---


### 315. [Multimodal Action Diffusion for Robust End-to-End Autonomous Driving](https://arxiv.org/abs/2606.02105)

**<font color=#1a73e8>作者：</font>** Jorge Daniel Rodríguez-Vidal, Diego Porres, Gabriel Villalonga Pineda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-End Autonomous Driving (E2E-AD) systems have largely converged on predicting intermediate trajectory waypoints, delegating final control to hand-crafted controllers with GPS access. Direct control-signal prediction (outputting throttle, steer and brake in an end-to-end fashion) remains underexplored, and critically, the role of action multimodality in such systems is not well understood. We argue that moving beyond deterministic, single-action outputs is not merely a modelling choice, but a key driver of driving performance, representational quality, and training stability. To validate this, we introduce the Action Diffusion Transformer (ADT), an anchor-free diffusion transformer trained with a MSE objective that natively models the multimodal distribution of plausible driving actions. Rather than committing to a single deterministic command, ADT generates K action candidates and selects the most suitable one at inference via Nearest Neighbour Matching (NNM). Beyond strong benchmark numbers, we show that action multimodality yields measurable benefits in learned representations and behavioral consistency, effects that deterministic architectures cannot replicate. ADT surpasses previous state-of-the-art on the challenging closed-loop Bench2Drive benchmark while achieving ten times lower latency, demonstrating that expressive, multimodal action modelling is both practically efficient and conceptually essential for robust end-to-end driving.

---


### 316. [When Tabular Foundation Models Transfer Across Modalities: A Systematic Evaluation Across 95 Datasets, 7 Modalities, and Two Regimes](https://arxiv.org/abs/2606.02106)

**<font color=#1a73e8>作者：</font>** Julien Lafrance  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a single classification pipeline that combines an Equiangular Tight Frame (ETF) preprocessing stage with a tabular foundation model for in-context inference, applied identically across modalities once data is mapped to fixed vector representations. We evaluate it on 95 datasets spanning seven signal modalities -- vision, audio, speech, text, molecular, time-series, and tabular. The main methodological contribution is to fix the comparison object: throughout the paper, performance is judged against the strongest lightweight tuned baseline on the same frozen features, while oracle selection, deployed selection, and specialized fine-tuning are reported separately.
The pipeline is broadly competitive with strong lightweight tuned baselines on the same frozen features. It does not match the very best specialized models or heavily tuned pipelines on every task, but it stays close, and it runs much faster -- typically 4 to 200 times faster than full backbone fine-tuning, often at comparable quality.
We describe how to deploy the pipeline in practice: when to apply ETF preprocessing, how to stop its training without a validation split, how to set up the in-context classifier, and how to calibrate the resulting probabilities. The calibration step is non-cosmetic: TabICL produces well-calibrated probabilities by construction, ETF preprocessing initially disrupts that calibration, and the post-hoc rescaling restores it -- yielding a per-prediction confidence signal that practitioners can use as a trust threshold for confidence-gated deployment. We also report where the pipeline should not be expected to help, and how to identify those cases in advance.

---


### 317. [BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning](https://arxiv.org/abs/2606.02109)

**<font color=#1a73e8>作者：</font>** Shannon Serrao, Soumitra Chatterjee, Dorina Strori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI systems that translate natural language into SQL queries and orchestrate multi-step agentic reasoning pipelines require evaluation approaches fundamentally different from academic benchmarks. Spider and BIRD established execution-accuracy protocols; G-Eval and RAGAS advanced LLM-based assessment; and recent work such as Spider 2.0, BEAVER, and BIRD-Interact has begun to address enterprise and agentic dimensions. No single framework unifies text-to-SQL assessment with agentic behavior evaluation into a production-grade pipeline calibrated against human expert judgment.
We present BADGER, developed at Merkle, a unified evaluation framework integrating text-to-SQL assessment with agentic behavior evaluation. BADGER offers three contributions. First, LLM-assisted SQL component extraction extending Spider methodology to handle CTE-heavy, dialect-specific SQL. Second, a hybrid execution accuracy metric (Hybrid-EX) resolving column-aliasing and numeric-tolerance brittleness by using an LLM to infer structural alignments before deterministic cell-level scoring. Validated on 150 human-annotated industry queries, Hybrid-EX achieves Cohen's kappa=0.717 [95% CI: 0.600-0.822] (Substantial agreement) and 87.3% balanced accuracy, outperforming all six competing frameworks (Delta-kappa: 0.322-0.502, all p<=0.001). Third, an enterprise agentic evaluation suite assembling RAGAS, G-Eval, and agent benchmark metrics into a unified pipeline; Excess Tool Usage is the sole novel element.
BADGER runs entirely within the client's governed data environment, supports configurable LLM judge backends, and enables rapid prototyping of client-specific judges and metrics, serving as a continuous evaluation backbone rather than a one-time quality gate.

---


### 318. [Jailbreaking Multimodal Large Language Models using Multi-Clip Video](https://arxiv.org/abs/2606.02111)

**<font color=#1a73e8>作者：</font>** Choongwon Kang, Seungjong Sun, Hyunmin Jun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal large language models (MLLMs) have advanced to process video inputs, concerns have emerged about their potential for malicious misuse. Prior jailbreak studies have shown that safety alignment in MLLMs can be bypassed through visual inputs, yet it remains unclear which properties of video inputs induce this vulnerability. To address this gap, we introduce Multi-Clip Video (MCV) SafetyBench, a dataset of 2,920 videos designed to evaluate how the diversity of video inputs affects the vulnerability of MLLMs. Each video consists of multiple short clips depicting diverse contexts related to a harmful query. Experiments on eight representative video MLLMs show that attack success consistently increases with the number of clips. Our results further indicate that the video modality is (1) more vulnerable than the image modality, (2) more vulnerable to dynamic videos than to static videos, and (3) more vulnerable when videos contain more diverse contexts. Building on these findings, we propose a defense strategy that leverages the relative robustness of the image modality.

---


### 319. [A Primer in Post-Training Reasoning Data: What We Know About How It Works](https://arxiv.org/abs/2606.02113)

**<font color=#1a73e8>作者：</font>** Yaoming Li, Guangxiang Zhao, Qilong Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training has become a primary driver of recent progress in large reasoning models, and reasoning data are often the key variable determining whether this stage succeeds. Work on post-training reasoning data has grown rapidly, yet this literature remains scattered across dataset papers, reinforcement-learning recipes, reward-model studies, benchmarks, and frontier system reports. This paper is the first primer to synthesize over 150 key public studies and system reports on post-training reasoning data. We organize the field around four questions: what data objects exist, what makes them useful, how they are constructed, and how they scale. Together, this organization provides an attribution framework for future reasoning-data releases and post-training recipes.

---


### 320. [Learning When Not to Act: Mitigating Tool Abuse in Agentic Reinforcement Learning](https://arxiv.org/abs/2606.02132)

**<font color=#1a73e8>作者：</font>** Liuji Chen, Dianxing Tang, Xing Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning can induce tool abuse, where models overuse external tools even for queries solvable by internal reasoning. Existing approaches mitigate this issue with uniform tool-use penalties or hard limits, which reduce tool frequency but may also suppress useful tool-assisted exploration. We propose EAPO, an Efficient Agentic Policy Optimization framework that learns selective tool use. EAPO introduces tool-free trajectories into each rollout group, applies difficulty-aware reward shaping to penalize redundant tool calls mainly on easier queries, and uses confidence-aware token reweighting to improve policy learning. Across nine mathematical and knowledge-intensive reasoning benchmarks, EAPO consistently improves the accuracy efficiency trade-off on Qwen2.5-3B, Qwen2.5-7B, and Llama3.1-8B. Compared with GRPO, EAPO improves average performance by 10.45%, 7.27%, and 9.69%, while reducing average tool calls by 18.33%, 18.33%, and 24.59%, respectively. These results show that agents can learn when not to use tools without compromising tool-integrated reasoning.

---


### 321. [InfoMerge: Information-aware Token Compression for Efficient Video Large Language Models](https://arxiv.org/abs/2606.02161)

**<font color=#1a73e8>作者：</font>** Xinxin Liu, Shiwei Gan, Xiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video-LLMs) achieve strong performance in video understanding, but their excessive visual tokens bring substantial computational overhead. Existing training-free compression methods improve inference efficiency by reducing visual tokens, yet they often rely on local adjacent-frame similarity for temporal redundancy estimation or allocate token budgets mainly according to segment length. Such designs are sensitive to frame-level noise and fail to capture the non-uniform information distribution of real-world videos. To address these challenges, we propose InfoMerge, a training-free visual token compression method that improves token utilization through robust redundancy estimation and content-aware budget allocation. Specifically, we propose the Temporal Fingerprint Difference: a segment-level second-order temporal redundancy estimation strategy, which models the temporal similarity structure of tokens at the same spatial positions within each segment. We further introduce Content-Aware Budget Allocation (CABA), which dynamically allocates segment-level token budgets based on segment uniqueness and spectral-entropy-based representational richness. By reducing repeated preservation of redundant static regions and allocating more tokens to informative segments, InfoMerge makes better use of the limited token budget while maintaining strong performance. Extensive experiments show that InfoMerge achieves strong efficiency--accuracy trade-offs across multiple benchmarks and backbones, with more pronounced advantages under aggressive compression. On LLaVA-OneVision-7B, InfoMerge retains 98.8\% of the original average performance while reducing 85\% of visual tokens and achieving a 4.24-fold speedup in the prefill stage.

---


### 322. [Multimodal Approaches for Visually-Rich Document Type Classification: A Comparative Analysis](https://arxiv.org/abs/2606.02162)

**<font color=#1a73e8>作者：</font>** Catyana Heyne, Jürgen Frikel, Filippo Riccio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document type classification in visually rich documents remains challenging, as relevant information is distributed across textual, visual, and layout modalities. To capture this complexity, current approaches rely on diverse multimodal modeling strategies, resulting in heterogeneous architectures that complicate systematic comparison. This variability is also reflected in existing comparative studies, which often rely on heterogeneous evaluation setups, further complicating systematic comparison and making it difficult to assess progress. To address these limitations, this work provides a structured analysis of multimodal design strategies across transformer- and LLM-based architectures, combined with a controlled empirical comparison within a unified experimental framework. Specifically, four representative models (LayoutLMv3, Donut, Qwen3-VL-32B-Instruct, and Qwen3-32B) are evaluated on the RVL-CDIP benchmark to systematically analyze the contributions of text, image, and layout information for document type classification, with a particular focus on contrasting OCR-dependent and OCR-free approaches. The results show that specialized multimodal Transformers outperform LLM-based approaches on visually rich and layout-intensive documents. Image information contributes most strongly to reliable classification, while OCR-derived text provides useful but secondary support. These findings highlight that multimodal processing remains essential for documents with pronounced layout structure. Overall, the study provides a systematic basis for comparing multimodal architectures and offers practical guidance for selecting effective feature combinations and model designs for document type classification.

---


### 323. [Context-Aware Workflow Decomposition for Automated Mobile UI Annotation Using Multimodal Large Language Models](https://arxiv.org/abs/2606.02208)

**<font color=#1a73e8>作者：</font>** Athar Parvez, Muhammad Jawad Mufti, Muqaddas Gull 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accurate mobile user interface annotation is important for UI understanding, accessibility tools, automated testing, dataset construction, and GUI agents. However, mobile screens are difficult to annotate because they often contain small, dense, nested, and visually ambiguous elements. Multimodal large language models can help automate this process, but their outputs are sensitive to prompt design and the organization of annotation tasks. This paper studies automated mobile UI annotation from a workflow design perspective, focusing on improving annotation precision. Rather than asking the model to annotate all UI elements in a single step, the task is divided into smaller context-aware stages, allowing related UI elements to be handled with clearer instructions and useful screen context. The proposed pipeline uses structured prompts, schema-constrained JSON outputs, and element-specific annotation instructions. Experiments are conducted on expert-annotated mobile UI screens from the MUIAnno dataset, using eight common UI element types: button, tab, clickable text, card, label, plain text, icon, and image. Four workflow strategies are evaluated: one-step, two-step, four-step, and eight-step annotation. Results show that the two-step workflow achieves the highest precision, while deeper decomposition improves recall but produces more false positives. Additional grouping experiments show that annotation quality depends on both workflow depth and element-class grouping. Overall, careful workflow design can make LLM-based mobile UI annotation more reliable for UI understanding, dataset construction, and GUI agent development.

---


### 324. [Do Gender Cues Affect LLM Value Trade-offs? Evidence from a Controlled Decision Benchmark](https://arxiv.org/abs/2606.02214)

**<font color=#1a73e8>作者：</font>** Yangyang Liu, Dong Yu, Pengyuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in value-sensitive decision settings, where irrelevant demographic cues should not alter judgments. We construct the Realistic Value Decision Benchmark (RVDB), a controlled benchmark that varies only the role-gender configuration while holding the scenario, ordered value pair, roles, candidate decisions, Value Distance, and Decision Severity fixed. Using a position-balanced evaluation across seven models, we test whether models preserve decision invariance under gender perturbations and whether their self-attributions reflect observed behavioral changes. We find that explicit gender cues induce bounded but systematic decision flips, including under an explicit gender-attribution prompt that asks models to report whether gender influenced their choice. Cross-gender role swaps reveal a consistent female-proposed-decision asymmetry, while models often attribute flipped decisions to No Influence or other non-gender factors. Further analysis shows that gender effects concentrate near less determinate value boundaries and under more severe decision contexts, suggesting that gender cues act as local boundary-shifting factors rather than global overrides of value reasoning. Value rankings remain largely stable, but ordered value-pair trade-offs shift unevenly across role-gender configurations. These results show that gender can enter LLM value trade-offs behaviorally while remaining obscured in self-attribution, motivating controlled behavioral audits beyond explanation-based evaluation.

---


### 325. [Better with Experience: Self-Evolving LLM Agents for Evidence-Grounded Health Community Notes](https://arxiv.org/abs/2606.02215)

**<font color=#1a73e8>作者：</font>** Zihang Fu, Fanxiao Li, Jianyang Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-augmented Community Notes offer a scalable path for timely, evidence-grounded correction of health misinformation on social platforms. However, they still reset at every post, leaving useful correction experience from prior cases unused. We introduce EvoNote, an agentic framework that enables health Community Notes generation to self-evolve through an evolving experience memory of prior misinformation correction episodes. Its core is fine-grained credit assignment: EvoNote grounds trajectory-level feedback in health-specific note qualities and distills it into action-level memory for claim analysis, evidence acquisition, and note writing. We evaluate EvoNote on MM-HealthCN, a 1.2K-instance multimodal benchmark of user-flagged health posts with human-written Community Notes and crowd-derived helpfulness labels. Under a human-validated hierarchical utility judge, EvoNote-generated notes are preferred over corresponding human-written notes in 89.6% of cases; on a separate set of Needs More Ratings posts without a crowd helpfulness verdict, EvoNote produces helpful notes for 82.0% of cases. It also reduces the median time needed to produce a candidate correction from over 13 hours in the human-note pipeline to under 2 minutes. Analyses link these gains to stronger evidence use and reusable correction strategies, positioning self-evolving note generation as a promising paradigm for health misinformation governance.

---


### 326. [Faster Synchronous On-Policy RL via Straggler-Aware Group Sizing](https://arxiv.org/abs/2606.02218)

**<font color=#1a73e8>作者：</font>** Azal Ahmad Khan, Ammar Ahmed, Zeshan Fayyaz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synchronous reinforcement learning methods such as Group Relative Policy Optimization (GRPO) provide stable and reproducible on-policy training, but they are highly vulnerable to stragglers, a single unusually long rollout can delay reward computation and parameter updates for the entire group. This problem becomes more severe as group size increases, creating a tension between the benefits of larger groups and the wall-clock cost of synchronization stalls. We propose Straggler-Aware Group Control (SAGC), a dynamic group-size controller that adapts the training group online based on observed rollout behavior. SAGC formulates group-size selection as an online constrained optimization problem, seeking to retain the benefits of larger groups while controlling the long-term rate of straggler events. Across synchronous GRPO and DAPO training, and on top of both vanilla and strong engineered baselines, SAGC consistently reduces straggler incidence and improves wall-clock efficiency while achieving competitive or better training reward. We further show that these gains transfer to final model quality: SAGC is competitive with or better than the strongest static group-size baseline on downstream reasoning benchmarks, and often produces shorter outputs without any explicit length penalty. These results position dynamic group control as a practical way to make synchronous on-policy RL more efficient and robust.

---


### 327. [Chroma Clues: Leveraging Color Statistics to Detect Synthetic Images](https://arxiv.org/abs/2606.02224)

**<font color=#1a73e8>作者：</font>** Lea Uhlenbrock, Davide Cozzolino, Christian Riess  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evolution and dissemination of AI-synthesized images is occurring at an unprecedented rate. Image generators are making rapid progress in their goal of perfectly imitating natural images, which also challenges image forensics.
In this work, we exploit an underexplored cue in current generative models, namely their weakness to imitate color statistics of natural images. We first show that the LPIPS loss used for training image generators is less sensitive to chrominance than to luminance, which may lead to statistical discrepancies in the colors of synthetic images. Building on this observation, we then introduce six hand-crafted color transformations and a method to learn a task-optimized color transform to statistically expose generated images. These transformations can be used in various ways. First, we define color-sensitive features at pixel-level or patch-level. A simple, interpretable classifier achieves with these features an average generalization accuracy of 93.27% and strong robustness against six types of post-processing. Second, we demonstrate that the transformations exhibit characteristic visual noise patterns in natural and synthetic image areas, which enables an intuitive visual image evaluation. Third, we demonstrate that the transforms can enhance color patterns in generated images for improved multiclass attribution.

---


### 328. [When Knowledge Is Not Free: Cost-Aware Evidence Selection in Retrieval-Augmented Generation](https://arxiv.org/abs/2606.02245)

**<font color=#1a73e8>作者：</font>** Mingyan Wu, Han Yang, Omer Ben-Porat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) typically assumes that external knowledge is free, but many high-quality sources are paywalled, licensed, restricted, or otherwise costly to access. We introduce cost-aware RAG, a setting where retrieved evidence is assigned access-cost tiers and systems must answer under an explicit evidence-access budget. We instantiate this setting by augmenting MS MARCO v2.1 with access-friction tiers and evaluate budgeted evidence selection across general-domain and domain-specific QA benchmarks. Our results show that static selection is brittle: no fixed selector uniformly dominates, and larger budgets do not reliably improve answer quality, even when costly evidence is domain-matched. We then study agentic cost-aware RAG, where an LLM decides when to retrieve, which tier to access, and when to stop. Agents show strong promise as adaptive evidence-acquisition controllers, but their behavior remains highly model- and task-dependent. These findings suggest that cost-aware evidence acquisition is a central challenge for the next generation of RAG systems. All code and data are available at this https URL.

---


### 329. [Ego-METAS: Egocentric online Multimodal Energy-efficient Temporal Action Segmentation benchmark](https://arxiv.org/abs/2606.02246)

**<font color=#1a73e8>作者：</font>** Maria Santos-Villafranca, Jesus Bermudez-cameo, Alejandro Perez-Yus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To operate in the physical world, embodied agents must perceive their environment in an "always-on" fashion, selectively accessing the most informative sensors to balance energy constraints and task accuracy. Despite its importance for resource-constrained devices, energy-aware perception remains under-explored, with most prior work assuming unlimited compute. To address this, we introduce Ego-METAS: the first Egocentric online Multimodal Energy-efficient Temporal Action Segmentation benchmark. Ego-METAS provides a unified testbed of more than 100 hours of untrimmed egocentric video from EgoExo4D, CMU-MMAC, and CaptainCook4D, spanning 5 modalities (RGB, audio, gaze, IMU, and monochrome camera). We formulate an online temporal action segmentation task where models must dynamically select which sensors to activate at each timestep while strictly adhering to hardware-representative energy budgets. Alongside the benchmark, we release unified splits, cleaned annotations, pre-extracted features, and a diverse suite of baseline routing policies. Our evaluations show that optimal routing is highly scenario-dependent, and that existing policy-learning methods, designed primarily for trimmed clips, struggle to adapt to continuous, untrimmed environments. However, even simple dynamic fusion of complementary modalities (e.g., via random routing) proves critical for balancing predictive accuracy against strict energy budgets. Ultimately, Ego-METAS provides a standardized foundation to develop robust, cost-aware policies for autonomous, always-on embodied AI.

---


### 330. [Geometric Latent Reasoning Induces Shorter Generations in LLMs](https://arxiv.org/abs/2606.02248)

**<font color=#1a73e8>作者：</font>** Shashi Kumar, Yacouba Kaloga, Petr Motlicek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models solve complex problems by generating lengthy chains of explicit reasoning tokens. While effective, this makes reasoning expensive, length-sensitive, and constrained to (discrete) natural language. While latent reasoning offers a continuous alternative, determining useful structures for intermediate latent states is an open challenge. In this paper, we formulate latent reasoning as a geometric path-approximation problem within the model's pretrained token-embedding space. We introduce Geometric Latent Reasoning (GLR), which uses a lightweight transition head to predict iterative direction updates in embedding space. Using textual chain-of-thought traces as anchors, GLR learns to approximate discrete reasoning trajectories while permitting continuous deviations from exact token embeddings. Evaluations on mathematical reasoning benchmarks using Qwen3 models reveal an emergent phenomenon: geometric latent reasoning induces substantially shorter generations without an explicit length objective. By replacing early explicit reasoning with continuous latent steps, models often reach correct answers using substantially fewer total generation steps. These findings suggest that continuous trajectories act as compact intermediate reasoning states, exposing a new tradeoff between latent computation budget, output length, and accuracy.

---


### 331. [ResMerge: Residual-based Spectral Merging of Large Language Models](https://arxiv.org/abs/2606.02252)

**<font color=#1a73e8>作者：</font>** Yandu Sun, Zhiyan Hou, Haokai Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model merging offers a training-free way to combine multiple post-trained expert models, but merging experts obtained through reinforcement learning (RL) remains challenging. Existing spectral merging methods often assume that leading singular directions contain the main task signal, while lower-energy residual components can be compressed, selected, or attenuated to reduce interference. We find that this assumption does not hold for RL task vectors: after decomposing each task vector into a leading spectral head and a residual component, both parts can independently recover substantial behavior knowledge, while exhibiting different merging properties. The head is highly concentrated and informative but more prone to sharp cross-expert conflicts, whereas the residual component is more dispersed and provides a more stable basis for aggregation. Based on this observation, we propose ResMerge, a residual-based spectral merging framework for RL experts. ResMerge first constructs a stable residual backbone with Spherical Residual Consensus Adaptation, which estimates a reliability-weighted consensus direction on the Frobenius sphere. It then reintroduces leading-head information through a Lightweight Head Correction module gated by positive cross-expert agreement. Experiments across multiple RL expert groups and capability domains show that ResMerge better preserves expert capabilities than representative task-vector and spectral merging baselines. The implementation of ResMerge is publicly available at this https URL.

---


### 332. [Vision-language Models for Driver Monitoring Systems: A Driver Activity Description Dataset](https://arxiv.org/abs/2606.02273)

**<font color=#1a73e8>作者：</font>** David J. Lerch, Sarath Mulugurthi, Manuel Martin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding subtle driver actions is essential for building reliable driver monitoring systems. Existing visionlanguage models (VLMs) are trained on general datasets and struggle to recognize fine distinctions in driver behaviors. This paper addresses this limitation by creating a detailed natural language version of the Drive&Act dataset. We evaluate three VLMs on our new benchmark using LLM-based scoring methods. Their performance on the new benchmark shows that they cannot reliably generate accurate fine-grained driver activity descriptions. Based on the labeled Drive&Act dataset we create a new Drive&Act description dataset containing finegrained descriptions to train VLMs on driver activity understanding. Cross dataset evaluation on the Driver Monitoring Dataset (DMD) shows that the VLM fine-tuned on our new Drive&Act description dataset generalizes well to actions in the DMD dataset. The VLM fine-tuned on our Drive&Act description dataset achieves an ACCR score of 76 outperforming the zero-shot VLM baseline with an ACCR score of 66. These findings demonstrate that adapting VLMs with richly described driver actions can significantly improve their ability to interpret driver behavior while also highlighting the need for more diverse datasets to support broader generalization in future applications. Our Drive&Act description dataset and code will be publicly available on GitHub.

---


### 333. [Cross-modal linkage risk in clinical vision-language models](https://arxiv.org/abs/2606.02276)

**<font color=#1a73e8>作者：</font>** Soroosh Tayebi Arasteh, Mahshad Lotfinia, Sven Nebelung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) trained on paired chest radiographs and radiology reports learn a shared embedding space that can preserve instance-level image-report correspondence. This poses a privacy risk in settings where radiographs and reports are deliberately kept separate after acquisition, such as image-only data sharing or access-controlled reports, because a de-identified image may be re-linked to its original narrative report through cosine similarity alone. We formalized this as image-to-report retrieval and used public paired cohorts, in which the true pairing is known by design, as ground-truth benchmarks to audit the risk rather than as the privacy scenario. Evaluating VLMs of increasing clinical specialization on 406,241 paired examples from 126,804 patients across MIMIC-CXR (43,793 held-out pairs) and external CheXpert Plus (29,296 pairs), we found that re-linkage rose systematically with specialization: the strongest VLM retrieved the correct report at 15 times chance at a candidate pool of N = 100, 50 times chance at N = 10,000, and well above chance at full-database scale. The signal persisted under pathology-matched hard negatives that removed disease-label shortcuts, indicating correspondence beyond broad diagnostic categories. To reduce it without retraining, we froze both encoders and applied differentially private optimization only to the projection heads defining the alignment layer (epsilon = 0.34, delta = 6x10-6). This reduced Recall@1 by 61.8% at N = 10,000 on MIMIC-CXR and transferred to CheXpert Plus without retraining, while image-side utility was largely preserved: macro AUROC for linear-probe classification across 14 labels shifted only from 79.63% to 79.43%. Targeted DP finetuning of the shared alignment layer can substantially reduce cross-modal re-linkage without materially degrading the image representations that make these models clinically useful.

---


### 334. [POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems](https://arxiv.org/abs/2606.02282)

**<font color=#1a73e8>作者：</font>** Iñaki Dellibarda Varela, R. Sendra-Arranz, Pablo Romero-Sorozabal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Orchestrating Large Language Models into Multi-Agent Systems (LLM-MAS) has unlocked remarkable reasoning capabilities, yet emergent failures and hallucinations that resist characterisation block their deployment in safety-critical domains -- a gap made legally untenable by emerging AI regulation. Existing evaluation paradigms share a common flaw: centralised judgment creates single points of failure and demands domain-specific expertise. Here we present POIROT, a protocol that repurposes a system's own agents as its diagnostic layer, leveraging the epistemic diversity already present in the architecture. Across evaluated settings, POIROT outperforms single-LLM evaluator baselines, with gains that scale with problem complexity (OR = 1.60, $p = 0.008$), agent count, and fault dimensionality, persisting under compound fault conditions. These results demonstrate that safety oversight need not be externalised: the agents executing a role carry sufficient collective intelligence to audit it. We release POIROT as an open-source library alongside BLAME, a benchmark for fault attribution in safety-critical multi-agent systems.

---


### 335. [Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization](https://arxiv.org/abs/2606.02288)

**<font color=#1a73e8>作者：</font>** Yung-Chin Chen, Chung Peng Lee, Ze-Wei Liou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Massive activation spikes in Large Language Models (LLMs) severely degrade quantization by stretching dynamic ranges. While prior hypotheses characterize these as high-level scalar biases, we argue that they are merely the scalar intermediates of rigid, structural vector biases in the spike-carrying tokens. We show that these tokens converge to constant vectors after normalization that drive the attention sink and value-state drain mechanisms. We geometrically substantiate this by analyzing the coordination of projection weights: $W_K$ contrastively amplifies the vector, $W_Q$ aligns semantic tokens toward it, and $W_V$ projects it into the spectral null-space. Furthermore, we reveal that the model actively preserves these structural biases against Rotary Positional Embedding (RoPE) perturbations by localizing them in "zones of rotational stability" utilizing low-frequency bands and coherent channel pairs. Leveraging this, we propose INSERTQUANT, a post-training quantization (PTQ) framework that clamps spikes and restores their function via pre-computed template vectors. This renders activations strictly spike-free, enabling robust low-bit quantization with high fidelity. INSERTQUANT achieves parity with state-of-the-art per-tensor quantization methods on LLMs and uniquely generalizes beyond text to other modalities such as ViTs.

---


### 336. [DECK: A Consistency x Confidence Taxonomy of LLM Hallucinations](https://arxiv.org/abs/2606.02289)

**<font color=#1a73e8>作者：</font>** Mohit Singh Chauhan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing hallucination taxonomies classify LLM errors by what is wrong with the output -- memorised misconceptions, reasoning failures, fluent fabrications. These taxonomies are useful for diagnosis but cannot answer a different question: which uncertainty scorer would have caught this error? We propose a complementary taxonomy that classifies errors by their detectability signature -- the signal a scorer family would read.
The DECK taxonomy is a 2x2 partition along inter-sample consistency and token-level confidence into four behavioural regimes (Drift, Entrenched, Confabulation, Knotted), each mapping to a specific scorer family (or families) that can detect it: black-box consistency scorers have signal in D and C, white-box token-probability scorers have signal in K and C, and only an LLM-as-a-Judge with independent pretraining can detect E. Cell membership is operationalised by a Youden's J optimal split on each scorer axis.
Across three models and four datasets we validate the taxonomy two ways: by analysing scorer-pair disagreement, and by checking that external labels (SelfAware unanswerable, HaluEval adversarial, PopQA entity popularity) land in the predicted DECK cells, with model-scale and content-specific secondary-cell refinements.
We further identify a universal blind spot of output-level UQ: on knowledge-gap inputs where the generator emits confident, repeatable fabrications, every output-level family collapses by construction. A linear probe on Llama-3-8B's hidden states also collapses to chance, giving preliminary evidence that the failure may persist at the activation level; richer internal-state methods (UQ heads, information-theoretic estimators) remain to be tested.

---


### 337. [Beyond Isolated Behaviors: Hierarchical User Modeling for LLM Personalization](https://arxiv.org/abs/2606.02300)

**<font color=#1a73e8>作者：</font>** Liang Wang, Xinyi Mou, Xiaoyou Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse domains, yet personalizing their outputs to individual users remains an open challenge. Existing approaches predominantly adopt a flat behavioral paradigm, aggregating user behaviors without an explicit account of how they are organized into deeper behavioral structures. In this work, we draw on Pierre Bourdieu's Theory of Practice to propose PHF (Practice-Habitus-Field), a sociologically grounded framework that reconceptualizes LLM personalization through three hierarchical levels: individual behaviors as practices, their temporal accumulation into stable dispositions as habitus, and shared regularities across similar users as fields. We instantiate PHF through $\mathrm{PHF}_{\text{Compass}}$, a lightweight and model-agnostic implementation based on a frozen LLM. Experiments on the Language Model Personalization (LaMP) benchmark demonstrate consistent improvements across diverse tasks, while further analyses validate the interpretability and extensibility of the learned behavioral structures.

---


### 338. [Unified Context Evolution for LLM Agents](https://arxiv.org/abs/2606.02304)

**<font color=#1a73e8>作者：</font>** Zixuan Zhu, Yitong Hu, Yong Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can solve multi-step interactive tasks by combining reasoning with environment feedback, yet each episode starts from the same fixed context and any useful strategy discovered along the way is lost once the task ends. Existing approaches either limit learning to the current task or pool all experience into a single untyped store, without distinguishing knowledge types, tracking quality through use, or balancing what the library still lacks. We introduce Unified Context Evolution (UCE), a gradient-free framework that externalizes agent experience into an evolving library of typed Evolvable Context Units (ECUs). UCE decomposes experience into four complementary types (Memory, Strategy, Workflow, and Skill), each generated from trajectories under type-specific conditions, retrieved at decision time, scored through repeated usage outcomes, and pruned when no longer valuable. A scheduling module allocates each cycle's generation budget toward the types where the library is weakest. Across two interactive benchmarks, UCE raises ALFWorld success from 75.4% to 96.3% and WebShop task score from 45.1% to 61.3%, and the accumulated library transfers to alternative actor backbones without retraining.

---


### 339. [Training-Free Composed Video Retrieval via Visual Representation-Guided Video-LLM Reasoning](https://arxiv.org/abs/2606.02321)

**<font color=#1a73e8>作者：</font>** Yang Liu, Qianqian Xu, Peisong Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large vision-language models have expanded video retrieval from simple text-based search to more flexible scenarios, where users may specify the desired result through both visual examples and textual instructions. In the CVPR 2026 Reason-Aware Composed Video Retrieval Challenge, the system is required to retrieve a target video according to a reference video and a modification instruction. To address this task, we develop Visual Representation-Guided Video-LLM Reasoning for Training-Free Composed Video Retrieval. Our framework first uses frozen DINOv3 models to obtain a compact set of visually relevant candidates, and then applies large vision-language models to evaluate whether each candidate satisfies the modification instruction. A final reasoning-based refinement is further performed on the top candidates to improve the first-ranked prediction. Without training, our system achieves 48.78 Recall@1 and 51.48 Recall@5 on the test set. Future work may further improve retrieval accuracy through stronger video-LLMs and detailed integration between visual representations and language reasoning.

---


### 340. [Repurposing Adversarial Perturbations for Continual Learning: From Defense to Active Alignment](https://arxiv.org/abs/2606.02322)

**<font color=#1a73e8>作者：</font>** Ran Liu, Min Yu, Mingqi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In dynamic environments, large language models need to keep adapting to new tasks, but continual learning often suffers from forgetting, limited transfer, and vulnerability to adversarial perturbations. To address this, we present AdvCL, which repurposes adversarial perturbations as a geometric control signal for stable continual adaptation. AdvCL combines three plug-in modules: Intra-Smooth promotes local smoothness via small adversarial perturbations; Proto-Clip uses similarity clipping to prevent excessive alignment to current task prototype; and Inter-Align applies directional alignment toward previous task prototype to reduce representational gaps. Experiments show consistent gains in both standard performance and robustness, with lower forgetting and stronger transfer. We further analyze key mechanisms by quantifying the sensitivity of Intra-Smooth to perturbation settings and the effect of Inter-Align on task similarity and geometric distance. In summary, the modules provide complementary gains when combined, and each can also be integrated individually into diverse CL paradigms, including replay, regularization, and dynamic architectures, thereby offering a geometric control mechanism for continual learning.

---


### 341. [Multi-modal Video Representation Alignment for Robust Self-supervised Driver Distraction Detection](https://arxiv.org/abs/2606.02352)

**<font color=#1a73e8>作者：</font>** David J. Lerch, Livien Majer, Zeyun Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust self-supervised learning of multi-modal video representations is critical for real-world applications such as driver distraction detection, where multiple sensors provide complementary but noisy signals. Conventional contrastive objectives, such as InfoNCE, assume all negatives are equally informative and all positives are reliable. However, this assumption is frequently violated in multi-modal data due to viewpoint changes, occlusions, or semantic overlap across modalities. In this work, we propose a novel framework for multi-modal global alignment that addresses these challenges by jointly modeling faulty negatives and unreliable or faulty positives. We introduce soft targets derived from cycle-consistency scores to relax the hard-negative assumption, and a weighting mechanism based on similarity distributions to mitigate the impact of noisy or faulty positives. Our approach extends traditional pairwise alignment to a principled global multi-modal setting, aggregating alignment information across all modality pairs. We evaluate our method on the Drive&Act dataset, demonstrating that it consistently outperforms both pairwise and existing global alignment baselines across RGB, IR, Depth, and Skeleton modalities. Cross-view ablation studies further show strong generalization to unseen camera perspectives, highlighting the robustness of our representations. Overall, our framework provides a scalable and effective solution for self-supervised global multi-modal representation learning, enabling reliable driver distraction detection and pioneering in real-world multi-modal video understanding. Our code will be published on GitHub.

---


### 342. [SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training](https://arxiv.org/abs/2606.02355)

**<font color=#1a73e8>作者：</font>** Zhongyu He, Yuanfan Li, Fei Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents can benefit from reusable skills, yet existing skill-based methods often rely on external skill generators during training or persistent skill retrieval at inference, increasing engineering complexity, context length, and deployment latency. We propose Self-Internalizing Reinforcement learning with Intrinsic skills (SIRI), a three-phase framework that enables agents to discover, validate, and internalize skills without external skill generators or inference-time skill banks. SIRI first warms up the policy with GiGPO to acquire basic interaction ability and collect successful skill-free trajectories. It then performs self-skill mining, where the current policy summarizes compact skills from its own successful plain rollouts and validates them through paired skill-augmented and skill-free rollouts. Finally, SIRI distills only beneficial skill-guided action tokens into the plain policy using trajectory-level utility and action-level advantage. At inference, the agent runs with the original prompt only. On ALFWorld and WebShop with Qwen2.5-7B-Instruct, SIRI improves GiGPO from 0.908 to 0.930 on ALFWorld and from 0.728 to 0.813 on WebShop, outperforming prompt-based, RL-based, and memory-augmented baselines. Further analysis shows that our self-mining strategy can achieve performance comparable to distillation with closed-source large model. Our code is available at this https URL.

---


### 343. [Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains](https://arxiv.org/abs/2606.02357)

**<font color=#1a73e8>作者：</font>** Garvin Guo, Donglei Yu, Yu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-augmented multimodal agents show strong benchmark gains, often taken as evidence that agents have learned to use tools. We argue that this interpretation can be premature: a tool-call trace alone does not show whether the tool supplied answer-critical information. We study two representative ``thinking with images'' agents, Thyme and DeepEyesV2, across real-world understanding, OCR, chart understanding, and mathematical reasoning. Each agent is compared with its Tool-Free counterpart and with a Pure-Text Reasoner trained from the same source pool without tool-calling trajectories. Tool access yields little consistent aggregate improvement, does not reliably reduce generated-token cost, and leaves only a small tool-only solved set: 93% of DeepEyesV2's tool-solved problems and 96% of Thyme's are also solved by at least one non-tool setting. Mechanism ablations further show that the full tool-use loop does not consistently outperform either the tool-call format or the returned execution result alone. In the settings we study, the analyzed agents appear to learn tool-calling patterns more reliably than tool-contributed capabilities, suggesting that evaluation should distinguish tool availability from whether tools actually expand what agents can solve.

---


### 344. [MOC: Multi-Order Communication in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2606.02359)

**<font color=#1a73e8>作者：</font>** Yao Guan, Lin Wang, Zhihu Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable progress of Large Language Model (LLM) based Multi-Agent Systems, most research focuses on optimizing coordination topology while largely underexploring the equally critical problem: how to transmit and optimize messages among agents effectively? Current communication schemes typically rely on the direct concatenation of first-order neighbor responses, which induces a restricted evidence receptive field and leads to the dilution of crucial insights over multi-hop paths. To address these limitations, we propose the Multi-Order Communication (MOC) scheme, which reconstructs the inter-agent communication to capture multi-hop dependencies and incorporates a structural message consolidation strategy to ensure efficiency. Specifically, we formalize the communication mechanism to construct a structured multi-order evidence stream, and subsequently design a Semantic-Topological Merging algorithm to optimize semantic fidelity within token constraints. Extensive experiments across six diverse datasets and LLM backbones of varying parameter scales demonstrate that MOC consistently improves task performance and reduces communication costs. The code is available at this https URL.

---


### 345. [COMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/abs/2606.02372)

**<font color=#1a73e8>作者：</font>** Youwei Liu, Jian Wang, Hanlin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution. However, existing textual world models are typically fixed after training, preventing them from adapting to the on-policy state-action distributions induced by an evolving agent. Meanwhile, agent-improvement methods often rely on external rewards or verifiers, limiting their applicability in realistic interactive environments. In this paper, we propose COMAP, a novel framework that co-evolves textual world models and agent policies through closed-loop interaction. At each decision step, the world model predicts future state feedback for candidate actions, and the agent performs future-aware reflection by estimating the reliability of this feedback and refining its action accordingly. The resulting on-policy trajectories are then used to update the world model via self-distillation, allowing it to better match the agent's evolving interaction distribution. Across embodied task planning, Web navigation, and tool-use benchmarks, COMAP consistently outperforms competitive baselines, e.g., +16.75% relative improvement with Qwen3-4B. Further analyses show that the co-evolutionary loop improves the world model's prediction accuracy over time and leads to more effective long-horizon decision-making. Our code is available at: this https URL.

---


### 346. [Spatial Representation Learning Beyond Pixels: Unifying Raster Data and Vector Semantics for Human-Centric Geospatial Foundation Models](https://arxiv.org/abs/2606.02374)

**<font color=#1a73e8>作者：</font>** Steffen Knoblauch, Hao Li, Gengchen Mai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO) has fundamentally transformed the monitoring of environmental processes and human activities up to planetary scale. Recent advances in self-supervised learning have given rise to Earth Observation Foundation Models (EOFMs), which leverage petabyte-scale unlabeled EO data to learn transferable representations across a wide range of downstream geospatial tasks. Despite these advances, current EOFMs remain largely confined to raster modalities, overlooking the rich, structured information encoded in openly-accessible vector data sources such as OpenStreetMap and Overture. Vector data provides explicit and compact representations of geographic entities, including geometry, topology, and semantic relationships, offering critical contextual signals that are often ambiguous or inaccessible in imagery alone. Raster and vector data thus represent complementary views of geographic space: raster data captures continuous physical and spectral patterns, while vector data encodes discrete objects and their relational structure and often represents more of the human rather than the physical systems (e.g. social or demographic data). However, existing geospatial representation learning paradigms treat these modalities in isolation, relying on imperfect and often lossy transformations to bridge them. This perspective paper calls for a paradigm shift toward joint Spatial Representation Learning (SRL) in an unified embedding space that integrate raster perception with vector-based reasoning. Building on emerging efforts in multimodal geospatial learning, we highlight conceptual foundations, technical challenges, and promising directions for aligning heterogeneous spatial data sources. We contend that such integration is essential for developing next-generation geospatial AI systems capable of more accurate, interpretable, and semantically grounded understanding of the Earth.

---


### 347. [AgentPLM: Agentic Protein Language Models with Reasoning-Augmented Decoding for Protein Sequence Design](https://arxiv.org/abs/2606.02386)

**<font color=#1a73e8>作者：</font>** Sahil Rahman, Maxx Richard Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein language models (PLMs) are passive oracles: they generate sequences in a single forward pass with no mechanism to consult external biophysical feedback or redirect generation when a candidate violates thermodynamic or structural constraints. We introduce AgentPLM, which addresses this by equipping a pre-trained PLM with i) Reasoning-Augmented Decoding (RAD), which interleaves autoregressive generation with tool calls (ESMFold, FoldX, AutoDock Vina), and ii) Contrastive Agent Policy Optimisation (CAPO), a trajectory-level extension of direct preference optimisation that trains the policy end-to-end to learn when oracle feedback is informative rather than merely imitating high-fitness sequences. We evaluate AgentPLM on benchmark tasks spanning de novo enzyme design, antibody optimisation, thermostability, PPI interface design, and zero-shot fitness prediction with standardised oracle APIs and controlled sequence-identity splits. AgentPLM achieves state-of-the-art results with a gain in antibody top-10% hit rate over the strongest passive baseline, providing mechanistic evidence of online error correction without explicit backtracking.

---


### 348. [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388)

**<font color=#1a73e8>作者：</font>** Ning Lu, Baijiong Lin, Shengcai Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) improves large language model (LLM) agents by teaching them which actions lead to high rewards, but provides little supervision on what those actions do to the environment. World modeling (WM) can fill this gap, yet existing approaches often require separate simulators, extra training stages, or additional inference-time computation. We observe that on-policy RL rollouts already contain the needed signal: each transition pairs an action with its resulting next observation. Based on this observation, we propose PaW, a Policy and World modeling co-training framework that adds auxiliary WM supervision to the same policy during RL, without changing the inference paradigm. To make auxiliary WM supervision informative and stable, PaW introduces three components: action-entropy-based WM data selection, noise-tolerant WM loss, and reward-adaptive loss balancing. Experiments on three agentic task benchmarks show consistent improvements over strong RL baselines across models and RL algorithms. These results suggest that standard RL rollouts are a practical source of WM supervision for language-agent training.

---


### 349. [A Local Perturbation Theory for Cross-Domain Interference and Recovery in Multi-Domain RL](https://arxiv.org/abs/2606.02398)

**<font color=#1a73e8>作者：</font>** Lei Yang, Siyu Ding, Deyi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training improves large language models (LLMs) on individual domains such as mathematical reasoning, code generation, question answering, and creative writing (CW), but training on one domain often degrades performance on others. Existing explanations based on catastrophic forgetting or global gradient conflict are incomplete: substantial interference can occur even when full-model gradients are nearly orthogonal. We show that single-domain RL produces sparse, small-magnitude parameter edits with weak overlap among top-changed neurons, while different domains still share substantial active computation routes on which update directions determine whether they act synergistically or conflict. Guided by this observation, we prove under a local perturbation model of multi-domain RL that later-domain training harms an earlier domain mainly through a second-order damage term, which under the observed sparse route structure concentrates in a low-dimensional shared conflict subspace. Moreover, a short domain refresh contracts the harmful component on this subspace, enabling selective recovery with limited collateral damage. Consistent with the theory, a brief Re-Math refresh after Code $\rightarrow$ Math $\rightarrow$ QA $\rightarrow$ CW recovers Math from 57.66 to 66.04 while largely preserving performance on the other domains, yielding the best average score of 66.39. Beyond refresh, a training-free rollback on a sparse proxy conflict coordinate set for the Math-QA pair partially restores Math, providing direct proxy-level evidence for localized damage. These results provide a localized mechanistic account of interference and recovery in multi-domain RL.

---


### 350. [K-BrowseComp: A Web Browsing Agent Benchmark Grounded in Korean Contexts](https://arxiv.org/abs/2606.02404)

**<font color=#1a73e8>作者：</font>** Nahyun Lee, Dongkeun Yoon, Guijin Son 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier model evaluations are shifting from foundational capabilities (e.g., instruction following and reasoning) toward compositional, agentic ones, but Korean agentic benchmarks remain scarce. We introduce K-BrowseComp, a web-browsing agent benchmark grounded in Korean contexts, consisting of 400 problems. The 300-problem K-BrowseComp-Verified subset is manually constructed and validated by native Korean speakers. On this subset, frontier LLMs, including GPT-5.5, DeepSeek-V4-Pro, and GLM-5.1, reach only 30.00--45.67\%, a substantial drop from BrowseComp, while Korean LLMs released through Korea's Proprietary AI Foundation Model program obtain only 0.00--10.33\%. We further construct a 100-problem synthetic split using hard few-shot exemplars and failure-mode-targeted generation to exploit the asymmetry between solving and creating web browsing problems. On the adversarially filtered synthetic diagnostic split, the strongest model reaches only 26.00\%, and we report this split separately as a targeted stress test. We publicly release our data and code.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
