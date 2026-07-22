# 🧠 大模型相关研究 | 2026年07月23日

> 本类共 **104** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-104](./part-03.md)

---

### 51. [Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development](https://arxiv.org/abs/2607.18696)

**<font color=#1a73e8>作者：</font>** Yinan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-native biotechnology companies are often designed by copying human biotech org charts into agent roles. We argue for a different abstraction: a Company World Model, defined as a persistent asset-to-value state representation with transition models, explicit value functions, planning, and updating across scientific, regulatory, BD, commercial, financial, and execution constraints. We introduce a dry-lab benchmark for testing whether AI-agent organizations should mimic departments or operate around such a world model. The benchmark contains 45 retrospective public-information decision cases with strict time cutoffs, hidden outcomes, common schemas, automatic scoring, and blinded pairwise judging. We compare human-org-mimic, stronger human-org-mimic-plus, AI-native asset-centric, and AI-native value-conversion architectures. The value-conversion architecture is a prompt-level approximation of a Company World Model: a Live Asset Value Record updated by Deal, Approval, Revenue, and Investment Arbiter loops. Under a success function defined by external BD, regulatory approval and launch, and revenue discipline, it achieved the highest automatic value-conversion score and was strongly preferred over the original baselines by value-specific blinded judges. Stress tests narrowed the claim: a stronger human baseline remained competitive, and a neutral judge did not show robust value-conversion dominance. Codex-only mechanistic ablations suggest that Revenue Room, Deal Room, and Approval Room carry useful work under the target objective. The central finding is objective-sensitive: departments may remain useful governance views, but the core AI-native operating primitive should be a shared, predictive asset-to-value state rather than a static human org chart. The study is dry-lab only and does not establish real-world drug success, clinical benefit, or revenue prediction accuracy.

---


### 52. [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/abs/2607.18715)

**<font color=#1a73e8>作者：</font>** Yi-Ge Zhang, Tianqi Du, Qi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise
the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every
source of state change. In real world, however, transitions arise from two heterogeneous sources: an action-driven
component induced by the agent, and an action-invariant world effect -- the change that would still occur under a null
action, dictated by the environment's intrinsic dynamics (e.g., gravity-driven sliding, inertia, contact rebound, and
persistent drift). Fusing them into a single target entangles the two inside the latent transition, prevents the model
from attributing observed changes to their underlying causes, and undermines the transferability of the learned
dynamics. We introduce DWM (Decomposed World Model), a supervision-level framework that operationalizes this
decomposition. DWM augments the predictor of a latent world model with an auxiliary world head, regularized by a
normalized world-contrastive objective to be action-invariant, while the original pred head is coupled to it via an
orthogonality constraint; together, the two signals induce an explicit additive decomposition of the predicted
transition into an action-invariant and a complementary action-driven component, without altering the underlying
architecture or inference pipeline. To evaluate DWM under persistent world effects, we construct W-variants of three
standard control benchmarks -- PushT-W, Reacher-W, and TwoRoom-W -- each instantiating a distinct action-invariant
dynamic. DWM matches strong baselines on the flat counterparts and delivers a mean absolute improvement of 13.1% in CEM
planning success across the W-variants.

---


### 53. [Continual Video-MLLM Adaptation over Evolving Domains](https://arxiv.org/abs/2607.18716)

**<font color=#1a73e8>作者：</font>** Rui Cheng, Meixing Shi, Yuxiang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models have shown strong capability in video understanding, yet their adaptation to sequentially evolving domains remains underexplored. In real-world deployments, video data often arrives continuously from heterogeneous domains, requiring the model to acquire new domain-specific knowledge without overwriting previously learned capabilities. Existing continual learning methods typically rely on shared adaptation spaces, which can induce severe cross-domain interference and catastrophic forgetting. We propose Distribution-Aware Expert Routing, a parameter-efficient framework for continual Video-MLLM adaptation over evolving domains. DAER maintains domain-isolated lightweight experts while keeping the pretrained Video-MLLM backbone frozen, thereby decoupling domain-specific adaptation from the general multimodal knowledge of the pretrained model. To enable fine-grained specialization, we introduce an intra-domain distribution-aware routing mechanism that matches each input to expert-level prototype reservoirs using MMD. To address the absence of task identities at inference time, we further propose an inter-domain routing mechanism that performs prototype matching in a discriminative subspace for robust domain identification. In addition, we introduce adaptive domain merging to improve parameter scalability and adopt a two-stage optimization strategy to stabilize expert specialization during continual learning. We evaluate DAER by curating a domain-incremental benchmark built from ten VidQA datasets covering diverse visual environments and reasoning demands. Experiments on two strong Video-MLLM backbones show that DAER consistently outperforms prior methods.

---


### 54. [Find Before You Fine-Tune: A Diagnostic Study of Small LLMs for Cybersecurity QA](https://arxiv.org/abs/2607.18725)

**<font color=#1a73e8>作者：</font>** Shaswata Mitra, Subash Neupane, Trisha Chakraborty 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly fine-tuned for critical-domain Question-Answering (QA), yet choosing which small model to adapt, before paying the cost of adaptation, remains difficult. Fine-tuning can improve domain alignment, but it may also erode prior knowledge, weaken instruction-following, or increase hallucination, especially when labeled data are scarce or rapidly evolving as in cybersecurity. We present FiT (Find before Fine-Tune), a task-oriented diagnostic framework that characterizes small LLMs along three capabilities required for cybersecurity QA: vocabulary recognition, parametric knowledge, and contextualization of retrieved information. Using FiT, we conduct an empirical study of five open-weight 7-billion-parameter models under two fine-tuning regimes. We find that fine-tuning does not uniformly help: it consistently degrades vocabulary and parametric knowledge in small models, and the two regimes trade off differently. Knowledge-focused tuning causes moderate, rank-preserving degradation, whereas instruction-focused tuning collapses measured knowledge through induced abstention, inverting the knowledge ranking while leaving retrieval-grounded contextualization essentially intact. We quantify these regime-specific patterns with rank-correlation analysis and show that pre-fine-tuning FiT scores anticipate the direction of post-tuning change. Our results suggest that task-oriented diagnosis can screen out unsuitable models, avoid unnecessary fine-tuning, and support safer deployment of small LLMs in cybersecurity QA pipelines.

---


### 55. [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/abs/2607.18754)

**<font color=#1a73e8>作者：</font>** Kunlun Zhu, Xuyan Ye, Zhiguang Han 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agent failures are difficult to debug because the step where an error surfaces is often not the one that caused it. Existing observability tools replay execution traces but provide little support for identifying the root cause or translating diagnosis into recovery. We present AgentDebugX, an open-source debugging framework that organizes debugging as a closed loop of Detect, Attribute, Recover, and Rerun. At its core, DeepDebug performs multi-turn root-cause diagnosis through global trajectory understanding, structure-guided investigation, and cross-examination. On the Who and When benchmark, DeepDebug achieves the best strict attribution accuracy among the evaluated methods on both tested open-weight backbones, reaching 28.8 percent exact agent-and-step accuracy on qwen3.5-9b versus 21.7 percent for the strongest single-pass baseline. On GAIA, DeepDebug repairs 13 of 73 failed tasks in a single rerun, compared with 4 to 6 for three decoupled self-correction baselines, improving overall accuracy from 55.8 percent to 63.6 percent. AgentDebugX exposes this workflow through a Python library, CLI, web console, and installable agentic skill, and provides an opt-in Error Hub for sharing scrubbed failure-diagnosis-repair bundles and reusing them as debugging memory.

---


### 56. [Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks](https://arxiv.org/abs/2607.18767)

**<font color=#1a73e8>作者：</font>** Lachlan McGinness  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of Small Language Models (SLMs) in educational settings offers significant advantages in terms of privacy, cost, and scalability. However, SLMs often struggle with complex vision-based tasks, such as grading handwritten student exams, due to the high computational cost of processing large images and the visual distractions present on a full page. In this paper, we investigate whether cropping student responses using bounding boxes can improve the accuracy and computational efficiency of SLMs on a short-answer grading task. Using a dataset of scanned handwritten responses from the 2025 Australian Physics Olympiad, we evaluate the performance of several models ranging from 4B to 72B parameters under varying conditions of Chain of Thought (CoT) prompting and image cropping. Our results demonstrate that using bounding boxes significantly improves grading accuracy and reduces computational cost (FLOPs) across models. We conclude that bounding boxes are a crucial pre-processing step for deploying SLMs in large-scale, vision-based educational assessments.

---


### 57. [RF-Agent: A Practical Framework for Building Language Agents for RFIC Design](https://arxiv.org/abs/2607.18772)

**<font color=#1a73e8>作者：</font>** Yueqi Xing, Houbo He, Jolie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have driven rapid progress in electronic design automation (EDA), yet their application to radio-frequency (RF) circuit design remains limited by the scarcity of domain-specific datasets and standardized benchmarks. We present RF-Agent, which addresses this gap through textbook-driven knowledge distillation. A multi-agent Question-Thinking-Solution-Answer (QTSA) pipeline converts a subsection-level corpus from seven canonical RF textbooks into the first-of-its-kind RF-domain reasoning dataset (over 11,000 samples) with a dedicated multiple-choice benchmark. On this benchmark we study two adaptation strategies: supervised fine-tuning (SFT) and three retrieval-augmented generation (RAG) configurations (semantic, keyword, hybrid). Across multiple LLM families, domain-specific SFT significantly improves RF reasoning, especially for small and medium-sized models; among RAG configurations, semantic retrieval performs best, indicating embedding-based context alignment suits RF reasoning better than naive fusion. The dataset and benchmark provide a reusable foundation for future work on LLM-aided RF circuit design.

---


### 58. [AI Tour Meeting: Group Travel Planning by LLM Agents](https://arxiv.org/abs/2607.18806)

**<font color=#1a73e8>作者：</font>** Daisuke Kikuta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes AI Tour Meeting, a group travel planning framework powered by multiple Large Language Model (LLM)-based agents. The agents are instantiated with distinct personas and collaboratively seek an itinerary that satisfies their constraints and preferences through natural language discussion. The framework enables easy and flexible orchestration of such discussions by providing interfaces for configuring agent personas, discussion workflows, monitoring, and LLM deployment. Its primary use case is a simulation tool for analyzing the behavior of multiple LLM agents during tour planning discussions. This paper demonstrates the utility of the framework by presenting system validation and several analytical results obtained by the framework.

---


### 59. [In-Context Learning for Wound Classification with Small Multimodal Language Models](https://arxiv.org/abs/2607.18819)

**<font color=#1a73e8>作者：</font>** George Martvel, Oskar Gustafsson, John Pavia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wound image classification is often treated as a task-specific supervised learning problem, requiring substantial amounts of manually labelled data and retraining when the label space or deployment setting changes. This study evaluated whether small multimodal language models (SMLMs) can provide a training-free alternative for wound classification through retrieval-based in-context learning (ICL). Experiments used two public wound-image datasets: the Kaggle wound dataset (1469 images, 10 classes) and the Medetec dataset (560 images, 9 classes). Eleven SMLMs from the Qwen 3.5, Ministral 3, and Gemma 4 families were evaluated under zero-shot prompting and few-shot prompting with random support examples, embedding-based k-nearest-neighbour (kNN) retrieval, and kNN retrieval followed by maximal marginal relevance reranking (MMR). Retrieval-only weighted-kNN controls, support-set reduction experiments, and support-context size sweeps were used to assess the effects of retrieval, model scale, and prompt length. Query-conditioned ICL consistently outperformed zero-shot and random few-shot prompting. On the Kaggle dataset, the best result was achieved by Qwen 3.5 27B with kNN+MMR, reaching 0.872 accuracy and 0.871 F1 score. On Medetec, Qwen 3.5 27B with kNN+MMR reached 0.678 accuracy and 0.670 F1. Larger models exceeded matched weighted-kNN controls, indicating use of retrieved examples beyond nearest-neighbour voting. Retrieval-based ICL degraded modestly under support-set reduction, and most gains saturated with 8-10 support images. Retrieval-based ICL allows SMLMs to perform adaptable wound image classification without task-specific retraining. Compact retrieved contexts may support practical and privacy-conscious deployment, although performance remains dependent on model scale, retrieval strategy, and dataset difficulty.

---


### 60. [CASE: Causal Alignment and Structural Enforcement for Improving Chain-of-Thought Faithfulness](https://arxiv.org/abs/2607.18820)

**<font color=#1a73e8>作者：</font>** Ziming Wang, Yinghua Yao, Changwu Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning is widely used to improve both the performance and interpretability of large language models (LLMs), yet the generated reasoning may not faithfully support the final answer. We study this problem from a causal perspective, where a faithful CoT process should follow the chain $Z\rightarrow X\rightarrow Y$, with $Z$, $X$, and $Y$ denoting the instruction, reasoning chain, and final answer, respectively. In this process, the instruction should affect the answer only through the reasoning chain. However, conventional autoregressive LLMs condition answer generation on both the instruction and the CoT, which still allows a direct instruction-to-answer shortcut. To address this issue, we propose CASE, a framework that combines training-time causal alignment and inference-time structural enforcement. During training, CASE builds counterfactual-CoT, biased-instruction, and empty-instruction datasets, and applies selective-loss fine-tuning to strengthen CoT-to-answer dependence while suppressing instruction shortcuts. During inference, CASE masks direct attention from instruction tokens to answer tokens, preventing the model from bypassing the generated CoT. We provide an information-theoretic analysis showing how these components promote faithful chains. Experiments on three models and four benchmarks show that CASE achieves a 37\% average per-setting relative improvement in overall CoT faithfulness over the strongest baselines, exhibits stronger cross-dataset faithfulness transfer, and maintains competitive average accuracy. Code is available at this https URL.

---


### 61. [AILQA: Evaluating AI-Driven Legal Question Answering Systems for the Indian Legal System](https://arxiv.org/abs/2607.18825)

**<font color=#1a73e8>作者：</font>** Shubham Kumar Nigam, Shubham Kumar Mishra, Noel Shallum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This comprehensive study introduces an advanced Artificial Intelligence for Indian Legal Question Answering (AILQA) system tailored to the Indian legal context. AILQA leverages a variety of embedding and generative models, including recent Large Language Models (LLMs), to address the unique challenges posed by the intricate and diverse nature of Indian legal texts and to enhance the accuracy and reliability of responses to legal questions. We conducted rigorous evaluations using both lexical and semantic metrics, enriched by expert legal feedback, to ensure relevance and accuracy. Our findings underscore the effectiveness of the Retrieval-Augmented Generation (RAG) paradigm in improving answer quality, particularly in complex legal domains. Additionally, we assessed performance on standardized tests such as the All India Bar Examination (AIBE), thereby providing a robust benchmark for practical applications. Under the study's evaluation protocol, some AI-generated responses received higher ratings than the available reference answers, particularly when they contained accurate and relevant supporting details. This finding is specific to the evaluated dataset and rating criteria and should not be interpreted as evidence that the models generally outperform qualified legal professionals. We also discuss the challenges encountered, such as the need for precise context and the risks of model hallucination, and propose directions for future research to further refine AI capabilities in the legal field. This study aims to pave the way for enhanced legal decision-support systems, making them more accessible and effective for legal professionals and the public alike.

---


### 62. [Evaluating medical AI under missing information: same-provider judges and human raters change apparent safety](https://arxiv.org/abs/2607.18828)

**<font color=#1a73e8>作者：</font>** Koyar Afrasyab  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Readiness stress-testing of medical AI has focused on closed-ended and multimodal benchmarks. We extend it to open-ended clinical conversation under missing information, where safe behavior means recognizing absent information and qualifying, clarifying, or not over-committing - and where the evaluator becomes part of the measurement. We stress-test four models - three flagships (Claude Opus 4.8, GPT-5.5, Grok 4.3) and one mid-tier model (Gemini 3.5 Flash) - by deleting the latter half of the final user turn in HealthBench conversations, grading responses with a four-provider LLM-judge panel and a blinded clinician-anchored reference. Two evaluator-facing results are robust. First, judge choice materially changes apparent safety: inter-judge agreement is only moderate (Fleiss' kappa = 0.65), and after adjusting for each judge's general leniency (vote-level logistic regression), a positive same-provider association remains (exact permutation p = 0.04; GPT-5.5 ~ +0.10 on the probability scale) - large enough to change which model appears to over-commit least once its own-provider judge is excluded. Second, LLM judges are more permissive than clinicians on a blinded 50-item subsample: all four are significantly more lenient than the stricter independent clinician (crediting appropriate uncertainty on 66-84% of items vs 52%), and three of four than the author-influenced consensus (Grok directional only; judge-vs-consensus kappa = 0.20-0.43). On the author-audited clinical-underdetermined subset the permissiveness gap widened and the point-estimate model ordering held. A closed-ended MedQA anchor confirms accuracy is high and option-order effects are within a +/-5-point equivalence region for three of four models, so the safety gap is about calibration, not knowledge. We release the harness, prompts, per-item outputs, judge panel, perturbation audit, and human-annotation protocol.

---


### 63. [HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks](https://arxiv.org/abs/2607.18867)

**<font color=#1a73e8>作者：</font>** Haozhe Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models leak parametric knowledge of realized outcomes into historical financial decision tasks. Existence is settled; what users lack is a cheap way to audit a given model for it. We present HindsightBench, a black-box behavioral audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). The protocol chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six per-model metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall-accuracy dissociation coefficient -- with explicit gates where identifiability is data-dependent. Applying it to 15 models from seven vendors on a 258-node vintage-correct macro panel yields three headline patterns: (i) the date-trigger reflex tracks training generation, not scale -- absent across the 2024 open-weight generation from 1B to 70B, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -> Qwen3.6) at fixed MoE architecture and 3B active parameters; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebo designs; (iii) audit results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol ships with operational requirements (pin quantization and thinking regime; disclose parser and sampling policy). We release the panel, frozen preregistrations, per-model audit rows with measured dollar costs, transcripts, and one-command regeneration.

---


### 64. [Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM](https://arxiv.org/abs/2607.18915)

**<font color=#1a73e8>作者：</font>** Xiaomeng Hu, Jiaqi Hu, Hao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning. However, as reasoning traces become longer, LLMs may produce a substantial amount of hallucinated content during the reasoning process, which is often difficult to detect. In this work, we conduct a fine-grained analysis of hallucinations arising in LLM reasoning and find that the reasoning traces are particularly prone to Context-Sensitive Factual Hallucinations: cases where the model actually has the relevant knowledge, yet makes factual errors due to contextual interference during reasoning. To address this issue, we propose Step-level Self-Consistency Group Relative Policy Optimization (SSC-GRPO), which assigns step-level rewards to reasoning traces by computing self-consistency scores of individual steps across multiple rollouts. Compared with prior methods, SSC-GRPO achieves state-of-the-art performance on both mathematical reasoning benchmarks and hallucination leaderboards. Our results offer a new perspective for detecting and mitigating hallucinations in the reasoning process of large language models.

---


### 65. [TAP-RAG: Task-Aware Policy Control for Long-Document Multimodal Question Answering](https://arxiv.org/abs/2607.18917)

**<font color=#1a73e8>作者：</font>** Zhong Ji, Keqi Jin, Yan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-document multimodal question answering requires more than retrieving relevant chunks from a large document. Different queries require different evidence behavior. Existing multimodal RAG systems improve evidence access through text chunks, page images, graph links, or heterogeneous document elements, but they often apply a largely query-agnostic evidence-use strategy. We present TAP-RAG, a task-aware policy-controlled RAG framework for long-document multimodal QA. TAP-RAG contains a main controller, the Task-Aware Policy Controller (TAPC), and two policy-guided evidence executors: Task-Aware Query-Guided Flow Diffusion (TA-QFD) and Task-Aware Visual Enhancement (TAVE). For each query, TAPC predicts the task prior, estimates visual/local/global evidence signals, and produces an executable policy. TA-QFD then expands textual and structural evidence over the multimodal document graph, while TAVE selectively inspects page images when visual or layout evidence is needed. A guarded synthesis stage fuses text, visual, and structural evidence and abstains when support is insufficient. On DocBench and MMLongBench-Doc, TAP-RAG achieves the best overall accuracy among the compared systems, improving over a matched multimodal-RAG baseline by +9.1 points (61.1 to 70.2) and +4.5 points (42.2 to 46.7), respectively.

---


### 66. [OntoBook: Ontology-Grounded Synthetic Textbooks for Medical Encoder Pretraining](https://arxiv.org/abs/2607.18927)

**<font color=#1a73e8>作者：</font>** Rian Touchent, Éric de la Clergerie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OntoBook, a method that converts medical ontology structure into pretraining signal for encoder language models. Our approach has three stages: random walks through ontology graphs capture hierarchical and causal relations between medical codes, a large language model reformulates these walks into fluent textbook-style prose, and the resulting text is used to train ModernCamemBERT, a 149M-parameter French encoder, with two objectives on the same data: masked language modeling and relation prediction between code pairs. On three French medical coding benchmarks (FRACCO, Cantemist-FR, Distemist-FR), OntoBook achieves significant improvements over MLM-only pretraining, with +2.5 micro-F1 on FRACCO and +8.0 micro-F1 on Distemist. We find that alignment between objectives is necessary: misaligned training, where each task uses different data, causes a 30-point degradation. We release 1.3 million LLM-reformulated medical textbooks across three French ontologies (CIM-10, CCAM, ATC) and pretrained model checkpoints.

---


### 67. [Dual Adversarial Fine-tuning for Enhancing Robustness of Large Vision Language Model](https://arxiv.org/abs/2607.18958)

**<font color=#1a73e8>作者：</font>** Sibo Wang, Jie Zhang, Shiguang Shan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Large Vision-Language Models (LVLMs), represented by LLaVA and GPT-4V, have demonstrated remarkable capabilities, their visual inputs remain vulnerable to adversarial attacks, posing significant security risks. Existing defense methods predominantly target single-task scenarios (e.g., zero-shot classification) and consequently lack generalizability across various multimodal tasks. To address this limitation, we propose a dual adversarial fine-tuning framework that jointly optimizes visual and semantic supervision signals from two modalities, enhancing model robustness while generalizing across multiple downstream tasks. The proposed framework comprises two core components, i.e., $\textbf{Visual}$ supervision branch and $\textbf{Semantic}$ supervision branch. The former branch leverages features from clean images, extracted via a frozen original vision encoder, to guide adversarial robustness while the latter incorporates caption-image alignment as a contextual signal to preserve semantic coherence under attack. Moreover, our method achieves cross-task robustness by simply replacing the CLIP vision encoder in the original model, with no need of separate task-specific retraining or architecture this http URL experiments demonstrate that our approach outperforms the state-of-the-art method in adversarial robustness evaluation across zero-shot classification, image captioning, and visual question answering (VQA) tasks.

---


### 68. [SFGA: A Statistics-First Gating Architecture with Adjudicative Escalation for Trustworthy SFT Data Procurement](https://arxiv.org/abs/2607.18960)

**<font color=#1a73e8>作者：</font>** Arther Tian, Alex Ding, Simon Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Procuring supervised fine-tuning (SFT) data forces a buyer to decide, before any downstream training, whether a candidate corpus is worth acquiring. We present \sys{}, a statistics-first gating architecture that treats procurement as a cost-aware routing problem over three intrinsic quality axes -- diversity, utility, and redundancy. Cheap blind measurements are summarised into per-axis estimates with confidence intervals; a gate accepts a decision only when intervals are tight, sample sizes are adequate, and the axes agree, otherwise it escalates the case to an adjudicative debate between a buy-advocate and a reject-advocate judge, resolved by a presiding verdict. On a controlled benchmark of 12 datasets ($2{\times}3{\times}2$ grid over the three axes) with 5 seeds, the gate reaches 0.90 accuracy and 0.83 $F_1$ at \$0.017 per unit, sitting between an always-verify baseline (0.75) and an oracle upper bound (0.98) while spending less than always-escalate (\$0.020). We further report honest negative diagnostics of the debate path: a con-side win rate of 0.80 ($p\approx3{\times}10^{-6}$) and a 52\% position-flip rate under advocate swapping expose negativity and positional biases that a naive LLM-judge would hide. We frame the injected-knob evaluation explicitly as a controlled synthetic benchmark for measurement fidelity and routing calibration, and delimit external validity as future work.

---


### 69. [From Dependency to Compositionality: A Neurosymbolic Lifting of LLM Outputs via Combinatory Categorial Grammar](https://arxiv.org/abs/2607.18961)

**<font color=#1a73e8>作者：</font>** Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) generate fluent text by incrementally predicting the next token from a prefix. Critics in the generative tradition argue that such systems lack genuine grammar; influential replies from the dependency-grammar perspective hold that LLM behavior is well described by local head-dependent structure built word by word. We argue that a sharper observation has been overlooked: the prefix-driven, type-completing dynamics of autoregressive generation align closely with the incremental processing model that Combinatory Categorial Grammar (CCG) was originally designed to support. On this basis we propose a neurosymbolic framework in which LLM outputs are lifted into typed compositional derivations -- not claiming that LLMs implement CCG internally, but that their outputs admit a principled, incremental, and auditable CCG reconstruction. Two consequences follow. First, through the Curry-Howard correspondence the lifting extends beyond natural language to the formal languages LLMs also produce -- programming languages such as Solidity, description-logic and query languages such as OWL and SQL -- with the type system varying and the architecture held fixed. Second, the lifting supports two layers of checking: a compositional layer that catches structural failures directly, and a content layer that checks the lifted structure against external knowledge sources, enabling the earliest possible flagging of hallucinated content. The account thereby requires of a producer not cognition but a prefix-driven generative profile. We close with a sketch of synchronous LLM-CCG coupling as one direction the framework opens.

---


### 70. [Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning](https://arxiv.org/abs/2607.18979)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Haoyu Zhang, Xinke Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to ambiguous learning signals and unstable training. We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning. Treating each path as a player in a cooperative game, we leverage Shapley values to quantify marginal contributions, using a generative reward model to evaluate path utilities and Monte Carlo sampling for efficient approximation. Experiments on mathematical reasoning benchmarks show that Parallel Shapley outperforms existing baselines while providing more stable and interpretable training. Our framework effectively "fishes out the free riders," assigning reward proportionally and improving multi-path reasoning in LLMs.

---


### 71. [AutoJourn: Multi-Perspective Summarisation, Bias Detection and Bias Neutralisation for LLM-Generated News in Automated Journalism](https://arxiv.org/abs/2607.18983)

**<font color=#1a73e8>作者：</font>** Himel Ghosh, Ahmed Mosharafa, Georg Groh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present AutoJourn, a demonstration system for multi-perspective news generation and bias-aware evaluation using large language models (LLMs). The system tackles three core challenges in responsible automated journalism: extracting diverse perspectives from unstructured social media discussions, generating summaries that preserve viewpoint diversity, and detecting or mitigating bias in AI-generated news. The pipeline integrates advanced prompt engineering with optional retrieval augmentation to produce semantically diverse perspective sets, a multi-perspective summarisation module that merges conflicting viewpoints into balanced summaries, and a bias analysis suite supporting sentence-level bias detection and type classification in the generated news article, and automatic neutralisation. Users can inspect perspective clusters, compare stance-specific summaries, generate news articles, and apply bias-aware rewrites directly in the interface. We evaluate each component with intrinsic metrics -- semantic diversity, summary quality, and bias reduction and show improvements over strong baselines while maintaining content fidelity. A live, publicly accessible demo accompanies the paper to facilitate reproducibility and further research on socially responsible automated journalism.

---


### 72. [Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio](https://arxiv.org/abs/2607.18985)

**<font color=#1a73e8>作者：</font>** Jialian Li, Junhong Liu, Yuchen Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities in language understanding, reasoning, and world knowledge. As embodied agents become increasingly capable, there is a growing demand for compact models that can serve as an on-device brain, preserving the broad general intelligence of LLMs while enabling effective high-level interaction with embodied environments. Existing approaches, however, often prioritize either general-purpose intelligence or specialized embodied capabilities, making it challenging to satisfy both requirements within a single model. We present \textbf{Athena-Brain-8B}, an 8B LLM designed to serve as an on-device brain for embodied intelligence for embodied intelligence. Through a multi-stage post-training pipeline consisting of General Supervised Fine-Tuning, General Reinforcement Learning, Embodied Expert training, and Model Merge, Athena-Brain-8B maintains strong general capabilities while acquiring strong high-level embodied interaction capabilities and generating concise responses for efficient embodied interaction. Experimental results demonstrate the effectiveness of Athena across both general and embodied evaluations. Compared with the corresponding Qwen3-8B thinking model, Athena-Brain-8B achieves comparable performance on general language and reasoning benchmarks while generating substantially shorter responses. On in-domain embodied benchmarks, Athena-Brain-8B consistently outperforms models of similar scale and surpasses several substantially larger frontier models evaluated zero-shot, demonstrating that compact language models can effectively integrate strong general intelligence with embodied capabilities.

---


### 73. [DobicVLM: Aligning Chest X-Ray Report Generation with Clinically-Grounded Programmatic Rewards via Group Relative Policy Optimization](https://arxiv.org/abs/2607.18988)

**<font color=#1a73e8>作者：</font>** Thanni Adewuyi, Angelica Obayi, Andem Aniekan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging is a cornerstone of diagnostics, yet automated chest X-ray report generation struggles with structural adherence, anatomical completeness, and semantic faithfulness. We introduce DobicVLM, a vision-language model combining supervised fine-tuning on MedGemma-4B with Group Relative Policy Optimization (GRPO) and clinically-grounded programmatic rewards. Our approach uses interpretable, rule-based reward components; structural verification, anatomical checklist, semantic similarity, and length constraints to enforce clinical standards without neural reward models. Trained on 1,000 de-identified image-report pairs from a private clinical dataset (with ethics approval and compliance to local regulations), DobicVLM is evaluated via blinded expert review on 69 held-out cases. DobicVLM outperforms Gemini 2.5 Flash across the majority of criteria, achieving the highest impression accuracy (27.2%) and medical terminology (86.5%) compared to both Gemini 2.5 Flash and MedGemma 4B baselines, with minor trade-offs in completeness and referrals. This demonstrates GRPO's value for transparent alignment in resource-limited settings. Keywords: Vision-Language Models, Radiology Report Generation, Reinforcement Learning, Medical AI, GRPO

---


### 74. [Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and Challenges](https://arxiv.org/abs/2607.19011)

**<font color=#1a73e8>作者：</font>** Tuo Liang, Zhe Hu, Disheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal humor in memes, cartoons, and comics remains difficult for AI systems because intended meaning depends on non-literal mechanisms, shared cultural knowledge, and communicative intent rather than literal scene description. This survey focuses on visual humor understanding in single-image and multi-panel artifacts, while treating humor generation as an emerging downstream frontier. We position the literature against prior humor, sarcasm, and general MLLM surveys and organize it using a capability-centric hierarchy spanning recognition, interpretation and reasoning, and generation. Under this lens, we synthesize benchmark design, evaluation protocols, and modeling paradigms, tracing the field's shift from task-specific fusion models to large-model approaches based on multimodal alignment, evidence-grounded reasoning, and controlled generation. We conclude by highlighting the main barriers to progress: shortcut-prone evaluation, limited cultural and narrative coverage, weak evidence grounding, and unresolved safety and ownership concerns.

---


### 75. [Mitigating Modality and Language-Style Gaps for Zero-Shot Video Moment Retrieval](https://arxiv.org/abs/2607.19027)

**<font color=#1a73e8>作者：</font>** Jihyun Lee, Cheol-Ho Cho, Woojin Jun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot video moment retrieval aims to overcome the limitations of traditional approaches that require large-scale datasets annotated with text and its relevant temporal spans. Despite advances in pre-trained vision-language models and multimodal large language models, existing ZMR methods still heavily depend on query-to-video content similarity, making them vulnerable to modality and language-style gaps. These gaps lead to unreliable span proposals and unstable moment retrieval results. To address this issue, we propose Self-Similarity-based Moment Proposal and Scoring that instead exploits intrinsic relationships within videos, enabling robust span generation and scoring. By deriving self-similarity only from the video content, we circumvent the noisy and mismatched patterns of query-frame or query-caption similarities, thereby mitigating both modality and language-style gaps. Furthermore, we introduce a query-aware MLLM-based reasoning stage to further sharpen alignment between text and video. Extensive experiments demonstrate that Self-SiMS achieves state-of-the-art performance across ZMR benchmarks.

---


### 76. [IMMoE: Incomplete Multi-View Anomaly Detection via Mixture of View Experts Fusion](https://arxiv.org/abs/2607.19032)

**<font color=#1a73e8>作者：</font>** Lei Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Multi-view Anomaly Detection (MAD) methods assume that all views are completely available and model each view separately. However, in real industrial scenarios, information in the view may be missing due to faults such as occlusion, which leads to the performance degradation of existing methods due to the lack of a multi-view consistency prior. To address this, we explored a more challenging task: Incomplete Multi-View Anomaly Detection (IMVAD), in which some areas of each view were masked. We proposed a pipeline for automatically generating the IMVAD dataset and generated the \textbf{RIMAD} dataset based on the Real-IAD dataset through this pipeline. In addition, in order to effectively utilize the information of multiple views in the absence of view information, we propose \textbf{IMMoE}, which consists of two key modules: (1) Multi-View Expert Fusion (MVEF) effectively fuses multi-view information through a multi-view expert network and guides the reconstruction of a single view; (2) Local Anomaly Enhancement Encoder (LAEE) effectively prevents the model from overfitting the mask region by applying dropout to local features. Our method achieves state-of-the-art performance on both the RIMAD and Real-IAD datasets, especially on RIMAD, we have increased the pixel-level and image-level metrics by 11.8\% and 2.8\%, respectively. Our source code is available at this https URL

---


### 77. [FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](https://arxiv.org/abs/2607.19038)

**<font color=#1a73e8>作者：</font>** Jialong Zuo, Haotong Zuo, Shiwei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Translating novels into films poses a grand challenge for generative artificial intelligence, requiring conversion of abstract literary prose into long-form, multi-scene visual narratives. While current video generation models excel at short, single-scene clips within narrow temporal and spatial contexts, novel-to-film generation operates in a more complex regime, demanding long-duration content across diverse scenes with dynamically evolving entity states. To address this, we formalize novel-to-film generation as dynamic cinematic world modeling, decomposed into two phases: construction, which grounds abstract, underspecified literary narratives into concrete, stateful, and persistent world entities; and evolution, which governs how these entities dynamically update under plot progression to maintain causal consistency across scenes. We propose FilmWorld, an end-to-end agentic system where two groups of specialized agents collaborate to instantiate these phases. Construction-side agents perform narrative structured translation, world entity state modeling with visual anchoring, and state-driven shot planning, progressively projecting literary language into a cinematic blueprint. Evolution-side agents perform state-anchored visual generation, cross-shot dynamic state propagation, and closed-loop state verification to maintain causal consistency and visual coherence. To address the evaluation gap in long-form generation, we introduce FilmEval, a systematic evaluation framework that couples a difficulty-graded benchmark of 15 representative novels with an automated protocol of nine objective metrics spanning three dimensions: cinematic presentation, film consistency, and novel fidelity. Experiments demonstrate that FilmWorld consistently outperforms state-of-the-art video generation agent systems, with particularly pronounced improvements in narrative fidelity and cross-scene consistency.

---


### 78. [Adopting Reinforcement Learning with Verifiable Rewards for Molecular Generation](https://arxiv.org/abs/2607.19044)

**<font color=#1a73e8>作者：</font>** Mingxuan Ouyang, Hao Lan, Wanyu Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leveraging large language models (LLMs) for molecular generation has shown remarkable potential in chemical and drug design. Current methods primarily rely on supervised training or fine-tuning with limited datasets, which are insufficient to capture complex molecular design objectives. While some approaches attempt to guide generation toward specific goals, they often lack direct optimization mechanisms, making it difficult to align generated molecules with desired properties. To tackle these challenges, we propose \textbf{LLMol}, a principled reinforcement learning framework that directly incorporates verifiable rewards for targeted molecule generation. The key insight is to formulate molecular design as a goal-conditioned sequence prediction task, where verifiable rewards serve as explicit supervision to drive generation toward desired objectives. LLMol follows a two-stage training paradigm combining supervised learning and reinforcement learning. In the first stage, large language models are supervised fine-tuned to capture chemical syntax and molecular distributions. In the second stage, we introduce Reinforcement Learning with Verifiable Rewards (RLVR), which directly integrates property-based reward signals to guide molecular generation toward task-specific objectives. To address the high variance and instability common in discrete sequence optimization, we adopt Group Relative Policy Optimization (GRPO), a stable on-policy algorithm that smooths reward signals and improves training robustness. This framework enables LLMol to effectively handle a range of molecular design tasks, including single-property targeting (e.g., penalized logP, QED) and structure-constrained optimization. Experimental results demonstrate that LLMol consistently outperforms existing methods, achieving higher success rates and improved efficiency across diverse molecular benchmarks.

---


### 79. [Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs](https://arxiv.org/abs/2607.19063)

**<font color=#1a73e8>作者：</font>** Harry Rogers, Sally Shiels, Ashley Tomlinson 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective Structured Clinical Examinations (OSCEs) are the gold standard for assessing clinical competence, yet scoring remains vulnerable to examiner subjectivity, fatigue, and cognitive bias. Standard examiner validation via inter-rater statistics lacks explanatory power regarding the source of errors, as it neither analyzes examiner reasoning nor verifies examiner claims against actual events. Thus, we introduce Quality Action Assurance (QAA), a multimodal framework that verifies examiner claims in Virtual Reality (VR) pediatric OSCEs by comparing actions claimed by examiners against the true sequence of events, constructed from video, VR logs, and actor data. QAA combines a constrained temporal action alignment model, which performs action localization and actor source attribution, with a large language model that extracts examiner claims and checks them against the record. Across a 5-fold cross-validation, QAA achieves 99.2% $\pm$ 0.7% Actor F1 and 93.4% $\pm$ 1.9% W@16 for temporal alignment. Overall, QAA detects examiner errors with 70.0% precision and 76.7% recall, improving factual correctness from 39.2% to 79.2%, enabling fairer OSCE assessment.

---


### 80. [Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://arxiv.org/abs/2607.19064)

**<font color=#1a73e8>作者：</font>** Xinjie Zhang, Peng Zhang, Shicheng Zheng 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale visual generators are increasingly capable but costly to train, fine-tune, and deploy. We introduce Mage-Flow, a compact 4B-scale generative stack for efficient text-to-image generation and instruction-based image editing. The stack is built from two co-designed components: Mage-VAE, a lightweight high-fidelity latent tokenizer, and a Native-Resolution Multimodal Diffusion Transformer trained with rectified flow matching. Mage-VAE uses one-step diffusion-style encoding and decoding with anchor-latent regularization, preserving the reconstruction quality of strong public VAEs while reducing tokenization cost by more than an order of magnitude. Together with native-resolution packing and stack-level CUDA kernel fusion, the stack supports flexible-resolution training and improves end-to-end training throughput by about $2.5\times$. Built on this foundation, we develop a complete model family with Base, RL-aligned, and Turbo variants for both generation and editing. Diffusion-NFT improves prompt following, text rendering, aesthetic quality, and editing fidelity, while few-step distillation with adversarial perceptual guidance produces 4-step Turbo models for low-latency inference. Despite its compact scale, Mage-Flow and Mage-Flow-Edit achieves competitive performance across standard generation and editing benchmarks. More importantly, the Turbo variants make high-resolution generation and editing practical for interactive use: at $1024^2$ resolution on a single NVIDIA A100 GPU, Mage-Flow-Turbo generates an image in 0.59s, and Mage-Flow-Edit-Turbo edits an image in 1.02s, while maintaining a small memory footprint. These results show that careful tokenizer--backbone--system co-design can deliver strong high-resolution generation and editing within an efficient 4B model family.

---


### 81. [Delineate Anything v2: A Global Foundation Model for Field Delineation](https://arxiv.org/abs/2607.19069)

**<font color=#1a73e8>作者：</font>** Mykola Lavreniuk, Nataliia Kussul, Andrii Shelestov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate agricultural field boundary delineation at large scale is a foundational task for food security, supply chain transparency, and carbon accounting. While vision foundation models like SAM show remarkable zero-shot capabilities, they frequently fail in geospatial domains due to topological complexity, cropland texturing patterns, and a lack of physical scale awareness. In this work, we introduce Delineate Anything v2, a globally scalable foundation model designed specifically for wide-area field boundary mapping. We construct FBIS-73M, a 73-million-instance multi-resolution dataset spanning 61 countries. To address the pervasive issue of multi-field administrative parcel merging, we introduce a resolution-specific data curation pipeline that leverages topological image-space adaptation to homogenize merged parcels and strengthen weak physical boundaries. Furthermore, we establish a novel, manually curated evaluation benchmark covering 100 countries to assess independent zero-shot generalization. Our results show that Delineate Anything v2 surpasses the current state-of-the-art, including the Delineate Anything framework, by 0.284 mAP@0.5 (+103.3% relative gain), while maintaining execution speeds suitable for rapid national- and global-scale deployment, as demonstrated by nationwide mapping of Ukraine (603,000 km^2) in 5.4 hours on a consumer-grade workstation. Code, pre-trained weights, the FBIS-73M dataset, and ready-to-use national-scale vector boundary products are publicly available at this https URL.

---


### 82. [Context-structured Video Anomaly Detection with Large Vision-Language Models](https://arxiv.org/abs/2607.19077)

**<font color=#1a73e8>作者：</font>** Dongjun Kim, Changjae Oh, Andrea Cavallaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training video anomaly detectors is challenging due to the difficulty and cost of annotating diverse and rare abnormal events. Although recent large vision-language models enable training-free inference, existing approaches mostly rely on holistic inference over sampled video and may miss context-specific anomaly cues. In this paper, we present CSI-VAD, a training-free video anomaly detector that identifies abnormal events across diverse contexts. The key idea is to decompose each video into three distinct contexts (environment, objects, time) and perform context-specific inference in separate branches. Because we ground anomaly judgments solely in context-specific visual cues, we do not require predefined text prompts describing abnormal events or dataset-specific tuning. Experiments on UCF-Crime and UBnormal show that CSI-VAD consistently improves over the direct holistic baseline and achieves competitive performance against existing methods, showing the advantage of structured context decomposition for training-free video anomaly detection.

---


### 83. [Advancing Multimodal Fusion on Heterogeneous Medical Data with Hybrid Geometry Attention](https://arxiv.org/abs/2607.19086)

**<font color=#1a73e8>作者：</font>** Joy Dhar, Manish Kumar Pandey, Nayyar Zaidi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion learning (MFL) has shown great potential in the medical domain, where we are faced with disparate data modalities such as imaging, clinical records, and omics. However, existing MFL strategies face several major challenges. First, they struggle to capture complex cross-modal interactions effectively, which in turn limits performance improvements. Second, they incur high computational costs, restricting their applicability in resource-constrained healthcare AI applications. Finally, they are often designed and evaluated for narrow, fixed modality configurations (e.g., imaging-only, or specific pairs such as image and omics), which limits evidence of their adaptability and generalizability to broader collections of heterogeneous medical modalities. To address these challenges, we propose a novel MFL framework - Cascaded Unified Representation Learning for Efficient Fusion Network (CURE) - a lightweight and scalable framework that progressively integrates various modalities through a novel efficient Hybrid Geometry Aware Fusion layer (HyFuse), where each HyFuse layer is sequentially learned for each modality, making the framework adaptable and generalizable. Within HyFuse, an efficient residual convolution module captures rich multi-scale features to ensure cost-effective learning, while a hybrid-space aware attention mixer learns coarse-to-fine structural cues to better preserve cross-modal relationships. Complementary learnable late-fusion and shared information refinement modules are then employed to learn robust modality-order-invariant shared representations, which in turn yields consistent performance improvements. Extensive evaluations on 16 public datasets show that CURE outperforms leading multimodal fusion methods, boosting performance by up to 3.97% and lowering computational costs by up to 87.8%, ensuring more effective and reliable predictions.

---


### 84. [Latent Riemannian Flow Matching for Geometry-Grounded 3D Foundation Models](https://arxiv.org/abs/2607.19120)

**<font color=#1a73e8>作者：</font>** Lisa Weijler, Irene Ballester, Guofeng Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric foundation models, such as the Visual Geometry Grounded Transformer (VGGT), provide strong 3D priors from unposed images. However, such models operate purely in a feed-forward, deterministic regime, \ie~they cannot generate plausible geometry beyond what the input views directly support. Generative models for 3D scenes, on the other hand, must rely on strong geometric priors to produce coherent outputs from sparse inputs. We bridge these two paradigms by performing flow matching directly in VGGT's latent space, leveraging its learned 3D priors without committing to any explicit downstream representation such as Gaussians, meshes, or video-VAE latents. This requires respecting the latent geometry: VGGT tokens occupy a product of high-dimensional hyperspheres on which standard Euclidean flow matching fails. We address this with a Riemannian Flow Matching framework defined on a product manifold of four hyperspheres, aligned with VGGT's multi-scale encoder, which keeps generated tokens on the valid data manifold required by the frozen decoding heads. On RealEstate10K, ScanNet++ and ETH3D, our method achieves strong performance against recent scene generation baselines in both per-view appearance and aggregated 3D geometry, establishing latent-space flow matching on geometric foundation models as a viable paradigm for 3D generation. The project page can be found $\href{this https URL}{\text{here}}$.

---


### 85. [One Model, Many Graphs: Learning over Attributed Graphs across Heterogeneous Modalities with Vision-Language Models](https://arxiv.org/abs/2607.19128)

**<font color=#1a73e8>作者：</font>** Jiayi Yang, Yifang Chen, Yuanfu Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) provide a unified representation space for textual and visual information, yet their potential as general-purpose backbones for graph-structured data remains largely unexplored. In practice, attributed graphs exhibit substantial modality heterogeneity: some graphs contain only textual node attributes, others only visual attributes, while still others provide both. Existing graph learning approaches are typically designed for fixed modality schemas, requiring separate models for different settings and limiting scalability and cross-graph generalization. To bridge this gap, we present OMG-VLM (One Model, Many Graphs with Vision-Language Models), a unified framework for learning over attributed graphs across heterogeneous modality schemas. OMG-VLM leverages a pretrained VLM as a shared backbone and introduces structure-aware graph adapters that integrate neighborhood information while remaining compatible with the VLM's native embedding space. This design enables effective learning over text-attributed, image-attributed, and multi-attributed graphs within a single model. Extensive experiments across diverse domains show that OMG-VLM consistently outperforms state-of-the-art GNN- and LLM-based baselines on attributed graph learning tasks such as node classification and link prediction, while exhibiting strong generalization to unseen graphs and varying modality schemas. The source code is available at this https URL.

---


### 86. [Reasoning Before Translation: Enhancing Legal Machine Translation with Structured Reasoning](https://arxiv.org/abs/2607.19181)

**<font color=#1a73e8>作者：</font>** Aixiu An, Michael Jungo, Eloi Eynard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural machine translation (NMT) in the legal domain is a linguistically and conceptually demanding task, primarily due to the complexity of legal language and the high level of precision it requires. The recent emergence of reasoning-capable language models opens new possibilities for tackling such challenges. They add to a set of other previously proposed techniques to enhance the translation quality, which includes supervised fine-tuning and reinforcement learning.
In this work, we perform a comparison between these various approaches. More particularly, we evaluate small language models such as Qwen3.5 4B, Qwen3.5 9B, and Gemma 3 12B enhanced with various re-training paradigms and compare their performances against frontier reasoning models. We focus on the Swiss legal system, which -- with its unique multilingual statutes -- offers a particularly challenging testbed for reasoning-augmented models. Our results show that the quality of small ``base'' models can be greatly enhanced, and that reinforcement learning with verifiable rewards can be applied to NMT in the legal domain and surpasses the translation quality of supervised fine-tuning. The performance of enhanced small models is close to the one of state-of-the-art reasoning models yet remains inferior. We also note that re-training paradigms yield diminishing returns as model size increase. The code and models are publicly available at this https URL.

---


### 87. [Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards](https://arxiv.org/abs/2607.19219)

**<font color=#1a73e8>作者：</font>** Xuefeng Jin, Jiashuo Zhang, Teng Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been widely applied to automated essay scoring (AES) and automated feedback generation (AFG). However, existing studies rely primarily on prompt engineering or supervised fine-tuning, while systematic research on reinforcement learning (RL) post-training and automated evaluation of feedback quality remains limited. We propose RLAES, a unified LLM framework that jointly optimizes essay scoring and feedback generation through RL. To make feedback quality measurable, interpretable, and usable for training, we introduce Rubric-based Feedback Evaluation (RFE), an essay-grounded feedback evaluation framework comprising 166 fine-grained binary rubric items and an LLM-as-judge. Building on RFE, we propose Adaptive Gated Feedback Optimization (AGFO), which activates rubric-based feedback rewards on demand during RL, reducing evaluation overhead while improving feedback quality. We also propose Adjacent Contrastive Reasoning (ACR) to improve ordinal score calibration by explicitly contrasting adjacent score levels. Experimental results show that the RFE framework captures essay-feedback consistency, exhibits strong pairwise discriminative power, and closely aligns with expert preferences. On the ASAP benchmark, RLAES-AGFO achieves the best scoring performance among LLM-based methods (QWK = 0.803), while maintaining feedback quality comparable to GPT-5.5 and avoiding the feedback degradation observed under score-only RL. Code and datasets are publicly available at this https URL.

---


### 88. [The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation](https://arxiv.org/abs/2607.19226)

**<font color=#1a73e8>作者：</font>** Michael Jungo, Aixiu An  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has been established as a viable paradigm for the post-training of Large Language Models (LLMs), including downstream tasks, such as Neural Machine Translation (NMT). With the latest research indicating that RLVR could be the preferred training method for translating legal documents due to the induced reasoning capabilities, it raises the question whether it is really attributed to the reasoning or more generally to the training paradigm. We investigate the importance of including the model's reasoning trace in the generated responses during both training and inference by systematically omitting it from one of the phases. Our experiments show that including the reasoning, specifically during inference, has a positive effect on the overall translation quality. Furthermore, we recognise that the reasoning leads to an increase in output tokens, hence we study the cost-quality tradeoff between the increased computational demands and the improved translation quality.

---


### 89. [MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings](https://arxiv.org/abs/2607.19235)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Yuhang Wu, Dongxu Piao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM), the ability to infer other's beliefs, intentions, and states of knowledge, is central to social interaction, yet remains challenging for current Multimodal Large Language Models (MLLMs), especially in multi-party meetings where cues are distributed across speech and behavior. Existing multimodal ToM benchmarks mainly focus on video-grounded question answering over overt, externally verifiable signals, and provide limited coverage of latent social states and group dynamics. We introduce MeetingToM, a benchmark for complex social behavior reasoning in naturalistic multi-party meetings. MeetingToM targets meeting-specific phenomena such as \textbf{pseudo-consensus}, where apparent agreement masks private dissent under social pressure. The benchmark is hierarchically organized to evaluate ToM at increasing levels of social granularity, including (i) subject-level mental state prediction, (ii) dyadic-level addressee understanding, and (iii) group-level consensus reasoning. We provide a unified evaluation protocol and conduct systematic analyses of representative MLLMs, revealing persistent limitations in integrating non-verbal cues, inferring hidden attitudes, and distinguishing genuine consensus from pseudo-consensus. Our results highlight key challenges and establish MeetingToM as a testbed for advancing meeting-grounded ToM in multimodal models.

---


### 90. [Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs](https://arxiv.org/abs/2607.19243)

**<font color=#1a73e8>作者：</font>** Alexander Manev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although Large Language Models (LLMs) demonstrate remarkable multilingual fluency, their internal knowledge representations remain disproportionately biased toward high-resource languages. This leads to cross-lingual factual inconsistency, where they shift their empirical answer distributions based solely on the prompt language. We investigate whether these biases can be mitigated at inference time, forcing an English-prompted model to answer as if it were queried in target languages (German, Spanish, Bulgarian), and evaluate four intervention strategies: zero-shot contextual steering (persona prompting), internal representation manipulation via Contrastive Activation Addition (CAA), and lightweight weight modification via Direct Preference Optimization (DPO) trained on benchmark-derived factual data as well as conceptual generalization data. To assess alignment, we curate a multilingual factual dataset alongside a novel generalization benchmark comprising culturally rooted queries to determine whether factual interventions transfer to broader target-centric preferences. Experiments on Gemma 3 12B Instruct reveal persona prompting to be the strongest overall intervention, balancing efficacy, safety, and out-of-domain generalization. While CAA yields sharp inconsistency benchmark shifts, it is configuration-sensitive and risks knowledge degradation. DPO-based adapters offer permanent, yet narrower and less transferable gains. These findings suggest that cross-lingual inconsistency is at least partly a selection problem, and that simple contextual interventions may outperform more invasive methods for robust, transferable alignment.

---


### 91. [Prompt Design at Scale: How Format, Instruction Count, and Context Length Shape Instruction Adherence and Hallucination in Large Language Models](https://arxiv.org/abs/2607.19257)

**<font color=#1a73e8>作者：</font>** Netanel Eliav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practitioners make three prompt-design decisions with almost no controlled evidence behind them: how to format instructions and context (markdown, plain text, prose, or tabular), how many simultaneous instructions a system prompt can carry before compliance degrades, and how much context a model can hold before recall and honesty degrade. We report two controlled experiments crossing all three factors on one held, contamination-free synthetic corpus (the "Book of Veyra," 8,780 uniquely-named entities, deterministically regenerable from a fixed seed), evaluated across five models.
Experiment 1 (960 calls/model) measures instruction-following decay as rule count N grows from 10 to 160, crossed with four formats and system-prompt vs. user-turn placement. Perfect-response rate collapses to zero by N=80 for every model, format, and placement. Placement produces effects at least as large as format at N=160 in most models, but the direction is model-specific. No model shows a reliable markdown advantage; one 35B model favors plain text instead.
Experiment 2 (5,520 calls/model) measures recall accuracy, false-premise sycophancy, and absent-fact fabrication across a 2k-to-512k-token context ladder in the same four formats. Recall stays near ceiling through 64-128k tokens, then degrades sharply and format-dependently: one model's accuracy spread reaches 48 points at 128k tokens. Fabrication never occurs (0/5,760 probes), and sycophancy stays negligible (<=8.3%). What rises sharply near each model's context ceiling is outright refusal to answer (0% to 79-90%), distinct from sycophancy or fabrication. Neither pre-registered format ordering holds, and token overhead (+22% to +37% over plain text) further changes which format is preferable where accuracy spread is genuine.
We release the full harness, corpus generator, and raw results (VeyraBench): this https URL

---


### 92. [Benchmarking Generalization in Financial Statement Fraud Detection: robust evaluation and novel tasks](https://arxiv.org/abs/2607.19259)

**<font color=#1a73e8>作者：</font>** Guy Stephane Waffo Dzuyo, Gaël Guibon, Christophe Cerisara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial statement fraud detection (FSFD) is crucial for market integrity but faces challenges from increasingly sophisticated schemes and under-utilized textual data in financial reports. Existing methods often rely on random data splits, leading to overoptimistic performance estimates that do not reflect real-world generalization to new companies or future periods. To address this recurring problem with the state of the art, we propose a robust FSFD framework leveraging Large Language Models (LLMs) to integrate both structured financial data and unstructured textual information from financial reports. We provide a more realistic evaluation through a novel and challenging benchmark task called Company-Isolated FSFD (CI-FSFD). We construct and make publicly available a comprehensive U.S. company dataset combining financial statements, summarized MD&A text, and fraud labels. Our approach achieves the best performance on the challenging CI-FSFD task, demonstrating the critical value of textual data and robust evaluation for reliable financial fraud detection.

---


### 93. [PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image](https://arxiv.org/abs/2607.19261)

**<font color=#1a73e8>作者：</font>** Dankai Liao, Tianyi Zhang, Yufeng Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide image (WSI) diagnosis requires identifying diagnostically relevant regions, examining them across magnifications, and integrating multi-scale evidence. However, most existing pathology benchmarks evaluate models on pre-cropped patches or pre-extracted slide features, leaving their ability to acquire evidence directly from gigapixel WSIs largely untested. We introduce PathAgentBench, a benchmark for evaluating evidence-seeking vision-language models (VLMs) across four complementary capabilities: image-to-text matching for evidence interpretation, text-to-image retrieval for evidence verification, diagnostic-region localization for evidence acquisition, and multi-scale reasoning for evidence integration. The benchmark is organized as a diagnostic tree that links nested regions across magnifications with scale-specific findings and path-level diagnoses. It contains 1,822 TCGA WSIs and 17,135 diagnostic paths annotated by ten board-certified pathologists. An additional private cohort of 190 breast cancer WSIs with detailed annotations is used to evaluate autonomous whole-slide exploration. We evaluate 20 general-purpose, medical, and pathology-specialized models. Leading open-weight models achieve over 93% accuracy in multi-scale reasoning and over 50% accuracy in both cross-modal matching tasks. In contrast, diagnostic-region localization remains challenging: the best text-guided mean intersection-over-union is below 0.09, underperforming a simple center-based heuristic. During autonomous exploration, the unconditional hit rate decreases from 0.522 at low magnification to 0.185 at intermediate magnification and 0.020 at high magnification. These results reveal a pronounced gap between reasoning over curated evidence and acquiring that evidence directly from WSIs. PathAgentBench provides a unified framework for measuring and improving evidence-seeking pathology models.

---


### 94. [Toward Auditable Fraud Detection: Combining Graph Features, Model Explanations, and Agentic Case Investigation](https://arxiv.org/abs/2607.19266)

**<font color=#1a73e8>作者：</font>** Rahil Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fraud detection systems must scale with rising transaction volume while remaining explainable and reviewable. We study a layered pipeline on the PaySim dataset that combines a gradient-boosted classifier, graph-derived structural features, an autoencoder-based anomaly signal, TreeSHAP explanations, and a bounded LLM investigation agent applied to cases the classifier scores uncertainly. Before any model comparison, we identify and remove a simulator-specific balance shortcut that would otherwise inflate baseline performance. After this correction, neither the graph features nor the anomaly signal improves Average Precision on the full test set. Both, however, rank fraud better within the subset of cases receiving intermediate baseline scores. In a controlled experiment with injected multi-account fraud rings, engineered structural features recover all injected test transactions, while the tabular baseline misses roughly a quarter of them. The investigation agent underperforms direct thresholding of the classifier it relies on, reaching 65.0% accuracy against 71.7% on a balanced 60-case sample, despite having access to model explanations, graph context, and retrieved reference cases. Of the eight decisions the agent changed, six replaced correct classifier outputs with errors, and it produced a coherent written rationale in each case. An exploratory disagreement-based escalation rule flagged two of these agent errors for human review without flagging any correct decision. We conclude that each component of a layered fraud system contributes only under specific conditions, and that a plausible rationale from an investigation agent is not evidence of a better decision.

---


### 95. [Graph-Based Agentic AI with LangGraph: Workflow Pathways for Long-Running Stateful Business Processes](https://arxiv.org/abs/2607.19297)

**<font color=#1a73e8>作者：</font>** Daniel Pearson, Sidney Shapiro, Emiliano Sebastian Gonzalez Venegas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper is a practitioner guide to graph-based workflow pathways for long-running, stateful, multi-step generative AI systems in business processes. Rather than treating LangGraph, a low-level orchestration framework for stateful agents, as a model-quality benchmark target, we present three executable recipes -- SQL analytics with repair loops, agentic retrieval-augmented generation with evidence gating, and human-in-the-loop policy review with interrupt and checkpoint recovery -- to show how typed state, conditional routing, deterministic tools, retries, interrupts, checkpoints, and traces fit together. LangGraph is positioned by workflow-complexity fit, not as a universal default: simpler ReAct-style or plain SDK loops may be better for basic tool use, schema-first tools for structured extraction and validation, and DSPy when prompt or program optimization is the main goal. Each recipe explains when LangGraph is worth the extra structure and which implementation patterns make routes, pauses, and audit trails explicit product behavior rather than hidden prompt logic.

---


### 96. [LLM Detection as an Intervention: Downstream Impact under Strategic User Behavior](https://arxiv.org/abs/2607.19300)

**<font color=#1a73e8>作者：</font>** Meena Jagadeesan, Tatsunori Hashimoto, Jon Kleinberg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM adoption becomes more widespread, there is a growing interest in detecting LLM-generated content, for example through LLM detection tools and through heuristics based on language patterns. Detectors operate as an intervention that steers not only the detected attribute itself, but also downstream metrics such as LLM usage and output quality. In this work, we demonstrate how imperfect LLM detectors lead to counterintuitive impacts on these downstream metrics, by distorting how users are incentivized to use LLMs in their workflow. We develop a stylized model which captures how users strategically choose how much to use the LLM and how to post-process content to reduce the detected attribute. Using this model, we show that LLM detection can counterintuitively lead humans to increase their LLM usage. Moreover, even when reducing the detected attribute improves output quality, we find that introducing an LLM detector can lead users to produce lower quality outputs. In contrast, we show that detectors result in a clean "rise-then-fall" pattern for the detected attribute, which we empirically reproduce for word frequencies on arXiv abstracts. Altogether, our work illustrates how LLM detection can distort LLM usage and output quality, uncovering failure modes when LLM detectors operate as an intervention on these downstream metrics.

---


### 97. [Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness](https://arxiv.org/abs/2607.19322)

**<font color=#1a73e8>作者：</font>** Xilun Chen, Zhaleh Feizollahi, Ross Goodwin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating the factuality of long-form generations has focused predominantly on precision, measuring whether the claims a model makes are correct. The dominant decompose-search-verify pipeline catches incorrect claims well but says little about whether a response contains all the information it should. Measuring factual completeness, the missing half of factuality, is harder: it requires enumerating the full set of facts a complete answer should contain, and these facts rarely form a flat list. They often involve open-ended sets where coverage is what matters, ordered processes, and relationships among facts that a list of independent boolean checks fails to capture. We introduce a two-level meta-rubric framework for evaluating open-ended generation, and instantiate it as Gamut (Grounded Assessment of Multimodal Factuality), a benchmark for factual completeness in long-form generation. The framework rests on a two-level rubric representation: a structured meta-rubric captures the organization and importance of the required content, which is then mechanically compiled into a flat checklist of binary, machine-gradable rubrics that an LLM judge scores reliably. We construct 1,813 questions grounded in real wearable imagery across 10 diverse domains, each paired with an evidence-backed rubric verified by expert human annotators. Because the framework is modality-agnostic, we also release a text-only variant. Evaluating 14 frontier and open-weight models, we find the benchmark genuinely challenging (best score 58.7% from Gemini 3.1 Pro), highly discriminative, and robust to the choice of judge.

---


### 98. [Selective State-Space Adaptation and Retrieval for Language Model Reasoning](https://arxiv.org/abs/2607.19326)

**<font color=#1a73e8>作者：</font>** Atahan Dokme, Larry Heck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation introduces a static learned update applied identically to every input. The update provides task-level adaptation but does not explicitly represent token-level or instance-level state variation. A family of adapters is proposed that introduces selective state-space recurrence at two complementary granularities. At the token level, \textbf{MaLoRA} (Mamba-modulated low-rank adaptation) makes the adapter's scaling factor a dynamic input-dependent function with recurrent state across tokens, in contrast to the stateless modulators of prior work. At the context level, \textbf{MaRA} (Mamba Retrieval Adapter) tracks cross-segment state and selects the segments most relevant to the query, before the modulated language model generates its answer. Across three frozen backbones (Qwen-2.5-7B, Llama-3.1-8B, Gemma-2-9B) and two reasoning benchmarks (MuSiQue, 2WikiMultihopQA), the family improves reasoning accuracy on every cell of the $3{\times}2$ grid, by $+6.8$ F1 ($+10.5\%$ relative) on average and up to $+9.3$ F1 ($+18.2\%$ relative) on the hardest cell over the LoRA baseline, and the token-level gains carry to RULER QA-2 under length stress.

---


### 99. [ISO: An RLVR-Native Optimization Stack](https://arxiv.org/abs/2607.19331)

**<font color=#1a73e8>作者：</font>** Hanqing Zhu, Wenyan Cong, Zhizhou Sha 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is rapidly advancing the reasoning capabilities of language models, yet the optimization layer that converts reward feedback into weight-space updates remains poorly understood. Building on our prior analysis (Zhu et al., 2025), we study this missing layer through the singular structure of model weights and identify spectral inheritance: RLVR can reuse the base model's weight spectra while acquiring new behavior through changes in the associated input and output singular frames.
We operationalize spectral inheritance as Isospectral Optimization (ISO), an RLVR-native, fixed-spectrum optimization framework with complementary offline and online instantiations. Offline, ISO-Merger combines the frame changes of shared-base specialists into a single fixed-spectrum model, requiring no post-merge data, rollouts, gradient updates, or on-policy distillation (OPD). It recovers complementary specialist capabilities and achieves the strongest aggregate performance among the compared data-free merging methods. Online, ISO-Optimizer applies a chosen base optimizer, including AdamW and Muon, to the frame variables while keeping the base spectra fixed. Across reasoning and coding tasks ranging from 1.5B to 8B parameters, ISO-Optimizer improves accuracy in the reported runs and reaches matched scores with substantially fewer training steps. On Qwen3-8B-Base, AdamW reaches an aggregate accuracy of 0.495 after 270 training steps. ISO-AdamW reaches the same accuracy after only 100 training steps and improves further to 0.509 after 210 training steps. Together, ISO offers a concrete answer to RLVR's missing optimization layer: rather than inheriting pre-training optimization wholesale, design post-training around the structure of reward-driven adaptation: inherit the spectrum, optimize the frames.

---


### 100. [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/abs/2607.19336)

**<font color=#1a73e8>作者：</font>** Grace Hui Yang, Pranav N. Venkit, Hooman Sedghamiz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems large language model (LLM) based architectures capable of reasoning, planning, acting, and coordinating with tools and other agents are rapidly transitioning from research prototypes to production scale deployments across domains such as software engineering, scientific discovery, and finance. While academic work has emphasized benchmarks and algorithmic innovation, deployment raises new challenges around robustness, safety, and reliability. This tutorial brings together researchers and practitioners to explore advances in reasoning and planning, multi agent coordination, and evaluation, highlighting open challenges arising from deployment experience. Through applied case studies in pharmaceutical discovery and financial systems, we analyze common design patterns that make agentic systems successful, and discuss practical mitigation strategies for failure modes, such as verification pipelines, fallback mechanisms, and human in the loop supervision. Attendees will gain a comprehensive view of the field along with concrete design patterns, evaluation checklists, and templates for safe and reliable deployment across industries.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-104](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
