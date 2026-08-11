# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 51. [From Single Chatbots to Governed Agent Ecosystems: An Agentic AI Pattern Catalogue and Orchestration Framework for Mission-Critical Hospital Information Management Systems](https://arxiv.org/abs/2608.07627)

**<font color=#1a73e8>作者：</font>** Manideep Dhar, Ritwik Singh, Sharat Chandra Kumar Manikonda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hospitals are racing to embed AI, while coping with the surge in adaptation of the technology in other industries, into the triage management, documentation, scheduling, and revenue-cycle workflows, yet most deployments remain as fragmented pilots that stall at the edge of production, exposing patients and institutions to operational fragility, ungoverned risk, and mounting technical debt. At the same time, the global AI-in-healthcare market is projected to exceed nearly USD 1 trillion by 2034, according to the report of Fortune Business Insights, amplifying the financial consequences of architectural missteps and failed scaling strategies. This research proposes a compliance-first Agentic AI pattern catalogue and orchestration framework, purposely built for HIMS, moving beyond the single LLM chatbots and towards a governed ecosystem of autonomous and semi-autonomous agents. The framework extends by adding (i) a taxonomy of Agentic roles, (ii) a formal risk-stratification model that maps each pattern to risk tiers, human-in-the-loop checkpoints, and governance hooks, and (iii) a unified orchestration runtime capable of coordinating multi-agent workflows across EHR/HIMS landscapes such as Epic, Cerner, and MEDITECH. Technically the framework combines vLLM-based inference, optimized paging memory, confidential computing, and MCP based on-premise deployment, enforcing end-to-end encryption and policy-as-code controls aligned with HIPAA, GDPR, the EU AI Act, India's DPDP and DISHA Acts, ISO 27001, ISO 27002, ISO 14971 and IEC 62304. We exhibit how the proposed architecture is capable and efficient to reduce the documentation time, integration effort, and AI pilot attrition while constricting the governance and auditability, offering hospital leaders and governing authorities an urgently needed blueprint to convert AI investment into sustainable clinical, operational, and financial ROI

---


### 52. [Adversarial Attacks on Deep OCR Systems](https://arxiv.org/abs/2608.07636)

**<font color=#1a73e8>作者：</font>** Wenbo Sun, Hongzong LI, Yanyun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep-OCR (DeepSeek-OCR) advances document recognition by treating the visual modality as an optical compression medium, enabling long-context OCR at low token cost. However, its increased complexity may introduce new security vulnerabilities. In this paper, we present, to the best of our knowledge, the first pure black-box adversarial attack against a generative OCR vision-language model, where only the decoded string can be queried and no gradients, logits, or model internals are available. We recast the attack as a zeroth-order optimization problem driven by a bounded scalar loss defined directly on the string output via sequence similarity, and estimate the gradient with a random-direction finite-difference scheme whose query cost is independent of the image dimension. An Adam update with ell_infinity projection yields imperceptible perturbations for both untargeted and targeted objectives. Pilot experiments on Deep-OCR validate the string-only attack and evaluation pipeline and expose severe qualitative decoder failures, including repetition, truncation, and prompt leakage. They also show that controlled targeted rewriting remains substantially harder than untargeted degradation; we avoid claiming targeted success until the pre-registered evaluation is complete.

---


### 53. [Agent-MD: Selective LLM Intervention with Event-Driven Escalation for Stateful GCMC--MD Campaigns](https://arxiv.org/abs/2608.07637)

**<font color=#1a73e8>作者：</font>** Yijie Wang, Zhen-Yu Yin, Zhenheng Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running molecular simulation campaigns require repeated continuation from saved states, provenance-aware progression, adaptive assessment, and occasional interpretation of workflow conditions that cannot be resolved safely by fixed rules. Here, we present Agent-MD, a framework that places large language model (LLM) reasoning selectively at campaign construction and event-triggered review, while routine simulation, analysis, continuation, archiving, and state progression are handled by a persistent rule-based campaign agent using approved policies and explicit state records. Agent-MD was demonstrated in a grand canonical Monte Carlo-molecular dynamics (GCMC-MD) water-vapor desorption campaign comprising five montmorillonite systems and three sequential relative-humidity states (RH = 0.9-0.3-0.1). Across 15 system-RH states, the workflow completed 120 segmented simulation cycles with state-specific sampling lengths and provenance-aware restart inheritance. Routine production required no live reasoning-agent invocation, while one state reached a review boundary; two preserved incidents were subsequently evaluated through blinded reasoning-agent replay, which identified the underlying workflow problems and recommended appropriate follow-up actions. The simulations also revealed distinct composition-dependent low-RH responses, with Ca-bearing montmorillonite retaining more interlayer water and maintaining a larger basal spacing than the Na- and K-bearing systems, while the highest-charge Na system retained more residual water under dry conditions. These results demonstrate that long-running scientific workflows need not place every operation inside an LLM reasoning loop: selective reasoning can instead be combined with deterministic execution, structured evidence, and validated control handoffs to provide reproducible and auditable agent-assisted molecular simulation.

---


### 54. [SkillConsist: Detecting Inconsistencies in Agent Skills via Bidirectional Graph Alignment](https://arxiv.org/abs/2608.07639)

**<font color=#1a73e8>作者：</font>** Chaofan Meng, Yuhang Zheng, Yingnan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent Skills provide reusable capabilities to LLM agents. Agent Skill inconsistencies can expose undisclosed dangerous behavior or cause wrong Skill selection. Recent Agent Skill research has increasingly examined Agent Skill consistency detection. Existing methods evaluate behaviors or security-property graphs against predefined categories or declared scopes. More recently, PL-HCL uses an LLM-based model to learn consistency across metadata, instructions, and resources. However, declaration and implementation behavior can be mixed across text and code, and a concise declaration can correspond to multiple connected implementation steps. We present SkillConsist to address both challenges. An LLM separates declaration and implementation content into behavior records on the implementation and declaration sides, while static analysis supplements implementation records. These records form declaration and implementation behavior graphs, respectively. Starting from a behavior record on either side, bidirectional graph alignment searches the other graph for a candidate subgraph and expands it along behavior relations until it completely expresses the source-side behavior. Graph differencing identifies conflicts between aligned subgraphs and outputs the detection results. We construct a 633-Skill benchmark from ClawHub's 500 most-downloaded public Skills and 133 Skill-Inject packages. The benchmark contains 319 inconsistent and 314 consistent Skills and 442 localized inconsistency annotations. On this benchmark, SkillConsist achieves 86.85% precision, 89.03% recall, and 87.93% F1 for package-level detection, improving F1 over the best baseline by 20.43 percentage points. For localization, it achieves 67.60% precision, 58.14% recall, and 62.52% F1.

---


### 55. [SurveyReview: A Reviewer-Aligned Benchmark for Survey Evaluators](https://arxiv.org/abs/2608.07641)

**<font color=#1a73e8>作者：</font>** Yuheng Zhang, Yuanchun Wang, Fanjin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models has transformed survey writing from a months-long manual effort into an automated process. As generation scales, reliable evaluation becomes the bottleneck, and LLMs are increasingly used as survey evaluators. However, existing approaches largely rely on off-the-shelf LLM-as-a-judge methods without systematic alignment to human reviewers, and there remains a lack of systematic frameworks for quantifying alignment with human reviewers. To address this gap, we propose SurveyReview, a reviewer-aligned, multi-dimensional benchmark and dataset for survey evaluation. We collect and annotate 675 survey papers with 1,630 review reports. We structure authentic peer-review reports by converting free-form comments into four-dimensional scores (Readability, Criticalness, Comprehensiveness, Structure) paired with supporting rationales. We further release standardized train/test splits and an evaluation protocol to measure alignment between automatic evaluators and human reviewers. To validate the benchmark, we develop SurveyAlign, a strong baseline evaluator by fine-tuning Qwen3-32B with LoRA on our annotated data, augmented with external knowledge for knowledge-intensive dimensions. On the test set, SurveyAlign substantially improves reviewer alignment over prompt-based judging with GPT-5.2, reducing average MSE from 2.28 to 1.38 and MAE from 1.15 to 0.69 across all four dimensions. Our contributions are twofold: (1) we establish the first multi-dimensional, reviewer-aligned dataset with a reproducible evaluation framework for survey reviewing; (2) we develop a strong baseline evaluator that substantially improves alignment with human reviewers, providing a competitive reference for future research. Our code and data are available at this https URL

---


### 56. [Contextual Value Alignment via Multilayer Combinatorial Fusion](https://arxiv.org/abs/2608.07642)

**<font color=#1a73e8>作者：</font>** Yuanhong Wu, Djallel Bouneffouf, D. Frank Hsu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning large language models (LLMs) with human values remains a major challenge, especially for trustworthy AI. While existing approaches such as RLHF, CAI, and their variants have achieved promising results, they often rely on a single-agent framework and a unified reward system. This limits their ability to capture ethical pluralism, adapt to diverse moral contexts, and reflect the dynamics of multi-agent moral reasoning.
In this work, we propose a framework that utilizes multilayer combinatorial fusion for contextual value alignment (MCF-CVA). At the first layer of the framework, it instantiates multiple moral agents, each fine-tuned to represent a distinctive value. Their outputs are then expanded combinatorially using both score- and rank-combinations as well as average and weighted aggregations. These combined models are then reduced to the same number of initial moral agents. This expansion and reduction (EAR) process continues for multi-layers until a stopping criterion is reached.
The MCF-CVA framework leverages cognitive diversity between agents to mitigate conflicts and redundancies across multiple agents, producing responses that better reflect contextual human values. The framework using the EAR algorithm is performed on the dual architecture of Euclidean score space and Kemeny rank space. Empirical evaluations demonstrated that the proposed framework outperforms single-agent baselines, multi-agent single-layer results, and previous aggregation approaches on standard metrics, showing that the MCF-CVA framework provides a robust and effective mechanism for advancing contextual value alignment in LLMs.

---


### 57. [Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution](https://arxiv.org/abs/2608.07645)

**<font color=#1a73e8>作者：</font>** Changzhi Liu, Yilun Liu, Sikuan Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving coding agents that iteratively rewrite their own source code have demonstrated impressive performance on coding tasks. However, existing solutions generally derive self-modification from a single failure trajectory at a time, overlooking rich comparative signals available in the agent's expanding archive of past attempts. According to Mendelian principles of controlled inheritance, we introduce Mendel Gödel Machine (MGM). In addition to the general single-trajectory clonal mutation, MGM includes two new types of self-modification that better utilizes evidences accumulated: the reaction-norm mutation edits an agent based on its trajectories on multiple tasks simultaneously, and the cross-lineage hybridization edits an agent using the trajectory of a reference agent from another lineage on the same task. Under an additive fitness landscape model, we prove theoretically and demonstrate via controlled surrogate simulation that the new strategies facilitate a faster and better convergence over single-trajectory baselines. Experiments on SWE-bench and Polyglot confirm MGM's consistent improvement in performance, efficiency, and generalizability.

---


### 58. [An Agentic AI Framework Overcomes Fundamental Limitations of Large Language Models for Glaucoma Detection from Fundus Photography](https://arxiv.org/abs/2608.07651)

**<font color=#1a73e8>作者：</font>** Jalil Jalili, Hossein Taghizad, Anuwat Jiravarnsirikul 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise in medical image interpretation but suffer from hallucination, limited accuracy, and run-to-run inconsistency. We developed and validated an agentic AI framework integrating LLMs with specialized deep learning tools for glaucoma detection from fundus photography. The workflow had three steps: (1) LLM initial assessment; (2) function calling to invoke specialized tools for image quality (QAModel, FundaQ-8), glaucoma classification (SwinV2-Tiny), and optic disc/cup segmentation (SegFormer-B0); and (3) LLM reflection integrating the initial impression with tool outputs. Two LLMs (Gemini 2.5 Flash, GPT-5.4 mini) were evaluated on two public datasets (ORIGA, n=100; RIM-ONE-v3, n=100) under uncropped and cropped fields of view; all images were independently graded by a masked fellowship-trained glaucoma specialist. The agentic workflow improved classification accuracy by 16 to 47 percentage points across all conditions, reaching within 6 points of the specialist; on RIM-ONE-v3 the best configurations matched the specialist accuracy of 88%. LLM-alone approaches failed in two ways: GPT-5.4 mini showed positive bias (sensitivity 95-100%, specificity 0-5%), while Gemini 2.5 Flash varied stochastically between runs; the agentic workflow corrected both. Cup-to-disc ratio error fell 15-50% (MAE 0.156-0.228 to 0.104-0.132), and correlation with specialist grading rose from weak (r=0.12-0.39) to moderate-strong (r=0.59-0.84). Run-to-run consistency rose from near-random (kappa as low as -0.01) to near-perfect (kappa up to 0.96). Integrating LLMs with specialized tools addressed key limitations of LLM-alone approaches, including over-diagnosis and run-to-run variability. Gains held for both LLMs, suggesting generalizability across backbones, and may signal a shift from monolithic models toward orchestrated multi-agent systems in medical AI.

---


### 59. [Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding](https://arxiv.org/abs/2608.07663)

**<font color=#1a73e8>作者：</font>** Yeeun Choi, Youngbeom Yoo, Joon-Young Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When videos extend from hours to days, directly processing them end-to-end becomes impractical for current Multi-modal Large Language Models (MLLMs). This ultra-long setting necessitates a two-stage paradigm: query-agnostic memory construction followed by retrieval-based inference. Prior work invests in complex memory construction to pre-model high-level relations in videos, despite not knowing the downstream query at build time. We instead prioritize high-recall retrievability during memory building, and defer query-specific, high-level relation composition to inference time. To this end, we propose MERIT(Multi-key Episodic Retrieval with Inference-time Temporal expansion), a simple yet effective agentic framework for ultra-long video understanding. First, we formulate an episodic multi-key representation that enables precise retrieval of fine-grained memories through a simple key-matching mechanism. Second, we introduce a neighbor filtering mechanism to capture broader semantic context without the massive computational overhead of global memory construction. This is achieved by expanding the temporal scope exclusively around the retrieved segments at inference time. By leveraging simple key-matching with this on-demand temporal expansion, MERIT achieves state-of-the-art performance across three long-video benchmarks: EgoLifeQA, LVBench, and Video-MME (Long).

---


### 60. [IntelliAudit: Using Large Language Models to Evaluate Audit Controls](https://arxiv.org/abs/2608.07688)

**<font color=#1a73e8>作者：</font>** Allison Wilson, Sina Moradi Sabet, Diar Shakimov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> IT audits require auditors to judge whether heterogeneous organizational evidence satisfies semantic security and compliance controls. This judgment is difficult to automate because relevant evidence is distributed across policies, records, spreadsheets, and operational artifacts, and because audit conclusions depend on evidentiary sufficiency rather than keyword matching. We present IntelliAudit, a retrieval-grounded multi-agent system for IT audit evidence evaluation. Given a control and an evidence corpus, IntelliAudit retrieves relevant artifacts, generates an evidence-grounded assessment, challenges adverse findings, adjudicates disagreements, and produces an auditor-facing recommendation with cited evidence, rationale, missing-evidence analysis, and remediation guidance. We instantiate IntelliAudit on ISO/IEC 27001 and evaluate it across multiple simulated organizations using expert auditor review and audit-readiness user feedback. The evaluation shows that IntelliAudit can support control interpretation, evidence-grounded reasoning, and audit-preparation workflows, while also revealing the importance of human oversight for calibrating sufficiency judgments and correcting overly permissive recommendations. These results suggest that retrieval-grounded multi-agent systems can assist audit evidence review, but should remain decision-support tools rather than autonomous certification systems.

---


### 61. [CosmosAlign: Adapting a World Foundation Model for Generative Traffic Video Forecasting](https://arxiv.org/abs/2608.07693)

**<font color=#1a73e8>作者：</font>** Quang Minh Dinh, Tuan Kiet Doan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative traffic video forecasting aims to synthesize long-horizon, temporally coherent future videos of traffic scenes from a short observation history and textual descriptions. In this paper, we present CosmosAlign, a generative traffic video forecasting framework built upon the pretrained Cosmos3-Nano world foundation model. Our approach is motivated by the observation that successfully adapting large pretrained world models to downstream forecasting tasks depends primarily on distribution alignment rather than increased model capacity. To this end, we propose a two-stage LoRA adaptation strategy that first aligns the conditioning-mode distribution with the target forecasting task, and then aligns the training captions with the model's native structured prompting interface through an LLM-based re-captioning pipeline. During inference, we further improve prediction quality using a fully training-free procedure consisting of consensus-based medoid sample selection and motion-adaptive blending of static scene regions. CosmosAlign achieves a final score of 76.49 on the AI City Challenge 2026 Track 5 benchmark, ranking first on the final leaderboard. Our code is publicly available at this https URL.

---


### 62. [Towards Researcher Agents for Knowledge-Graph Question Answering](https://arxiv.org/abs/2608.07700)

**<font color=#1a73e8>作者：</font>** Tommaso Soru, Abdulsobur Oyewale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Translating a natural-language question into a SPARQL query that can be executed against a large knowledge graph requires resolving lexical ambiguity, grounding surface terms in the target ontology, and producing graph patterns that are both syntactically valid and semantically faithful. We present an agentic text-to-SPARQL system that goes one step beyond static tool-using agents: a researcher agent that, after each round of inference on a validation set, proposes and tests changes to its own prompts, rules, and tool-orchestration code. We instantiate the loop on DBpedia, evolve nine successive versions of the agent driven by a low-cost reasoning model, and deploy the best-performing configuration with two stronger backbone models. The study yields three observations: (i) self-improvement converges quickly and then achieves 0.22 overall accuracy on the 2025 DBpedia validation set; (ii) the bottleneck is consistently in basic-graph-pattern predicate selection, not in SPARQL syntax or modifiers; and (iii) several benchmark items appear to penalise correct queries due to property ambiguity in DBpedia, suggesting that future Text-to-SPARQL benchmarks should be scored using a combination of machine translation and information retrieval metrics.

---


### 63. [Evaluating Dedicated Monolingual and Joint Multilingual Causal Models for Dravidian Languages](https://arxiv.org/abs/2608.07727)

**<font color=#1a73e8>作者：</font>** Venkata Naga Sai Vishnu Rohit Pulipaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dravidian languages, mainly Tamil, Telugu, Kannada, and Malayalam make up only a small part of the data used to train multilingual language models, so it's not clear how much per-language ability these models actually keep. I have trained five GPT-2 architecture models from scratch to compare four monolingual models (one each for Tamil, Telugu, Kannada, and Malayalam, each with its own 32K-vocabulary subword tokenizer) against one multilingual model sharing a 64K-vocabulary subword tokenizer across all four languages. All the 5 models are trained on cleaned CC-100, Wikipedia, and Samanantar data. I have tested the models on perplexity, bits-per-byte, tokenizer efficiency, and fine-tuning results which are compared against mGPT. The monolingual models outperform mGPT on sentiment classification and named entity recognition, and their tokenizers proved more efficient than the shared multilingual model across all the languages tested.

---


### 64. [BRUCE: Benchmarking Robustness Under Corruption Escalation for Scientific Vision-Language Reasoning](https://arxiv.org/abs/2608.07742)

**<font color=#1a73e8>作者：</font>** Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual-language models (VLMs) frequently struggle with robustness issues in real-world situations due to low- or varying-quality input images. In this paper, we aim at analyzing VLMs' robustness by applying perturbations and distortions to the input images, such as blur or low contrast. Toward this goal, we propose BRUCE (Benchmarking Robustness Under Corruption Escalation, a multimodal reasoning fragility framework for scientific vision-language reasoning.
State-of-the-art evaluation frameworks/studies primarily focus on clean-task accuracy and rarely analyze how reasoning stability degrades across robustness dimensions. Besides varying over a wide-range of input perturbations, BRUCE employs two novel metrics -- Robustness Corruption Index (RCI) and Traversal-RCI (T-RCI) -- to quantify how rapidly multimodal reasoning performance deteriorates in VLMs as visual corruption severity increases under progressive perturbation scaling. We evaluate BRUCE across chemistry and mathematical reasoning tasks for multiple datasets, while analyzing corruption-induced prediction failures in terms of four high-level reasoning domains: OCR-dependent reasoning, spatial reasoning, symbolic reasoning, and semantic failures, with each containing fine-grained corruption specific failure subtypes, thereby enabling an interpretable failure analysis.

---


### 65. [Who Verifies the Benchmark? Decentralizing Trust in Large Language Model Evaluation](https://arxiv.org/abs/2608.07762)

**<font color=#1a73e8>作者：</font>** Sahil Pardasani, Madhusudan Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM benchmarks can build an organization's reputation and attract customers, but only when results are transparent and verifiable. Unverified claims that DeepSeek R1 outperformed OpenAI's o1 contributed to market panic on January 27, 2025, when Nvidia lost USD589 billion in market value. Yet vendor benchmarks often depend on an honor system. Academic reassessments and independent leaderboards have found undisclosed changes to proprietary models, contaminated training data, and selective reporting. LLM-as-a-judge methods scale evaluation by reducing human review. Studies, however, suggest that judges may show identity-aware bias, scoring an answer according to its source model rather than its quality. This bias has not been fully measured or corrected across politically sensitive, reasoning-intensive, and preference-based tasks. We examine this problem using seven verifier models: GPT-OSS 120B, Llama 3.3 70B, GLM 5.1, Qwen3 32B, DeepSeek V4 Pro, Mistral Large3, and Sarvam M. They score anonymous and identity-disclosed responses from three primary models on 58 factual, reasoning, political, and preference-based questions. Identity disclosure slightly raises scores for factual questions, moderately affects stress-reasoning tasks, and causes large changes for geopolitically sensitive topics. Notable results include GLM5.1 (+7.00 points, p = 0.0249) and Llama 3.3 70B (+1.56 points, p = 0.00). We also introduce a blockchain-based commit-reveal protocol using Autonomous Economic Agents on an Ethereum-compatible ledger. In Phase 1, each judge records a one-way hash of its score and a secret salt before candidate identities are revealed. In Phase 2, the identity and raw score are disclosed and verified on-chain. This creates a tamper-evident audit trail that separates blind evaluation from post-hoc claims and reduces the verification burden on independent researchers and leaderboard operators.

---


### 66. [Jako Tako or Fluent? Presenting PoVisLE: A Polish Vision-Language Evaluation](https://arxiv.org/abs/2608.07763)

**<font color=#1a73e8>作者：</font>** Anna Kołos, Grzegorz Statkiewicz, Karolina Seweryn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance on tasks such as image captioning, visual question answering, and image-to-text generation. However, they are predominantly trained on English-centric data, which limits their ability to handle culturally grounded visual understanding and leads to failures in interpreting region-specific meanings, symbolic content, and context-dependent visual cues. Existing benchmarks for cultural competence are often template-driven and focused on surface-level recognition, making them insufficient for evaluating deeper linguistic and pragmatic understanding in culturally situated settings. We introduce PoVisLE, a monocultural vision-language benchmark for Polish designed to evaluate culturally grounded multimodal understanding under a grounded evaluation paradigm, where language is interpreted in interaction with visual context. The dataset contains 1,117 images and 2,366 manually annotated VQA pairs. Overall, our dataset provides a controlled and challenging resource for assessing culturally grounded vision-language understanding beyond surface-level recognition.

---


### 67. [Can AI Write Compliant Code, and to What Extent? Evaluating SOC 2 Compliance of Claude Fable 5, Claude Opus 4.8, and Claude Opus 5 Across Four Use Cases](https://arxiv.org/abs/2608.07776)

**<font color=#1a73e8>作者：</font>** Iccha Sethi, Herman Errico  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software teams now delegate production code to language models, including code that provisions storage, handles credentials, and stores regulated data, so we asked whether a model applies the controls a SOC~2 program expects (encryption, restricted access, logging, retention) when nobody mentions security, and how much one sentence naming the standard changes the answer. We tested three frontier models (Claude Fable~5, Opus~4.8, and Opus~5) across four use cases (an S3 CLI, an authentication service, an RDS Terraform module, and a file-upload handler holding personal data), each generated once from a neutral task statement and once with a single SOC~2 sentence added, scoring all 24 outputs against binary rubrics mapped to specific Trust Services Criteria and hand-verifying every failure and flagged act. Unprompted conformance ran from 47\% to 88\% and tracked whether a control is part of how the code is normally written, so password hashing and \texttt{storage\_encrypted} appear unasked while S3 hardening calls, retention, and MFA hooks do not. The neutral prompt also shipped real vulnerabilities, including a reachable Werkzeug debugger allowing remote code execution, an unauthenticated download, and an endpoint returning every stored name and email, all scored clean by our first checklist, with a fourth defect passing because its value was computed by a conditional. One SOC~2 sentence moved every case to 86--100\%, worth 23 to 50 points, and removed every insecure construction, though controls outside the model's conception of the task survived it, including MFA hooks, cookie flags, and account lifecycle. Model choice mattered least, with same-generation models within one rubric item across all eight cells, and the pattern-matching scorer proved unreliable, disagreeing with semantic grading on 27 of 216 judgments and passing a real defect, so it needs replacing with semantic checks.

---


### 68. [Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space](https://arxiv.org/abs/2608.07786)

**<font color=#1a73e8>作者：</font>** Yiwei Chen, Bingqi Shang, Sijia Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) are increasingly developed through complex, multi-stage pipelines, leading to intricate lineage relationships that reflect model origin, ownership, and evolution. Understanding these relationships is important for model provenance, governance, and supply-chain integrity. In this work, we investigate the notion of LLM "biometrics" (analogous to human biometrics) to ask whether LLMs exhibit intrinsic fingerprints in weight space alone, without access to input data, that reveal their origin and lineage. We formulate this as a lineage discrimination problem, distinguishing among independent-origin, same-series, and shared-base models. To characterize these relationships, we propose a unified geometric fingerprinting framework that analyzes weight matrices from two complementary perspectives: (i) spectral energy, captured by singular value distributions to encode global magnitude patterns, and (ii) subspace alignment, quantified via subspace deviations to capture directional geometry. Our analysis uncovers a clear hierarchy of structural similarity in weight space: spectral energy reliably distinguishes independently trained models and different model families, while subspace alignment enables fine-grained discrimination among closely related models, including variations in dataset scale and post-training procedures. Extensive experiments on over 110 diverse open-weight LLM pairs demonstrate that weight-space geometry provides a robust and interpretable signal for model lineage, enabling coarse-grained regime separation and fine-grained discrimination within shared-base models.

---


### 69. [CliniCARE-Bench: Clinical Calibrated Audit of Medical Reasoning in EHR](https://arxiv.org/abs/2608.07796)

**<font color=#1a73e8>作者：</font>** Veronica Chatrath, Bryan Zhu, George Pu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models perform strongly on medical knowledge benchmarks, but reliable clinical deployment requires agents to conduct defensible investigations over heterogeneous, longitudinal records: determining what evidence is needed, retrieving and reconciling structured and free-text data, grounding conclusions in verifiable evidence, and deferring cases that cannot be resolved reliably. We introduce CliniCARE-Bench (Clinical Calibrated Audit of Medical Reasoning in EHR), a benchmark for retrospective clinical audit: 25 clinician-validated scenarios instantiated as 750 patient-specific cases over real-patient-derived MIMIC-IV data. Systems investigate each case through a governed, logged tool environment for record retrieval, computation, and policy access, and return one of four verdicts---Yes, No, Indeterminate: Lack of Data, or Indeterminate: Medically Ambiguous---the last two separating missing evidence from residual medical ambiguity. Beyond verdict accuracy, we score patient-evidence and policy grounding, process adherence, calibrated abstention, reliability, and efficiency against case-level reference verdicts produced by independent multi-model adjudication and calibrated against Clinical Board review. Every retrieval, computation, and report is replayable, so the investigation trace is inspectable and scorable. To our knowledge, CliniCARE-Bench is the first deployment-oriented clinical-agent benchmark to jointly evaluate real longitudinal EHR investigation, claim-level evidence grounding, governing-policy use, process adherence, and calibrated abstention within a common patient-level adjudication framework. Across 16 agentic systems, four-way accuracy spans 65.3-76.1%, but raw accuracy overstates investigation quality. Defect-free accuracy, which credits a verdict only when correct and free of prohibited shortcuts, is 4.8-14.8 points lower and reorders the leaderboard.

---


### 70. [When the Judge Should Not Decide: Evidence-Locked, Non-Compensatory Selection Bounds LLM-Judge Failure in Reasoning Pipelines](https://arxiv.org/abs/2608.07813)

**<font color=#1a73e8>作者：</font>** Yiyao Zhang, Diksha Goel, Hussain Ahmad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM judge deployed inside a reasoning pipeline does not merely measure quality, it decides which answer ships. We show that the cost of that decision depends less on judge accuracy than on the decision rule the judge is embedded in. On frozen candidate pools from four GRPO policies, an unconstrained scalar DeepSeek-R1-7B judge buys almost nothing over answer-level majority vote (+1.0 pp on 500 GSM8K questions, +0.34 EM on 300 HotpotQA questions), and on a frozen-rule 30-question confirmation split it is 10 points worse than majority, a judge that destroys accuracy while scoring candidates confidently. We then subordinate the same judge to Evidence-Locked Derive-Gate-Repair (EL-DGR), a task-adaptive non-compensatory rule under which a judge preference may override evidence-supported consensus only with an extractive evidence certificate, and a repair only when neither alternative is certified and the repair is. With no change to the judge, the candidates, or the budget, EL-DGR reaches 58.2% on GSM8K (vs. 56.8% judge, 55.8% majority, 55.4% first candidate) and 17.33 EM / 25.46 F1 on HotpotQA (vs. 15.67/23.49, 15.33/23.19, 15.33/22.97), improving on first-candidate GRPO by +2.8 pp (exact McNemar p=0.0026) and +2.00 EM (p=0.070, borderline). A decision audit shows why: EL-DGR overturns consensus on only 8 of 30 pilot questions and never converts a correct consensus into an incorrect answer. We also report what did not work: the same seven-channel decomposition used as a step-level gated training reward is null, and corrected channel-drop ablations show no channel is individually necessary (p=1.0 throughout). The practitioner-facing finding is negative about judges and positive about admissibility, bound the judge's blast radius rather than trying to make it accurate.

---


### 71. [Shape Mutating Expert Compression:LorExperts and BTExperts](https://arxiv.org/abs/2608.07814)

**<font color=#1a73e8>作者：</font>** Inesh Chakrabarti, Sourjya Roy, Bowen Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models deliver high capacity at low per-token compute, but deploying them cheaply requires compressing their many expert weight matrices. Expert pruning (e.g., REAP) and merging reduce cost but sacrifice accuracy and require retraining the router; low-rank delta decomposition of experts (e.g., D^2-MoE) preserves all experts and the router, but degrades sharply as the expert count grows because a single shared component cannot approximate many near-orthogonal experts.
Because MoE expert weights are near-orthogonal, a single shared component (as in prior delta decomposition) scales poorly with the expert count; we show that experts nonetheless organize into functional co-activation communities that are decoupled from weight similarity. Building on this, we introduce LorExperts, a router-preserving compression method that clusters experts, keeps one full-precision dominant per cluster, and represents the remaining members as low-rank corrections to their local dominant. LorExperts retains all experts and the original router (no router retraining). At ~50% expert compression on Qwen3-30B-A3B and Gemma-4-26B-A4B, LorExperts preserves downstream accuracy and perplexity better than the baselines on most of the tasks; the margin over D^2-MoE grows with expert count E. We further give a reconstruction fine-tuning procedure for LorExperts, and BTExperts, a tree organization of dominants and corrections that enables inference-time amortization of shared computation.

---


### 72. [From token probabilities to calibrated confidence: An empirical study of mathematical question answering](https://arxiv.org/abs/2608.07827)

**<font color=#1a73e8>作者：</font>** Avery Ma, Lorne Schell, Vin Bhaskara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Confidence estimation for large language models (LLMs) aims to estimate the probability that a generated answer is correct, while calibration aligns these estimates with empirical accuracy. Prior work has shown that token probabilities are often overconfident, we investigate whether these readily available signals can nevertheless provide well-calibrated confidence estimation for mathematical question answering. We compare single-pass estimators, which reuse token probabilities from the original generation, with multi-pass estimators, which obtain additional confidence signals through verification or stochastic forward passes. While individual token probabilities can be highly saturated, we find that aggregating token probabilities over the full sequence captures small but consistent differences between correct and incorrect generations, yielding more informative confidence estimates. Multi-pass methods can yield calibrated confidence estimates. We study two such approaches: self-verification through re-prompting, including a lower-cost in-situ variant, and Monte Carlo Dropout, which derives confidence from variation across stochastic forward passes. We further evaluate two post-hoc calibration methods, Platt scaling and isotonic regression, both of which substantially reduce in-domain calibration error. However, their data efficiency varies with dataset difficulty, and the calibration mappings often transfer asymmetrically across datasets and models.

---


### 73. [Counterfactual Benchmarking and Training for Factuality Consistency and Order-Robust Grounded Reasoning in LLMs over Heterogeneous Knowledge](https://arxiv.org/abs/2608.07838)

**<font color=#1a73e8>作者：</font>** Shibo Chu, Yuze Liu, Tiehua Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have increasingly supported response generation grounded in user-provided knowledge spanning heterogeneous structures. However, existing benchmarks provide limited assessment of whether LLMs can faithfully perform multi-hop reasoning chains across such knowledge contexts while remaining robust to variations in their input order. We introduce TKFQA, a factuality consistency benchmark comprising 10,130 question-answering (QA) pairs grounded in tables, texts, and knowledge graphs (KGs). Each example is constructed from an explicit counterfactual reasoning chain, enabling the joint evaluation of answer correctness, reasoning-chain accuracy, and robustness to different input-order. An extensive evaluation of 14 open- and closed-source LLMs reveals that state-of-the-art models exhibit limited reasoning-chain accuracy and remain sensitive to variations in the input order of heterogeneous knowledge contexts. To address these limitations, we propose ORLF, an LLM-agnostic training framework that models cross-context topological relations through knowledge-specific latent vectors. ORLF integrates context-wise position encoding, a latent-bridge attention mask, and topological knowledge bias to preserve knowledge-specific bias and encode topological semantics. Experiments across four LLM backbones show that ORLF outperforms competitive training-free and LoRA-based baselines, improving average Exact Match and Reasoning-Chain Accuracy by 2.15% and 4.29%, respectively, while reducing order-induced performance standard deviation by 0.04% to 3.01%.

---


### 74. ["Many Are My Names": The Anatomy of the Assistant and Its Personas via Sparse Autoencoders](https://arxiv.org/abs/2608.07852)

**<font color=#1a73e8>作者：</font>** Adelaide Danilov, Aria Nourbakhsh, Oleksandr Marchenko Breneur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How a language model internally represents who is speaking, the Assistant, an assigned roleplay persona, or a narrated story character, remains underexplored. We study speaker representations using a dataset of user-expressed emotional text and corresponding model responses. We decompose three generation settings (Assistant, Roleplay, and Story) into sparse autoencoder features extracted at turn-boundary and pronoun-token positions and selected through a filtering pipeline for different depths. We characterize each surviving feature through its steering effects and activation distribution. Our main finding is that the Assistant and roleplay personas are not independent alternatives: personas retain the Assistant-associated feature core while progressively differentiating from it across layers, starting from operational machinery towards behavioral and stylistic features. Meanwhile, generated story characters lack the Assistant-associated core. Both Story and Roleplay can be distinguished from the Assistant with Immersive Simulation Mode. However, the Assistant can sometimes enter or slowly drift into it even in the default setting.

---


### 75. [CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents](https://arxiv.org/abs/2608.07855)

**<font color=#1a73e8>作者：</font>** Weizhong Huang, Jinchao Zhang, Xiawu Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn Reasoning-and-Acting (ReAct) agents accumulate growing trajectories of reasoning, tool calls, and observations. Their key-value (KV) caches grow accordingly, increasing memory use and attention cost during model inference. Existing KV cache compression methods reduce these costs by evicting states with low attention scores. However, low attention in the current turn does not imply future irrelevance, as temporarily inactive information may become important later. Snapshot-based eviction methods therefore do not explicitly distinguish temporarily dormant information from information that appears to have completed its role. In this paper, we present CommitKV, which identifies KV lifecycles through commit transitions. Specifically, CommitKV first divides completed agent events into token pages and compares each eligible page's deletion effect before a tool-call commit and after the commit's returned observation has been incorporated. Based on these paired measurements, CommitKV distinguishes dormant pages from high-to-low completion candidates. It then applies a greedy joint test, accepting candidates for retirement only when their combined post-commit effect remains bounded. Finally, at a later compression checkpoint, accepted pages are excluded, a bounded set of pages awaiting post-commit measurement is protected, and the remaining KV states are retained within the cache budget using the same token indices for keys, values, and absolute positions. These mechanisms ensure that CommitKV can distinguish dormant information from information that has completed its observed role and can be safely removed. Experiments on various benchmarks show that CommitKV reduces agent memory use, accelerates end-to-end inference, and achieves higher accuracy than existing KV cache compression methods.

---


### 76. [How Much Does It Cost to Answer My Question? Benchmarking Cloud VLM-based VQA Systems](https://arxiv.org/abs/2608.07861)

**<font color=#1a73e8>作者：</font>** Henri Vanhuynegem, Weitao Xu, Yiran Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are becoming a practical backend for mobile visual question answering (VQA) systems, enabling smartphones and smart glasses to answer users' questions about the physical world. Since modern VLMs remain difficult to run on mobile and edge devices, VQA systems increasingly offload inference to cloud-based VLMs. This gives mobile devices access to stronger computation, but it also makes visual input preparation a key system variable: how the image is prepared before offloading affects not only answer quality but also payload size, token cost, and system latency. Proprietary APIs expose little control over model internals or serving behavior, leaving client-side preprocessing as the main practical optimization space for downstream developers. Many such techniques have been proposed for visual offloading, yet their cost-quality impact on commercial cloud VLMs has never been studied. To fill this gap, we present VQABench, the first systematic benchmark that treats client-side input preprocessing as a controlled variable for cloud-VLM-based VQA. We evaluate 12 preprocessing techniques across three VQA datasets and four commercial VLMs from three providers, totaling 95,168 API calls. Our results show that preprocessing is not universally beneficial: its effectiveness depends on the target model, API paradigm, provider token-accounting rule, and task formulation. A poorly selected preprocessing strategy can increase deployment cost or latency while degrading answer accuracy. Overall, our benchmark clarifies when preprocessing helps, when it fails, and why, providing insights to guide future research and real-world deployment of VQA systems.

---


### 77. [SurakshaEval: An Indic Safety Benchmark for Multilingual LLMs](https://arxiv.org/abs/2608.07862)

**<font color=#1a73e8>作者：</font>** Debopriyo Banerjee, Kapil Rajesh Kavitha, Angana Borah 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing safety evaluation datasets for large language models (LLMs) predominantly focus on English and Western contexts, often overlooking the linguistic diversity and culturally grounded safety risks present in other languages. To address this gap, we introduce SurakshaEval, a novel safety benchmark composed of human-written prompts spanning real-world scenarios, explicitly designed for ten major Indian languages - Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Punjabi, Tamil, and Telugu, along with English. SurakshaEval includes both generic prompts common across India and region- and language-specific prompts that capture localized sociocultural sensitivities. We benchmark a broad range of state-of-the-art LLMs on SurakshaEval, establish baseline safety performance, and identify recurring failure modes, including over-refusal, missed detection of implicit bias, and insufficient contextual awareness in regionally sensitive settings. Our results show that even strong multilingual LLMs struggle to reliably meet nuanced safety requirements when operating in Indic languages, particularly in native scripts. These findings highlight the urgent need for safety evaluation frameworks that incorporate region-specific data and structured assessment protocols, enabling the development and deployment of AI systems that operate securely, ethically, and in alignment with diverse societal values. Our code and data are available at this https URL. Warning: This paper contains text that may be offensive or unsafe.

---


### 78. [LHSDet: High-Resolution AI-Generated Image Detection via Visual Question Answering](https://arxiv.org/abs/2608.07863)

**<font color=#1a73e8>作者：</font>** Qian Yao, Jun-Jie Huang, Yongjun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by advances in diffusion models and autoregressive models, the fidelity and resolution of AI-generated images now rival those of real images. However, existing AI-generated image detection methods often downsample the images, inevitably overlooking critical low-level texture details in high-resolution AI-generated images, therefore limiting their detection performance. In addition, the ceaseless emergence of unknown generative models makes large-scale pre-training datasets inaccessible. To address these challenges, we propose a novel high-resolution AI-generated image detector, termed LHSDet. Specifically, we formulate the AI-generated image detection task as a Visual Question Answering problem, leveraging a fine-tuned vision-language framework to fully exploit the complementary information between visual and textual modalities. Recognizing that the default visual encoder of existing vision-language models is not tailored for AI-generated image detection, we redesign a visual encoder to better capture both the low-level and high-level artifacts inherent in AI-generated images. Furthermore, we incorporate a semantic-level textual branch to enable multi-modal feature fusion and detection. Consequently, LHSDet employs a triple-branch architecture to extract complementary multi-modal features: a low-level visual branch that aggregates non-overlapping patches for local texture cues, a high-level visual branch based on SigLIP2 for global perception feature extraction, and a semantic-level textual branch that generates captions using BLIP-2. Extensive experimental results demonstrate that LHSDet achieves high detection accuracy and robust performance across diverse generative models, including both diffusion and autoregressive models.

---


### 79. [Back to the Future: A workbook time machine for spread sheet creation benchmarks](https://arxiv.org/abs/2608.07873)

**<font color=#1a73e8>作者：</font>** Mansi Uniyal, Agamdeep Singh, Ananya Singha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the workbook time machine, a pipeline that automatically creates benchmarks evaluating the ability of language models to create derived objects in spreadsheets (formulas, charts, pivot tables, and conditional formatting). Applied to public workbook corpora, it produces wtmcorpus--a collection of (input workbook, output workbook, query) triples spanning four artifact types and varying complexity. From this corpus we curate wtmbench, a 150-task evaluation benchmark with queries at three levels of specificity. We evaluate existing spreadsheet manipulation agents and baselines on wtmbench across artifact types, step complexity, and instruction granularity. Our evaluations show that query specificity, agent orchestration, and interface API used to control spreadsheets play a big role in LLM performance on Excel tasks.

---


### 80. [GRACE: LLM-Grounded Semantic Metric Spaces for Scalable Mixed-Data Clustering](https://arxiv.org/abs/2608.07881)

**<font color=#1a73e8>作者：</font>** Zihua Yang, Zhencheng Xie, Junyang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clustering mixed tabular data requires a unified metric space to bridge the inherent heterogeneity between continuous numerical measurements and discrete categorical symbols. Traditionally, algorithms rely entirely on dataset-internal statistics to estimate categorical relationships, which confines the learned metric to empirical co-occurrences and ignores conceptually obvious yet statistically unobserved affinities. Although LLMs offer external world knowledge, applying their text-centric reasoning to highly abstract tabular concepts presents significant challenges. Bridging this modality gap to construct a semantically complete metric typically requires embedding LLMs into iterative metric learning loops to dynamically optimize cross-modality representations. This incurs intractable computational overhead, forcing a compromise between semantic enrichment and scalability. Therefore, we propose GRACE, an LLM-grounded framework for scalable mixed-data clustering. GRACE shifts semantic acquisition to the attribute-value level via a multi-perspective LLM querying strategy, mapping heterogeneous values into knowledge-informed descriptions. Crucially, this one-shot grounding extracts general-purpose semantic representations that embed heterogeneous attributes into a unified space, decoupling expensive LLM invocation from iterative optimization. Furthermore, GRACE cross-validates these external semantics against dataset-internal statistical evidence to ensure alignment with the dataset-specific cluster structure. Ultimately, GRACE matches the scalability of conventional statistics-driven baselines while achieving superior clustering accuracy and conceptual interpretability over 11 competing methods. The source code is available at this https URL

---


### 81. [Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills](https://arxiv.org/abs/2608.07885)

**<font color=#1a73e8>作者：</font>** Agamdeep Singh, Srishti Gautam, Priyanshu Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning modes of language models outperform their non-reasoning counterparts on multi-step agentic tasks, but pay a 3-6x premium in output tokens on every episode -- much of it spent re-deriving procedures that are shared across episodes of the same domain. We show this recurring cost can be amortized: a coding agent analyses a small corpus of existing trajectories from a training split and compiles a compact natural-language skill that is injected into the non-reasoning model's system prompt. Across four agentic benchmarks (ALFWorld, tau$^2$-bench telecom and retail, and SpreadsheetBench-Verified), skills recover 55%-100%+ of the reasoning gap for GPT-5.4-mini on held-out tasks -- exceeding the reasoning mode outright on two of four -- while emitting 2.7-6x fewer output tokens and zero reasoning tokens. Notably, reasoning traces are not a prerequisite: skills distilled from non-reasoning trajectories alone remain competitive with skills distilled from paired reasoning/non-reasoning corpora, with domain-dependent differences between the two sources. We interpret these results through a search lens: test-time reasoning is deep search inside a single episode, re-paid at every deployment, while corpus distillation is wide search across episodes, paid once. The two recover overlapping procedural knowledge, and width over cheap trajectories is often the better buy -- with the residual gap on some domains (telecom, SpreadsheetBench) delineating where genuinely per-instance deep search remains necessary.

---


### 82. [Vision-Language Grounding as Bidirectional Concept Correspondence](https://arxiv.org/abs/2608.07886)

**<font color=#1a73e8>作者：</font>** Jieyu Zhang, Ziqi Gao, Luke Zettlemoyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language grounding connects language to visual content, yet most existing formulations reduce grounding to a unidirectional localization problem: given a prespecified text phrase or category name, identify the corresponding image region. This setup assumes that the relevant linguistic unit is already known, overlooking a more basic challenge in grounded communication: determining which parts of the text are visually referential and how they correspond to entities in the image. We formulate grounding as $\textit{bidirectional concept correspondence}$ over an image-text pair. Given an image and its paired text, the goal is to recover all correspondences between visually referential text spans and instance-level image segments, without assuming that the relevant text spans are provided. This formulation unifies common grounding tasks, including phrase grounding, referring expression grounding, and open-vocabulary detection, by treating text segmentation, image segmentation, and cross-modal alignment as a single correspondence prediction problem. To address this task, we introduce $\textbf{ConCor-1}$, a grounding model built on top of a pretrained vision-language model. It uses learnable $\textit{bridge tokens}$ to represent candidate image-text correspondences and predicts, for each token, a text mask, an image mask, and a correspondence presence score. To train and evaluate this task, we convert diverse grounding and segmentation datasets into a unified correspondence format. Experiments show that $\textbf{ConCor-1}$ consistently outperforms baselines, improving correspondence F1 by 48% on the long-caption dataset and by 29% on zero-shot LVIS, where the large category list serves as the text input.

---


### 83. [Router Sensitivity Under Lightweight Fine-Tuning Identifies Prunable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2608.07890)

**<font color=#1a73e8>作者：</font>** Ali Janati, Kaoutar El Maghraoui, Xinyi Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models decouple total parameters from per-token compute, but deployment still requires storing every expert. Recent theory shows that pruning experts with the smallest router-norm changes during fine-tuning can preserve accuracy, but assumes full fine-tuning. We test whether lightweight adaptation can recover this signal. We briefly fine-tune with a parameter-efficient adapter, rank experts by the induced $\ell_2$ router change, and prune the least-changed experts in one shot. On Mixtral-8$\times$7B-Instruct (44.83% MMLU-Pro), router-only LoRA trains 0.002% of parameters and outperforms all-module LoRA at matched rank with half the experts removed (27.54% vs. 24.42%); signal quality declines as adaptation spreads to attention and expert weights. Accuracy improves monotonically with LoRA rank, reaching 28.76%. IA3, which leaves router weights frozen, matches direct router adaptation, whereas unconstrained additive adapters degrade the signal. Router-guided MMLU-Pro accuracy decays quasi-linearly rather than collapsing, remains nearly 1.8 times that of magnitude-based or random pruning at maximal compression, and reduces memory by 49% and per-token latency by 37%. At 25% compression, retention is competitive with methods using full activation statistics. The criterion also transfers to Qwen1.5-MoE fine-tuned for mathematics, retaining 49.7% mean accuracy over eleven benchmarks with half the experts removed while random pruning falls to single digits. Router sensitivity under lightweight fine-tuning therefore makes provably motivated expert pruning practical at scale.

---


### 84. [LLM-Based Embeddings for Program Analysis and Optimization](https://arxiv.org/abs/2608.07894)

**<font color=#1a73e8>作者：</font>** Calvin Higgins, Marco Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances have highlighted the potential of machine learning, particularly Large Language Models (LLMs), for analyzing and optimizing programs. We present the first application of program embeddings from LLMCompiler---an LLM massively pretrained on intermediate representation (IR) code---to representative program analysis and optimization tasks. We generate program embeddings directly from source and IR code using a simple approach: split programs into chunks, independently embed each chunk with pretrained LLMs, and then aggregate the chunk embeddings into a single program embedding. Our experiments show that combining source and IR code embeddings achieves an error rate of 1.54\% in algorithm classification, a 12\% improvement over the current state-of-the-art, and a competitive accuracy on heterogeneous device mapping. These findings suggest that training a performance-aware LLM for embedding IR code might yield state-of-the-art results in code optimization tasks.

---


### 85. [TelemetrySuffBench: Is Agent Telemetry Sufficient for Failure-Origin Diagnosis?](https://arxiv.org/abs/2608.07899)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhu, Peng Pu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems increasingly expose execution traces, yet telemetry that reveals a failure may still be inadequate for identifying where that failure originated. We introduce TelemetrySuffBench, a controlled benchmark that separates failure detection, fault-origin localization, and safe abstention under insufficient evidence. The benchmark constructs canonical multi-component traces with delayed-binding faults and renders them as paired coarse views, seven-factor telemetry masks, and exact-equal ambiguous origin pairs. We evaluate five frontier language models using unified protocols, explicit candidate sets, invalid-output accounting, subgroup analyses, and a frozen blind holdout. With full telemetry, origin-step Top-1 accuracy ranges from 33.8% to 97.2% across models. Metadata, OpenTelemetry-compatible, and OpenInference-compatible views retain 99.5% to 100% detection F1 while limiting origin-step accuracy to at most 0.5%, exposing a robust detection-localization gap. Factor ablations further show that removing decision content reduces origin-step accuracy to zero for every model, while provenance removal also causes large model-dependent losses. On rich ambiguous inputs that require abstention, evidence gating reduces unsupported unique-origin answers by 12.5 to 48.6 percentage points for three models, whereas two models still answer every case, revealing strong model dependence in safe abstention. Results on the frozen holdout reproduce the central pattern within the same generator family. These findings show that terminal status can support detection, whereas reliable causal attribution requires explicit decision-to-provenance links and abstention safeguards that remain effective across models. The dataset and benchmark implementation are available at this https URL.

---


### 86. [GraphThink: Graph-Enhanced LLM Thinking for Long-Horizon Embodied Task Planning](https://arxiv.org/abs/2608.07905)

**<font color=#1a73e8>作者：</font>** Chen Li, Sijie Cheng, Yuelin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents using LLM-based planners often struggle with physical hallucinations, poor generalization to long-horizon tasks, and lack of environmental awareness. We propose GraphThink, a novel framework that integrates a task graph to provide structured knowledge for robust planning and a scene graph to maintain environmental memory for event-driven replanning. Specifically, the task graph guides LLM thinking through contextual prompting and iterative refinement, effectively mitigating planning hallucinations. Furthermore, within the GRPO framework, the task graph offers delicate reward design to train the LLM planner, enhancing long-horizon planning capabilities and improving generalization. Finally, an event-driven replanning module, powered by the scene graph, enables closed-loop environment awareness and error correction. GraphThink achieves state-of-the-art performance on the ALFRED benchmark. In particular, our high-level planner surpasses leading API-based LLMs on both the validation set and held-out long-horizon tasks, underscoring its robust zero-shot and few-shot capabilities. Additional evaluations further demonstrate strong out-of-distribution generalization to novel tasks and environments.

---


### 87. [When Does Trace-Driven Evaluation Mislead MoE Expert Caching? Replay Semantics, Workload Contamination, and Operating Regimes](https://arxiv.org/abs/2608.07911)

**<font color=#1a73e8>作者：</font>** Yu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have outgrown accelerator memory, and offloading expert weights to host memory is now standard. This makes expert cache management an attractive lever: a policy that raised the hit rate would cut expert traffic per token. Evaluating that is a measurement problem, and we find the measurement fragile.
With a trace-driven, event-atomic simulator over three MoE models (40, 64, 128 experts), we isolate three evaluation axes that change conclusions, not just numbers. Replay semantics: under a fused-event traffic contract, an inconsistent per-access replay inflates recency-based policies by 27-29% while leaving frequency-based and static ones within 4%, inverting the policy ranking. Workload contamination: probe sets using one instruction template per category produce verbatim-identical generation prefixes; a matched-pair rendering intervention moves the measured early-window effect by 19.4-31.9 points and reverses which workloads look most cache-friendly. Operating regimes: normalized miss fractions do not transfer across models, so the per-step expert union relative to per-layer capacity must be reported -- yet permuting only the temporal order of an identical event stream moves the offline-optimal gap from 44.9% to 30.8%, so it is not sufficient.
Corrected, a stable gap to the offline optimum remains (44.2-45.9% over 13 frozen workload compositions). A forced-admission oracle attributes 84.3-96.6% of it to knowing which resident expert is used furthest in the future. A causal next-use predictor, used as an eviction rule, recovers -11.4% of the gap; it picks an optimal victim 3.4% of the time, against 2.4% for a random resident block and 20.6-22.1% for LRU and LFRU. Our position is narrow: in our evaluated settings a large offline-optimal gap substantially overstates the gains recovered by representative lightweight causal mechanisms.

---


### 88. [Private Anytime Selective-Risk Certification for Federated Retrieval-Augmented Generation: Guarantees and Empirical Limits](https://arxiv.org/abs/2608.07913)

**<font color=#1a73e8>作者：</font>** Sanjeda Akter, Ibne Farabi Shihab, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Selective-risk certificates promise that accepted outputs meet a declared error target. We develop Fed-SRC, a score-agnostic certificate for federated, differentially private, adaptively monitored retrieval-augmented generation. Clients release only Gaussian-perturbed score and loss histograms. Record-indexed and noise-variance-indexed martingales jointly bound target-risk contrast and accepted mass over all registered thresholds and rounds, permitting predictable recruitment, dropout, threshold selection, and optional stopping. A range-one total-variation term transfers the calibration mixture to a declared deployment mixture. The contribution is this private, federated, anytime combination, rather than the contrast statistic or acceptance floor individually. Empirically, no simultaneous-bound violation occurs in any evaluated cell, privacy level, or policy. Operational power depends on the score and population: the primary target r*=0.10 never certifies, and on RAGTruth the secondary target r*=0.20 never certifies either, whereas on HaluEval question answering it certifies in all 200 non-private trials, with held-out risk below the target. Naively privatized non-private certificates violate their bounds in 146 to 198 of 200 trials. As an exploratory comparison, we also evaluate a private betting-capital heuristic for which we do not establish e-process validity. This heuristic stops certifying at epsilon <= 4, where Fed-SRC still certifies. Certification nevertheless consumes roughly 30 times more stream events than unique calibration items.

---


### 89. [When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits](https://arxiv.org/abs/2608.07914)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral contamination detectors can return "no evidence" either because a benchmark is clean or because the audit has little power. We formalize this distinction for a benchmark in which an unknown fraction alpha of items was seen during training. With matched clean and seen controls, the behavioral channel is the sparse mixture Q_alpha = (1 - alpha) P_0 + alpha P_1, and an exact second-moment argument shows that detectability is governed by alpha * rho * sqrt(m), where rho^2 = chi^2(P_1 || P_0) measures behavioral separability. Any scalar detector reduces to its efficacy, ef = |E_1 f - E_0 f| / sqrt(Var_0(f)) <= rho, which can be estimated from controls before the audit is run. A separate sample-split certificate lower-bounds alpha distribution-free, without requiring an orientation assumption. Our empirical finding is two-sided. Frozen calibration efficacy predicts held-out power curves, with R^2 = 0.83-0.98 across six exact-permutation channels, but the efficacy-only Gaussian budget is miscalibrated at the small sample sizes it prescribes, failing in 9/9 gate-passing channels even though efficacy itself transports. The failure is in the inversion, not the calibration. A predeclared two-stage planner that simulates the deployed test repairs the budgets, is uniformly conservative, and abstains when its probe does not transport. The certificate is valid but vacuous at audit scale, and a five-seed paired injection study recovers the mechanism ordering verbatim > paraphrase > surface, in which the apparent answer-only signal is explained by baseline drift. We report the audit contract and its failures together: a non-rejection is interpretable only alongside the efficacy, budget, and validity gates that produced it.

---


### 90. [SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding](https://arxiv.org/abs/2608.07915)

**<font color=#1a73e8>作者：</font>** Jiamu Zhang, Liang Wu, Kelly Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly read long inputs in the agentic era, from whole documents and codebases to conversations across many turns. Their inference memory is then dominated by the key-value (KV) cache, the stored attention keys and values of every token the model has read and generated. Because the cache grows with context length and is re-read in full at every generated token, a longer context means more GPU memory.
To reduce this cost, most existing methods compress the KV cache by lowering every stored value to the same low precision, a technique known as quantization. They can push this to nearly two bits per value, but rarely further, because quality drops sharply at this 2-bit cliff: four levels are too few for the cache's outlier-heavy values, where a few large entries consume the levels and collapse the rest into noise. A natural remedy is to spend more bits on the channels (feature dimensions) that matter and fewer on the rest, but the raw cache offers no handle: its channels are strongly correlated, so none stands out as more important.
Our analysis shows that this handle appears once the cache is rotated into a coordinate system computed from its own statistics, removing these correlations. There, a small fraction of channels carries almost all the information, and spending the budget on those few is far more accurate than spreading it evenly.
Guided by this analysis, we develop SPECTRA, a training-free, drop-in codec that re-encodes the cache into this coordinate system and concentrates the bit budget on the channels that carry the signal. On Llama-3.1-8B and Qwen2.5-7B over long-context benchmarks, SPECTRA is near-lossless at 4x compression, competitive at 8x where uniform quantization has collapsed, and reaches up to 12x, pushing usable compression past the 2-bit cliff so the same GPU holds longer contexts and larger batches.

---


### 91. [TongGuOCR: A Layout-Aware and Token-Augmented OCR Framework for Chinese Historical Documents](https://arxiv.org/abs/2608.07917)

**<font color=#1a73e8>作者：</font>** Zhongheng Zhou, Yi Sun, Huiguo He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chinese historical documents preserve valuable cultural heritage, but many collections remain accessible only as scanned page images, preventing full-text retrieval, collation, and computational analysis. Optical character recognition (OCR) can bridge this gap, but accurate transcription remains challenging because historical documents often contain complex layouts, rare characters, and nontrivial reading orders. We propose TongGuOCR, a layout-aware and token-augmented OCR framework for Chinese historical documents. First, a Layout-Aware Preprocessing module constructs and refines locally coherent recognition blocks to preserve local context while reducing interference across regions. Second, a Token-Augmented Recognition module augments the transcription target at two complementary levels: character-level vocabulary expansion gives each rare glyph a direct one-token representation and shortens its decoding path, while line-to-line transition modeling injects discrete spatial displacement tokens that guide the decoder along complex reading paths without requiring precise coordinates. Experiments on two Chinese historical document OCR benchmarks show that TongGuOCR outperforms representative traditional task-specific OCR models, general-purpose multimodal large language models (MLLMs), and OCR-oriented MLLMs. On the more challenging M5HisDoc benchmark, TongGuOCR achieves 93.76 AR and reduces NED from 10.43 to 6.15 and RO-ED from 7.53 to 3.49 relative to the best competing score for each metric. An online demo is available at this https URL.

---


### 92. [Forged Peer Judgments Mislead Multimodal LLM Judge Panels: Source-Blind Anchoring and Panel-Consensus Verification](https://arxiv.org/abs/2608.07920)

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLM judge panels can cross-reference peers, but a quoted peer judgment may itself be untrusted. We expose source-blind anchoring as a text-level attack surface in vision-language model (VLM) panels. Quoting independent visual judgments creates large anchoring gaps (19--26 percentage points) under both self and peer framing. A matched-content, label-only control changes the broken rate by only $-0.17$pp (95\% CI $[-0.68,0.35]$), showing that the self/peer label itself does not explain the effect. Under our tested construction, deliberately generated, concise wrong quotes overturn originally-correct verdicts 1.5--2.7$\times$ more often than naturally occurring wrong peer statements, with bootstrap 95\% CIs excluding parity across two datasets and seven VLM judges. Because the two statement populations differ in selection and form, this ratio measures differential damage under the tested attack rather than a provenance-only causal effect. We then introduce panel-consensus verification, which cross-checks a quote against independently collected blind votes. It blocks 84.9\% of fabricated attacks, cuts their net harm by 97.5\%, and preserves the positive but statistically inconclusive point estimate for genuine peer information under leave-one-out re-verification. These results identify a low-cost attack surface and a concrete defense for safer multimodal collaborative evaluation.

---


### 93. [Spectral Outliers Reveal Dominant Learned Structure in Transformer Attention](https://arxiv.org/abs/2608.07921)

**<font color=#1a73e8>作者：</font>** Kasun Dewage, Marianna Pensky, Suranadi De Silva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We apply Marchenko-Pastur (MP) random matrix theory to pre-trained attention weights in order to separate each projection matrix into a random-like bulk and a set of spectral outliers. We validate this decomposition causally: zeroing the MP-identified outliers (signal) in Mistral-7B drives HellaSwag, MMLU, and PIQA close to random-chance performance, whereas zeroing a count-matched subset of bulk singular values causes smaller but non-negligible degradation. Across 11 pre-trained transformers we identify five recurring patterns: spectral outliers encode a dominant component of the learned structure; Q projections carry the most outliers; V projections under grouped-query attention lack a clean signal/noise separation; entry-level outliers form structured row-bands in Q and column-bands in O; and specific residual-stream dimensions persist as band outliers across layers in K and O. We close by outlining how these observations could inform parameter-efficient fine-tuning and structured pruning.

---


### 94. [ZhuLong: Execution-Grounded LLM Agent for EDA Scripting with Offline API Self-Exploration](https://arxiv.org/abs/2608.07925)

**<font color=#1a73e8>作者：</font>** Yang Liu, Shiwei Hou, Xiyuan Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EDA scripting with tool-specific, often undocumented APIs remains a long-tail bottleneck that existing LLMs fail to address. This paper presents ZhuLong, an execution-grounded LLM coding agent for PyAether and SKILL that combines API retrieval, documentation inspection, and sandbox execution via unified MCP tools, augmented by an offline API self-exploration mechanism that infers undocumented API behaviors through counterfactual experimentation.
We evaluate ZhuLong on EDA-Eval-PyAether, a benchmark of 158 real-world tasks with assertion-based execution, where the complete system achieves 78.5% Pass@1 in the commercial Empyrean Aether environment, substantially outperforming a pure LLM baseline (23.6%). Ablation studies identify sandbox execution as the dominant performance driver (41.2 pp drop when removed), with the self-exploration mechanism contributing an additional 3.2 pp accuracy gain and a 22.1% reduction in per-task tool calls. On 20 interactive tasks involving unsaved layouts and schematics, ZhuLong achieves 60.0% Pass@1 for PyAether and 50.0% for SKILL.

---


### 95. [SportsGrounder: Proposal-Aided Interleaved Grounding for Dense Sports Video Reasoning](https://arxiv.org/abs/2608.07932)

**<font color=#1a73e8>作者：</font>** Yizhi Li, Jiawei Jiang, Guanhong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sports video analysis is crucial for athletic analytics and broadcasting enhancement. Dense sports video reasoning, however, demands a fine-grained understanding of numerous small-scale, highly interactive, and visually homogeneous entities (e.g., players sharing identical uniforms, the ball) across long temporal contexts. Current Large Multimodal Models (LMMs) inherently struggle with such dense visual complexities. Due to the lack of fine-grained visual details, these models often over-rely on textual priors to guess answers, especially when distinguishing visually similar actions and players. To address this, we propose \textbf{SportsGrounder}, a framework that leverages an open-vocabulary visual expert to aid interleaved grounding specifically for dense sports video reasoning. To achieve precise spatial localization, we extract domain-guided object proposals and introduce an Interleaved Grounding Fusion (IGF) mechanism. The IGF frame-by-frame integrates explicit bounding box coordinates and implicit visual semantics with global grid features. This design preserves strict temporal alignment and prevents sequence length explosion. Furthermore, we design an Action-Aware Supervision (AAS) module that directly regularizes the model's hidden states, forcing the network to learn accurate motion representations rather than relying on language bias. Optimized with Mixed Preference Optimization (MPO) to better distinguish deceptive distractors, our extensive experiments on newly curated dense sports VQA datasets (derived from SoccerNet and FineSports) demonstrate that SportsGrounder significantly improves fine-grained reasoning and achieves state-of-the-art accuracy.

---


### 96. [EvoTrustRAG: Evolution-Aware Conflict Attribution and Evidence Handling for Reliable Retrieval-Augmented Generation](https://arxiv.org/abs/2608.07933)

**<font color=#1a73e8>作者：</font>** Xi Nie, Hongwei Li, Shenghao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves the factuality of large language models with external knowledge, yet conflicting evidence remains a fundamental challenge in dynamic and adversarial environments. Existing approaches often treat conflicts as static inconsistencies and select more reliable knowledge, overlooking that the same conflict may arise from legitimate knowledge evolution, malicious manipulation, or unresolved uncertainty. We formulate conflict origin attribution as a new problem in RAG: identifying which explanation of conflicting evidence is supported by observable context rather than simply which fact should be trusted. We propose EvoTrustRAG, a training-free framework for evolution-aware conflict attribution and evidence handling before answer generation. EvoTrustRAG represents span-grounded retrieved facts as a conflict evidence graph, evaluates grounded evolution and directional intervention hypotheses using temporal relations, support structure, and auxiliary consistency, and projects local decisions onto a globally consistent explanation of each conflict group. The attribution determines whether earlier and later states are preserved as temporal knowledge, an intervention candidate is separated from the primary context, or an unresolved conflict remains visible to the generator. Unlike provenance-based approaches focused on post-hoc analysis, EvoTrustRAG determines during inference whether conflicting evidence follows plausible knowledge evolution, exhibits intervention-like support, or cannot be reliably attributed. Experiments show that EvoTrustRAG achieves 81.4% average accuracy on benchmark-native conflict settings, improves attribution macro-F1 from 72.2% to 79.1% over the strongest baseline, and reduces the error rate under the strongest coordinated attack from 31.2% to 16.0%.

---


### 97. [Adaptive Supervised Anchoring for On-Policy Self-Distillation](https://arxiv.org/abs/2608.07935)

**<font color=#1a73e8>作者：</font>** Meilin Yang, Zixuan Ding, Jianhao Nie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) adapts a language model by distilling guidance from a frozen teacher on trajectories sampled from the student. Its effectiveness, however, depends critically on the quality of those trajectories. We show that when student rollouts drift from target trajectories, conditioning the teacher on off-target prefixes substantially weakens its task-relevant supervision. Controlled prefix-corruption experiments expose this failure mode, which we term rollout-conditioned signal degradation. To address this problem, we propose a unified training framework that separates two complementary supervision pathways. The first retains rollout-conditioned distribution matching, providing guidance on states the student actually visits. The second applies supervised cross-entropy on canonical ground-truth contexts, avoiding the incompatibility of imposing target tokens on erroneous rollout prefixes. Token-level rollout-target alignment is used to adapt the strength of the canonical-context anchor, emphasizing it during cold start and relaxing it as rollout quality improves. Experiments across multiple model scales, two task families, and general-reasoning benchmarks show that the proposed approach improves task acquisition over OPSD while preserving general capabilities, resulting in a more favorable empirical plasticity-stability trade-off. These findings identify context quality as a central bottleneck in on-policy self-distillation and demonstrate the value of separating rollout-conditioned guidance from canonical supervision.

---


### 98. [LAD-COD: Language-Aligned Dense Perception for Camouflaged Object Detection](https://arxiv.org/abs/2608.07941)

**<font color=#1a73e8>作者：</font>** Shangye Song, Tianzhi Zhu, Syed Ariff Syed Hesham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection (COD) aims to segment objects that exhibit high visual similarity to their surroundings, which reduces foreground-background discriminability and weakens boundary evidence across appearance, texture, and structure. Such limitations motivate the use of instruction-conditioned semantics as top-down guidance for identifying which weak visual cues are relevant to the target. Recent segmentation systems built on large multimodal models (LMMs) demonstrate this possibility through instruction-conditioned target embeddings that guide mask decoding. However, in this language-to-mask paradigm, the generated target embedding conditions mainly the mask decoder, leaving the dense visual features that must preserve low-contrast boundaries and fine local structure without explicit guidance. We propose Language-Aligned Dense perception for COD (LAD-COD), a framework that aligns top-down semantic target guidance with bottom-up hierarchical visual features. Instead of fully adapting a large generic image encoder, LAD-COD learns a trainable hierarchical visual branch that captures camouflage-sensitive texture, boundary, and contextual information. To align these features with the target embedding, LAD-COD applies Language-Aligned Dual Visual Fusion (LADVF), which extends the embedding beyond sparse prompting to query patch-level language-aligned features and to gate their residual integration with the hierarchical features. This design allows semantic information to guide localization while preserving the fine structural details needed for camouflage segmentation. Experiments on CAMO, COD10K, and NC4K show that LAD-COD obtains the best reported value in all 12 dataset-metric comparisons.

---


### 99. [Directed Neuro-Symbolic Stochastic Execution for Verification of Distributed Parallel AI Programs](https://arxiv.org/abs/2608.07947)

**<font color=#1a73e8>作者：</font>** Gautham Koorma, Vikas Sharma, George Edwards 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed parallel Artificial Intelligence (AI) programs expose reliability gaps that conventional testing cannot close: parallel executions are non-deterministic, and AI workloads bring high-dimensional inputs and non-linear operations that defeat fuzzing and symbolic execution in isolation. We present Directed Neuro-Symbolic Stochastic Execution (DNSSE), a hybrid testing framework that couples schedule prediction guided by a Large Language Model (LLM) with symbolic constraint solving and coverage-guided stochastic mutation. We model distributed AI executions as non-deterministic transition systems, specify correctness in linear temporal logic, and prove soundness, bounded completeness, and probabilistic completeness of the hybrid solver, together with an expected-cost analysis of LLM-guided schedule exploration. A scalable implementation on PyTorch and Ray detects 2.9% more concurrency bugs than the strongest baseline and raises average branch coverage from 68.6 % to 91.6 % across five realistic distributed AI benchmarks.

---


### 100. [Persistent Semantic Entities in Tool-Augmented LLM Systems](https://arxiv.org/abs/2608.07952)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents can harbor implicit state that persists across sessions, activates through events, and propagates across agent boundaries---largely invisible to standard debugging. We formalize this as Persistent Semantic Entities (PSEs): constructs defined by name binding, event triggering, and cross-boundary propagation, and evaluate them across 24 models from 11 families (1.5B--1T parameters). First, every tested model is susceptible (20--100% on the 20-model susceptibility panel), with name binding as the necessary and dominant mechanism: without it, contamination is 0%. Second, persistence depends on contamination type rather than scale or deployment: preference contamination persists undecayed on every model probed (100% at t=10) and instruction contamination persists wherever adopted, persona-style injection decays partially (90%$\to$10%), while factual injection is model-dependent---self-corrected on Llama-3.1-8B and GPT-4o-mini but held at ceiling on both Qwen2.5-coder variants, so we do not claim it self-corrects in general. The preference and instruction results hold across providers in our controlled setting. Third, context-isolated self-verification achieves 20--79% reduction (median 36.5%) without oracle references while keyword-based detection produces systematic false positives, and contamination compounds 1.9$\times$ along a four-stage agent pipeline (40%$\to$75%). Preference and instruction contamination---persistent, lacking self-correction, and poorly captured by standard monitoring---represent a particularly concerning attack surface for deployed agent systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
