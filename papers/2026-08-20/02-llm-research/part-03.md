# 🧠 大模型相关研究 | 2026年08月20日

> 本类共 **161** 篇论文：已确认 **151** 篇，待复核 **10** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-161](./part-04.md)

---

### 101. [Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability](https://arxiv.org/abs/2608.17723)

**<font color=#1a73e8>作者：</font>** Abdul Mueez, Aaditya Baranwal, Junior Chaj-Mejia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analog gauges remain common in industrial environments where manual inspection is costly or hazardous. The engineering application addressed here is direct numerical reading of single-target analog-gauge images, while the artificial-intelligence contribution is a systematic evaluation of specialization, transfer, robustness and reliability for a general-purpose vision-language model (VLM) without an explicit pointer-segmentation and geometric-reading pipeline. The Qwen2.5-VL-7B-Instruct model is evaluated using zero-shot prompting, in-context learning (ICL) and parameter-efficient fine-tuning with Quantized Low-Rank Adaptation (QLoRA) on a public synthetic dataset, a video-derived Pressure Gauge dataset and a proprietary industrial dataset. All fine-tuning experiments use a fixed 20-epoch protocol with the final epoch used for analysis; separate models with and without supplied gauge ranges remove prompt-setting confounds. The primary metric is range-normalized mean percentage error (MPE). The best fine-tuned MPE values are 2.39% on the synthetic dataset, with a 95% bootstrap confidence interval (CI) of 1.43-3.90%; 2.61% on the Pressure Gauge dataset, with a CI of 1.66-3.80%; and 4.43% on the proprietary industrial dataset, with a CI of 2.31-7.14%. Leave-one-dataset-out experiments reveal substantial transfer degradation on held-out synthetic and proprietary data, while robustness tests identify Gaussian blur as the strongest tested corruption. Reliability analysis shows that high-confidence errors remain possible, motivating abstention and independent validation in safety-critical use. These results support QLoRA-specialized VLMs for direct single-gauge reading but not yet a deployment-ready plant-monitoring pipeline.

---


### 102. [Evaluating the Diversity of AI-Generated Content with Diversity Profiles](https://arxiv.org/abs/2608.17731)

**<font color=#1a73e8>作者：</font>** Xiuyuan Hu, Xuege Hou, Guoqing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diversity is a fundamental criterion for evaluating generative artificial intelligence (AI) systems, yet its measurement remains inherently ambiguous. Existing approaches typically represent generated samples in an embedding space, compute pairwise distances or similarities, and aggregate them into a single scalar score. Such scalar summaries are convenient, but they often encode different inductive biases and may yield contradictory rankings of the same sample sets. In this paper, we argue that diversity evaluation for AI-generated content is intrinsically under-specified when reduced to a single number. We first review representative diversity metrics, and then diagnose their limitations from two complementary perspectives: an axiomatic analysis showing that no representative scalar metric satisfies all desirable properties simultaneously, and an empirical analysis showing that high-dimensional representation spaces can induce concentrated, modality-dependent distance distributions. To address these issues, we propose diversity profiles: curve-valued, condition-aware summaries that evaluate a parameterized diversity family across a range of thresholds, scales, exponents, or orders under a specified representation and distance or kernel function. Diversity profiles reveal whether a comparison is robust across resolutions or instead depends on an arbitrary parameter choice. We instantiate profiles for several representative metric families and demonstrate their practical use in generative AI evaluation. Overall, diversity profiles provide a more transparent and resolution-aware framework for comparing the diversity of AI-generated content.

---


### 103. [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](https://arxiv.org/abs/2608.17756)

**<font color=#1a73e8>作者：</font>** Xule Liu, Yijun Liu, Chao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory is a key capability of LLM agents. Persistent memory extends this across sessions---enabling recall, revision, and personalization. Yet its multi-stage pipeline (ingestion, retrieval, filtering, generation) makes failures difficult to localize: end-to-end evaluation reveals that an error occurred, but not which stage caused it. Existing evaluations often report aggregate performance without paired statistical comparisons, slice-level non-regression checks, or stage-level diagnostic traces. We propose D$^2$ACCI (Diagnostic-Driven Artifact-based Closed-loop Controlled Iteration), a dual-loop protocol whose outer diagnostic gate promotes, feature-flags, or rejects memory interventions based on paired evidence, protected-slice monitoring, and trace-level localizability. We further introduce DCR, a graded observability metric that measures whether failures remain localizable, and D$^2$ACCI-Eval, a reusable artifact for gate replay. We instantiate the protocol in MemStack and evaluate on three public benchmarks, achieving 93.59% on LoCoMo, 90.93% on LongMemEval, and 57.20% on PersonaMem-V2. Five paired ablations show that supplement extraction, session-memory retrieval, and Forget Guard yield statistically significant gains (+1.9 to +3.7pp, all p $\le$ .003). In contrast, BM25/RRF is retained as a monitored feature flag---a distinction invisible to aggregate-only evaluation. A diagnostic audit shows enriched traces substantially improve root-cause agreement over result-only relabeling. Diagnostic artifacts reach 98--100% DCR@3 versus 0% for results-only logs. These results establish that robust memory-system iteration demands traceable, statistically grounded, and regression-aware evidence---exactly the gap D$^2$ACCI fills.

---


### 104. [Debate Training Reduces Reward Hacking in RLAIF](https://arxiv.org/abs/2608.17776)

**<font color=#1a73e8>作者：</font>** Zachary Kenton, Lili Janzer, Rory Greig 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting most relevant to overseeing increasingly capable AI systems. We study mathematics tasks, where final-answer correctness is verifiable, allowing us to measure reward hacking dynamics. We train a Gemini~2.5 Flash-class policy with a frozen, weaker Gemini~2.5 Flash Lite judge, comparing a single-player RLAIF baseline against debate. While the baseline quickly hacks the judge, debate maintains judge performance throughout training, leading to a higher peak validation accuracy (45\% performance gap recovered) that persists through many RL steps. Additional experiments show that: 1) further weakening the judge leads to faster hacking, but this can be compensated by adding an additional debate round; 2) debate incentives override prompted misalignment; 3) RL using an LLM judge has a smaller train/validation reward gap than RL from verifiable rewards; 4) learning to critique to convince the judge using ground truth labels is possible but slow. Taken together, our results are a positive update on the feasibility of debate, while highlighting that balancing multi-agent training is critical: without player constraints, adversarial training risks defaulting to critic judge-hacking. We show that critique word limits (effective up to 150 words) successfully balance the game and avoid judge hacking, though this introduces a trade-off by restricting critic expressive clarity.

---


### 105. [Preference Is Not Intervention: The Structure and Stability Boundaries of Reader-Specific Evidence Utility](https://arxiv.org/abs/2608.17781)

**<font color=#1a73e8>作者：</font>** Shi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ML systems increasingly condition decisions on downstream model identity, but this is useful only if model-specific differences form reusable structure rather than input-local interactions. We test this in retrieval-augmented generation (RAG), where evidence utility can be measured under controlled interventions. Holding query, evidence, task, scoring, and intervention fixed, nine readers disagree on effect sign in 33\% of jointly affected cells; reader$\times$query interaction explains 29.8\% of utility variance versus an 8.4\% permutation null; and self-selected evidence improves F1 by $+0.031$ ($t=3.39$). We then ask the sharper question: \emph{which components of this heterogeneity are stable reader properties across queries?} Separating three measurable objects---evidence \emph{activity}, \emph{ordinal preference}, and \emph{conditional signed direction}---we find ordinal reader geometry stable across four independent settings (split-half $\rho=0.60$--$0.83$): leave-one-out interventions, PRISM preferences, RAMDocs, and RAGuard. Signed geometry is task-bounded: weak in open-ended QA (0.14, 0.35), especially for misleading and irrelevant evidence, but strong in binary fact-checking (0.75) with no significant ordinal gap, though still below its sparsity-matched ceiling. Sparsity, decoding noise, and metric artifacts do not explain the main ordinal--signed gap. Finally, stable ordinal similarity fails to predict cross-reader intervention transfer (oracle-distance $\rho=-0.27$; regret reliability $-0.28$). Reader-specific utility exists, but preference is not intervention: stable ranking similarity does not license transfer of help/harm decisions.

---


### 106. [TraceSQL: Traceable Answerability Estimation for Reference-Free Text-to-SQL Verification](https://arxiv.org/abs/2608.17795)

**<font color=#1a73e8>作者：</font>** Neelesh Kumar Shukla, Debasmita Panda, Srutanik Bhaduri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems are commonly evaluated using ground-truth SQL queries or reference execution results, but such supervision is unavailable at inference time in real-world deployments. This creates a critical verification problem: given only a user question, database context, and generated SQL, can a system estimate whether the generated query is likely to correctly answer the question? Recent approaches use LLMs as judge or specialized agents to inspect generated SQL, but their decisions can be difficult to trace. Outcome Reward Models (ORMs) address this by learning from execution-labeled candidate SQLs and assigning correctness scores to unseen queries, yet they still provide limited visibility into the signals behind each verification. To address this limitation, we propose TraceSQL, a lightweight and traceable verification model built on explicit diagnostic features. TraceSQL combines 67 features capturing question ambiguity, question requirements, question-schema-SQL consistency, SQL structure, and intent alignment. These signals remain available for examining which factors influence each prediction and for tracing decisions back to diagnostic evidence. On BIRD development databases, TraceSQL achieves 66.47% F1 and 64.48% ROC-AUC, compared with 61.87% F1 and 58.26% ROC-AUC for the GradeSQL-7B ORM baseline on the same generated-SQL evaluation. Feature attribution further shows that the model relies on both semantic grounding and deterministic SQL-structure signals. These results show that SQL verification can be performed with a lightweight learned model while retaining feature-level evidence for inspecting and diagnosing its predictions.

---


### 107. [StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End Workflows](https://arxiv.org/abs/2608.17800)

**<font color=#1a73e8>作者：</font>** Liya Zhu, Xin Ma, Tao Liu 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models(LLMs) and agents have substantially improved the ability of AI systems to execute complex tasks. Yet existing benchmarks largely rely on researcher-selected tasks, leaving uncertain whether such progress extends to the work that real-world users actually demand from AI systems. We introduce \textbf{StartupBench}, an E2E agent benchmark grounded in market-validated AI startup products. Rather than defining tasks from pre-defined assumptions about useful agent capabilities, we systematically study AI products with demonstrated adoption, together with their product workflows and users, to identify real-world tasks for which AI has established practical demand across diverse professional domains. We translate these workflows into complete deliverable-oriented tasks and evaluate them with fine-grained rubrics capturing their complex requirements. Across representative models evaluated under a unified agent harness, even the strongest model successfully completes only approximately 30\% of StartupBench, despite making substantial partial progress on many tasks. Further analysis identifies aspects like complex instruction following and domain-specific expertise as major sources of failure. Our results reveal that many market-validated workflows remain beyond the reliable capabilities of current general-purpose agents, establishing StartupBench as an empirical measure of progress toward E2E completions of real-world user tasks.

---


### 108. [Fourth-Moment Geometry of Rademacher Sums](https://arxiv.org/abs/2608.17802)

**<font color=#1a73e8>作者：</font>** Peigan Gao, Jian Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Let $\varepsilon_1,\ldots,\varepsilon_n$ be independent Rademacher signs and let $a=(a_1,\ldots,a_n)\in\R^n$ satisfy the normalization below. For the normalized Rademacher sum, we determine how its higher moments depend on the fourth-order mass. Combining a sharp fixed-q moment envelope with a separate argument below the convexity threshold gives the Gaussian stability inequality for the full range $p\geq4$ of this linear-in-q bound. The same fourth-order framework determines the sharp finite dimensional $L_p/L_4$ Khintchine constant for $p\geq5$, with the flat coefficient vector as the extremizer. These results settle the conjectures of Jakimiuk and of Barański, Murawski, Nayar, and Oleszkiewicz stated below. We also prove Jakimiuk's conjectured quadratic stability estimate at $p=3$. The resulting bounds retain information about sparsity and effective dimension, with applications to Rademacher random projections and randomly signed errors; those applications are not developed further here. Their Laplace-transform form also gives coefficient-sensitive tail bounds. The proofs are discovered with substantial assistance from ChatGPT 5.6 Sol.

---


### 109. [An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning](https://arxiv.org/abs/2608.17804)

**<font color=#1a73e8>作者：</font>** Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, anti-refusal shaping, rubric-based broad answering, and an explicit refusal contrast, with and without SFT warm-up. The experiments show that optimization success is not equivalent to behavioral unlearning: RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics can point to different conclusions. We trace these disagreements to reward-hacking endpoints, policy-support limits in GRPO, benchmark probes that miss endpoint changes, and rewards that can select broad-topic answering with low semantic leakage during optimization.

---


### 110. [Whether LLMs Can Navigate Beliefs and Facts Depends on How You Phrase It](https://arxiv.org/abs/2608.17809)

**<font color=#1a73e8>作者：</font>** Quang Minh Nguyen, Luis Frentzen Salim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans naturally form and express beliefs in daily communication, e.g., "I think the answer is 3" or "I suppose that's right." Such beliefs inevitably intertwine with fact and knowledge, making the ability to handle them in tandem desirable for large language models (LLMs), as they are increasingly deployed in user-facing settings. Prior work showed that even capable LLMs exhibit a systemic weakness in acknowledging user beliefs grounded in incorrect information. We extend this evaluation to 10 LLMs across 18 epistemic expressions and find that the size and direction of the weakness depend on the verb used to express the belief, with the accuracy gap between factual and false information ranging from +50% on "I vaguely remember" to -14% on "I seriously doubt". We further show that the phenomenon stems from task confusion: models default to fact-checking the underlying claim, overriding the user's stated belief; chains of thought that explicitly fact-check show lower accuracy on false information than those that do not; and a single instruction can reverse the failure across verb families. Mechanistically, models attend more to false beliefs they fail to confirm, but suppressing this attention at decoding time recovers accuracy only partially and only in some models, calling for future work on intervention methods. Our findings clarify prior results and show how fact-checking, a generally desirable behavior, can interfere with belief tracking in LLMs. Our code is available at this https URL.

---


### 111. [Interpretable Humans, Alien LLMs: Expert Analysis of Latent Structures in Assessment Responses](https://arxiv.org/abs/2608.17810)

**<font color=#1a73e8>作者：</font>** Alona Strugatski, Licol Zeinfeld, Jason Cooper 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evaluation of large language models (LLMs) relies heavily on human-designed assessments, implicitly assuming that AI and humans employ similar underlying cognitive constructs. Challenging this assumption, we investigate whether the latent factors governing LLM performance carry the same substantive, human-interpretable meaning as the cognitive constructs governing human learners. Using responses from humans and six LLMs across quantitative reasoning and chemistry assessments, we conducted Exploratory Factor Analysis (EFA) separately for both groups. Subject-Matter Experts (SMEs) then blindly evaluated the resulting factor graphs to ascribe pedagogical meaning to the emerged constructs. SMEs successfully interpreted most of the human-derived factors. Conversely, they could not ascribe meaning to any LLM-derived factors in quantitative reasoning and interpreted only half of the LLM factors in chemistry. By combining data-driven EFA with blind expert interpretation, this framework shows that LLMs frequently operate on statistically opaque mechanisms distinct from human reasoning.

---


### 112. [MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure](https://arxiv.org/abs/2608.17823)

**<font color=#1a73e8>作者：</font>** Sumit S. Shevtekar, Chandresh K. Maurya, Gourab Sil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Powered two-wheeler riders face critical safety challenges in low- and middle-income countries, yet limited studies exist on how cognitive stressors such as Time Pressure influence collision risk. To address this gap, we introduce a large-scale dataset of over 129,000 labeled multivariate time-series sequences from 153 simulator rides by 51 participants under No, Low, and High TP, capturing 64 features across vehicle dynamics, control inputs, proximity, and behavioral violations. Building on this dataset, we propose MotoSafety, a novel edge-AI architecture grounded in the Learned Temporal Importance principle. MotoSafety achieves 94.97% accuracy and 99.33% ROC AUC, outperforming ten baselines, including TimesNet and LLM4TS, and achieves 0.039 MSE and 0.094 MAE for forecasting (4.4x lower error than Time-LLM and iTransformer). With only 1.15M parameters and 0.135 ms latency, it is suitable for edge deployment on low-cost CPU hardware. Using ground truth TP as an inductive bias improves accuracy from 94.09% to 94.97%, while predicted TP achieves 94.82%. Using only 21 IMU+GPS features, it achieves 93.91% accuracy, indicating practical deployment. Beyond PTW safety, the architecture shows better transferability to human activity (97.66%) and clinical (99.65%) domains. This lightweight framework advances PTW collision risk assessment, supporting the Safe System Approach for Intelligent Transportation Systems.

---


### 113. [From Global Benchmarks to Local Evaluations: Benchmarking LLMs for the German Public Sector](https://arxiv.org/abs/2608.17827)

**<font color=#1a73e8>作者：</font>** Camilla Dalerci, Thilo Michael, Robin Schaefer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public institutions face a persistent challenge in selecting LLMs suited to their specific context. Existing benchmarks, however, are of limited use as they primarily reflect English-language and US-centric settings, and often only evaluate task performance. In this paper, we present first results of MÖVE, a holistic evaluation framework for the German public sector, examining three rarely considered governance dimensions: energy consumption, provider transparency, and knowledge of German-party positions. Our results reveal significant trade-offs, with no single model excelling across all dimensions: estimated energy consumption varies more than 60-fold and is not explained by model size alone, information disclosure varies systematically across providers, and European models do not exhibit stronger knowledge of German party positions. Model selection for public institutions thus cannot rely on performance rankings alone. Instead, evaluations should also reflect the governance requirements of the deployment context.

---


### 114. [The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges](https://arxiv.org/abs/2608.17829)

**<font color=#1a73e8>作者：</font>** Maosen Zhang, Jianshuo Dong, Boting Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a more accessible ``tell'' before decoding. We propose LeakGauge, which probes this response by appending a suffix that gauges leakage behavior and mapping its prefill token probabilities to an attack-risk score. While a direct gauge uses the initial tokens of confidential content, we find that a content-agnostic one that verbalizes leakage behavior yields more robust signals. Across 11 LLMs, including GLM-5.2 (753B) and Kimi-K3 (2.8T), LeakGauge reaches an AUROC range of 0.944--0.996 on unseen attacks. The signal remains stable when the content changes language or the attack shifts from verbatim to semantic disclosure. By activation-steering interventions, we further show that the risk score is sensitive to an internal leakage-related direction, relating the observable signal to the model's internal representation. In addition, LeakGauge enables an input detector with fewer than 0.5K extra parameters and added latency of 10.34 ms. Code: \href{this https URL}.

---


### 115. [AdaLens: Interactive Storyline for Monitoring and Steering Long-Running Agentic Data Analysis](https://arxiv.org/abs/2608.17834)

**<font color=#1a73e8>作者：</font>** Yangtian Liu, Yan Miao, Shuhan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are pushing data science toward increasingly autonomous and agentic workflows, with recent systems already supporting multi-step and long-running analyses. As these workflows become more autonomous, conventional interfaces no longer provide adequate support for two critical requirements: observability for understanding an agent's evolving reasoning and evidence, and steerability for redirecting low-value directions or deepening promising ones during execution. Existing interactive approaches improve process visibility and open intervention points, but they remain largely designed for discrete, turn-by-turn exchanges rather than the parallel branches and evolving decision structures of long-running agentic analysis. We study this need as interactive oversight in long-running agentic data analysis and present AdaLens, an interactive system for monitoring and steering ongoing runs. AdaLens combines a storyline-based representation that unifies analytical plans, execution progress, intermediate findings, and data-column involvement with steering interactions grounded in these analytical elements for directional guidance and execution control. We evaluate AdaLens through two case studies and a user study, examining how it supports analysts in monitoring and steering long-running agentic data analysis.

---


### 116. [Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs](https://arxiv.org/abs/2608.17836)

**<font color=#1a73e8>作者：</font>** Roman Maksimov, Vladimir Aletov, Vladimir Solodkin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are granted increasing autonomy, it is essential to investigate methods that can induce unsafe behavior. We propose a novel white-box attack inspired by locate-then-edit approaches from the field of Knowledge Editing. Our choice is motivated by the observation that models edited with such schemes tend to assign unusually high prediction probabilities to the edit target, a property that is particularly advantageous when designing attacks. We modify the editing framework by incorporating as- sociative knowledge retrieved from the model, thereby extending constraint removal to an entire thematic category rather than being limited to prompts from a predefined dataset. Experiments with various archi- tectures demonstrate improved attack effectiveness over competing methods without dealing critical damage to general model performance.

---


### 117. [Encoded but Not Actionable: Auditing the Decode-Generate-Steer Gap in Frozen LLMs for Geometric Constraints](https://arxiv.org/abs/2608.17843)

**<font color=#1a73e8>作者：</font>** Man Liang, Xinzhao Cheng, Faizan Wajid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong performance on structured reasoning tasks, but what they encode and whether it informs model behavior remain unclear. We investigate this question through geometric reasoning, using parametric CAD constraints as a controlled testbed for separating local pairwise relations from sketch-level constraint status. By probing the hidden states of six frozen decoder-only LLMs, we examine four properties: linear decodability, forced-choice generation, activation-level influence, and behavioral steerability. Pretraining substantially improves the decoding of local geometric relations, and this advantage persists after accounting for positional cues with shuffled-order controls. In contrast, sketch-level DOF status is already highly decodable from randomly initialized representations and improves only modestly with pretraining, indicating that much of its probe performance is available without learned weights. Further analyses show that decodable information is not always actionable. Generation often fails to express this information, and on the two intervention-tested backbones, activation-restoration effects at the patched entity position vanish while decodability persists across depth. Mean-difference steering also does not reliably control outputs. These results show that decodability, generation, activation-level influence, and steerability can diverge in the tested setting. The audit provides a controlled way to distinguish failures to encode geometric structure from failures to express or control encoded information.

---


### 118. [ARASH: Adaptive Retrieval And Shot Selection for Tabular Prediction](https://arxiv.org/abs/2608.17856)

**<font color=#1a73e8>作者：</font>** Samirasadat Jamalidinan, Yue Xu, Kazem Cheshmi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tabular prediction is a critical task across numerous applications. The recent success of large language models has sparked various approaches for adapting them to the tabular domain. A prevalent strategy involves training or fine-tuning specialized Tabular Foundation Models (TFMs) such as TabPFN. However, TFMs require substantial computational resources, and frequent model retraining is often impractical. In-context learning (ICL), specifically, few-shot prompting, offers a resource-efficient alternative to enhance performance. Yet, identifying the most relevant rows to serve as shots remains a challenge for tabular data. This paper introduces ARASH (Adaptive, query-specific Retrieval And Shot selection), a method that improves TFM efficiency by selecting optimal shots based on local neighborhood analysis within the training set. Our results demonstrate that ARASH reduces the prompt length and memory usage of TabPFN by 1261.5$\times$ and 2.56$\times$, respectively, while providing comparable accuracy.

---


### 119. [BayesPrompt: human readable prompts that make sense](https://arxiv.org/abs/2608.17866)

**<font color=#1a73e8>作者：</font>** Franky Kevin Nando Tezoh, Ali Hussaini Umar, Alessandro Laio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reconstructing prompts that can elicit a desired answer or behaviour in an LLM is an open and important research topic. Optimisation methods which aim at minimising the perplexity of a given answer, however, consistently yield so-called pseudoprompts, unintelligible strings of tokens which can lack human interpretability. We argue that this is a consequence of the ill-posedness of the prompt optimisation task. By reframing the task as a Bayesian posterior inference over prompts, we propose an efficient algorithm to sample prompts which are both efficient (in terms of perplexity) and human readable. We compare our approach with state of the art alternatives showing on a real data set a marked improvement over a range of metrics.

---


### 120. [Improving Complex Moiré Removal with Generative Supervision](https://arxiv.org/abs/2608.17883)

**<font color=#1a73e8>作者：</font>** Xinyang Gu, Zhilu Zhang, Honglei Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The availability of high-quality paired data is essential for training learning-based image demoiréing models. However, it remains challenging for existing datasets to encompass the complex moiré patterns captured in uncontrolled real-world scenarios. Such degradations typically manifest as large-scale, multicolored moiré patterns. Moreover, these patterns frequently occur in images for which clean counterparts are difficult to obtain, such as photographs acquired from public displays or existing online resources. In this work, we propose a novel data engine designed to improve the removal of complex moiré patterns by generating training supervision. Specifically, we initially collect real-world images containing complex moiré patterns and localize the corresponding screen regions. Multiple image-conditioned generative foundation models are subsequently deployed to produce candidate references. To establish reliable supervision, these candidates are subjected to patch-level quality control to filter and select the optimal results. Based on this systematic paradigm, we construct the WildMoiré dataset, which contains 6.8K moiré-GT training pairs. For evaluation, we additionally build an independent test set comprising $\sim$250 pairs with captured clean ground truth. Extensive experiments on ESDNet, SDXL, and Qwen-Image-Edit demonstrate that the proposed generative supervision consistently improves the performance of complex moiré removal.

---


### 121. [BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models](https://arxiv.org/abs/2608.17895)

**<font color=#1a73e8>作者：</font>** Liubov Chubarova, Alexandra Kuleshova, Daniil Volkov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have made significant strides in visual comprehension, their ability to reason about text-dense, professional documents remains incompletely evaluated. Existing benchmarks emphasize information extraction, require external domain knowledge, or cover professional documents only as one of many settings. They are also largely English- or Chinese-centric, leaving other languages and Russian, in particular, substantially underrepresented. To address these limitations, we introduce BEAR-Bench (Bilingual Enterprise and Academic Reasoning), a self-contained, complex English-and-Russian benchmark comprising 1000 human-annotated questions based on text-rich business and scientific documents. We evaluate 16 proprietary and open-weight MLLMs, including Gemini 3.1 Pro and Qwen3.5-397B, on BEAR-Bench and observe clear headroom even for the strongest systems. Finally, we use the resulting model outputs to compare existing hallucination detection methods, evaluating not only how often models fail on BEAR-Bench but also how reliably those failures can be identified.

---


### 122. [CABLE: Extending the Reach of Memory Retrieval via Complementary Antecedent-Based Linking and Expansion](https://arxiv.org/abs/2608.17911)

**<font color=#1a73e8>作者：</font>** Zheling Tan, Jin Gao, Dequan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents operate across structured workflows and sessions, preserving long-term history does not ensure that later contexts can recover relevant evidence through a bounded memory interface. We study this evidence-reachability problem in long-term conversational memory, where retrieval still relies heavily on semantic similarity. This works well for topical recall, but it often misses earlier experiences, plans, or motivations that are semantically distant from the later events they help explain. Existing memory graphs provide cross-memory structure, yet links driven mainly by semantic overlap can duplicate what the host retriever already recovers. We argue that link construction should instead prioritize a sparse set of retriever-complementary associations. We present CABLE (Complementary Antecedent-Based Linking and Expansion), a plug-in augmentation that constructs links designed to extend the host retriever's direct semantic reach. For each new memory, CABLE generates antecedent-oriented queries, retrieves prior memories, subtracts candidates in the direct semantic neighborhood, and verifies the remainder before adding the accepted complementary associations into a sparse directed graph. At retrieval time, CABLE expands the host system's retrieved seeds along these links to surface implicit supporting evidence. We evaluate CABLE with A-MEM on LoCoMo and MA-LongMemEval, and further integrate it into SimpleMem and Mem0g on LoCoMo, using Qwen3.5-27B, DeepSeek-chat, and GPT-4o-mini. CABLE yields higher mean LLM-judge scores in every evaluated system-level setting, with the largest gains in categories where useful evidence is distributed across memories or sessions, including open-domain, multi-session, and preference-oriented questions. These results support prioritizing sparse, reasoning-relevant associations that complement rather than duplicate the host retriever.

---


### 123. [Analysis of Types of Inquiries in Student-AI Interaction: A case study of two CS2 tasks](https://arxiv.org/abs/2608.17919)

**<font color=#1a73e8>作者：</font>** Matin Amoozadeh, Amin Alipour  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background and Context: Question and inquiry are integral parts of knowledge seeking and learning. Despite their importance, students tend not to ask enough questions in the classroom. However, studies have shown that students interact extensively with generative AI systems for learning and problem solving.
Objective: In this paper, we seek to better understand the types of questions that students ask AI systems, and how those questions evolve during problem solving and across tasks.
Method: We use the Graesser et al. taxonomy to classify students' inquiries into 18 types. We develop a few-shot learning approach to automatically classify students' interactions with AI into these categories. We use this system to analyze 830 interactions of CS2 students across two programming tasks.
Findings: Our results suggest that a small subset of question types accounts for the majority of student inquiries, and that the types of questions students ask change substantially as the task progresses.

---


### 124. [PerFact: Perception-Derived Fact Prompting for 3D Brain MRI Report Generation](https://arxiv.org/abs/2608.17926)

**<font color=#1a73e8>作者：</font>** Jianyu Sun, Zhenxuan Zhang, Guang Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation has matured almost entirely on 2D chest radiographs, where the default route to better reports is a larger backbone or a pre-training one on medical data. We revisit that assumption on 3D multi-sequence brain MRI, a volumetric multi-disease regime, and find that the model is not the lever. Zero-shot medical and radiology vision-language models transfer poorly to brain MRI, with chest radiograph specialists failing most conspicuously, and five backbones fine-tuned identically across three model families and an order of magnitude in scale differ only marginally. What determines the quality of the report is the information injected into the prompt. We delegate perception to upstream 3D segmentation and classification, serialize their outputs into a structured fact sentence, and prompt a LoRA-adapted vision-language model with it; we call this \textbf{PerFact}. In a controlled study that fixes the backbone, data split, target reports, and adaptation while varying only the injected grounding, perception-derived facts outperform retrieved prior reports, retrieval becomes redundant once facts are present, and end-to-end predicted facts remain effective without any ground-truth annotation at inference. The residual gap between predicted and oracle facts is explained by the granularity of the facts rather than by the generator. Closed-ended visual question answering comes at no measurable cost to report quality, though the grounding source has little effect on it. On 3D brain MRI, grounding information, not model choice, is the dominant controllable factor in report quality.

---


### 125. [SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis](https://arxiv.org/abs/2608.17931)

**<font color=#1a73e8>作者：</font>** Shicheng Ma, Wenqian Cui, Irwin King  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI have revolutionized speech processing, yet effective speech understanding requires discerning not just what is said, but how it is said. Speech Sentiment Analysis plays a critical role in decoding these paralinguistic cues for diverse real-world applications such as recruitment and customer service. However, existing Speech Sentiment Analysis research faces two primary limitations. First, dominant approaches rely on text-centric pipelines that cascade Automatic Speech Recognition with text analysis. This process inevitably discards essential acoustic features like prosody and tone, failing to capture attitudinal meanings in acoustically ambiguous utterances. Second, current benchmarks suffer from a mismatch in label granularity, prioritizing basic emotions (e.g., happy, sad) over the nuanced interpersonal stances (e.g., confident, impatient) necessary for social sensitivity. To address these limitations, we propose a novel dataset, SpeechSense, for fine-grained speech sentiment analysis. Specifically, we define a specialized 8-class taxonomy of interpersonal stances detectable primarily through prosodic cues beyond lexical content alone. We then construct a curated dataset based on this taxonomy, built from high-fidelity speech synthesis and rigorous human validation. Comprehensive experiments across multi-modal LLMs, text-only LLMs, and speech encoders demonstrate that models with acoustic access consistently outperform text-only baselines. These results empirically validate the primacy of acoustic cues in detecting subtle speaker attitudes, highlighting the necessity of SpeechSense. Dataset and supplementary materials are available at this https URL.

---


### 126. [EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection](https://arxiv.org/abs/2608.17933)

**<font color=#1a73e8>作者：</font>** Lei Jiang, Ye Wei, Xinyu Xi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-series change-point detection. EvoTS-Agent first performs curated exploratory data analysis to characterize dataset properties and initialize candidate detection models. It then evolves executable experiment trajectories through three complementary operators: \textit{Revision} exploits the current best solution, \textit{Alternative Strategy} explores fundamentally different modeling directions when progress stagnates, and \textit{Recombination} synthesizes complementary evidence from high-performing trajectories. Validation feedback guides trajectory evolution throughout the search, enabling the agent to adapt its detection pipeline to the statistical characteristics of each dataset while preserving reliable optimization. Experiments across four benchmark datasets demonstrate that EvoTS-Agent consistently outperforms existing LLM-based agents while maintaining a 100\% execution success rate across all evaluated backbone LLMs.

---


### 127. [Grading Needs a Rubric, Not Intelligence](https://arxiv.org/abs/2608.17938)

**<font color=#1a73e8>作者：</font>** Jhen-Ke Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models can grade open-ended examination answers as reliably as substantially more expensive models when they grade against an explicit rubric. We test this claim as the design principle behind any-to-bench: a frontier model reads source documents once, at ingestion, to extract each question and its rubric; lower-cost models then perform all repeated grading work. We evaluate six cost-efficient model configurations from two model families at three reasoning-effort levels. Each configuration answers 24 open-ended examination questions, and each also grades every answer sheet three times, yielding 3,456 per-question grades. Scores depend overwhelmingly on the answer being graded: answer identity explains 95.6% of score variance, whereas judge identity explains only 0.2%. Raising a writer's reasoning effort moves earned scores by as much as 0.143 of full marks, while raising a judge's reasoning effort moves assigned scores by at most 0.006. Six frontier-tier judges, added as a check, reproduce these scores and are no more reliable as a panel. Two ablations then decompose the rubric on the same questions and answers. Removing its criteria and levels while keeping the official answer changes nothing measurable. Removing the official answer as well collapses reliability (ICC 0.888 to 0.628), inflates scores, and makes judge reasoning effort matter again. The rubric is what decouples grading from judge intelligence, and within the rubric the official answer does nearly all the work. We find no evidence of length preference or same-family preference under rubric-anchored grading.

---


### 128. [Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation](https://arxiv.org/abs/2608.17941)

**<font color=#1a73e8>作者：</font>** Zhizhao Liu, Zhiliang Tian, Xi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but relies on costly rollout exploration. Assigning the same exploration budget to samples with different difficulty levels is inefficient: easy samples may receive redundant rollouts, whereas difficult but learnable samples may receive too little exploration. Existing adaptive schedulers address this mismatch through curriculum-based sample selection or non-uniform rollout allocation based on estimated sample difficulty. However, obtaining reliable online difficulty estimates remains challenging: dedicated probing adds substantial generation overhead, whereas history-based estimators face a cold start with no initial observations and stale feedback, and typically ignore relations among samples. To address these limitations, we propose a plug-and-play graph-based online difficulty estimator that shares rollout feedback across related samples and continuously updates their difficulty estimates, mitigating cold start and staleness without dedicated probing. Specifically, we first construct a difficulty-aware sample graph based on semantic and reasoning similarities. Based on this graph, we introduce latent difficulty states and use a Potts prior to encourage neighboring samples to share the same state. We then employ a state-level Beta-Binomial model to aggregate the rollout outcomes associated with each state. Finally, we use an online mean-field variational algorithm to continuously update the latent-state assignments and state-level difficulty as new feedback arrives. Our framework can be integrated into sample-selection and rollout-allocation schedulers, enabling difficulty-adaptive exploration without dedicated probing. Experiments across multiple base models, RL schedulers, and benchmarks demonstrate that our framework achieves better performance.

---


### 129. [Procedural Content Metageneration via Program Search and Continual Abstraction Discovery](https://arxiv.org/abs/2608.17947)

**<font color=#1a73e8>作者：</font>** Matthew Siper, Ahmed Khalifa, Julian Togelius  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can generate executable programs, which makes it possible to search directly over procedural content generators rather than individual levels. We study this approach in Sokoban, Zelda, Dangerous Dave, and Lode Runner. Each run evolves complete Python generators through language-model mutation and crossover. We introduce Continual Abstraction Discovery, or CAD, which extracts reusable primitives from high-fitness programs into a run-specific helper module. A 2x2 experiment crosses CAD with access to a fixed hand-written domain API. The completed data set contains 160 complete runs, with at least ten 50-generation runs in every cell. CAD raises mean final best fitness in all eight domain and API comparisons. Across all CAD runs, learned libraries are adopted by most later programs and repeatedly rediscover validation, reachability, and structural utilities. These results support that discovering reusable primitives improves evolutionary program search for content generators.

---


### 130. [SIGMA: SHAP-Guided Implicit-Trajectory Generation for Metadata-Free LLM-Based AutoFE](https://arxiv.org/abs/2608.17948)

**<font color=#1a73e8>作者：</font>** Xuan Zheng, Kento Uchida, Shinichi Shirakawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent research has leveraged Large Language Models (LLMs) to enhance Automated Feature Engineering (AutoFE) through semantic descriptions and trajectory-based prompting. However, there exist two challenges that limit their applicability and scalability in long-horizon optimization: (1) semantic metadata is unavailable in many practical settings, and (2) trajectory accumulation increases the risk of exceeding the context window, while without it, the generation process can become unstable, leading to becoming stuck in the local optima and a high duplicate rate of generated features. To this end, we propose a SHAP-enhanced Implicit-trajectory Generation for Metadata-free AutoFE (SIGMA), a scalable constant-context optimization framework. SIGMA leverages SHAP values to provide task-aware signals for guiding group feature generation instead of semantic information. In addition, we adopt an EXposed-feature Implicit Trajectory (EXIT) approach, where the exposed features in the prompt implicitly represent the trajectory. Empirical results demonstrate that SIGMA achieves performance comparable to the state-of-the-art (SOTA) LLM baselines with a nearly constant prompt length. Notably, EXIT significantly reduces the duplicate ratio of generated features from 37.2% to 6.8%. At the same time, SIGMA matches traditional SOTA performance with only 5.4 features on average, demonstrating substantial efficiency gains in feature utilization.

---


### 131. [Do Large Language Models Play Six Degrees of Separation? Measuring Topological Compression in Long-Context Manifolds](https://arxiv.org/abs/2608.17950)

**<font color=#1a73e8>作者：</font>** Md. Faiyaz Abdullah Sayeedi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate remarkable multi-hop reasoning capabilities over long contexts, yet the internal mechanisms enabling these distant cognitive leaps remain poorly understood. Traditional attention-based interpretability often fails to capture true semantic proximity due to routing artifacts like attention sinks. In this paper, we bypass attention weights to directly analyze the dynamic geometry of the hidden state manifold, proving that deep LLM latent spaces natively organize into Small-World networks. By sparsifying the continuous similarity matrices of long-context representations into unweighted graphs, we trace the connectivity between highly disjoint semantic anchors across two distinct architectures. Our findings reveal a sharp topological phase transition: while early syntactic layers remain entirely fractured, deep reasoning layers abruptly compress massive conceptual distances into highly navigable pathways strictly bounded by the "Six Degrees of Separation" limit (=< 6 semantic hops). Furthermore, we demonstrate the practical efficacy of this framework by applying it to zero-shot hallucination detection within Retrieval-Augmented Generation (RAG) using the RAGognize dataset. We show that factually grounded generations maintain structural integrity with their source context (approximately 3 hops), whereas hallucinations induce severe topological collapse. Ultimately, this work mathematically formalizes how transformers execute abstract reasoning and provides a novel, strictly geometric signature for evaluating factual reliability.

---


### 132. [An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models](https://arxiv.org/abs/2608.17956)

**<font color=#1a73e8>作者：</font>** Javier Aguilar Martín  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On three hybrid instruments the accepted mode-blind model is exploited: the planner is pinned at the mode boundary at a regret of nearly the whole attainable return. We prove a localization budget, valid at boundary points: models with Lipschitz constant at most L differing by eta at a point disagree above tolerance eps on a region of volume at least kappa((eta-eps)/L)^(d+m); the discontinuous reset modes studied pay no such budget. With real LLM synthesis, GPT-5.x repairs an omitted 1D clamp in 105 of 111 mode-containing draws -- every attempt exact on 50 of 56 instrument-stream blocks (95% CI [0.781, 0.960]). On 2D regions no artifact recovers the rule (0/156); eight targeted interventions leave the failure in place, and positive controls locate it: a located rule is not induced, while given form and location the constants follow exactly. A version-space certificate proves identification is class-relative: at the widest dose the declared fit succeeds in 20/20 blocks and every sample-consistent circle is within tolerance in 18/20. We prove a class of entry rules exactly consistent with every sample yet harmless at play, so identifiability is a measurable property of the instrument. Re-scoring all 1034 artifacts on independent samples confirms acceptance certifies sample consistency and no more: where the gate is provably informative it covers about two percent of the exploited planner's queries.

---


### 133. [COMA: A Compositional Misleading Attack Class on Security-RAG, and a Causal Counterfactual Defense](https://arxiv.org/abs/2608.17960)

**<font color=#1a73e8>作者：</font>** Chinmay Gondhalekar, Urjitkumar Patel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Every document a security copilot retrieves can be true, instruction-free, and non-contradictory --- and the copilot can still be driven to assess a critical, exploitable vulnerability correctly and then recommend a remediation that leaves it open. We study this failure in retrieval-augmented generation (RAG) backing analyst-facing copilots in Security Operations Centers, and identify a class of attacks, \emph{\compmis{}} (COMA), in which every adversarial document is factually correct, instruction-free, non-contradictory, and distributionally benign --- yet the answer is misled by their \emph{composition}. We realize \compmis{} through \emph{action-corruption}, which steers a correctly-diagnosed vulnerability toward an inferior remediation, and \emph{verdict-flip}, which destabilizes the exploitability verdict via an undecidable reachability chain. Action-corruption bites all five tested models --- including frontier reasoning models --- on every run, on two synthetic domains and a real CVE (CVE-2021-33813); verdict-flip bites stochastically, decreasing with model capability but never vanishing. A single principle governs both: the attack succeeds when the disambiguating fact must be \emph{inferred} rather than \emph{read}. We propose \ccd{} (Causal Counterfactual Defense), an audit that measures the leave-one-out causal influence of each retrieved document and flags answers whose influence concentrates on low-trust documents. \ccd{} localizes the attack to attacker-controlled documents with no false positives on four benign multi-document controls; an adaptive influence-spreading adversary is caught by an \emph{aggregate} variant. We release attack seeds and a \ccd{} reference implementation.

---


### 134. [Too Sure to Be Safe: Model Calibration for Reliable Log Anomaly Detection](https://arxiv.org/abs/2608.17965)

**<font color=#1a73e8>作者：</font>** Bin Li, Dongdong Wang, Siyang Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online log anomaly detection is critical for maintaining the reliability of large-scale computing systems. Although recent language model-based log anomaly detectors achieve strong detection performance, their confidence estimates remain poorly calibrated. We show that these detectors frequently assign excessive confidence to incorrect predictions, particularly for anomalous logs under severe class imbalance. Moreover, confidence on erroneous predictions remains persistently high even when conventional calibration metrics indicate good calibration, creating a critical reliability gap for operational monitoring systems. To address this issue, we propose Log Reconstruction and Distance (LoRD), a lightweight post-hoc calibration framework for reliable log anomaly detection. LoRD learns prediction-route-specific reliability models from latent representations of correctly classified validation samples and estimates prediction reliability through route-wise reconstruction distances. Based on the estimated reliability, LoRD selectively recalibrates high-risk predictions to suppress overconfident errors while preserving reliable predictions. Extensive experiments on four large-scale log benchmark datasets and multiple language model-based detectors demonstrate that LoRD consistently improves confidence reliability and substantially reduces overconfident anomaly-related errors without sacrificing anomaly detection performance.

---


### 135. [LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching](https://arxiv.org/abs/2608.17973)

**<font color=#1a73e8>作者：</font>** Jinshan Liu, Haoran Qin, Xiaobing Tu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in image and video generation, yet the high computational cost of iterative sampling remains a critical bottleneck for practical deployment. Feature caching has emerged as a promising acceleration paradigm by reusing or predicting intermediate features across timesteps. However, existing training-free methods apply uniform prediction strategies that cannot adapt to the heterogeneous feature dynamics, causing significant quality degradation under high acceleration ratios. We propose LinCa, a feature caching framework based on learnable invertible networks. LinCa decomposes cached features into sub-components with distinct continuity properties via a lightweight invertible network and applies differentiated prediction orders matched to each component. The strict invertibility guarantees lossless reconstruction back to the original feature space, forming a unified Decompose-Predict-Reconstruct pipeline. By training separate predictors for different models and timestep segments, LinCa adapts to heterogeneous feature dynamics. Experiments on FLUX, Qwen-Image, and HunyuanVideo demonstrate that LinCa, with less than 0.2% additional parameters, significantly outperforms existing methods and maintains near-lossless quality at 5-7x speedup. Code: this https URL

---


### 136. [When Writing Style Drifts: Benchmarking Authorship Verification under Distribution Shifts in Genre, Time and the AI-Era](https://arxiv.org/abs/2608.17979)

**<font color=#1a73e8>作者：</font>** Lotta Kiefer, Brisca Balthes, Christoph Leiter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship verification (AV) assumes that an author's writing style remains sufficiently stable to distinguish it from that of other writers. In practice, however, this assumption is challenged by distribution shifts caused by changes in genre, time, and AI-assisted writing. Existing AV benchmarks typically study these factors in isolation and focus predominantly on English, limiting our understanding of model robustness under realistic conditions. We introduce AVShift, the first German benchmark for systematically evaluating AV under multiple distribution shifts. AVShift comprises over 150,000 text pairs spanning three genres and 21 years, enabling controlled evaluation of cross-genre, temporal, and AI-era shifts within a unified framework. We benchmark representative feature-based, embedding-based, and LLM-based approaches. Our experiments show that fine-tuned LLMs generalize best across genres and benefit substantially from stylistically diverse training data. We further demonstrate that temporal drift is one of the strongest factors affecting AV, with performance degrading significantly as the time gap between documents increases. In contrast, we find no evidence of a measurable AI-era distribution shift within AVShift. Finally, our feature analysis reveals stylistic features that remain stable across genres, while their relative importance varies depending on the specific genre transition. We release AVShift and our code for future research.

---


### 137. [Recirculation](https://arxiv.org/abs/2608.17981)

**<font color=#1a73e8>作者：</font>** Michael C. Mozer, Shoaib Ahmed Siddiqui, Danny Sawyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We describe an inference-time architectural enhancement for off-the-shelf foundation models that markedly reduces perplexity and boosts accuracy across generation and reasoning tasks. Our approach incurs essentially no additional latency during generation, though it requires serial processing in the prefill phase. Motivated by the fundamental limitation that state updates in feedforward transformers are bounded by model depth, our technique, recirculation, introduces a specific form of recurrence that allows the model to act as a dynamical system and track belief states. We distinguish this technique from chain-of-thought computation---which is better reserved for complex inferences rather than basic state tracking---as well as from popular depth-recurrence techniques (looping) and the costly training of recurrent transformers. We also propose and evaluate an adaptive variant of recirculation which requires only light tuning of hyperparameters while freezing the original model weights. Relative to the off-the-shelf baseline, adaptive recirculation achieves remarkable gains on the Gemma3 family, including a 23% reduction in perplexity on a suite of datasets, a 21% increase in accuracy on GSM8k, and reliable improvements in accuracy on other downstream tasks. Our training-free approach succeeds by leveraging the model itself to inform architectural modifications, suggesting a route to architectural evolution guided by a trained network's properties rather than forced, arbitrary design choices.

---


### 138. [Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees](https://arxiv.org/abs/2608.17994)

**<font color=#1a73e8>作者：</font>** Sher Badshah, Ali Emami, Hassan Sajjad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Using LLMs as judges has become standard practice for evaluating model outputs at scale. This is particularly common for subjective, open-ended tasks such as assessing helpfulness or alignment, where no single reference answer exists. However, objective tasks introduce a distinct reliability challenge for reference-free LLM judging. In the absence of a reference answer, the judge evaluates factual correctness either through its parametric knowledge or through tool augmentation. Although the former enables efficient evaluation, the judge may hallucinate or lack sufficient evidence for its verdict. Conversely, tool augmentation can provide additional evidence but introduces extra computational cost and requires an appropriate mechanism to determine when and how that evidence should be used reliably. More importantly, neither approach alone provides formal control over the risk of accepted verdicts or guarantees their reliability at a specified level. We propose a risk-controlled framework that calibrates uncertainty thresholds on a held-out set so that the false discovery rate among accepted verdicts remains below a user-specified level~$\alpha$ with high probability, using finite-sample Clopper--Pearson intervals. When the parametric mode is not sufficiently confident, the instance is routed to a retrieval-augmented mode, where the judge gathers web evidence and re-evaluates the instance under a second calibrated threshold. The finite-sample guarantee carries over to this two-threshold routing without additional assumptions. Across open-domain QA benchmarks and judges of varying scales, the framework maintains the target error rate while achieving substantially higher coverage than single-mode baselines.

---


### 139. [AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation](https://arxiv.org/abs/2608.17995)

**<font color=#1a73e8>作者：</font>** Haoran Qin, Zhengan Yan, Shikang Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve high-quality generation but are costly due to iterative sampling. Dynamic-resolution sampling reduces early-stage cost by denoising at low resolution; however, uniformly upsampling all latent tokens at resolution transitions incurs redundant computation and may degrade fine-detail consistency. Existing partial upsampling strategies typically rely on local latent structure cues or single-step statistics, making it difficult to jointly capture token-text semantic relevance and token-wise representation dynamics across diffusion steps. We propose AViTS, an adaptive spatiotemporal token selection framework for dynamic-resolution DiTs. AViTS models spatial importance via latent-text attention and temporal importance via token-level feature variation across diffusion timesteps, and fuses them to enable spatiotemporal importance-aware selective upsampling: it prioritizes resolution refinement for critical tokens while deferring less important ones, thereby reducing redundant high-resolution computation and improving the quality-efficiency trade-off. AViTS achieves up to 6.34x on FLUX and nearly 9x FLOPs reduction on Qwen-Image-Edit and FLUX.1-Kontext-dev, orthogonal to distillation, quantization, and feature caching, and reaching 14.76x with distilled models. Code: this https URL

---


### 140. [Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents](https://arxiv.org/abs/2608.18008)

**<font color=#1a73e8>作者：</font>** Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.

---


### 141. [Memory Tree Guided Key Frame Querying for Efficient 3D Question Answering](https://arxiv.org/abs/2608.18009)

**<font color=#1a73e8>作者：</font>** Hsiang-Wei Huang, Fu-Chen Chen, Li-Wu Tsao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering questions accurately and efficiently in embodied scenarios presents significant challenges due to limited computational and memory resources for Vision Language Model (VLM) inference. Existing methods adopt visual search key frame retrieval method to select critical question-related key frames for VLM input. However, visual search methods are inefficient because they require visual search among thousands of video frames for each individual user query. In this work, we propose a memory tree guided key frame selection paradigm for efficient 3D question answering in embodied scenarios. Our method leverages a compact and reusable 3D scene representation, termed MemTree3D, which supports real-time online construction leveraging camera 6-DoF poses. MemTree3D captures multi-level 3D scene information, enabling a Large Language Model to efficiently query and retrieve question-relevant key frames through our scoring-based frame selection without reprocessing the entire video stream. On OpenEQA, our method improves the LLM-Match of GPT-4o by 17.4%, LLaVA-OneVision-7B by 5.8%, outperforms existing visual search methods. Our code is available at this https URL

---


### 142. [The IOL-AI Challenge: An Open Challenge towards Advancing Linguistic Reasoning](https://arxiv.org/abs/2608.18011)

**<font color=#1a73e8>作者：</font>** Eduardo Sánchez, Rita Berrada, Dan-Mircea Mirea 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning in LLMs is overwhelmingly studied in domains that provide a model with rules: mathematics and code. Linguistic puzzles invert this: the solver must first discover the system before reasoning within it. We present the IOL-AI Challenge, an open-science competition run on the unseen problems of the International Linguistics Olympiad (IOL) 2026 Individual Contest, evaluated both automatically and, for the first time, by members of the official IOL Jury under the same rubrics applied to human contestants. The challenge drew 731 submissions from 46 teams under a strict compute budget (one T4, 30 mins). We additionally benchmark 15 unconstrained frontier and open models, with Claude Opus 4.8 earning a jury score equivalent to a gold medal, while both resource-constrained systems we submitted for jury grading scored in the range of the bottom 5% of contestants. Capability was not determined by scale: 14B submissions outperform models twice their size, and gains come from decoding and output-handling rather than model capacity. We also found that automatic metrics rank systems exactly as the jury does, but compress the scale, upscoring weak systems by ~13 points and understating strong ones. Our analysis shows that while frontier models might have prior knowledge about some of the problem languages, it does not significantly help them solve the linguistic reasoning tasks, leaving linguistic reasoning as a strong benchmarking proxy for generalizable reasoning skills.

---


### 143. [Can Large Language Models Explain Flight Safety Events? A Prior-Guided Semantic LLM-based Approach](https://arxiv.org/abs/2608.18017)

**<font color=#1a73e8>作者：</font>** Lu Xu, Xu Li, Linjiang Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving flight safety with flight data requires not only accurate detection of risk events, but more importantly, clear interpretation of their underlying causes at the level of pilot control behavior. Existing explainable AI techniques, such as feature importance maps, often require considerable domain knowledge to translate them into operationally meaningful explanations. Large Language Models (LLMs), which excel at language reasoning, bring a promising solution to this issue. However, applying LLMs in this domain presents key challenges such as modal inconsistency, limited classification ability, scarcity of task-specific data for fine-tuning, and lack of domain knowledge. To overcome these challenges, we propose FlightLLM, a prior-guided semantic LLM-based approach for interpretable flight safety analysis. Specifically, we first perform feature engineering to address modal inconsistency, combining statistical descriptors with physically meaningful flight indicators. This representation is further processed by a Semantic Discretization module, which converts abstract numerical patterns into qualitative descriptions that are more compatible with language reasoning. In addition, since LLMs are not inherently strong classifiers, CatBoost is incorporated as a statistical expert, and its prediction results are injected into the prompt as prior guidance. A contrastive few-shot learning strategy is further adopted to compensate for limited data. Finally, we design structured prompts to embed aviation-specific knowledge into the inference process. Using hard landing, a representative risk event with complex causal mechanisms, as an anchor point, we evaluate FlightLLM on a dataset of 704 real-world A320 flight samples. Experimental results show that the proposed approach achieves competitive classification performance while generating direct and reasonable explanations for event causes.

---


### 144. [Why GPT-Style Models Do Not Directly Transfer to Symbolic Music: Compression in the Wrong Coordinate System](https://arxiv.org/abs/2608.18025)

**<font color=#1a73e8>作者：</font>** Yi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPT-style models achieve strong performance by representing language with finite vocabularies of reusable discrete tokens. This success has motivated symbolic music tokenizations to treat recurring musical structures, such as chords, motifs, and phrases, as reusable units analogous to linguistic tokens. However, tokenization derives its advantage not from reusable combinations alone, but from compression: effective compression requires coordinates in which recurring regularities form stable and predictable conditional distributions. The key problem is therefore not to find larger musical combinations, but to discover the coordinate system in which musical facts become predictively compressible. We formulate the Effectiveness--Losslessness Framework and define tokenization as the construction of a predictively effective and relationally lossless coordinate system. The Predictive Effectiveness Principle defines the Fact--Token Boundary: decoupling and denesting construct coordinate interfaces that expose predictive regularities. The Relational Losslessness Principle defines the Token--State Boundary: tokenization stops before context-dependent relations are fixed, leaving their computation to model states. Controlled symbolic-music experiments validate these boundaries. Effective coordinate construction improves predictive compressibility, while fixed relational projections constrain contextual modeling. Sequence compaction alone does not guarantee predictive compression, while preserving contextual freedom allows higher-order musical organization to emerge without explicit structural labels. These results reveal why GPT-style models do not transfer directly across modalities: architectures transfer, but tokenization interfaces do not. Tokenization must discover effective representations while preserving the relational freedom from which contextual structure can emerge.

---


### 145. [Chain-of-Experience for Continual LLM Improvement](https://arxiv.org/abs/2608.18027)

**<font color=#1a73e8>作者：</font>** Haoqin Tu, Yunhao Fang, Yizhong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans continuously learn from experience, whereas conventional large language model (LLM) evaluations ignore the models' ability to improve through inference-time interaction. In this paper, we study how LLMs learn from iterative experience at test time, a setting we refer to as Chain-of-Experience (CoE), where models accumulate experiential traces through iterative interactions with self or environmental feedback to form a continual improvement loop beyond zero-shot inference. We instantiate CoE with diverse feedback mechanisms, including model self-feedback and environmental signals such as correctness or public coding test pass rates, and evaluate across math, coding, and knowledge domains using 8 LLMs, including GPT-5, Gemini-2.5 Pro, Claude-4.5 Sonnet. Our study shows that leveraging iterative experience consistently outperforms feedback-free baselines, achieving substantial gains with self feedback alone, alongside a 5.6% overall improvement and 19% lower API cost across tasks and models. We further show that combining complementary feedback channels (e.g., model and correctness signals) yields additional gains, and that CoE delivers higher accuracy per token than existing test-time strategies. We observe a positive correlation between LLM base ability and improvement capacity, and show that models remain robust under weak or spurious feedback, with different feedback contributing to distinct improvement aspects and most gains emerging early in the iterations.

---


### 146. [Plug-and-Play Traffic Element Awareness for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.18035)

**<font color=#1a73e8>作者：</font>** Zongzheng Zhang, Jijun Wang, Saining Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic elements such as traffic lights and road signs play a fundamental role in human driving decisions and should naturally influence end-to-end driving performance. However, existing end-to-end driving research predominantly focuses on dynamic road participants (e.g., vehicles and pedestrians), while the role of traffic elements remains largely unexplored. The community still lacks a systematic study quantifying their impact, largely because public datasets rarely provide structured traffic-element annotations and modern driving systems vary widely in architecture and training paradigm. In this work, we present the first systematic investigation of traffic element awareness for end-to-end autonomous driving. We construct a unified research infrastructure by augmenting multiple public driving datasets with comprehensive traffic-element annotations. To support diverse model families, we adopt a minimal and universal integration design that incorporates traffic-element signals into existing pipelines in a plug-and-play manner with negligible architectural modification. We evaluate this design across modern paradigms, including perception-prediction-planning pipelines, vision-language-action models (VLA), regression-based planners, diffusion-based policies, and trajectory-scoring frameworks, on nuScenes, NAVSIM-v1, NAVSIM-v2, and Bench2Drive. Across all paradigms and datasets, this simple integration consistently improves driving performance, demonstrating that traffic element awareness provides a robust and generalizable signal for end-to-end driving systems. Notably, on the challenging NAVSIM-v2 benchmark, our approach significantly improves state-of-the-art architectures and data pipelines, establishing a new state of the art.

---


### 147. [Language Has Two Parameters: Narrative-Induced Semantic Plasticity and Phase-Sensitive Interpretation](https://arxiv.org/abs/2608.18041)

**<font color=#1a73e8>作者：</font>** Hollis Robbins  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language has two parameters. Count how often words occur together and you estimate amplitude, the strength of association. Word embeddings and attention weights refine that count, which sums every writer in the corpus together. This paper claims a second parameter, phase, which signed weights learned from a corpus do not supply. Phase exists only between meanings: it determines how coactivated meanings combine, and it can reverse what a meaning contributes while that meaning stays fully present. A speaker can set phase in the signal through linguistic form; encounters install phase relations and history distributes them. Population averaging deletes history-indexed phase: agent-deindexed corpora identify the population marginal state and determine no individual or dyadic state, at any scale. The standard transformer has no explicit representation for phase in frozen inference, and the interpretability program measuring progress by monosemanticity is optimizing against it: the coexistence it treats as a defect is the condition of allusion, irony, and quotation. Six predictions test whether a suppressed meaning stays active, whether encounter order changes what a phrase does, whether marking the signal changes how a shared phrase is taken, and whether a model given a history is changed by it or only informed about it. The claim defended is the weak version: interpretation requires a second relational parameter, signed, persistent, and indexed to individuals and dyads. Quantum probability is one notation for the parameter; nothing in the formalism claims quantum processes in the brain. The strong version, that the quantum calculus constrains these phenomena as signed classical models do not, rests on an encounter-order constraint not yet derived. The architecture the theory calls for is a language model with agent-indexed, phase-bearing semantic states.

---


### 148. [StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents](https://arxiv.org/abs/2608.18050)

**<font color=#1a73e8>作者：</font>** Yining Hua, Hongbin Na, Yifan Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly perform knowledge work (i.e., produce and modify persistent digital artifacts such as code repositories, documents, spreadsheets, slides, reports), yet the parsed views they search, the native files they edit, the changes they review, and the artifacts they submit can refer to different versions of the same work product. We formulate this as a workspace-state contract: every view should be explicitly tied to a version of the evolving workspace state. Coding agents partly address this need through repository contracts for search, diffs, and tests, whereas an analogous contract is less explicit for PDFs, spreadsheets, slides, notebooks, and mixed-format project folders. We propose StagedWorkspace, a versioned workspace for knowledge-work agents. The workspace binds parsed records and review diffs to content hashes of the native files as they change. In fixed-harness ablations on OfficeQA Pro and APEX-Agents, dual parsed/native access has the highest point estimate for every tested model; relative to the more limiting single view, it improves OfficeQA Pass@1 by 8.3-12.1 points and APEX mean rubric score by 4.7-9.2 points. SW-AGENT scores 63.9% with Gemini 3.1 Pro on OfficeQA and 42.1 with GPT-5.4 Nano on APEX, compared with published same-model scores of 29.3% and 25.5, respectively. A paired review-axis ablation on 57 file-editing tasks further finds higher observed scores when diffs are visible. These results identify workspace state as an experimental variable in knowledge-work agents and motivate benchmarks that score evidence, staged edits, and submitted artifacts as explicit state transitions.

---


### 149. [Delegation Asymmetry in Agentic Recommender Systems: Measuring Two-Sided Receptivity in Online Dating](https://arxiv.org/abs/2608.18058)

**<font color=#1a73e8>作者：</font>** Daria Leshchikova, Valentina V. Kuskova, Dmitry Zaytsev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents that converse on a user's behalf are an emerging design pattern in matching platforms, yet their viability depends on a condition rarely examined: users must accept not only delegating conversation to an agent, but also receiving agent-mediated communication from others. We study this condition using two large-scale surveys of active users of a major dating platform (N=2,894 on generative profile features; N=2,617 on autonomous conversational agents, fielded in two languages). We develop a latent-variable measurement model of agent receptivity based on graded response models with latent regression, and show via model comparison that willingness to send and willingness to receive agent communication are distinct constructs: highly correlated (rho=0.92) but separable (Delta BIC=52), with partial measurement invariance across languages. The model quantifies a systematic delegation asymmetry: deploying one's own agent requires far lower receptivity (threshold -0.38) than engaging a counterpart's agent (+0.32; full engagement +1.39), and mean deployment propensity exceeds engagement propensity roughly threefold. Under a random-pairing counterfactual derived from stated receptivity, only 4-13% of directed dyads combine agent deployment with receiver engagement, with a pronounced gender-directional imbalance. Design counterfactuals quantify the levers: a reciprocity requirement cuts interaction volume by half or more by excluding nearly two-thirds of would-be deployment, while routing agent contacts on receive receptivity triples per-contact engagement, a lift that survives out-of-sample validation with the target item held out (AUC 0.88, 3.1x quartile lift under respondent-level cross-validation). We discuss implications for agentic recommender design, including disclosure, opt-in mechanics, and receptivity-aware matchmaking.

---


### 150. [TokEval: A Tokenizer Evaluation Suite](https://arxiv.org/abs/2608.18062)

**<font color=#1a73e8>作者：</font>** Clara Meister  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language model tokenizers are typically selected with minimal evaluation, despite the fact that their design choices directly impact model capabilities. This can be partly attributed to a limited understanding of which tokenizer properties affect which aspects of downstream performance. We introduce TokEval, a framework of tokenizer evaluation metrics that goes beyond standard measures like fertility and compression rate to capture linguistically and structurally meaningful properties, e.g., UTF-8 character boundary integrity and digit place-value boundary alignment for mathematics. To validate whether these metrics are predictive of downstream model performance, we conduct controlled language model pretraining experiments, varying solely the tokenizers' training data mixture, pretokenization strategy, and training algorithm. We evaluate the resulting models on bits-per-byte (a tokenizer-agnostic version of perplexity) and several benchmarks, spanning linguistic understanding, mathematical reasoning, and code generation. Our experiments suggest that different intrinsic properties have different impacts on model abilities: information-theoretic metrics predict language modeling abilities (Spearman rho up to 0.80), while structure-sensitive metrics, such as those measuring digit and line-break handling, correlate with task accuracy. We hope TokEval enables more principled tokenizer evaluation, replacing pretraining sweeps with intrinsic measurement wherever the two agree.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-161](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
