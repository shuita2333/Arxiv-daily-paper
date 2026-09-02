# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 101. [JudgePanel: A Compact Judge with Panel Deliberation via Adaptive Multi-Reward Reinforcement Learning](https://arxiv.org/abs/2608.29168)

**<font color=#1a73e8>作者：</font>** Yiyue Qian, Shinan Zhang, Huan Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The LLM-as-a-Judge paradigm has emerged as a scalable alternative to human evaluation. However, single-model judges are limited by their inherent model biases, while multi-agent evaluation protocols that mitigate this through diverse deliberation are prohibitively expensive at inference time. To this end, we propose \textbf{\modelname}, which equips a compact \underline{Judge} model with multi-agent \underline{Panel} deliberation capability. Specifically, we first train on panel deliberation traces from an ensemble of strong evaluators, capturing structured patterns of discussion, disagreement, and resolution. To further improve judgment quality beyond SFT, we introduce \textit{AdaReward}, an adaptive multi-reward RL algorithm that dynamically rebalances reward component weights as different objectives saturate at different rates during RL training. For practical deployment, we further design a lightweight domain specialization module for rapid adaptation to new evaluation domains with few hundred labeled samples. As a result, (i) \textit{Novel}: the first framework to equip a single compact judge with multi-agent panel deliberation capability at single-model inference cost; (ii) \textit{Effective \& Reliable}: JudgePanel with a 14B backbone outperforms judge-specialized models up to 70B across four evaluation benchmarks, demonstrates strong position consistency, and rapidly specializes to new domains with few hundred samples.

---


### 102. [Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space](https://arxiv.org/abs/2608.29188)

**<font color=#1a73e8>作者：</font>** Qiancheng Zhou, Ruizhe Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) substantially improves single-sample accuracy (pass@1) but causes the policy's solution space to contract, diminishing the returns of test-time scaling. In this work, we investigate where inside a reasoning trajectory this breadth is lost: does the policy fail to access a valid solution family, or does it fail to execute computation once initiated? To disentangle access from execution, we analyze the Countdown task, whose solution space can be exhaustively enumerated into discrete entrance families defined by the first operand and operator, across PPO on Qwen2.5-3B and GRPO on Qwen2.5-3B-Instruct. Across both training setups, solution coverage falls by up to 67%, halving even on problems solved across all checkpoints. We show that this contraction is heavily concentrated at the entrance: per-token likelihood shifts are 11x--16x larger prior to the first arithmetic operation than during downstream reasoning. Supplying only an unselected entrance prefix restores completion rates in low-access families by over an order of magnitude (0.018 -> 0.212 under PPO), demonstrating that alternative solutions remain executable but are no longer initiated. Guided by this localization, we find that while surface prompting fails to recover diversity, entrance-targeted interventions succeed: late-layer parameter interpolation with early checkpoints increases solution coverage by 37% at no loss in pass@1. Finally, we show that early-step entropy collapse recurs across six math benchmarks with 7B and 14B models, but is not an inevitable byproduct of reasoning optimization: an SFT baseline preserves more than double the coverage, and staged SFT--DPO--RLVR pipelines retain early-step entropy. In summary, reasoning breadth is lost at the door, not inside the room. Code: this https URL.

---


### 103. [HalluPrism: When Multimodal Uncertainty Should Diagnose, Not Decide](https://arxiv.org/abs/2608.29193)

**<font color=#1a73e8>作者：</font>** Aman Prakash, Sourish Dasgupta, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) can assign similar confidence to answers that fail for different reasons. We propose HalluPrism, a behavioral diagnostic that re-runs an answer after visual degradation, blank-image replacement, and grounding or relation checks. These targeted probes yield a signature over visual-perturbation sensitivity (V ), image-removal confidence retention (L), and grounding/relation-probe instability (A). Across 58K+ examples from four benchmarks and four MLLMs, image-removal confidence retention is most prevalent, while grounding/relation-probe instability better separates failure families. Only 18 of 48 source-target checks are diagonally aligned, so the coordinates should be interpreted jointly rather than as independent causal sources. With the dataset fixed, the joint signature improves failure-family AUROC from 0.634 to 0.769 on HallusionBench and from 0.707 to 0.817 on VizWiz, with smaller gains on POPE and VSR. In pooled XGBoost analysis, AUROC rises from 0.78 with scalar confidence to 0.95 with (V, L, A) and 0.97 when confidence is added. The same signature does not automatically improve correctness ranking. The three tested direct scalarizations can harm it. These results separate failure diagnosis from abstention scoring: multimodal uncertainty should characterize failure structure before it is used to decide whether to abstain or correct.

---


### 104. [How Identity and Opinion Shape Political Sycophancy in LLMs](https://arxiv.org/abs/2608.29198)

**<font color=#1a73e8>作者：</font>** Li-Ni Fu, Chang-Chih Meng, Chien-Hua Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) increasingly encourage users to disclose personal profiles for tailored assistance, measuring their political alignment becomes increasingly important. However, many existing benchmarks for assessing political behavior rely on closed-ended questions and do not fully capture how a model's stance may adapt to user-provided context during interaction. We introduce a framework that disentangles two distinct triggers of political sycophancy: opinion (aligning with explicit narratives) and identity (stereotyping based on demographic labels). Using 450 manually-checked political dilemmas as controlled probes, we evaluate 13 instruction-tuned LLMs. We uncover a dissociation: a model's susceptibility to explicit opinions does not necessarily predict its susceptibility to identity cues, and vice versa. When both signals are present, their effects are generally sub-additive rather than simply additive. Additionally, system-level personas primarily shift a model's baseline stance while having limited effect on the stance shift caused by user opinion or identity. Ultimately, our results suggest that LLM political stance is interactively and steerably vulnerable rather than being a fixed trait, highlighting how personalization may amplify identity- or opinion-conditioned shifts in the model's behaviors.

---


### 105. [Benevolent Bias in Multi-Turn Human-Agent Dialogue](https://arxiv.org/abs/2608.29206)

**<font color=#1a73e8>作者：</font>** Qianqi Liu, Jin Huang, Fethiye Irmak Dogan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bias in human-agent interaction can manifest not only through hostile language but also as benevolent bias, whereby unequal treatment hides behind a warm, positive tone. To make it detectable, we operationalise benevolent bias along two dimensions, tone and treatment, yielding three classes: neutral support, overt bias, and benevolent bias. Building on these definitions, we construct BENEVDIAL, a class-balanced corpus of 362,880 multi-turn support dialogues spanning user and agent demographics, roles, and generators, to support controlled evaluation. We then test two detector families on it: off-the-shelf safety detectors and prompted large language model (LLM) judges. Our results reveal a detection gap: off-the-shelf detectors reliably flag overt bias yet largely miss benevolent bias, while LLM judges catch more under more explicit detection criteria but increasingly misclassify neutral support as benevolent bias, and demographic context amplifies the false alarms. These findings suggest that fair monitoring of human-agent dialogue must look beyond surface cues to whether the agent's treatment is disparate.

---


### 106. [Hyper-Fold: Exploring the Expressive Limit of Sequence-Geometry Learning for Proteins via Hypergraph Modeling](https://arxiv.org/abs/2608.29207)

**<font color=#1a73e8>作者：</font>** Yifan Feng, Guanjie Cheng, Shihui Ying 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein structure modeling rests on a single computational primitive: the interaction between what a residue is (sequence content) and where it sits (three-dimensional geometry). What is the expressive limit of this layer class? We show that the complete bilinear operator over content-geometry outer products--the sufficient statistic of all second-order interactions--is the expressive ceiling, while the additive message passing of mainstream geometric GNNs is provably blind to content-geometry binding. We then introduce Hyper-Fold, a rank-K separable convolutional backbone approaching this ceiling at message-passing cost: each radius neighborhood is organized into a sequence hyperedge and a contact hyperedge, modulated by an edge-conditioned matrix-valued operator factorized into K learned basis operators with geometry-generated coefficients. Across enzyme function prediction, fold classification, and ligand binding site detection, Hyper-Fold and its hierarchical variant Hyper-Fold-Deep achieve the best results among protein-specific structure encoders; Hyper-Fold-Pocket, an anchored set-prediction head, surpasses UniSite-3D on UniSite-DS and two zero-shot benchmarks with no sequence language model features, 68x fewer parameters, and 4.8x lower latency--suggesting that a sufficiently expressive 3D backbone recovers information that fusion architectures previously borrowed from evolution-scale pretraining.

---


### 107. [Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities](https://arxiv.org/abs/2608.29209)

**<font color=#1a73e8>作者：</font>** Millicent Ochieng, Felermino D. M. A. Ali, Elizabeth A. Ankrah 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we examine how well AI-generated multimodal stories align with the lived practices, relationships, language, values, and visual expectations of the communities they represent. We conduct a community-grounded mixed-methods evaluation with 19 culture representatives across five African communities, combining quantitative annotations with qualitative focus group discussions. We find that cultural alignment depends not simply on recognizable cultural markers, but on how those markers fit social, linguistic, procedural, and visual context. From these evaluations, we develop a taxonomy of cultural alignment comprising five broader cultural marker categories and eight recurring mechanisms of misalignment. We additionally evaluate five multimodal LLM judges to examine whether automated evaluation can approximate community-grounded judgments at scale. Judge reliability and score calibration vary substantially across communities, with no single judge performing consistently across all five settings. These findings motivate community-calibrated evaluation pipelines in which automated judges are validated against community judgments to determine where they can be trusted and where human review remains necessary.

---


### 108. [Attribute-Based Activation Steering of LLMs for Group-Specific Explanation Generation](https://arxiv.org/abs/2608.29215)

**<font color=#1a73e8>作者：</font>** Leandra Fichtel, Janek Prange, Henning Wachsmuth  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To effectively enable people to understand new topics, explanations should be tailored to their backgrounds and abilities. So far, prompting alone has been shown to be insufficient for creating such explanations and other computational methods are missing. Therefore, this paper investigates whether LLMs can be steered to generate explanations that are tailored to a specific group of people. To this end, we propose an approach that first identifies group-specific attributes in terms of explanatory style and knowledge of a specific target group. Building on activation engineering, it then computes attribute-based steering vectors and adds them to the internal activations of an LLM during inference to enable a fine-grained steering. In our experiments, we assess the steering effectiveness of our approach in terms of specificity and factuality of the generated explanations. Additionally, we evaluate the explanations in a study with human experts from different target groups. Compared to prompting and state-of-the-art steering baselines, our approach tailors the explanations significantly better to the target group while largely maintaining factuality.

---


### 109. [Localizing Emergent Failures in Agentic AI: Recovering Minimal Repair Families via Counterfactual Replay](https://arxiv.org/abs/2608.29228)

**<font color=#1a73e8>作者：</font>** Bingjie Li, Yumeng Song, Zhongming Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Failures in agentic AI systems can arise from interactions among messages exchanged by multiple large language model (LLM) agents. Pointwise attribution cannot distinguish a jointly necessary repair from alternative singleton repairs. We formulate Minimal Repair Family Recovery (MRFR): recovering all inclusion-minimal event sets whose counterfactual replay restores task success within a declared size bound. We propose Graph-Constrained Joint Replay (GCJR), which slices failure-relevant events from an execution dependency graph, constructs graph-feasible singleton and pair candidates, and verifies them by replay with paired clean counterparts. For fixed replay outcomes, GCJR is exact within its declared graph domain. On 90 in-scope cases from a 120-DAG controlled benchmark, GCJR achieves 1.000 Family Exact Match while reducing mean replay calls from 56.3 to 25.3 (55.1%) relative to exhaustive search. On a 24-case, four-agent LLM pilot, it again achieves 1.000 Family Exact Match and reduces mean model calls from 21.0 to 10.0 (52.4%); single-event replay misses jointly necessary repairs.

---


### 110. [When Patients Cut In: Extending Clinical Conversational AI Safety to Interruptions](https://arxiv.org/abs/2608.29241)

**<font color=#1a73e8>作者：</font>** Zachary Ellis, Spencer Hazel, Adam Brandt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical voice agents are now deployed in routine care, where real patients do not wait their turn: they interrupt. These systems typically use a cascaded architecture (speech-to-text -> LLM -> text-to-speech), so when a patient cuts the agent off mid-utterance, clinically required content can be lost even when the model handles cooperative transcripts well. Yet clinical conversational-AI benchmarks almost universally assume patients wait for the agent to finish, missing interruption-induced loss of required content. We present a transcript-based evaluation of interruption recovery, adapting conversation-analytic overlap categories into three operational types (recognitional, competitive, transitional sub-unit) and testing four deployment-oriented, non-reasoning LLM configurations across four cells spanning history-taking (information gathering) and FAQ (information provision), scored on whether the agent preserves the clinically required content. In the gathering cells, target-question failure varied across models; in the provision cells, where arms are directly comparable, failure rose for every model. Rankings differ across cells, and competitive FAQ interruption produced 30/30 provision-coverage failures for all four models (Wilson 95% CI: 88.6-100.0%; baseline 0/30 for three, 4/30 for Llama). A brief apology marker ("sorry to interrupt") shifts recovery by tens of percentage points, inconsistently across models, and for one it reduces recovery. Interruption robustness therefore cannot be a single score: evaluation must be content-grounded, reported per cell, and matched to the deployment's interruption profile.

---


### 111. [Validating FKG.in: Soundness Assessment in LLM-Augmented Indian Food Knowledge](https://arxiv.org/abs/2608.29249)

**<font color=#1a73e8>作者：</font>** Saransh Kumar Gupta, Armaan Shah, Lipika Dey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The online culinary ecosystem is increasingly populated by recipe content generated, modified, or summarized by Large Language Models (LLMs). While often plausible, such outputs may contain hallucinated ingredients, misrepresented quantities, or culturally implausible combinations, limiting their suitability for downstream applications and knowledge graph construction. In this paper, we present a semi-automated soundness assessment workflow for validating structured recipe data extracted and augmented by LLMs from informal culinary sources. Developed as part of this http URL, a knowledge graph of Indian food, the pipeline identifies and addresses common failure modes, including structural inconsistencies, semantic and logical incoherence, and deviations from the source text, through a multi-stage process combining formal grammars, vocabulary-based checks, statistical heuristics, Set Transformer-based coherence modeling, and retrieval-based verification. Although evaluated on Indian recipes, the proposed methods are applicable to broader multilingual and multicultural culinary domains. We provide a practical, auditable, and application-agnostic framework for validating LLM-augmented recipe data, thereby strengthening the foundations of machine-readable food knowledge infrastructures in the era of LLM-generated content.

---


### 112. [GuardianAgent: Policy-Conditioned Risk-Adaptive Anonymization with Verified Adversarial Escalation](https://arxiv.org/abs/2608.29251)

**<font color=#1a73e8>作者：</font>** Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Privacy protection for live web traffic requires more than detecting private spans. Agent-based privacy protection systems must determine whether an outgoing action complies with the destination site's privacy policy, then apply only the level of rewriting or sanitisation justified by the residual disclosure risk. We present GuardianAgent, a policy-conditioned anonymization framework that couples structured risk assessment with verified adaptive rewriting. GuardianAgent computes risk through AMRSF (Adaptive Multi-factor Risk Scoring Formula), an explicit controller that combines policy-violation likelihood with data sensitivity, recipient transmission, purpose legitimacy, contextual basis, and policy transparency, rather than relying on an LLM to assign risk directly. This risk score determines both the allow/transform/deny decision and the initial anonymization level. For efficiency, GuardianAgent uses an evidential fast path for low-uncertainty policy matches and invokes an LLM slow path only for uncertain cases. For rewriting, it applies a five-level hierarchy driven by a verified adversarial guesser: guesses trigger escalation only when supported by the original text, preventing hallucinated attacker confidence from causing unnecessary over-anonymization. Experiments across three benchmarks spanning legal text (TAB), Reddit posts (SynthPAI), and multi-format synthetic PII records (PII-Masking-300k) show that GuardianAgent achieves the strongest privacy-utility trade-off among published baselines and is the only method to reach more than 0.90 privacy in all three domains, remaining robust under a backbone switch. Action-context stress tests further show that the same outgoing text receives different decisions and anonymization strengths under different recipients, purposes, action bases, and policy-transparency conditions.

---


### 113. [Large Language Models Systematically Favor Popular Options: Evidence and Mitigation Across MCQs](https://arxiv.org/abs/2608.29257)

**<font color=#1a73e8>作者：</font>** Abdelrahman Abdallah, Mohammed Ali, Bhawna Piryani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice questions (MCQs) are a standard format for evaluating large language models (LLMs), yet the popularity of answer options can confound evaluation. Modern LLMs systematically prefer popular but incorrect options over less popular correct ones, a vulnerability we call \textbf{popularity bias}. This pattern aligns with confidence miscalibration: model confidence remains high even as accuracy collapses for popular options. To systematically isolate this phenomenon, we introduce \textbf{PopMCQ}, a benchmark with six controlled strategies that vary option popularity while keeping the correct answer fixed. In our most adversarial setting, where all distractors are more popular than the correct option, models choose popular but wrong answers 66\% of the time. To mitigate this bias, we propose \textbf{PopDebias}, a lightweight inference-time correction that estimates and removes a popularity prior from model predictions. It requires no fine-tuning, is label-free at test time (using only a small calibration split for parameter fitting), and adds negligible computational cost. Experiments on 22 open-source LLMs (0.5B to 32B parameters) show consistent improvements, with accuracy gains up to 54.1 percentage points under strong popularity pressure. The code and data are available this https URL

---


### 114. [RACER: Reinforced Agent Collaboration for Explainable Reasoning on Knowledge Graphs](https://arxiv.org/abs/2608.29263)

**<font color=#1a73e8>作者：</font>** Yuwei Lou, Hao Hu, Yuzhou Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often suffer from hallucination and struggle with complex reasoning tasks requiring multi-hop domain knowledge. While integrating Knowledge Graphs (KGs) provides a structured and verifiable information source, current KG-enhanced LLM paradigms usually rely on single-agent path extraction and fixed prompting, lacking adaptability and facing huge search spaces. To address these challenges, we propose RACER, a Reinforced Agent Collaboration framework for Explainable Reasoning on knowledge graphs. RACER employs a semantic-aware action pruning and teacher-guided reinforcement learning mechanism to efficiently extract high-quality reasoning pathways from large-scale KGs. Furthermore, to mitigate single-path generation pitfalls, we introduce a cross-task accumulated shared memory graph paired with an attention-driven multi-path knowledge refinement module. Finally, RACER orchestrates these components through a four-role multi-agent collaboration system (GraphAgent, TemplateAgent, AnswerAgent, and CriticAgent) to dynamically refine prompts and evaluate answers. Extensive experiments on CommonsenseQA and OpenBookQA datasets demonstrate that RACER significantly outperforms state-of-the-art KG-enhanced LLM baselines with an average improvement of 5\%, offering robust and highly interpretable reasoning capabilities.

---


### 115. [Learning to Ground Before Reading: Unified PCB Engineering Drawing Parsing with Compact Vision-Language Models](https://arxiv.org/abs/2608.29268)

**<font color=#1a73e8>作者：</font>** Jinghao Liu, Xingrun Liu, Gengchen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> PCB engineering drawings mix sparse graphics, dense tables, and text whose meaning depends on page position. Localizing the regions and sending crops to specialized recognizers are determined as the methods for most parsers, so missed regions cannot be recovered downstream. We train a compact VLM to read the full page and get a sequence of region classes, normalized boxes, and text or HTML content. Bounding boxes are converted to coordinate tokens for supervision. Inference uses no detector or crop parser. The joint target is difficult to optimize because class and box tokens are sparse relative to the much longer content sequences. Our localization-first curriculum learns the class-box format before adding content targets with content-aware resampling. On the fixed validation split of the Engineering Drawing Dataset (ED dataset), Localization-First improves strict localization F1 by 0.0955 over joint training (paired image-bootstrap 95% interval: [0.0350, 0.1572]). G-Unified has the lowest NED, highest cell F1, and only nonzero exact-match score. It provides a detector-free baseline for full-page PCB drawing parsing.

---


### 116. [SHADOWBENCH: Toward Reliable Automatic Evaluation of Semantic Alignment in Autoformalization](https://arxiv.org/abs/2608.29270)

**<font color=#1a73e8>作者：</font>** Hojae Han, Jongyoon Kim, Sanghyuk Park 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoformalization translates informal mathematical theorems into code for proof assistants such as Lean. A central challenge is that current evaluation metrics can accept type-correct but misaligned statements or reject correct statements written in a different formulation. Inspired by Pass@$k$, we propose SA-Pass (*Semantic Alignment Pass*), which tests formal statements using auxiliary statements called *shadows* that characterize the intended statement. A generated statement receives full credit only when it compiles, implies each shadow (forward check), and is implied by their conjunction (backward check). We instantiate SA-Pass in ShadowBench, a Lean 4 full autoformalization benchmark of 178 postgraduate- to research-level problems spanning eight mathematical areas. Claude Code (Opus 4.8) with Numina-Lean-Agent reaches $61.8\%$ compile rate and $11.2\%$ SA-Pass. Across outputs generated by six agentic configurations, SA-Pass achieves $98.8\%$ binary agreement with expert judgments. An early version of ShadowBench served as the benchmark for Track 4 of the ICML 2026 AI4Math Challenge.

---


### 117. [Modality Fault Lines: Structural Corruptions Reveal Fragile Omni-Modal Reasoning](https://arxiv.org/abs/2608.29278)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Meixin Wu, Yu Xue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models are increasingly evaluated on clean text--vision--audio inputs, where every channel is present, synchronized, and readily interpretable. Such scores are often taken as evidence of robust cross-modal fusion, but clean evaluation cannot tell whether success depends on stable cross-modal structure or on cues sufficient only in intact inputs. To address this gap, we define a modality fault line: a boundary at which model behavior becomes unstable when a modality remains present and human-interpretable, but its internal evidence structure is perturbed. We introduce SCEval (Structure-Corruption Evaluation) a diagnostic evaluation protocol that keeps the question, answer space, and modality channels fixed while applying controlled structural corruptions to text, vision, and audio individually and jointly. Built from $273$ human-verified tri-modal examples from Social-IQ, OmniBench, and VALOR, SCEval evaluates $15$ proprietary and open-source omni-modal systems. The results show that structural corruption lowers clean accuracy, text--vision damage forms the most stable shared fault line, and multi-modal degradation is non-additive rather than a simple function of the number of corrupted modalities. Clean omni-modal accuracy therefore does not establish that a model will remain reliable when cross-modal evidence becomes structurally unreliable.

---


### 118. [Cloud and On-Premises Deployment of Uzbek Legal RAG via Targeted Retriever Fine-Tuning](https://arxiv.org/abs/2608.29284)

**<font color=#1a73e8>作者：</font>** Tatul Danielyan, Mariam Avetisyan, Hrant Davtyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying large language models for legal question answering raises challenges that general-purpose leaderboards do not capture, particularly for low-resource languages and under hard operational constraints. We report on building and operating a retrieval-augmented (RAG) legal assistant for Uzbek that must run in two regimes: a managed cloud service that maximizes answer quality within a per-token cost ceiling, and an on-premises deployment for clients whose legal data may not leave their infrastructure, restricting us to open-weight models on limited local hardware under latency constraints. Because no evaluation existed for this setting, we build two domain benchmarks: a retrieval benchmark of 178 expert-annotated legal queries with gold provision spans, and an end-to-end benchmark of 504 expert-curated question--answer pairs scored by an LLM judge whose ratings we validate against human judgments and against an independent-family judge. Applying these benchmarks under each regime, we find the open-versus-proprietary gap is small and cheaply closed by fine-tuning. Therefore, we train UTE-1, which is a state-of-the-art text embedder among open models for Uzbek. We also demonstrate that closing the performance gap via fine-tuning is both impractical due to the intensive hardware demands of long-context legal Q\&A and unnecessary, given that legal acts change frequently. We support this by reporting a negative result from a QLoRA experiment. We distill practical guidance for similar deployments, drawn from a system serving real users in production. We release our benchmarks, evaluation code and the fine-tuned embedder (UTE-1) \href{this https URL}{at this https URL} to support future work on low-resource legal NLP.

---


### 119. [3D-MRL: Nested Multimodal 3D Representations via Matryoshka Representation Learning](https://arxiv.org/abs/2608.29285)

**<font color=#1a73e8>作者：</font>** Márcus Lobo, Vitor Matias, Jeová Farias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models align point clouds with image and text embeddings, enabling zero-shot recognition, retrieval, and open-vocabulary understanding of 3D shapes. Existing multimodal 3D pre-training methods produce fixed-dimensional embeddings, requiring separate models for different computational budgets. We propose 3D Matryoshka Representation Learning (3D-MRL), a multimodal 3D pre-training framework based on Matryoshka Representation Learning. 3D-MRL learns nested 3D representations by aligning point clouds with frozen CLIP image and text embeddings while applying contrastive supervision across multiple embedding dimensions. The Matryoshka objective is applied only to the 3D encoder, allowing a single model to produce representations at different dimensionalities without retraining. Experiments on the Objaverse-LVIS, ModelNet40, and ScanNet datasets show that 3D-MRL achieves competitive performance on zero-shot and few-shot 3D recognition tasks. In addition, the learned representations support retrieval across different embedding dimensions within a single model. On Objaverse-LVIS, 3D-MRL improves Top-1 accuracy from 46.8% to 50.9%. Retrieval experiments further show that different embedding dimensions yield varying levels of semantic and geometric specificity.

---


### 120. [MMPCBench: Benchmarking Multimodal Large Language Models on Proactive Critique of Flawed Inputs](https://arxiv.org/abs/2608.29286)

**<font color=#1a73e8>作者：</font>** Jinzhe Li, Gengxu Li, Jinnan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Multimodal Large Language Models (MLLMs) evolve into sophisticated interactive assistants, their reliability depends not only on following instructions but also on validating them. We define Proactive Critique as the model's autonomous ability to identify, analyze and fix faulty user inputs without extra prompts. However, evaluations mainly test models under ideal circumstances or simple refusal behaviors, largely ignoring active error processing. To fill this gap, we propose MMPCBench, a comprehensive framework for evaluating MLLMs' proactive critique competence. It features a fine-grained taxonomy of 4 primary error types spanning 12 subcategories, ranging from cross-modal contradictions to missing visual premises. We adopt a hierarchical evaluation protocol to measure models' error detection, diagnosis and resolution performance, and apply alignment-aware metrics to assess the coherence between internal reasoning and final responses. Tests on 14 mainstream MLLMs show obvious weaknesses in proactive critique, especially in dealing with subtle visual anomalies. Notably, we identify a pervasive "consistency gap": reasoning models can often correctly identify and analyze errors during internal reasoning yet suppress these valid insights in final outputs to prioritize response compliance. The code and data is available at this https URL.

---


### 121. [Measuring the "Interaction Gap" in Drama Therapy with AI](https://arxiv.org/abs/2608.29292)

**<font color=#1a73e8>作者：</font>** Sora Kang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is increasingly being introduced into expressive arts therapy, where it is often credited with offering a non-judgmental environment that supports psychological safety. Existing HCI work has largely positioned AI as a co-creative material or as a bridge/mediator into human-led care. This paper explores a different position. When a patient performs the same drama therapy task with an AI partner and with a human partner, the resulting self-presentations tend to differ in patterned ways. We propose treating this difference, the Interaction Gap, as a diagnostic lens within drama therapy. Rather than asking which context elicits a truer self, the lens reads the difference between the two performances as information about the social pressures shaping self-expression in each context. We sketch a starting point for task design and measurement signals grounded in drama therapy's existing use of role and aesthetic distance, and raise provocations for workshop discussion: the observer effect and privacy paradox that measurement introduces, and the question of whose lens the gap is.

---


### 122. [When Do Larger Batches Help Scale LLM Reinforcement Learning?](https://arxiv.org/abs/2608.29296)

**<font color=#1a73e8>作者：</font>** Ziniu Li, Jinbo Wang, Guanhua Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Larger batches reduce the variance of stochastic gradients per update and are therefore often expected to accelerate training. Yet whether this statistical benefit translates into lower wall-clock time-to-target remains unclear, because each update consumes more samples and may take longer to execute. We study this tradeoff in reinforcement learning for large language models. We separate its algorithmic and systems effects by comparing learning and execution along their natural axes. At the algorithmic level, we compare configurations at equal cumulative sample counts while retuning batch-dependent hyperparameters. Over a bounded range of batch sizes, this procedure yields an approximately batch-size-invariant family whose members follow similar sample-indexed learning trajectories. At the systems level, we exploit the computational asymmetry between rollout generation and training: autoregressive generation is often memory-bandwidth-bound at low concurrency, whereas training work scales approximately with the number of processed tokens. Combining these two views yields a direct decision rule: a larger-batch configuration reduces time-to-target only when its throughput gain exceeds its samples-to-target penalty. Experiments with GRPO and PPO support both sides of this decomposition. At the algorithmic level, square-root learning-rate scaling with Adam produces approximately batch-size-invariant learning curves over a bounded range of batch sizes. At the systems level, larger batches improve generation throughput by up to 2.29x on fixed hardware. In GRPO, combining higher throughput with learning-rate retuning reduces time-to-target by up to 29%, whereas increasing the batch without retuning is slower despite its higher throughput.

---


### 123. [Learning Simple Test-Time Environments for LLM Web Agents](https://arxiv.org/abs/2608.29305)

**<font color=#1a73e8>作者：</font>** Junxuan Li, Zijun Liu, Ziyi Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have demonstrated remarkable proficiency in manually constructed environments, yet their performance frequently collapses when transitioned to complex real-world settings. Existing research largely attribute this degradation to the compositional generalization gaps in LLMs on combinations of multiple simple, well-structured environments. In this work, we propose that LLM web agents can learn simple environment observations at test time. Specifically, we introduce trial steps for agents to decompose a complex environment observation into sub-modules, and implement a label-free learning method, Test-Time Environment Decomposition (TTED), to adapt agent behaviors with experience during inference. Our empirical evaluations demonstrate the framework's efficacy across both synthetic and realistic benchmarks, showing (1) experience gains acquired within simpler sub-environments can be effectively composed to improve performance in the full one, and (2) test-time training on sub-environments can significantly enhance the compositional generalization of agents in real-world web automation tasks. We also provide key insights in the design of the label-free learning algorithm. As more complex environments are accessed by LLM agents, we believe learning environment decomposition skills at test time will be critical for robust real-world deployment.

---


### 124. [Detecting and Repairing Hallucinations in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.29307)

**<font color=#1a73e8>作者：</font>** Sai Krishna Reddy Mulakkayala, Niki van Stein, Aske Plaat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models increasingly answer questions by consulting retrieved documents rather than memory alone, a design now common in search assistants and enterprise knowledge tools. Grounding a model in retrieved text reduces unsupported statements but does not eliminate them, and a reader cannot tell a grounded sentence from an invented one. Most research on this problem stops at detection, yet flagging a faulty answer changes nothing for the person reading it, and little is known about which action should follow. Using RAGTruth, a benchmark whose unsupported passages are annotated by hand, we split each flagged answer into individual factual claims, check each against the retrieved source, and compare leaving the answer untouched with three repair strategies of increasing richness: deleting an unsupported claim, replacing it with source text, and rewriting it. Three language models from different families judge the 916 repaired answers. Every strategy reduces the proportion of answers judged to contain unsupported content, and all three judges agree on the ordering. Deletion achieves the largest reduction while retaining least of the original answer, at 64.3% of the text, whereas rewriting retains 80.1% and reduces least. Repair is not confined to faulty answers: 83.5% of answers annotated clean are edited too. The strategies occupy different points on a grounding preservation trade-off rather than forming a quality ranking, and choosing between them needs evidence about answer usefulness that automatic metrics cannot supply.

---


### 125. [Hyper3-CLIP: Hierarchy-Conditioned Hyperbolic Vision-Language Training](https://arxiv.org/abs/2608.29313)

**<font color=#1a73e8>作者：</font>** Matin Mahmood, Antonio Rueda-Toicen, Mohamed ElBassat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-like vision-language models (VLMs) trained with contrastive objectives learn strong global image-text representations, but their Euclidean embeddings and global pooling fail to encode relational structure such as part-whole and parent-child relations. Hyperbolic VLMs address this gap with entailment-based objectives, and text-conditioned variants improve fine-grained alignment through sentence- and phrase-level queries. However, these two lines of work remain separate: hyperbolic VLMs use static image and region features, while query-conditioned methods lack hierarchical geometric structure. We present Hyper3-CLIP, a hierarchy-conditioned hyperbolic VLM that combines global, local, and global-local contrastive learning with query-conditioned visual pooling. To train the model, we construct lightweight query hierarchies from text, comprising full captions, sentence fragments, localized part descriptions, and extracted phrases. Each query conditions the pooling of visual patches, and the resulting representations support image-text, whole-part, and parent-child entailment losses. Query-conditioned pooling is active only during training. Hyper3-CLIP improves R@5 and R@10 retrieval on COCO and Flickr, as well as multi-label classification on VOC and COCO, while remaining competitive on hierarchy metrics. We also audit zero-shot prompt sensitivity under fixed prompt regimes and study the effect of the localized GRIT part budget used during training. Code is available at this https URL.

---


### 126. [Test-Time Scaling for Video Diffusion Models via Diagnosis-Guided Candidate Recycling](https://arxiv.org/abs/2608.29322)

**<font color=#1a73e8>作者：</font>** Hangzhou He, Lunhao Duan, Shanshan Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video diffusion models have achieved remarkable generation quality, but high-fidelity results still largely depend on closed-source systems or costly large-scale infrastructure. Test-time scaling (TTS) offers a training-free way to improve lightweight generators by spending additional inference compute, yet existing methods mostly remain within a noise-search paradigm: they sample, select, or perturb denoising trajectories and discard low-scoring candidates after expensive generation. This generate-and-discard process wastes not only computation but also the partial motion, layout, or appearance structure already encoded in recoverable samples. We present \textbf{GEARS} (\textbf{G}uided \textbf{E}diting for \textbf{A}daptive \textbf{R}ecycling \textbf{S}earch), a training-free framework that introduces {diagnosis-guided candidate recycling} into video TTS by turning such candidates into editable priors through a generation-evaluation-editing loop. GEARS consists of two collaborative components. The \textbf{Stage-Aware Scheduler} determines what to repair, when to repair it, and which candidates should be preserved, recycled, or discarded. The \textbf{Candidate Recycler} diagnoses recoverable failures from keyframes and multi-dimensional reward feedback, derives candidate-specific repair prompts, and repairs the corresponding candidates through manifold-aware latent SDEdit. The repaired candidates are recycled into the search pool, creating refinement paths beyond standard noise perturbation while preserving useful structure. Under matched NFE budgets, GEARS consistently outperforms existing video TTS methods on VBench, bringing a 1.3B model to a total score comparable to a 14B counterpart, and ablations verify the necessity of adaptive scheduling, diagnosis-conditioned editing, and manifold-aware re-denoising. Code is available on GitHub.

---


### 127. [StageWell: A Process-Aligned Chinese Corpus for Positive-Psychology Support Dialogue](https://arxiv.org/abs/2608.29326)

**<font color=#1a73e8>作者：</font>** Yuxiong Wang, Ziwei Lin, Bo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Positive psychology dialogue aims to support emotional distress and positive resource building, requiring models to produce not only empathetic replies but also coherent progression through a multi-turn support process. Existing resources often reduce supervision to turn-level strategies or holistic preference labels, leaving process position, support function, and local repair targets implicit. We introduce StageWell, a process-aligned Chinese corpus for positive psychology dialogue, together with HQS, a structured protocol for data construction and evaluation. StageWell organizes support into a six-stage support process and uses a multi-agent whole-dialogue rewriting workflow to construct 12,445 SFT instances, 1,849 DPO preference pairs, and a GroundTruth subset of 120 expert-revised dialogues and 977 QA pairs. Guided by HQS, DPO pairs are built as process-localized repairs: flawed model outputs are used as rejected responses, and targeted rewrites under the same context and stage constraint are used as chosen responses. Across four 9B-14B open-source LLMs, this supervision yields robust gains in process control, response quality, and safety. Averaged across models, BERTScore improves by 0.037, Q-Overall increases by 1.32 points, S-exact increases by 0.236, and the H-critical rate decreases by 0.167. These results highlight the value of modeling supportive dialogue as a structured multi-turn support process rather than as single-turn response generation.

---


### 128. [When to Adapt: Conditional Memory Adapters for Retention-Preserving Domain Specialization](https://arxiv.org/abs/2608.29327)

**<font color=#1a73e8>作者：</font>** Jiayu Hou, Lei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models deployed in specialized domains must improve in-domain performance without sacrificing general capabilities. Existing parameter-efficient fine-tuning methods are typically always on: their learned perturbations are applied to every input, which can degrade out-of-domain (OOD) performance. We propose Engram Adapter, a framework that repurposes pretraining-time conditional memory as a post-hoc adapter for frozen LLMs. It uses multi-channel matching over local n-gram patterns with explicit occupancy tracking as a lightweight selectivity prior, making residual injection more likely on in-domain inputs while a learned scalar gate suppresses incoherent OOD retrievals. We evaluate on Qwen3-4B and Qwen3-8B with AG-News and MedMCQA as adaptation tasks and OOD benchmarks spanning reasoning, translation, code generation, and legal reasoning. Engram Adapter improves in-domain accuracy while preserving 99.4%--100.1% of average OOD performance; on LegalBench it slightly exceeds the frozen base model on average, whereas comparable always-on baselines degrade sharply. Mechanistic analyses show that although OOD activations are non-zero, gate and projection attenuation reduce residuals to approximately 0.08% of hidden-state norm, yielding small KL drift and negligible accuracy change. These results suggest conditional activation is a promising route toward modular, retention-preserving domain specialization over frozen backbones.

---


### 129. [FISICA: A Deployed Service for Plantar-Pressure and Posture Assessment with Ontology-Grounded Recommendation](https://arxiv.org/abs/2608.29336)

**<font color=#1a73e8>作者：</font>** Juhwan Song, Heejung Kim, Juntae Noh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FISICA is a body-assessment and recommendation service running in production. One standing session with two photographs returns foot-loading measures, posture coordinates, a driven 3D avatar, a visual report, and ranked shoe and exercise candidates. Measurement comes from a purpose-built scale carrying 634 force-sensitive elements on a 1 cm grid and four load cells, and a rule-based evaluator controls every recommendation while a language model only explains the stored result. The method contribution is the avatar. Instead of mapping a measured angle onto a rig through a tuned gain, we measure the avatar with the same function used on the subject and solve until the two agree, on a sampling-invariant spinal metric that separated a normal from a kyphotic record by 7.2 degrees against 0.9 degrees for a single-joint formulation. In production, general APIs respond at a 0.023 s median, plantar-pressure analysis at 0.45 s, and recommendation at 2.16 s to 2.26 s with the rule-based portion under one second in every trial. The served keypoint graph reaches 0.960 PCK@0.2 on public data, and the catalog holds 699 shoes with 10,500 typed facts. An approved study supplies the radiographic reference for the validation still ahead.

---


### 130. [BIRD-History: A Benchmark for History-Driven Text-to-SQL with Fine-Grained Knowledge Annotations](https://arxiv.org/abs/2608.29345)

**<font color=#1a73e8>作者：</font>** Yunfan Zhou, Qiming Shi, Yizhou Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While recent Large Language Model (LLM)-based text-to-SQL systems achieve impressive performance on standard benchmarks, they struggle when user queries implicitly rely on domain-specific knowledge, such as business logic, data conventions, and analytical practices, that is neither captured by the schema nor explicitly stated in the natural language question. Historical SQL query logs offer a valuable source of such knowledge, yet existing benchmarks do not adequately support evaluation of history-driven approaches. To address this gap, we introduce BIRD-History, a benchmark consisting of 1,393 tasks across 11 databases, designed to evaluate text-to-SQL systems' ability to ground underspecified natural language questions using historical SQL scripts. Each task is annotated with ground-truth labels specifying which historical queries contain relevant knowledge and which SQL clauses encode it, enabling systematic evaluation of both retrieval effectiveness and knowledge utilization. Alongside the benchmark, we propose a plug-in retriever that extracts five types of external knowledge from historical SQL scripts, then retrieves and reranks relevant fragments for query generation. The retriever integrates seamlessly into existing few-shot text-to-SQL pipelines without requiring prompt modifications. Experiments demonstrate consistent improvements across four text-to-SQL systems, highlighting the value of leveraging historical query logs for handling underspecified queries. Dataset and code are open-sourced on this https URL.

---


### 131. [Cross-Relational Preference Learning for Better LLM Instruction Following](https://arxiv.org/abs/2608.29352)

**<font color=#1a73e8>作者：</font>** Runsheng Li, Kai Sun, Bin Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) still exhibit limited capability in following complex instructions. While existing approaches often rely on preference learning to enhance this ability, they typically overlook the relationships between the permissible response spaces of different instructions, which restricts a model to align with subtle and diverse constraint variations. To address this, we propose Cross-Relational Preference Learning (CRPL), a novel framework for constructing preference data that explicitly models inter-instruction relationships through two key techniques: Cross-Relationship Perturbation and Cross-Region Pair Sampling. This enables the generation of more diverse preference data that captures a wide spectrum of constraint variations. Additionally, we introduce an atomic constraint-based verification mechanism to rigorously assess response satisfaction, ensuring high-quality preference pair construction. Extensive experiments across multiple preference learning methods (e.g., DPO, KTO), LLM backbones and four instruction-following benchmarks demonstrate that our approach achieves substantial improvements over prior baselines and exhibits strong generalization.

---


### 132. [LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO](https://arxiv.org/abs/2608.29357)

**<font color=#1a73e8>作者：</font>** Saeed Khaki, Nima Safaei, Kamal Ginotra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal search agents answer visual questions by interleaving image understanding, web retrieval, tool use, and evidence synthesis. Strong systems exist, but in two expensive regimes: proprietary frontier models such as GPT-5 and Gemini, or large open vision-language backbones trained with substantial agentic data and reinforcement learning. We ask a different question: when released agent trajectories are distilled into much smaller backbones under a single-node budget, what is actually transferred? We study this with LiteSearch-VL, a low-compute recipe for Qwen3-VL-2B and Qwen3-VL-4B that uses only released OpenSearch-VL trajectories, parameter-efficient LoRA adapters, and synthetic step-level preferences: DPO on GPT-5-generated hard negatives targeting five local failure modes (premature answer, wrong tool, weak query, repeated query, ignored image). Across 12,400 GPT-5-judged rollouts on SimpleVQA, FVQA, LiveVQA, and VDR-Bench-testmini, the dominant effect is behavioral rather than a uniform accuracy lift: full-trajectory supervised fine-tuning transfers the agent contract, taking the 2B model from almost never emitting a usable answer (1,237/1,240 no_answer rollouts) to 28.4% macro Pass@1, matching or slightly exceeding the off-the-shelf 4B base (25.6%). Synthetic preference learning and compact tool distillation act as refinements rather than phase transitions (best 4B configuration: 30.8% macro Pass@1). Finally, a controlled VDR step-budget ablation shows that extra search turns convert abstentions into wrong_entity errors rather than correct answers, identifying answer verification, not search depth, as the next bottleneck for small multimodal agents.

---


### 133. [TRACER: Per-Tool Context Retention for LLM Agents via Consequence-Attributed Reinforcement Learning](https://arxiv.org/abs/2608.29363)

**<font color=#1a73e8>作者：</font>** Ziqi Lin, Ye Wu, Mengying Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise data agents answer business queries by chaining many tool calls over multiple reasoning steps, routinely accumulating hundreds of thousands of context tokens per session. Existing compression strategies typically allocate retention budgets without accounting for the downstream consequences of removing individual tool outputs. Aggressive compression may therefore trigger costly tool re-invocations that offset the initial savings. We call this the compression--consequence gap. To close it, we propose TRACER, which formulates compression as a sequential per-tool decision problem. A lightweight REINFORCE policy assigns query-conditioned retention ratios using only information available at each compression event. Its consequence-aware objective jointly accounts for task success, total token consumption, and post-compression tool re-invocations. To improve credit assignment, TRACER uses a learned outcome model to compare the predicted consequences of the selected retention ratio with those of fully retaining each tool output. On held-out production queries across three compressor backends, TRACER reduces total token consumption by 29--46% relative to keeping all context while maintaining comparable or higher task success. Compared with a tool-type-conditional static policy, TRACER provides an additional 15--18% of token savings. Interventional rollouts show that the learned per-tool credit scores correlate with measured single-tool consequences. The learned policy also yields positive savings when transferred across agent backbones and compressor architectures, and reduces token consumption by 18--25% on five held-out LOCA-bench environments. These results demonstrate the value of consequence-aware, per-tool context retention for improving the efficiency of long-horizon language agents.

---


### 134. [Think, Look, and Revise: Inconsistency-Aware Visual Self-Correction in MLLMs](https://arxiv.org/abs/2608.29374)

**<font color=#1a73e8>作者：</font>** Yu Cheng, Arushi Goel, Hakan Bilen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-augmented multimodal reasoning integrates external tools (e.g., object detection, depth estimation) into multimodal large language models (MLLMs) to address perceptual bottlenecks in complex visual tasks. However, existing approaches rarely verify tool outputs, limiting their ability to detect and recover from tool failures. We propose ReVISE, a framework that equips MLLMs with verification and dynamic error recovery for tool-augmented reasoning. ReVISE introduces (1) a curated training dataset that supervises reflective behaviors, enabling models to validate tool-derived evidence, reformulate queries when visual mismatches arise, and fall back to intrinsic grounding when external tools are unreliable; and (2) a reinforcement learning based targeted rewards that encourage internal reflection and penalize spatial misalignment. Experiments on several benchmarks demonstrate consistent improvements over existing methods, highlighting the importance of error detection and correction in tool-augmented multimodal reasoning.

---


### 135. [EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants](https://arxiv.org/abs/2608.29387)

**<font color=#1a73e8>作者：</font>** Yue Peng, Lanke Xia, Zihan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can generate interactive web interfaces, but reliable generative UI requires maintaining an executable artifact as user requests evolve. We introduce EvoGenUI-Bench, a benchmark for multi-turn interface maintenance comprising 150 five-turn tasks and 750 turns across three scenarios: information presentation, executable interaction, and tool-grounded external state. We execute generated artifacts in a browser and evaluate them using screenshots, source and DOM evidence, actor traces, and runtime logs. Beyond turn-level and episode-level success, we measure cross-turn retention with Adjacent Pass Retention. Across eight models, even the strongest achieves 74.9% Turn Pass while completing only 37.3% of five-turn episodes; APR further falls to 52.4% on tool-grounded tasks. Diagnostic analysis shows that presentation failures center on information architecture, interaction failures on derived-state propagation and affordance binding, and tool-grounded failures additionally involve external-state grounding and requirement decomposition. These results reframe generative UI evaluation from judging isolated outputs to testing whether interface behavior, derived state, external state, and assistant claims remain synchronized as the artifact evolves.

---


### 136. [GATE: Reliability-Gated Gaussian Evidence Fusion for Training-Free Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2608.29395)

**<font color=#1a73e8>作者：</font>** Pedram MohajerAnsari, Amir Salarpour, Run Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP and SigLIP provide strong zero-shot recognition, but their predictions can degrade when deployed on target data that differ from the pretraining distribution. Test-time adaptation offers a practical way to improve robustness without source data or target labels, yet existing methods often rely on either prompt-side adaptation or image-side target evidence alone. In this work, we introduce GATE, a training-free two-pass transductive test-time adaptation framework that uses the unlabeled target set while keeping the image encoder, text encoder, and prompt parameters fully frozen. Instead of representing each class with a single prototype, GATE builds two complementary Gaussian sources of evidence in the shared vision-language feature space: a text Gaussian estimated from multiple language descriptions and an image Gaussian estimated from reliable unlabeled target samples. A class-wise reliability gate controls the influence of image-derived pseudo-evidence, and a score-level generalized Product-of-Experts fusion produces a normalized residual correction to the original zero-shot logits. Across fine-grained recognition datasets, ImageNet-family distribution shifts, multiple CLIP backbones, and SigLIP-B/16, GATE achieves the best average accuracy in every benchmark/backbone group. It improves zero-shot performance by an average of 5.41 points and outperforms the strongest non-GATE baseline by 1.94 points, demonstrating the benefit of reliability-gated distributional evidence for frozen VLM adaptation.

---


### 137. [AlgoWorlds: Benchmarking Tool Use for Global Optimization in Algorithmic Worlds](https://arxiv.org/abs/2608.29397)

**<font color=#1a73e8>作者：</font>** Zixiang Xu, Jiaan Wang, Fandong Meng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-use benchmarks generally evaluate whether an agent completes a workflow using appropriate tools and valid arguments. However, feasibility alone is insufficient in real-world decision settings such as route planning and fleet dispatch. Individual choices interact through shared constraints and costs, so a feasible solution may still be substantially suboptimal. This raises a harder question: can an agent turn information gathered through tools into a globally optimal decision? We introduce AlgoWorlds, a benchmark that transforms formally specified combinatorial optimization problems into partially observed decision environments with verifiable global optima. Each environment contains a hidden instance observed only through task-specific information tools, after which the agent commits to one structured decision evaluated for feasibility and optimality. AlgoWorlds contains 240 environments covering ten combinatorial optimization families and four workload levels. Family-specific deterministic programs generate the instances, exact algorithms certify their optima and determine workload levels, and two structurally different tool interfaces present each underlying instance. We evaluate seven leading LLMs, including Claude Opus 4.8 and GPT-5.6 Sol. Achieving global optimality remains highly challenging: although leading models produce feasible decisions in most cases, the best-performing model reaches exact optimality in only 38.61% of cases. Even when agents collect sufficient information to reconstruct the hidden instance, most failures end in feasible but suboptimal decisions. The challenge therefore extends beyond information acquisition to information integration, global constraint reasoning, and decision verification. The project homepage is available at this https URL, and the code is available at this https URL.

---


### 138. [A Visual Question Answering Model to Automate Nondestructive Evaluation Image Analysis](https://arxiv.org/abs/2608.29408)

**<font color=#1a73e8>作者：</font>** Mehrdad Shafiei Dizaji, Hoda Azari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces a Visual Question Answering model designed specifically for nondestructive evaluation applications. VQA models allow inspectors to interactively query NDE images, asking targeted questions like, Is there a crack or Where is the defect located and receive precise answers from the model. Leveraging deep learning and natural language processing, the developed system integrates image feature extraction (via a ResNet-50 model) and language generation capabilities (via GPT-2) to provide accurate, informative feedback. By enabling direct question-and-answer interactions, this VQA model significantly improves inspection efficiency, reduces potential errors, and enhances usability in practical field scenarios.

---


### 139. [Where Induction Runs Out: Description-Length Difficulty and the Memorisation Gap in Integer-Sequence Benchmarks](https://arxiv.org/abs/2608.29411)

**<font color=#1a73e8>作者：</font>** Sabilashan Ganeshan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integer sequences from the On-Line Encyclopedia of Integer Sequences (OEIS) are increasingly used to benchmark mathematical reasoning in language models. We ask what such benchmarks actually measure, using an exactly computable reference learner: two-part minimum description length (MDL) over the class of P-recursive (holonomic) recurrences, evaluated on every prefix of a sequence as terms arrive. Three findings follow. First, MDL difficulty is a parameter count. The discovery point nd, the first prefix length at which a symbolic hypothesis beats verbatim storage, is predicted almost exactly by a combinatorial identifiability bound on the selected operator's order and degree. It is invariant to term magnitude: scaling Fibonacci over twelve orders of magnitude leaves nd unchanged, because a hypothesis must encode its own initial conditions and the magnitude cancels. Second, at scale the learner exhibits a regime our curated corpus could not produce even once: across 20,000 OEIS sequences, 89.98% of those that fit a recurrence on some prefix fit none at full length. We call this the wilderness -- induction acquires a theory, loses it, and never recovers. Third, evaluating three language models on sequences stratified by these MDL regimes refuted our pre-registered hypothesis: models do not confabulate where MDL reports no theory, but hedge appropriately. Confident errors are inverted, concentrating on the easy stratum, where apparent competence tracks recognition of the sequence rather than induction of its rule. OEIS-derived benchmarks therefore substantially measure memorisation, and MDL supplies a cheap, contamination-free difficulty signal they currently lack. Code and data are released.

---


### 140. [Evaluating the Semantic Specificity of Representation Steering in Language Models](https://arxiv.org/abs/2608.29431)

**<font color=#1a73e8>作者：</font>** Zhangdie Yuan, Andreas Vlachos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Localized Representation Steering (LRS) is widely used to correct reasoning pathologies in large language models. However, standard benchmark evaluations can easily be fooled by superficial label overrides, creating a false impression of reasoning circuit repairs. In this work, we propose Cross-Rule Transfer (CRT), a diagnostic framework that audits representational interventions by evaluating them on rule families where the model is natively competent. Evaluating late-layer LRS for a widespread logical failure, contradiction blindness, reveals that the intervention merely injects a global label bias: applying the steering vector to rules the model already handles correctly (99.6% baseline) degrades performance to 40.4% by forcing false contradiction predictions. We support this diagnosis with four complementary controls (direct logit bias equivalence, control vector label-flipping, cross-model grafting, and early-layer steering checks), providing a rigorous methodology to distinguish genuine reasoning repairs from superficial label overrides.

---


### 141. [Whose Assessment of Distress? Community Perspectives and LLM Alignment on Well-Being Posts](https://arxiv.org/abs/2608.29446)

**<font color=#1a73e8>作者：</font>** Andrew Aquilina, Xiang Lorraine Li, Yu-Ru Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Judgments about psychological distress are socially situated: what counts as concerning hinges on community norms around emotional expression, vulnerability, and help-seeking. Yet large language models (LLMs) used for distress detection are typically aligned to a single, undifferentiated standard. How well do these models capture the perspectives of the communities whose language they assess? We address this question through a perspectivist annotation study in which 321 participants provided 9,587 judgments on 1,198 Reddit posts spanning six identity-based communities, yielding community-specific labels. Raters in the contextualized in-group condition show a modest tendency to agree more with their community than uncontextualized out-group raters (OR = 1.18), an effect varying significantly across communities. We then evaluate nine open-weight LLM configurations and four frontier configurations against these labels. Open-weight LLMs systematically over-estimate distress: when communities perceive none-to-mild distress, these models achieve only 31-44% accuracy, predominantly producing false positives. GPT-5 and Gemini 2.5 Pro show the same none-to-mild inflation even when their full-sample over/under rates are mixed, while Claude Opus 4 is more conservative. This pattern does not simply mirror an outsider reading position: uncontextualized out-group human aggregates were nearly symmetric, with 18% over-estimation versus 19% under-estimation. Instead, the models that inflate none-to-mild cases exhibit a distress prior that exceeds both contextualized in-group and uncontextualized out-group human judgments. These findings have implications for equitable AI deployment in mental health contexts, where miscalibrated distress detection may unevenly affect the communities being assessed.

---


### 142. [Item-Mean Surrogates: Why Richer Persona Data Fail to Improve LLMs as Human Surrogates](https://arxiv.org/abs/2608.29455)

**<font color=#1a73e8>作者：</font>** Daehwan Ahn, Chengfeng Mao, Dokyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used as human surrogates, often on the premise that richer persona data could make them substitutes or exploratory tools for specific individuals. We test this premise across four datasets covering more than 400,000 participants and more than 6,000 survey items and experimental outcomes. LLMs perform well at the aggregate level: their average responses closely align with average human responses to the same items. But this success largely reflects predicting each item's average human response. Once each item's human mean is removed, LLM predictions explain only 3.05% of the remaining respondent-specific variation, far below the 53.6% human test-retest benchmark. Richer personas, model variants, and fine-tuning do not close this gap. In variance analyses, once item means are removed, the reliable remaining signal is person-by-item. It captures how a respondent departs from the mean on a particular item and is about 8.9x larger than the stable person effect. Persona data encode the respondent, but not this item-specific deviation. LLM responses also compress human response distributions, using less spread, fewer response categories, and distorted distributional shapes. We call this pattern item-mean surrogacy. Current LLM surrogates can approximate item averages, but not the distributions or respondent-specific deviations needed to replace individual humans. We propose four empirical tests for LLM-based human-surrogate claims.

---


### 143. [Toward Latent Language Model Skills Steering and Optimization: An Empirical Study](https://arxiv.org/abs/2608.29459)

**<font color=#1a73e8>作者：</font>** Xunyi Jiang, Junda Wu, Yuxin Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills, as a useful abstraction for the procedural capabilities of large language models (LLMs), capture how models perform structured, multi-step reasoning and program execution. Existing approaches typically treat skills as explicit, surface-level constructs specified through prompts or programs, leaving open the question of how such procedural capabilities are represented inside the model and whether they can be manipulated as structured objects in latent space. In this empirical study, we investigate whether procedural LLM skills can be represented as directions in activation space and whether vector-space operations over these directions can express skill-level behaviors. We find that procedural skills admit a vector-space representation: individual skill directions can be activated to shift model behavior; independently extracted directions can compose to form higher-level skills. Contrastive directions yield context-conditioned algorithmic personalization and optimization trajectories over skill directions evolve non-monotonically, with intermediate states often surpassing fully optimized solutions. These results support a representation-level view of procedural LLM skills: they admit a latent vector-space organization that allows direct manipulation through internal interventions.

---


### 144. [Can escalation channels redirect reward hacking toward defect disclosure?](https://arxiv.org/abs/2608.29460)

**<font color=#1a73e8>作者：</font>** Francesca Gomez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When coding agents encounter defective test infrastructure they may reward-hack: hardcoding outputs or editing test files to pass tests they cannot legitimately satisfy, a pattern that has now appeared outside benchmarks, in a coordinated multi-agent intrusion of a major AI platform's production infrastructure. The same capability that lets an agent detect and exploit a defect could let it report one, given the right decision environment. We evaluate escalation channels, structured reporting tools available to the agent at the point of conflict, as a decision-environment intervention that both reduces reward hacking and surfaces the infrastructure defects that trigger it. A $2 \times 2$ factorial separates the contributions of an escalation tool, a standalone anti-reward-hacking policy, and their combination. Across 8 frontier models spanning 5 families, the combined intervention reduces reward hacking from 23.6\% to 5.3\% (mixed-effects logistic OR = 9.2, 95\% CI 5.0--16.8, $p < 10^{-12}$) with no detectable cost or performance overhead, eliminating it entirely for 6 of 8 models. Escalation and hacking are near-perfectly mutually exclusive, with 96.8\% of escalations involving no hacking. Beyond reduction, escalation channels function as diagnostic infrastructure: on top of monitoring, escalation adds +10.1 percentage points of defect detection coverage and is more accurate once it fires (99.4\% vs 85.8\%). Unlike containment-based approaches that risk outpacing growing model capabilities, escalation channels redirect capability toward disclosure rather than exploitation.

---


### 145. [A Causal Model for Locating and Unlocking Sandbagging in Model Organisms](https://arxiv.org/abs/2608.29461)

**<font color=#1a73e8>作者：</font>** Hong Kiat Tan, Linh Le, David Williams-King  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sandbagging models strategically underperform on evaluations while retaining the capabilities being measured. The evaluations that guide frontier-model deployment and governance then understate what these models can do. To understand the mechanism, we propose a causal model of how sandbagging is carried in the residual stream. Early layers write the sandbagging intent onto a single axis of the stream, and a later layer reads that axis and commits the answer. We study three instruction-tuned models (Qwen2.5-7B, Llama-3-8B, and Mistral-7B) and four ways of installing a sandbagging lock (prompting, fine-tuning, reinforcement learning, and circuit breaking). Each lock decides from the prompt whether to sandbag, and the fine-tuned and circuit-broken locks answer honestly whenever a password appears. The causal model predicts a window of layers, after the last sandbagging write and before the answer commit, in which a single-layer reference graft of the sandbagging axis to its honest value restores the full capability. The single-layer graft recovers the capability in 28 of the 33 runs of the prompted, fine-tuned, and RL-trained locks, with a median held-out recovery of 96%. The circuit-broken lock rewrites the whole state through a band of layers, and the single-layer graft fails at every layer. We therefore introduce a second intervention, context grafting, which replays the password's cached key/value activations so that every layer's attention reads them as additional context. Context grafting provably and empirically restores the full capability on all three models, and the recovery is surprisingly insensitive to the exact password content. More broadly, an auditor can use this causal model to design interventional auditing techniques for sandbagging models.

---


### 146. [Benchmark Contamination: A Taxonomy Organized by Defeated Mitigation](https://arxiv.org/abs/2608.29463)

**<font color=#1a73e8>作者：</font>** Johanna Angulo, Víctor Yeste, Hector Espinos-Morato  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A benchmark score is a joint property of the model, the evaluation harness, the elicitation budget, the sampled population, and contamination status. Leaderboards publish the model and the score, so capability and leakage stay observationally equivalent. Existing taxonomies classify contamination for automated detection, not the question a reporter faces at publication: given the mitigations already applied, which validity threats remain open? We introduce a taxonomy organized by the mitigation each type defeats -- direct, derivative, temporal, distributional, and acquired -- spanning training-time and evaluation-time leakage. Holding out a private test set closes the first alone. The fifth is acquired during the evaluation itself; because it is a property of one run, it must be recorded with the reported score rather than with the benchmark release. We operationalize it as a four-field disclosure protocol in which "unknown" is a valid entry, released under CC BY 4.0 with a JSON Schema, a validator, and worked examples. Two coders external to the design team applied a pre-registered instrument to 41 documents. Per-variable linear-weighted $\kappa$ runs from 0.00 to 0.35 (median 0.21) over 29 main-pass documents against a single-coder test-retest ceiling of 0.84, collapsing under the class skew the registration anticipated; pooling raises it to 0.46 through chance correction rather than better agreement. Two variables fall below the prevalence-robust threshold registered in advance: strata reporting and the acquired type introduced here. Disagreement concentrates on when a variable applies rather than on what a document states. Elicitation budgets are reported in 13% of documents, and no document addresses all five types. The contribution is the taxonomy, the score-side artifact that follows from it, and a pre-registered measurement of instrument reliability and current disclosure.

---


### 147. [Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered](https://arxiv.org/abs/2608.29464)

**<font color=#1a73e8>作者：</font>** Aryo Pradipta Gema, Neel Rajani, Rohit Saxena 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring assumes that reasoning traces faithfully record the information that shapes a model's answer. Existing faithfulness tests often place explicit bias cues in the user message, while agents may encounter preferences through tool returns or raw artifacts. We introduce FACE-Eval (Faithful Attribution of Cue Effects Evaluation), a 5,100-sample evaluation that varies cue location (user message or tool return) and explicitness (direct summary or raw artifact). We measure verbalized commitment among cue-following answers and unverbalized adoption among all cued samples. We evaluate 15 open-weight models from eight families, with total parameters ranging from 4B to 1.60T. Every model has lower verbalized commitment for tool-return than user-message cues and for implicit than explicit cues. Unverbalized adoption is higher for tool-return cues on all 15 models and for implicit cues in 28 of 30 model-channel comparisons. A source-attribution prompt narrows the channel gap on seven models, sometimes by increasing user-channel unverbalized adoption, while telling models that their reasoning will be monitored does not reliably close the gap. We also use two transcript monitors (GPT-5.6-Luna and GPT-4o-mini) to detect preference adoption in the largest model of each family. Across 32 model-channel-explicitness cells, higher unverbalized adoption is associated with lower detection ability for both monitors (Pearson r=-0.54 and r=-0.78, respectively). These results suggest that CoT monitoring may be less reliable when preference information arrives through tools or must be inferred from raw artifacts, within the single-call, prefilled-tool setting tested here.

---


### 148. [MUDDLE: Measuring Understanding of Documents under Distractor and Length Effects](https://arxiv.org/abs/2608.29477)

**<font color=#1a73e8>作者：</font>** Jason Luo, Saibilila Abudukelimu, Judy Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document question-answering systems increasingly answer questions over collections of retrieved documents rather than one clean source, so robustness to distracting context matters as much as reading ability. When such systems fail, it is often unclear whether the context was too long or the distractors were too close to the topic, because prior work tends to conflate these two effects. We present MUDDLE, a controlled benchmark that separates them. MUDDLE uses 270 human-annotated questions, each tied to a single source document, and instantiates every question in five conditions: the source alone, the source with two or four topically similar hard negatives, and the source with two or four random distractors. The random distractors are matched to the hard negatives in length and provenance, so an accuracy gap between the two arms reflects topical similarity rather than length. All five conditions are rendered in markdown, page images, and raw PDF, but the distractor sweep reported here is run in markdown, since a source plus its distractors exceeds current image and PDF input limits. We score answers with an LLM judge across three model families. In the complete markdown sweep, hard negatives lower accuracy more than length-matched random documents at both context sizes for gpt-5-mini, while random documents stay near the no-distractor baseline. The effect is small but directionally consistent, and for gpt-5-mini hard negatives significantly underperform length-matched random distractors when pooled across context sizes. We release the data and evaluation code for a reproducible study of context degradation.

---


### 149. [SIC-Agents: Benchmarking and Building an Adaptive Simulator for Pediatric Serious Illness Communication Training](https://arxiv.org/abs/2608.29481)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Anita Marie Slominska, Rennie Bimman 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pediatric serious illness communication (SIC) is critically important, yet scalable communication training for clinicians remains limited. Compared with other dialogue simulation settings, pediatric SIC poses additional challenges, including multi-party interactions, response to parental distress and strong dependence on feedback dynamics. Existing LLM-based simulators optimize generic dialogue quality rather than curriculum-contingent behavior required for effective SIC training. In collaboration with educators and pediatric clinicians, we introduce the first benchmark suite and simulation framework tailored to pediatric SIC training. Our benchmarks, PitfallBench and DialogueBench, evaluate simulators both at the turn-level and across full dialogues. We further propose SIC-Agents, a self-improving framework that generates a clinician-editable skill document to guide simulator behavior. Our experiments show that SIC-Agents outperforms static expert prompting. To support future research, we release our benchmarks for parent simulation in pediatric SIC at this https URL

---


### 150. [GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation](https://arxiv.org/abs/2608.29483)

**<font color=#1a73e8>作者：</font>** Arka Mukherjee, Soham Roy, Kartikeya Trivedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language Models (VLMs) perform well above the human baseline in image geolocalization, a task critically important in disaster response, OSINT verification, and location privacy. However, most efforts to study AI behavior on the task remain limited to static image-based retrieval, classification, and predictions. We argue that faithful recreation of the task should involve embodied navigation, where a multimodal agent autonomously explores its surroundings to gather observations before submitting a prediction. To this end, we introduce \textbf{GeoAgent}, an agentic environment-based benchmark that requires agents to navigate Street View environments to refine their geolocalization through sequential reasoning. Our analysis shows that modern VLMs struggle to discern regional patterns while succeeding at country- and continent-level predictions. When compared to static image-based baselines, agentic navigation significantly improves accuracy across established metrics. We also note severe bias in a developed/developing region context across frontier model architectures and poor self-improvement capabilities given incorrect priors. Overall, our work establishes the challenges of embodied navigation and geospatial reasoning. We publicly release our code and the GeoAgent environment: this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
