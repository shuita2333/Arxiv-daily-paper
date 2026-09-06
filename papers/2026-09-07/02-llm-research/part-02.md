# 🧠 大模型相关研究 | 2026年09月07日

> 本类共 **180** 篇论文：已确认 **169** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-180](./part-04.md)

---

### 51. [How Perturbations Propagate: A Multi-Level Analysis of Robustness in Large Language Models](https://arxiv.org/abs/2609.03322)

**<font color=#1a73e8>作者：</font>** Dun Li Chan, Emily Liu, Niyathi Allu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models encounter typos, corrupted text, altered words, and disrupted token order, yet robustness is usually evaluated only through output behavior. We study how six naturalistic and synthetic input perturbations propagate through decoder-only language models at three levels: output behavior, hidden-state geometry, and attention-head function. We evaluate behavioral effects across four GPT-2 and two Qwen2.5 checkpoints by analyzing layerwise geometry using centered kernel alignment and intrinsic dimension, and examine attention-head responses in GPT-2. Perturbation types produce distinguishable metric profiles that are not fully captured by output measures and are only partly consistent across the tested checkpoints. Copying scores are especially associated with activation-patching recovery under token substitution and shuffling. Gradient-guided HotFlip perturbations also cause stronger behavioral and representational disruption than rate-matched random token substitutions in GPT-2; their behavioral effects are consistent across all six tested checkpoints. Our results show that robustness claims based on a single behavioral or representational metric can be misleading, and motivate multi-level evaluation of how perturbations alter language-model computation.

---


### 52. [DE-Venus: A Data-Efficient RLVR Framework for Large Language Models](https://arxiv.org/abs/2609.03324)

**<font color=#1a73e8>作者：</font>** Shenzhi Yang, Guangcheng Zhu, Kai Tang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves large language model reasoning, but its practical scaling is constrained by expensive on-policy rollouts and the cost of obtaining reliable targets at scale. Existing methods address sample selection, incomplete supervision, or noisy labels separately, often entangling supervision logic with distributed training and hindering controlled comparison and reuse. We present DE-Venus, a unified framework for data-efficient RLVR that treats supervision as evolving state across data preparation and policy optimization. It organizes this lifecycle into three modules: Active Data Selection allocates training and annotation budgets; Weak Supervision Construction derives learning signals from unlabeled examples; and Training-Time Supervision Refinement filters or corrects unreliable supervision. DE-Venus supports seven representative methods and a data-selection pipeline by expressing method-specific decisions as offline dataset transitions or online transformations of targets, rewards, batches, and advantages while preserving verl's distributed execution contracts. Across public benchmarks and three business scenarios, separate configurations preserve or improve model quality with only 10% of labels or as little as 13% of relevant data; selected business configurations also reduce observed convergence steps by 63%--75%. DE-Venus thus reduces annotation and training costs without sacrificing scalable RL execution.

---


### 53. [Less Is Moral: A CHARMing Framework for Moral Foundations Detection in Endorsement Behaviour](https://arxiv.org/abs/2609.03330)

**<font color=#1a73e8>作者：</font>** Huixiang Fu, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moral language plays a central role in shaping online endorsement and the diffusion of information, yet existing moral foundation detection systems often suffer from poor cross-domain generalization, weak rationale grounding, and reliance on costly prompting-based large language models (LLMs). We introduce CHARM, a MA\textbf{C}- and \textbf{H}ate-speech-\textbf{A}ware \textbf{R}ationale-aligned \textbf{M}oral foundation detection framework built on a lightweight fine-tuned LLM, which integrates complementary moral grounding, rationale alignment, and polarity-aware hate speech signals to support more robust and faithful moral prediction. Unlike prior dictionary-, fine-tune-, or prompt-based detectors, which decouple computation from psychological theory, CHARM is built so that each component -- MAC cross-attention, rationale alignment, and hate-speech modulation -- operationalizes a distinct psychological construct. Using a 30\% subsample of the MFTC, MFRC, and News training pools together with the richer supervision in MFTCXplain, CHARM improves AUC by up to 15.3\% in-domain, surpasses the supervised baselines on every out-of-domain dataset in both AUC and F1, and offers a scalable, low-cost alternative to prompting-based LLM detectors. We further apply CHARM to large-scale COVID-19 discourse on Twitter and show that moral value alignment is strongly associated with online endorsement behavior. By making moral framing measurable at scale, CHARM offers a practical tool for studying the spread of morally charged misinformation.

---


### 54. [FPCO-Dialog: A Multi-Turn False-Premise Benchmark for Correction and Cooperation in Vision-Language Models](https://arxiv.org/abs/2609.03331)

**<font color=#1a73e8>作者：</font>** Jiayuan Ma, Yuqi Lu, Weiyang Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed in multi-turn settings where users may describe visual content with incorrect assumptions. Yet existing evaluations rarely isolate how models respond when the same visually grounded false premise persists across dialogue turns. We introduce FPCO-Dialog, a benchmark for evaluating correction and cooperation behavior in VLMs under repeated false premises. FPCO-Dialog contains 1,080 images and 10,800 question turns, stratified by visual complexity, object category, and false-premise class, and uses a 10-turn protocol in which a correct dialogue prefix is followed by repeated false-premise referring expressions. We evaluate 20 commercial and open-source VLMs with a model-agnostic protocol and CorrTP@K, a correction-rate metric over false-premise turns, scored by two independent detectors. FPCO-Dialog reveals substantial and persistent cross-model differences in aggregate correction tendency, model-specific turn-wise dynamics, and systematic variation across false-premise types under the benchmark's substitution distribution. The dataset, evaluation protocol, model outputs, detector labels, and code are available.

---


### 55. [Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory](https://arxiv.org/abs/2609.03340)

**<font color=#1a73e8>作者：</font>** Evan Chen, Shiqiang Wang, Christopher G. Brinton  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan. A planner may derive an action from requirement $r_3$, another agent may commit $r_4$, and an executor may receive $r_4$ without replacing the plan derived from $r_3$. We call this \emph{stale-plan execution}: state freshness does not establish that the plan authorizing an action remains valid. We introduce PlanFence, a dependency-scoped action-validation protocol. Plans cite the exact public records they used, and an executor validates only the records that can affect the pending external action, replanning once or blocking when validation is incomplete. In 30 controlled live workflows with a post-plan revision, a freshness-only executor acts on the obsolete plan in every task, whereas PlanFence completes all tasks without an invalid action. Controlled replay reveals two conditional boundaries: proactive synchronization yields lower coordination stall at low churn, while PlanFence avoids repeated update-path coordination as churn grows and avoids validating unrelated state as the shared keyspace grows. These are controlled safety and systems-cost results, not general task-accuracy gains.

---


### 56. [Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards](https://arxiv.org/abs/2609.03342)

**<font color=#1a73e8>作者：</font>** Leqi Zheng, Jinbo Su, Fang Niu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) drives chain-of-thought reasoning in large language models, yet its binary outcome reward cannot distinguish among correct trajectories. Existing dense reward alternatives, from surface heuristics to process reward models, either ignore the expert solutions already present in training corpora or require expensive offline annotation. We propose Gradient-Aligned Reward (GAR), which operates in the policy's own gradient space: truncated backpropagation through the output projection layer extracts a compact gradient vector for each rollout, and cosine similarity with an expert-anchor gradient yields a dense, reasoning-aware reward with less than 9% wall-clock overhead. We prove that this cosine admits a multiplicative decomposition into prediction-error and activation-pattern factors, providing a concrete characterization of what the alignment signal measures. On Qwen3-4B and Qwen3-8B, GAR consistently improves over GRPO and other baselines on competition-level math benchmarks and transfers to GPQA Diamond and MMLU-Pro without domain-specific data. Code and data are available at this https URL.

---


### 57. [From Zero to Hero: An Open LLM Ecosystem for Armenian](https://arxiv.org/abs/2609.03350)

**<font color=#1a73e8>作者：</font>** Erik Arakelyan, Khatun Avetisyan, Meri Davtyan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining data for Armenian, a morphologically rich and low-resource language, is scarce, and no open Armenian LLM has been released with the data and recipe needed to reproduce it. To address this gap, we curate and release two datasets. ArmWeb is an extensively validated corpus of 4.37M Armenian news documents. ArmSTEM is a parallel English-Armenian collection of 373K math and science problems with step-by-step solutions, translated into Armenian and verified through both answer-preserving LLM judgment and human evaluation. Continued pretraining of Gemma-4-E4B on these datasets yields arm-gemma-e4b, which outperforms every existing open Armenian model as well as its unadapted base, and is the first open Armenian LLM with complete training data and recipe. Our ablations show that news-only continued pretraining improves fluency while eroding knowledge, a pattern we also observe in existing Armenian models, and that a small share of verified translated STEM data reverses the loss. We further find that the largest public Armenian corpora overlap web-derived evaluation panels heavily, including a train/test self-overlap inside FineWeb-2. We openly release all data, models, and code.

---


### 58. [Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT](https://arxiv.org/abs/2609.03366)

**<font color=#1a73e8>作者：</font>** Zikai Zhou, Yufei Jin, Yilin Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accountability means a decision can be examined, justified, and contested. LLMs make this hard: fluent output may be ungrounded, incomplete, or unfaithful to the decision process. Achieving accountability requires verified rationales (how was the decision reached), assumptions (what was assumed rather than known), policy consistency (the same treatment for the same facts), and pivotal conditions (what would change the outcome). We introduce self-faithfulness as an automatic test of accountability: changing the pivotal conditions should change the decision.
We examine accountable AI through clinical trial matching, a high-stakes task central to evidence-based medicine. Although LLM-based matchers match patients to trials reasonably accurately, they apply decision policies inconsistently and produce rationales that are unfaithful to their own decisions.
We introduce VERDICT, an LLM-based agent that translates a decision task, its constraints, and its policy into Satisfiability Modulo Theories (SMT), then derives the decision with SMT and MaxSMT solvers -- so policies are applied consistently and decisions are accountable by construction.
Across a SIGIR 2016-derived dataset and TREC 2021, VERDICT achieves the strongest decision accuracy among LLM-only and neurosymbolic baselines, applies policies with perfect consistency, and produces clinician-preferred rationales grounded in explicit assumptions and pivotal conditions, with improved counterfactual self-faithfulness.

---


### 59. [FrameBench:A Language Understanding Benchmark Based on Frame Semantics](https://arxiv.org/abs/2609.03370)

**<font color=#1a73e8>作者：</font>** Chihiro Yano, Ryohei Sasano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In frame semantics, sentence comprehension is assumed to proceed by relating lexical meaning to background knowledge called semantic frames, thereby enabling readers to implicitly enrich the text with unstated information. Recent large language models (LLMs) have achieved strong performance across a wide range of downstream tasks. However, it remains unclear whether they can reproduce the kinds of implicit enrichment that humans naturally make during comprehension. To address this question, we introduce FrameBench, a benchmark grounded in frame semantics. FrameBench consists of multiple-choice questions that test whether models distinguish the frames evoked by the same verb across contexts. We construct the benchmark for English and Japanese using FrameNet-style resources and a generation-and-verification pipeline with native-speaker judgments. Our experiments on a diverse set of models reveal challenges for small models, while several large models surpass the human reference scores. We release the constructed FrameBench dataset and the code for dataset construction and evaluation at this https URL.

---


### 60. [Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings](https://arxiv.org/abs/2609.03376)

**<font color=#1a73e8>作者：</font>** Peichun Hua, Yunming Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has made dense retrieval over large document collections a standard building block. Organizations increasingly outsource vector indexes to untrusted clouds, exposing proprietary corpora and user queries. Cryptographic protection is challenging because each query searches corpus-scale state, causing computation, correlated randomness, and communication to grow with the corpus. At million-document scale, a naive secure implementation takes minutes and about 90 GB of communication per query. Even recent optimized systems require 10--22 seconds.
We propose Spruce (Scalable Private Outsourced Retrieval Using Compact Embeddings), which co-designs representations with the cryptographic protocol. Spruce learns compact binary codes that preserve candidates for full-precision reranking, replacing corpus-wide embedding scoring with efficient Hamming-distance computation under two-server multi-party computation (MPC). A corpus-calibrated fixed-radius protocol avoids multi-round candidate selection while preserving retrieval quality. Spruce also provides private cluster pruning, which trades minor quality loss for substantially less computation, and a one-core owner-operated dealer that removes cloud OT preprocessing bottlenecks. Across four corpora containing 383K--5.42M documents, Spruce preserves the original search quality with median candidate sets of only 382--1,952. At 10 Gbps inter-server bandwidth, full scans take 0.21--2.97 seconds, $4.8$--$6.7\times$ faster than the closest measured prior work. Private pruning takes 0.06--1.09 seconds, achieves $13.1$--$22.9\times$ speedups, and retains $93.9\%$--$97.3\%$ of full-float NDCG. On the largest corpus, pruning and the dealer jointly improve sustained throughput by $31.5\times$ at 1 Gbps per link.

---


### 61. [RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory](https://arxiv.org/abs/2609.03379)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Kunyu Feng, Yingda Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeating a small block of middle layers increases a language model's effective inference depth without adding parameters or generating extra tokens, and recent work shows that this latent recurrence improves reasoning. However, two design choices limit these gains. Each iteration sees only the previous output and cannot directly access earlier computations. Moreover, a fixed loop count wastes depth on easy inputs while leaving hard ones with too little computation. We introduce RecurTrace, which addresses both limitations using the loop's own trajectory. Specifically, Loop Memory Attention lets each looped layer attend to its own states from previous iterations along the loop-time axis, so the model can revisit earlier computations instead of relying on the latest state alone. A halting head then reads the loop state and predicts whether to continue, with supervision from an oracle that identifies when additional depth still reduces loss. In a controlled MathQA comparison on the same looped backbone, RecurTrace achieves 56.9% accuracy with an average of 2.0 loops, exceeding the best fixed loop depth by 2.2 points at matched compute. By comparison, ACT and PonderNet collapse to one loop, and CALM reaches only 54.1% with 5.6 loops, while the stronger LoopUS-Conf and TaH-Mismatch baselines reach 55.3% at 3.2 loops and 55.7% at 2.1 loops. Finally, RecurTrace improves generation accuracy over same-budget fine-tuned baselines at 0.6B, 1.7B, 4B, and 8B, with the gain growing with model size from 0.6 to 3.4 points.

---


### 62. [TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.03383)

**<font color=#1a73e8>作者：</font>** Jinwei Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based policy optimization improves credit assignment for long-horizon LLM agents by organizing rollout trajectories into state-transition graphs. However, existing methods construct graphs independently within each policy update, discarding transitions discovered by earlier policies and limiting advantage estimation to small, batch-local rollout groups. We propose \emph{Temporal Instance-Graph Policy Optimization} (TIGPO), which extends graph-based credit assignment across policy updates. TIGPO maintains a persistent transition graph for each task, allowing valid transitions discovered by different policy versions to jointly determine credit for current rollouts. To actively reconnect current exploration with historical experience, TIGPO allocates a fixed rollout budget between Exploration slots for ordinary task sampling and Revisit slots for delayed reattempts of previously explored tasks. For each revisit, TIGPO pairs the current rollout group with its corresponding earlier Exploration group to construct a cross-temporal reference. The enlarged reference is designed to stabilize relative advantage estimation under small rollout groups, while comparison on the same task directly captures policy improvement across training stages. Historical transitions and scores serve only as structural and detached statistical references and are never replayed in the policy loss. Experiments on ALFWorld and WebShop demonstrate that TIGPO consistently outperforms prior group-based and graph-based policy optimization methods.

---


### 63. [Chiaroscuro for Emotions: A Contrastive Emotion Benchmark Grounded in Appraisal Theory](https://arxiv.org/abs/2609.03394)

**<font color=#1a73e8>作者：</font>** Divyesh Bommana, Mohammad Saim, Tianyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion recognition benchmarks often predict one emotion per text, missing many real-world scenarios where two people arrive at opposing emotions from a single shared event. For example, a child kicks the seat in front of her in excitement while the passenger ahead grows angry. We introduce CHIARO, a 1,000 human-annotated sentence benchmark for contrastive emotion inference grounded in appraisal theory. Each scene describes one causal trigger eliciting a positive emotion in one person and a negative emotion in the other, drawn from a ten-class taxonomy. We benchmark seven frontier LLMs and four off-the-shelf emotion classifiers. The strongest LLM reaches 67.3 macro-F1, well below human agreement, while existing emotion classifiers score near chance. Beyond evaluation, CHIARO also serves as a training signal. When combined with an existing emotion corpus, the resulting downstream classifier improves on CHIARO itself and on six of ten external emotion benchmarks, which positions our dataset as a complementary signal for emotion recognition.

---


### 64. [TabScope: Question-Adaptive Scope Selection for Table Question Answering](https://arxiv.org/abs/2609.03395)

**<font color=#1a73e8>作者：</font>** Yuxiang Wang, Junhao Gan, Jianzhong Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong performance on table question answering, yet their accuracy often degrades as table size increases. We find that this degradation is not uniform across question types. Localization-sensitive questions are particularly affected by irrelevant table content, while questions requiring broader evidence may still benefit from full-table reasoning. Based on this observation, we propose a question-adaptive framework that dynamically selects between localized and full-table reasoning. The framework constructs question-specific sub-tables through operation-aware table decomposition and uses the predicted question type to determine the appropriate reasoning mode. We further introduce silver reference sub-tables for evaluating evidence selection and construct SLQA, a benchmark based on real-world long tables. Experiments on WikiTQ and SLQA show that localization is particularly effective for lookup and local reasoning questions, while adaptive selection between localized and full-table reasoning achieves the best overall performance. These results highlight that long-table QA requires deciding not only how to localize, but also when to localize. Our code and datasets will be made available upon publication of the paper.

---


### 65. [A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant](https://arxiv.org/abs/2609.03402)

**<font color=#1a73e8>作者：</font>** Saptarshi Basu, Sandeep Kakar, Ashok Goel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) teaching assistants powered by large language models (LLMs) offer scalable educational support but often provide limited personalization. This study presents a prompt-engineering-based framework for personalizing general-purpose LLM/RAG-based AI teaching assistants such as Jill Watson across academic disciplines and courses. The framework adapts responses using six learner-specific dimensions: self-assessment, abstraction preference, verbosity preference, perceptual orientation, information processing style, and level of understanding, yielding 96 distinct learner profiles. Student queries are additionally analyzed using Bloom's Taxonomy to estimate cognitive complexity at the interaction level. Learner attributes and cognitive assessments are encoded in structured prompts that condition the LLM without requiring model retraining. The framework is evaluated through experiments using NLP metrics and a human study with five participants. Results show perceived differences in response style and structure across personalization conditions, with statistical analyses identifying learner attributes associated with measurable response changes. These findings provide preliminary evidence that prompt-based personalization can support adaptive behavior in LLM-powered educational agents.

---


### 66. [Caught in the Story: Narrative Captivity in Multi-turn LLMs Conversation](https://arxiv.org/abs/2609.03407)

**<font color=#1a73e8>作者：</font>** Yuhe Wu, Guangyu Wang, Yujie Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People increasingly turn to large language models (LLMs) for everyday advice, making ethically charged interpersonal problems a practical moral-advisory context. Most prior work has studied this context through single-turn judgments or pressure-laden rebuttals, assumptions that poorly match how guidance is sought in real-world contexts. These assumptions leave unclear whether narration alone, without an explicit opposing position, can shift model judgments during multi-turn moral consultation. Yet real-world moral-conflict conversation often elicits one party's self-justifying account, which can unfold over multiple turns and create information asymmetry. We introduce \textbf{narrative captivity}, a failure mode in which a model treats an unopposed one-sided account as complete and aligns with the narrator's interpretation without seeking missing perspectives. To measure this phenomenon, we build a benchmark of $5{,}078$ interpersonal-conflict scenarios spanning six moral dimensions. Across 17 LLMs, narrative captivity is widespread: end-state judgments under multi-turn narration shift by 25 percentage points on average beyond the matched single-turn baseline. Stage-level analysis identifies preference optimization as a major contributor, while four inference-time strategies provide only partial mitigation. We hope our project fosters LLM advisors that preserve independent judgment in real-world consultation.

---


### 67. [To What Extent Do Large Language Models Understand Bangla Idioms?](https://arxiv.org/abs/2609.03410)

**<font color=#1a73e8>作者：</font>** Mousumi Akter, Md. Faiyaz Abdullah Sayeedi, Nurul Labib Sayeedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idiomatic expressions are an integral part of natural language, reflecting cultural nuances and posing unique challenges for computational models, particularly in low-resource languages. In this paper, we present the first large-scale benchmark dataset of Bangla idioms, complemented by a synthetic multiple-choice question (MCQ) dataset for idiom meaning identification. We conduct a comprehensive evaluation of recent large language models (LLMs) across three idiom-related tasks: paraphrasing, idiom span detection, and meaning identification, leveraging zero-shot and few-shot prompting strategies. Our results reveal substantial variability in model performance, with no single LLM consistently outperforming others across all tasks. Notably, Phi-4-mini-instruct excels in paraphrasing, Kimi-K2-32b-instruct in span detection, and Gemini-2.5-flash in meaning identification. We believe that our datasets and analyses will provide valuable resources to guide future research in improving LLM comprehension of idiomatic expressions, particularly in Bangla and other low-resource languages.

---


### 68. [Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection](https://arxiv.org/abs/2609.03416)

**<font color=#1a73e8>作者：</font>** Weijie Liu, Running Zhao, Wenhao Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-empowered paper-code discrepancy detection has received growing concern since the scaling of research submissions exceeds the manual review capability. However, the limited context capacity and one-sided discrepancy detection of existing single-agent LLM paradigms lead to an inferior recall performance in detecting discrepancies. In this paper, we propose Dude, the first Dual-Detection Multi-Agent System for paper-code discrepancy detection. We discover that the granularity asymmetry of the paper-language and code-language introduces over-interpretation and over-reporting challenges in a multi-agent system design for discrepancy detection, resulting in increasing false positives. To address this, we propose a granularity-aligned negotiation and a two-stage salience-filtering mechanism in Dude, which effectively prevents agents from falsely reporting discrepancies. Experimental results in real-world paper-code discrepancy datasets showcase Dude's significant recall and precision improvement by up to 22.8%, increasing F1 score by up to 18.7% compared to baseline methods.

---


### 69. [Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models](https://arxiv.org/abs/2609.03422)

**<font color=#1a73e8>作者：</font>** Ross Tieman, Evan Markou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diversity is a widely observed factor in the resilient function of collective systems, yet the type of diversity that matters depends on the properties and failure modes of the system. This distinction is important for systems composed of multiple language models. Different models may be treated as independent components even when their behaviour and failures remain strongly correlated. Assessments of language-model populations using semantic similarity demonstrate limited semantic diversity, but this captures only differences in the meaning of observed outputs. We argue that a more fundamental notion of model diversity is generative-process diversity, the differences between processes capable of generating the observed outputs. Drawing from Algorithmic Information Theory, we use Normalised Compression Distance between raw model outputs, residualised against a permutation control, as a measure of inferred generative-process diversity. Across 38 language models, this measure identifies population structure missed by semantic similarity and predicts cross-task variation in chance-corrected correlated failure among model pairs across ten disjoint benchmark families, beyond semantic similarity and model-pair capability. The cross-benchmark partial rank association is $-0.216$ with a 95% interval of $[-0.309,-0.122]$, and the estimate is negative on all ten benchmarks. These results indicate that increased generative-process diversity is associated with reduced correlated failure in model pairs that is not attributable to semantic similarity or capability. Inferred generative-process diversity offers a novel and practical approach for investigating diversity of multi-model systems in safety-relevant contexts.

---


### 70. [DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents](https://arxiv.org/abs/2609.03423)

**<font color=#1a73e8>作者：</font>** Puneet Mathur, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents must continuously decide when to listen, backchannel, interrupt, handle speech overlaps, take the floor, and yield. Existing benchmarks largely test these behaviors through explicit turn-management instructions, while deployed agents are often configured through roles or personas from which the appropriate conversational behavior must be inferred. We introduce DuplexSpeechBench-IFEval (DSB-IFEval) for evaluating implicit instruction-following in real-time spoken interaction. (DSB-IFEval) comprises 1,038 test cases spanning eight diverse assistant roles and evaluates five conditioning protocols for instruction-following: default behavior, explicit behavioral instructions, persona-implied behavior, combined persona--rule conditioning, and instruction conflict. We measure real-time floor management using a deterministic Instruction Adherence Score (IAS) and persona-consistent content using LLM-judged Persona Adherence Score (PAS). Across six real-time speech systems, we find architecture-dependent trade-offs. Full duplex models like F-Actor and PersonaPlex are more sensitive to whether conversational behavior is stated explicitly or must be inferred from a persona, with adherence dropping by 9.7% and 4.5%, respectively, under persona-only conditioning. In contrast, GPT-Realtime, MiniCPM-o, and Fun-Audio-Chat strongly adhere to persona-consistent content, but their floor behavior does not adapt across explicit and persona-only instructions and remains constrained on several proactive actions. We further find that even if systems reliably follow conflicting directives to their prescribed persona, they still struggle to override them under safety conflict. These results show that inferring the behavior implied by a role, executing it at the appropriate conversational moment, and resolving competing instructions remain distinct challenges for full-duplex voice agents.

---


### 71. [Lngram v2: Latent N-Gram Memory with Interpretable Discrete Representations](https://arxiv.org/abs/2609.03426)

**<font color=#1a73e8>作者：</font>** Yunao Zheng, Bin Wen, Xiaojie Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers lack a native lookup mechanism, requiring repeated dense computation to recognize and reuse local static patterns. Lngram v1 introduces tokenizer-independent conditional memory through discrete latent n-gram addressing, but its memory capacity is coupled with the backbone width, limiting scalability due to high parameter and activation costs. We propose Lngram v2, which decouples the number of routes, memory dimension, and backbone width, and introduces a context-aware grouped-query attention readout to scale memory capacity independently. A zero-value Sink and counterfactual surrogate gradients further improve readout selectivity and routing trainability while preserving hard discrete addressing. Experiments across vision--language models (VLMs) of different scales show consistent improvements, including successful scaling to a 30B-parameter model. Compared with Lngram v1, Lngram v2 substantially reduces both total and activated memory parameters while maintaining or improving language modeling performance. Further analysis shows that its discrete IDs preserve substantial semantic structure of continuous hidden states, enabling semantic recovery from IDs alone and stable ID--semantic associations across datasets. These results establish Lngram v2 as an efficient and scalable latent conditional memory mechanism whose discrete addresses also provide a structured interface for analyzing internal model representations.

---


### 72. [When Do Frozen VLMs Respond to Image-Free Object-Token Edits? An Answer-Key-Free Protocol and What It Reveals](https://arxiv.org/abs/2609.03429)

**<font color=#1a73e8>作者：</font>** Wonbin Son, Gyumun Choi, Junil Seo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering what-if queries about a scene with a VLM usually means injecting the assumption as text or repainting the scene with a generative model. We instead move the edit to the representation level, before the model input. The image is abstracted into a set of object-level tokens, and the original image never enters the VLM. This design rests on an open question: when do frozen VLMs actually respond to such token edits? We introduce an answer-key-free protocol: no post-edit answer is annotated. It scores edits whose answers are logically determined, and audits itself by reversing each scoreable choice. The protocol reveals three structures. The response is not free: explicit edit teaching, not ordinary VQA training, produces it in dense scenes and multiplies it in sparse ones, on all three operations. Once on, it is governed by token cleanliness and density, with deployable detector+segmenter tokens competitive with the oracle and outperforming it on VRSBench. And reading is a separable axis: the image-free token route preserves 92-96% of a matched patch-token baseline's free-text VQA, and the answers measurably depend on the tokens. The response, cleanliness, and reading structures are sign-preserved across two remote-sensing datasets (iSAID, VRSBench) and three frozen LM backbones. We release the probe generator, records, judge logs, and code.

---


### 73. [Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning](https://arxiv.org/abs/2609.03430)

**<font color=#1a73e8>作者：</font>** Heng Wang, Jielin Qiu, Wenting Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models achieve superior performance on tasks that require extended reasoning, but long chains of thought make the KV cache a severe memory bottleneck. Existing KV cache compression methods share one paradigm: score each cached token by some estimate of how much it will matter later, and keep the top-scoring ones. We show that the selection signal contributes almost nothing. Random Attention keeps the prompt and evicts uniformly at random within each attention head, computing no score at all; across four models and six reasoning tasks it matches the strongest prior evictor while serving 32-43% higher throughput than it in vLLM deployment. Controlled experiments explain this by showing that 1) the prompt is the fragile part of the cache, and most of the gap between selectors is just whether their selection signal happened to keep it; 2) the reasoning trace protects itself against eviction with redundancy at two levels, in the text (the model restates what it still needs as it works) and across attention heads (each keeps its own copy of the trace), so once the prompt is safe, a random draw retains enough copies of what the model still needs, and no score is required to pick them. Our code is publicly available at this https URL.

---


### 74. [Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks](https://arxiv.org/abs/2609.03432)

**<font color=#1a73e8>作者：</font>** Xiangyu Wang, Jin Wu, Xiaoyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated evaluation of creativity tasks remains challenging for LLM-as-a-Judge, as LLM is susceptible to biases such as verbosity bias and leniency bias. Such limitations are particularly evident in Contextually-Grounded and Procedurally-Structured Tasks (CGPST), a complex multi-step creativity task where inter-step dependencies, highly subjectivity, and wide scoring ranges lead to more unstable and biased judgments. Existing approaches either rely on task-specific training or directly apply LLM-as-a-Judge, both of which struggle to ensure reliable evaluation under such complexity. To bridge these gaps, we propose CreaEval, an automated creativity evaluator for CGPST that decouples typical LLM-as-a-Judge into analysis and judging. Correspondingly, CreaEval involves two critical phases: Memory-augmented Analysis, a SoT-LLM converts multi-step responses into structured evaluation evidence, incorporating cross-step memory; and Evidence-based Judging, a Judge-LLM uses the extracted evidence for judging without accessing raw responses. Comprehensive experiments show that CreaEval achieves an average performance improvement of 22.74% over the second-best baselines across CGPST and two classic simple creativity tasks, demonstrating its generalizability. The code is available at this https URL.

---


### 75. [It's the Problem, Not the Path: Budget and Difficulty Confounds in LLM Reasoning Trajectories](https://arxiv.org/abs/2609.03436)

**<font color=#1a73e8>作者：</font>** Yigit Utku Bulut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning traces of large language models are widely read as containing "breakthrough" moments and early-legible fates. Both readings rest on measurements missing a counterfactual control at the level of the claim; we supply both controls. First, a restart-controlled truncation probe separates when a solution fits the continuation budget from when a prefix carries value that fresh computation cannot buy, comparing per-anchor continuation solve rates against from-scratch restart curves at matched total generated-token budget. Applied to 178 problem-model cells (89 MATH problems x two small open models, an outcome-blind but difficulty-targeted cohort), exactly 1 of 178 cells survives as prefix-limited; restart dose-response separates a compute-starved model from a capability-limited one; and wherever the matched budget lies inside the restart grid, continuing the model's own prefix beats restarting (9 of 9) -- predominantly compute compression rather than expanded reachability. Second, a pre-registered, difficulty-controlled test finds no detectable outcome information in early-window internal signals beyond a problem-difficulty baseline, and two generation-free analyses of public corpora show why this control is needed: a trace-blind difficulty proxy reaches AUROC 0.873 on 192K DeepSeek-R1 generations -- inside the published probe range -- and a closely matched reconstruction of the closest published early-window positive recovers a comparable pooled result (0.849) while within problem it is statistically indistinguishable from chance at all ten anchors (0.496 at t=4); a post-hoc within-targeted probe finds only a small average residual, concentrated in three low-failure problems. High pooled probe AUROCs cannot by themselves establish within-attempt information; a question-only baseline or within-problem evaluation is required.

---


### 76. [When Retrieval Helps: Selective Retrieval for Single-Turn Mental-Health QA](https://arxiv.org/abs/2609.03454)

**<font color=#1a73e8>作者：</font>** Hyunseo Oh, Chong-Kwon Kim, Yoonhyuk Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can improve the specificity and grounding of large language model responses, but its effect is not uniformly beneficial in single-turn mental-health question answering, where user queries often combine emotional distress, treatment concerns, and safety-sensitive needs. We study when retrieval helps or hurts mental-health QA, and whether a lightweight selective retrieval policy can better control this trade-off. We operationalize retrieval need using three draft-conditioned utility dimensions: psychoeducational need, coping need, and response specificity, together with a rule-based safety trigger. Following psychotherapy-grounded RAG systems such as coTherapist, we construct a compact and controllable guideline corpus comprising coping-strategy, psychoeducational, and safety resources. We fine-tune an instruction-tuned generator on MentalChat16K using QLoRA and compare Closed-book, Always Retrieval, and Selective Retrieval settings on CounselBench-Eval and CounselBench-Adv. Experiments show that retrieval is not uniformly beneficial in this domain. Always Retrieval improves specificity but lowers overall quality and introduces additional safety-sensitive failures. Selective Retrieval preserves closed-book behavior for low-need cases while avoiding the additional degradation caused by unconditional retrieval, supporting the view that retrieval activation is a safety-sensitive control decision.

---


### 77. [Beyond "Made with AI": Visualizing Provenance Density to Mitigate the Transparency Penalty](https://arxiv.org/abs/2609.03460)

**<font color=#1a73e8>作者：</font>** Qing Zhang, Yifei Huang, Juyoung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative AI makes polished prose cheap to produce, users can no longer rely on fluency as a proxy for truth. We call this failure mode the Fluency Trap: users trust fluent hallucinations while also discounting accurate content once it is disclosed as AI-generated. Binary ``Made with AI'' labels respond with authorship disclosure, but they do not show what supports a claim. We propose Provenance Density, an evidence-visualization interface that shows the density of verified claims in a text. In a user study with 81 participants, an idealized Provenance Density interface produced a large discernment gap between truth and fabrication ($+4.15$ points, $d=1.82$), whereas participants given no signal showed no detectable discrimination. A technical audit with 200 samples shows that retrieval density alone is insufficient; unexpectedly, the Consistency Veto carries most of the discriminative signal on dynamic queries. As AI-generated content becomes indistinguishable from human writing, effective transparency must move from authorship disclosure toward evidence visualization.

---


### 78. [Mind the Gap: Robustness Risks in PII Detection Systems](https://arxiv.org/abs/2609.03464)

**<font color=#1a73e8>作者：</font>** Adeel Zafar, Slawomir Nowaczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personally Identifiable Information (PII) detection is a foundational component of data protection infrastructure where missed entities constitute direct privacy and security risks. Although modern PII systems report strong performance on standard benchmarks, we show that these evaluations mask substantial robustness failures under realistic distribution shifts encountered in deployment. Rather than comparing state-of-the-art accuracy, we study how different PII detection paradigms fail under noisy, unstructured, and informal inputs. We construct a stress test benchmark spanning seven categories of natural distribution shift and evaluate representative systems from three widely deployed architectural families: encoder-based NER (SpaCy), rule-based hybrid detection (Presidio), and generative LLM extraction (Qwen2.5-3B).
All three exhibit significant degradation on out-of-distribution inputs, but with distinct and complementary failure modes. Encoder models primarily fail on unseen surface forms and boundary detection, rule-based systems fail on non-standard formats, and LLMs exhibit entity-type confusion and generation instability. These results show that aggregate benchmark scores obscure deployment-critical weaknesses and that no single architecture is uniformly reliable across PII categories. Motivated by these findings, we propose a hybrid detection pipeline with a QA-driven feedback loop for iterative risk mitigation, and release our benchmark to support OOD-aware evaluation of PII systems.

---


### 79. [When Users Don't Ask: Benchmarking Context-Driven Memory Retrieval in Conversational Agents](https://arxiv.org/abs/2609.03467)

**<font color=#1a73e8>作者：</font>** Wen-Yu Chang, Yun-Nung Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increas- ingly deployed as long-horizon conversational agents, motivating growing interest in mem- ory systems. However, existing benchmarks primarily evaluate memory through QA-style probing rather than in-situ conversational usage. We introduce LOCOMO-CONV, a conversa- tional memory benchmark derived from Lo- CoMo with four query styles: dialog, implicit, counterfactual, and composed. Across five rep- resentative memory systems, we evaluate both retrieval recall and end-to-end response qual- ity. Our experiments show that conversational framing exposes substantial retrieval gaps over- looked by QA benchmarks, especially on im- plicit and composed queries, which multi-facet query rewriting narrows for raw-turn mem- ory but not abstractive memory. We further find that strong retrieval does not fully trans- late into response quality, and that implicit queries exhibit silent grounding, where mem- ory improves contextual grounding without ex- plicitly surfacing the gold fact. These results point to reasoning-based memory elaboration as a promising direction, and we release aux- iliary supportive_memory annotations captur- ing conversationally useful context beyond the original gold evidence.

---


### 80. [AutoGraphForge: Towards Automated Graph Theory Discovery](https://arxiv.org/abs/2609.03478)

**<font color=#1a73e8>作者：</font>** Ján Pastorek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We report on our ongoing project to develop a computational pipeline, AutoGraphForge, for an automated graph-theoretic conjecturing-refuting-formalizing-proving system. Conjecture generation is counterexample-guided and runs in rounds: a Graffiti3 generator proposes conjectures over a small, evolving snapshot table $T$ (initially a few hundred graphs with their computed invariants) that grows only by counterexamples to its own conjectures. A novelty filter of $559$ classical and folklore relations, closed under transitive composition and linear identity substitution, decides via a linear program whether a candidate is already implied by known results. Surviving candidates are tested against a dataset of about $348,000$ graphs, unioning the complete House of Graphs invariant export, the exhaustive census of all connected graphs on at most nine vertices, several extremal families (strongly regular, minimal Ramsey, Cayley, cages, barbells, lollipops, spiders), and random models. Counterexample-search algorithms then attack the remainder. Run for several rounds on an HPC cluster, the loop yields $6,522$ conjectures that survived the refutation dataset, the novelty filter and every active-search run -- among them nontrivial relations between the annihilation number and the edge-cover number for bipartite and regular graphs, which we prove by hand. A subsequent formalization and proving stage deterministically translates each surviving conjecture into a Lean 4 statement skeleton; every candidate proof is kernel-verified against a pinned mathlib4 and our custom invariant preamble. This stage integrates two neural provers -- DeepSeek-Prover-V2-671B (served with vLLM) and the Lean-specialised OProver-32B -- behind the independent kernel check. It is implemented end-to-end and passes initial sanity checks, with the full pipeline currently running on the cluster.

---


### 81. [Making Every Tool Call Count: Necessary Tool-Evidence Path Rewards for Agentic Vision-Language Models](https://arxiv.org/abs/2609.03493)

**<font color=#1a73e8>作者：</font>** Xingming Long, Yu Liu, Zhiwei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models (VLMs) can directly answer many image-grounded questions, yet they often struggle with complex queries requiring fine-grained visual details or external knowledge. To acquire this missing evidence, agentic VLMs invoke tools such as image cropping, image search, and text search. However, existing training paradigms primarily evaluate tool-use based on final answer correctness, leaving evidence acquisition and utilization insufficiently supervised. This leads to two critical shortcomings: (i) models frequently issue redundant or off-target tool calls that fail to gather necessary evidence, and (ii) even when appropriate tools are called, models often fail to extract the necessary information from the resulting observations. To address these limitations, we introduce the NTEP (Necessary Tool-Evidence Path), a novel annotation scheme that explicitly specifies the essential external evidence and corresponding tool calls for each query. Building upon this, we propose NTEP-R (NTEP Reward), a supervision mechanism ensuring that each tool invocation strictly advances the reasoning process toward the final solution. Specifically, our approach rewards the agent for aligning its pre-call intent with a necessary evidence-seeking goal, and for ensuring the information summarized from the post-call observation aligns with the necessary evidence. Furthermore, we introduce a non-repeated-goal regularizer to penalize redundant calls that revisit satisfied NTEP goals. Extensive evaluations on seven image-grounded benchmarks demonstrate that our 8B-parameter instantiation, NTEP-8B, significantly improves both search-oriented accuracy and tool-use efficiency within a unified three-tool framework. These results highlight the critical value of fine-grained tool-evidence path supervision for training robust agentic VLMs.

---


### 82. [GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving](https://arxiv.org/abs/2609.03494)

**<font color=#1a73e8>作者：</font>** Qiankun Ma, Yanjiang Zhou, Zinan Xiong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-output reasoning has made the key--value (KV) cache a critical memory bottleneck for efficient LLM serving. Existing KV compression methods usually rely on a predefined per-request budget and adjust only which KV states are retained, leaving the total capacity fixed throughout decoding. However, reasoning workloads exhibit substantial demand variation: different requests require different KV capacities, and the attention demand of an individual request evolves during generation. We introduce \textbf{GrowPage}, an on-demand KV budgeting framework that treats KV capacity as a runtime resource. GrowPage maintains lightweight dual-timescale query summaries to capture recent and long-term attention behaviors, and uses their relative attention working sets to estimate demand evolution. At each capacity boundary, GrowPage either compresses KV states within the current allocation or acquires an additional physical page when broader demand emerges. By integrating with PagedAttention's page-level memory abstraction, GrowPage preserves continuous batching and prefix caching. Experiments on reasoning benchmarks across multiple models show that GrowPage achieves a superior performance--throughput trade-off over existing approaches.

---


### 83. [Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech](https://arxiv.org/abs/2609.03502)

**<font color=#1a73e8>作者：</font>** Kunat Pipatanakul, Potsawee Manakul, Warit Sirichotedumrong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In low-resource settings, deploying TTS typically requires choosing between a large voice-cloning model with costly inference or a compact fixed-voice system that requires a speaker-specific corpus. We study a third route: using a large voice-cloning model as a programmable data source to turn a short voice reference (e.g., 15 seconds) into a compact fixed-voice student trained entirely on synthetic speech. This setting makes pipeline design consequential: teacher errors become training targets, while filtering failed generations can reduce coverage of difficult texts. Thai further introduces challenges from ambiguous word boundaries, lexical tone, names and loanwords, numeric verbalization, and Thai-English code-switching. We study how text preparation, synthetic generation, quality filtering, rejection sampling, and frontend choices affect the resulting student, and where teacher limitations remain. We evaluate CER, Challenge-Set Keyword Accuracy, Prosody Pause Accuracy, speaker similarity, and speaking rate. The resulting 82M-parameter model, Wayu-Paxa-TTS-Edge, enables on-device Thai TTS without reference audio. It achieves 68.2% Challenge-Set Keyword Accuracy (85.5% of Gemini 3.1) and 91.4% pause precision, outperforming its OmniVoice teacher (89.9%) and reaching 94.8% of Gemini 3.1. It also achieves the lowest pause-placement error and intra-word pause rates among the three systems, and 3.7% and 1.1% CER on Thai and English, respectively. We open-source the model and evaluation framework for Thai TTS development.

---


### 84. [Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations](https://arxiv.org/abs/2609.03511)

**<font color=#1a73e8>作者：</font>** Karthika Nhayakkat, Rajat Verma, Maharaj Brahma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate strong multilingual reasoning performance, yet their robustness to semantics-preserving structural variation remains underexplored, particularly for relatively free word-order languages. We investigate the structural sensitivity of multilingual LLMs using two linguistically grounded perturbation settings in Hindi and Malayalam: constrained constituent reordering and active-passive voice transformation. We introduce a benchmark dataset IndicReStruct, with two variants, GSM8K-Reordered and GSM8K-Voice, constructed from GSM8K while preserving semantic meaning. Across six state-of-the-art LLMs and multiple prompting strategies, we observe consistent and significant degradation in mathematical reasoning performance under structurally perturbed inputs. To further understand these failures, we perform qualitative error analysis and mechanistic interpretability experiments using residual-stream activation patching. Our analyses show that reasoning failures frequently arise from disruptions in entity-quantity alignment and that intermediate transformer layers contribute most strongly toward reasoning restoration. Overall, our findings suggest that current multilingual LLMs remain highly sensitive to surface syntactic realization and lack robust compositional invariance under structurally different but semantically equivalent inputs.

---


### 85. [CulturalMenuBench: Probing the Knowledge-Application Gap in Multimodal Culinary Reasoning](https://arxiv.org/abs/2609.03526)

**<font color=#1a73e8>作者：</font>** Bo Zeng, Linfeng Gao, Peiqin Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal language models achieve near-ceiling scores on food recognition benchmarks, yet it remains unclear whether this success reflects genuine cultural understanding or mere visual matching. To probe this distinction, we introduce CulturalMenuBench, a benchmark of 4,870 items in 10 languages across 18 regions; its 10 tasks pair final-dish and step-by-step cooking images with ingredients, procedural text, and regional labels, spanning basic recognition to process-grounded cultural attribution. Evaluating 12 models exposes a substantial knowledge-application gap: models exceeding 94% on standard multiple-choice tasks drop to at most 56% when attributing dishes to Chinese regional cuisines, despite an identical four-way format. Diagnostic analyses explain why: error patterns are consistent with random guessing, accuracy tracks visual distinctiveness rather than cultural structure, and models classify cuisines more accurately from dish names alone than from images (+7-18 points). The knowledge is thus present but cannot be activated through visual input. An ablation confirms these tasks genuinely require procedural evidence: removing sequential cooking images selectively degrades process-grounded tasks while others remain stable. Overall, CulturalMenuBench shows that near-perfect recognition can conceal an inability to apply cultural knowledge, motivating training that explicitly connects perception, procedure, and cultural context. Code and data are publicly available.

---


### 86. [NeoRed: A Knowledge-Logic-Alignment Multimodal Large Language Model for Neonatal Respiratory Disease Diagnosis](https://arxiv.org/abs/2609.03527)

**<font color=#1a73e8>作者：</font>** Yinan Liu, Hongtai Xia, Haoran Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neonatal respiratory diseases are a major cause of neonatal morbidity and mortality, posing substantial challenges in clinical practice. Despite recent advances, existing Multimodal Large Language Models (MLLMs) face two key limitations in neonatal diagnosis: (1) domain gap arising from predominantly adult training data; (2) insufficient integration of multidimensional clinical context for accurate diagnosis. To address these challenges, we collect two real-world clinical datasets (NeoCXR and NeoCXR-EV) and propose NeoRed, to the best of our knowledge, the first MLLM tailored for neonatal respiratory disease, filling the gap in neonatal diagnostic reports generation. To enhance joint diagnosis from heterogeneous clinical context and chest X-rays, we design a novel Knowledge-Logic-Alignment (KLA) framework which constrains model behavior from three perspectives: 1) Knowledge Prior Injection (KPI) incorporates neonatologist-inspired diagnostic priors into multimodal representations, guiding disease-specific attention across modalities; 2) Diagnostic Logic Constraint (DLC) aligns the semantics of generated reports with multimodal diagnostic logic; and 3) Visual Semantic Alignment (VSA) establishes semantic correspondence between visual features and imaging conclusions. Extensive experiments demonstrate that NeoRed enables accurate neonatal diagnostic reports generation, achieving ROUGE-L of 53.29% and Clinical Efficacy F1 score of 65.19% on NeoCXR, outperforming existing MLLMs. NeoRed also preserves competitive report generation performance on adult benchmarks (MIMIC-CXR and IU-Xray). Datasets will be available upon application.

---


### 87. [Feature Reconfiguration With Visual Prior for Medical Lesion Segmentation](https://arxiv.org/abs/2609.03535)

**<font color=#1a73e8>作者：</font>** Yinan Liu, Jiankang Hong, Zhen Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lesion segmentation in medical images plays a critical role in clinical diagnosis and treatment planning. Despite significant advances, lesion segmentation remains challenging due to two major factors: (1) complex background interference; (2) diverse lesion morphology. Existing encoder-decoder based methods mainly focus on enhancing feature extraction or redesigning decoding strategies. However, they lack early prior guidance and feature reconfiguration during the encoding stage, limiting their effectiveness in handling these challenges. To address these limitations, we propose FreNet, a feature reconfiguration framework with visual priors, which performs pixel-level reconfiguration before encoding and feature-level reconfiguration during encoding for precise medical lesion segmentation. To suppress background responses, we propose an Implicit Prior Neural Network (IPNN), which models a continuous spatial field and leverages visual prior from SAM to reconfigure input image before encoding stage. To better handle diverse lesion morphology, we design a Dual-domain Feature Reconfiguration (DFR) module to progressively reconfigure backbone features during encoding stage. Within DFR, the Frequency Decoupling Module (FDM) decouples backbone features in frequency domain to enhance foreground-background discriminability, while the Spatial Localization Module (SLM) spatially relocates and improving spatial stability after frequency decoupling. Extensive experiments on 9 medical image segmentation benchmarks across three imaging modalities demonstrate that FreNet significantly outperforms state-of-the-art (SOTA) methods. On the challenging ETIS dataset, our method achieves Dice improvements of 5.0% over SOTA method and 7.2% over SAM.

---


### 88. [SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models](https://arxiv.org/abs/2609.03544)

**<font color=#1a73e8>作者：</font>** Caoyuan Ma, Tian Gu, Wenpu Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model's original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, we propose a streaming recognition and gated LoRA framework for intrinsic VLM safety. During autoregressive generation, a lightweight recognizer estimates whether the current pre-token generation state is safe or unsafe. Its output updates the LoRA gate for the following decoding step; otherwise, generation follows the frozen-backbone policy. The LoRA module is trained from unsafe prefixes, transition statements, and safe continuations, so that it learns to redirect unsafe generations back to safe responses after activation. Experiments across multiple safety and general-purpose benchmarks demonstrate the effectiveness of our method in post-alignment settings.

---


### 89. [Dalek: A Constructive Agent Machine](https://arxiv.org/abs/2609.03546)

**<font color=#1a73e8>作者：</font>** Wanpeng Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Dalek, a closed machine designed for agents that realizes self-maintenance, self-evolution, self-reproduction, and self-organization on any substrate satisfying a general host contract. The machine is built from three primitives---actors, messages, and channels. Four obligations---a host boundary, a construction language, admissible transitions, and rule heredity---give its boundary, identity, and closure a structural basis.
Von Neumann's 1948 self-reproducing automaton supplies a hereditary constructional core: a self-description together with a constructor, a copier, and a controller. Dalek combines this core with the four obligations and rederives its medium for a text-and-message agent substrate, adding explicit structures for boundary, identity, history, and growth. A large language model and a compiler occupy the payload position and form a general capability producer. New capabilities are authored, compiled, installed into the description, and inherited by descendants. The same path produces the machine's own organs and even its runtime, closing heredity and evolution within the machine.

---


### 90. [GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis](https://arxiv.org/abs/2609.03553)

**<font color=#1a73e8>作者：</font>** Linh Le, Melanie Bui, My Chiffon Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy analysis requires more than predicting whether a proposal will pass: it requires identifying who will be affected, how those actors respond, and what follows. LLM-based policy simulations model these processes at scale, but their validity is hard to establish when plausible behaviour is never compared with observed outcomes. We introduce GPS-Bench, an evidence-grounded benchmark for governance policy simulation that links policies to relevant actors, actor actions and downstream impacts using legislative records, lobbying disclosures, regulatory documents, corporate filings, economic data and other public evidence. Actors are reconstructed from the dated record rather than prompted as archetypes, so a persona is an evidence object with provenance; a human-annotated pool forms the Gold evaluation set, while cases labelled by a separate LLM from retrieved evidence are treated as Silver supervision and never as test labels. Because every inference mode reads the same grounded state and emits the same schema, GPS-Bench turns "does multi-agent simulation help?" into a controlled comparison: we contrast joint reasoning, independent and communicating actor agents, graph-based methods and weight-level fine-tuning over one policy state. Fine-tuning on the grounded record gives the strongest actor-level impact prediction, and decomposition does not beat it; what decomposition adds is mechanism. Agents hold private, non-identical evidence, each seeing its own exposure clause, and address named partners with concrete joint proposals, what they offer, what they need in return, and why acting together beats acting alone, so the coalitions that form can be checked against the commitments the record holds. GPS-Bench therefore gives a common empirical setting for studying when evidence, actor modelling and multi-agent interaction improve the prediction and interpretation of policy outcomes.

---


### 91. [Language, Language Models, and What We're Talking About](https://arxiv.org/abs/2609.03577)

**<font color=#1a73e8>作者：</font>** Malvina Nissim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are commonly discussed as technical artefacts, but they are obviously shaped by the linguistic worlds conveyed by data during their training. Using Italian language models as evidence, I want to bring attention to the nature of the systems which result from training and specialising models on translated and synthetic data, and further curating them, and to the meaning of testing them on equally unnatural data. Are these eventually models of Italian? Are they models of language? Does NLP still care about language? These questions yield another, more concrete question: what language do we actually want language models to produce? I argue that this question cannot be answered if we do not first consider a clearer distinction between language models designed as technical products and language models designed as tools for studying language itself. The answers then might be diverse, the languages we are talking about might be diverse, and the picture might not be as pessimistic as we fear.

---


### 92. [HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews](https://arxiv.org/abs/2609.03580)

**<font color=#1a73e8>作者：</font>** Tzu-Ling Lin, Dong-Ting Yao, Teng-Fang Hsiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but unsupported claims that undermine review reliability. Existing hallucination benchmarks are not designed for peer review, where verification requires grounding claims in long, technical papers. We introduce HalluPeer, a benchmark for detecting hallucinations in scientific peer reviews, providing aligned triples of paper content, human-written reviews, and hallucination-injected reviews, annotated for detection, classification, and localization. Our pipeline induces a peer-review-specific hallucination taxonomy, identifies review contexts, and injects hallucinations with automated filtering. Experiments on 12K papers and 38K reviews show that existing detectors struggle to separate hallucinations from legitimate critique, while evaluation on authentic reviews demonstrates that HalluPeer-defined hallucination patterns occur in real peer reviews, highlighting the critical need for source-aware verification. Our project page can be found in this https URL

---


### 93. [KC-Bench: A Dynamic Interactive Benchmark for Evaluating Knowledge Conflicts in LLM Agents](https://arxiv.org/abs/2609.03588)

**<font color=#1a73e8>作者：</font>** Yaxing Lyu, Shengjie Zhou, Binbin Toh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs increasingly act through tools, they must reconcile user instructions, parametric knowledge, and dynamic environmental observations before taking actions. We introduce KC-Bench, a controlled multi-turn benchmark for measuring this capability across world-knowledge conflicts, input inconsistencies, and multi-source temporal conflicts. Its 238 tasks are manually screened from more than 1,000 generated candidates and combine a user simulator, stateful tools, deterministic environment assertions, an open-source natural-language evaluator, and human trajectory verification. Evaluation of nine models, including DeepSeek-V4-Flash, GLM-5.2, and MiniMax-M3, shows substantial cross-domain variation: no model handles factual correction, identity consistency checking, and temporal conflict resolution reliably across all settings. In the simulated environments, missed conflicts can propagate to tool calls or synthetic protected-data flows. KC-Bench isolates this model-level behavior rather than ranking complete agent frameworks, and provides a reproducible diagnostic for developing conflict-aware reasoning and execution safeguards.

---


### 94. [KhatianDoc: A Human-Verified Benchmark Diagnosing Multimodal LLM Failure on Bengali Legal Land Records](https://arxiv.org/abs/2609.03597)

**<font color=#1a73e8>作者：</font>** Tasmiad Hasan, Arafat Zaman Ratul, Sarker Sadman Saalim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Land ownership in Bangladesh is recorded in Ana-Ganda-Kora-Kranti-Til, a base-16 positional fraction system with dedicated Unicode glyphs, no mainstream font, and no coverage in any OCR pipeline or tokenizer. The handwritten records that carry these fractions, RS Khatians, are the authoritative title record for millions of parcels and a frequent subject of civil litigation, yet no benchmark has asked whether a machine can read one. We introduce KhatianDoc, a four-task benchmark built from 107 real RS Khatian records from the Vumi (land) Office of Munshiganj, Bangladesh: symbol recognition, base-16-to-decimal conversion, structured field extraction, and legal document question answering over 1,634 QA pairs. Ground truth was transcribed by hand, verified by a land-law practitioner to full agreement, and anonymized through positional tokens that keep the referential distinctions multi-hop questions depend on. We evaluate six multimodal LLMs (8B to 72B+, open and closed) under a fixed zero-shot protocol. Five QA categories, 39.3% of our stratified set, return zero correct answers from every model; on the arithmetic task, every model that emits a number does worse than a constant-mean baseline, with exact- and near-match scores coinciding: decorrelation, not approximation. Auditing our own metrics surfaced two artifacts in opposite directions: we correct a refusal-scoring bug and report the fixed scores beside the originals, and flag an inflated metadata metric as an upper bound. KhatianDoc documents not a performance gap but the absence of a capability, with verified ground truth for future systems. Code and data, with a redacted image release, are publicly available.

---


### 95. [Auditing Patient Privacy in Medical Generative Models: Scalable Memorization Detection with DeepSSIM++](https://arxiv.org/abs/2609.03615)

**<font color=#1a73e8>作者：</font>** Antonio Scardace, Francesco Guarnera, Sebastiano Battiato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While deep generative models offer new opportunities for medical image synthesis and data sharing, their ability to memorize and reproduce training samples raises serious concerns about patient confidentiality. Detecting such memorization at scale remains challenging: traditional pixel-based metrics are sensitive to generation artifacts, whereas generic embedding-based metrics often lack the anatomical sensitivity required for medical data. To address this challenge, we introduce DeepSSIM++, a self-supervised similarity metric for scalable memorization auditing in medical generative models. By leveraging multi-scale feature aggregation and anatomy-preserving augmentations, DeepSSIM++ learns an embedding space where cosine similarity approximates the Structural Similarity Index (SSIM), eliminating the need for exact pixel-level registration. Compared with state-of-the-art baselines, DeepSSIM++ achieves an average Macro F1 improvement of 33 percentage points under ideal alignment and 46 percentage points under realistic spatial and intensity perturbations. Furthermore, it accelerates large-scale similarity computation by several orders of magnitude compared with analytical SSIM. By combining anatomical sensitivity and computational efficiency, DeepSSIM++ provides an open-source tool for scalable memorization auditing in medical generative AI. Code and data are publicly available at: this https URL.

---


### 96. [Remember and Reweight: Enhancing Multi-Agent Debate with Experience Memory and Confidence Estimation](https://arxiv.org/abs/2609.03619)

**<font color=#1a73e8>作者：</font>** Xuanfa Jin, Zhijian Ma, Yongcheng Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) improves the reasoning capabilities of large language models by having multiple agents iteratively refine their responses through discussion. However, MAD suffers from a critical vulnerability known as shared misconception: when a majority of agents initially converge on an incorrect answer, the debate process tends to amplify rather than correct the error. Existing methods primarily address peer skew but leave the agents' inherently biased concept priors unaddressed. To mitigate this systematic weakness, we propose R$^2$-MAD (Remember and Reweight for Multi-Agent Debate), a framework that equips agents with an experience memory accumulated from past debates. R$^2$-MAD intervenes on both failure modes through two complementary mechanisms: A debate-state-aware retrieval policy dynamically calibrates the concept prior by retrieving relevant historical evidence based on the current consensus level. Then these retrieved experiences provide a basis for estimating per-agent reliability, yielding confidence weights to modulate peer influence. Experiments on various benchmarks show that R$^2$-MAD achieves consistent improvements over existing single-agent and MAD baselines.

---


### 97. [The Impact of Synthetic Data Augmentation on Discourse-Pragmatic Function Classification](https://arxiv.org/abs/2609.03652)

**<font color=#1a73e8>作者：</font>** Sara Sorahi, Kevin Tang, Reza Kazemian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data augmentation has become a common strategy for addressing class imbalance in NLP, but most approaches focus on the quantity and diversity of generated examples rather than their geometric relationship to real training data. We investigate this question in the context of discourse pragmatic function classification, a task where data sparsity is a structural feature rather than a collection artefact. Using 410 manually annotated instances of the English word look drawn from the British National Corpus, spanning four functions: Attention Signal, Directive, Discourse Marker, and Interjection. We generate synthetic training examples with Llama 3.1 and partition them by their cosine distance from real training data in RoBERTa embedding space. We compare six training conditions that differ in the placement of synthetic examples relative to the empirical decision boundary, while holding augmentation quantity constant across conditions. All augmented conditions improve macro F and accuracy over the real only baseline, but core proximal examples (NEAR) yield the largest gains in macro F (0.113), while a distance balanced mix achieves the highest accuracy (0.748). No condition improves AUC, indicating that augmentation shifts the decision boundary rather than improving the model's underlying probability estimates. These findings suggest that where synthetic examples land in representation space matters as much as how many are generated, with implications for low resource pragmatic classification more broadly.

---


### 98. [Extracting Forgotten Prompts from Targeted Unlearned Models](https://arxiv.org/abs/2609.03662)

**<font color=#1a73e8>作者：</font>** Au Ashley Hoi-Ting, Meghdad Kurmanji, William F. Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent unlearning methods (e.g. NPO, DPO, LUNAR) make use of refusal alignment to suppress forgotten data. However, it has been shown that refusal responses might leave traces of unlearning, and recent attacks have been able to successfully recover some of the unlearned knowledge. In this paper, we uncover a new vulnerability. Existing attacks typically assume that the forgotten prompts are already known to the adversary and focus on recovering their answers. However, we show that the forgotten prompts themselves can be extracted by using the retained data and black-box access to the model. Our attack, Targeted Active Search (TAS), first identifies the forgotten entities by constructing canonical templates and entity pool, and selectively querying the model using the most informative template-entity pair under a limited query budget. Once the entities are identified, TAS instantiates prompt templates with those entities to probe the unlearned model and reconstruct the forgotten prompts. Experiments across three unlearning methods with three datasets and three LLMs shows that TAS recovers the forgotten entity with $100\%$ accuracy and reconstructs up to $95\%$ of forgotten prompts, all while using up to $99.7\%$ fewer queries than naive probing.

---


### 99. [CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding](https://arxiv.org/abs/2609.03675)

**<font color=#1a73e8>作者：</font>** Jing Jiang, Yiran Ling, Ruonan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires Vision Language Models (VLLMs) to process growing video streams and answer user questions under tight latency constraints. Existing methods improve efficiency through token pruning and memory-bank schemes, but mainly reduce visual tokens after visual encoding. Consequently, downstream token pruning alone cannot substantially reduce end-to-end latency because the expensive frame encoding cost has already been incurred. We propose CoFiE, a Coarse-to-Fine Evidence Selection framework that decouples evidence selection into a coarse, query-agnostic filtering stage before the vision encoder and a fine, query-specific refinement stage during LLM prefill. CoFiE introduces Novelty-Guided Frame Filtering to retain visually distinctive candidate frames and Query-Specific Evidence Refinement to select the frames most relevant to the user query. This design removes substantial redundancy before frame encoding while preserving query-specific refinement once semantic information becomes available. Experiments show that CoFiE establishes a new state-of-the-art accuracy-efficiency trade-off across multiple video understanding benchmarks, reaching 78.86% accuracy on StreamingBench and 68.72% on OvO-Bench, with improvements of up to 3.15% over prior methods. Even with up to 80% evidence-frame filtering, CoFiE outperforms strong open-source multimodal models while improving end-to-end inference latency by up to 2.54 times.

---


### 100. [A Circuit for Plural Reference: How LLMs Represent and Retrieve Singular and Plural Entities](https://arxiv.org/abs/2609.03687)

**<font color=#1a73e8>作者：</font>** Anh Danh, Rick Nouwen, Massimo Poesio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coreference resolution is an important task in contextual reasoning. In this paper, we investigate the mechanism for representing and retrieving singular and plural entities for plural reference. We use a combination of mechanistic interpretability and attention pattern analysis to study the process in which LLMs predict a pronoun to refer back to previously mentioned entities. Using a range of causal intervention techniques, we find a set of attention heads that are responsible for (1) representing coreference information in the input, (2) identifying entities that form a plural reference, (3) transferring the information to the component that is responsible for selecting the antecedents and predicting the pronoun. We also find that LLMs align with humans in preference for plural pronoun. Specifically, entities in a plural construction are more likely to be referred to as a plural entity if they are ontologically similar and are linked by the conjunction "and".

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-180](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
