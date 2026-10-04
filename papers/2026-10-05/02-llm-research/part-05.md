# 🧠 大模型相关研究 | 2026年10月05日

> 本类共 **384** 篇论文：已确认 **365** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

---

### 201. [My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning](https://arxiv.org/abs/2610.01161)

**<font color=#1a73e8>作者：</font>** Yihua Zhu, Qianying Liu, Weixu Qiao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) has emerged as a powerful approach for training large language model agents on multi-step tasks, yet reliance on terminal outcome rewards creates two credit-assignment problems, particularly in long-horizon tasks. First, same-outcome rollout groups provide no learning signal from terminal rewards. Second, terminal rewards provide only trajectory-wide feedback, making it difficult to identify which decisions caused a failure. Recent work supplements terminal rewards with finer-grained information from trajectory analysis, such as natural-language reflections on intermediate decisions and errors. However, natural-language diagnoses are difficult to use directly for credit assignment: their error claims may be unreliable, and they do not quantify how much each error should affect learning. We propose Self-Diagnosis-guided Terminal Credit Redistribution (FAULT), which turns diagnosed errors into explicit step-level credit anchored by terminal outcomes. FAULT checks diagnostic evidence and learns relative error costs from task outcomes. During training, the policy and self-diagnoser co-evolve, while error costs are updated online from recent outcomes. On ALFWorld, FAULT recovers learning signals from same-outcome groups, reaching 95% signal coverage versus 41% for GRPO and 72% for GiGPO, while better localizing credit to specific error steps. Across two model scales, FAULT delivers strong. improvements on the long-horizon ALFWorld and WebShop tasks while remaining competitive on short-horizon Search-based QA.

---


### 202. [Persistent Depth Ordering amid Shifting Block-Bypass Responses in Language Model Pretraining](https://arxiv.org/abs/2610.01165)

**<font color=#1a73e8>作者：</font>** Shengye Tao, Yinzhu Cheng, Haihua Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer interventions are widely used to probe the internal organization of language models, yet most analyses examine a single training checkpoint even though model representations and computations evolve throughout pretraining. This leaves open which depth-dependent intervention responses reflect persistent organization and which are transient consequences of training. We study this question using single-block identity bypass on fixed teacher-forced contexts across five released trajectories and 11 model-domain combinations. We find that block-bypass responses retain recognizable depth ordering while their magnitudes redistribute: nearby checkpoints preserve stronger rank correspondence than distant ones, and large changes concentrate at positions that recur across text samples and transfer across evaluation domains. Controlled experiments further show that changes in the natural bypass effect cannot be reduced to a single downstream sensitivity: in replicated Pythia runs, local missing-update magnitude grows while the pooled matched downstream response decreases, whereas OLMo-2 7B exhibits a different balance. These matched responses also depend on perturbation strength and direction, without identifying targeted compensation. Together, our results show that longitudinal layer sensitivity is structured but not static, and that single-checkpoint intervention responses should be interpreted in the context of how the underlying perturbation pathway evolves during training.

---


### 203. [CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment](https://arxiv.org/abs/2610.01166)

**<font color=#1a73e8>作者：</font>** Kunyang Li, Hai Nguyen, Joshua Lowe 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiovascular magnetic resonance (CMR), including cine imaging, is a reference standard for the noninvasive assessment of cardiac morphology and ventricular function. Cine CMR interpretation integrates qualitative visual assessment with quantitative measurements of ventricular volumes, ejection fraction, myocardial mass, wall thickness, and regional wall motion. Current medical vision-language models (VLMs) cannot reliably derive quantitative measurements from multidimensional cine images without analysis tools. We present CineMR, a tool-augmented VLM that invokes cardiac image-analysis tools and integrates their outputs into interleaved reasoning for quantitative CMR assessment. We also construct a multi-cohort visual question answering benchmark covering quantitative metric extraction, multiclass diagnosis, and differential diagnosis, together with tools for segmentation, phase selection, volumetry, morphometry, and regional wall motion analysis. CineMR is trained with supervised fine-tuning (SFT) on tool-interaction traces followed by Group Relative Policy Optimization (GRPO) with conditional tool-use rewards. On the multi-cohort cine CMR benchmark, CineMR achieves 35.9% pass@1 and 58.9% pass@4, compared with 1.5% pass@1 for the Qwen3-VL-8B backbone and 0.0% and 7.0% pass@1 for LLaVA-Med v1.5 and MedGemma-4B, respectively. Correct tool invocation reaches 99.8% after GRPO, up from 78.9% after SFT. Live tool outputs improve ventricular measurement accuracy by 20.4--23.7% over direct model predictions, and removing all tools reduces pass@1 from 35.9% to 27.9%. These results highlight the importance of reliable tool use for quantitative cine CMR reasoning and support CineMR as a promising approach for assistive cardiac image assessment. Code, benchmark resources, and model weights are available at this https URL.

---


### 204. [Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability](https://arxiv.org/abs/2610.01168)

**<font color=#1a73e8>作者：</font>** Roberto Stanzione, Jules Barbe, Magali Parrino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time Series Anomaly Detection has received increasing attention, driven by the growing availability of complex time series data. This surge has led to the development of numerous detection methods, as well as a variety of benchmarks aimed at thoroughly evaluating their performance. However, most existing detectors remain largely agnostic to domain context, overlooking explainability and interpretability. One of the main reasons for this gap is that current benchmarks primarily focus on detection accuracy, and only few of them evaluate spatial explainability. Moreover, no benchmark currently provides sufficiently rich semantic annotations to support the generation of human-understandable interpretations of anomalies. To address these limitations, we introduce SHAD (Scality High-dimensional Anomaly Detection benchmark), a fully annotated benchmark composed of 215 multivariate, high-dimensional time series collected from real-world distributed cloud storage systems operated by Scality. The proposed dataset includes rich contextual information, covering three families of anomalies with varying degrees of severity. As further contribution, we provide a foundation for future work by evaluating baseline methods for Detection, Explainability, and Interpretability, covering all stages of a TSAD pipeline. For Detection, we benchmark a wide range of existing anomaly detectors, testing their effectiveness on the proposed real-world dataset. Then, we consider explainability by evaluating whether measuring the contribution of each dimension in the generated anomaly score can provide accurate anomaly attributions. Finally, for interpretability, we investigate the effectiveness of frozen LLM baselines in localizing and interpreting anomalies.

---


### 205. [HeadEdit: Calibrating Language Model Behavior Through the Frozen Unembedding Matrix](https://arxiv.org/abs/2610.01170)

**<font color=#1a73e8>作者：</font>** Zirui He, Haiyan Zhao, Jingyu Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Alignment does not eliminate behavioral errors in language models. Models may still refuse benign requests, call unnecessary tools, or yield to false user claims. Current methods mitigate such errors as a computation problem, and rarely explore if the desired behavior is already encoded in the model's representation. Motivated by the observation that behavior-relevant information remains linearly decodable from the final hidden state even when the resulting logits produce the undesired behavior, we introduce HeadEdit, a gradient-free method that calibrates model behavior through the unembedding matrix. HeadEdit extracts a low-rank behavioral subspace from paired completions and uses each prompt's coordinates within it to generate a vocabulary-wide correction, thereby implementing implicitly adaptive steering without manually specified target tokens or parameter updates. HeadEdit improves all nine experimental settings across three tasks and three model families, with negligible inference overhead and no systematic loss of general capabilities. It also reveals a connection to gradient-based alignment. HeadEdit's low-dimensional representation partly predicts how preference tuning changes output logits on unseen prompts. The subspace learned from the model can also be reused after tuning, improving performance without re-extracting or retuning. These results show that HeadEdit provides a practical, lightweight, and interpretable way to calibrate model behavior through the unembedding matrix.

---


### 206. [Learning Rate Transfer for Hybrid Transformer-SSM Architectures](https://arxiv.org/abs/2610.01172)

**<font color=#1a73e8>作者：</font>** Jimin Seo, Gyubok Lee, Yeonsik Jo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning rate (LR) scaling for hybrid architectures combining Transformer and State-Space Model (SSM) blocks, a class adopted by several recent production language models. In particular, we focus on the gap between the theoretical scaling rules derived for SSMs under zero-order-hold (ZOH) discretization at infinite width with growing state size, and the field-standard practical implementations using simplified-ZOH Mamba at fixed state size. Surprisingly, in this practical regime hybrid architectures achieve a near-zero LR transfer gap across widths 256-2048 and depths 4-32 up to billion-parameter scale using only the original $\mu$P prescription, even though SSM operations fall outside its Tensor Programs representability conditions and every parameterization we test fails the standard coordinate-check diagnostic of $\mu$P correctness. We attribute this to a two-condition decomposition of LR transfer in hybrid architectures: a global update-to-weight invariance, enforced by $\mu$P's initialization and LR scaling; and a local per-component balance, provided by AdamW's per-parameter normalization. Our observations show that the optimal LR is invariant to width up to 8$\times$, that this width invariance holds across depth, sequence length, batch size, and Transformer-to-SSM ratio, and that it transfers to Nemotron-H, a production hybrid outside our custom architecture set. We hope these findings fill the gap between theoretical scaling rules and practical hybrid implementations, and stimulate further research toward bridging it.

---


### 207. [Temporally-Resolved Token Attribution Reveals the Generation Dynamics of Diffusion Language Models](https://arxiv.org/abs/2610.01177)

**<font color=#1a73e8>作者：</font>** Darpan Aswal, Céline Hudelot  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work presents Diffusion Layer Integrated Gradients (DLIG), a token attribution method for diffusion language models (DLMs) that extends Integrated Gradients (IG~\cite{sundararajan2017axiomatic}) to arbitrary layers and denoising steps. DLIG attributes a DLM's progressive commitment to a self-generated or fixed completion for an input prompt. We establish direct correspondences between DLIG and the IG axioms of completeness, implementation invariance, linearity, and symmetry preservation. As a lightweight complement to interventional analysis, DLIG provides an inexpensive first check of mechanistic hypotheses across the denoising trajectory. We demonstrate this on word-sense disambiguation, multi-hop graph reasoning, and sentence infilling, revealing how DLMs draw on inputs across positions, layers, and denoising steps.

---


### 208. [Skeleton-and-Strategy Prompting: Training-Free Negation Understanding for Vision-Language Models](https://arxiv.org/abs/2610.01180)

**<font color=#1a73e8>作者：</font>** Yuliang Cai, Mohammad Rostami, Jesse Thomason  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the strong performance of Vision-Language Models (VLMs) on a wide range of visual question answering (VQA) tasks, these models consistently struggle to understand negation and produce incorrect answers when questions involve negated clauses. To address this limitation, we propose Skeleton-and-Strategy Prompting (\textbf{SSP}), a training-free, in-context learning method that improves VLM negation understanding capabilities without any parameter updates. Given a negation question, our method first abstracts the underlying question structure into a skeleton, retrieves a small set of same-skeleton questions from a lightweight question pool, then prompts the VLM to analyze their shared negation pattern and synthesize a single-sentence answering strategy. The skeleton and strategy are prepended to the test sample to guide the model correctly tackle the negation problems. Experiments on multiple negation VQA benchmarks show that SSP achieves state-of-the-art performance on negation-focused VQA tasks while remaining computationally efficient.

---


### 209. [FlashBack: Knowing When to Remember in Streaming Vision-Language Models](https://arxiv.org/abs/2610.01192)

**<font color=#1a73e8>作者：</font>** Yi Chen, MingMing Yu, Rui-Qi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming vision-language models must process continuously growing video streams under a bounded compute budget, creating a persistent tension between real-time perception and long-term memory. Retrieving historical information provides a natural remedy, yet historical recall is not uniformly beneficial: unnecessary history may introduce irrelevant context into current reasoning and interfere with native real-time perception. Effective streaming memory should therefore address not only what to remember, but also when and how to access it. To this end, we introduce FlashBack, a training-free framework for selective, multi-level memory in streaming vision-language models. Before retrieving history, FlashBack draws on the semantic understanding of the frozen streaming VLM to infer whether a query calls for historical evidence. This assessment determines whether inference remains on the Native trajectory or invokes an isolated Recall trajectory. The Recall trajectory combines recent context with retrieved long-term memory through a query-local Side-KV pathway, preserving local temporal continuity without modifying the persistent Native state. We instantiate FlashBack on StreamingVLM and Mage-VL-4B and evaluate it on OVO-Bench and StreamingBench. The results show improvements on several long-horizon and memory-dependent tasks while largely preserving real-time perception, with performance competitive with strong training-based streaming methods despite requiring no additional training. Our code will be announced later.

---


### 210. [Federated Agent Optimization](https://arxiv.org/abs/2610.01195)

**<font color=#1a73e8>作者：</font>** Qiang Yang, Zhiqiang Kou, Xueyi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate in private environments and accumulate valuable experience from task execution, tool use, feedback, and local knowledge. Yet such experience is distributed across organizations and cannot be directly shared because of privacy and proprietary constraints. Conventional federated learning is insufficient for this setting, as agent capabilities extend beyond model parameters to memory, tools, rewards, skills, and structured knowledge. In this paper, we formulate \textbf{Federated Agent Optimization (FAO)}, which studies how distributed agents can collaboratively improve through controlled information exchange while keeping raw data, complete trajectories, and private knowledge local. We define FAO as a multi-objective problem balancing agent utility, privacy leakage, and communication cost, and organize its optimization space across policy, memory, tool use, reward, and structured knowledge and skills. We further characterize how private experience can be abstracted, protected, aggregated, and adapted into transferable capabilities, providing a unified view of how agents can benefit from one another without direct experience sharing. Finally, we identify the key challenges of FAO and outline several promising directions for future research toward trustworthy federated agent systems.

---


### 211. [Dependency-Aware Reward Shaping for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.01207)

**<font color=#1a73e8>作者：</font>** Ziyi Chen, Yan Zhang, Jianhui Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When training large language models with reinforcement learning, terminal rewards provide little guidance about which steps matter. Common methods for assigning step credit overlook that work built on uncorrected mistakes is wasted while independent work remains valid. With only a final success/failure reward, every step in a failed episode has zero total future reward, even when it made progress. We propose Dependency-Aware Reward Shaping (DARS), which represents task progress as predicates linked by prerequisite relations and assigns step-level credit over the dependency graph. An annotator marks which predicates each step verifies, invalidates, or repairs. Verified predicates are discounted according to graph distance from the nearest broken prerequisite, while independent predicates are unaffected. Repairs update these weights based on any errors that remain; invalidated predicates need re-verification to regain credit. A fixed potential converts these annotations into signed per-step rewards. A common reward and annotation interface allows DARS to integrate with a range of reasoning and agentic training methods, such as GiGPO and ARPO/AEPO, without changing their rollout strategies or optimizers. Across five task families and models from 1.5B to 8B, DARS improves success by up to 10 points over GiGPO trained with the same budget and harness (ALFWorld), raises the WebShop task score and Search-R1 QA accuracy, complements AEPO's entropy-based training on AIME24/25 with a Python interpreter, and exceeds OmniOPD in controlled tool-free reasoning comparisons at 1.7B and 4B. Ablations show that step-level credit, dependency attenuation, and graph topology each contribute. On ALFWorld, a distilled 8B annotator matches the API annotator, enabling DARS to run efficiently without a frontier judge. Code is available at this https URL.

---


### 212. [AutoGUIWorld: Image Generators as Visual World Models for GUI Agent](https://arxiv.org/abs/2610.01215)

**<font color=#1a73e8>作者：</font>** Cheng Yang, Yifan Wu, Yutao Huang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents require high-quality interaction trajectories to learn how software environments respond to actions, maintain state, and support multi-step workflows. However, the diversity of available trajectories is constrained by the applications, interface states, and workflows accessible in the underlying environments. Expanding this coverage requires deploying increasingly diverse and complex software, with specialized applications imposing additional installation, configuration, and runtime costs. We introduce AutoGUIWorld, a data generation framework that combines the visual priors of image generators with the task knowledge of a planner to synthesize GUI interaction trajectories without deploying or running the corresponding software environments. AutoGUIWorld samples initial GUI scenes from structured specifications of operating-system context, visual appearance, and interface state, and generates tasks conditioned on those scenes. A planner then specifies atomic actions and their intended visual consequences, while an image generator iteratively edits the current screenshot to produce subsequent observations. Action grounding and transition-level quality filtering yield 79,266 spatially annotated step-level training samples across Ubuntu, Windows, macOS, and Chrome. Fine-tuning Qwen3.5-35B-A3B on AutoGUIWorld trajectories improves the mean task score on OSWorld from 33.0% to 40.8% and the task success rate on ScienceBoard from 14.0% to 32.2%. These results show that generated trajectories improve GUI-agent performance on real desktop and scientific tasks.

---


### 213. [AGO AI Quality Gate: Evidence-First Release Decisions for Retrieval-Augmented Generation](https://arxiv.org/abs/2610.01218)

**<font color=#1a73e8>作者：</font>** Giulio Zeloni, Enrico Lo Conte, Salvatore Rionero 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprises adopting retrieval-augmented generation (RAG) face a recurring operational decision: promote, revise, or block a system version. The evidence is incomplete and the metrics come from fallible LLM judges. We report on AGO AI Quality Gate (AGO), an evidence-first quality-gate framework deployed in industrial RAG assessment engagements. AGO integrates four key components: a four-state decision model that treats missing data and judge errors as explicit outcomes; layered scoring combining deterministic checks, local guardrails, and structured LLM evaluation; a stratified beta-binomial gate that quantifies regression risk probabilistically; and a mandatory meta-evaluation protocol to validate the LLM judge before it influences decisions. Since engagement data is proprietary, we evaluate the judge layer on RAGBench, a public benchmark of 100k annotated RAG traces across 12 datasets. On identical stratified test samples (N=1200 per judge), a low-cost judge (gpt-4.1-nano) detects non-adherent answers barely above chance (AUROC 0.603 [0.570, 0.634]), despite producing flawless protocol output, while gpt-4o reaches 0.783 [0.756, 0.807] -- yet its per-domain performance still ranges from 0.62 to 0.88. A fixed-seed gate study spanning regression, no change, and improvement quantifies unsafe promotion, false-alarm cost, and improvement throughput. Under regression, the decision-grade profile reduces unsafe promotion to 22.2%-35.1%, against 29.3%-41.8% for a naive gate. These results support the design choices that judge quality must be measured per engagement and that point estimates alone are not a release decision.

---


### 214. [Reputation, Strategy, and Emotion Effects on Generative AI Cooperation: A Comparison Across Reasoning and Non-Reasoning Models](https://arxiv.org/abs/2610.01222)

**<font color=#1a73e8>作者：</font>** Celso de Melo, Zishan Feng, James Hale 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative AI (Gen AI) systems take on increasingly autonomous roles in economically and socially consequential interactions, understanding their propensity to cooperate -- and the signals that shape this propensity -- has become essential. We examine cooperative behavior in frontier Gen AI models using the iterated prisoner's dilemma, manipulating counterpart reputation (positive, unknown, negative), strategy (extortion vs. generosity), and non-verbal emotional signaling (facial expressions conveying competitive or cooperative appraisals). In a first study with non-reasoning models (Claude 3.5, Gemini 2.0 Flash, GPT-4o), cooperation was systematically shaped by all three factors, paralleling patterns long documented in human behavioral research, though models varied substantially in how heavily each factor was weighted. A second study with reasoning models (Claude 4.6, Gemini 3, GPT-5.2) revealed a more concentrated reliance on strategy and reputation, a near-elimination of the Potemkin effect observed in non-reasoning models (evidenced by near-uniform cooperation in a diagnostic harmony game), and a more conditional role for emotion consistent with a hierarchical cue-weighting strategy rather than a simple loss of social sensitivity. Reasoning models also showed heterogeneous end-game behavior, ranging from sustained cooperation to systematic last-round defection effect, revealing model-specific exploitability profiles with direct practical relevance for deployment in negotiation and other multi-round interactions. Together, these findings characterize Gen AI models as increasingly sophisticated, though heterogeneous, social actors, and underscore the practical value of developing standardized cooperation benchmarks to inform the responsible deployment of Gen AI in interactive, socially consequential settings.

---


### 215. [Have an LLM Write Your Anomaly Detector: Autonomous Discovery of Compact, Interpretable Detectors for Time Series](https://arxiv.org/abs/2610.01223)

**<font color=#1a73e8>作者：</font>** David Berghaus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection trades off predictive accuracy, computational efficiency, and interpretability. We use a large language model not as the detector but as the author of one: an autonomous research loop in which the model repeatedly edits a single short NumPy program under a leakage-free objective, keeping the best-scoring detector it finds. The loop discovers two compact detectors, one for univariate and one for multivariate series, that describe short windows by their local spectral features and compare them with the training-region distribution through a covariance-aware distance. On the TSB-AD benchmark these detectors lead the field across metrics, ahead of the strongest classical, deep, and foundation-model baselines including Time-RCD, yet they train no network and use no GPU, and the multivariate detector is faster than every similarly performing baseline. LLM-driven program search is thus a practical route to accurate, efficient, and transparent detectors.

---


### 216. [HHR: Hierarchical Hash Retrieval for Efficient LLM Generation](https://arxiv.org/abs/2610.01230)

**<font color=#1a73e8>作者：</font>** Lianjun Liu, Tiantian Zheng, You Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient long-context inference is essential for large language models (LLMs), yet it poses a severe computational bottleneck. Hash-based retrieval offers an efficient alternative by encoding queries and keys into binary codes and using Hamming distance for key selection. However, this leads to a critical mismatch between Hamming distance and attention relevance. Query-Key logits depend jointly on directional similarity and feature magnitudes, whereas hash binarization discards magnitude information, causing both false-positive retrieval of low-logit keys and false-negative omission of high-logit keys. To address these failures, we propose Hierarchical Hash Retrieval (HHR), a coarse-to-fine framework that progressively improves retrieval accuracy through Geometry-Aware Key Routing (GKR) and Learned Hash Projection (LHP). GKR learns a head-wise orthogonal transformation to redistribute feature magnitudes and derive more discriminative page-level logit bounds, enabling effective pruning of low-logit keys while preserving important candidates. LHP then learns a head-wise projection space that aligns Hamming distance with the true Query-Key relevance ranking for fine-grained retrieval. By combining GKR and LHP, HHR suppresses false positives and recovers false negatives, substantially improving the fidelity of hash-based sparse attention. Extensive experiments across diverse LLMs and benchmarks demonstrate that HHR achieves superior performance over existing methods. For example, on LongBench, HHR improves the average score by 1.10 points and, at a context length of 128K, achieves up to a 3.30x decoding speedup and a 2.83x end-to-end speedup for Llama-3.1-8B-Instruct. The code is publicly available at this https URL.

---


### 217. [ASCRIBE: Atomic and Significance-Based Reasoning for Thai Clinical SOAP Note Generation](https://arxiv.org/abs/2610.01234)

**<font color=#1a73e8>作者：</font>** Tarm Kalavantavanich, Teerawut Ponarchar, Pattaramanee Arsomngern 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic SOAP note generation can ease the documentation burden on physicians, but existing reasoning methods often omit clinically important information and generate unsupported content. Progress in Thai is further hindered by the lack of publicly available datasets. We propose ASCRIBE, a physician-inspired reasoning framework that ascribes a clinical-significance level to each extracted atomic fact in the conversation before summarization, making a general-purpose LLM a more reliable scribe. We also release ThaiClinicBench, the first de-identified Thai clinical summarization benchmark of real encounters, together with a synthetic training corpus derived from real clinical notes. As a prompt, ASCRIBE outperforms chain-of-thought prompting on GPT-5.4 and Gemini 3.1 Pro across the physician-aligned LLM-judge metrics and improves on standard prompting by up to 10.3 points on the completeness LLM-judge metric. As a GRPO reward, it enables a Gemma-4-E4B model trained solely on synthetic data to match Gemini 3.1 Pro in factual precision and surpass it in completeness. Code and data can be found at this https URL.

---


### 218. [Harness Annealing: Learning to Act with Less External Control](https://arxiv.org/abs/2610.01235)

**<font color=#1a73e8>作者：</font>** Yingxuan Yang, Huacan Chai, Ying Wen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents rely on external harnesses to track state, organize workflows, and verify answers. Beyond providing tools and information, these harnesses supply control decisions about what to investigate, whether to revise, and when to stop. Training on successful harness-supported trajectories can improve task performance while leaving these decisions dependent on runtime intervention. We ask whether harness-supported experience can also teach the model to make these decisions, allowing the division of control to change as the model learns. We call this objective harness internalization: learning to assume specified control responsibilities while retaining task performance after the corresponding support is withdrawn. We introduce HARNESS ANNEALING TRAINING (HAT), which combines explicit control supervision with a curriculum over teacher trajectories collected under progressively weaker harnesses. Experiments with 9B and 35B models on SWE-QA and SWE-QA-Pro evaluate every checkpoint under four deployment harnesses. Selected annealed checkpoints operating with tools alone achieve scores close to those of their respective starting checkpoints deployed with the full harness. The benefits vary with model scale and deployment configuration, and further annealing does not uniformly improve performance. These findings suggest that harness-supported experience can help reduce the runtime control required by a trained agent.

---


### 219. [Learning to Ask: Information Acquisition for SLM-LLM Collaboration, under a budget](https://arxiv.org/abs/2610.01236)

**<font color=#1a73e8>作者：</font>** Yongjun Kim, Xiaoxiao Li, Jaeho Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaboration between a small language model (SLM) and a large language model (LLM) offers an opportunity to combine the efficiency of smaller models with the strong reasoning capabilities of larger ones. Existing approaches primarily frame such collaboration as a computation allocation problem, determining which model should handle each portion of the reasoning process. In black-box API-based settings, however, this paradigm can be inefficient due to coarse-grained delegation or repeated transmission of context across model switches. In this work, we instead formulate SLM-LLM collaboration as an information acquisition problem, under an API budget constraint. The SLM remains the primary reasoner and selectively queries a black-box LLM advisor only when needed, issuing targeted queries rather than delegating the reasoning process itself. To realize this strategy, we develop a three-stage RLVR framework that learns whether to call the advisor, how to formulate useful queries, and how to integrate the collaboration into the reasoning process by jointly refining advisor invocation and information use. Across mathematical reasoning and coding tasks, our approach improves the performance--cost tradeoff over existing collaboration baselines and, in some settings, matches or exceeds oracle problem-level routing. Finally, we show that our strategy can transfer to other advisor model families, without further training.

---


### 220. [Mixture-Trained Merging for Unified Multi-Objective Models](https://arxiv.org/abs/2610.01238)

**<font color=#1a73e8>作者：</font>** SeongHyeon Kim, Chaeyun Jang, Seungyoo Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unified language models are increasingly expected to combine heterogeneous capabilities, such as mathematics, code, instruction following, and controllable thinking behavior, within a single set of parameters. A common solution is sequential post-training on multiple objectives, but this entangles all objectives along one optimization trajectory and makes the final model highly sensitive to training order, data ratios, schedules, and stopping criteria. Weight-space merging offers a modular alternative, but naive merging of single-objective experts often fails: domain capabilities degrade sharply, or think/non-think modes collapse into one dominant behavior. We attribute both failures to incompatible weight-space geometry: experts trained on single objectives drift to distant regions of parameter space, placing their interpolations outside any shared low-loss basin. We propose Mixture-Trained Merging (MTM), which trains each branch on an objective-biased data mixture rather than a single objective, exposing it to cross-objective interactions and making branches compatible at merge time. MTM uses merged-model evaluations as a low-cost signal for selecting branch mixtures, avoiding expensive data-mixture ablations. The procedure is iterative: each round promotes the base model using globally selected merge coefficients and refines each branch mixture using domain-preferred coefficients under constraints that preserve other objectives. To scale beyond simplex grid search, MTM uses qNEHVI-based multi-objective Bayesian optimization. Across code, mathematics, instruction following, and think/non-think control, MTM outperforms naive merging and preserves behavioral separation where single-objective merging collapses, suggesting that effective unified models require branches trained to be mergeable.

---


### 221. [Evaluating the Robustness of Japanese LLMs to IME-Related and Typographical Errors](https://arxiv.org/abs/2610.01241)

**<font color=#1a73e8>作者：</font>** Ryota Mibayashi, Hiroaki Ohshima  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance across various natural language processing tasks. However, their robustness to typographical errors remains underexplored, particularly in Japanese, where text input involves multiple writing systems and IME-based conversion. In this study, we evaluate the robustness of Japanese LLMs against realistic Japanese-specific typos. We introduce five typo categories: Character Transposition, Character Replacement, Homophone Conversion, Japanese IME Conversion, and Full-Width Conversion. These perturbations are applied to three Japanese benchmark datasets (JMMLU, JCommonsenseQA, and JamC-QA), and eleven Japanese and multilingual LLMs are evaluated. The results show that Character Transposition and Character Replacement typos consistently reduce accuracy across benchmarks, whereas IME Conversion, Full-Width Conversion, and Homophone Conversion have relatively limited impact. These findings reveal that current Japanese LLMs remain vulnerable to realistic Japanese typing errors, particularly those that substantially distort the original input, highlighting the importance of robustness evaluation in practical input environments.

---


### 222. [When the Judge Acts: Auditing VLM-Guided Image Selection on Culturally Situated Prompts](https://arxiv.org/abs/2610.01243)

**<font color=#1a73e8>作者：</font>** Huichan Seo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly act as judges that pick the best of several generated images, so their choices decide what users see. Such judges are usually validated by score agreement with human ratings, not by the images they return. We audit VLM judges as decision-makers: on 300 culturally situated prompts, we compare the returned image with human ratings the judge never sees and with random choice from the same candidates, and repeat every decision with the candidates reordered. A 4B-parameter judge barely beats random and falls short of a CLIP similarity baseline. It picks the first image shown in 49% of calls (chance: 28%), and reordering changes its choice on 60% of prompts. For this judge, agreement across orders is informative: decisions that survive reordering are much better than random, whereas agreement with a weaker second judge keeps the wrong ones. An 8B judge shows almost no position bias and outperforms CLIP, yet for it the same filter mostly discards good decisions. Agreement helps only when it targets the judge's failure mode, so filters must be re-audited whenever the judge changes. The 4B judge's slight rise in stereotype ratings is no longer detectable after aggregating across orders or with the larger judge.

---


### 223. [Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration](https://arxiv.org/abs/2610.01244)

**<font color=#1a73e8>作者：</font>** Herun Wan, Jiaying Wu, Minnan Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems are often judged by whether they reach the correct answer. This can miss a distinct failure: collaboration may leave behind a corrupted information state even when the immediate decision is correct. We call this an off-query failure. To study this failure in collaborative decision support, we introduce OffQuery, which separately evaluates evidence verification (T1), shared-state reconstruction (T2), and task resolution (T3) in two representative high-stakes settings: healthcare and disaster response. Across GPT, Gemini, and Qwen models, standard collaboration shows much stronger task performance than state reliability. Averaged over 21 model--setting combinations, task resolution reaches 64.7%, while evidence verification and state reconstruction reach only 14.3% and 43.1%. We trace this gap to selective information use: current queries often bypass corrupted facts, which become consequential when later tasks require them. We further introduce ReGround, which resolves conflicting evidence, verifies shared facts, reconstructs a trusted state, and reasons over that state. Across seven models from three families, ReGround improves all three capabilities in every evaluated setting, with average relative gains of 309.0%, 82.9%, and 17.6% on T1, T2, and T3. Reliable collaboration therefore requires both a correct decision and a reliable shared state for future reasoning.

---


### 224. [DeFA: Dependency-Guided Failure Attribution for LLM Agents](https://arxiv.org/abs/2610.01256)

**<font color=#1a73e8>作者：</font>** Bo Deng, Xinlei Zheng, Yi Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Errors in LLM agent executions and their visible consequences can be separated by many steps, making decisive-error localization a matter of understanding both step content and step dependencies. We introduce DeFA, a dependency-guided framework for agent failure attribution. DeFA first combines protocol relations and semantic dependencies into an event dependency graph spanning the trajectory. It then identifies events that may violate task requirements and traces their sources and subsequent effects to construct a failure propagation graph. Finally, DeFA uses step evidence and the steps' roles in failure propagation to identify the decisive error, responsible agent, and error category. To support long trajectories, DeFA partitions executions into segments and combines the current segment's detailed content with summaries of the other segments, giving local diagnosis access to global execution context. Across Who and When and the Who and When Pro text subset, DeFA achieves the highest responsible-agent and exact step accuracy with all evaluated backbones, and the highest failure-mode accuracy among taxonomy-aligned methods on Pro. Further experiments on image and video trajectories demonstrate its applicability to multimodal failure attribution. Ablations support the contributions of segmentation, the event dependency graph, and the failure propagation graph. Using DeFA's diagnostic feedback for skill evolution in Trace2Skill improves downstream task accuracy by 6-15 percentage points over the native pipeline, showing that the diagnoses can also support agent improvement on subsequent tasks.

---


### 225. [Science Utopia? Closed-Loop LLM Simulation of Academic Research Ecosystems](https://arxiv.org/abs/2610.01257)

**<font color=#1a73e8>作者：</font>** Yiqiao Jin, Yiyang Wang, Lucheng Fu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific progress emerges from a longitudinal ecosystem in which researchers, institutions, funding agencies, collaboration networks, and the scientific literature co-evolve. As AI becomes increasingly involved throughout the scientific research cycle, understanding these interconnected and evolving processes becomes increasingly important. We introduce SciUtopia, a persistent, closed-loop LLM-agent simulation framework for studying academic research ecosystems. SciUtopia models interconnected scientific processes such as research-direction choice, collaboration, submission, peer review, resubmission, citation, funding, and researcher attrition, while maintaining evolving states across simulated years. Its configurable institutional mechanisms and information channels provide a controlled testbed for matched counterfactual experiments and targeted interventions. Across 61 simulation worlds, SciUtopia simulates over 40,000 researchers from 8,000 institutions, producing around 400,000 publication decisions and 1.2 million LLM-generated peer reviews. Using these longitudinal simulations, we find that rejection-driven resubmission substantially amplifies reviewer burden beyond population growth alone, cautious exploration balances citation impact with career success and long-term topic diversity, and resource inequality can emerge even without detectable cumulative advantage from narrowly winning early funding. Code is available at this https URL.

---


### 226. [Feedback Without the Wait: Piloting a Generative AI Practice Platform in a Large Maths Class](https://arxiv.org/abs/2610.01262)

**<font color=#1a73e8>作者：</font>** Lili Chen, Gavin Buskes, Yuxin Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Timely and specific feedback is one of the strongest influences on student learning, yet it is difficult to sustain in large electrical engineering classes where the ratio of students to demonstrators is high and a learner who is stuck may wait days to find out why an approach was wrong. Generative Artificial Intelligence (GenAI) offers a way to scale conversational feedback, but using it to grade assessed work raises trust and accountability concerns, and keeping a human in the loop to assure its judgements reintroduces the very delay that erodes the value of feedback. The result is a tension between the immediacy that makes feedback so impactful and the human oversight that makes it trustworthy. In this work, we set out to resolve that tension in practice by designing and piloting a GenAI practice platform that delivers immediate, scaffolded feedback during self-directed practice. This relocates human oversight from real-time grading to the upfront verification of solutions. Our goal was to understand how students engaged with the tool, how they perceived the value and reliability of its feedback, and what lessons transfer to other engineering subjects.

---


### 227. [Autonomous OSS Threat Detection via Taxonomy-Aligned LLMs](https://arxiv.org/abs/2610.01263)

**<font color=#1a73e8>作者：</font>** Md. Robiul Islam Niloy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open source software (OSS) ecosystems face growing threats from sophisticated supply chain attacks including typosquatting, dependency confusion, Trojan Source obfuscation, malicious build injection, and CI/CD pipeline poisoning. Existing detection approaches rely on signature-based tools and rule-based systems that struggle to generalize across attack variants and emerging threat patterns. In this paper we propose a taxonomy-aligned large language model framework for automated detection and classification of OSS supply chain threats. We introduce a structured AV-xxx threat taxonomy covering five attack categories and construct a curated dataset of 999 verified real-world OSS supply chain incidents sourced from GitHub Security Advisories, CISA alerts, and security research reports spanning 2018 to 2026. Using taxonomy-aligned prompt engineering with GPT-4, our framework achieves 97.0\% multi-class classification accuracy and 97.0\% macro F1 score across all five threat categories. Comparative evaluation against five traditional machine learning baselines, one zero-shot open source LLM, and two fine-tuned neural models reveals a surprising finding: fine-tuned Llama 3.1 8B (70.5%) and SecRoBERTa (77.5%) both underperform simple TF-IDF classifiers (82.3%), while Mistral 7B without taxonomy alignment achieves only 65.7%. These results confirm that taxonomy-aligned prompting rather than model scale, domain pretraining, or fine-tuning is the critical factor enabling high classification accuracy. Our dataset and code are publicly available to support reproducible supply chain security research.

---


### 228. [Know When to Hold 'em: Correct-Token Retention in Uniform-State Diffusion Language Models](https://arxiv.org/abs/2610.01275)

**<font color=#1a73e8>作者：</font>** Mojtaba Nafez, James Henderson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uniform-state diffusion models (USDMs) can revise any token at any denoising step, which lets them correct their own mistakes, a key advantage over masked diffusion. Self-correction, however, requires both revising incorrect tokens and retaining correct ones, and we show that current USDMs lack the latter. Even under greedy-tail decoding, state-of-the-art USDMs (DUO, UDLM, and uniform-noise SEDD) keep revising 173--270 of 512 positions at every step, and these large, uncoordinated edits collapse sample diversity. A random-token corruption experiment traces this deficit to the models themselves: they reconstruct clean and corrupted tokens with nearly identical accuracy, even though clean tokens are easier targets. A decomposition of the validation NELBO shows that training barely rewards retention: incorrect predictions are heavily penalized at corrupted positions but almost free at clean ones. We propose Correct-Token Retention Regularization (CTR-Reg), a simple but effective auxiliary loss that trains the model to retain tokens left unperturbed by the forward process and requires no change to the sampler. CTR-Reg improves clean-token accuracy by 26.5 percentage points on average across six benchmarks, while leaving corrupted-token accuracy virtually unchanged, and its per-step revisions converge to only 3--11 positions. With just five greedy-tail steps, generative perplexity more than halves under CTR-Reg for all three models while diversity is preserved, and these gains hold across sampling budgets. Our results identify correct-token retention as a key missing ingredient for self-correcting diffusion language models, and demonstrate an effective fix.

---


### 229. [SCOPE-AD: Sequential cost-aware ordinal-belief planning with energy-based models for diagnostic agents](https://arxiv.org/abs/2610.01278)

**<font color=#1a73e8>作者：</font>** Ziwen Yu, Ivan Koychev, Elizabeth Coulthard 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) diagnosis requires sequential evidence acquisition under heterogeneous test costs and patient burden. Fixed-modality predictors do not jointly decide which test to acquire or when the available evidence is sufficient for diagnosis. We propose SCOPE-AD (Sequential Cost-Aware Ordinal-Belief Planning with Energy-Based Models for Diagnostic Agents) for cost-aware classification of cognitively normal (CN), mild cognitive impairment (MCI), and AD cases. A mask-aware ordinal model represents uncertainty along the ordered CN--MCI--AD continuum. Retrospective training records provide sampled Bellman targets for an energy-based teacher, whose action distributions are distilled into a Qwen policy. At deployment, the agent selects acquisition or diagnosis actions under availability and budget constraints without access to unacquired values. After each acquisition, the evidence and ordinal belief are updated before the next decision. On ADNI, SCOPE-AD achieves 77.70\% Macro-F1 at an average acquisition cost of \$50.46, exceeding the strongest evaluated baseline by 9.34 percentage points. Full-modality evaluation raises Macro-F1 by only 1.89 points while increasing acquisition cost by 116.7 times. These results support selective acquisition for cost-effective diagnosis.

---


### 230. [Dyna3: VLM-Guided Training-Free 4D Reconstruction via Depth Foundation Models](https://arxiv.org/abs/2610.01286)

**<font color=#1a73e8>作者：</font>** Xinhao Xiang, Weiyang Li, Zhijie Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent depth foundation models like Depth Anything 3 (DA3) achieve remarkable multi-view depth estimation but assume static 3D scenes, limiting their applicability to real-world dynamic environments. Existing training-free 4D methods like Easi3R and VGGT4D rely on correspondence-trained backbones whose attention encodes cross-frame matching, a property absent in depth-only models like DA3. We present Dyna3, a training-free framework that extends DA3 for 4D dynamic scene reconstruction without any fine-tuning. Our key insight is that DA3's cross-view features, though trained only for depth consistency, implicitly encode motion-discriminative signals when combined with best-match feature search across frames. Its static surfaces find consistent matches globally, while dynamic objects cannot. We further adopt vision-language models (VLM) to automatically generate scene-specific semantic prompts for SAM 3, enabling precise instance-level segmentation that distinguishes which objects move from what objects exist. For reconstruction, we decouple the scene into a cross-frame aligned static background and per-frame dynamic point clouds. Experiments on four datasets demonstrate that Dyna3 surpasses correspondence-trained methods with +5.5pp J-Mean over state-of-the-art VGGT4D on dynamic object segmentation, while achieving up to 13x faster pose estimation and 3x faster 4D reconstruction with 4 to 8x lower memory. Dyna3 could therefore enable much denser temporal sampling that prior methods cannot support.

---


### 231. [ITC-MoE: Importance-guided Token-aware Compression for MoE Diffusion Language Models](https://arxiv.org/abs/2610.01296)

**<font color=#1a73e8>作者：</font>** Lianjun Liu, Shipeng Li, You Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) Diffusion Language Models (DLMs) offer flexible parallel decoding and increased model capacity, but their large number of expert parameters incurs substantial computation and storage costs. Existing low-rank MoE compression methods largely rely on static factorization and fixed rank allocation, which overlook the distinctive properties of MoE DLMs. Specifically, we identify two properties: cross-mode non-uniform redundancy, where parameter redundancy and sensitivity to rank truncation vary across the input, output, and expert modes, and token-wise utilization variation, where hot and cold tokens exhibit distinct spectral characteristics and expert activation patterns. To address these challenges, we propose ITC-MoE, an Importance-guided Token-aware Compression framework for MoE DLMs. ITC-MoE consists of two complementary components. First, Importance-guided Adaptive Tucker Compression (IATC) incorporates activation and gradient importance into expert weight transformation, jointly factorizes expert weights across multiple modes, and adaptively allocates ranks under a fixed parameter budget. Second, Token-aware Compensation and Routing (TCR) applies lightweight low-rank compensation to compression-sensitive hot tokens and restricts the candidate expert set for cold tokens with concentrated routing patterns. By jointly adapting compression capacity and inference execution to both parameter redundancy and token-wise variation, ITC-MoE substantially reduces the computation and storage costs of MoE DLMs while preserving their generation quality. For example, on SDAR-30B-A3B-Chat-b32, ITC-MoE maintains an accuracy of 96.33% on MultiArith under a 30% compression budget, while achieving up to a 7.22x end-to-end speedup. The code is publicly available at this https URL.

---


### 232. [DAYJOB: A Benchmark for Long-Horizon Professional Work](https://arxiv.org/abs/2610.01306)

**<font color=#1a73e8>作者：</font>** Stephanie Finley, Liudas Panavas, Thomas Mikkelson 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Professional work often starts with a brief request that leaves the professional to work out what is needed, which documents matter, and whether the request's premise holds. We introduce DAYJOB, a benchmark of 130 tasks built by professionals in healthcare (50) and finance (80). The tasks are estimated to take a professional 13.6 hours on average in healthcare and 16.6 in finance. Each task is a containerized Harbor environment with an expert rubric of binary criteria (median 47.5 and 57.5 per task) that an agentic judge applies to the delivered files, and an attempt passes only if it meets every criterion. Across 30 model configurations from 13 developers, the strongest, Claude Opus 5.5, passes 24.7% of healthcare and 23.9% of finance attempts, and the median configuration passes 0.6% and 2.5%. In case studies, agents accept premises that the record contradicts and carry wrong inputs through otherwise consistent analyses. We release all healthcare tasks, 50 of the 80 finance tasks, the evaluation harness, and the leaderboard.

---


### 233. [What Wins a Vote? Formatting, Length, and Lexical Diversity in the French Compar:IA LLM Arena](https://arxiv.org/abs/2610.01316)

**<font color=#1a73e8>作者：</font>** Simonas Zilinskas, Maayeesha Farzana, Christophe Benavent  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM arenas turn pairwise human preferences into model rankings. Those preferences may reflect how an answer is presented as well as what it says. We take a stylometric approach to 137,293 decisive French-language votes from the July 2026 Compar:IA release; the primary formatting analysis includes 137,113 battles across 116 models, and the joint estimates use the 127,092 battles with all required measurements. For each battle, we reconstruct the response visible when the user voted. We then compare the raw ranking with rankings adjusted for formatting, length, readability, vocabulary variety, and sentence structure. Presentation is associated with winning, but length, bold text, and lists tend to occur together, making their individual contributions hard to separate. Across the measured features, two associations change least across specifications: bold usage (+11.0% win odds per standard deviation in the joint model) and moving-average type-token ratio (MATTR), a measure of vocabulary variety that is less sensitive to answer length (+16.8%). The bold association is substantially smaller in observed multi-turn conversations, whereas the MATTR association changes little; because users choose whether to continue, this difference is descriptive rather than causal. The full adjustment moves 36 of 116 models by at least ten ranks. Yet comparisons with external benchmarks do not show that adjusted rankings better measure capability. We therefore recommend publishing raw and adjusted rankings side by side as a transparent sensitivity analysis.

---


### 234. [TRACE: Trajectory Return Attribution and Contrastive Erasure for Multi-Turn Safety](https://arxiv.org/abs/2610.01323)

**<font color=#1a73e8>作者：</font>** Fengpeng Li, Kemou Li, Qizhou Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models (LLMs) often refuse a harmful request but comply once the same goal is spread over several turns. Preference objectives score whole responses to single prompts, so their training loss alone cannot control risk on unseen histories. Our analysis gives sufficient conditions under which suppression at supervised single-turn contexts yields a bound on multi-turn trajectory risk. The bound accounts for coverage, transfer slack, and leakage, and characterizes contraction relative to a base-policy risk budget evaluated on the trained policy's contexts. TRACE (Trajectory Return Attribution and Contrastive Erasure) turns this principle into a token-level objective. On the safe response, each token is weighted by the discounted return of a refusal-attributable advantage. The advantage compares a frozen reference model with its refusal-ablated copy, allowing earlier response tokens to receive credit from later refusal-related evidence. At high-gap positions on rejected responses, TRACE combines the observed token with policy-selected alternatives in the erasure target. A gradient-norm penalty replaces the retain set. Across five open-weight models and seven multi-turn attacks, TRACE gives the lowest attack success rate (ASR) in all 35 model and attack pairs, while the model utility evaluated on MMLU and HellaSwag drop by at most 1\.23 points. Source code can be found in the supplemental material.

---


### 235. [Evaluating Biomedical Reranking for LLM-Based Question Answering over Longitudinal Clinical Notes](https://arxiv.org/abs/2610.01324)

**<font color=#1a73e8>作者：</font>** Maryam Shahbaz Ali, Laura B. Strachan, Caitlin Sherman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patient-specific clinical question answering requires locating the right evidence within long, heterogeneous longitudinal clinical records in which relevant facts may be scattered across encounters, repeated in copied-forward notes, or expressed using different clinical terminology. We evaluated whether biomedical reranking can improve evidence selection and downstream answer quality in a locally deployed retrieval-augmented generation pipeline for longitudinal clinical notes. The pipeline combines PubMedBERT dense retrieval, BM25 lexical retrieval, weighted reciprocal-rank fusion, and MedCPT cross-encoder reranking. Across 1,000 open- and closed-ended question-answer pairs from a cohort of 200 bariatric surgery patients, reranking increased exact source-chunk retrieval within the top 10 items, Hit@10 from 46.6% to 60.6% and mean reciprocal rank from 0.2371 to 0.3252. With Qwen3-8B generation, local judge-assessed answer correctness increased from 44.8% to 48.6%. These results show that biomedical reranking can improve the placement of relevant clinical evidence within a limited context window, although gains in retrieval do not translate proportionally into gains in answer correctness.

---


### 236. [ARCCS: An Automated Regulatory Compliance Checking System](https://arxiv.org/abs/2610.01345)

**<font color=#1a73e8>作者：</font>** Giorgos Filandrianos, José Menezes, Chrysoula Zerva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Regulatory compliance checking - deciding whether a target document satisfies the obligations of a regulation - requires interpreting dense legal text, identifying which provisions apply, and grounding each decision in explicit evidence. We present ARCCS, an end-to-end, automated, agentic, and regulation-agnostic Legal NLP system for compliance checking. ARCCS decomposes raw regulatory text into atomic, traceable requirements and evaluates a target document against them using retrieved evidence, confidence scores, and human-interpretable justifications. This design decouples compliance assessment from any fixed regulatory template or predefined rule set, enabling the pipeline to operate over regulations of varying size and structure. We evaluate ARCCS in two complementary settings. First, in a GDPR policy-document evaluation, LLM-based judges find its decisions and justifications legally and evidentially consistent in up to 96.67% of the assessed cases. Second, on an EU public-procurement benchmark comprising more than 1,200 individual rule checks, the system attains 98.8% accuracy in violation detection. ARCCS is, to our knowledge, the first fully open-source system for end-to-end regulatory compliance checking and auditable report generation.

---


### 237. [PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents](https://arxiv.org/abs/2610.01349)

**<font color=#1a73e8>作者：</font>** Fengpeng Li, Qizhou Wang, Yuke Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents turn generated text into real side effects, so poisoned tool metadata, retrieved pages, memory, and reusable skills can steer the next call. Vetting an artifact before admission does not settle this. A safe variant and a leaking variant can produce the same admission evidence, and a sound gate then cannot relax that site for either. We make that condition precise, which leaves the last boundary a deployment can still act on. We present Provenance-Aware Capability Enforcement (PACE), which mediates every tool call immediately before it executes. Path confinement proposes an executable cut of represented influence paths, while capability and effect verification checks schema-defined effects against authority compiled from the authenticated request. We distinguish the certified execution contract from the evaluated configuration, which can restore an authorized call after a proposed block or apply a declared repair. Confinement requires the final action to preserve the certified cut. On eight executable agent-security benchmarks with three target-model families, the evaluated configuration gives strictly lowest attack success in 62 of 79 eligible attack columns and ties in 14; full-benchmark native utility loses at most three points relative to the undefended agent. A complete ablation over 1167 paired cases attributes most security gains to effect verification and refusal control to boundary adaptation. A reduced-scale adaptive search succeeds on 0/30 out-of-authority targets against the defense.

---


### 238. [MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning](https://arxiv.org/abs/2610.01352)

**<font color=#1a73e8>作者：</font>** Juekai Lin, Honglin Lin, Yuqian Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open multimodal reasoning models have benefited from large-scale reasoning supervision, yet reliable post-training remains challenging due to uneven data quality, inefficient supervision construction, imbalanced difficulty, and cross-domain interference. We introduce MMVistaReason (MVR), an open-data post-training recipe with three components: (1) broader capability coverage across complementary Analytical and Real-World reasoning groups, emphasizing structured reasoning versus visual perception and spatial grounding; (2) efficient SFT and RL data construction, standardizing heterogeneous open data through staged cleaning and annotation, combining difficulty-aware cascaded teacher distillation with answer-likelihood-based trajectory selection to construct MVR-SFT-528K, and applying scale-specific frontier filtering for MVR-RL-63K; and (3) specialize-then-integrate training, which trains complementary RL experts and consolidates their capabilities through multi-teacher on-policy distillation (MOPD). Our analyses reveal a capacity-dependent interaction between supervision difficulty, trajectory quality, and model capacity: smaller students benefit more from selected supervision, while larger students are robust to trajectory variation and mixed-domain interference. Mixed-domain RL introduces benchmark-level negative transfer, whereas MOPD provides consistent capability integration, with the preferred KL direction varying across model scales. Across 15 multimodal benchmarks, MVR-4B achieves an average score of 72.8, outperforming Qwen3.5-9B (Instruct) and MMFineReason-8B while using about 70% fewer samples than MMFineReason. Scaling to 9B improves the average to 74.4, surpassing Qwen3.5-35B-A3B (Instruct). Overall, MMVistaReason demonstrates that systematic open-data construction and capacity-aware post-training provide a practical and scalable path toward reliable multimodal reasoning.

---


### 239. [Does AI-Generated Scientific Text Follow Human Argumentation Patterns? A CARS-Based Comparison of Research Article Introductions](https://arxiv.org/abs/2610.01353)

**<font color=#1a73e8>作者：</font>** Abdelrahman Sadallah, Narjes Sheikh Asadi, Lonneke van der Plas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are moving from helping write up research to helping do it, which makes it important to know how the scientific text they produce differs from human writing. Work on this question has stayed mostly at the surface, using lexical and stylistic cues that light paraphrasing erases. We look instead at rhetorical structure, the sequence of argumentative moves through which a text makes its case. We study research-article introductions under Swales' CARS model, and compare original introductions from published linguistics articles with generated counterparts of the same papers. We find that human-written introductions are more flexible in which moves they use and in what order, while the generated ones are more uniform. Giving the models the CARS definitions makes them more rigid.

---


### 240. [LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing](https://arxiv.org/abs/2610.01364)

**<font color=#1a73e8>作者：</font>** Kay Köhle, Darko Anicic, Thomas A. Runkler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Factories are shifting toward smaller lot sizes with high product customization, requiring frequent re-programming of flexible and reconfigurable automation systems. LLM-based agents can be deployed in two complementary roles: Offline, they generate deterministic production sequences, reducing programming effort; online, they operate live machines and handle unforeseen runtime faults that static programs cannot anticipate. We propose a solution in which each factory module is paired with a dedicated LLM-based agent and an MCP tool server that exposes the module's skills via OPC UA method calls, with agents coordinating over MQTT and grounded by real-time updates of the factory state. We compare three agent architectures (orchestrator, peer-to-peer, and monolithic) across nine production challenges of increasing complexity in a simulation of a physical six-module hexagonal factory, including silent hardware fault detection. The monolithic and peer-to-peer architectures both achieve the highest mean solve rate (93\%), while the orchestrator uniquely resolves a silent conveyor-belt fault in all ten runs by autonomously rerouting plates around the blocked segment. All architectures exhibit emergent fault-diagnosis behavior without any explicit failure-handling logic, establishing standardized MCP tooling, MQTT-based inter-agent communication, and real-time state injection as a viable and reproducible foundation for LLM-programmed smart manufacturing.

---


### 241. [Sleeping Secrets: How Fine-Tuning Reawakens Privacy Risks in Language Models](https://arxiv.org/abs/2610.01365)

**<font color=#1a73e8>作者：</font>** Jianhong Li, Jiahao Chen, Yuwen Pu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Beyond adapting Large Language Models (LLMs) to specialized applications, fine-tuning has recently been shown to recover private information that is no longer accessible through direct queries. Previous fine-tuning recovery attacks, however, require genuine private supervision drawn from the same distribution, i.e., the previous training dataset. We argue that such recovery remains possible without such impractical knowledge. We show that LLM-generated candidates can provide sufficient supervision to recover previously learned private associations. Based on this, we propose ReGap, a data-free attack that recovers private associations using task structure, filters them by answer-token likelihood, and updates the target model via low-rank adaptation. Specifically, ReGap requires neither target answers nor auxiliary genuine private supervision. Across six GPT-2, OPT, and Qwen3 models, ReGap improves target-association recovery by 6-21 percentage points over the post-training target model. Recovery remains substantial even when the adaptation identities are disjoint from all memorized and evaluation identities, with no exact target answers appearing in the generated or selected supervision. Moreover, the same trained adapters increase recovery from 42\% to 63\% on a previously exposed checkpoint, but produce no gain on a matched checkpoint that never encountered the targets. This contrast shows that adaptation alone is insufficient to explain the observed recovery and that prior target exposure strongly affects post-adaptation recoverability. Our findings highlight that routine model customization can reawaken latent privacy risks, warranting urgent attention from the academic and industrial communities.

---


### 242. [Gacha Decoding: Eliciting Diverse Generations Through Instruction Following](https://arxiv.org/abs/2610.01382)

**<font color=#1a73e8>作者：</font>** Scott Geng, Yufei Zhang, Joseph Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Gacha Decoding, an inference-time method for eliciting diverse language model generations that scales with model capability. Across open-ended domains (in-the-wild chat, creative writing, planning for image generation, and protein design), Gacha Decoding significantly outperforms existing generation diversity approaches at equal quality (up to 2.4x Vendi over the next-best prior approach), reaching the same number of high-quality modes with over an order of magnitude fewer samples (11.0x) and discovering novel modes that no other approach surfaces. Our key insight is to treat diversity as an instruction-following problem: rather than relying on the LM's token entropy, we combine its instruction-following capability with randomness from an external RNG tool to scalably identify and realize distinct modes of the response space. This approach of "planning with dice" enables Gacha to invert the long-observed tension between diversity and model capability. As the underlying LM becomes a better instruction follower, diversity under Gacha Decoding consistently improves--even as its token entropy and diversity under prior approaches decline. Together, our results highlight that instruction following, rather than token entropy alone, can drive generation diversity.

---


### 243. [PRISM: A Category-Theoretic Framework for Measuring and Refining Multimodal Analogies](https://arxiv.org/abs/2610.01383)

**<font color=#1a73e8>作者：</font>** Mirella Zeisler, Ojas Shirekar, Mircea Licǎ 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analogical reasoning involves identifying and preserving relational structures across domains. However, existing approaches to AI-driven multimodal analogy generation lack an interpretable measure of whether this structure is understood and maintained in the generated output. We address this gap with Pullback Refinement via Interpretable Structural Mapping (PRISM), a modality-agnostic framework for measuring and improving relational alignment in multimodal analogies, evaluated on visual metaphor generation. PRISM represents analogies as explicit relational mappings grounded in category theory and uses VLMs to instantiate these structures across modalities. Its first component, the pullback score, quantifies relational alignment from the resulting graph representation. On the AnaloBench benchmark, selecting the correct analogy purely by pullback score achieves 82.5% accuracy, demonstrating that the score captures meaningful relational information. PRISM's second component is an iterative refinement loop that uses the pullback score as an in-context feedback signal to iteratively revise the generated image towards greater relational depth. VLM-as-a-judge and human evaluations show that PRISM consistently improves metaphor consistency and analogy appropriateness over zero- shot generation, with human participants preferring the refined output in 57.65% of pairwise comparisons. However, a qualitative analysis reveals that refinement can favour visually crowded compositions rather than genuinely deeper relational correspondences.

---


### 244. [AiSearch: Interactive Multi-Modal Search with VLMs](https://arxiv.org/abs/2610.01389)

**<font color=#1a73e8>作者：</font>** Ali Koksal, Mei Chee Leong, Vicky Sintunata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern retrieval systems must both be automated and interactive, allowing users to search and refine results in real time. We present AiSearch, a flexible multimodal retrieval framework that leverages the zero shot capabilities of Vision Language Models (VLMs) for natural language search over images and videos. AiSearch supports interactive search refinement through user feedback to tailor results to the user's intent, and allows visual benchmarking across multiple VLMs, enabling users to select the most suitable model for their task.

---


### 245. [LLM-Assisted Discovery of Typed Semantic Links for Ontology Network Construction](https://arxiv.org/abs/2610.01393)

**<font color=#1a73e8>作者：</font>** Nouha Hayouni, Sheeba Samuel, Alsayed Algergawy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constructing typed, justified semantic links between ontologies is essential for enabling interoperability across heterogeneous and interdisciplinary knowledge domains. However, manually curating such links is difficult to scale. To address this challenge, we propose an end-to-end framework for ontology network construction that automates the discovery and generation of both intra-domain and inter-domain relationships. Our approach combines domain-adapted DistilBERT embeddings for dense contextual representation, clustering-based pre-filtering to reduce the candidate search space, and GPT-4o-driven relationship generation via iterative prompt engineering to produce semantically rich, interpretable links. Applied to ReproduceMeON - a network of 33 ontologies spanning machine learning, microscopy, computational science, and experimental workflow - the pipeline reduces approximately 800k raw concept pairs to 95k high-quality candidates. Human expert validation of 429 generated relationships by two independent annotators yields an overall precision of 80.19% (91.49% on high-certainty annotations) and an F1 of 0.890, with substantial inter-annotator agreement. Comparative experiments against five similarity-based baselines, including Sentence-BERT, show a substantial performance gap (best baseline F1 = 0.581), while an ablation study demonstrates that similarity-based methods alone fail to discriminate valid from invalid relationships (AUC approx 0.5) on the filtered candidate set. These findings highlight the necessity of LLM-based reasoning over concept roles and domain semantics for accurate relationship construction.

---


### 246. [AF-Muon: An AdamW-Free Muon Optimizer for Tied-Embedding Models](https://arxiv.org/abs/2610.01395)

**<font color=#1a73e8>作者：</font>** Arash Lagzian, Paniz Halvachi, Junming Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon improves large-scale training by applying a spectral-norm steepest-descent update to matrix parameters, but practical models also contain parameter blocks that do not fit dense-matrix geometry. One important case is the tied vocabulary table, which appears in language models and other token generators and can receive multiple structurally different gradient sources, from sparse input lookups to dense output-classifier updates. In the reference recipe these blocks are handed to an auxiliary AdamW optimizer, which restores second-moment state and updates the aliased table as a generic tensor. We propose AF-Muon, an AdamW-free extension of Muon that keeps the Muon matrix update for hidden weight matrices while using a support-aware finite-cap linear minimization oracle for tied vocabulary tables and an RMS-normalized update for one-dimensional auxiliary parameters. AF-Muon therefore trains every parameter class with a single first-moment buffer and no second-moment state, saving around 20% optimizer-state memory relative to Hybrid Muon in our benchmark. Across nine tied-token settings - decoder-only language models from 124M to 1B parameters, a fully shared T5-style encoder-decoder, and ImageGPT-style image-token, protein, and sparse-MoE variants, spanning text, image, and protein-sequence data - AF-Muon improves mean validation loss and perplexity over both Hybrid Muon and a SCION-style Sign endpoint. Long-horizon runs and hyperparameter sensitivity studies confirm the gain is robust, and identical-momentum diagnostics attribute it to the finite cap, which preserves more within-row magnitude than Sign while bounding the coordinate concentration of row-RMS. These results identify tied vocabulary tables as a distinct optimizer geometry and yield a robust AdamW-free Muon variant across models, modalities, and architectures, with about 1% step-time overhead in matched training.

---


### 247. [Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States](https://arxiv.org/abs/2610.01415)

**<font color=#1a73e8>作者：</font>** Yu Luo, Jiamin Jiang, Yimin Zuo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can now undertake increasingly complex tasks, but the way they organize interaction history into memory does not ensure a coherent understanding of the current world. We introduce PoS, an inference-time framework that constructs and continually maintains explicit belief states as the agent's decision context. Each belief combines an estimate of the current world state with unresolved task requirements, making explicit what the agent still needs to learn and accomplish. To keep this belief reliable and actionable, PoS validates its consistency and monitors task progress to detect Belief Trapping, where the agent continues to act without making meaningful progress toward the goal. Recovery is then tailored to both the trapping pattern and the type of unresolved task requirement. Experiments on four benchmarks spanning execution and diagnosis show that PoS achieves the highest overall performance on every benchmark with all three LLM backbones. Ablations demonstrate the importance of consistency validation and recovery, while context-scaling experiments show resilience to context growth. Together, these results support belief construction and continual maintenance as a foundation for long-horizon context management beyond history retention and compression.

---


### 248. [SpikeMoE: Brain-Inspired Competitive Routing for Flexible Spiking Mixture-of-Experts](https://arxiv.org/abs/2610.01418)

**<font color=#1a73e8>作者：</font>** Xiaoli Liu, Yujie Liang, Jialin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) enable event-driven computation through biologically inspired dynamics at the neuronal scale, while Mixture-of-Experts (MoE) perform conditional computation through expert selection at the model scale. Integrating their strengths offers potential for flexible neural architectures. A key challenge, however, lies in designing an expert selection mechanism based on spiking activity. To address this, we introduce a spike-based k-WTA Router inspired by competition-inhibition observed in the hippocampal CA1 region. The router incorporates lateral inhibition and refractory period to select Top-K experts according to discrete spike counts. Building on this, we present SpikeMoE, a framework that integrates neuronal-scale spiking dynamics with model-scale expert selection. To address incomplete multisensory inputs in multimodal tasks, we further equip SpikeMoE with a two-stage missing-modality modeling module that combines empirical prototypes from an observed-modality pool with modality-specific learnable embeddings to construct missing-modality representations. Experiments on vision, language, and multimodal benchmarks demonstrate that SpikeMoE achieves state-of-the-art performance among the SNN baselines, matches or exceeds the performance of ANN counterparts, and maintains robustness across diverse missing-modality conditions. These results demonstrate a favorable trade-off between performance and energy efficiency, validating the integration of spiking dynamics with sparse expert computation and highlighting SpikeMoE as a promising approach to energy-efficient brain-inspired computing.

---


### 249. [Why Does Train-Validation Separation Emerge? Update-Pressure Density Dynamics in Pretrained Backbones](https://arxiv.org/abs/2610.01425)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Mingyu Du, Zongqi Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Train-validation separation is the evolving difference between performance on observed training examples and a finite held-out validation set. We propose a dynamic structural account of how this gap develops during adaptation of pretrained models: continued fitting can shift update demand from broadly reusable support toward narrower support with weaker held-out transfer. A conditional local model links this shift to increasing heterogeneity in gradient allocation and train-validation separation. Fixed training probes make this structural evolution observable without validation examples entering the readouts; held-out performance is used separately to evaluate its relation to the gap. In a constructed hierarchy implemented with a residual multilayer perceptron (ResMLP), increasing the target share of example-private features from $p=.3$ to $.5$ to $.7$, while preserving the relative mixture $1{:}2{:}3{:}4$ among the four shared feature levels, increases the final mean accuracy gap from $.185$ to $.331$ to $.527$ across five runs per condition. Masked-input losses measured separately on training and validation examples expose the corresponding transfer asymmetry. The natural language processing (NLP) analysis uses 10-epoch runs of RoBERTa, DeBERTa, and Qwen on six datasets (90 runs): the training-probe-weighted within-class and overall dispersion readouts each have positive raw and smoothed level correlations with the accuracy gap in all 90 runs. Raw changes paired at approximately one-epoch intervals remain positively associated in 86/90 and 87/90 runs, respectively. A 40-epoch ResNet-18 study tests both readouts on three vision datasets. Together, controlled simulation, NLP, and vision support the dynamic structural account across settings, with real-model evidence testing its observable predictions under the specified monitors.

---


### 250. [Generalization Is Stability, Not Accuracy: Multi-Axis Evaluation of LLMs](https://arxiv.org/abs/2610.01428)

**<font color=#1a73e8>作者：</font>** Nagham Omar, Mahmoud Jabarin, Maya Rozenshtein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generalization in large language models (LLMs) is the ability to produce consistent and semantically stable outputs when the same input is expressed in different ways. Existing work typically evaluates generalization through aggregate accuracy on a single prompt format, task, or set of variations, which conflates robustness with overall benchmark performance. In this work, we show generalization evaluation at the level of individual examples, across multiple input variants, and across different aspects of model behavior, focusing on variability rather than reducing performance to a score that can be improved through narrow training or other ways that obfuscate generalization evaluation. Following this view, we introduce the Stability-Aware Generalization Objective (SAGO), a framework that measures how much model behavior changes for the same input under different variations and benchmarks, capturing variability across several dimensions including generation consistency, internal activations, confidence, and response mirroring. We show that many commonly used models exhibit statistically significant and consistent generalization instability: no model generalizes uniformly, behavioral axes capture independent failure modes, and cross-dataset variation can reverse model rankings.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-384](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
