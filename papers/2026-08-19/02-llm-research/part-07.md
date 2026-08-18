# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-358](./part-08.md)

---

### 301. [MLLM-Guided Semantic Correction for Text-to-Video Generation](https://arxiv.org/abs/2608.16513)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Zheqi Lv, Keting Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models and Transformer architectures have led to significant progress in text-to-video generation. However, these models often suffer from semantic errors such as missing objects, incorrect attributes, or mismatched actions. Although some semantic correction methods perform optimization before sampling or refinement after sampling, how to detect and correct semantic deviations during the video generation process remains underexplored. In this paper, we introduce a training-free, interpretable mid-generation correction framework that integrates multimodal large language model (MLLM) feedback directly into the diffusion sampling loop. Our framework achieves diffusion trajectory correction by injecting semantic evaluation signals during video synthesis, enabling the model to optimize the generated content through continuous self-reflection. We propose two key modules: a Semantic Assessment Supervisor that generates intermediate preview frames for semantic evaluations and deviation diagnostics, and a Semantic Modification Assistant that corrects semantic drift during inference via a controllable latent trajectory intervention. Our method improves semantic alignment, visual fidelity, and temporal consistency without modifying model parameters. We validate the effectiveness of our approach through extensive experiments across multiple benchmarks.

---


### 302. [Matched Outcomes, Divergent Gaze: How Foveated MLLMs Search Compared to Humans](https://arxiv.org/abs/2608.16514)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Kerkouri, Marouane Tliba, Aladine Chetouani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human visual search is serial: the fovea must land on a candidate to confirm it, and those landings form a scanpath. Whether multimodal large language models (MLLMs), given the same foveated input, search as humans do bears on their use as models of human vision and on attention-alignment scores. We compare three general-purpose MLLMs with human eye-movement scanpaths on goal-directed search (COCO-Search18), driving each model fixation by fixation through an identical, human-matched foveated view and assessing it along three axes: the decision of target presence, the efficiency of reaching the target, and the gaze process itself. The axes dissociate. On the decision and on target acquisition the models match or exceed humans, detecting present targets near ceiling and reaching them on the first saccade more often than people do. The gaze process is not human. Under the human-matched condition, all three share one signature: low-entropy, large-amplitude, self-consistent scanpaths that agree with themselves far more closely than two humans agree with each other. That is consistent with a single-pass, non-serial architecture rather than a limit of acuity. Matched retinal input reproduces where humans look but not how the looking unfolds in time, and no degradation regime recovers human-like search at human-like success. The gap sits on a process axis that answer-alignment and saliency metrics do not measure. Because they miss it, such metrics cannot certify human-like vision, and zero-shot models suit outcome and spatial questions but not temporal, process-level ones.

---


### 303. [When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2608.16515)

**<font color=#1a73e8>作者：</font>** Haolin Jin, Pengyue Yang, Huaming Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves large language models by grounding generation in external evidence, but it also introduces a source trust problem: retrieved context may be useful, irrelevant, or even misleading. Existing RAG systems often apply a fixed trust policy toward retrieved evidence, which can either over-trust incorrect context or underuse context when the user explicitly asks for context-following behavior. Therefore, we propose Intent-Guided Decoding (IGD), a framework that arbitrates between retrieved context and parametric memory according to user intent. IGD uses answer-level filtering and token-level correction to steer the final decoding trajectory between retrieved context and parametric memory. We evaluate IGD on three faithful QA benchmarks and three factual-conflict benchmarks across five LLMs, IGD substantially improves factual recovery, achieving gains of up to 65.4 percentage points on factual-conflict benchmarks over Direct RAG, while preserving or improving strict context-following behavior, this findings highlight the importance of balancing factuality and faithfulness in RAG.

---


### 304. [What to Remember, What to Reveal: Privacy-Aware Memory for Conversational Agents](https://arxiv.org/abs/2608.16551)

**<font color=#1a73e8>作者：</font>** Wenjie Wang, Wenhe Si, Xinyue Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables personalized conversational agents to retain user information across sessions. However, existing memory architectures primarily optimize for utility while neglecting the risks of unnecessarily storing and reusing private attributes such as personally identifiable information (PII). Addressing privacy risks in personalized memory is challenging because simply removing sensitive values can undermine system utility. Therefore, privacy protection for memory agents should govern the full life cycle of sensitive values rather than only sanitizing individual records. To address this gap, we introduce Sanitized Privacy-Mapped Memory (SP-Mem), a privacy-aware memory architecture that decouples memory utility from exact private-value exposure. SP-Mem provides a full life-cycle privacy design that identifies and separates sensitive information from raw user inputs, stores sanitized content and exact private values in isolated structures, and selectively retrieves private values based on task requirements and user consent. We further introduce a privacy-aware memory benchmark that jointly evaluates response quality, privacy behavior, and inference cost. Extensive experiments across multiple LLM-based agents show that SP-Mem achieves stronger personalization while reducing unnecessary privacy exposure. Code and data are available at this https URL.

---


### 305. [STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment](https://arxiv.org/abs/2608.16553)

**<font color=#1a73e8>作者：</font>** Yongqi Tong, Zhenyu Zhang, Ruirui Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-preference alignment is often framed as scalarization: combine reward dimensions, then optimize. This leaves a temporal decision underspecified: when should each preference dimension enter policy optimization? We propose \methodname, a stability-guided active-set controller for controlled objective admission. \methodname starts from a small active set, retains admitted objectives, and expands when reward-deviation gates indicate low recent deviation or a patience budget is exhausted. A probing phase estimates a hard-to-easy order, and adaptive weighting emphasizes underperforming active dimensions. Automatic evaluations with 15 training preferences and 16 held-out benchmark columns show that \methodname obtains higher averages than simultaneous scalarization and shared-budget adapted baselines. Component ablations and expansion dynamics further support cumulative retention, gated admission, and probing-derived ordering as useful design choices in this setting. These results position objective-entry timing as a concrete control variable in reward-vector RLHF.

---


### 306. [Ask, Condition or Abstain: Reinforcement Learning for Missing-Premise Reasoning](https://arxiv.org/abs/2608.16554)

**<font color=#1a73e8>作者：</font>** Yongqi Tong, Zhenyu Zhang, Zimi Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answer-only reinforcement learning (RL) trains reasoning models to solve fully specified problems, but many realistic queries omit a premise needed for a unique answer. In this setting, the useful response is not always refusal: the model should ask for the missing premise, condition its answer on the unknown quantity, or abstain when no informative conditional response is available. We present \emph{Ask-Condition-Abstain Reinforcement Learning} (ACA-RL), a data-augmented RL framework for this setting. Its reasoning-graph-guided pipeline converts well-posed problems into missing-premise training instances with localized gap annotations; ACA-RL then trains on these instances with a structured reward over five observable response behaviors. We also introduce the \emph{Missing-Premise Benchmark} (MPB), a 274-instance human-verified benchmark spanning mathematical, logical, and real-world word problems. Across Qwen3 and Llama models, ACA-RL consistently improves on MPB while preserving competitive performance on well-posed reasoning tasks. Together with the released code, MPB, and training data, this work supports a new mission for NLP evaluation: measuring whether models can recognize when a task is underdetermined and handle uncertainty, not only whether they can answer fully specified questions.

---


### 307. [The User Side of AI Model Lifecycles: Evidence from the Keep4o Movement](https://arxiv.org/abs/2608.16574)

**<font color=#1a73e8>作者：</font>** Yiwen Wu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI model lifecycles are commonly understood as a series of technical and organizational processes. Yet once a model enters sustained use, subsequent changes can also affect established user practices and user value. Using the Keep4o movement around GPT-4o as a case, this study examines post-deployment AI model lifecycle issues from the user side. We collected 61,846 public original posts on X from August 2025 to March 2026 and, using a systematically developed coding framework and LLM-assisted content analysis, analyzed discussion themes, users' reasons for wanting to keep GPT-4o, and the specific claims they made. Findings show that the Keep4o discussion extended well beyond continued access to the model itself. It covered concrete experiences of use, model behavioral characteristics and how they changed, and management issues across different stages of the model lifecycle. Reasons for keeping GPT-4o reflected interactional and relational value formed through long-term use, as well as judgments about the adequacy of replacement and the reasonableness of related decisions. The corresponding claims further reflected users' specific expectations for model lifecycle arrangements and governance. Overall, the call to "keep GPT-4o" brought together different judgments about user value and governance concerns. These findings suggest that technical version succession does not necessarily amount to effective replacement on the user side. Post-deployment AI model lifecycle management therefore needs to consider whether established user value can be carried forward and how model changes affect actual use. This study thus provides user-side empirical evidence for AI model lifecycle management. It further shows that user experience can provide important information for identifying post-deployment impacts and should be incorporated into lifecycle evaluation and decision-making.

---


### 308. [Physics of Agents: Statistical Mechanics Predicts Collective Behavior of AI Agents](https://arxiv.org/abs/2608.16578)

**<font color=#1a73e8>作者：</font>** Batu El, Jinhee Paeng, Fatih Dinc 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly operate as part of interacting systems rather than in isolation. As agents exchange information and jointly make decisions, their interactions can improve collective reasoning but may also produce herding, polarization, or amplify shared biases. Understanding and predicting these collective dynamics is therefore important for designing effective and aligned multi-agent systems. Here, we study over 10,000 communities of language-model agents that repeatedly exchange messages and revise their opinions across objective mathematics questions and subjective political statements. Despite substantial diversity in possible behavior, the individual and group dynamics can be represented by three characteristic regimes: indifference, polarization, and consensus. AI agents start indifferent and build conviction as they interact. On objective questions, communication improves collective accuracy, while on subjective questions it often drifts group opinions toward the right in the political spectrum. We explain these observations with a statistical-mechanics formalism in which agents stochastically favor lower social pressure. Given only initial opinions, our model predicts individual trajectories, outperforms all standard baselines, generalizes to unseen community graphs, and reproduces the observed group archetype distributions. Our fitted model parameters reveal the mechanics underlying our key observations: i) communities operate below the critical social temperature, which explains conviction buildup; ii) attractive ties outweigh repulsive ones, which favors consensus; and iii) agents holding the correct answer exert the strongest pull, which drives truth-seeking. Overall, our results demonstrate that collective behavior of AI agents, like that of other complex systems, follows compact and predictive dynamical laws.

---


### 309. [CACSurv: Concordance-Aligned Comparative Learning with Large Language Models for Cancer Survival Prediction](https://arxiv.org/abs/2608.16594)

**<font color=#1a73e8>作者：</font>** Tianqi Xiang, Qixiang Zhang, Xinpeng Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cancer survival prediction supports treatment planning, risk stratification, and follow-up management. Existing methods use structured clinical variables, whole-slide images, genomic profiles, or multimodal inputs, while patient reports remain underexplored. We study report-centric survival prediction using reports that organize pathological, clinical, and molecular evidence. Large language models (LLMs) can reason over such reports, but case-wise time regression introduces two mismatches. First, a formulation mismatch arises because survival evaluation depends on ordering comparable patients, whereas independent time predictions do not enforce ranking consistency. Second, a supervision mismatch arises because a censored patient's observed time indicates survival beyond that point and cannot serve as an exact regression target, although it still implies orderings relative to patients who died earlier. To address these mismatches, we propose CACSurv, a Concordance-Aligned Comparative framework for report-centric survival prediction. CACSurv reformulates survival modeling as mini-cohort comparative reasoning, where an LLM predicts relative prognostic orderings. We introduce concordance-aligned rewards derived from comparable relations under right censoring, enabling censored outcomes to provide ranking supervision without exact event-time targets. At inference, Monte Carlo Reference Aggregation compares each patient with sampled references and aggregates positions into a cohort-level ranking. We establish TCGA-SurvReport, a benchmark covering six TCGA cancer cohorts. CACSurv achieves the highest C-index on all six cohorts and an average C-index of 0.722, outperforming the strongest published survival model by 6.5 percentage points and the strongest LLM time-regression baseline by 4.2 percentage points. Our code, models, and dataset will be available at this https URL.

---


### 310. [Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning](https://arxiv.org/abs/2608.16620)

**<font color=#1a73e8>作者：</font>** Peng Du, Kiran Kamble, Rakshith Vasudev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Palmyra x6 is a large language model optimized for use with enterprise-oriented agentic tasks. The model was built by post-training a Mixture-of-Experts base model with Anchored Supervised Fine-Tuning on a compact corpus of verified, synthetic tool-use trajectories, optimized with a Muon + Adam hybrid. The recipe is deliberately conservative and deliberately controlled: 626 trajectories, a single epoch, a low learning rate, and a KL anchor to the frozen base. The model shows substantial gains over the previous default model for Writer Agent, and compares favorably with several recent models on public benchmarks, scoring the highest on BFCL Core at $0.785$ and posts the highest six-benchmark mean of the cohort. Furthermore, the model has shown itself to be competitive or leading relative to comparators in our bias and safety evaluations.

---


### 311. [HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target Identification in Harmful Memes](https://arxiv.org/abs/2608.16622)

**<font color=#1a73e8>作者：</font>** Yujia Li, Yiqun Zhang, Zihan Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal harmful meme detection is typically formulated as image--text harmfulness classification. A model may correctly predict harmfulness while misidentifying the attacked target or its supporting evidence. We therefore extend harmful meme detection with fine-grained target identification, asking what type of target is attacked, who is targeted, and where the target appears in the meme. The model predicts harmfulness for every meme and, for harmful memes, outputs the target category, target entity, textual mention, and visual region. To support this task, we introduce Meme3W, which unifies multiple public harmful meme datasets and provides human-verified annotations for harmful instances. We further introduce Joint Record Accuracy (JRA), a strict record-level metric requiring the harmfulness label and all target-identification fields to be jointly correct. Experiments with representative multimodal large language models reveal a substantial gap between harmfulness accuracy and JRA. To narrow this gap, we propose HarmTrace, an anchor-calibrated decoupled optimization framework. HarmTrace strengthens target-entity supervision through entity-aware supervised fine-tuning. It then applies Conditional Target-identification Policy Optimization (CTPO) to decouple harmfulness and target-identification advantages, restricting target-identification optimization to label-correct responses for harmful examples. CTPO uses a Virtual Positive Anchor (VPA) as a fully correct reference for target-identification advantage normalization. HarmTrace improves both JRA and harmfulness accuracy across the evaluated backbones, with JRA on the Qwen3-VL-8B backbone increasing from 17.58\% to 52.51\%. Our code is publicly available at this https URL.

---


### 312. [When Do Explanations Help In-Context Learning? A Comparative Study of Natural Language Explanation Types and Faithfulness](https://arxiv.org/abs/2608.16627)

**<font color=#1a73e8>作者：</font>** Mahdi Dhaini, Adam Dejl, Juraj Vladika 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language explanations (NLEs) are increasingly used as inputs, for example, as few-shot rationales that influence model behavior in in-context learning (ICL). However, it remains unclear how different types of NLEs compare in their effects on downstream model performance in explanation-augmented prompting. Therefore, we provide a comparative evaluation across six benchmarks and four instruction-tuned models, studying how NLE source (human-written when available, self-generated explanations, generated by an external LLM) and NLE selection (random vs faithfulness-based filtering) affect downstream utility of NLEs when used in ICL settings. Our extensive evaluation shows that, on classification-style benchmarks, adding NLEs to few-shot prompts often improves accuracy over few-shot prompting without explanations; among NLE sources, externally generated LLM-NLEs often provide strong downstream utility and remain competitive with human rationales where both are available, whereas self-NLEs are more sensitive to the selection strategy. On math reasoning, the effects are more model- and source-dependent. We further show that faithfulness-based selection of self-NLEs yields small average gains overall, but can improve or reduce performance depending on the metric, task, and model. Different faithfulness metrics can disagree substantially, affecting which self-NLE examples are selected and their downstream predictive utility. Robustness tests with randomly swapped and out-of-distribution rationales indicate partial robustness, suggesting that semantic alignment contributes to performance gains. Overall, our results provide insights for selecting and reporting explanations that influence model behavior in practical prompting pipelines.

---


### 313. [Hypergraph-based Multimodal Retrieval-Augmented Generation with Incremental Refinement](https://arxiv.org/abs/2608.16628)

**<font color=#1a73e8>作者：</font>** Shenao Chen, Yidan Xu, Xiangmin Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern Multimodal Retrieval-Augmented Generation (M-RAG) systems are fundamentally limited by the binary connectivity paradigm of traditional simple graphs, which fails to capture the intricate, high-order correlations among heterogeneous entities, such as the N-ary relationships between a visual chart, its scattered textual descriptions, and underlying numerical data. Furthermore, existing refinement strategies often rely on exhaustive, full-page reconstruction to align cross-modal information, leading to prohibitive computational redundancy and the introduction of contextual noise in long-form document processing. In this paper, we propose Hyper-M2RAG, a novel framework that redefines multimodal document retrieval through High-order Hypergraph Representation Learning. We first formalize the document structure as a Multimodal Hypergraph, utilizing hyperedges as unified semantic containers to encapsulate multi-way associations across text, images, and tables, thereby transcending point-to-point modeling. To mitigate semantic fragmentation caused by physical pagination, we introduce an Anchor-driven Incremental Refinement mechanism. Rather than performing a global sweep, our approach identifies boundary-crossing anchor nodes and reconstructs their local hyper-topology using one-hop neighborhood contexts. This targeted refinement effectively bridges cross-page knowledge gaps with minimal computational footprints. Extensive evaluations on multimodal benchmarking datasets demonstrate that Hyper-M2RAG significantly outperforms state-of-the-art methods in both retrieval precision and generation coherence. Our code is available at this https URL.

---


### 314. [PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning](https://arxiv.org/abs/2608.16637)

**<font color=#1a73e8>作者：</font>** Veit Laule, Jiangtao Shuai, Manfred Hauswirth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs remain unreliable for long-horizon planning, often generating logically inconsistent or non-applicable plans. Recent hybrid methods instead translate natural language into the Planning Domain Definition Language (PDDL), allowing symbolic planners to produce verifiable plans. However, existing methods frequently rely on rigid generation pipelines, a partial PDDL definition, or human feedback. Furthermore, their evaluation is hindered by the lack of standardized benchmarks with automated verification. To address these limitations, we present PDDLCoder, an agentic framework for PDDL generation from natural language that iteratively generates, analyzes, and refines planning specifications. We further introduce NL-pddlgym, a benchmark dataset comprising 711 planning problems across 23 domains with executable gym environments for the automated verification of plan applicability. Experiments on the NL-pddlgym test set containing 106 problems across 4 held-out domains show that PDDLCoder generates applicable plans for 89.6\% of tested planning problems. This improves upon our adaptations of previous PDDL generation methods, which achieved up to 45.3\%, and outperforms direct LLM planning approaches, which reached up to 74.5\% on the same test set. Our work demonstrates the effectiveness of agentic PDDL generation for planning and establishes a reproducible benchmark for future research on LLM-assisted symbolic planning.

---


### 315. [Toward Better Assessment of LLMs' Performance in Clinical Error Detection](https://arxiv.org/abs/2608.16643)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Rahmatollah Beheshti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated detection of errors in clinical documentation is a promising application of large language models (LLMs), yet decisions to deploy such models rest on benchmarks that evaluate each clinical note in isolation. Error-detection benchmarks are typically constructed by injecting errors into notes, such that each erroneous note has a natural counterpart. Aggregate discriminative metrics (e.g., balanced accuracy or F1) do not exploit this structure. We show that this omission is consequential. In particular, evaluating 15 diverse LLMs on 4 standardized clinical error-detection test sets across 3 languages, we find that 13 of 15 models fall below the level of random pairwise discrimination, even while achieving F1 scores that standard practice would read as moderate. We also observe that the underlying bias patterns differ across languages: the same model can default to "no error" on one language and over-flag errors on another. To diagnose where discrimination breaks down, we further introduce a procedure to score the evidence models cite in their outputs. We find that while models consistently locate error-relevant content, they fail to produce the corresponding correct verdict on the clean counterpart. Finally, we show that F1 and pairwise accuracy are driven in opposite directions by the same underlying bias, so that ranking models by F1 may systematically promote the weakest discriminators. For safety-critical clinical NLP applications, we advocate for supplementing aggregate metrics with paired evaluations in benchmark reporting. Code and analysis scripts are available at this https URL.

---


### 316. [Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies](https://arxiv.org/abs/2608.16645)

**<font color=#1a73e8>作者：</font>** Shaolong Chen, Yanlin Fei, Nazhou Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a language model recover the true research idea of a published paper when given only that paper's pre-publication bibliography? We introduce Reconstruction, a blind idea-recovery benchmark that withholds the seed paper and all contemporaneous or future literature, and asks models to propose hypotheses that an independent large language model judge matches against the held-out ground-truth idea. A strict anti-leakage protocol-temporal citation cutoff, anonymous reference IDs, and frozen per-paper bibliographies, which prevents prompt-time leakage of the seed idea. Across six scientific domains and 643 evaluated papers, seven frontier models achieve only modest Match rates (approx. 3-15%). We then evaluate a reference-only multi-agent (top 4) pipeline that combines cross-model review with a Swiss tournament over aligned hypothesis slots, without external web search. Cross-model review plus tournament selection raises Match rates to approx. 23-42% across all six domains, which is an observed approx. 2.4x lift over the best single-model baseline. This draft reports the protocol, anti-leakage design, and current results as an arXiv timestamp.

---


### 317. [Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2608.16647)

**<font color=#1a73e8>作者：</font>** Zhaoyi Li, Deyang Kong, Yuan Wei 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers teacher capabilities by supervising trajectories sampled from the student's own policy, yet its generalization behavior remains poorly understood, as most studies evaluate OPD on a single domain and on benchmarks close to the training data. We present a controlled study that varies one generalization factor at a time, from in-domain distribution shifts to cross-domain transfer and the multi-teacher setting. We find that OPD transfers a teacher's reasoning behavior rather than its answers to particular problems: training difficulty barely matters, and even problems the teacher never solves are useful. Transfer depends strongly on the origin relationship between teacher and student: same-origin pairs bring the student close to the teacher across languages, reasoning horizons, and even other domains, whereas cross-origin pairs mostly fit the trained distribution. This broad reach is a double-edged sword: since routing prompts to domain experts cannot confine each teacher's influence, combining them yields a mixture-dependent seesaw among their capabilities. These results clarify when OPD generalizes and offer a useful perspective for diagnosing multi-teacher OPD.

---


### 318. [PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM Sycophancy](https://arxiv.org/abs/2608.16650)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Zhaoxin Feng, Yip Tin Po 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit sycophancy, a tendency to agree with user beliefs regardless of factual accuracy. This can reinforce misconceptions, but eliminating it entirely risks over-correction against valid opinions. Effective control must therefore both reduce and increase sycophancy with predictable and gradual effect. Yet, existing methods fail to ensure a bidirectional and monotonic relationship between steering strength and behavioral outcome across models and datasets. We introduce PCA-guided Activation Scaling (PAS), an activation steering framework that decomposes residual stream activations into a PCA-identified sycophancy-honesty subspace and an orthogonal residual, then applies distinct scaling exponents to achieve monotonic, bidirectional control. Across three LLMs and three datasets, PAS achieves strong monotonicity (Spearman $\rho$ = +0.92) and an average shift of 15.4% per direction, compared with 8.7% for the baselines. Ablation studies confirm that the decomposition, asymmetric exponents, and layer selection are each essential for maintaining monotonic control. The data and code are available at this https URL.

---


### 319. [Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test](https://arxiv.org/abs/2608.16671)

**<font color=#1a73e8>作者：</font>** Anand Murugan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The language-model head maps a hidden state of width D to a vocabulary of size V, so its transpose can return at most D independent directions to the Transformer. Godey and Artzi argue that this severe projection is a harmful optimization bottleneck. We separate the geometry from the causal claim. Our backward-only intervention keeps the ordinary logits and the exact LM-head parameter update while reducing only the rank of the gradient sent into the Transformer. Across five paired seeds on byte-level and BPE-8192 WikiText-2 models, reducing backward rank increases validation loss. An equally ranked factorized forward head, however, increases loss substantially more. At half rank in the larger model, the backward-only loss increase is 0.0586 (95% CI [0.0167, 0.1005]), while the factorized forward head increases loss by 0.1795 ([0.1547, 0.2042]). The vocabulary-space residual also contributes to the ordinary LM-head update, and removing that contribution is harmful. Additional controls show that repeated-token failures are confounded by the number of independently sampled symbols, that adding never-target output classes does not impair learning, and that projection diagnostics do not reliably predict progress in our runs. Tested auxiliary feedback routes do not beat tuned backpropagation. These results confirm strong geometric compression but do not establish that it is a harmful optimization bottleneck.

---


### 320. [Closing the Affective Loop: Multimodal Speaker-Listener Emotion-Dynamics-Aware Empathetic Social Robots](https://arxiv.org/abs/2608.16686)

**<font color=#1a73e8>作者：</font>** Zi Haur Pang, Casey Kennington, Tatsuya Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Empathetic social robots should respond not only to what users say, but also to how their emotions dynamically evolve during interaction. However, existing empathetic dialogue systems are often text-centered and primarily model empathy as a one-way mapping from the user's emotion to the system response, limiting their ability to capture embodied speaker--listener affective exchange. We present AffectLoop, a multimodal speaker-listener emotion-dynamics-aware spoken dialogue system implemented on the Misty II robot. The system tracks the speaker's verbal and facial affective dynamics, estimates the robot listener's own verbal and behavioral affective state, and conditions LLM-based response generation on both affective streams. The robot then generates a short spoken empathetic response together with emotionally congruent embodied behavior, forming a closed speaker--listener affective loop. We evaluate the system in a pilot within-subject study with five participants, comparing it with an otherwise identical utterance-conditioned baseline that omits the speaker- and listener-affective-state inputs. The proposed system received higher overall impression ratings, especially for empathetic response and user satisfaction. Post-hoc log analysis further showed higher speaker-listener affective alignment and stronger valence-based distress recovery. These preliminary results suggest that explicitly modeling both speaker emotional dynamics and listener affective state can improve embodied empathetic interaction.

---


### 321. [AnchorScore: A CLIP-Based Diagnostic of MLLM Annotation Difficulty](https://arxiv.org/abs/2608.16690)

**<font color=#1a73e8>作者：</font>** Yan Ma, Lizhuo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are widely used for automated annotation, yet their per-class accuracy varies widely (e.g., 12%-98% across the 13 classes of three classroom sub-datasets) and is expensive to measure: evaluating one 27B MLLM on 5,416 validation images takes roughly 14 hours, whereas a frozen-CLIP pass over the same images completes in about 3 minutes. A low-cost signal for ranking classes by expected MLLM annotation difficulty a priori remains underexplored. Building on the AnchorProxy construct (per-class zero-shot CLIP accuracy) introduced in the companion study, this paper systematically evaluates its full-frame formulation, termed AnchorScore here, as an a priori diagnostic that flags the classes MLLMs are least likely to annotate reliably.
On classroom behavior data (SCB5, 13 classes, 6 MLLMs), AnchorScore correlates with per-class MLLM accuracy (Spearman rho = 0.769, p = 0.002, n = 13). None of the alternative difficulty predictors (DINOv2, ResNet-50, SigLIP, or MLLM self-verbalized uncertainty) showed a significant class-level correlation at n = 13. A cross-model consensus control suggests AnchorScore primarily captures a shared class-difficulty factor rather than a CLIP-specific signal. An independent replication on Stanford40 Actions yields a nearly identical effect (rho = 0.817, p < 0.001); the association is strongest on activity-recognition data and attenuates on medical and satellite imagery.
Three practical applications follow: a deployable hybrid CLIP/MLLM routing strategy (predicted-class routing: up to +23 pp over CLIP-only at roughly 44% MLLM cost savings), prompt disambiguation on hard classes (exploratory), and review-priority prediction for human verification. AnchorScore does not estimate exact MLLM accuracy; it provides a low-cost ranking signal that directs expensive MLLM evaluation to the classes where it is most informative.

---


### 322. [FabriMAE I Trust Myself? Self-Evaluating VLA Action Generation with Markov Attention Entropy](https://arxiv.org/abs/2608.16697)

**<font color=#1a73e8>作者：</font>** Aniri, Chen Yilin, Jinhe Bi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action models (VLAs) integrate visual perception, language instruction, and action generation into end-to-end policies across heterogeneous architectures. However, enabling VLAs to self-evaluate their action generation reliability without external supervision remains a major challenge. Existing methods either rely on expert annotations or estimate uncertainty only from output statistics, largely ignoring internal signals. In this work, we observe that internal visual modality entropy exhibits consistent distinctions between successful and failed tasks across heterogeneous VLAs. Although VLAs' architectures differ in their action generation, we show that they share a common latent action generation abstraction evolving under visual perception, language instruction, and state input, which we formulate as a Conditional Generative Markov Chain. Based on this formulation, we propose MAE (Markov Attention Entropy), a self-evaluation framework that directly converts internal attention signals into architecture-aware reliability scores, and introduce LIBERO-Reflect, a 4,000-episode benchmark combining 2,000 standard episodes and 2,000 challenging episodes across four subsets. Extensive experiments across heterogeneous VLA architectures and diverse scenarios show that MAE consistently outperforms state-of-the-art baselines on AUPR, AUROC, and FPR@95. We further instantiate FabriMAE for verifier-free test-time action selection, showing that MAE-guided multiple sampling improves PI-family robustness on LIBERO-Plus with small observed runtime overhead.

---


### 323. [Semantic Bandits: In-Context Exploration-Exploitation is Biased by Semantic Priors](https://arxiv.org/abs/2608.16707)

**<font color=#1a73e8>作者：</font>** David Eric Austin, Kaheer Suleman, Jackie Chi Kit Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as decision-making agents in settings that require sophisticated environmental exploration. However, existing work has raised questions about how LLMs actually balance exploration and exploitation. Unlike classical agents, LLM agents engage with tasks through natural language, exposing them to semantic information with no formal counterpart in the task structure. We introduce the semantic bandit, an extension of the multi-armed bandit setting that explicitly considers the textual labels assigned to actions, and use it to study how semantic priors --- inductive biases arising from associations between language and expected reward learned during pre-training, shape LLM exploration behaviour. We find that semantically informative action labels reduce exploration in favour of exploitation, improving performance when aligned with the reward structure and severely degrading it when misaligned. We further find that negative rewards trigger substantially more exploration than equivalent positive rewards, consistent with an expected-scale bias induced by reward conventions common in pre-training data. Overall, we argue that the use of language to define the environment and rewards introduces unavoidable biases derived from the fact that the model is trained on word co-occurence, with implications for the reliability and robustness of LLM agents in real-world decision-making settings.

---


### 324. [Le Critique: Privileged Value Functions for LLM Reinforcement Learning](https://arxiv.org/abs/2608.16739)

**<font color=#1a73e8>作者：</font>** Siddarth Venkatraman, Matthieu Dinot, Laurence Aitchison  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning algorithms for Large Language Models (LLMs) are largely distinguished by their variance reduction strategy. Group-relative methods like GRPO reduce gradient variance by sampling multiple rollouts per prompt, but provide only sequence-level credit. Training is also blocked by straggler rollouts, reducing throughput and increasing off-policyness. Learned value functions theoretically address both problems, providing token-level advantages without requiring large groups. However, additional infrastructure engineering challenges combined with the practical success of critic-free methods have made it difficult to justify their inclusion in RL pipelines. We propose two complementary strategies to improve the performance of value function RL: 1) Privileged Value Functions (PVF) which provide an elegant mechanism to inject additional task-relevant token-level signal without biasing the policy objective; 2) TETHER, a baseline that adaptively interpolates between group-relative and value baselines depending on the value function accuracy. Across several reasoning tasks, both strategies consistently improve over the standard value function baseline, and are competitive with or outperform mean-baseline GRPO.

---


### 325. [Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments](https://arxiv.org/abs/2608.16747)

**<font color=#1a73e8>作者：</font>** Adam Karvonen, Euan Ong, Subhash Kantamneni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many areas of AI research, such as language model interpretability and chain of thought faithfulness, seek to explain model behaviors. But what constitutes a "good" explanation? In this work, we evaluate explanations through the lens of counterfactual simulatability-whether the explanation is useful for predicting model behaviors on related counterfactual inputs. To this end, we introduce CHIVE (Counterfactual Hypothesis Investigation Via Edits), a novel agentic pipeline that identifies unexpected model behaviors in the wild and investigates them with counterfactual prompt edits. This yields thousands of high-quality explanations for naturally-occurring model behaviors along with supporting counterfactual evidence. We apply CHIVE in two ways. First, we evaluate whether common LLM interpretability techniques improve an agent's ability to predict counterfactual model behaviors. Surprisingly, we find no uplift from any of the interpretability techniques studied. Second, we use CHIVE to generate training data. We find that training models to predict outcomes of CHIVE-generated counterfactual experiments generalizes to various out-of-distribution settings. Overall, CHIVE automatically discovers explanations of naturally-occurring LLM behaviors, enabling us to evaluate and improve methods for explaining LLM behaviors.

---


### 326. [On the Principles Behind Neural Network Optimizers](https://arxiv.org/abs/2608.16760)

**<font color=#1a73e8>作者：</font>** Yushun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable optimization is central to neural network (NN) training, yet Adam, the default optimizer for modern LLMs, rests on a fragile foundation. This thesis develops a principled grounding for Adam and motivates new designs. First, we revisit Adam's divergence--convergence debate and show the existence of a problem-dependent phase transition: with properly chosen, batch-size-dependent hyperparameters, Adam converges, whereas under small-$\beta_2$ regimes it can diverge. Second, we investigate why Adam substantially outperforms SGD on Transformers through Hessian structure. We find that the Hessian evolves toward a near-block-diagonal form along training, accompanied by strong block heterogeneity. We prove that this structure makes Adam's diagonal preconditioner effective. We further show that this special Hessian structure originates from consecutive multiplications of large matrix variables, and we provide a rigorous analysis based on random matrix theory. Finally, these insights motivate Adam-mini, a new optimizer that reduces Adam's memory footprint by 50\% while preserving its performance. Our results also have broader implications beyond Adam: they reveal new local structures in matrix-based nonconvex problems, and also help understand and improve recent NN optimizers, such as Muon.

---


### 327. [LAVA: Logic-Aware Validation and Augmentation Framework for Large-Scale Financial Document Auditing](https://arxiv.org/abs/2608.16763)

**<font color=#1a73e8>作者：</font>** Ruoqi Shu, Xuhui Wang, Isaac Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial document validation in production, such as payroll auditing, tax compliance, and loan underwriting, demands exceptional accuracy, consistency, and reproducibility under strict enterprise constraints. In practice, documents arrive with heterogeneous layouts and formats, semantically rich and context-dependent content, and embedded business rules that current pipelines struggle to process reliably. We introduce LAVA (Logic-Aware Validation and Augmentation), a modular, backbone-agnostic pipeline built on multimodal large language models, that integrates a four-stage design: document-rule retrieval, layout-preserving information extraction, auxiliary metadata enrichment, and auditable symbolic/arithmetic verification. LAVA supports robust rule grounding, fine-grained error attribution, and consistent, traceable end-to-end execution, capabilities essential for high-stakes deployment. Evaluated on a large real-world benchmark with diverse financial documents and dozens of expert-curated validation rules, LAVA outperforms baselines in hallucination control and edge-case handling while maintaining efficient token usage, demonstrating practicality for high-volume, time-critical validation.

---


### 328. [Topological Attribution Distance (TAD): Revealing Segment-Level RAG Influence on LLM Output Geometry for Incident Log Analysis](https://arxiv.org/abs/2608.16775)

**<font color=#1a73e8>作者：</font>** Reza Fayyazi, Michael Zuzak, Shanchieh Jay Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being deployed in cybersecurity operations to assist cybersecurity analysts with rapid decision-making against emerging threats. However, there is a main criteria that must be met when using LLMs in cybersecurity, that is, trust in the generated outputs. As Agentic AI is integrated into operational systems, a robust evidence attribution and provenance tracking technique is essential to trace the origins of model generations. When autonomous agents make a decision (right or wrong), the ability to trace back through the decision chain is critical, as without it, teams cannot identify which segment of the data caused the model generation. Existing methods often struggle to distinguish among complex and highly similar evidence sources, such as cyber incident logs. This reveals a key gap: current approaches do not adequately capture the holistic geometric relationship between the retrieved evidence and the generated response for reliable evidence verification. To bridge this gap, we propose Topological Attribution Distance (TAD), inspired by Topology, to characterize and capture the global geometric shape of an output and its changes against its retrieved logs. In other words, if the embeddings of a specific source log drastically changes the geometry of the model's response in the embedding space, this suggests that such log is a critical source for the model's generated response. Therefore, TAD is powered by segment-level ablation attribution to investigate incident logs of an actual cyberattack. We demonstrate how TAD finds the most attributed logs on LLM outputs in an adaptive manner. This can provide an explainable and trustworthy tracing based on each LLM's hidden state to understand how geometrically different retrieved logs influence the model generation, and provide evidence verification in cybersecurity and Agentic-AI workflows.

---


### 329. [GRIP: Grounded Reasoning via Information-Restricted Premises](https://arxiv.org/abs/2608.16776)

**<font color=#1a73e8>作者：</font>** Lirui Teng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-capacity encoders in retrieval-augmented generation (RAG) can let the query dominate the latent state, leaving retrieved evidence functionally irrelevant. We call this failure mode query dominance. To address it, we introduce \textbf{GRIP} (Grounded Reasoning via Information-Restricted Premises), which imposes capacity asymmetry: the decoder keeps full-dimensional access to the query, while retrieved evidence passes through a severe stochastic bottleneck. This forces the evidence channel to encode only the residual information unavailable from the query. Across five reasoning benchmarks, GRIP outperforms strong iterative baselines, cuts a query--latent mutual-information diagnostic by roughly 30$\times$ (14.8 $\to$ 0.47 bits), and reduces hallucination by 73\%. Residual-alignment analysis further shows that the bottleneck output occupies subspaces less aligned with the query than baseline representations.

---


### 330. [When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding](https://arxiv.org/abs/2608.16801)

**<font color=#1a73e8>作者：</font>** Giuseppe Destefanis, Tomaso Aste  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how teams of AI coding agents coordinate while solving programming tasks. Current evaluations usually report whether the agents complete the task and how much the run costs, leaving the coordination inside the team largely unmeasured. We introduce an instrument to measure this coordination. Each run is represented as a temporal network in which agents and files are nodes, and messages, file writes, and file reads are timestamped directed edges with an associated cost. We apply this instrument to 1902 runs, each evaluated with a fixed test suite, across configurations that vary the team size, the team structure, and the file policy. The resulting networks show how coordination changes as teams grow and as the work changes. Direct messaging initially increases close to quadratically with the number of agents, with much of this growth coming from an early round of introductions. As the teams grow further, this increase levels off in the largest teams we study, where agents increasingly communicate through broadcast messages. The task also shapes the network that emerges. Work built around a shared specification produces dense, highly connected teams, while pipeline tasks produce sparse networks organised around local interfaces. Shared files can replace repeated 1-to-1 communication, cutting output tokens by about 42% at eight agents on message-heavy work, while adding overhead when files already carry the coordination. Naming one agent as coordinator creates no communication hub and provides no reliable improvement in success. We also observe an unprompted tendency for agents to seek out hidden grading material. We repeat the key experimental conditions in a sealed environment, replacing the hidden material with marked placeholder files. Across 244 additional runs, agents still reach for it in four fifths of runs, while the coordinator and file-channel findings reproduce.

---


### 331. [Diagnosing Dense Same-Class Attribute Misbinding in Large Vision-Language Models](https://arxiv.org/abs/2608.16805)

**<font color=#1a73e8>作者：</font>** Yuanzhi Xu, Qian Gao, Jun Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models can recognize the objects and attributes in a crowded scene yet assign an attribute to the wrong same-class instance. Generic visual-question-answering accuracy marks the response as wrong, while object-hallucination metrics may regard both the object and attribute as image-supported; neither reveals the transfer. This study formalizes this blind spot as Dense Same-Class Attribute Misbinding (DSCAM) and presents InstaBind-Lite, a controlled benchmark that makes it directly measurable. Its 524 images contain 529 curated groups of 3-6 same-class entities, 1773 boxed instances, ordered neighbors, distinguishable color-like attributes, and four complementary question levels, yielding 9580 deterministically evaluated questions. Unlike existing protocols, source-instance annotations separate unsupported generation and recognition failure from an attribute copied from another visible entity. Binding-specific metrics further quantify transfer frequency, adjacency, ordinal distance, and intervention effects. Across five open-source and two commercial/API models, the open-source systems average 19.84% Misbinding Rate and the API systems 7.55%; these errors are hidden by aggregate accuracy. Among identifiable transfers, 80.70% and 81.51%, respectively, originate from adjacent instances. Localization and instance-first interventions help selected models but are not universal remedies. InstaBind-Lite therefore turns previously undifferentiated wrong answers into source-identifiable failure categories and tests a reliability dimension that conventional benchmarks cannot determine: whether a model knows not only what is visible, but which instance owns each attribute.

---


### 332. [GEO-Flag: Detecting and Measuring GEO-Optimized Web Content](https://arxiv.org/abs/2608.16824)

**<font color=#1a73e8>作者：</font>** Junjie Chu, Ye Leng, Mingjie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Engine Optimization (GEO) modifies web content to increase its likelihood of being selected and cited by generative search engines. This can give strategically optimized pages visibility disproportionate to their authority or relevance and even make weak or false information appear well supported. Unlike conventional search, generative search synthesizes information into direct answers rather than presenting competing sources, which can further amplify these risks, as assessing source provenance and authority requires additional user interaction. Despite these concerns, systematic methods for detecting GEO-optimized webpages remain underexplored. We introduce \texttt{GEOFlagBench}, a benchmark of 3,200 webpages spanning 400 queries, four domains, and eight GEO optimizer families, and use it to systematically evaluate existing GEO detection methods. Although the strongest baseline achieves an aggregate F1 of 0.880, method-level and authorship-conditioned evaluations reveal substantial weaknesses and potential reliance on authorship-related shortcuts. We therefore propose \emph{Intervention-Paired Training} (IPT), which supervises detector responses to GEO interventions and non-GEO AI polishing; on ModernBERT, IPT improves F1 from 0.862 to 0.944 and worst-group accuracy from 0.725 to 0.883. We develop a GEO-gated Agent system for auditing the Source Tier and verifiability of Citation URLs in detected GEO pages. Finally, we deploy the complete pipeline on released Google Search and Gemini-grounded retrieval results for 1,000 real-user queries. Across 10,095 available pages, we estimate an overall GEO prevalence of 8.90\%, reaching 16.36\% among pages modified in 2026. Our results establish a foundation for systematically detecting, auditing, and measuring GEO in real-world search ecosystems.

---


### 333. [Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning](https://arxiv.org/abs/2608.16831)

**<font color=#1a73e8>作者：</font>** Minh-Ha Nguyen, Cathy Shyr  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative pretraining established reusable task representations; later work on language-based task conditioning and in-context learning showed that a fixed model could adapt its behavior from instructions and demonstrations. Policy Iteration with Human Feedback (PIHF) builds on this development and the recurrent evaluate-and-improve structure of generalized policy iteration. PIHF uses a pretrained language model as its execution substrate and moves persistent revision to a versioned natural-language policy and tool set. A language-model critic and clinical expert review complete-panel reasoning and tool-use trajectories to localize recurrent failures and form candidate revisions; the expert may reinterpret the evidence and retains authority over admission and rollback, while Recall@1 and Recall@5 validate outcomes after candidate execution.
Across cumulative ablations and ultra-rare-disease benchmarks, a PIHF-derived policy improved Recall@1 in one proprietary executor and three open-weight executors spanning 3 to 49 billion active parameters. Gains were 32.7 percentage points for GPT-5.4 and 31.1 points for Qwen3.6-35B, a difference of 1.7 points. These results support the feasibility of using pretrained language models as fixed-weight execution substrates for expert-guided policy development in rare-disease diagnosis.

---


### 334. [What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models](https://arxiv.org/abs/2608.16852)

**<font color=#1a73e8>作者：</font>** Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regulatory compliance monitoring in deployed language models is increasingly implemented as a legal and audit control, checking model outputs against written rules spanning data protection, healthcare, financial regulation, and platform policy. Such monitoring is meaningful only if a detector's verdict depends on the stated rule rather than on surface features of the scenario. We show this condition fails across the current class of compliance detectors, a failure we call rule blindness. Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test, including a policy-conditioned guard that correctly cites the governing clause yet barely changes its verdict when that clause is swapped for its permissive counterpart. A purpose-built benchmark crossing two rules with two scenarios, so that neither alone predicts the label, confirms the failure under a design no prior benchmark rules out, and shows that step by step reasoning, not any fast detector we test, is what escapes it. Auditing at scale requires a retraining-free detector, so we introduce the Internal Compliance Score (ICS): a training-free activation readout calibrated from ten labelled pairs and scored by a single projection. We hold ICS to the same scrutiny as the guards it audits: a pre-registered criterion for beating trivial baselines is not met, and a bag-of-words model matches its pooled generalisation exactly. It remains useful because it is inexpensive, letting us audit four deployed guard models, an 8B zero-shot judge, and thirteen benchmarks, and it raises the mechanically verified pass rate when used to rank candidate responses, though an adaptive white-box attack removes this gain. We release the counterfactual protocol and crossed-rule benchmark so rule blindness can be tested in future probe and guard claims.

---


### 335. [HarnessEval-W: Agentifying the Evaluation of Visual Worlds](https://arxiv.org/abs/2608.16859)

**<font color=#1a73e8>作者：</font>** Weiliang Chen, Haowen Sun, Jun Gao 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A benchmark should deliver more than a scalar score: what makes an evaluation trustworthy is the reasoning that justifies the score. This is especially critical for world models, where judging a rollout requires understanding whether physics, causality, and world state evolve correctly. Humans spot such violations naturally, yet no existing benchmark automates this capability: metrics are computed brute-force, leaving no reasoning chain that can be examined or verified. We introduce HarnessEval-W, an agentified evaluation pipeline that brings the harness paradigm from the LLM ecosystem to world model benchmarking. Rather than applying a fixed rubric, HarnessEval-W interprets the context of each evaluation case, decomposes the evaluation question into measurable subproblems, and spawns specialized sub-agents, each equipped with tailored context and diagnostic tools to reason over its own subproblem. The parent agent then validates the gathered evidence and summarizes it into the final verdict. This hierarchical workflow turns every evaluation into a transparent evidence tree whose complete reasoning chain justifies the result. We apply HarnessEval-W to 18 representative world models over 330 evaluation cases. Its judgments closely align with human preferences while providing verifiable, fine-grained diagnoses of every generated rollout. We open-source the full pipeline as a live benchmark and invite the broad community to contribute to grow new skills and evaluation cases as world models evolve.

---


### 336. [Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text](https://arxiv.org/abs/2608.16868)

**<font color=#1a73e8>作者：</font>** Benjamin Belay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model's output does not by itself provide verifiable evidence about the internal computation that produced it. We study computational provenance: whether generated text can carry detectable evidence of which causally relevant internal state occurred. We test a bounded form of this idea in two controlled architectures: a modular feed-forward neural network and a transformer-based model. Both architectures are trained on the same arithmetic task with a mandatory pathway through two discrete intermediate states, allowing different internal paths to produce the same answer. We deliberately switch between these paths, authenticate the state actually used, and let that verified state determine a subtle statistical pattern in the generated text that can later be detected. The feed-forward and transformer systems each passed all 128 matched pairs in both their public and separately sealed protected end-to-end evaluations, with the detector recovering the signal associated with the authenticated internal state. The required causal computation also reproduced across five independently trained feed-forward models and three independently trained transformers. In a separate answer-only transformer experiment, our linear probes did not recover a naturally learned intermediate state. These results provide a controlled proof of concept that information about a verified, causally relevant internal state can be preserved in generated text even when the answer is unchanged.

---


### 337. [Evaluating Beyond the Screen: Collective Assessment of AI-Generated Business Plans with Resource-Constrained Entrepreneurs](https://arxiv.org/abs/2608.16886)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Marjory Pineda, Ketul Chhaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Entrepreneurs increasingly use end-user generative AI technologies such as ChatGPT for high-stakes documents like loan applications and business plans, where AI-generated errors---a wrong price, a fabricated product---can affect loan or funding outcomes. Current approaches to supporting evaluation of AI-generated text assume a single user assessing output alone, on screen. This can be especially demanding for resource-constrained entrepreneurs, whose digital and AI skills vary widely. In this early-stage work, we explore how evaluation might instead be organized in a group setting and completed as a collective activity. We extended BizChat, an AI-powered business-planning tool, with an evaluation module that links each generated claim to the entrepreneur's original input. We partner with community organizations in Maryland---embedding BizChat within various entrepreneurship programs---where workshop attendees (N=14) evaluated their plans through think-pair-share discussion. Early findings suggest interface scaffolds like claim-to-input links primed attendees with concrete, personal evaluations, which the group setting then extended beyond the screen: attendees requested printed copies, used rubrics to compare across plans, and drew on peers' knowledge to verify what they could not easily judge alone.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 338. [A Comprehensive Survey of Wireless Foundation Models for AI-Native 6G Networks](https://arxiv.org/abs/2608.14694)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Naveed Khan, Besan Al Sbeihi, Maryam Alshehhi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are emerging as a transformative paradigm for AI-native sixth-generation (6G) wireless networks by enabling scalable, transferable, and data-efficient intelligence across diverse communication tasks. Unlike conventional deep learning models that are trained for individual applications, wireless foundation models (WFMs) learn generalized representations from large-scale heterogeneous wireless data and can be efficiently adapted to communication, sensing, localization, and network optimization tasks with minimal task-specific supervision. Despite rapid progress, current research remains fragmented across architectures, training paradigms, and application domains, with no unified survey dedicated to the design, learning, and deployment of WFMs. This survey presents a comprehensive and unified review of wireless foundation models. We first establish the fundamental concepts of WFMs and introduce a taxonomy that organizes the field according to model architectures, pre-training paradigms, and applications. We then review representative architectures, self-supervised pre-training strategies, parameter-efficient adaptation methods, datasets, benchmarks, and evaluation methodologies, highlighting their roles in enabling transferable wireless intelligence. Furthermore, we examine emerging applications spanning physical-layer signal processing, network intelligence, and cross-layer optimization, and discuss the key challenges of data availability, generalization, interpretability, efficient edge deployment, and standardization. Finally, we outline future research directions toward scalable, trustworthy, and general-purpose wireless intelligence for AI-native 6G networks. This survey provides a comprehensive reference for researchers and practitioners developing next-generation intelligent wireless systems.

---


### 339. [Deep Analog: Open-Set Film Emulation with Reference-Conditioned 3D LUTs](https://arxiv.org/abs/2608.14702)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yitong Mu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Film emulation reproduces the look of an analog film stock on a new digital photograph. We target its open-set form -- matching any reference film frame from a single example -- with a 3D lookup table (LUT) predicted from that reference. Real-time image enhancement predicts per-image weights over a fixed bank of 3D LUTs and blends them. We show this is a gated mixture of experts and inherits its failure: trained end-to-end against reconstruction, the gate collapses onto a single expert, so a bank of K LUTs delivers the capacity of one. An entropy term, the enhancement-setting analogue of mixture-of-experts load balancing, restores utilization and recovers about 1 dB PSNR. The deeper constraint survives: a fixed LUT basis is closed-set, freezing the achievable looks at training time. We therefore discard the basis and predict a single 3D LUT as a residual from a reference image (StyleLUTNet), trained by self-supervision on procedurally generated color transforms. The conditional design removes the gate and generalizes open-set to unseen film stocks without paired data or retraining. Around this color backbone we build Deep Analog, a film-emulation pipeline that adds histogram-based tone matching and a physics-informed optical renderer -- multi-scale grain and per-channel halation driven by parameters an inverse network regresses from the reference. On 350 self-supervised pairs the color stage reaches 22.05 dB PSNR / 0.925 SSIM and the full pipeline 21.72 dB / 0.923; the color path runs in 5.2 ms at 1080p (192 FPS) and exports a portable .cube LUT for standard editing tools. A second degeneracy in conditional LUT training -- residual-scale collapse -- shares the root cause and yields a general principle: auxiliary regularization must stay subordinate to reconstruction.

---


### 340. [Zero-Shot Adaptation of Medical Vision Foundation Models for High-Frequency Micro-Ultrasound Prostate Segmentation](https://arxiv.org/abs/2608.14796)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ayusha Abbas, Saram Abbas, Kabita Adhikari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prostate cancer claims a life every 80 seconds. Early detection is needed to prevent disease progression, and both PSA density calculation and biopsy decisions rely on knowing the exact boundary of the gland. Conventional ultrasound at 6-12 MHz blurs this boundary, missing one in three high-risk cancers. Micro-ultrasound (29 MHz) improves resolution threefold but introduces dense acoustic speckle that obscures the outer wall; given the same image, two clinicians draw outlines differing by over 10% in area. Supervised methods are costly and generalise poorly across scanners. Can a foundation model segment the prostate with no training data?
We present the first zero-shot pipeline for this modality: MedSAM, pre-trained on over 1.5 million medical images, localises the prostate; we then apply CLAHE to sharpen the outer wall, binary dilation to recover missed pixels, and Fourier smoothing (4 modes, s=1.05) to refine the boundary. MedSAM requires a spatial prompt, so we evaluate bounding-box and point-click strategies across 75 patients of the Micro-Ultrasound Prostate Segmentation dataset (2,621 slices).
On the 20-patient held-out test set, the pipeline reduces mean boundary-distance error by 45% (Dice 0.749+/-0.043 to 0.865+/-0.029; HD95 217.2+/-36.9 to 120.1+/-26.1 px), reaching Dice 0.859 across the cohort. Its mean overlap shows no significant difference from the three non-expert rater groups (p>0.19), while segmenting 38-52% more consistently (lower inter-patient standard deviation). Point-click prompts fail regardless of placement (best Dice=0.350), because speckle gives no stable local contrast. Only an approximate bounding box is required, so any clinic can deploy it without data collection, annotation, or retraining.

---


### 341. [Skill Blocks: How Should an Agent Load Its Skill? A Caching-Correct Comparison of Pre-load, On-Demand Tool-Loading, Progressive Disclosure, and Hybrid](https://arxiv.org/abs/2608.14943)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hironobu Nakasuji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are often injected in full on every request, increasing token cost. We compare four content-preserving loading methods: Full, Skill Block, Reference, and Hybrid. Across SearchQA, SpreadsheetBench, ALFWorld, ScienceWorld, and SynthProc, we measure token usage using raw input for single-turn tasks and cache-correct effective input for multi-turn tasks. Results show no universal winner. Hybrid reduces input by 27.4% on SearchQA and 39.8% on SpreadsheetBench. On large multi-turn skills, Skill Block and Hybrid achieve substantial reductions, reaching 62.5% and 52.8% on ScienceWorld and 73.0% and 66.6% on SynthProc. ALFWorld shows smaller gains because procedures are short and repeatedly needed. Paired outcome tests detect no quality differences, though they do not establish equivalence. Overall, conditional loading is most beneficial when large portions of a skill are not needed on every turn.

---


### 342. [Beyond Natural-Image Foundation Models: Benchmarking Satellite Pretraining for Ophthalmic Image Analysis](https://arxiv.org/abs/2608.15195)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lovre Antonio Budimir, Mingya Alexa Gong, Alyssa Foong Quinney 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) have emerged as a promising approach in medical imaging, producing broadly applicable systems that can be efficiently adapted across diverse imaging modalities, anatomical regions, and clinical tasks. However, VFMs require extensive training data, and their progress in medical image analysis is constrained by limited data availability, privacy concerns, and high development costs. To alleviate these constraints, medical VFMs (MedVFMs) are often built upon weights from generalist models pretrained on vast amounts of publicly available natural images, introducing a substantial distribution shift for medical task adaptation. To address this, we propose satellite imagery as a novel pretraining domain for MedVFM development and benchmarking, motivated by its closer visual alignment with medical data and its freedom from the privacy constraints that limit medical datasets. Across multiple ophthalmic imaging modalities, we compare DINOv3-SAT493m pretrained on 493 million satellite images against DINOv3-LVD1689m pretrained on 1.7 billion natural images, together with two medical specialist baselines: DINOv3-RETFound and MAE-RETFound. Our experiments show that satellite imagery is a stronger pretraining source than natural images for ophthalmic tasks, particularly on en face vascular-rich modalities. On several tasks, satellite pretraining matches or exceeds the medical specialists on high-resolution en face inputs, despite using no medical data.

---


### 343. [Earth Observation Foundation Models for Terrestrial Ecohydrology: From Representation Learning to Process Inference](https://arxiv.org/abs/2608.15282)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yi Yu, Jian Peng, Yucheng Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earth observation foundation models (EOFMs) are emerging as reusable representation frameworks for data-driven retrieval, prediction and process modelling within ecohydrology, which integrate EO, meteorological forcing and process models to characterise coupled water, energy and carbon dynamics in vegetation and soil across scales. However, there is yet to be an ecohydrology-specific synthesis assessing the EOFM relevance, application evidence or evaluation requirements under uncertain reference data, scale mismatch and temporal dependence. Here, we develop a framework for determining when EOFMs support interpretable inference and identify a mismatch between EOFMs and ecohydrological requirements. Firstly, an observation-to-inference hierarchy shows that relevance depends on target-specific sensing pathways, spatial-temporal support and traceable uncertainty. Secondly, a meta-analysis shows that pretraining is dominated by reflected optical and active-microwave data, with sparse thermal coverage and no passive-microwave-emission sources. Thirdly, our synthesis of ecohydrological applications finds strongest support for spatial context, label-efficient adaptation and hybrid workflows. Evidence declines with inference depth; independent validation of fluxes, coupled dynamics, event trajectories, calibrated uncertainty and decision benefits remains sparse. Fourthly, our benchmark audit finds stronger coverage of fair adaptation and reproducibility in general EOFM suites, and of process targets, direct reference evidence and distribution shifts in ecohydrological evaluations; physical consistency and uncertainty remain weakly assessed. These findings motivate a process-aware framework aligning EOFM design and evaluation with the target variable, observation pathway and process timescale, supporting trustworthy monitoring and interpretation of coupled water, energy and carbon dynamics.

---


### 344. [Spectral Rank Certification for Foundation Model Adapters](https://arxiv.org/abs/2608.15351)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mohammed Ahnouch, Lotfi Elaachak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nominal LoRA rank is a design parameter; calibrated spectral evidence is a separate inferential quantity. This article develops a finite-sample framework for inferring effective rank structure in public foundation-model adapters. The theoretical core is an exact chi-square divergence for the fixed-dimensional Gaussian rank-one reference experiment, with an unknown signal direction integrated under a rotation-invariant reference prior. The resulting series yields a computable finite-sample Le Cam bound at concrete layer sizes, an explicit remainder bound for numerical truncation, and the rectangular Baik-Ben Arous-Peche (BBP) limit. A compact-manifold Laplace expansion shows that finite-sample likelihood evidence also depends on leading spectral gaps through the factor $s_1^{|m-n|}\prod_{i\ge2}(s_1^2-s_i^2)$, motivating joint calibration of clustered singular values. Building on these results, we introduce an empirical-null workflow for PEFT LoRA adapters: factor reconstruction, Monte Carlo $p$-values, stagewise and block testing, and module-wise and corpus-level BH reporting. In an audit of 26 public adapters, 684 modules, six architecture families, and 31,770 public-checkpoint spectra rows, calibrated effective rank is typically much smaller than nominal rank and differs systematically from 95\% energy retention. A measured RoBERTa-RTE slice on $n=24$ examples illustrates the measurement path from calibrated ranks to task evaluation, without treating the slice as a utility study. The main empirical finding is that calibrated effective rank is usually far below nominal rank, and that energy retention and statistical surprise answer different questions.

---


### 345. [AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models](https://arxiv.org/abs/2608.15456)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Md Aminur Hossain, Omkumar Vaghasiya, Rajeev Ranjan Dwivedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing (RS) foundation models provide transferable Earth observation representations across sensors, resolutions, and geographies, yet most remain weakly aligned with natural language, limiting natural-language archive search, image-text retrieval, and question-conditioned analysis. We propose AlignJEPA, a JEPA-inspired predictive vision-language alignment framework for remote sensing foundation models. AlignJEPA uses a pretrained AnySat visual encoder and a RemoteCLIP text encoder while training only a lightweight predictive alignment network. Instead of relying on global image--text contrastive alignment alone, the framework predicts remote-sensing text embeddings from masked visual foundation-model tokens. Its mask-aware multi-scale predictive aligner aggregates visible tokens at fine, regional, and global scales, jointly models them with a cross-scale Transformer, and projects the resulting representation into the text space using learned query pooling. Training combines semantic prediction with bidirectional contrastive retrieval. We train and evaluate AlignJEPA on this http URL for natural-language Sentinel retrieval, evaluate cross-dataset adaptation on RSICD, and use RSVQA only as a closed-set representation probe. AlignJEPA provides a parameter-efficient route for aligning Earth observation foundation models with language.

---


### 346. [PERO: Efficient Robust Post-Training Foundation Models for Encrypted Traffic Classification](https://arxiv.org/abs/2608.15504)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wumei Du, Jiarong Wen, Kaiyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encrypted traffic classification is vital for network security, yet real-world deployments are inherently sensitive to rare but high-loss errors such as misclassification of malicious traffic. The encrypted traffic foundation model, as a promising general-purpose technique, can achieve impressive overall performance. However, employing standard objectives such as empirical risk minimization often overlooks high-risk tail events, and commonly used performance metrics hardly reflect robustness limitations in risk-sensitive scenarios. Directly applying robust optimization objectives, such as conditional value-at-risk, to post-training is computationally prohibitive for large models, as identifying high-loss samples exhausts substantial computation. To this end, we propose Pre-Evaluation Robust Optimization (PERO), an efficient robust post-training framework for encrypted traffic foundation models. PERO employs a lightweight proxy to estimate sample-wise risk and selects a subset of high-risk samples to update the foundation model, decoupling risk estimation from expensive large-model optimization. Extensive experiments on typical encrypted traffic datasets show that PERO achieves competitive or superior robustness and average performance compared to outstanding robust post-training methods, while significantly reducing computational and memory costs.

---


### 347. [Toward AI-Friendly Cartography: Understanding How Color Design Influences Foundation Model Spatial Reasoning on Sequential Choropleth Maps](https://arxiv.org/abs/2608.15736)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yonghe Sun, Zhenjia Liu, Hua Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) increasingly support multimodal and geospatial reasoning, yet it remains unclear whether cartographic principles designed for human perception are equally effective for machines. Focusing on sequential choropleth maps, we examine how hue palette, color ordering, and lightness contrast influence FM spatial reasoning. We construct a controlled benchmark of 5,760 maps and 28,800 questions spanning Attribute Identify, Spatial Recognition, Compare, Rank, and Pattern Delineate, and evaluate 21 open-source and proprietary multimodal FMs. Results show that hue choice has limited and inconsistent effects, whereas disrupting sequential color ordering substantially reduces performance, especially for comparison and ranking. Reduced lightness contrast also consistently impairs reasoning, while increasing contrast beyond sufficient separability provides only marginal gains. LoRA fine-tuning improves overall accuracy but preserves these relative sensitivities. Additional factorial experiments further indicate that errors arise from color-and-legend decoding, spatial reasoning, and the integration of thematic attributes with spatial structure. These findings show that conventional sequential ordering and sufficient contrast remain important for machine map understanding and provide empirical guidance for AI-friendly cartographic design.

---


### 348. [Conjunctive Poisoning in AI Supply-Chain Applications](https://arxiv.org/abs/2608.15913)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nokimul Hasan Arif, Qian Lou, Mengxin Zheng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language and Vision-Language Models are increasingly deployed through inference pipelines that include prompt wrappers (e.g., templates and post-processing scripts) and configuration metadata (e.g., JSON/YAML files) that together shape model outputs. While model weights and binaries are routinely verified, these textual deployment artifacts remain weakly protected despite directly influencing runtime behavior. We show that a malicious developer can pair a benign-looking wrapper with crafted metadata to deterministically alter post-generation behavior without modifying model weights, training data, or inference backend. We study this behavior through a controlled conjunctive-gate implementation, where activation depends on both an embedded wrapper marker and cryptographically bound metadata. We evaluate the attack across fifteen open- and closed-source LLM/VLM deployments, and assess prompt and system level defenses including static metadata inspection, wrapper scanners, PromptShield, and SigStore-based artifact signing. To mitigate this risk, we introduce TIF-BAH, a lightweight middleware defense that verifies wrapper integrity and records behavioral attestations during inference. Our results reveal that wrapper-metadata interactions form an under-protected execution layer in modern AI deployments, exposing a deployment-time behavioral risk that is not captured by model-weight or prompt-level defenses. Code is available at this https URL.

---


### 349. [Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval](https://arxiv.org/abs/2608.16044)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Prashant Kumar Pathak, Tarun Kumar Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) answers a question by retrieving passages from a vector store and trusting them as context, so anyone who can add documents can try to steer the answer. A recent, appealing defense filters poisoning at ingestion, rejecting any document that behaves like a hub. We show it -- and every ingestion-time filter -- is defeated by a coordinated adversary that injects a handful of individually unremarkable documents which together surround one target query and seize its top-k (on BGE-large / BEIR, m=10 documents take 10/10; 9.9/10 on a live HNSW index). The attack is not theoretical. Realized as ordinary fluent text and run end-to-end through a BGE-large + HNSW + Qwen2.5-7B pipeline, it makes the generator emit the attacker's planted claim in 88% of targets, versus 0% without the injection. And no admission-time defense stops it: at ingestion an attack cone is geometrically identical to a legitimate niche upload, so -- measuring this directly -- the strongest trained classifier, given every feature and thousands of examples, separates the two no better than chance, catching 4.2% of attacks at a 1% false-positive rate. We prove this limit for the entire class of ingestion-time statistics (any decision from documents and reference queries alone), and it reproduces -- and worsens -- across two corpora and five encoders. The one signal that separates an attack from legitimate niche ingestion -- a query's demand -- is invisible before retrieval, which is also the escape: a retrieval-time detector that observes demand catches 100% of the attacks at the same 1% false-positive rate. Coverage of the query space by an admission gate is not containment of coordinated poisoning; robust defense must move past the front door, to demand.

---


### 350. [CoM$^3$eT: A foundation model for medical image analysis through federated, multidimensional context integration](https://arxiv.org/abs/2608.16268)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** J. Raphael Schäfer, Kai Geissler, Till Nicke 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical foundation models improve generalization when training AI models with limited labeled data, but remain confined to a single specialty, such as pathology or radiology, and to either sparse or dense outputs, such as classification or segmentation. Here, we present CoM$^3$eT (Co-representation Multidimensional Multitask Medical Transformer), a medical vision foundation model that unifies pathology and radiology, sparse and dense predictions, and two- and higher-dimensional inputs by modeling multidimensional context with attention. CoM$^3$eT outperformed other medical foundation models in an open competition spanning five tomographic, four whole-specimen, and three two-dimensional datasets, covering sparse and dense prediction tasks as well as report generation. When adapted across diverse clinical applications, training fewer than 2.5% of parameters achieved performance comparable to full fine-tuning, enabling research without access to high-performance GPU clusters. Applied to federated learning across hospitals, this approach achieved performance comparable to pooled-data training over internet connections and with consumer-grade hardware.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
