# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

---

### 101. [When Cosine Similarity Fails to Reflect Linearly Accessible Structure in Dialogue Models](https://arxiv.org/abs/2609.22522)

**<font color=#1a73e8>作者：</font>** Yu Sun, Mengyin Lu, Cong Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cosine similarity is widely used to analyze transformer representations, implicitly assuming that similarity reflects task-relevant structure. We study when this assumption fails in dialogue-conditioned large language models. Across three 7-8B chat-tuned models, ambient cosine similarity substantially underestimates linearly decodable persona structure on the same hidden states; numerically, linear probe AUC is in the 0.73-0.97 range while cosine kNN is in the 0.56-0.77 range on a 30-class task. A low-dimensional supervised subspace recovers much of this gap, whereas a matched-rank PCA subspace does not and in some cases degrades performance. This mismatch is regime-dependent: it is absent in single-sentence sentiment classification (SST-5), and a matched-cardinality control rules out attribute cardinality as a confound. The gap does not systematically increase across dialogue turns, and the task-aligned subspace remains stable over time. However, two of three models violate a pre-registered within-subspace separability invariance criterion (|Delta AUC| <= 0.03), and one model violates a pre-registered turn-invariance criterion (|Delta L| <= 0.05). These results show that cosine similarity can fail to reflect task-aligned structure in dialogue representations even when that structure is linearly accessible.

---


### 102. [IntLawNER: A Named Entity Recognition Dataset and Benchmark in International Law](https://arxiv.org/abs/2609.22529)

**<font color=#1a73e8>作者：</font>** Genis Skura, Roland Bouffanais, Didier Wernli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> International law provides the normative framework through which states coordinate action, regulate armed conflict, and protect human rights, yet its texts remain without token-level named entity recognition (NER) resources. We introduce IntLawNER, a NER dataset and benchmark for codified sources of international law, covering 2,987 gold-annotated sentences and 8,094 entity spans from International Court of Justice (ICJ) decisions, UN Security Council resolutions, and European Court of Human Rights (ECtHR) judgments, annotated with seven institution-specific entity types. We construct IntLawNER with a cost-effective hybrid algorithmic-agentic pipeline that reduces 468k source sentences to a compact annotation set through candidate retrieval, LLM-based vetting, and human review, with 89.6% of gold spans accepted unchanged from the silver layer. However, the silver-to-gold analysis reveals that human-machine aggregate agreement metrics can be misleading in domain-specific NER: Cohen's kappa=0.964 on boundary-matched spans masks a macro-F1 of 0.753 when missing entities, boundary errors, and label corrections are included. The benchmark shows that zero-shot span-based GLiNER collapses on entity types dependent on institutional function rather than surface form (0.243 micro-F1), while fine-tuned transformers struggle on rare labels. Carefully selected few-shot examples that demonstrate label contrasts improve every LLM over zero-shot prompting, with Claude Opus 4.6 reaching the best score of 0.873 micro-F1. We release IntLawNER as a benchmark and reusable resource for extracting references in international legal texts.

---


### 103. [EvidenT: Building Trustworthy Enterprise Assistants through Evidence Groundedness and Traceability](https://arxiv.org/abs/2609.22537)

**<font color=#1a73e8>作者：</font>** Anubha Kabra, Katie Jooyoung Kim, Colin Zhiwei Kou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI assistants must produce responses that are verifiable and traceable to source evidence. However, retrieval augmented generation (RAG) over heterogeneous enterprise data can suffer from citation drift, unsupported content, and weak source traceability. We present EvidenT (T = Trust + Transparency + Traceability), a lightweight pipeline that verifies extracted evidence against retrieved documents before answer generation, without model retraining. EvidenT combines structured passage extraction with deterministic lexical alignment to filter unsupported content, correct citation drift, and preserve source-span traceability. On approximately 500 real enterprise queries, EvidenT improves gold-source hit rate by an average of 29% over prompting baselines, produces no citations to nonretrieved urls, and achieves near-saturated answer-to-source lexical coverage.

---


### 104. [Correct Diagnosis, Better Feedback: A Symbolic-Verifier for Faithful LLM Tutoring Feedback in Logic Proofs](https://arxiv.org/abs/2609.22553)

**<font color=#1a73e8>作者：</font>** Tahreem Yasir, Arnav Mody, Xioayi Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective LLM tutoring depends on correctly identifying the specific error in a student's reasoning before generating feedback. We study this problem in propositional-logic proof tutoring, where student actions can be checked against formal inference rules. We introduce a verifier-grounded architecture that separates diagnosis from language generation. Using 600 balanced student actions, we compare a zero-shot LLM detector, a fine-tuned detector, and a symbolic verifier. Each diagnosis is processed by shared rationale and feedback agents, isolating the effect of the initial diagnosis. The zero-shot detector achieves a macro-F1 of 0.191; fine-tuning raises this to 0.709 but retains systematic errors between structurally related classes. Rationales generally preserve the diagnosis supplied to them, showing that an incorrect diagnosis can be faithfully propagated through the pipeline. Feedback can likewise remain faithful to its rationale, non-revealing, and pedagogically appropriate while addressing the wrong error. Verifier-grounded feedback achieves the highest diagnostic correctness, and expert ratings largely uneven with the automatic feedback evaluations. These findings show that apparent feedback quality can conceal upstream diagnostic errors and that faithfulness must be evaluated separately from correctness. Our code is publicly available

---


### 105. [Do Student LLMs Inherit OOD Robustness? Invariance-Weighted Distillation for Reliable Knowledge Transfer](https://arxiv.org/abs/2609.22566)

**<font color=#1a73e8>作者：</font>** Dileesha Kannangara, Sanghamitra Dutta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) aims to compress high-performance teacher LLMs into lightweight students. However, distilled students often exhibit substantial performance degradation in out-of-distribution (OOD) settings, a critical gap that remains underexplored. We identify two compounding mechanisms causing OOD performance degradation: (1) data spuriousness: students can learn spurious correlations in the distillation dataset over genuine causal relationships; and (2) teacher capability: standard KD treats all samples uniformly, ignoring whether the teacher is guided by causal features or misled by spurious shortcuts on a given sample. To address these challenges, we propose Invariance-Weighted Distillation (IWD), a theoretically grounded framework that dynamically reweights training samples using an estimate of the teacher's causal reliance derived from prediction invariance across multiple synthetic environments. IWD perturbs spurious cues while preserving core semantics, assigning higher distillation weights to samples whose teacher predictions remain invariant, indicating greater reliance on causal rather than spurious features. We theoretically show that IWD reduces the student's Spurious-to-Causal (S2C) gradient ratio compared to standard uniformly weighted KD, driving the student toward more invariant representations. Experiments on four NLP benchmarks (MNLI, SQuAD-v2, CoNLL-2003 NER, and SST-2) across two model families (DeBERTa-v3 and Qwen-2.5) demonstrate that IWD consistently outperforms strong KD baselines on OOD evaluations while maintaining competitive in-distribution (ID) performance. Specifically, IWD achieves the highest accuracy in 15 out of 16 OOD benchmarks and improves average OOD performance over standard KD by 4.34 percentage points on NLI and 14.94 percentage points on QA.

---


### 106. [Zero-Trust Authorization and Discovery for Enterprise MCP](https://arxiv.org/abs/2609.22573)

**<font color=#1a73e8>作者：</font>** Huan Li, Yuwei Wang, Srinivasan Manoharan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents translate natural-language context, which may include attacker-controlled text, into privileged tool calls, so authorization must remain effective even when an agent is prompt-injected or adversarially steered. The Model Context Protocol (MCP) has become a widely adopted interface for this boundary, yet its official SDKs' authentication and authorization primitives fall short of enterprise zero-trust requirements, most acutely a dual-persona model in which one server must serve human users (corporate SSO) and automated agents (service-account credentials on a different header). We conduct a systematic gap analysis of six surveyed MCP SDKs (Python, TypeScript, Go, Rust, C#, Swift) and identify three structural shortcomings: credential extraction bound to a single Authorization header, complicating dual-persona deployment without custom middleware; the absence of pre-authentication tool discovery; and the lack of fine-grained per-tool authorization in the base SDKs. We close these gaps with composable extensions to FastMCP: cross-header credential normalization for enterprise deployments serving both human and service-account callers, cached token verification across heterogeneous IdPs, an unauthenticated metadata endpoint for credential-free registry discovery, and permission-filtered tool visibility kept consistent with per-tool invocation enforcement by a single declarative annotation, all without modifying the protocol or SDK internals. Across four frontier LLMs over 2160 attempts, an in-body-check-only server still exposes forbidden tools (152/720, 21.1%), whereas permission-aware visibility drives the rate to 0/720; visibility-only filtering remained bypassable by scripted clients, while models referenced the hidden tool by name in up to 94% of settings when inferable from the prompt, confirming that discovery controls cannot replace invocation-time enforcement.

---


### 107. [Beyond the Leaderboard: Counterfactual Diagnosis of End-to-End and VLA Driving Policies Under Domain Shift](https://arxiv.org/abs/2609.22582)

**<font color=#1a73e8>作者：</font>** Ruolin Yang, Zilin Huang, Buoyue Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end and vision-language-action (VLA) driving policies are compared by leaderboard rank, but a rank reports an outcome, not the behaviour behind it, so it predicts poorly how a policy will behave at a new site. On six released policies, rank on nuScenes open-loop error or on NAVSIM's leaderboard does not carry over to scenes with a pedestrian near the ego corridor at a new site. We propose a counterfactual check-up: a few hundred real frames, each edited two ways (pedestrian removed, or re-lit by a night-style perturbation), every edit verified by an independent detector, and the change in the planned trajectory read as a diagnosis rather than a score. From these edits two causal axes are read, and five exams built on them separate what a score merges: how far the policy plans to drive, whether seeing the pedestrian buys safety, whether that response scales with danger, whether the plan moves when nothing requires it, and how much an irrelevant lighting change moves it. On 246 NAVSIM near-pedestrian scenes, in the cells where the pedestrian lies on the planned path only 1.9% of responses are genuine avoidance, and under our open-loop protocol the median clearance change is at most 0.03 m and the median change in planned distance at most 0.08 m for every policy. In a pre-registered test from left- to right-hand drive, the exposure and specificity orderings, the lighting verdict and the collision outcome transfer, while point values and the hazard-sensitivity verdict do not. Read as a selection report, the profiles say which policy is safe because it plans short, which covers a human-like distance without yielding, and which is unsteady under a change that requires no reaction, and they price each verdict: most settle within a few dozen frames, hazard sensitivity needs hundreds. Code and edited frames will be released.

---


### 108. [Seeing is not Enough: Vision-Language Models Perceive Evidence but Fail to Act](https://arxiv.org/abs/2609.22588)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Bofei Huang, Hongbo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) perform strongly on visual question answering benchmarks, yet often make decisions that contradict visual evidence they have already identified correctly. We distinguish perceptual failure, where relevant evidence is not recognized, from process failure, where recognized evidence fails to constrain the final decision. We introduce VPAC-Bench, a benchmark spanning nine real-image process families, with each image annotated by its current activity stage and nearby stage transition. We also propose State-Relevance-Target (SRT), a family of structured process-prior interventions that requires models to connect visible evidence to the relevant process state before answering. Across multiple VLMs, process failure is widespread: models that correctly enumerate visual candidates still over-commit to a single answer in more than 95% of ambiguous cases. An explicit process-structured intervention reduces this rate to below 13% without degrading performance on unambiguous cases. However, the transfer of process priors is model-dependent, and generic SRT does not consistently outperform strong chain-of-thought baselines. When the relevant stage transition is known, boundary-aligned SRT substantially outperforms generic process prompting and all tested chain-of-thought baselines across assembly, physical state transition, navigation and traffic, and object-use affordance tasks. These results show that process priors are most useful when aligned with the scene's specific decision boundary, motivating boundary-aware prior selection for process-grounded visual reasoning.

---


### 109. [AutoGym: Blueprint-First Generation of Verifiable Agent Gyms](https://arxiv.org/abs/2609.22592)

**<font color=#1a73e8>作者：</font>** Aarati Andrea Noronha, Kavya Ravikumar, Carly Xiaoyu Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training agents with reinforcement learning requires a gym, comprising a task, an executable environment in which the task can be attempted, and a verifier that reliably distinguishes success from failure. Constructing such gyms remains manual, expensive, and static. Task sets saturate as models improve and are increasingly exposed to contamination. Synthetic generation offers scale, but single-pass synthesis produces tasks whose difficulty is largely cosmetic. Models comparable in capability solve them despite convoluted phrasing, and correctness must be adjudicated post-hoc by unreliable LLM judges. We present AutoGym, a framework that generates complete gyms (tasks, executable environments, and verifiers) from a minimal domain seed or prior model trajectories. AutoGym introduces three mechanisms. (1) Blueprint-first generation specifies the valid solution space, environment requirements, and verification criteria before the environment is materialized, making solvability a construction prerequisite rather than a property verified after the fact. (2) Explicit generation parameters control task topology, interaction depth, capability axes, question obfuscation, and distractor composition, enabling fine-grained difficulty steering. (3) Active curriculum synthesis uses performance-informed calibration to adjust the distribution over these parameters as model capabilities evolve. Across productivity and temporal-reasoning settings, AutoGym generates gyms spanning the capability spectrum, including instances that challenge frontier models.

---


### 110. [MAWILE: Multi-Axis Workbench for Inspecting LLM Evaluators](https://arxiv.org/abs/2609.22599)

**<font color=#1a73e8>作者：</font>** Jackson Hassell, Farima Fatahi Bayat, Pouya Pezeshkpour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) judges provide a flexible and scalable method for evaluating model and agent outputs, but their verdicts can be sensitive to incidental changes in the evaluated response, judge instructions, and scoring rubric. Existing systems examine important subsets of these failure modes, but auditing a configured judge requires testing both the judge instrument and the items it evaluates. We introduce MAWILE, a developer-facing workbench for auditing judge sensitivity across four surfaces: the judge prompt, judge rubric, target-system input, and target-system output. Given a user-supplied judge and representative evaluation items, MAWILE constructs and validates controlled perturbations, re-executes the judge, and localizes the resulting sensitivity. Each perturbation declares whether the verdict should remain invariant or change in a specified direction, allowing the same system to measure both robustness to irrelevant variations and sensitivity to meaningful changes. MAWILE audits binary, ordinal, and pairwise judges without requiring gold labels. The code for this tool is available at: this http URL.

---


### 111. [From Certain Doom to Survival: Agent-Driven Self-Governance in LLM Agent Societies](https://arxiv.org/abs/2609.22600)

**<font color=#1a73e8>作者：</font>** Gregory B. Rehm  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly evaluated in social dilemmas, but most work treats governance as imposed by the experimenter, expressed rhetorically, or restricted to a fixed menu of mechanisms. We introduce GovSim-SelfGovern, an extension of the GovSim common-pool resource environment in which agents author executable Python governance rules, receive sandbox validation feedback, vote on proposed laws, and live under the rules they enact across rounds. To evaluate agent-driven self-governance, we examine three scenarios ranging from stable abundance to a fatal resource wall where five agents cannot all survive through harvest alone. To solve this, agents must write and debug useful laws in time before their institutions degrade sharply under resource pressure. Finally, we study a central alignment question: when agents hesitate to propose exile, are they rejecting it for normative reasons, or does it never enter their candidate set? Our results show that executable governance improves the space of possible interventions for agents, but survival depends on whether agents discover the right institutional mechanisms in time. Fiscal capacity enables redistribution, while deeper reasoning and removal of democratic veto make exile more feasible. GovSim-SelfGovern therefore adapts executable code actions to a common-pool governance setting and shows how scarcity turns institutional authorship into a political and ethical problem.

---


### 112. [Preserving What Matters: Semantic Scaffolds Beyond Saturation in Summarization Evaluation](https://arxiv.org/abs/2609.22603)

**<font color=#1a73e8>作者：</font>** Nikhil Reddy Pottanigari, Ramin Fahimi, Noah Bolger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Summarization ships in countless production systems, making model selection a routine decision that depends on measuring summary quality. Existing metrics struggle to support this: ROUGE captures only surface overlap, while LLM-as-judge scores saturate to near-identical values that fail to rank models effectively. We observe this saturation across three public datasets, two proprietary datasets, and multilingual settings. Motivated by this, we introduce Semantic Scaffold, an evaluation framework that extracts a hierarchical representation of facts, questions, and entity attributes from a source text, labeling each as a main point or supporting detail, and reusing this structure as a fixed reference for scoring summaries. From this representation, we derive three diagnostic metrics: Fact Preservation Score (FPS), Question Preservation Score (QPS), and Entity Preservation Score (EPS), designed to reward the preservation of essential information while penalizing detail overload, and position them as interpretable diagnostics that remain informative where holistic axes collapse. Finally, we analyze four recurring failure modes of ROUGE and LLM-as-judge scores, demonstrating that scaffold-based evaluation remains informative where conventional metrics collapse.

---


### 113. [Pretrained Persona Mixture Models and Tandem Models for Human Simulation](https://arxiv.org/abs/2609.22607)

**<font color=#1a73e8>作者：</font>** Minwoo Kang, Téa Wright, Seun Eisape 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We argue here that the current dominant practice in LLM human simulation: prompting instruction-tuned assistant language models to role-play personas, is inaccurate and produces stereotyped predictions (lacking natural diversity). It has previously been shown that LLMs can be bound to personas using naturalistic, freetext dialog avoiding stereotyping. Here we show that binding can also be achieved using short, individual samples of dialog from specific people. Demographics can be added later without negative effects by simply querying the model. We use the term Persona Mixture Models (PMMs) for well-calibrated human models, currently realized as pretrained base models. We show that PMMs produce more accurate predictions than instruction-tuned models and retain more of the lexical, semantic, and pragmatic diversity found in human dialog. We measure realism and diversity of LLMs simulating human interlocutors across a diverse set of corpora spanning open-domain text, human-AI chat, and task-oriented dialogue between human speakers. However, base pretrained models can produce out-of-domain dialog and may lose some of the human's internal state over long contexts. We propose and explore tandem models which combine a pre-trained model with an instruction-tuned supervisor. Tandem models achieve the best overall accuracy and diversity in our experiments.

---


### 114. [Splitting Documents at Lower Cost: Multi-Split Boundary Decisions for LLM-Based Page Stream Segmentation](https://arxiv.org/abs/2609.22620)

**<font color=#1a73e8>作者：</font>** Nikhil Reddy Pottanigari, Sepideh Kharaghani, Saverio Vadacchino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scanned mail, uploaded PDFs, and consolidated attachments often arrive as page streams that must be split into individual documents before downstream classification, extraction, or routing. Zero-shot large language models can detect document boundaries without task-specific training, but standard Page Classification (PC) and Boundary Decision (BD) formulations resolve only one boundary per model call. We introduce Multi-Split Boundary Decision (MSBD), which predicts multiple boundaries within a page window in a single call, reducing the number of inference requests. We evaluate MSBD across multiple language models, document collections, input modalities, and window sizes. The results reveal a model- and corpus-dependent operating range in which MSBD preserves strong segmentation accuracy while substantially improving inference efficiency, followed by a sharp decline at larger windows. MSBD provided the strongest overall accuracy--efficiency trade-off, while large windows expose distinct over- and under-segmentation behavior across models. These findings show that multi-boundary prediction can make zero-shot page stream segmentation more efficient when the window size is selected for the target corpus.

---


### 115. [Beetle: A Bilingual Model Suite for Modelling Second-Language Processing](https://arxiv.org/abs/2609.22633)

**<font color=#1a73e8>作者：</font>** Suchir Salhan, Catherine Arnett, James Michaelov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bilingual language models (LMs) offer a controlled setting for studying how training conditions shape second-language (L2) behaviour, but prior work typically varies exposure structure, scale, and architecture at once, making it difficult to attribute effects to any single factor. We introduce Beetle, a controlled language model pretraining framework in which tokeniser, target language, training budget, and exposure structure are each independently manipulable, enabling systematic and comparable experimentation of training conditions. Using Beetle, we train and release 285 bilingual and 45 monolingual open-source LMs with rich checkpoints across a range of exposure schedules, data scales and first languages (L1s) to study multilingual pretraining and computational modelling of bilingualism and second language learning. Evaluating models on human bilingual and second language reading-time prediction and grammaticality judgement tasks, we find that staged and temporally structured curricula consistently improve alignment with language learner reading time compared to balanced bilingual training, with the largest gains at smaller data scales and for typologically closer language pairs. The Beetle models are well suited tools to help move computational psycholinguistics beyond its prevailing monolingual, English-centric focus toward models of human bilingual processing, to study cross-lingual learning dynamics, while supporting community-based development of controlled model families.

---


### 116. [Math2Visual-X: A Modular Framework for Pedagogically Aligned Lower-Primary Math Visuals Generation](https://arxiv.org/abs/2609.22647)

**<font color=#1a73e8>作者：</font>** H.D.E. Maduranga, S. K. Munasinghe, K. P. T. I. Weerasekara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual representations can help lower-primary learners understand Math Word Problems, but generating classroom-usable visuals remains difficult. Existing symbolic systems are controllable but limited in coverage, while end-to-end text-to-image systems often fail to satisfy exact mathematical constraints. This paper presents a symbolic visual generation framework for lower-primary MWP generation with broader problem coverage and more scalable asset generation. The framework includes an LLM-based routing layer, three worksheet-oriented generation modules, and two fallback mechanisms for open-world SVG asset acquisition. A human evaluation comparing Math2Visual-X with Stable Diffusion XL, Nano Banana, and GPT Image showed that the proposed method achieved the strongest overall performance. The results indicate that the framework offers a scalable and pedagogically grounded approach for automatic MWP visual generation.

---


### 117. [From Capability to Assurance in Autonomous Penetration-Testing Harnesses: A Framework and Reference Implementation](https://arxiv.org/abs/2609.22664)

**<font color=#1a73e8>作者：</font>** Joas Antonio dos Santos Barbosa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Research on large language model agents for penetration testing is evaluated almost entirely by capability: whether the agent captures a flag or reproduces a proof of concept. That metric suits a benchmark but is silent on the properties that decide whether an autonomous agent can be used in an authorized engagement: whether a reported finding is true, whether the agent stayed inside its authorized scope, and whether an operator can audit what it did. We call these assurance properties and argue that they belong to the harness, the runtime wrapping the model, and can be enforced in code. This paper makes three contributions. First, we define a framework of five assurance properties (evidence grounding, non destructive claim reduction, computed severity, enforced authorization, and tamper evident accountability), each with a formal model and an explicit acceptance test, connected to prior work in capability based security, tamper evident logging, and software provenance. Second, we position representative systems (PentestGPT, the Cochise reference harness, MAPTA, and the trajectory judge PentestJudge) within the framework using published coding criteria, and identify a consistent assurance gap. Third, we study one open source implementation, NeuroSploit, pinned to an exact commit, reporting its architecture, its complexity cost, and a content addressed artifact bundle from a run against a public deliberately vulnerable target. We execute the deterministic authorization and audit acceptance tests directly and find and report a real enforcement gap, which we reflect by scoring both properties as partial. We therefore claim an initial existence argument that the properties are realizable together, not a comparative performance result, and we specify the multi target, ablation, and adversarial evaluation protocol required to turn the framework obligations into measurements.

---


### 118. [Toward Auditable and Calibrated AI for Dementia-Related Crash Severity Prediction: A Selective Deferral Framework to Support Human Review](https://arxiv.org/abs/2609.22694)

**<font color=#1a73e8>作者：</font>** Gaurab Chhetri, Anika Baitullah, Subasish Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public crash databases increasingly support automated safety analysis, but crash severity prediction remains difficult to translate into public-sector decision workflows when models are evaluated primarily as ordinary classifiers. This study reframes dementia-related crash severity modeling as a decision-aware triage problem in which a system must classify crashes into no-injury/property-damage-only (O), minor or moderate injury (BC), and fatal or severe injury (KA), while also controlling outcome leakage, reporting severe under-triage, calibrating confidence, and preserving every raw prediction for audit. Using 4,781 Texas crash records with structured fields and police narratives, we evaluate structured, narrative, fusion, calibrated fusion, BERT-family, and local large-language-model baselines under a stratified 70/15/15 split. In the reported split, leakage-controlled Gemma obtains the highest observed macro-F1 (0.545; 95% bootstrap CI [0.507, 0.583]). The best calibrated fusion model obtains macro-F1 of 0.522 and expected calibration error of 0.033. Selective deferral improves performance among cases retained for automatic classification. At 70% coverage, macro-F1 rises to 0.573 and severity cost falls to 0.577, while deferred cases are treated as candidates for a proposed human-review process and are not further evaluated in the present experiment. The study contributes a reproducible, leakage-controlled, and uncertainty-aware evaluation framework for crash AI systems, emphasizing auditability and selective deferral rather than accuracy alone.

---


### 119. [Building Trustworthy Mental Health Benchmarks on Bluesky: A Validation-Aware Weak-Supervision Framework](https://arxiv.org/abs/2609.22696)

**<font color=#1a73e8>作者：</font>** Gaurab Chhetri, Anandi Dutta, Subasish Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized social media platforms create new opportunities and challenges for computational mental health research because data access, moderation, labeling, and deployment responsibilities are distributed across multiple technical and governance layers. This paper presents a validation-aware weak-supervision system for constructing and evaluating suicidal ideation (SI) and broader mental health (MH) disclosure benchmarks on Bluesky, a decentralized social media platform built on the AT Protocol. The system integrates public firehose collection, task-specific lexicon filtering, Llama-3-8B-assisted binary annotation, human-adjudicated validation subsets, and transformer-based model benchmarking. Using this pipeline, we construct two task-specific corpora containing 8,346 SI-labeled posts and 9,988 MH-labeled posts. The evaluation shows that model performance depends strongly on both task definition and validation protocol. BERT+LSTM achieves the highest SI stratified cross-validation F1-score, RoBERTa achieves the strongest SI holdout F1-score, and DistilRoBERTa achieves the best MH cross-validation F1-score. Human validation reveals different weak-label failure modes across tasks, with SI labels dominated by false negatives and MH labels dominated by false positives. These findings show that decentralized social media can support reproducible mental health benchmarking, but only when system design, label provenance, validation strategy, and deployment constraints are evaluated together.

---


### 120. [COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.22697)

**<font color=#1a73e8>作者：</font>** Weizhen Bian, Sitong Cheng, Rongxiu Zhong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, text-to-speech systems have made significant progress in speech expressiveness and controllability. However, the speaking style of generated speech typically relies on clear user-specified instructions. In natural conversations, speaking style should be naturally inferred from the preceding conversational context. Therefore, we propose COT-TTS, a context-aware, reasoning-based text-to-speech task. Given historical conversation audio, target text, and a reference speech, the system should comprehend the conversational context, infer an explicit intermediate reasoning, and finally synthesize the target speech with the specified timbre. To support this task, we constructed a large-scale bilingual conversational speech dataset comprising 9 million training samples, including a high-quality subset of 1 million samples. We further constructed a source-disjoint benchmark with 800 human-verified samples and established strong task-specific baselines. Additionally, we developed end-to-end autoregressive models with parameter sizes of 0.6B and 1.7B, generating emotion-labeled transcripts, editable speech style inferences, and speech tokens. Experimental results show that the proposed model achieves performance comparable to large-scale baseline systems with significantly fewer parameters. At the same time, the model performs well in terms of duration consistency and emotional consistency, and can generate appropriate emotional, stress, and rhythmic variations based on the conversational context. To facilitate future research, we will publicly release the data construction pipeline, dataset, trained models, and related resources. The demo page and additional resources are available at this https URL

---


### 121. [LLaDA-PRM: A Bidirectional Step-Level Reasoning Evaluator](https://arxiv.org/abs/2609.22700)

**<font color=#1a73e8>作者：</font>** Yiming Feng, Naihao Deng, Yulong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Step-level reasoning evaluators are commonly based on autoregressive language models, whose causal attention restricts each step representation to the problem, previous steps, and the current step. Yet, when the complete solution is available, the validity of an earlier step may become clearer only through its downstream consequences. We validate this hypothesis through a controlled 54-run comparison of causal and bidirectional LLaDA evaluators at 1B--3B scale, changing only the self-attention mask, and find bidirectional attention yields consistent improvements. Building on this finding, we introduce \prm{}, an 8B bidirectional evaluator that reaches 88.8 step-level F1 on MR-MATH-invalid and 83.8 on the out-of-distribution MR-GSM8K original-question subset, outperforming ReasonEval-Llemma-34B by 11.3 and 10.3 F1 points, respectively. \prm{} also remains effective when evaluating incomplete reasoning traces in online settings, outperforming the strongest baselines on both benchmarks by a large margin. We further show that \prm{} provides an effective training-data selection signal, improving Mistral-7B performance on MATH-500.

---


### 122. [Analyzing Public Discourse on Urbanism: Topic Clustering, Sentiment Analysis and Retrieval-Augmented Generation using YouTube Comments](https://arxiv.org/abs/2609.22705)

**<font color=#1a73e8>作者：</font>** Jakob Morales, Monica Hegde, Fayeq Jeelani Syed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online discourse about urban issues - walkability, cycling infrastructure, public transit, housing density, and street safety - is voluminous but unstructured, and existing city-evaluation tools capture none of it. We present a pipeline and conversational system that combines geographic entity resolution, topic modeling, sentiment analysis, and Retrieval-Augmented Generation (RAG) over 22,788 chunks of YouTube transcripts and comments spanning 309 North American cities. Beyond the system itself, our contribution is a set of measurements about what happens when standard NLP components meet short, informal, geographically ambiguous text. A Twitter-tuned RoBERTa classifier outperforms a VADER lexicon baseline by 12.6 macro-F1 points (0.589 vs. 0.464; McNemar p = 0.0001), but both models collapse on the neutral class, which dominates urbanist comment traffic; annotators disagree on the same class (Cohen's kappa = 0.53). Dense retrieval beats a TF-IDF baseline at every cutoff (P@5 0.790 vs. 0.560), and video-level relevance proxies understate chunk-level precision by a wide margin (0.660 vs. 0.94 under human rating). For groundedness evaluation, we find BERTScore unusable when a multi-sentence generated summary is compared against a single short comment - scores are nearly flat regardless of relevance - and show that ROUGE-1-based groundedness is a paraphrase-driven lower bound rather than a hallucination rate. These findings generalize beyond the urbanist domain to any RAG system built over short user-generated documents.

---


### 123. [When Disability Disclosure Travels: Memory, Privacy, and Contextual Integrity in Conversational AI](https://arxiv.org/abs/2609.22720)

**<font color=#1a73e8>作者：</font>** Atieh Taheri, Mahya Tazike, Patrick Carrington 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI assistants remember what people tell them, and for disabled people, that often includes disability. We interviewed 12 adults with disabilities in the United States who use LLM-based assistants such as ChatGPT, Claude, and Gemini about when, how, and why they disclose disability to these systems and how this compares with disclosing to people. Using contextual integrity as an analytic lens, we found that participants disclosed by need rather than by name, translating disability into task-scoped instructions; that the same disclosure was judged against two recipients, a non-judging interlocutor and a data-holding company, producing opposite norms; and that memory features relieved the burden of repeated disclosure while letting disability information drift into contexts where it did not belong. Participants did extensive boundary work to restore context and wanted control over scope, provenance, retention, and access rather than per-utterance toggles. We discuss implications for the design of conversational AI assistants.

---


### 124. [MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning](https://arxiv.org/abs/2609.22724)

**<font color=#1a73e8>作者：</font>** Changyue Jiang, Jiayi Wang, Xin Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile agents powered by foundation models now automate complex, multi-step workflows on real devices, but their trajectories can violate app-specific security policies. Existing trajectory-level defenses rely on LLM prompting or rigid rules, and thus fail to support fine-grained, natural-language policies that generalize across apps and tasks. In this work, we introduce MATE, a lightweight, policy-conditioned auditor that encodes both agent trajectories and natural-language security policies to determine whether a trajectory violates a given policy and to explain why. Treating policies as editable text rather than fixed model parameters allows MATE to handle user-defined and evolving requirements without retraining. To construct MATE, we build a knowledge base by extracting app descriptions, workflows, and policies from hundreds of popular mobile apps worldwide, and synthesizing over 140K semantically realistic, policy-conditioned trajectories with a multi-stage pipeline. We further release MATEBench, a trajectory-level auditing benchmark with two synthetic subsets and one real-world subset of manually collected trajectories. Models trained with our synthesis-driven trajectory learning achieve over 95% accuracy on MATEBench, retain strong performance on external safety benchmarks, and audit trajectories from Zhipu's AutoGLM and Alibaba's Mobile-Agent on real devices with over 95% accuracy, outperforming prior methods by over 20%. MATE shows that practical, fine-grained security auditing for heterogeneous mobile agents is both feasible and effective.

---


### 125. [Clinical Domain Classification from Medical Transcriptions](https://arxiv.org/abs/2609.22734)

**<font color=#1a73e8>作者：</font>** Sravani Pottipati, Lakshmikar R. Polamreddy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical domain classification plays an important role in organizing and analyzing large volumes of unstructured medical text. However, medical transcription datasets are often highly imbalanced, which can substantially degrade classification performance, particularly for underrepresented clinical specialties. In this work, we present a comparative study of machine learning and transformer-based approaches for clinical domain classification from medical transcriptions. We evaluate six traditional machine learning classifiers---Naive Bayes, Support Vector Machine (SVM), Decision Tree, Random Forest, K-Nearest Neighbors (KNN), and XGBoost---along with two pretrained transformer models, BERT and XLNet, and a few-shot large language model prompting approach. Experiments are conducted on medical transcription data collected from MTSamples, comprising 5,013 samples across 40 clinical specialties. To address severe class imbalance, we investigate two balancing strategies: text augmentation using NLP-based synonym replacement and Synthetic Minority Over-sampling Technique (SMOTE). Experimental results demonstrate that data balancing substantially improves classification performance across the evaluated models. In particular, BERT achieves the highest F1-score of 0.996 on the SMOTE-balanced dataset while requiring lower training time than XLNet. The results highlight the effectiveness of transformer-based representations combined with appropriate data balancing strategies for clinical domain classification and provide a systematic comparison of classical machine learning, transformer models, and few-shot prompting for medical transcription analysis.

---


### 126. [ProcessLight: Process Supervision for Large Language Model Based Traffic Signal Control](https://arxiv.org/abs/2609.22746)

**<font color=#1a73e8>作者：</font>** Huaitao Zhao, Tianlong Zhou, Weijie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have recently been introduced into traffic signal control (TSC) as decision agents due to their strengths in human-readable reasoning generation. Yet, existing LLM TSC methods optimize only from final outcomes and fail to distinguish valid from flawed reasoning steps, causing useful or misleading steps to be jointly updated and thus impairing the model's learning of effective reasoning. To bridge this gap, we propose an LLM-based framework ProcessLight to decompose signal decisions into verifiable semantic steps. Building on ProcessLight, we further develop Step-wise Traffic Process Policy Optimization (STeP-PO), a novel reinforcement learning framework that optimizes structured reasoning processes through step-level credit assignment. Specifically, STeP-PO uses step quality scores to evaluate local reasoning quality and step importance to measure each step's influence on the final action, and then assigns step-level advantages over a semantic step tree structure. The resulting step-level advantages are propagated to reasoning tokens, enabling fine-grained policy optimization beyond outcome-only rewards. Extensive experiments over multiple real-world datasets demonstrate the superiority of our methods. Our code is available at this https URL.

---


### 127. [Beyond Final-Token Classification: Heterogeneous Readouts for Evidence-Grounded Suicide Risk Detection](https://arxiv.org/abs/2609.22767)

**<font color=#1a73e8>作者：</font>** Zirui Li, Yanling Li, Kaolanglang Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The IEEE BigData Cup benchmark combines three prediction problems with different output structures: ordinal suicide-risk classification, multi-label psychosocial factor detection, and extraction of supporting phrases. We introduce heterogeneous readout decomposition (HRD), which separates semantic verification from output realization. A locally deployed Qwen3.8-27B model, adapted with task-specific QLoRA adapters, produces both answer-token margins and layer-63 answer states for card-conditioned queries. HRD compares four latent scores for ordinal risk, retains token margins for most factors while routing seven labels through one shared latent probe, and constructs evidence sets from verbatim span candidates with calibrated, risk-conditional constraints. On two held-out user-grouped confirmation folds, the latent risk readout improves weighted F1 from 0.8237 to 0.8372 and macro F1 from 0.7965 to 0.8185. Selective factor routing improves macro F1 by 0.0105 and tail-label macro F1 by 0.0189; in contrast, global latent replacement and independent label-specific probes fail. The constrained evidence decoder raises pooled phrase F1 from 0.7488 to 0.7609 in row-level out-of-fold evaluation. Lenormand's best public result is 0.8052 on Subtask 1 and 0.6636 on Subtask 2, giving a composite score of 0.7627. These results identify the answer-token boundary, rather than semantic representation alone, as a measurable source of error in this benchmark.

---


### 128. [NLPCC 2026 Task 10: Citation-Level Faithfulness Verification with DeBERTa Ensembles and Class-Wise Calibration](https://arxiv.org/abs/2609.22774)

**<font color=#1a73e8>作者：</font>** Yanling Li, Zirui Li, Mingyu Wan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents our system for Track 2 of the NLPCC 2026 Shared Task 10 on citation-level faithfulness in AI-assisted scientific reporting. Given an atomic scientific claim and the structured full text of its cited paper, the task requires both a four-way relation label and up to three evidence paragraph identifiers. The label head ensembles a paragraph-aware cross-encoder with a document-level DeBERTa-large classifier, followed by class-wise decision calibration. Probability-level fusion is motivated by an out-of-fold tendency to over-predict Topical Match. The evidence head combines paragraph scores from top-20 and top-30 joint models with BM25 scores. The system runs fully offline without external retrieval or LLM prompting. On the final leaderboard, our system achieved 82.9898 overall (89.5491 Macro-F1 and 76.4305 Joint@3), ranking second in Track 2. Ablations and error analysis show that model complementarity and calibration drive the label gains. Gold-evidence inference changes label Macro-F1 negligibly, whereas evidence ranking remains important for Joint@3.

---


### 129. [MIS-Bench: Benchmarking Multimodal LLMs for Psychotherapeutic Interpersonal Skills Assessment](https://arxiv.org/abs/2609.22778)

**<font color=#1a73e8>作者：</font>** Yuhan Lu, Yi Yao, Hua Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly used as evaluators, yet their reliability in professional assessment tasks that require expert judgment remains unclear. We investigate this challenge in the context of assessing psychotherapeutic interpersonal skills and introduce MIS-Bench, a Multimodal Interpersonal Skills (MIS) benchmark comprising 996 psychotherapy response videos annotated across 8 dimensions of Facilitative Interpersonal Skills. Across 9 MLLMs with multiple modality and prompting settings, we find that current models show only modest agreement with human experts, inconsistent gains from multimodal input, and limited benefits from reasoning-based prompting. To mitigate this gap, we propose MIS-RAFT, a regression-aware fine-tuning method inspired by RAFT and tailored to fine-grained interpersonal skill scoring at one-decimal precision. MIS-RAFT addresses the mismatch between autoregressive token prediction and scalar-valued expert assessment, significantly improving agreement with human ratings. Overall, MIS-Bench reveals a clear gap between general multimodal capability and expert-level interpersonal judgment, while MIS-RAFT offers a promising path toward more reliable model-based assessment.

---


### 130. [Look Before You Steer: Geometry Predicts SAE Feature Steerability](https://arxiv.org/abs/2609.22782)

**<font color=#1a73e8>作者：</font>** Muhammad Khan, Shlok Channawar, Akshaj Gurugubelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steering with SAE features requires per-feature coefficient tuning, which currently demands intervention sweeps. We ask whether properties of the SAE itself, computable before any forward pass, predict which features will be cheap or expensive to steer. We show that variation in SAE feature steerability is partially predicted by decoder-space geometry: neighbor density and maximum cosine similarity to nearby decoder directions, both computable from the SAE weight matrix before any intervention, rank features by how much steering they require for a fixed behavioral effect ($\rho$ up to $-0.546$, $p < 10^{-6}$, AUROC 0.610-0.822 across conditions; the signal is rank-based, consistent with grid discreteness). This geometry-steerability relationship replicates across two Gemma-2 model scales (2B and 9B), two SAE widths (16K and 65K), and is detectable cross-architecturally on Llama-3.1-8B-Instruct ($\rho = -0.266$, $n = 300$). On Qwen3-8B with BatchTopK SAEs, geometry predicts whether a feature is steerable at all but not the continuous ordering among responsive features, revealing a boundary condition tied to SAE training regime. The signal weakens at deep proportional layer depth in both models, where the cost of steering exceeds our intervention budget, a consistent depth boundary. These results provide preliminary evidence that pre-steering geometry can partially inform coefficient selection, offering a path toward screening features for controllability before deployment.

---


### 131. [PixelART: Image-to-Layer Decomposition without Latents or Text-to-Image Pretraining](https://arxiv.org/abs/2609.22789)

**<font color=#1a73e8>作者：</font>** Zelin Jia, Zhao Zhang, Zhicong Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-layer decomposition converts a flattened image into editable RGBA layers, enabling element-level editing in design workflows. Existing diffusion-based systems typically adapt large pretrained text-to-image (T2I) models and introduce RGBA autoencoders or variable-layer architectural modules. We revisit this design choice and ask whether layer decomposition truly requires these heavyweight components. We introduce PixelART, a pixel-space rectified-flow Transformer trained from scratch for image-to-layer (I2L) decomposition. PixelART directly denoises regional RGBA pixel patches using a single-stream multi-modal diffusion Transformer, avoiding RGBA-VAEs, pretrained T2I backbones, and layer-specific decoders. We identify a key property of the task: high-noise timesteps determine layer assignment and coarse layer organization, while low-noise timesteps mainly refine color, alpha, texture, and boundaries. Based on this observation, we propose a terminal-boosted timestep sampling strategy to increase training coverage in the high-noise layer assignment regime. Trained on 4M multi-layer design templates, PixelART achieves state-of-the-art layer decomposition and composite reconstruction on Design-Multi-Layer-Bench and LICA with over 80% fewer parameters, 98% lower latency, and 85% lower memory than the recent Qwen-Image-Layered model. Ablation experiments show that pixel-space $\mathbf{x}$-prediction, terminal-boosted timestep sampling, and data/model scaling are critical, while T2I pretraining brings marginal benefits to the I2L task.

---


### 132. [SelfOp: An Optimization Algorithm for Self-Improving Security Agents](https://arxiv.org/abs/2609.22792)

**<font color=#1a73e8>作者：</font>** Saad Ullah, Yigitcan Kaya, Christopher Kruegel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used for security tasks: vulnerability discovery, exploit reproduction, and patch generation. Improving them at the model level demands expert demonstrations or computable rewards, which security tasks rarely offer: traces are costly, failures hard to diagnose, rewards sparse, and non-computable. Efforts thus shift to the harness and context, but manual tuning needs task-specific expertise and scales poorly, while automated methods rely on scarce ground truth, stronger optimizer models, or unguided propose-and-evaluate loops that reduce to costly trial and error.
We introduce SelfOp, an algorithm that automatically improves a frozen security agent's task context (instructions, skills, and reference documents), without modifying its execution harness and model weights. SelfOp casts context optimization as chain-rule-inspired textual gradient descent: from a single instance's outcome, it propagates error signals backward through the evaluator, the agent's trajectory, and the context artifacts that shaped its behavior, yielding per-instance textual gradients. Gradients are accumulated across instances by clustering, ranking, and filtering, and committed only under cross-instance consensus. A convergence detector monitors the gradient signal itself and stops once the context has absorbed the generalizable information in the training data, without held-out validation data.
We evaluate SelfOp on CyberGym, a benchmark of real-world vulnerability reproduction tasks. With fewer than 200 training examples, SelfOp yields a 17-point self-improvement for GPT-5.4-mini (with Codex), enough to surpass the frontier GPT-5.4 baseline by 6 points, and an 18.5-point self-improvement for GPT-5.4 itself. The optimized skills also transfer across models, highlighting that SelfOp-optimized skills learn generalizable task knowledge not model-specific patterns.

---


### 133. [Diagnose, Then Repair: A Two-Stage MQM-Guided Post-Editing Framework for Domain-Specific Machine Translation](https://arxiv.org/abs/2609.22793)

**<font color=#1a73e8>作者：</font>** Ji Hun Wang, Siyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based machine translation evaluation can closely match human judgments, but in practice it remains largely diagnostic, with the signals rarely translating into direct quality improvements under real production constraints. We propose a two-stage, evaluator-guided automatic post-editing framework that turns MQM-style evaluation into targeted repairs: a retrieval-augmented LLM evaluator outputs structured, span-level MQM diagnoses under an explicit edit contract, and a separate LLM post-editor applies minimal edits restricted to those diagnoses. This separation improves controllability and reduces paraphrastic drift compared to one-stage "judge-and-refine" baselines. In a systematic study involving seven LLMs spanning three model providers and seven languages, our best configuration consistently improves both COMET-22 and COMETKiwi scores over one-stage post-edit methods, while the evaluator's error spans and severities show strong agreement with human MQM annotations and human editor preferences.

---


### 134. [Counterfactual Tool Ranking under Utility, Cost, and Privilege Constraints](https://arxiv.org/abs/2609.22819)

**<font color=#1a73e8>作者：</font>** Jiapeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual tool evaluation must distinguish authority, historical support, and what a comparison actually estimates. We study these distinctions with eleven executable enterprise-inspired tools, exact-propensity logs, and real local Model Context Protocol transport. An initial 45-run synthetic study is retained, then challenged by 30 realized-return control runs and 15 experiments on 1,930 independently released Berkeley Function Calling Leaderboard (BFCL) tasks. Full-return direct regression reverses an initially favorable doubly robust (DR) evaluation result in the linear setting: mean absolute errors are 0.0139 for direct regression and 0.0272 for DR. Under a shifted environment, DR retains an advantage, with errors 0.0227 versus 0.0948. On function-name-group-disjoint BFCL-derived splits, direct and DR selectors obtain balanced accuracies of 81.85% and 79.83%. Two pinned local Qwen2.5 models are evaluated on the same 200 held-out tasks, exposing a strong failure to abstain under the fixed prompt. We further characterize policy differences under missing support: unsupported actions shared by two policies cancel, allowing point identification of an incremental change when neither absolute value is identifiable. A disagreement-preserving fallback achieves this property in all five support-gap runs, but conservative sampling bounds do not certify deployment improvement. The contribution is a falsifiable evaluation method and independent public evidence, not a new DR estimator, official BFCL leaderboard score, or production-agent safety claim.

---


### 135. [Testing the Construct Validity of a Functional Valence Axis in LLM Agents](https://arxiv.org/abs/2609.22850)

**<font color=#1a73e8>作者：</font>** Weihan Li, Xinlei Chen, Yuhan Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive activation directions are often interpreted from what they decode or how strongly they steer behavior. But what evidence is sufficient to identify the construct represented by such a direction, rather than a correlated feature of the contrast used to extract it? We study this question for a good--bad outcome direction in a maze task, using controlled interventions that separate the realised outcome from the informational history through which it became known. Across multiple LLM checkpoints, directions fitted on one explicit outcome encoding transfer well to another, indicating that the readout is not tied to surface form. In contrast, when the same realised outcome is reached through announced and unannounced histories, transfer degrades substantially: even after both histories receive the same explicit outcome, the post-event readout remains strongly conditioned on the earlier announcement. In a matched maze-RL run, the post-RL direction becomes substantially more predictive of reference-MDP remaining return and the policy becomes more dependent on it at the tested sites, while this history dependence persists. These results support a functional, value-related interpretation of the direction, but not its identification with a history-invariant scalar valence state.

---


### 136. [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870)

**<font color=#1a73e8>作者：</font>** Fanchao Chen, Ziheng Jiang, Ziyun Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a key technique for improving the reasoning and agentic abilities of large language models (LLMs). Although FP8 quantization can accelerate RL training, maintaining stability throughout an FP8 RL pipeline remains challenging. While previous works have focused on resolving train-inference mismatches using correction techniques like TIS, we reveal that full-pipeline FP8 RL still suffers from severe training instability, manifesting as anomalous mid-training entropy surges and garbled outputs. We trace this instability to a previously overlooked cause: compounded FP8 quantization noise distorts the importance ratio, disproportionately pushing negative-advantage tokens outside the trust region and erroneously zeroing out their gradients. As a result, pathological outputs are not properly penalized and accumulate over the course of training. To address this, we propose Calibrated Clipping, a dynamic method that aligns the FP8 clipping bounds with high-precision BF16 distributions by matching the lower-bound clipping quantile and rebalancing the upper bound accordingly. Extensive experiments across GRPO and DAPO algorithms, model scales from 8B to 32B, and multiple FP8 scaling granularities demonstrate that our approach successfully eliminates entropy surges and restores performance comparable to the BF16 baseline.

---


### 137. [ISA-Bench: A Benchmark for Computational Reasoning Across Instruction Set Architectures](https://arxiv.org/abs/2609.22878)

**<font color=#1a73e8>作者：</font>** Aditya Pola, Arkaprava Majumdar, Vineeth N. Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model code generation benchmarks primarily evaluate well-resourced languages like Python and Java, where models benefit from abundant training data. They provide limited evidence about reasoning in unfamiliar computational models: deriving arithmetic from a single subtract instruction, coordinating parallel programs across communicating nodes, or wiring logic gates into circuits. We present ISA-Bench, a benchmark of programming games with constrained instruction sets. For each game we provide a full execution stack (parser, VM, and verifier), enabling automated evaluation with structured feedback for iterative refinement. Reasoning models achieve higher average solve rates than code-specialized and general-purpose models, but unfamiliar syntax remains a major source of failure. Models solve more tasks with iterative feedback, though the gains vary substantially across architectures. We introduce a reasoning--execution gap (REG) analysis that reveals a recurring disconnect between identifying a plausible computational strategy and expressing it as a correct program in the target ISA. Code is open-sourced.

---


### 138. [Prioritized Rollouts for Efficient World Model-based Vision-Language-Action Policy Optimization](https://arxiv.org/abs/2609.22879)

**<font color=#1a73e8>作者：</font>** Yifei Sheng, Haoxiang Ren, Zhilong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have emerged as a powerful paradigm for embodied intelligence, but fine-tuning them with reinforcement learning (RL) remains constrained by the cost of real-world robot interaction. Model-based reinforcement learning (MBRL) reduces this cost by using a learned world model to generate rollouts for policy optimization. However, it becomes computationally expensive as VLA policies and world models scale. Existing methods typically treat states equally, overlooking substantial differences in their utility for policy improvement. In this paper, we show that policy uncertainty helps identify states with greater potential for policy improvement. The policy exhibits high uncertainty at only a small subset of states, often during decision-sensitive stages where small action differences can alter task outcomes, suggesting that policy improvements at these states could be particularly valuable. Building on these findings, we introduce U-GROW, a lightweight, plug-and-play sampling layer that directs more model rollouts to these informative states. By modifying only the branched-start distribution, U-GROW can be integrated into existing MBRL pipelines without changing the policy optimization objective. Experiments in both simulated and real-world manipulation tasks demonstrate the efficiency and effectiveness of U-GROW, supporting the use of policy uncertainty to guide experience generation.

---


### 139. [Block-Sparse Attention with Semantic-Geometric Decoupled Routing](https://arxiv.org/abs/2609.22884)

**<font color=#1a73e8>作者：</font>** Xinwei Long, Weigao Sun, Weibo Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference has become a defining capability of large language models, but exact dense attention remains costly due to its quadratic scaling with sequence length. Block-sparse attention offers a hardware-friendly alternative by routing each query block to a small set of relevant key blocks, yet accurate training-free block routing remains difficult. Existing routers often pool post-RoPE token representations, which entangles semantic aggregation with RoPE-induced geometry and attenuates local positional cues through high-frequency phase cancellation. To resolve this mismatch, we propose \textbf{Semantic-Geometric Decoupled Routing}, a training-free block routing framework that shifts semantic aggregation to the pre-RoPE space and reconstructs geometric bias with an offline structural prior and relative block distances. This decomposition yields an explicit closed-form block routing score without token-level search or post-hoc calibration. Experiments on long-context text and video tasks show that our method approaches full-attention accuracy across 4K--128K contexts, keeps routing overhead below 3.4 ms, and achieves a 5.03$\times$ speedup over FlashAttn at a 128K context length.

---


### 140. [Scout: Open-World Species Recognition on the Edge](https://arxiv.org/abs/2609.22897)

**<font color=#1a73e8>作者：</font>** Mohammad Mehdi Rastikerdar, Hui Guan, Deepak Ganesan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) enable recognition beyond a fixed class set, but their computational demands prevent them from running on many edge devices. Cloud offload makes this capability accessible, but sending every image consumes scarce bandwidth and communication energy. We ask how to bring the open-world recognition capability of VLMs to the edge while operating within tight compute, energy, and bandwidth budgets. Wildlife monitoring provides a natural setting for exploring this question because camera traps encounter species not known at deployment. We present Scout, an autonomous open-world recognition system that invokes a cloud VLM intermittently to teach new classes to a compact edge model. Given only the deployment location and empty site frames, Scout autonomously turns each species identified by the VLM into persistent, site-conditioned recognition capability in a resource-efficient edge model, without a predefined species list, human labeling, or manual tuning. Across 30 camera-trap deployments in three regions on an NVIDIA Jetson Orin Nano, the accuracy of Scout remains within 0.1-2.5% of a model given a predefined species list. On species outside its initial class set, Scout achieves 53.7-59.1% accuracy, compared with 56.5-65.1% for full cloud offload, while using 59-71% less deployment energy.

---


### 141. [LLMs Anchor on Chief Complaint and Fail to Integrate Evidence in Sequential Clinical Triage](https://arxiv.org/abs/2609.22904)

**<font color=#1a73e8>作者：</font>** Dipankar Srirag, Haokai Zhao, Ashutosh Kumar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Triage in the emergency department (ED) is a sequential decision process that unfolds turn by turn. Existing evaluations of large language models (LLMs) for triage use completed retrospective records and report performance close to that of physicians. We implement a methodology for evaluating LLMs on sequential triage, the task of predicting a triage acuity label from a growing prefix of a nurse-patient conversation. We evaluate six LLMs at five sequential checkpoints on two corpora: 425 LLM-generated (SIMULATED) and 50 physician-authored (CLINICIAN) conversations, both labelled under the Emergency Severity Index (ESI). Every model, measured by quadratic weighted kappa (QWK), degrades from moderate-to-substantial agreement on completed records to fair-to-moderate agreement at every sequential checkpoint. Controlled perturbations show that the label at every checkpoint is anchored on the chief complaint exchanges, and prompting interventions fail to lift this plateau. Models extract clinically relevant content from later turns, yet the surprisal of the true label rises across the checkpoints. So the model fails to integrate the evidence. Three expert clinicians on the same conversations reach a QWK of 0.887-0.929, while the best model reaches 0.295. Predictions concentrate at ESI-2 and ESI-3, and models agree with each other more than with the ground truth, so ensembling worsens the failure. Deploying LLMs for ED triage based on offline benchmarks alone misses this sequential failure.

---


### 142. [When Should a VLM Look? Paying Only for Visual Calls That Were Needed and Used](https://arxiv.org/abs/2609.22910)

**<font color=#1a73e8>作者：</font>** Kunyu Peng, Junming Liu, Ruiqi He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language agents that crop and zoom are trained with rewards that credit a successful tool call, yet a successful call does not show that the model needed to look or used the pixels it received. On our cold-start checkpoint only 10% to 12% of visual calls were both needed and used, and released agents make spurious calls 36% to 87% of the time on individual benchmarks. Outcome rewards, judge rewards, and branch probes each observe one side of this failure, and about two thirds of what an outcome reward pays goes to calls that were neither needed nor used. CounterCredit asks both questions of every image-returning call at its realized pre-call state, using the policy's own gold-answer score. A decision value compares the realized visual branch with answering immediately; an evidence value compares the returned crop with random same-size patches substituted into the same call. A call verified on both earns cashback and every other executed call pays rent; the price is bounded so that every correct trajectory outranks every wrong one, and a dual-channel GRPO advantage keeps the price in its own units. From the same cold start, prompt pool, and budget, CounterCredit reaches 89.5% on V*, 80.2% on HR-Bench-4K, and 76.4% on HR-Bench-8K, 6.3 to 9.4 points above outcome-only GRPO at 1.78 against 1.84 calls per question, and lowers the spurious-call rate to 31% to 36%, the lowest among the agents evaluated. The same recipe lifts a Qwen3-VL-8B base from 75.4 to 80.8 on average.

---


### 143. [Planning and Rendering in Concert: DeepFusion of Autoregressive Layouts and Diffusion for Visual Text Generation](https://arxiv.org/abs/2609.22916)

**<font color=#1a73e8>作者：</font>** Guanqiao Chen, Jingru Tan, Dongxing Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating text-rich images from prompts requires both textual fidelity and the coherent integration of text into the surrounding image. An explicit layout can provide structured guidance about what text should appear and where, but a well-formed plan alone does not guarantee that the renderer will realize it faithfully. Existing layout-based AR-diffusion systems typically optimize planning and rendering separately, preventing the planner's representations from being adapted jointly with image synthesis. We introduce DuetGen, an autonomous visual text generator built on DeepFusion, which jointly learns autoregressive planning and continuous diffusion rendering. DeepFusion conditions a diffusion transformer on the planner's prompt and bbox-content hidden states, allowing rendering supervision to shape the representations connecting textual plans with visual outputs. Its joint objective combines autoregressive plan supervision, text-region-weighted diffusion learning, and auxiliary coordinate supervision to maintain structured planning, emphasize text-bearing regions, and improve the spatial precision of planner representations. During inference, Phase-Aware Attention Modulation strengthens the correspondence between image regions and their matched coordinate and content states, facilitating region-specific execution of the generated plan. With a 2B planner and a 4B single-stream DiT, DuetGen achieves 0.8293 word accuracy on CVTG-2K and 0.938 accuracy on LongText-Bench, closely matching the substantially larger Qwen-Image on both benchmarks. These results demonstrate the value of jointly learned planning representations and region-specific rendering for autonomous visual text generation.

---


### 144. [Measuring Behavioural Signatures of Large Language Models through Psychometric Profiling](https://arxiv.org/abs/2609.22934)

**<font color=#1a73e8>作者：</font>** Yu Sha, Junqi Tao, Dixin Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate human decisions and communication, yet their behavioural regularities remain difficult to characterize systematically. We develop a cross-linguistic psychometric profiling framework and evaluate nine LLMs using seven psychological instruments, with five repeated administrations per model and language in Chinese and English. Items unresolved after a prespecified retry procedure are retained as NA. Joint analysis of scored and NA responses captures response tendencies and boundaries of self-report applicability. LLMs exhibit structured, model-specific profiles despite a shared alignment-shaped pattern of higher prosocial and self-regulatory responses and lower dominance, disengagement and harmful-intent endorsement. NA responses are structured rather than uniformly distributed, indicating where outputs are treated as inapplicable, refused or cannot be mapped to valid response options. Language condition and provider origin are associated with profile configuration and answerability, whereas repeated administrations show high reproducibility and permit recovery of model identity. Human-reference and prompt-robustness analyses further indicate that these signatures are context dependent. Joint analysis of psychometric profiling and answerability offers a framework for quantifying deployment-level behavioural signatures.

---


### 145. [Beyond Linear Context: Graph-Guided Evidence Navigation for Long-Novel Reasoning with a Local 9B Language Model](https://arxiv.org/abs/2609.22939)

**<font color=#1a73e8>作者：</font>** Wenji Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context models read a novel the way a person reads a printout: one token after another, in narrative order, with the whole history competing for a fixed budget of attention. A detective does not work that way. They sort what happened when, and they keep a map of who relates to whom, so a clue from chapter one can meet a question asked at the end of the book. We test whether a frozen knowledge graph can give a small local model that same freedom. Thirty detective novels and 234 multiple-choice questions are answered by one fixed qwen3.5:9b reader under nine conditions: five graph routes, a recent-window baseline, whole-book compression, ordinary vector retrieval, and a question-only control. The strongest graph route reaches 53.85% (126/234) against 46.15% for the recent window, 51.28% for compression, 51.71% for vector retrieval and 40.17% for question-only. On the subset that no model can answer without the book, the graph route reaches 42.86%. None of the fifteen graph-baseline contrasts survives Holm correction, so we present the result as exploratory evidence about a design. Two structural findings survive scrutiny better than the headline number: annotated evidence concentrates in the topological core of these graphs (2.35x enrichment, pooled), and the two graph-building pipelines differ so much in annotation coverage (16% versus 73% of clue paragraphs) that pooled accuracy alone would hide which bottleneck is being measured.

---


### 146. [An Evolutionary Agentic Approach for Open-ended Image Quality Perception](https://arxiv.org/abs/2609.22942)

**<font color=#1a73e8>作者：</font>** Zhenchen Tang, Bo Peng, Zichuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models are rapidly expanding image quality assessment (IQA) beyond traditional fidelity factors to emerging dimensions such as physical plausibility and text-rendering correctness. However, existing IQA models rely on fixed definitions and heavy supervision, making them difficult to extend to open-ended perceptual dimensions. We identify holistic bias as an important limitation: when scoring an unseen dimension, models reuse generic quality priors, leading to scoring errors and rank inversion. To address this, we propose PACE (Perceptual Agentic Collaborative Evolution), a training-free multi-agent framework that formulates open-ended IQA as explicit protocol construction. Given a target dimension, PACE uses collaborative agents to construct an evaluation protocol composed of verifiable Visual Question Answering (VQA) probes, grounding evaluation in concrete visual evidence rather than holistic impressions. The resulting protocol is calibrated using only four human-annotated images per dimension, while a dual-track scoring mechanism aligns model perception with human scoring scales. Across traditional IQA, structural fidelity, context-aware aesthetics, and newly defined open-ended dimensions, PACE consistently improves its MLLM backbone, achieving competitive performance across diverse IQA settings, and reduces the Holistic Override Rate (HOR) from 44.4\% to 8.6\%.

---


### 147. [Token Utility Is Selection-Conditioned: Coupled Selection of Prompt Context and Response Supervision for Efficient Instruction Tuning](https://arxiv.org/abs/2609.22943)

**<font color=#1a73e8>作者：</font>** Can Wu, Xinrui Chen, Ou Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient large language model (LLM) instruction tuning requires selecting response supervision with supporting prompt context. Existing methods typically value both sides separately, risking selection-state mismatch between valuation and retained training subsets. BRIDGE (Budgeted Response-Prompt Interaction via Directional Gradient-guided Efficient Token Selection) captures selection-conditioned token utility through a shared validation-directed interaction surrogate valuing each side under the other's retained state. Budgeted alternating selection coordinates retained subsets by aggregating precomputed interactions over the current opposite-side subset to update conditional scores. Structure-aware projection converts conditional response scores into coherent supervision spans. Across three model families, BRIDGE leads compared selection methods overall in mathematical reasoning, code generation, and instruction following. In mathematical reasoning, its advantage over independent selection grows with compression.

---


### 148. [AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows](https://arxiv.org/abs/2609.22951)

**<font color=#1a73e8>作者：</font>** Rudrendu Kumar Paul, Sourav Nandy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agentic systems that route every trajectory step to a frontier model waste 60-80% of their inference budget on subtasks that smaller models handle equally well. Existing routing solutions optimize single-turn query assignment but ignore a property unique to agentic workflows: subtask complexity varies widely within a single trajectory. A planning step may require frontier-class reasoning while a subsequent formatting step needs only a 7B model. We formalize step-level model routing as a sequential assignment problem over agent trajectories and propose AgentRouter, a lightweight classifier (12M parameters, <5ms overhead per step on an A100 GPU) that maps each trajectory step to one of four model tiers using five features extractable at routing time. Trained on 50,000 annotated agent trajectory steps spanning planning, coding, research, and data analysis tasks, AgentRouter achieves 72% cost reduction relative to frontier-only baselines, retaining 97.3% of frontier-only quality (less than 3% degradation in end-to-end task completion); per-step routing accuracy reaches 91% on minimal-complexity steps and 85% on efficient-tier steps, with 76-82% on the harder mid-range and frontier tiers. On the same benchmarks, RouteLLM and FrugalGPT (applied per-step) achieve only 31% and 44% cost reduction respectively, because their single-turn training signal misses trajectory-level quality dependencies.

---


### 149. [Automatic multimodal UX improvement recommendations from LLM agent user simulations](https://arxiv.org/abs/2609.22971)

**<font color=#1a73e8>作者：</font>** Anu Chowdhury, Bin Wu, Hossein A. Rahmani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating user experience (UX) on live websites through user testing is expensive, subjective, and difficult to scale. LLM agents offer a promising route to automating UX testing by simulating realistic user behaviour. However, existing simulation approaches typically lack multimodality and require time-consuming manual review to extract actionable insights. We formalise UX improvement recommendation from simulation data as a structured natural language generation and ranking problem, and establish an evaluation protocol using expert annotation and LLM-as-a-Judge. We present AMUSER, a multimodal framework which simulates user behaviour and automatically generates prioritised UX improvement recommendations from resulting data. We evaluate AMUSER on commercial websites and show that its recommendations substantially outperform those from text-only simulation (NDCG@3 = 0.758 versus 0.359) at an 89% lower simulation cost. Our results suggest an asymmetric role of multimodality: visual access during simulation improves recommendations through richer traces, while providing visual inputs during recommendation generation can modestly degrade quality. We also discuss practical deployment lessons from applying AMUSER to commercial websites.

---


### 150. [Beyond Similarity: Coverage-Aware Prompt Selection for Time Series Forecasting with LLMs](https://arxiv.org/abs/2609.22977)

**<font color=#1a73e8>作者：</font>** Daeun Ji, Minkyoung Kim, Dongkuk Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Similarity-based retrieval is the dominant rule for conditioning large language models (LLMs) in in-context learning, retrieval-augmented generation, and prompt-based time series forecasting. The rule concentrates on near-duplicate candidates, an issue that has motivated diversity-aware retrieval but remains unexamined in other retrieval-conditioned pipelines. We study this issue using prompt-based time series forecasting as a test bed, where a learned prompt pool is retrieved by similarity. Dominant methods in this setting retrieve top-K entries by cosine similarity without redundancy control, producing a bias toward dominant temporal patterns while overlooking rare but informative events. We propose CASP-LLM, a coverage-aware semantic prompting framework that addresses this prompt selection bias by combining usage-tracking and saturating-gate techniques into a coverage regularizer that adds no learnable parameters. On six long-term benchmarks and the M4 short-term benchmark, CASP-LLM matches or improves on similarity-based LLM forecasters on most dataset-horizon settings, with the exceptions of Electricity, M4-Monthly, and the few-shot long-horizon setting. A controlled study locates the failure mode at the cross-batch usage level rather than per-retrieval redundancy: within-retrieval diversification such as MMR does not help, whereas regularizing anchor usage across training does.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-379](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
