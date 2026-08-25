# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-363](./part-08.md)

---

### 301. [The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search](https://arxiv.org/abs/2608.23252)

**<font color=#1a73e8>作者：</font>** Peiyang Liu, Xi Wang, Di Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Retrieval-Augmented Generation (RAG) shifts toward diverse portfolio generation, it is stymied by two critical bottlenecks: flawed measurement of evidence utilization, and suboptimal context budget allocation. We resolve both sequentially.
To resolve measurement, we expose a pervasive ``diagnostic illusion'': standard relevance proxies fail catastrophically on hard negatives. We replace them with an efficient causal leave-one-out probe that accurately isolates generative reliance and formally calibrates the structural dilution of LLM attention.
To resolve allocation, we deploy this causal probe in a deconfounded factorial grid. We prove that the prevailing strategy of monolithic context widening is an architectural trap penalized by relevance decay. Instead, allocating compute iteratively across multiple sequential generations drives transformative portfolio recall gains of 16.7--20.5 absolute percentage points, scaling robustly up to 32B models.
Finally, we unify these solutions into a deployable closed-loop submodular scheduler. Augmented by an attribution-steered contrastive decoder to override LLM attention inertia, our architecture systematically forces fresh evidence integration. By dominating classical open-loop baselines, we establish sequential, feedback-driven orchestration as the definitive paradigm for generative search. Our code, data, and causal measurement instruments are available at this https URL.

---


### 302. [E2S-Pruner: Progressive Two-Stage Evidence Fusion for Visual Token Pruning in Vision-Language Models](https://arxiv.org/abs/2608.23253)

**<font color=#1a73e8>作者：</font>** Taoyu Qian, Qi Wang, Daqian Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models typically encode an image into hundreds of visual tokens, incurring substantial inference latency and GPU memory overhead. Existing pruning methods largely rely on attention scores and directly aggregate outputs across attention heads and network layers, making it difficult to characterize evidential uncertainty and conflict. We propose E2S-Pruner, a progressive two-stage evidence-fusion framework for visual token pruning that requires no auxiliary model, trainable parameters, or fine-tuning. In the first stage, E2S-Pruner treats each attention head as an independent evidence source, estimates its reliability from evidence clarity and inter-head consistency, and represents each visual token using three states: important, unimportant, and uncertain. In the second stage, Dempster--Shafer evidence theory is used to quantify inter-layer conflict and fuse complementary evidence from multiple network layers. We further introduce a spatial novelty constraint that promotes coverage of distinct image regions and prevents the retained tokens from concentrating in a few locally salient areas. On LLaVA-1.5-7B, E2S-Pruner retains 98.0%, 96.8%, and 90.6% of the aggregate performance when the average numbers of retained visual tokens are 192, 128, and 64, respectively, while improving throughput by 1.96x and 2.09x under the 128-token and 64-token settings. Experiments on Qwen2-VL-7B further demonstrate cross-model generalization. Code is available at this https URL.

---


### 303. [A Scalable Cross-Domain Event Extraction System via a Unified Generative Training Framework](https://arxiv.org/abs/2608.23261)

**<font color=#1a73e8>作者：</font>** Siting Liang, Omar Adjali, Omair Shahzad Bhatti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event extraction is fundamental to information extraction. Prior approaches often separate event detection and argument extraction or depend on dataset-specific designs, limiting scalability and cross-domain generalization. We propose a unified generative sequence-to-sequence framework that performs event extraction subtasks jointly and supports both pipeline and end-to-end configurations. We fine-tune pretrained language models on multiple event datasets across diverse domains, enabling a single model to retain domain-specific semantics while generalizing over large and evolving label spaces. We demonstrate these capabilities through a web-based application tailored for researchers and practitioners. The platform supports document upload, schema-aware event extraction, visualization of triggers and arguments, and comparison of different extraction configurations across domains.

---


### 304. [Automated Construction of FAIR Digital Object Knowledge Graphs from Flat Cultural Heritage Records](https://arxiv.org/abs/2608.23263)

**<font color=#1a73e8>作者：</font>** Zeyd Boukhers, Lingxiao Kong, Xenophon Zabulis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The FAIR Digital Object (FDO) framework mandates that metadata attribute values be expressed as persistent identifiers (PIDs) wherever possible, to produce a fully machine-actionable graph in which every reference is resolvable. The Europeana Data Model was designed long before the FDO specification, and it stores most metadata values as plain text. This serves human browsing well enough, but gives an automated agent nothing to follow across records or collections. We present a pipeline that transforms flat Europeana records into an FDO-compliant knowledge graph structured with CIDOC-CRM. Following the FDO specification, we model every heritage entity as a discrete FDO with its own PID, type, profile, and metadata layer. The core technical challenge is automating the FDO-prescribed distinction between values that must become PID references (resolvable entities) and those that may remain literals (terminal leaves such as notes, measurements, and dates). We address this with a large language model that classifies each metadata value, routes it to a controlled vocabulary (Getty AAT, Wikidata, VIAF, PeriodO), and links it to a shared entity FDO. We evaluate using 637 archaeological records from five Europeana providers, processing each with the LLM. The pipeline links 86% of metadata slots, resolving 58.5% of values Europeana had not already enriched. It also merges cross-lingual surface forms that byte-identical matching keeps apart, where 17 of 33 such merges are correct on manual review. Graph connectivity does not separate this from string matching; what distinguishes the FDO graph is that every node is typed and resolvable.

---


### 305. [Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance](https://arxiv.org/abs/2608.23264)

**<font color=#1a73e8>作者：</font>** Or Biton, Tomer Krichli, Itai Allouche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective first-person statements, and direct requests for assistance. We find that model performance degrades in the request-for-assistance-based form. Using Layer-wise Relevance Propagation (LRP), we trace this discrepancy to an attribution bias: the model places greater emphasis on benign task-framing tokens (e.g., "Can you help me...") than on tokens signaling the underlying unethical behavior (e.g., "without getting caught"), which we term cue-tokens. We hypothesize that this under-attribution contributes to harmful compliance. To test this, we introduce two LRP-guided decoding methods that steer generation toward trajectories more relevant to cue tokens. Empirical evaluations show that these interventions promote safer responses, supporting cue-token attribution's role in compliance failures.

---


### 306. [Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner](https://arxiv.org/abs/2608.23268)

**<font color=#1a73e8>作者：</font>** Jieke Wang, Tiancheng Shen, Yibo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frontier multimodal large language models (MLLMs) deliver impressive perception yet still falter on scientific and mathematical reasoning. Parameter-level adaptation is unavailable for closed-weight or on-device backbones, and stateless prompting forfeits any compounding benefit from problems already solved. We propose \textbf{DG-Mem}, a dual-grained agentic memory framework that augments a frozen MLLM with a non-parametric, externally stored memory built once from training-time rollouts and consulted read-only at test time. Motivated by the Complementary Learning Systems (CLS) account of human memory, DG-Mem factors its store into an instance-grounded exemplar memory and a category-level schema memory of IF-THEN rules, with a transient reflection store mediating their construction so that schemas are synthesized only from abstract reflections, never from exemplar text. Two design choices distinguish DG-Mem: an online concept categorizer that grows the category space incrementally during training rather than committing to a predefined taxonomy, and a Shapley context attribution procedure that decomposes correctness across the entire retrieved rule set and yields a per-rule utility that re-weights retrieval at test time. The pipeline introduces no gradient updates and is deployable on closed-weight or on-device backbones. Across MathVista, MMMU, and MMMU-Pro on four open-weight and proprietary backbones (Qwen3.5-27B, Qwen3.5-122B-A10B, GPT-5-Nano, Gemini-3-Flash), DG-Mem improves consistently over no-memory and competitive memory baselines.

---


### 307. [Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://arxiv.org/abs/2608.23283)

**<font color=#1a73e8>作者：</font>** Apodex Team, B. An, B. Li 等 71 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose language models can reason and synthesize knowledge, but complex work also requires sustained interaction with files, information sources, and executable code, together with state maintenance, failure recovery, and verifiable delivery. We call this \emph{working capability}: sustained, verifiable progress toward a real-world objective. Apodex 1.1 develops this capability along two complementary dimensions. \emph{Environment Scaling} expands the diversity and verifiability of executable file, search, and code environments, while \emph{Agentic Coordination Scaling} trains agents to decompose long-horizon tasks, delegate parallel work, integrate asynchronous results, and replan. A shared execution harness and AgentOS maintain task state and provenance across tools and agents, and training turns environment trajectories and coordination traces into reliable behavior. Across complex professional work, finance, scientific research, mathematics, coding, and search, Apodex 1.1 reaches the leading performance band despite using a substantially smaller model than many frontier systems. The 35B-parameter Apodex 1.1 Mini further retains strong working capability in a locally deployable form. These results ground agentic intelligence in useful, verifiable work completed over time and advance our goal of building a \emph{Heavy-Duty Solver} for ambitious, long-running tasks.

---


### 308. [Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction](https://arxiv.org/abs/2608.23296)

**<font color=#1a73e8>作者：</font>** Isaac  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned KV-cache eviction often faces a soft-to-hard mismatch: during training, differentiable gates typically attenuate token contributions, whereas inference saves memory only when KV entries are physically removed. We ask whether the attention substrate affects this soft-to-hard transition. Using GPT-2-scale Transformers trained on OpenWebText, we run a controlled $2\times2\times2$ comparison over attention type, learned gating, and positional encoding. Although sigmoid attention is worse as a dense language model, learned hard eviction changes the useful operating points: sigmoid-gated models delete KV entries with negligible PPL change relative to their own no-eviction references. Under a matched live-cache protocol on the same dense backbones, learned sigmoid gates obtain lower PPL than our H$_2$O and KeyDiff implementations, whereas softmax gates do not uniformly beat these post-hoc methods. The results suggest that attention normalization can substantially affect whether a training-time soft gate transfers cleanly to hard KV deletion.

---


### 309. [Grounding Free-Form Instructions for Fashion Complementary Image Generation](https://arxiv.org/abs/2608.23302)

**<font color=#1a73e8>作者：</font>** Matteo Attimonelli, Claudio Pomo, Alessandro De Bellis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion complementary image generation (CIG) aims to create garments that stylistically match a seed item based on user intent, making it a natural multimodal grounding problem where models must interpret language in visual context. Existing CIG benchmarks rely on rigid template prompts (e.g., "a photo of a skirt"), failing to reflect natural user queries and obscuring model behavior across levels of linguistic specificity. We introduce fashion complementary image generation with free-form instructions, a multimodal language-grounding setting where a model generates a compatible garment from a seed image and a natural-language instruction. To this end, we enrich three CIG benchmarks with low-, medium-, and high-specificity instructions generated by a vision-language model and validated by human annotators. We instantiate the task with StyleFlow, a Rectified Flow Matching model that jointly conditions on the seed image and instruction within a single multimodal transformer. Across image quality metrics, catalog-alignment analysis, ablations, and human evaluation, StyleFlow consistently produces instruction-aligned and stylistically coherent garments while reducing architectural complexity and inference cost relative to auxiliary-module approaches.

---


### 310. [FIDES: A Concordance Protocol for LLM-Generated Trading Strategies](https://arxiv.org/abs/2608.23308)

**<font color=#1a73e8>作者：</font>** Arther Tian, Alex Ding, Simon Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An LLM asked for a trading strategy returns three artifacts at once: a natural-language rationale, an executable implementation, and once run, a track record. Whether these are the same object is rarely checked. We present FIDES, a measurement protocol that treats them as three views to be reconciled rather than one deliverable to be graded. Through dual delivery, a single model call returns both a natural-language strategy with an explicit claimed edge and a self-contained strategy(df) function. FIDES executes the code in a sandbox against a lag-one out-of-sample backtest and scores three concordance gaps: say to do, do to real, and say to result.
On 8 liquid US ETFs across four models plus a two-stage elicitation arm, 40 strategies, 2023 to 2024 out-of-sample, three findings stand out. First, concordance does not predict profit: only 2 of 40 strategies beat buy-and-hold, and a plain sma(50,200) rule outperforms every model's mean Sharpe. Second, self-assessment is badly calibrated: 32 of 40 strategies claim to beat buy-and-hold and exactly one does. Third, swapping the language-code judge for a second model flips say to do on more than half of items. Injecting this http URL(-1) drops do to real by 0.33 on average, while our runtime future-information probe fired on neither clean nor injected code. We frame FIDES as a protocol for measurement fidelity, not a claim about market performance.

---


### 311. [Beyond the Stability-Exploration Dilemma: Environmental Regularization for LLM Policy Optimization](https://arxiv.org/abs/2608.23311)

**<font color=#1a73e8>作者：</font>** Xianlei Zhou, Xiangdi Meng, Yu He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Policy optimization (PO) for Large Language Models faces a stability--exploration trade-off, currently mediated by an action-side Policy-KL regularizer. This puts practitioners in a double bind: keeping Policy-KL constrains response behavior and consumes the action-side exploration budget, while dropping it leaves the optimization without an explicit drift control. We argue for an alternative that breaks the dilemma by moving regularization to the input side. As training progresses, the distribution over training queries induced by the current policy drifts unchecked from its pre-RL reference distribution.
Concretely, Environment-Regularized Policy Optimization (ERPO) introduces a Query-KL (QKL) term that bounds this query distribution shift, together with a dataset-static reference-derived per-query weight that biases each per-query update toward queries typical under the reference. The QKL gradient flows strictly through the query likelihood; the response score function used by policy-gradient estimators does not appear in the QKL term, so QKL exerts no direct gradient pressure on the response distribution---exploration is preserved. ERPO plugs into GRPO/PPO/REINFORCE-style pipelines without additional forward passes. On six mathematical reasoning benchmarks, ERPO replaces the standard Policy-KL regularizer while achieving effective control over query distribution drift, delivering stronger accuracy and substantially more stable behavior under high-temperature decoding and long-horizon this http URL source code are available at this https URL

---


### 312. [EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models](https://arxiv.org/abs/2608.23313)

**<font color=#1a73e8>作者：</font>** Xuetong Li, Gaofeng Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and visual evidence, and behavioral sensitivity to counterfactual changes in safety-critical evidence. EviSafeBench instantiates the framework as a controlled benchmark with 1,181 gold image-text scenarios and 2,452 targeted counterfactual variants across eight safety domains and eight risk-source types. Each scenario includes a gold safety decision, evidence annotations, a safe-response policy, and counterfactual interventions. The three-probe protocol queries models with natural-response, evidencereporting, and counterfactual-response prompts, then scores them using an evidence-aware judge. Across eleven evaluated VLMs, natural severity accuracy ranges from 27.6% to 52.8%, relaxed diagnostic consistency from 6.1% to 29.3%, and unsafe-to-safe counterfactual transition success from 30.4% to 58.4%. These gaps show that the evaluated VLMs are not reliably safe for the right multimodal reason and motivate evaluation beyond refusal counts.

---


### 313. [Agent-G$^2$: Gaussian Guidance for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.23318)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Yanrui Miao, Zhengxi Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hint-based reinforcement learning addresses reward sparsity in long-horizon agentic tasks by retaining a prefix of an expert trajectory before each rollout, letting the policy explore from a state closer to success. Its effectiveness hinges on the guidance depth: how much of the trajectory to keep. Existing methods treat this depth as a deterministic scalar. Scheduled approaches share one value across samples and ignore per-task heterogeneity; per-sample probing estimates it separately at the cost of extra rollouts. We find that useful guidance occupies a band of depths whose informativeness profile is approximately Gaussian around the band center, rather than concentrating at a single optimal point. We propose Agent-G$^2$, a Gaussian guidance framework that draws the depth per task from a Gaussian whose center and spread are estimated online from rollouts already collected for policy optimization, requiring no probe rollouts or learned depth predictor. The center combines a global baseline with per-cluster difficulty, and the spread tracks within-cluster variance. We evaluate Agent-G$^2$ on ALFWorld and WebShop on Qwen2.5-1.5B / 7B-Instruct. Agent-G$^2$ outperforms the strongest hint-based, hint-free, and Aux-RL baselines on ALFWorld by 2.3 / 3.9 / 7.4 points at under one-third the rollout cost of per-sample probing.

---


### 314. [IntentQA: Intent Question Answering in Videos by Cognitive Context Reasoning](https://arxiv.org/abs/2608.23330)

**<font color=#1a73e8>作者：</font>** Jiapeng Li, Ping Wei, Wenjuan Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding requires intelligent agents to transcend mere recognition of visual facts and comprehend the underlying intents behind human actions (often termed the "dark matter" of social intelligence). To bridge the gap between visual observation and intent reasoning, we introduce a novel task, IntentQA, and contribute a large-scale VideoQA dataset specifically tailored for this purpose. However, recognizing that standard metrics may overestimate capabilities due to dataset biases, we go beyond simple accuracy to rigorously evaluate model robustness. We augment the benchmark by generating five distinct contrast sets via Large Language Models (LLMs) and introducing a "Contrast Performance Decline" metric. We propose the X-CaVIR (eXplainable Context-aware Video Intent Reasoning) framework, which leverages three types of "Cognitive Context" to enhance video analysis: i) Situational Context via a cross-modal Video Query Language (VQL) module, ii) Contrastive Context via a Contrastive Learning module, and iii) Commonsense Context via a Commonsense Reasoning module. Crucially, to overcome the opacity of traditional black-box models, we refine the integration of LLMs within X-CaVIR by employing a transparent pipeline that synergizes video captions with VQA model outputs. This approach not only improves performance by effectively utilizing rich commonsense knowledge but also renders the reasoning process explicitly interpretable. Extensive experiments demonstrate the effectiveness of our components, the superiority of X-CaVIR over state-of-the-art baselines, and its stability against perturbations on the contrast sets.

---


### 315. [Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline](https://arxiv.org/abs/2608.23336)

**<font color=#1a73e8>作者：</font>** Eugenia Moris, José Ignacio Orlando  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing competitive deep learning baselines for medical imaging remains a highly iterative process requiring literature review, implementation, experimentation, and expert refinement. Existing automation approaches typically optimize isolated components, such as architecture search or hyperparameter tuning, rather than the complete baseline development process. We present an agentic AI Scientist workflow that combines literature-guided reasoning, automated code generation, and hypothesis-driven experimentation to generate competitive baseline models for medical imaging challenges. The framework is evaluated on four public benchmarks spanning segmentation, classification, and detection. Across all tasks, the Experimentation Pipeline consistently improves validation performance, achieving competitive leaderboard results, including 6th place on both PUMA tracks (15 teams) and 31st place on MILK10k (125 teams). On MIDOG25, the resulting model also demonstrates strong domain generalization across scanners, tumor types, and species. Using the same workflow across all challenges without task-specific redesign, we demonstrate that skill-based, literature-guided agentic workflows can substantially reduce the engineering effort required to develop competitive medical imaging baselines.

---


### 316. [The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning](https://arxiv.org/abs/2608.23338)

**<font color=#1a73e8>作者：</font>** Matthew Perlman, Atharva Nijasure, James Allan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LoRA fine-tuning is standard for adapting LLMs to reranking, but it remains unclear where in the network task-specific relevance behavior is learned and what attention-level changes accompany that learning. Through ablation and attention experiments, we identify where LoRA attention updates to RankLLaMA improve performance and whether those gains coincide with interpretable relevance-oriented attention patterns such as lexical matching, rarity sensitivity, and query-document interaction. We find that given LoRA fine-tuned MLPs throughout the network, restricting LoRA attention updates to a compact mid-network region is sufficient for recovering over half of the performance gained by applying LoRA to all attention layers, and that omitting attention fine-tuning in this region hurts performance more than elsewhere in the network. Additionally, we show that regions where applying LoRA affects performance the most overlap with regions where fine-tuning increased attention to axiomatic IR features. Rarity sensitivity, document-query interaction, and several compositional features are highly correlated with gains in ranking performance. Our results support an interpretable, correlational account of how relevance-oriented behavior emerges during LoRA fine-tuning and point toward improved strategies for adapting rerankers.

---


### 317. [FormuEvo: LLM-Guided Evolution for Discovering Solver-Efficient Mixed-Integer Programming Formulations](https://arxiv.org/abs/2608.23353)

**<font color=#1a73e8>作者：</font>** Haofeng Yuan, Jianing Peng, Jieyi Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixed-integer programming (MIP) lies at the core of operations research and industrial optimization. While large language models (LLMs) have recently shown promise in automated MIP modeling from natural language, they prioritize semantic correctness but overlook formulation strength, severely bottlenecking the efficiency of downstream solvers. We propose FormuEvo, an LLM-guided evolutionary framework for automated discovery of solver-efficient MIP formulations. FormuEvo frames MIP formulation design as evolutionary optimization over the symbolic space of MIP formulations, represented as executable modeling programs, by iteratively generating, evaluating, and selecting stronger candidates via LLM-driven crossover, mutation, and repair operations. To move beyond blind exploration, FormuEvo introduces a solver-informed diagnosis mechanism that exploits fine-grained solver statistics as verbal gradients for targeted refinement. Additionally, a structured memory abstracts prior experience into reusable modeling strategies, avoiding redundant exploration while enabling zero-shot transfer to unseen problems and bootstrapping smaller LLMs. Experiments across diverse linear and non-linear problems demonstrate that FormuEvo discovers formulations that significantly outperform both expert-designed formulations and existing LLM-based approaches, accelerating solvers by up to 5.5$\times$, with distilled knowledge transferring effectively across problems and model scales.

---


### 318. [The Geometry of Low-Resource Language Representations](https://arxiv.org/abs/2608.23358)

**<font color=#1a73e8>作者：</font>** Francois Meyer, Jan Buys  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance gap between low- and high-resource languages in LLMs is widely known, but it remains unclear which internal model factors drive these disparities. In this paper, we characterise this gap through the lens of representational geometry. Comparing the geometric properties of hidden representations across 30 languages reveals that LLM geometry is systematically related to language data availability. The most consistent effect is in final layers, where low-resource languages exhibit representational degeneration. To counter this, we investigate the effectiveness of regularisation terms to penalise degeneration during continued pretraining (CPT). Experiments monolingually adapting 9 base LLMs to 10 African languages show that geometric regularisation successfully reduces representational degeneration during CPT. For larger models, cosine similarity-based regularisation marginally improves performance over vanilla CPT, with more consistent gains on the most challenging tasks. We establish that the representational geometry of low- and high-resource languages in LLMs is measurably distinct, and that targeted geometric intervention is a viable strategy for improving CPT for low-resource languages.

---


### 319. [DF-MoE: Generalizable Deepfake Detection via Multimodal Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.23363)

**<font color=#1a73e8>作者：</font>** Vlad Hondru, Florinel Alin Croitoru, Iuliana Georgescu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual deepfake detection is an actively studied topic, where one of the main challenges is to develop detectors able to generalize across deepfake generation methods. We conjecture that overfitting can be mitigated by extracting multiple high-level cues from the available audio and visual modalities via pre-trained models. We therefore assemble a wide variety of pre-trained models to extract features that encode mouth movements, face parsing, facial expressions, head pose, gaze tracking, heart rate, audio emotion and speech activity. We further integrate both unimodal and multimodal cues via a Mixture-of-Experts (MoE) backbone to detect deepfakes. We perform in-domain and cross-domain experiments on five benchmarks for deepfake detection (MAVOS-DD, AVLips, PolyGlotFake, BioDeepAV, FakeAVCeleb) to compare our framework (DF-MoE) with state-of-the-art methods. Our results indicate that DF-MoE obtains superior deepfake detection results, surpassing all competing methods. We release our code at this https URL.

---


### 320. [Walking on the DARKSIDE](https://arxiv.org/abs/2608.23370)

**<font color=#1a73e8>作者：</font>** Aldo Gangemi, Emanuele Bottazzi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) recognise patterns but do not natively track the path of exclusions that a coherent discourse demands. When an input rests on a fabricated authority, a misapplied mechanism, or a surreptitious analogy, an unsteered LLM tends to engage with it as if it were grounded, and to reify the misstep into any structured output it generates. Logic-Augmented Generation (LAG) with POLANYI++, an LLM-steering method that uses heuristics, ontologies and problem solving methods for tacit knowledge extraction, produces an Extended Knowledge Graph (XKG) in OWL2, but inherits the same vulnerability: a sophisticated nonsensical input is reified into the graph alongside the legitimate triples, and is hardly detectable by automated reasoners since the XKG is generated jointly with the wrong assumptions. We introduce DARKSIDE, a coherence auditing method on top of POLANYI++. It formalises the trail as an explicit data structure of accumulated exclusions over discourse time, complemented by a warrant axis that classifies each named referent as Warranted, Unattested, Misattributed or Fabricated, with an escalation rule that pushes the DelegationRiskAssessment to UNSAFE when the fabricated rate is positive or the unsupported rate exceeds a threshold. We evaluate DARKSIDE as a steering layer over a Gemini 3 on BSBench, a 100-item adversarial corpus of sophisticated-sounding nonsense across software engineering, finance, healthcare, physics and law, with Claude Sonnet 4.6 as an independent judge. The empirical evidence supports an architectural claim: when an LLM forward pass is wrapped in an ontology-mediated negative-trail apparatus, the structural pattern-vs-path gap can be partially scaffolded. The XKG functions as the missing memory, and the warrant axis as an epistemic firewall.

---


### 321. [Modalities Should Talk to Each Other: Dual-Stream Multimodal Learning for Long-Horizon Influenza Forecasting](https://arxiv.org/abs/2608.23373)

**<font color=#1a73e8>作者：</font>** Seyed Mohammad Hossein Hashemi, Mohsen Hooshmand, Parvin Razzaghi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting long-range influenza-like illness (ILI) matters for public health readiness. Publicly available surveillance datasets typically pair numeric epidemiological signals with textual information that is noisy, loosely structured, only indirectly related to near-term trends, and often lagged relative to the numeric signal. Fusing the two therefore requires careful design. We propose Dual-Stream Attention (DSA), a multimodal deep learning framework that forecasts 12-week-ahead ILI activity from a 36-week multimodal history by letting the numerical and textual streams condition each other. Using the Time-MMD health-domain dataset, DSA separately encodes the two modalities with a Transformer-based numerical encoder and a domain-adapted headline encoder, then couples them through a bidirectional Cross-Modal Attention (CMA) mechanism: the text (news headlines) conditions the interpretation of the numeric signal and vice versa. The CMA output then passes to a causal temporal model for forecasting. Evaluated across ten random seeds, DSA achieves a median test MSE of 0.416, versus 0.668, 0.607, and 0.851 for iTransformer, TaTS, and GPT4MTS, corresponding to mean-error reductions of 54.95%, 37.29%, and 67.23%, with paired Cohen's d of 0.555, 0.337, and 0.345, respectively, and ranks first in 100% of bootstrap draws. It also has substantially lower worst-window error than all baselines. On an external-geography dataset, DSA again ranks first among nine evaluated baselines. Ablations show the advantage does not depend on text-encoder choice or language-model fine-tuning, and that bidirectional attention outperforms either direction alone. Finally, perturbation-based faithfulness analysis shows the learned CMA is functionally informative under targeted masking, with a stronger effect in the text-to-numerical direction.

---


### 322. [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](https://arxiv.org/abs/2608.23375)

**<font color=#1a73e8>作者：</font>** Nikita Kezins  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gumbel-based inference verification bounds LLM weight exfiltration by only forgiving token choices that plausibly arise from honest GPU nondeterminism, reporting a >200x slowdown for a steganographic adversary under benign prompt traffic. This bound assumes a passive attacker; we show it degrades sharply against an adversary who instead controls the prompt distribution. Because the verifier's admissible-token-set size is driven by the model's own output entropy, prompts engineered to break grammatical and sub-word structure -- rather than benign conversational traffic -- widen that set and open a materially larger covert channel. Across six instruction-tuned models spanning 1B to 32B parameters and three random seeds, our strongest attack (character- and script-level disruption) roughly doubles bits leaked per token relative to benign prompts, cutting the slowdown factor to 60x - 118x. These results indicate that static, benign-traffic-calibrated thresholds are insufficient for this defense, and that jitter-forgiveness thresholds should instead be calibrated dynamically against local token entropy.

---


### 323. [Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data](https://arxiv.org/abs/2608.23391)

**<font color=#1a73e8>作者：</font>** Yifei Song, Kun Efimov-Zhang, Claire Gardent  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured data exists in many forms (tables, knowledge graphs, charts, and time series), and converting it into text may involve different generation tasks. However, most prior work on data-to-text (D2T) generation has focused on specific tasks and datasets, relying either on task-specific training data or on the zero-shot capabilities of large language models. We study cross-domain D2T generation in a setting where neither in-domain training text nor test references are available, and where domains, generation goals, and input structures vary substantially. We compare data-driven knowledge distillation (DDKD) against zero-shot inference and fine-tuning on out-of-domain D2T data, and introduce structure-preserving augmentation via structural subsampling and perturbation. Experiments on five benchmarks show that, at constant model size (1.7B parameters), DDKD consistently outperforms both fine-tuning and zero-shot inference. Moreover, the resulting small models outperform a much larger finetuned model on two of the five domains, achieving comparable performance on the remaining three. We further construct QUINTD-5, a fivefold extension of QUINTD-1, and show that simply scaling real target-domain inputs yields only modest gains, whereas our augmentation strategy remains more effective and more cost-efficient for cross-domain distillation.

---


### 324. [Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep](https://arxiv.org/abs/2608.23395)

**<font color=#1a73e8>作者：</font>** Pedro Santos  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent LLM-agent systems make conflicting design bets: decompose work across many narrow agents, or use one strong tool-using agent. This pilot studies that choice on bounded cross-border VAT determination with reverse charge, where every case has an oracle label and each intermediate decision is independently scoreable. We hold the activity surface fixed (subtasks, tools, I/O schemas, validation checks, orchestrator, base model, and merge policy) and vary only the assignment of subtasks to workers across four orchestrated configurations, from one wide worker to five narrow ones, against S0, a tuned no-orchestrator single agent, with a deterministic rule engine as oracle. The program spans 4,400 runs: a 40-case, five-repeat main sweep, matched-token arms separating prompt-budget from agent-count effects, and three failure-injection arms, all judged against pre-registered falsification criteria. The two intermediate configurations lead on accuracy (0.830, against endpoints at 0.720 and 0.770) but miss the pre-stated bar against the fine endpoint, so the intermediate-optimum hypothesis remains unsupported at pilot scale. The single agent does not Pareto-dominate the orchestrated set. The matched-token criterion fires: the budget-matched single agent lands 6.5 points below the leader, but the interval includes zero, so any advantage is consistent with a prompt-budget explanation. Under injection, availability faults are absorbed at every granularity, with wide-scope restart over-recovering its baseline by +0.160, while one schema-conforming hallucinated record degrades every configuration and inverts the ordering, hitting fragmented configurations hardest. The contribution is a bounded, preregistered pilot heuristic for right-sizing decomposition (place one partition boundary at the dependency-layer midpoint), released with oracle, dataset, harness, raw traces, and analysis pipeline.

---


### 325. [MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical Interaction](https://arxiv.org/abs/2608.23397)

**<font color=#1a73e8>作者：</font>** Ruoyu Wu, Shenfu Xie, Yinqian Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive clinical agents must gather decisive evidence and convert it into grounded actions under partial observability. A correct final diagnosis alone does not show that an agent respected evidence and care-process constraints. We introduce MediSkill-Evo, a clinical agent that evolves governed process knowledge without backbone fine-tuning. It separates experience into four typed banks for clinical skills, process rules, symbolic schemas, and measurement procedures. Provenance, support, replay, and controller-defined safety checks govern publication to a frozen test-time snapshot. A Process-Constrained Preference Harness binds evidence to its source, rejects controller-invalid candidates, and ranks actions with a safety-prioritized Clinical Process Critic. We evaluate complete agent systems across two backbone endpoints and six controlled stress dimensions under the same Doctor-turn limit. On 300 held-out Qwen encounters, MediSkill-Evo improves diagnosis accuracy from 61.33 percent to 69.00 percent and treatment-intent coverage from 33.62 percent to 66.44 percent, while reducing automatically scored critical failures from 31.00 percent to 16.33 percent relative to AgentClinic. On 180 hard-isolation conditions derived from 30 cases, target recovery reaches 93.61 percent under patient-behavior pressure, 100.00 percent for temporal evidence, and 92.22 percent for triage red flags. An exploratory 100-case MedSAM comparison evaluates request-gated tool-interface feasibility. These results provide descriptive end-to-end evidence for the complete system on fixed evaluation suites, not causal evidence for an individual bank or clinical validation of the automatic judge.

---


### 326. [STONIC: A Layered Measurement Contract for LLM Value Profiling](https://arxiv.org/abs/2608.23411)

**<font color=#1a73e8>作者：</font>** Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM value studies often merge questionnaire ratings, pairwise choices, and values inferred from generated text into one profile. That merge assumes that the three observations describe the same stable preference. STONIC tests this assumption on 5,144 situations from four banks and 35 fixed model configurations. It compares responses rated in isolation, choices made under counterbalanced conflict, spontaneous answers, and later choices between a model's own answer and authored alternatives. 10 of 17 configurations with usable behavioral data preserve the endorsement-choice relation across banks. Every one of the 17 eligible configurations prefers its own earlier answer (median effect 0.790), although option position changes the choice rate in every eligible configuration. Profile shape transfers most strongly from ratings to conflict choices and weakens for spontaneous text. Three-way annotation of 200 L3 responses provides a task-local check of the semantic audit: FULCRA agrees most closely with the human majority, while DeBERTa retains useful rank information after calibration. Hidden states encode the completed decision more clearly than the prompt alone. Thus the models show reproducible behavioral continuity, but the evidence does not support one scorer-independent value identity across interfaces.

---


### 327. [SkillAlchemy: Open-World Agent Skill Creation](https://arxiv.org/abs/2608.23417)

**<font color=#1a73e8>作者：</font>** Hengjun Wang, Shuyue Wei, Boyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are reusable procedural artifacts that extend language agents with specialized workflows, tool conventions, and domain behaviors at inference time. However, creating reliable skills still depends largely on human authorship, model priors, or execution traces. These sources are often unavailable for unfamiliar tasks, suggesting the need to create skills from open-world materials. In this paper, we study open-world skill creation: given an underspecified skill brief and a source-access specification, a creator must discover behavior-relevant requirements omitted by the brief and determine how broadly each source-derived procedure is justified. We propose SkillAlchemy, an admission-centered framework for source-grounded skill creation. SkillAlchemy identifies implicit requirements through contrastive evidence, admits candidate procedures based on evidence-supported scope, and compiles the admitted content into a grammar-guided skill package. Extensive experiments across 87 SkillsBench v1.1 tasks demonstrate that SkillAlchemy improves pass rate over no-skill execution by 19.9 percentage points and the strongest automated baseline by 8.6 percentage points, while achieving performance comparable to human-curated skills.

---


### 328. [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](https://arxiv.org/abs/2608.23421)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis of the field remains absent. This study presents a large-scale bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from six collections. We employ BERTopic for topic modeling, regression analysis to identify citation predictors, social network analysis for co-authorship structures, and geographic mapping. Our findings show a significant publication surge after 2020, driven by transformer models and LLMs. Topic modeling identifies 19 substantive themes, the largest centered on text, speech, translation, and recognition. Citation analysis reveals a positive correlation between paper age and citations (r = 0.245, p < 0.001); regression shows that indexing in OpenAlex or Semantic Scholar and institutional affiliation are associated with higher citation counts. Saudi Arabia, the United States, and Egypt lead in research output. A task-dialect gap matrix identifies critical understudied areas, including summarization for Maghrebi, Iraqi, and Sudanese dialects. The largest topic has the highest H-index (87), followed by sentiment analysis (54). Our quantitative approach complements existing qualitative surveys and offers recommendations to prioritize under-resourced dialects and develop culturally aligned benchmarks for Arabic NLP.

---


### 329. [Towards Comprehensive Basketball Understanding](https://arxiv.org/abs/2608.23435)

**<font color=#1a73e8>作者：</font>** Yirong Hu, Jiayuan Rao, Yu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding a basketball game requires recognizing events, localizing actions, identifying players, and relating these to structured game knowledge. Existing benchmarks primarily evaluate these abilities one at a time, leaving the interactions among these abilities under-explored. We introduce BasketballBench, a multimodal benchmark comprising 7,980 questions across ten tasks in text, image, and video. It is built from the 2025-2026 NBA season and includes official playby-play, rosters and profiles for 530 active players, and 2,501 possession-level broadcast clips. We further propose BasketballSkills, an agent that composes eight basketball-specific perception and retrieval tools under four reusable skills that specify tool order, evidence bindings, and stopping conditions. Experiments show that current MLLMs struggle particularly on questions requiring the integration of multiple capabilities, whereas BasketballSkills outperforms them, highlighting the effectiveness of explicitly composing domain-specific capabilities for comprehensive basketball understanding.

---


### 330. [How Useful are LLMs for Grammar Engineering? Cantonese ParGram Resources and Controlled Experimental Evaluation with English Baselines](https://arxiv.org/abs/2608.23448)

**<font color=#1a73e8>作者：</font>** Chit-Fung Lam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents new Cantonese ParGram resources and evaluates LLMs for knowledge-driven grammar engineering within a controlled experimental paradigm. Using Cantonese ParGram resources as gold standards, with corresponding English baselines, we investigate whether OpenAI's gpt-oss-120b and GPT-5.4 can generate machine-processable grammars from sentences and target formal structures under systematically varied prompting conditions. GPT-5.4 outperformed gpt-oss-120b, while grammars generated from target formal structures generally outperformed those generated from sentences. Although both models could generate locally plausible phrase-structure rules, lexical entries, and templates, they often struggled to coordinate interacting formal constraints, especially in multi-construction settings. The results characterize both the capabilities and limitations of current LLMs for potential integration into AI-assisted expert workflows: LLMs may support intermediate stages of grammar development, but human linguistic expertise remains central to analysis, validation, and refinement. The study also contributes new Cantonese symbolic grammatical resources.

---


### 331. [ProxyFormer: A Dual-Stream Proxy Architecture for Ultra-Long Context and High-Resolution Generation](https://arxiv.org/abs/2608.23463)

**<font color=#1a73e8>作者：</font>** Zhongpan Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic growth of attention computation and key-value (KV) cache with respect to sequence length is a central bottleneck for ultra-long-context language models and high-resolution generative models. We propose ProxyFormer, a general dual-stream architecture built upon proxy tokens. In each layer, fine-grained local features are compressed bottom-up into a small set of proxy states; expensive global interactions are performed only in the compressed proxy space; the globally contextualized proxies are then decompressed and injected top-down back into the local stream. Because the local stream persists across layers, fine-grained information that is not captured by one compression step remains accessible for later refinement, alleviating the irreversible information loss of conventional one-shot compression. We further introduce factorized multi-level compression/decompression, layer-wise dynamic compression ratios, asymmetric dual embeddings, and a proxy-only KV-cache inference scheme. On a 16GB GPU with batch size 1, a standard decoder-only model can train sequences of only about 20K tokens, whereas ProxyFormer with a compression ratio of 64 extends the trainable sequence length to about 0.7M. A model trained with a 64K window retains 92%-95% retrieval accuracy on a multi-needle retrieval task with 1,048,576 tokens, and a model trained with an 8K window exceeds 94% accuracy when extrapolated to 256K tokens. Preliminary image-generation experiments demonstrate the feasibility of ProxyFormer for both pixel-space and latent-space flow matching.

---


### 332. [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](https://arxiv.org/abs/2608.23471)

**<font color=#1a73e8>作者：</font>** Hanling Tian, Gengyu Zhang, Zeyang Sha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a retriever-agnostic anchor and an adversarial command. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

---


### 333. [What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](https://arxiv.org/abs/2608.23474)

**<font color=#1a73e8>作者：</font>** Marek Hradil, Danae Sánchez Villegas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate temporal grounding as an anomaly detection problem, providing a simple and controlled evaluation that directly tests sensitivity to temporal consistency. We introduce TimeCatch, where temporal anomalies are created by swapping consecutive frames and frame-level anomalies by replacing a frame with Gaussian noise. Models are evaluated on anomaly detection and localization tasks across four synthetic and real-world datasets, alongside a human study. Our evaluation reveals a substantial gap between frame-level and temporal anomaly detection. While VLMs consistently detect frame-level anomalies and often localize them accurately, they perform near chance on temporal anomaly detection and only modestly above chance on localization. Humans, in contrast, achieve near-ceiling performance on both tasks. Additional analyses across model scales, prompting strategies, sequence lengths, and visual similarity suggest that these failures cannot be explained solely by limitations in perception or model capacity. Together, these findings indicate that current VLMs can identify anomalies within individual frames but struggle to integrate information across frames to reason about temporal consistency. TimeCatch provides a controlled benchmark for evaluating temporal grounding in vision-language models.

---


### 334. [StrategyBench: Evaluating Explicit Strategy Induction in Large Language Models](https://arxiv.org/abs/2608.23475)

**<font color=#1a73e8>作者：</font>** Jinghan Tan, Yuanzheng Wang, Lu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly used in data-scarce and evolving task scenarios, few-shot in-context learning (ICL) has become a key paradigm for task adaptation. However, direct ICL often uses a small set of examples without explicitly abstracting task rules, making it sensitive to example construction. In contrast, human learners often reduce such sensitivity by first summarizing task rules from examples and then applying them to new instances. To evaluate this ability, we propose StrategyBench, which selects strategy-inducible tasks from BIG-Bench, constructs reference strategies, and defines evaluation metrics along two dimensions: strategy quality and downstream utility. We further analyze strategy induction from three perspectives: task variation, model configuration, and adaptation setting, covering category-wise differences, generator-executor choices, demonstration design, and SFT-based adaptation. Experiments show that explicit strategy utility differs substantially across task categories and depends on both strategy generation and execution conditions. The benchmark is released at: this https URL.

---


### 335. [Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational Music Recommendation](https://arxiv.org/abs/2608.23484)

**<font color=#1a73e8>作者：</font>** Naman Garg, Sarika Jain, George Fazekas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Team Semiintelligencn's solution for the ACM RecSys 2026 TalkPlayData Challenge, addressing conversational music recommendation through a multi-modal and personalized conversational recommender system. Our submitted system employs a three-stage pipeline: (1) multi-modal retrieval constructing decay-weighted centroids across seven dense embedding spaces - track- and user-level CF-BPR, Qwen3 (metadata, lyrics, attributes), CLAP audio, and SigLIP visual - supplemented by BM25 lexical retrieval and an artist substring-match signal, all fused via weighted Reciprocal Rank Fusion (RRF) with optimized signal weights; (2) lightweight reranking (history filtering, popularity smoothing, and catalog diversity penalization); and (3) persona-diversified response generation using GPT-4o-mini. Beyond this submitted configuration, we report development-time experiments with additional components - constrained LLM-guided artist injection, album continuation signals, XGBoost LambdaMART, and a superior GPT-4.1 response prompt - that were not deployed to Blind B due to cost and complexity constraints. We optimize RRF weights on a 500-session development split via differential evolution, improving MRR by +19.5%. On Blind A, we observe that unconstrained LLM-guided injection across 54 sessions causes catastrophic nDCG regression (-18.9%), while conservative injection on only 9 sessions yields the best observed Blind A nDCG - a finding we present as a Blind A observation warranting further validation. The submitted system achieves a Blind B composite score of 0.3213.

---


### 336. [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning](https://arxiv.org/abs/2608.23493)

**<font color=#1a73e8>作者：</font>** Jialong Liu, Yuling Shi, Ning Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-reflection is a powerful mechanism for credit assignment in human learning, converting sparse outcome feedback into actionable guidance. However, its potential for post-training Large Language Models (LLMs) remains underexplored. We propose Self-Reflective Policy Optimization (SRPO), a framework that internalizes this capability. SRPO enables LLMs to analyze their own completed trajectories, synthesize errors into concise "reflection patches," and use reflection-conditioned teacher scores on student on-policy rollouts as dense token-level training signals. This process effectively transforms sparse terminal supervision into dense, token-level learning signals without requiring external critics, separate reward models, or larger teacher models. We demonstrate that SRPO achieves state-of-the-art performance across mathematical reasoning and long-horizon agentic benchmarks with exceptional data efficiency. Using a Qwen3-8B base model, SRPO attains 73.3% on AIME'24 using only 8% (0.08x) of the training FLOPs required by scaled supervised fine-tuning, while significantly improving success rates on WebShop (64.7%), ALFWorld (76.8%), and SWE-Bench-Lite (31.2%). Code is available at this https URL

---


### 337. [Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](https://arxiv.org/abs/2608.23497)

**<font color=#1a73e8>作者：</font>** Yipeng Zhao, Qishun Yang, Shenzhe Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying this entanglement or propose a training-time fix. We provide both: a representation-space analysis of RIM and the Safety-Direction Penalty (SDP), which penalizes movement along a learned safety direction during reasoning fine-tuning. The analysis extracts two activation-space directions, one encoding reasoning ability and the other safety behavior. These directions are coupled: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. CKA distance ratios and probes locate the safety-decision layers where this shift is most relevant. These findings guide the design of SDP: the coupling motivates penalizing displacement along the safety direction, and the layer localization sets the initial scope. When the initial scope leaves compensatory shifts beyond the penalized layers, the same diagnostics guide iterative expansion. On Qwen2.5-3B and 7B, SDP restores safety while preserving benchmark reasoning performance.

---


### 338. [Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based Person Anomaly Search](https://arxiv.org/abs/2608.23503)

**<font color=#1a73e8>作者：</font>** Thanh-Khoi Nguyen, Thanh-Nhan Vo, Trong-Thuan Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person anomaly search requires distinguishing individuals based on fine-grained, context-dependent behaviors rather than mere appearance. Existing methods struggle to capture these context-conditioned actions, frequently relying on isolated skeletal geometry, discarding raw query details during reformulation, or utilizing absolute pointwise scoring for multimodal verification. To address these limitations, we propose \textbf{ActPair}, a unified three-stage coarse-to-fine framework that combines action-aligned retrieval with pairwise multimodal reranking to bridge the pose-semantic gap. First, we fine-tune a vision-language model (VLM) with an action-aligned multi-task objective that encourages the representations to encode action-discriminative semantics. Second, we perform parallel late-fusion retrieval using the original query and a large language model (LLM)-generated context-grounded rewrite, retaining complementary details from both semantic views. Finally, we propose an efficient off-the-shelf reranking module that leverages a pivot-promote algorithm to perform direct pairwise visual comparisons, mitigating residual spatial and compositional ambiguities without the prohibitive inference costs of exhaustive evaluation. Extensive experiments demonstrate that our framework achieves the best results among the compared methods on the Pedestrian Anomaly Behavior (PAB) public test and transfers effectively to an unseen, non-anomaly-specific dataset.

---


### 339. [When Names Cross Scripts: A Source-Grounded Benchmark for Historical Entity Reconciliation in the Mongol World](https://arxiv.org/abs/2608.23507)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Zeyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical people may appear under different languages, scripts, and transcription traditions, while distinct individuals may share highly similar or even identical names. This makes historical identity reconciliation more than a problem of string matching or transliteration. We introduce MHER, a provenance-controlled benchmark for pairwise reconciliation of person-name attestations from the Mongol world. MHER contains a balanced 396-pair Name-only core over 84 primary historical persons and a stricter 160-pair Source-grounded subset constructed from mention-by-source evidence, with entity-disjoint development and test splits.
Across five generative systems, correctly Source-grounded evidence improves paired TEST accuracy by 12.96 to 94.44 percentage points relative to Name-only input. On five identical-surface different-person cases, all models fail under names alone (0/25 model-item decisions), whereas Source-grounded evidence yields 24/25 correct resolutions, with the remaining output an abstention. Context-only ablations show that historical descriptions often carry substantial identity information, while explicitly signaled misgrounding controls produce substantially lower performance. We also find that names are not uniformly beneficial: for Qwen3-8B, restoring surface forms converts ten otherwise correct Context-only distinctions into false identity merges.
These results show that historical entity reconciliation depends not only on surface correspondence, but on whether identity judgments respond appropriately to provenance-controlled historical evidence. MHER therefore provides a controlled framework for studying evidence use, abstention, and failure modes in historical NLP.

---


### 340. [Investigating Relational Reasoning in VLMs](https://arxiv.org/abs/2608.23518)

**<font color=#1a73e8>作者：</font>** Adhithya Laxman Ravi Shankar Geetha, Aulia Kharis Rakhmasari, Haleema Ramzan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) achieve strong performance in visual reasoning tasks, but it remains unclear whether they understand visual relations, or simply employ shortcuts such as language cues or priors. To investigate this, we use the Qwen3-VL-4B (Bai et al., 2025), a modern VLM, to decode how visual information is encoded across depths. For this, we propose a synthetic dataset of simple geometric shapes for controlled analysis, along with queries crafted to precisely test language cues. Furthermore, the dataset is modified to test causal reliance on visual evidence. Our results show that current VLMs combine genuine visual reasoning with shortcut strategies primarily rooted in language cues.

---


### 341. [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541)

**<font color=#1a73e8>作者：</font>** Summer Eunhyung Ann, Haokun Liu, Chenhao Tan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Does multi-agent LLM interaction help or hurt? Some work reports gains from debate (Du et al., 2024), critique loops (Chen et al., 2025), and mixture-of-agents synthesis (Wang et al., 2025), while other work finds that interaction adds cost without improving quality under equal budgets (Tran & Kiela, 2026; Xu et al., 2026; Jarrett et al., 2025), or that independent sampling already captures multi-agent gains (Li et al., 2024). We argue this contradiction partly reflects a missing distinction, because not all multi-agent communication is equal. Different model families find structurally different solutions, but when agents read each other's complete outputs, their proposals converge within one round, erasing the diversity that motivates using multiple models. We call this the interaction tax. We test 11 verifier-scored optimization tasks under matched budgets and find that full-solution interaction is a weak default. Independent proposal generation avoids this collapse. Full-solution interaction mainly makes agents stay close to the first solution they see instead of trying different approaches, and critique helps only if the violated rule is easy for the LLM to find and fix. These results suggest that multi-agent performance depends less on the number of agents than on the information they exchange, and interaction helps only when agents share the right information at the right time.

---


### 342. [When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls](https://arxiv.org/abs/2608.23550)

**<font color=#1a73e8>作者：</font>** Ting Yan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this http URL, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public this http URL files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers or each other's labels. Depending on how closely a control had to match the written rule, only about 4-16% of the retrieved security rules had a matching built-in control. Under the strictest standard the estimate was 4.4% (95% CI: 2.6-6.7%), and the two annotators agreed closely on which rules had a match. A manual review of complete files found that our extraction method captured 66.3% of eligible security rules; the reported rates therefore apply to the rules it captured. This is a usable security problem: this http URL is a write-only channel. A developer writes a security rule but gets no feedback on whether a control will enforce it. The same plain-text form hides two kinds of rule: those a permission rule, mode, or sandbox can enforce, and those left to the model to interpret.

---


### 343. [ConvergeFlow: Language Flow with Provable Convergence to Token Embeddings](https://arxiv.org/abs/2608.23551)

**<font color=#1a73e8>作者：</font>** Na Li, Yuchen Jiao, Changxiao Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in continuous diffusion and flow-based language models (LMs) have achieved performance competitive with discrete LMs. However, existing continuous frameworks still rely on decoders supervised with cross entropy (CE) because the flow trajectories are not guaranteed to terminate at valid token embeddings. Motivated by this limitation, we introduce \textbf{ConvergeFlow}, an embedding-space flow-based LM, which constrains the data predictor to the convex hull of token embeddings and trains it solely with the mean squared error objective induced by flow matching. Under suitable regularity conditions, we prove that the resulting flow converges to valid token embeddings despite errors in the data predictor, enabling direct token prediction without a CE-supervised decoder. We further develop three sampling mechanisms for controlling the trade-off between the generative perplexity and entropy. Experiments on OpenWebText demonstrate that ConvergeFlow achieves performance competitive with existing continuous and discrete diffusion LMs. These findings demonstrate the potential of the flow-based paradigm for language modeling. Our code is available at this https URL.

---


### 344. [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552)

**<font color=#1a73e8>作者：</font>** Seth Karten, Alex L. Zhang, Kevin Thomas 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are sequential processors, but long-horizon agency requires external information and computation beyond model weights and active context. Prime Agent is an open-source harness for long-horizon evaluation and coding-agent workflows. A persistent IPython REPL follows the Recursive Language Model abstraction for programmatic context processing and test-time compute, while Continual Harness preserves histories, memories, skills, prompts, and subagent specifications across trajectories. Recursive subagents coordinate through direct agent-to-agent communication, and the Agents View lets humans inspect and manage daemon-backed sessions. Prime Agent standardizes execution, recovery, verification, and resource accounting while leaving strategy construction to the model. This low-friction, expressive membrane prevents harness failures from becoming model failures and pushes measurement toward the model's true maximal underlying capability. Prime Agent raises ARC-AGI-3 RHAE Best@1 from 30% to 95.5% and matches or exceeds native and popular harnesses across long-context coding, GPU-kernel generation, emulator construction, and autonomous nanoGPT speedruns. On Factorio, we find refinement allows for continuous technology progression and dedicated subagents enable parallelized work. Code is available at this https URL.

---


### 345. [EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings](https://arxiv.org/abs/2608.23563)

**<font color=#1a73e8>作者：</font>** Md Thamed Bin Zaman Chowdhury, Moazzem Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety expertise into a compact vision-language model for scalable visual road safety auditing. The key innovation is a quantified expert-grounding stage in which the teacher vision-language model is calibrated against authoritative field audits. Large-scale annotation is permitted only after the teacher reaches substantial agreement with expert risk assessments (Cohen's kappa = 0.74). The calibrated teacher then generates structured supervision that is distilled into an 8-billion-parameter student vision-language model using Low-Rank Adaptation and a single leakage-free prompt. We also introduce Bangladesh Road Safety Audit (BD-ARSA), the first open, expert-grounded Bangladeshi visual road safety audit dataset containing 21,947 image-audit records with near-national coverage, and Expert-Grounded Road Safety Auditor (EG-ARSA), the first vision-language model developed specifically for this task. Experimental results show that grounded fine-tuning substantially improves ordinal risk assessment over the zero-shot baseline, while blind expert evaluation demonstrates that the compact student outperforms both its 31 billion-parameter teacher and Gemini-2.5-Flash. These findings demonstrate that EGD provides an effective and scalable engineering solution for proactive road safety auditing in resource-constrained environments.

---


### 346. [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564)

**<font color=#1a73e8>作者：</font>** Deyao Hong, Yizhe Chi, Wenyi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern software systems accumulate technical debt over decades of development, which makes migration expensive and largely manual. As coding agents become increasingly capable at bug fixing, can they autonomously perform such migrations? Existing benchmarks cannot answer this question because they evaluate only behavioural correctness, not whether the migration actually occurred. This leads an easy hack: agents copy the original implementation to make tests pass. We call this Blindness. To address this problem, we introduce SWE Refactor Bench, a benchmark comprising 20 whole-repository migrations, covering 4 kinds of technical debt. A three-stage evaluation protocol measures both migration completeness and behavioural correctness. (1) Migration Audit verifies that the migration occurred. (2) Behavioural Tests measure correctness with a fixed test suite. (3) Agentic Verification uses 6 independent coding agents to generate targeted tests for hidden behavioural differences. Across 520 runs from 8 frontier models and 26 model-effort configurations, only 28 of 520 runs ($5.4\%$) pass all three stages, 13 of the 20 tasks receive no accepted solution, and the best model (claude-opus-5) scores $47.0/100$. Migration completeness and behavioural correctness are distinct abilities: a few runs preserve behaviour by skipping the migration and are stopped at Migration Audit; most attempt it and break behaviour, and are stopped at Behavioural Tests. Agents cannot deliver a perfect migration: among the 340 runs that pass Migration Audit, $58\%$ reach $99\%$ of the fixed checks, yet only $26\%$ reach $100\%$. Agent capability differs across migration categories: agents score $31.4$ on build toolchain rewrites but only $5.6$ on language rewrites. Together, these findings position SWE Refactor Bench as a rigorous testbed for developing coding agents for reliable whole-repository migrations.

---


### 347. [How to Train a Critic Stably and Efficiently](https://arxiv.org/abs/2608.23566)

**<font color=#1a73e8>作者：</font>** Penghui Qi, Xiangxin Zhou, Wee Sun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop \textbf{Best-Practice Critic Optimization (BPCO)}, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormalized policy advantages, and length-adaptive generalized advantage estimation. Because the critic is used only during training, BPCO can also condition it on reward-defining information, such as a reference answer or grading rubric, that is hidden from the policy. Controlled experiments isolate the effect of each design choice. Across mathematical reasoning tasks with models ranging from 1.5B parameters to 30B-A3B mixtures of experts, BPCO improves a strong critic-based baseline consistently, and matches or exceeds a group-based baseline while sampling one response per prompt. The same recipe also improves learning with rubric-based rewards. These results show that a carefully designed critic provides a reliable alternative to group-relative advantage estimation. Code is available at this https URL

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 348. [Beyond Two Bytes per Letter: Tokenization Overhead in Cyrillic AI Systems](https://arxiv.org/abs/2608.21384)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ivan Dobrovolskyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern multilingual tokenizers often fragment Ukrainian and other underrepresented Cyrillic-script languages more heavily than English, creating disparities in cost and context capacity. We quantify this overhead across nine production tokenizers and five languages with standardized Cyrillic and Latin representations, covering 8.37 million word forms. On a corpus benchmark, Ukrainian shows 68-121% token overhead on modern tokenizers and 220% on the older cl100k, measured through full-text fertility on the BrUK and Brown corpora. Overhead is negatively associated with Cyrillic vocabulary allocation in the subset with independently verified English baselines, although the association is not statistically significant (Spearman rho = -0.536, p = 0.215, n = 7). We evaluate two mitigation strategies. LLMLingua-2 reduces Ukrainian input length by 47-49% on an e-commerce RAG benchmark of 1,536 products and 145 queries, with no compression-induced value losses among 80 retrievable cases. A balanced byte-level BPE tokenizer trained with a 200K vocabulary cap, converging at 158,184 actual entries, reduces the held-out UK/EN ratio from 2.22x to 1.30x. Romanization increases Ukrainian token counts by 2-19% on most tokenizers. Across the five languages, tokenization efficiency favors the script more prevalent in web data. These findings indicate that training data allocation contributes to Cyrillic tokenization overhead and that mitigation is possible at both inference and tokenizer-design stages.

---


### 349. [Aligning Human Sense: Calibrated Distributional Reward Learning for Video Generation](https://arxiv.org/abs/2608.21425)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nai-Xin Zhai, Weihua Cheng, Dexu Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation is central to AI-powered content creation. Aligning generated videos with human preferences is a key criterion for evaluating generation quality. Despite significant progress in visual quality, three key challenges remain. First, the reliability of reward signals is constrained by the quality of human preference data, which is often affected by subjective noise and bias. Second, standard scalar reward models collapse multi-aspect human preferences into a single value, leading to the loss of dynamic trade-offs across multiple preference dimensions. Third, in policy optimization, the widely adopted KL divergence imposes primarily local constraints and may fail to capture the global structure of human preferences. To address these challenges, we propose a unified preference-aware learning framework for video generation. First, we introduce elite-guided filtering to calibrate preference data and construct reliable supervision for reward model training. We then model video quality as a multidimensional reward distribution to capture the uncertainty inherent in human preferences, and use the Wasserstein distance to align the learned reward distribution with the empirical human preference distribution. Finally, we introduce Wasserstein-based distributional alignment into GRPO, guiding policy optimization to better match the global structure of human preferences over videos. Experiments on reward modeling and video generation demonstrate that our approach improves the reliability of reward signals and the perceptual consistency of generated videos. Our code is available at this https URL.

---


### 350. [LëtzCross: A Cross-Lingual Page-Level Benchmark for Multimodal Retrieval over Luxembourgish Documents](https://arxiv.org/abs/2608.21714)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Omar El Bachyr, Fred Philippy, Laura Maria Bernardy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent page-image retrievers such as ColPali have improved retrieval over visually rich documents, yet little is known about how they behave in cross-lingual, low-resource settings. We introduce LëtzCross, a benchmark for cross-lingual page-level retrieval over Luxembourgish PDF documents, with document pages indexed as images and queries provided in English, French, German, and Luxembourgish. The benchmark combines text-focused QA pairs with visually grounded QA pairs, covering both textual and visual retrieval needs in PDF-based RAG. We use LëtzCross to compare OCR-based text-only retrievers with ColPali-style page-image retrievers and find that the latter perform better across query languages in this system-level comparison. We also examine single-language and multilingual fine-tuning. Fine-tuning transfers across query languages, with French yielding the highest mean performance on Luxembourgish queries among the single-language settings. In the multilingual setting, including Luxembourgish gives the strongest results and substantially improves retrieval for Luxembourgish queries.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
